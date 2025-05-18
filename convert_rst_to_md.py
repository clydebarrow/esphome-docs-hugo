#!/usr/bin/env python3
"""
Convert Sphinx RST files to Hugo Markdown format.
This script helps migrate the ESPHome documentation from Sphinx to Hugo.
"""

import os
import re
import sys
import argparse
import shutil
import glob
import textwrap
from collections import defaultdict

# Global anchor map to store all anchors and their document paths
anchor_map = {}

def build_anchor_map(input_dir):
    """Scan all RST files and build a map of anchors to their document paths."""
    print("Building anchor map...")
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.rst'):
                rst_file = os.path.join(root, file)
                rel_path = os.path.relpath(rst_file, input_dir)
                doc_path = os.path.splitext(rel_path)[0]
                
                # Convert to Hugo path format
                doc_path = doc_path.lower()
                
                # Handle index files
                if os.path.basename(doc_path) == 'index':
                    doc_path = os.path.dirname(doc_path) + '/_index'
                
                with open(rst_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find all anchor definitions (.. _anchor:)
                for match in re.finditer(r'^.. _([^:]+):$', content, re.MULTILINE):
                    anchor_name = match.group(1).strip()
                    anchor_map[anchor_name] = doc_path
    
    print(f"Found {len(anchor_map)} anchors across all documents")

def convert_rst_to_md(rst_content, filename):
    """Convert RST content to Markdown using line-by-line processing."""
    lines = rst_content.split('\n')
    
    # Extract title and SEO data
    title = ""
    explicit_title = ""
    seo = {}
    
    # Check for explicit title directive
    for i, line in enumerate(lines):
        if line.startswith('.. title::'):
            explicit_title = line.replace('.. title::', '').strip()
            break
    
    # Find title (first line with underline of = characters)
    for i in range(len(lines) - 1):
        if re.match(r'^=+$', lines[i + 1]) and lines[i]:
            title = lines[i]
            break
    
    # Use explicit title if available, otherwise use the heading title
    if explicit_title:
        title = explicit_title
    
    # Extract SEO data
    in_seo = False
    seo_lines = []
    seo_start = -1
    seo_end = -1
    
    for i, line in enumerate(lines):
        if line.startswith('.. seo::'):
            in_seo = True
            seo_start = i
            continue
        
        if in_seo:
            if line.strip() and line.startswith('    '):
                seo_lines.append(line.strip())
            elif line.strip() == '':
                continue
            else:
                in_seo = False
                seo_end = i
                break
    
    # Parse SEO data
    for line in seo_lines:
        if ':' in line:
            key, value = line.split(':', 1)
            seo[key.strip()] = value.strip()
    
    # Process lines
    md_lines = []
    i = 0
    
    # Skip SEO block
    if seo_start != -1 and seo_end != -1:
        i = seo_end
    
    while i < len(lines):
        line = lines[i]
        
        # Skip title directive
        if line.startswith('.. title::'):
            i += 1
            continue
        
        # Skip title (we'll add it later with frontmatter)
        if line == title and i + 1 < len(lines) and re.match(r'^=+$', lines[i + 1]):
            i += 2
            continue
        
        # Handle RST anchors (.. _anchor:)
        if re.match(r'^.. _[^:]+:$', line):
            anchor_name = line.strip()[4:-1]  # Remove '.. _' and ':' from the line
            # Don't replace the anchor
            #md_lines.append(f'<a id="{anchor_name}"></a>')
            i += 1
            continue

        # Handle list-table directive
        if line.strip().startswith('.. list-table::') or line.strip().startswith('..  list-table::'):
            table_lines, new_i = process_list_table(lines, i)
            md_lines.extend(table_lines)
            i = new_i
            continue
        
        # Handle headers
        if i + 1 < len(lines) and re.match(r'^=+$', lines[i + 1]) and line:
            md_lines.append(f"# {line}")
            i += 2
            continue
        
        if i + 1 < len(lines) and re.match(r'^-+$', lines[i + 1]) and line:
            md_lines.append(f"## {line}")
            i += 2
            continue
        
        # Handle code blocks - check for both standalone and nested code blocks
        if line.lstrip().startswith('.. code-block::'):
            # Get the indentation of the current line
            current_indent = len(line) - len(line.lstrip())
            
            # Extract language
            language = line.lstrip().replace('.. code-block::', '').strip()
            
            # Add the code block start with proper indentation
            md_lines.append(' ' * current_indent + f"```{language}")
            
            # Skip the blank line after the code-block directive
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            
            # Determine the indentation level of the code block content
            code_indent = 0
            if i < len(lines) and lines[i].startswith(' '):
                code_indent = len(lines[i]) - len(lines[i].lstrip(' '))
            
            # Add code content
            while i < len(lines):
                if not lines[i].strip():  # Empty line
                    md_lines.append('')
                    i += 1
                elif lines[i].startswith(' ' * code_indent):  # Line with correct indentation
                    # Remove only the code block indentation, preserve any existing indentation
                    md_lines.append(' ' * current_indent + lines[i][code_indent:])
                    i += 1
                else:  # Line without expected indentation - end of code block
                    break
            
            # Add the code block end with proper indentation
            md_lines.append(' ' * current_indent + "```")
            continue
        
        # Handle notes
        if line.startswith('.. note::'):
            md_lines.append("{{< note >}}")
            
            # Skip the blank line
            i += 2
            
            # Add note content
            while i < len(lines) and (lines[i].startswith('    ') or not lines[i].strip()):
                if lines[i].startswith('    '):
                    md_lines.append(lines[i][4:])
                else:
                    md_lines.append('')
                i += 1
            
            md_lines.append("{{< /note >}}")
            continue
        
        # Handle warnings
        if line.startswith('.. warning::'):
            md_lines.append("{{< warning >}}")
            
            # Skip the blank line
            i += 2
            
            # Add warning content
            while i < len(lines) and (lines[i].startswith('    ') or not lines[i].strip()):
                if lines[i].startswith('    '):
                    md_lines.append(lines[i][4:])
                else:
                    md_lines.append('')
                i += 1
            
            md_lines.append("{{< /warning >}}")
            continue
        
        # Handle figures
        if line.strip().startswith('.. figure::'):
            image_path = line.replace('.. figure::', '').strip()
            
            # Adjust image path for component files
            if '/components/' in filename:
                # Convert absolute path to relative
                image_path = image_path.replace('/components/', '../')
            elif image_path.startswith('images/'):
                # Add parent directory prefix
                image_path = '../' + image_path
            
            # Skip options
            i += 1
            while i < len(lines) and (not lines[i].strip() or lines[i].strip().startswith(':')):
                i += 1
            
            # Get caption if present
            caption = ""
            if i < len(lines) and lines[i].strip():
                caption = lines[i].strip()
                i += 1
            
            # Add the image with caption if present
            if caption:
                md_lines.append(f"![{caption}]({image_path})")
                md_lines.append(f"*{caption}*")
                md_lines.append("")
            else:
                md_lines.append(f"![Image]({image_path})")
                md_lines.append("")
            
            continue
        
        # Skip toctree
        if line.startswith('.. toctree::'):
            i += 1
            while i < len(lines) and (lines[i].startswith('    ') or not lines[i].strip()):
                i += 1
            continue
        
        # Process the line for inline markup
        processed_line = process_inline_markup(line)
        if ":ghedit:" in processed_line:
            processed_line = re.sub(r':ghedit:`([^`]+)`',
                                    lambda m: f"[Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/{filename.replace('.rst', '.md')})",
                                    processed_line)


    # Fix image paths in markdown content
        if '/components/' in filename and '![' in processed_line and '](/components/' in processed_line:
            processed_line = processed_line.replace('](/components/', '](../')
        elif '/components/' in filename and '![' in processed_line and '](images/' in processed_line:
            processed_line = processed_line.replace('](images/', '](../images/')
        
        # Fix SVG image paths in markdown content
        if '![' in processed_line and '](_build/_images/' in processed_line and '.svg)' in processed_line:
            processed_line = processed_line.replace('](_build/_images/', '](/images/_build/_images/')
        
        # Add the processed line
        md_lines.append(processed_line)
        i += 1
    
    # Generate frontmatter
    frontmatter = []
    frontmatter.append('---')
    
    # Use description from SEO if available, otherwise use title
    description = seo.get('description', title)
    if not description:
        description = title
    
    # Avoid repeating "ESPHome" in the description if it's already in the title
    if title.startswith('ESPHome') and description.startswith('ESPHome'):
        description = description[len('ESPHome'):].strip()
        if description.startswith('-'):
            description = description[1:].strip()

    description = description.replace('"', '\\"')
    frontmatter.append(f'description: "{description}"')
    title = title.replace('"', '\\"')
    frontmatter.append(f'title: "{title}"')
    frontmatter.append('---')
    
    # Add Hugo shortcode for SEO
    seo_shortcode = ""
    if seo:
        seo_shortcode = f'{{{{< seo description="{seo.get("description", "")}" image="{seo.get("image", "")}" >}}}}\n\n'
    
    # Combine frontmatter and content
    frontmatter_yaml = "\n".join(frontmatter)
    md_content = "\n".join(md_lines)
    final_content = f"{frontmatter_yaml}\n\n{seo_shortcode}{md_content}"
    
    return final_content

def process_inline_markup(line):
    """Process inline markup in a line of text."""
    processed_line = line
    
    # Code
    processed_line = re.sub(r'``([^`]+)``', r'`\1`', processed_line)
    
    # Bold
    processed_line = re.sub(r'\*\*([^*]+)\*\*', r'**\1**', processed_line)
    
    # Italic
    processed_line = re.sub(r'\*([^*]+)\*', r'*\1*', processed_line)
    
    # Pre-process the line to handle nested references
    # Replace :ref: and :doc: with placeholders to avoid nested processing
    ref_matches = []
    doc_matches = []
    
    # Find and store all :ref: patterns
    for match in re.finditer(r':ref:`([^`]+)`', processed_line):
        ref_content = match.group(1)
        ref_matches.append((match.span(), ref_content))
    
    # Find and store all :doc: patterns
    for match in re.finditer(r':doc:`([^`]+)`', processed_line):
        doc_content = match.group(1)
        doc_matches.append((match.span(), doc_content))
    
    # Replace matches with placeholders, starting from the end to preserve positions
    for i, ((start, end), content) in enumerate(reversed(ref_matches)):
        placeholder = f"__REF_PLACEHOLDER_{i}__"
        processed_line = processed_line[:start] + placeholder + processed_line[end:]
    
    for i, ((start, end), content) in enumerate(reversed(doc_matches)):
        placeholder = f"__DOC_PLACEHOLDER_{i}__"
        processed_line = processed_line[:start] + placeholder + processed_line[end:]
    
    # Process the placeholders
    for i, ((start, end), content) in enumerate(ref_matches):
        placeholder = f"__REF_PLACEHOLDER_{i}__"
        
        # Handle references with text and ID
        if " <" in content and ">" in content:
            text, ref_id = content.split(" <", 1)
            ref_id = ref_id.rstrip(">")
            
            # Look up the document path for this anchor
            doc_path = anchor_map.get(ref_id, "")
            if doc_path:
                replacement = f"[{text}]({{{{< ref \"{doc_path}#{ref_id}\" >}}}})"
            else:
                # If we can't find the document, just use the anchor
                replacement = f"[{text}]({{{{< ref \"#{ref_id}\" >}}}})"
        else:
            # Simple references
            # Look up the document path for this anchor
            doc_path = anchor_map.get(content, "")
            if doc_path:
                replacement = f"[{content}]({{{{< ref \"{doc_path}#{content}\" >}}}})"
            else:
                # If we can't find the document, just use the anchor
                replacement = f"[{content}]({{{{< ref \"#{content}\" >}}}})"
        
        processed_line = processed_line.replace(placeholder, replacement)
    
    for i, ((start, end), content) in enumerate(doc_matches):
        placeholder = f"__DOC_PLACEHOLDER_{i}__"
        
        # Handle document references with text and path
        if "<" in content and ">" in content:
            text, doc_path = content.split("<", 1)
            doc_path = doc_path.rstrip(">")
            # Fix the path for Hugo content structure
            doc_path = fix_doc_path(doc_path)
            replacement = f"[{text}]({{{{< relref \"{doc_path}\" >}}}})"
        else:
            # Simple document references
            doc_path = fix_doc_path(content)
            replacement = f"[{content}]({{{{< ref \"{doc_path}\" >}}}})"
        
        processed_line = processed_line.replace(placeholder, replacement)
    
    # External links
    processed_line = re.sub(r'`([^<]+) <([^>]+)>`__*', r'[\1](\2)', processed_line)
    
    return processed_line

def process_list_table(lines, start_idx):
    """Process a list-table directive and convert it to a Markdown table."""
    # Extract table title and options
    title = ""
    header_rows = 0
    width = ""
    align = ""
    
    current_line = lines[start_idx].strip()
    if current_line.startswith('.. list-table::') or current_line.startswith('..  list-table::'):
        title = current_line.replace('.. list-table::', '').replace('..  list-table::', '').strip()
    
    # Process table options
    idx = start_idx + 1
    while idx < len(lines) and lines[idx].strip().startswith(':'):
        option_line = lines[idx].strip()
        if option_line.startswith(':header-rows:'):
            try:
                header_rows = int(option_line.split(':', 2)[2].strip())
            except (ValueError, IndexError):
                pass
        elif option_line.startswith(':width:'):
            width = option_line.split(':', 2)[2].strip()
        elif option_line.startswith(':align:'):
            align = option_line.split(':', 2)[2].strip()
        elif option_line.startswith(':class:'):
            # We don't use class in Markdown, but we'll parse it anyway
            pass
        idx += 1
    
    # Skip any blank lines
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    
    # Process table rows
    table_data = []
    current_row = []
    
    while idx < len(lines):
        line = lines[idx].strip()
        
        # End of table when we hit a non-indented line after a blank line
        if not line:
            if idx + 1 < len(lines) and not lines[idx + 1].startswith('    '):
                break
            idx += 1
            continue
        
        # New row starts with *
        if line.startswith('*'):
            if current_row:
                table_data.append(current_row)
            current_row = []
            
            # Extract the first cell value
            cell_value = line[1:].strip()
            if cell_value.startswith('-'):
                cell_value = cell_value[1:].strip()
                current_row.append(cell_value)
            
            idx += 1
            continue
        
        # Cell values start with -
        if line.startswith('-'):
            cell_value = line[1:].strip()
            current_row.append(cell_value)
            idx += 1
            continue
        
        # If we get here, it's either the end of the table or something we don't understand
        if not line.startswith('    '):
            break
        
        idx += 1
    
    # Add the last row if it has content
    if current_row:
        table_data.append(current_row)
    
    # Generate Markdown table
    md_table = []
    
    # Add title if present and not empty
    if title and title.strip():
        # Remove any leading colon from the title
        if title.startswith(':'):
            title = title[1:].strip()
        md_table.append(f"### {title}")
        md_table.append("")
    
    # Ensure all rows have the same number of columns
    if table_data:
        max_cols = max(len(row) for row in table_data)
        for row in table_data:
            while len(row) < max_cols:
                row.append("")
        
        # Create the table header
        if header_rows > 0:
            header_row = table_data[0]
            md_table.append("| " + " | ".join(process_inline_markup(cell) for cell in header_row) + " |")
            
            # Add alignment to the separator row if specified
            if align == "center":
                md_table.append("| " + " | ".join([":---:"] * len(header_row)) + " |")
            elif align == "right":
                md_table.append("| " + " | ".join(["---:"] * len(header_row)) + " |")
            elif align == "left":
                md_table.append("| " + " | ".join([":---"] * len(header_row)) + " |")
            else:
                md_table.append("| " + " | ".join(["---"] * len(header_row)) + " |")
            
            # Add data rows
            for row in table_data[header_rows:]:
                md_table.append("| " + " | ".join(process_inline_markup(cell) for cell in row) + " |")
        else:
            # No header, just data rows
            for row in table_data:
                md_table.append("| " + " | ".join(process_inline_markup(cell) for cell in row) + " |")
    
    # Add a blank line after the table
    md_table.append("")
    
    return md_table, idx

def fix_doc_path(path):
    """Fix document paths to match Hugo's content structure."""
    # Remove .rst extension if present
    path = path.lower()
    if path.endswith('.rst'):
        path = path[:-4]
    
    # Handle special cases for components
#    if path.startswith('components/'):
#        path = path[11:]  # Remove 'components/' prefix
#    elif '/' in path and not path.startswith('/'):
#        # For paths like 'switch/gpio', we need to make them '/components/switch/gpio'
#        path = f"/components/{path}"
    
    # Don't add trailing slash for file references
    # Check if it's likely a file reference (contains no hash and has a name after the last slash)
    if not path.startswith('#') and '/' in path:
        last_part = path.split('/')[-1]
        # If the last part looks like a filename (not empty and doesn't end with a slash)
        if last_part and not path.endswith('/'):
            # Don't add a trailing slash
            return path
    
    # Add trailing slash for section references (if not to a specific anchor)
    if not path.startswith('#') and not path.endswith('/') and '#' not in path:
        path = f"{path}/"
    
    return path

def process_includes(lines, current_dir):
    """Process include directives in RST files."""
    processed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check for include directive
        include_match = re.match(r'^(\s*)\.\.[\s]+include::[\s]+(.+\.rst)$', line)
        if include_match:
            indent = include_match.group(1)
            include_file = include_match.group(2).strip()
            
            # Construct the full path to the included file
            include_path = os.path.join(current_dir, include_file)
            
            if os.path.exists(include_path):
                # Read the included file
                with open(include_path, 'r', encoding='utf-8') as f:
                    include_content = f.read()
                
                # Process the included content
                include_lines = include_content.split('\n')
                
                # Add indentation to all lines from the included file
                for include_line in include_lines:
                    if include_line.strip():
                        processed_lines.append(f"{indent}{include_line}")
                    else:
                        processed_lines.append("")
            else:
                # If the file doesn't exist, just keep the include directive as a comment
                processed_lines.append(f"{indent}<!-- Include not found: {include_file} -->")
        else:
            processed_lines.append(line)
        
        i += 1
    
    return processed_lines

def process_file(rst_file, output_dir, input_dir):
    """Process a single RST file and convert it to Markdown."""
    try:
        print(f"\nProcessing file: {rst_file}")
        
        # Read the RST file
        with open(rst_file, 'r', encoding='utf-8') as f:
            rst_content = f.read()
        
        print(f"File size: {len(rst_content)} bytes")
        
        # Get the relative path of the file
        rel_path = os.path.relpath(rst_file, input_dir)
        
        # Process includes before conversion
        current_dir = os.path.dirname(rst_file)
        rst_lines = rst_content.split('\n')
        rst_lines = process_includes(rst_lines, current_dir)
        rst_content = '\n'.join(rst_lines)
        
        # Convert RST to Markdown
        md_content = convert_rst_to_md(rst_content, rel_path)
        
        # Determine output path
        if os.path.basename(rst_file) == 'index.rst':
            # Convert index.rst to _index.md for Hugo
            output_path = os.path.join(output_dir, os.path.dirname(rel_path), '_index.md')
        else:
            output_path = os.path.join(output_dir, os.path.splitext(rel_path)[0] + '.md')
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Write the Markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"Converted {rst_file} -> {output_path}")
        print(f"Output file size: {len(md_content)} bytes")
        
        return output_path
    except Exception as e:
        print(f"Error converting {rst_file}: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

def process_directory(input_dir, output_dir):
    """Process all RST files in a directory and its subdirectories."""
    success_count = 0
    total_count = 0
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.rst'):
                total_count += 1
                rst_file = os.path.join(root, file)
                if process_file(rst_file, output_dir, input_dir):
                    success_count += 1
    
    print(f"Conversion complete. {success_count}/{total_count} files successfully converted to {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Sphinx RST files to Hugo Markdown format')
    parser.add_argument('input_dir', help='Input directory containing RST files')
    parser.add_argument('output_dir', help='Output directory for Markdown files')
    parser.add_argument('--single', help='Process a single file (relative to input_dir)')
    args = parser.parse_args()
    
    if not os.path.isdir(args.input_dir):
        print(f"Error: Input directory '{args.input_dir}' does not exist")
        sys.exit(1)
    
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Build the anchor map first
    build_anchor_map(args.input_dir)
    
    if args.single:
        # Process a single file
        rst_file = os.path.join(args.input_dir, args.single)
        if not os.path.isfile(rst_file):
            print(f"Error: File '{rst_file}' does not exist")
            sys.exit(1)
        process_file(rst_file, args.output_dir, args.input_dir)
        print(f"Converted {rst_file} to {args.output_dir}")
    else:
        # Process all files in the directory
        process_directory(args.input_dir, args.output_dir)
