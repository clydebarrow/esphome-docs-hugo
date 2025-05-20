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

# Global variables for image tracking
image_map = defaultdict(int)
image_sources = {}
included_files = set()

def find_included_files(file_path):
    """
    Parse a file for include directives and return a list of included files.

    Args:
        file_path: Path to the file to parse
        base_dir: Base directory for resolving relative paths

    Returns:
        List of absolute paths to included files
    """
    included_files = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for .. include:: directives
        include_pattern = r'^\s*\.\.\s+include::\s+(.+?)$'
        matches = re.finditer(include_pattern, content, re.MULTILINE)

        for match in matches:
            included_path = match.group(1).strip()

            # Handle relative paths
            if not os.path.isabs(included_path):
                included_path = os.path.normpath(os.path.join(os.path.dirname(file_path), included_path))

            # Check if the file exists
            if os.path.exists(included_path):
                included_files.append(included_path)
            else:
                print(f"Warning: Included file not found: {included_path}")

        return included_files

    except Exception as e:
        print(f"Error parsing includes in {file_path}: {e}")
        return []

def get_all_included_files(input_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.rst'):
                included_files.update(set(find_included_files(os.path.join(root, file))))

def build_anchor_map(input_dir):
    """Scan all RST files and build a map of anchors to their document paths."""
    print("Building anchor map...")
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            rst_file = os.path.join(root, file)
            if not rst_file in included_files and file.endswith('.rst'):
                rel_path = os.path.relpath(rst_file, input_dir)
                doc_path = os.path.splitext(rel_path)[0]
                
                # Convert to Hugo path format
                doc_path = doc_path.lower()
                
                # Handle index files
                if os.path.basename(doc_path) == 'index':
                    doc_path = os.path.dirname(doc_path) + '/_index'

                rel_path, rst_content = get_rst_content(input_dir, rst_file)
                for i, line in enumerate(rst_content):

                    if line.startswith('.. _') and line.endswith(':'):
                        anchor_name = line[4:-1]  # Extract the anchor name without the '.. _' prefix and ':' suffix
                        if i < len(rst_content) - 2:
                            text = rst_content[i + 2].strip()
                        else:
                            text = ''
                        anchor_map[anchor_name] = doc_path, text

    print(f"Found {len(anchor_map)} anchors across all documents")

def convert_rst_to_md(lines, filename):
    """Convert RST content to Markdown using line-by-line processing."""

    # Extract title and SEO data
    title = ""
    explicit_title = ""
    seo = {}
    
    # Check for explicit title directive
    for i, line in enumerate(lines):
        if line.startswith('.. title::'):
            explicit_title = line.replace('.. title::', '').strip()
            break
    
    # Find title (first line with underline of = or - characters)
    for i in range(len(lines) - 1):
        if re.match(r'^[=-]+$', lines[i + 1]) and lines[i]:
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

        if line.startswith('.. option::'):
            text = line.replace('.. option::', '').strip()
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            md_lines.append(f'{{{{< option "{text}" >}}}}')
            while i < len(lines):
                if not lines[i]:
                    md_lines.append('')
                    i += 1
                    continue
                if lines[i].startswith(' '):
                    md_lines.append(lines[i].strip())
                    i += 1
                else:
                    break
            md_lines.append('{{< /option >}}')
            continue

        # Handle imgtable directive
        if line.strip() == '.. imgtable::':
            i += 1
            # Skip empty lines
            while i < len(lines) and not lines[i].strip():
                i += 1
            
            # Start the imgtable shortcode
            md_lines.append('{{< imgtable >}}')
            
            # Process each entry (each line should be indented)
            while i < len(lines):
                current_line = lines[i].strip()
                
                # If we hit an empty line or a non-indented line, we're done with this imgtable
                if not lines[i].startswith('    ') and current_line:
                    break
                
                # Skip empty lines within the imgtable
                if not current_line:
                    i += 1
                    continue
                
                # Process the entry - format is typically: Title, Link, Image, [Description]
                md_lines.append(current_line)
                i += 1
            
            # Close the imgtable shortcode
            md_lines.append('{{< /imgtable >}}')
            continue

        if line.startswith('.. program::'):
            i += 1
            continue

        # Skip title (we'll add it later with frontmatter)
        if line == title and i + 1 < len(lines) and re.match(r'^=+$', lines[i + 1]):
            i += 2
            continue
        
        # Handle RST anchors (.. _anchor:)
        if line.startswith('.. _') and line.endswith(':'):
            anchor_name = line[4:-1]  # Extract the anchor name without the '.. _' prefix and ':' suffix
            md_lines.append(f'{{{{< anchor "{anchor_name}" >}}}}')
            i += 1
            continue

        # Handle raw HTML blocks that might contain buttons
        if line.strip().startswith('.. raw:: html'):
            button_lines, new_i = process_raw_html_button(lines, i)
            md_lines.extend(button_lines)
            i = new_i
            continue
        
        # Handle list-table directive
        if line.strip().startswith('.. list-table::') or line.strip().startswith('..  list-table::'):
            table_lines, new_i = process_list_table(lines, i)
            md_lines.extend(table_lines)
            i = new_i
            continue
            
        # Handle csv-table directive
        if line.strip().startswith('.. csv-table::'):
            table_lines, new_i = process_csv_table(lines, i)
            md_lines.extend(table_lines)
            i = new_i
            continue
        
        # Handle equals-style headings (main headings)
        if i + 1 < len(lines) and re.match(r'^=+$', lines[i + 1]) and line:
            md_lines.append(f"# {line}")
            i += 2
            continue
        
        # Handle dash-style headings (section headings)
        if i + 1 < len(lines) and re.match(r'^-+$', lines[i + 1]) and line:
            md_lines.append(f"## {line}")
            i += 2
            continue

        # Handle star-style headings (section headings)
        if i + 1 < len(lines) and re.match(r'^\*+$', lines[i + 1]) and line:
            md_lines.append(f"### {line}")
            i += 2
            continue

        # Handle caret and tilde-style headings (subsection headings)
        if i + 1 < len(lines) and re.match(r'(^\^+|^~+)$', lines[i + 1]) and line:
            md_lines.append(f"##### {line}")
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
        if line.strip().startswith('.. note::'):
            # Get the indentation level of the note directive
            note_indent = len(line) - len(line.lstrip())
            md_lines.append(" " * note_indent + "{{< note >}}")
            
            # Skip the blank line
            i += 2
            
            # Add note content
            note_content = []
            content_indent_level = 0
            
            while i < len(lines):
                current_line = lines[i]
                
                # Empty line
                if not current_line.strip():
                    note_content.append('')
                    i += 1
                    continue
                
                # Determine indentation level
                current_indent = len(current_line) - len(current_line.lstrip())
                
                # If this is the first content line, set the base indentation level
                if content_indent_level == 0:
                    content_indent_level = current_indent
                
                # If the line is not indented enough, we've reached the end of the note
                if current_indent < note_indent + 4 and current_line.strip() and not current_line.strip().startswith('..'):
                    break
                
                # Handle code blocks within notes
                if current_line.strip().startswith('.. code-block::'):
                    language = current_line.replace('.. code-block::', '').strip() or 'yaml'
                    note_content.append('```' + language)
                    i += 1
                    
                    # Skip blank line if present
                    if i < len(lines) and not lines[i].strip():
                        i += 1
                    
                    # Add code content
                    while i < len(lines) and (len(lines[i]) - len(lines[i].lstrip()) > content_indent_level):
                        code_line = lines[i]
                        # Remove the extra indentation but preserve indentation relative to the note
                        extra_indent = current_indent - content_indent_level
                        code_line = " " * extra_indent + code_line[content_indent_level + 4:]  # 4 spaces for code block indentation
                        note_content.append(code_line)
                        i += 1
                    
                    note_content.append('```')
                    continue
                
                # Regular content - remove the base indentation but preserve indentation relative to the note
                if current_indent >= content_indent_level:
                    extra_indent = max(0, current_indent - content_indent_level)
                    processed_line = " " * extra_indent + current_line[content_indent_level:].rstrip()
                    # Process inline markup
                    processed_line = process_inline_markup(processed_line)
                    note_content.append(processed_line)
                else:
                    # End of the note block
                    break
                
                i += 1
            
            # Add the processed note content
            md_lines.extend(note_content)
            md_lines.append(" " * note_indent + "{{< /note >}}")
            continue
        
        # Handle warnings
        if line.strip().startswith('.. warning::'):
            # Get the indentation level of the warning directive
            warning_indent = len(line) - len(line.lstrip())
            md_lines.append(" " * warning_indent + "{{< warning >}}")
            
            # Skip the blank line
            i += 2
            
            # Add warning content
            warning_content = []
            content_indent_level = 0
            
            while i < len(lines):
                current_line = lines[i]
                
                # Empty line
                if not current_line.strip():
                    warning_content.append('')
                    i += 1
                    continue
                
                # Determine indentation level
                current_indent = len(current_line) - len(current_line.lstrip())
                
                # If this is the first content line, set the base indentation level
                if content_indent_level == 0:
                    content_indent_level = current_indent
                
                # If the line is not indented enough, we've reached the end of the warning
                if current_indent < warning_indent + 4 and current_line.strip():
                    break
                
                # Handle code blocks within warnings
                if current_line.strip().startswith('.. code-block::'):
                    language = current_line.replace('.. code-block::', '').strip() or 'yaml'
                    warning_content.append('```' + language)
                    i += 1
                    
                    # Skip blank line if present
                    if i < len(lines) and not lines[i].strip():
                        i += 1
                    
                    # Add code content
                    while i < len(lines) and (len(lines[i]) - len(lines[i].lstrip()) > content_indent_level):
                        code_line = lines[i]
                        # Remove the extra indentation but preserve indentation relative to the warning
                        extra_indent = current_indent - content_indent_level
                        code_line = " " * extra_indent + code_line[content_indent_level + 4:]  # 4 spaces for code block indentation
                        warning_content.append(code_line)
                        i += 1
                    
                    warning_content.append('```')
                    continue
                
                # Regular content - remove the base indentation but preserve indentation relative to the warning
                if current_indent >= content_indent_level:
                    extra_indent = max(0, current_indent - content_indent_level)
                    processed_line = " " * extra_indent + current_line[content_indent_level:].rstrip()
                    # Process inline markup
                    processed_line = process_inline_markup(processed_line)
                    warning_content.append(processed_line)
                else:
                    # End of the warning block
                    break
                
                i += 1
            
            # Add the processed warning content
            md_lines.extend(warning_content)
            md_lines.append(" " * warning_indent + "{{< /warning >}}")
            continue
        
        # Handle tips
        if line.strip().startswith('.. tip::'):
            # Get the indentation level of the tip directive
            tip_indent = len(line) - len(line.lstrip())
            md_lines.append(" " * tip_indent + "{{< tip >}}")
            
            # Skip the blank line
            i += 2
            
            # Add tip content
            tip_content = []
            content_indent_level = 0
            
            while i < len(lines):
                current_line = lines[i]
                
                # Empty line
                if not current_line.strip():
                    tip_content.append('')
                    i += 1
                    continue
                
                # Determine indentation level
                current_indent = len(current_line) - len(current_line.lstrip())
                
                # If this is the first content line, set the base indentation level
                if content_indent_level == 0:
                    content_indent_level = current_indent
                
                # If the line is not indented enough, we've reached the end of the tip
                if current_indent < tip_indent + 4 and current_line.strip() and not current_line.strip().startswith('..'):
                    break
                
                # Handle code blocks within tips
                if current_line.strip().startswith('.. code-block::'):
                    language = current_line.replace('.. code-block::', '').strip() or 'yaml'
                    tip_content.append('```' + language)
                    i += 1
                    
                    # Skip blank line if present
                    if i < len(lines) and not lines[i].strip():
                        i += 1
                    
                    # Add code content
                    while i < len(lines) and (len(lines[i]) - len(lines[i].lstrip()) > content_indent_level):
                        code_line = lines[i]
                        # Remove the extra indentation but preserve indentation relative to the tip
                        extra_indent = current_indent - content_indent_level
                        code_line = " " * extra_indent + code_line[content_indent_level + 4:]  # 4 spaces for code block indentation
                        tip_content.append(code_line)
                        i += 1
                    
                    tip_content.append('```')
                    continue
                
                # Regular content - remove the base indentation but preserve indentation relative to the tip
                if current_indent >= content_indent_level:
                    extra_indent = max(0, current_indent - content_indent_level)
                    processed_line = " " * extra_indent + current_line[content_indent_level:].rstrip()
                    # Process inline markup
                    processed_line = process_inline_markup(processed_line)
                    tip_content.append(processed_line)
                else:
                    # End of the tip block
                    break
                
                i += 1
            
            # Add the processed tip content
            md_lines.extend(tip_content)
            md_lines.append(" " * tip_indent + "{{< /tip >}}")
            continue
        
        # Handle figures
        if line.strip().startswith('.. figure::'):
            shortcode, new_i = process_image_directive(lines, i, is_figure=True)
            md_lines.append(shortcode)
            md_lines.append("")
            i = new_i
            continue
        
        # Handle image directives
        if line.strip().startswith('.. image::'):
            shortcode, new_i = process_image_directive(lines, i)
            md_lines.append(shortcode)
            i = new_i
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
            doc_path, anchor_text = anchor_map.get(ref_id, ("", ""))
            if not doc_path:
                print(f"Warning: Could not find document path for anchor '{ref_id}'")
            text = text or anchor_text
            if doc_path:
                replacement = f"[{text}]({{{{< ref \"{doc_path}#{ref_id}\" >}}}})"
            else:
                # If we can't find the document, just use the anchor
                replacement = f"[{text}]({{{{< ref \"#{ref_id}\" >}}}})"
        else:
            # Simple references
            # Look up the document path for this anchor
            doc_path, anchor_text = anchor_map.get(content, ("", ""))
            anchor_text = anchor_text or content
            if doc_path:
                replacement = f"[{anchor_text}]({{{{< ref \"{doc_path}#{content}\" >}}}})"
            else:
                # If we can't find the document, just use the anchor
                replacement = f"[{anchor_text}]({{{{< ref \"#{content}\" >}}}})"
        
        processed_line = processed_line.replace(placeholder, replacement)
    
    for i, ((start, end), content) in enumerate(doc_matches):
        placeholder = f"__DOC_PLACEHOLDER_{i}__"
        
        # Handle document references with text and path
        if "<" in content and ">" in content:
            text, doc_path = content.split("<", 1)
            doc_path = doc_path.rstrip(">")
            # Fix the path for Hugo content structure
            doc_path = fix_doc_path(doc_path)
            # Use the docref shortcode with custom text
            replacement = f"{{{{< docref \"{doc_path}\" \"{text.strip()}\" >}}}}"
        else:
            # Simple document references
            doc_path = fix_doc_path(content)
            replacement = f"{{{{< docref \"{doc_path}\" >}}}}"
        
        processed_line = processed_line.replace(placeholder, replacement)
    
    # External links
    processed_line = re.sub(r'`([^<]+) <([^>]+)>`__*', r'[\1](\2)', processed_line)
    processed_line = re.sub(r'^\.\. _([^:]+):\s*(http.*)$', r'[\1](\2)', processed_line)
    
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

def process_csv_table(lines, start_idx):
    """Process a csv-table directive and convert it to a Markdown table."""
    # Extract table title and options
    title = ""
    header_rows = 0
    width = ""
    align = ""
    delimiter = ","
    
    current_line = lines[start_idx].strip()
    if current_line.startswith('.. csv-table::'):
        title = current_line.replace('.. csv-table::', '').strip()
    
    # Process table options
    idx = start_idx + 1
    while idx < len(lines) and lines[idx].strip().startswith(':'):
        option_line = lines[idx].strip()
        if option_line.startswith(':header:'):
            try:
                header_rows = int(option_line.split(':', 2)[2].strip())
            except (ValueError, IndexError):
                pass
        elif option_line.startswith(':width:'):
            width = option_line.split(':', 2)[2].strip()
        elif option_line.startswith(':align:'):
            align = option_line.split(':', 2)[2].strip()
        elif option_line.startswith(':delim:'):
            delimiter = option_line.split(':', 2)[2].strip()
            # Handle special delimiter cases
            if delimiter == 'tab':
                delimiter = '\t'
            elif delimiter == 'space':
                delimiter = ' '
        elif option_line.startswith(':file:'):
            # Handle CSV file inclusion
            csv_file = option_line.split(':', 2)[2].strip()
            # This would need to be implemented to read from the file
            # For now, we'll just print a warning
            print(f"Warning: CSV file inclusion not yet supported: {csv_file}")
        idx += 1
    
    # Skip any blank lines
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    
    # Process table rows
    table_data = []
    
    while idx < len(lines):
        line = lines[idx].strip()
        
        # End of table when we hit a non-indented line after a blank line
        if not line:
            if idx + 1 < len(lines) and not lines[idx + 1].startswith('    '):
                break
            idx += 1
            continue
        
        # End of table when we hit a line that doesn't start with whitespace
        if not lines[idx].startswith('    '):
            break
        
        # Process CSV line
        # Remove leading whitespace but keep the rest of the line intact
        csv_line = lines[idx][4:].rstrip('\n')
        
        # Split by delimiter, respecting quotes
        import csv
        from io import StringIO
        
        try:
            reader = csv.reader(StringIO(csv_line), delimiter=delimiter)
            row = next(reader)
            # Improved quote stripping from values - handle both single and double quotes
            # and make sure to strip from both beginning and end of each cell
            processed_row = []
            for cell in row:
                # First strip whitespace
                cell = cell.strip()
                # Then strip quotes if they exist at both beginning and end
                if (cell.startswith('"') and cell.endswith('"')) or (cell.startswith("'") and cell.endswith("'")):
                    cell = cell[1:-1]
                processed_row.append(cell)
            table_data.append(processed_row)
        except Exception as e:
            print(f"Warning: Error parsing CSV line: {csv_line} - {e}")
            table_data.append([csv_line])
        
        idx += 1
    
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
        
        # Create the table header and separator
        if header_rows > 0 and len(table_data) > 0:
            # Add header row
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
            # No header specified, but we still need to add a separator after the first row
            if table_data:
                # Add first row
                first_row = table_data[0]
                md_table.append("| " + " | ".join(process_inline_markup(cell) for cell in first_row) + " |")
                
                # Add separator row
                if align == "center":
                    md_table.append("| " + " | ".join([":---:"] * len(first_row)) + " |")
                elif align == "right":
                    md_table.append("| " + " | ".join(["---:"] * len(first_row)) + " |")
                elif align == "left":
                    md_table.append("| " + " | ".join([":---"] * len(first_row)) + " |")
                else:
                    md_table.append("| " + " | ".join(["---"] * len(first_row)) + " |")
                
                # Add remaining data rows
                for row in table_data[1:]:
                    md_table.append("| " + " | ".join(process_inline_markup(cell) for cell in row) + " |")
    
    # Add a blank line after the table
    md_table.append("")
    
    return md_table, idx

def process_raw_html_button(lines, i):
    """Process raw HTML button patterns and convert them to button shortcode."""
    button_lines = []
    raw_html_indent = len(lines[i]) - len(lines[i].lstrip())
    
    # Skip the ".. raw:: html" line
    i += 1
    
    # Skip any blank lines
    while i < len(lines) and not lines[i].strip():
        i += 1
    
    # Collect HTML content
    html_content = []
    raw_html_content = []
    while i < len(lines) and (not lines[i].strip() or lines[i].startswith(' ' * (raw_html_indent + 4))):
        raw_html_content.append(lines[i].lstrip())
        if lines[i].strip():
            html_content.append(lines[i].strip())
        i += 1
    
    # Join the HTML content
    html = ' '.join(html_content)
    
    # Check if it's a button pattern
    href_match = re.search(r'<a\s+href="([^"]+)"[^>]*>', html)
    img_match = re.search(r'<img\s+src="([^"]+)"[^>]*alt="([^"]*)"[^>]*/?>', html)
    
    if href_match and img_match:
        href = href_match.group(1)
        img = img_match.group(1)
        alt = img_match.group(2)
        
        # Create button shortcode
        button_lines.append(f'{{{{< button href="{href}" img="{img}" alt="{alt}" >}}}}')
    else:
        # If it's not a button pattern, just keep the raw HTML
        button_lines.append('\n'.join(raw_html_content))
    
    return button_lines, i

def process_image_directive(lines, i, is_figure=False):
    """Process an image or figure directive and convert it to a Hugo shortcode."""
    line = lines[i]
    
    if is_figure:
        image_path = line.replace('.. figure::', '').strip()
    else:
        image_path = line.replace('.. image::', '').strip()
    
    # Extract the image filename
    image_filename = os.path.basename(image_path)
    
    # Skip options
    i += 1
    
    # Process options
    alt_text = "Image"
    caption = ""
    width = ""
    height = ""
    align = ""
    
    while i < len(lines) and (not lines[i].strip() or lines[i].startswith('  ') and lines[i].strip().startswith(':')):
        option_line = lines[i].strip()
        if option_line.startswith(':alt:'):
            alt_text = option_line.replace(':alt:', '').strip()
        elif option_line.startswith(':width:'):
            width = option_line.split(':', 2)[2].strip()
        elif option_line.startswith(':height:'):
            height = option_line.split(':', 2)[2].strip()
        elif option_line.startswith(':align:'):
            align = option_line.split(':', 2)[2].strip()
        i += 1
    
    # Get caption if present (for figures)
    while i < len(lines) and lines[i].startswith('  ') and is_figure:
        caption += lines[i].strip()
        i += 1

    # Skip any blank lines after the caption
    while i < len(lines) and not lines[i].strip():
        i += 1
    
    # Escape quotes in alt text and caption
    if alt_text:
        alt_text = alt_text.replace('"', '\\"')
    if caption:
        caption = caption.replace('"', '\\"')
    
    # Create the shortcode
    shortcode = f'{{{{< img src="{image_filename}" alt="{alt_text}"'
    if caption:
        shortcode += f' caption="{caption}"'
    if width:
        shortcode += f' width="{width}"'
    if height:
        shortcode += f' height="{height}"'
    if align:
        shortcode += f' class="{align}"'
    shortcode += ' >}}'
    
    return shortcode, i

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

def scan_image_references(input_dir):
    """Scan all RST files for image references and track their usage."""
    print("Scanning for image references...")
    
    # Regular expressions to match different types of image references
    image_patterns = [
        r'.. figure:: ([^\s]+)',  # Figure directive
        r'.. image:: ([^\s]+)',   # Image directive
        r'image:: ([^\s]+)',      # Image reference
        r'src="([^"]+\.(png|jpg|jpeg|gif|svg))"',  # HTML img tag
        r'!\[(.*?)\]\(([^)]+\.(png|jpg|jpeg|gif|svg))\)'  # Markdown image syntax
    ]
    
    # Initialize image tracking dictionaries
    image_map = defaultdict(int)
    image_sources = {}
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.rst'):
                rst_file = os.path.join(root, file)
                rel_path = os.path.relpath(rst_file, input_dir)
                
                with open(rst_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.splitlines()
                
                # Find all image references using regex patterns
                for pattern in image_patterns:
                    for match in re.finditer(pattern, content):
                        image_path = match.group(1).strip()
                        
                        # Skip alignment options and other non-image paths
                        if image_path in ['center', 'left', 'right']:
                            continue
                        
                        # Skip URLs
                        if image_path.startswith(('http://', 'https://')):
                            continue
                        
                        # Normalize path
                        if image_path.startswith('/'):
                            # Absolute path within docs
                            abs_image_path = os.path.join(input_dir, image_path.lstrip('/'))
                            rel_image_path = image_path.lstrip('/')
                        else:
                            # Relative path
                            abs_image_path = os.path.join(os.path.dirname(rst_file), image_path)
                            rel_image_path = os.path.relpath(abs_image_path, input_dir)
                        
                        # Only count if the image file exists
                        if os.path.exists(abs_image_path):
                            image_filename = os.path.basename(image_path)
                            image_map[image_filename] += 1
                            image_sources[image_filename] = abs_image_path
                            print(f"Found image: {image_filename} in {rel_path}")
                
                # Find images in imgtable directives
                i = 0
                while i < len(lines):
                    line = lines[i].strip()
                    
                    # Check for imgtable directive
                    if line == '.. imgtable::':
                        i += 1
                        # Skip empty lines
                        while i < len(lines) and not lines[i].strip():
                            i += 1
                        
                        # Process each entry in the imgtable
                        while i < len(lines):
                            current_line = lines[i].strip()
                            
                            # If we hit an empty line or a non-indented line, we're done with this imgtable
                            if not lines[i].startswith('    ') and current_line:
                                break
                            
                            # Skip empty lines within the imgtable
                            if not current_line:
                                i += 1
                                continue
                            
                            # Process the entry - format is typically: Title, Link, Image, [Description]
                            parts = [part.strip() for part in current_line.split(',')]
                            if len(parts) >= 3:  # We need at least 3 parts (title, link, image)
                                image_path = parts[2]
                                
                                # Skip URLs
                                if image_path.startswith(('http://', 'https://')):
                                    i += 1
                                    continue
                                
                                # Normalize path
                                if image_path.startswith('/'):
                                    # Absolute path within docs
                                    abs_image_path = os.path.join(input_dir, image_path.lstrip('/'))
                                    rel_image_path = image_path.lstrip('/')
                                else:
                                    # Relative path
                                    abs_image_path = os.path.join(os.path.dirname(rst_file), image_path)
                                    if not os.path.exists(abs_image_path):
                                        abs_image_path = os.path.join(input_dir, "images", image_path)

                                # Only count if the image file exists
                                if os.path.exists(abs_image_path):
                                    image_filename = os.path.basename(image_path)
                                    image_map[image_filename] += 1
                                    image_sources[image_filename] = abs_image_path
                                    print(f"Found image in imgtable: {image_filename} in {rel_path}")
                                else:
                                    print(f"Image not found: {image_path} in {abs_image_path}")
                            
                            i += 1
                    else:
                        i += 1
    
    # Print statistics
    print(f"Found {len(image_map)} unique images")
    print(f"Images used more than once: {sum(1 for count in image_map.values() if count > 1)}")
    
    return image_map, image_sources

def process_file(rst_file, output_dir, input_dir):
    output_dir = os.path.join(output_dir, "content")
    """Process a single RST file and convert it to Markdown."""
    try:
        print(f"\nProcessing file: {rst_file}")
        
        # Read the RST file
        rel_path, rst_content = get_rst_content(input_dir, rst_file)

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


def get_rst_content(input_dir, rst_file):
    with open(rst_file, 'r', encoding='utf-8') as f:
        rst_content = f.read()
    print(f"File size: {len(rst_content)} bytes")
    # Get the relative path of the file
    rel_path = os.path.relpath(rst_file, input_dir)
    # Process includes before conversion
    current_dir = os.path.dirname(rst_file)
    rst_lines = rst_content.split('\n')
    rst_lines = process_includes(rst_lines, current_dir)
    return rel_path, rst_lines


def process_directory(input_dir, output_dir):
    """Process all RST files in a directory and its subdirectories."""
    success_count = 0
    total_count = 0

    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.rst'):
                rst_file = os.path.join(root, file)
                included_files.update(set(find_included_files(rst_file)))

    for root, _, files in os.walk(input_dir):
        for file in files:
            rst_file = os.path.join(root, file)
            if rst_file in included_files:
                print("Skipping included file:", rst_file)
            elif file.endswith('.rst'):
                included_files.update(set(find_included_files(rst_file)))
                total_count += 1
                if process_file(rst_file, output_dir, input_dir):
                    success_count += 1
    
    print(f"Conversion complete. {success_count}/{total_count} files successfully converted to {output_dir}")

def should_copy_file(source_path, target_path):
    """
    Determine if a file should be copied based on existence and modification time.
    Returns True if the target doesn't exist or if the source is newer than the target.
    """
    if not os.path.exists(target_path):
        return True
    
    # Check if source is newer than target
    source_mtime = os.path.getmtime(source_path)
    target_mtime = os.path.getmtime(target_path)
    
    return source_mtime > target_mtime

def copy_images_to_output(output_dir, input_dir, image_map, image_sources):
    """Copy images to the appropriate locations based on usage."""
    print("Copying images to output directories...")
    
    # Create global images directory
    global_images_dir = os.path.join(output_dir, 'static', 'images')
    os.makedirs(global_images_dir, exist_ok=True)
    
    # Track which files have been copied to which component directories
    component_image_map = {}
    
    # Copy images based on usage
    for image_name, count in image_map.items():
        source_path = image_sources[image_name]
        
        if count > 1:
            # Used more than once - copy to global images folder
            target_path = os.path.join(global_images_dir, image_name)
            if should_copy_file(source_path, target_path):
                shutil.copy2(source_path, target_path)
                print(f"Copied {image_name} to global images folder")
            else:
                print(f"Skipped copying {image_name} to global images folder (unchanged)")
        else:
            # Used only once - copy to component-level images folder
            # Find the RST file that references this image
            for root, _, files in os.walk(input_dir):
                for file in files:
                    if file.endswith('.rst'):
                        rst_file = os.path.join(root, file)
                        with open(rst_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                            
                        if image_name in content:
                            # Get the relative path of the RST file
                            rel_path = os.path.relpath(rst_file, input_dir)
                            component_dir = os.path.dirname(rel_path)
                            
                            # Create component-level images directory in content
                            component_content_dir = os.path.join(output_dir, 'content', component_dir)
                            component_images_dir = os.path.join(component_content_dir, 'images')
                            os.makedirs(component_images_dir, exist_ok=True)
                            
                            # Create component-level images directory in static
                            component_static_dir = os.path.join(output_dir, 'static', component_dir)
                            component_static_images_dir = os.path.join(component_static_dir, 'images')
                            os.makedirs(component_static_images_dir, exist_ok=True)
                            
                            # Copy the image to both locations
                            target_content_path = os.path.join(component_images_dir, image_name)
                            target_static_path = os.path.join(component_static_images_dir, image_name)
                            
                            copied = False
                            if should_copy_file(source_path, target_content_path):
                                shutil.copy2(source_path, target_content_path)
                                copied = True
                            
                            if should_copy_file(source_path, target_static_path):
                                shutil.copy2(source_path, target_static_path)
                                copied = True
                                
                            if copied:
                                print(f"Copied {image_name} to {component_dir}/images folder")
                            else:
                                print(f"Skipped copying {image_name} to {component_dir}/images folder (unchanged)")
                            
                            # Track which component this image was copied to
                            component_image_map[image_name] = component_dir
                            break
    
    return component_image_map

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Sphinx RST files to Hugo Markdown format')
    parser.add_argument('input_dir', help='Input directory containing RST files')
    parser.add_argument('output_dir', help='Output directory for Markdown files')
    parser.add_argument('--single', help='Process a single file (relative to input_dir)')
    parser.add_argument('--no-images', action='store_true', help='Skip image processing')
    args = parser.parse_args()
    
    # Ensure output directory exists
    os.makedirs(args.output_dir, exist_ok=True)
    os.makedirs(os.path.join(args.output_dir, 'content'), exist_ok=True)
    os.makedirs(os.path.join(args.output_dir, 'static'), exist_ok=True)
    
    # Build the anchor map first
    get_all_included_files(args.input_dir)
    build_anchor_map(args.input_dir)
    
    # Scan for image references
    image_map, image_sources = scan_image_references(args.input_dir)
    
    if args.single:
        # Process a single file
        rst_file = os.path.join(args.input_dir, args.single)
        if os.path.exists(rst_file):
            process_file(rst_file, args.output_dir, args.input_dir)
        else:
            print(f"Error: File {rst_file} not found")
    else:
        # Process all files in the directory
        process_directory(args.input_dir, args.output_dir)
    
    # Copy images to output directories
    if not args.no_images:
        copy_images_to_output(args.output_dir, args.input_dir, image_map, image_sources)
