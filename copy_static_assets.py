#!/usr/bin/env python3
"""
Copy static assets from the Sphinx documentation to the Hugo site.
This script helps migrate images, CSS, and other static files from Sphinx to Hugo.
"""

import os
import sys
import argparse
import shutil
from pathlib import Path

def copy_images(source_dir, target_dir):
    """Copy images from Sphinx _static directory to Hugo static/images directory."""
    source_images = os.path.join(source_dir, '_static')
    target_images = os.path.join(target_dir, 'static/images')
    
    # Create target directory if it doesn't exist
    os.makedirs(target_images, exist_ok=True)
    
    # Copy image files
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg']
    count = 0
    
    for root, _, files in os.walk(source_images):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                source_path = os.path.join(root, file)
                # Preserve relative directory structure
                rel_path = os.path.relpath(source_path, source_images)
                target_path = os.path.join(target_images, rel_path)
                
                # Create subdirectories if needed
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                
                # Copy the file
                shutil.copy2(source_path, target_path)
                count += 1
                print(f"Copied: {rel_path}")
    
    print(f"Copied {count} image files to {target_images}")

def copy_component_images(source_dir, target_dir):
    """Copy images from component directories to Hugo static/components directory."""
    source_components = os.path.join(source_dir, 'components')
    target_components = os.path.join(target_dir, 'static/components')
    
    # Create target directory if it doesn't exist
    os.makedirs(target_components, exist_ok=True)
    
    # Copy image files
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg']
    count = 0
    
    for root, _, files in os.walk(source_components):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                source_path = os.path.join(root, file)
                # Preserve relative directory structure
                rel_path = os.path.relpath(source_path, source_components)
                target_path = os.path.join(target_components, rel_path)
                
                # Create subdirectories if needed
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                
                # Copy the file
                shutil.copy2(source_path, target_path)
                count += 1
                print(f"Copied component image: {rel_path}")
    
    print(f"Copied {count} component image files to {target_components}")

def copy_css(source_dir, target_dir):
    """Copy CSS files from Sphinx _static directory to Hugo static/css directory."""
    source_css = os.path.join(source_dir, '_static')
    target_css = os.path.join(target_dir, 'static/css')
    
    # Create target directory if it doesn't exist
    os.makedirs(target_css, exist_ok=True)
    
    # Copy CSS files
    count = 0
    
    for root, _, files in os.walk(source_css):
        for file in files:
            if file.lower().endswith('.css'):
                source_path = os.path.join(root, file)
                # Preserve relative directory structure
                rel_path = os.path.relpath(source_path, source_css)
                target_path = os.path.join(target_css, rel_path)
                
                # Create subdirectories if needed
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                
                # Copy the file
                shutil.copy2(source_path, target_path)
                count += 1
                print(f"Copied: {rel_path}")
    
    print(f"Copied {count} CSS files to {target_css}")

def copy_js(source_dir, target_dir):
    """Copy JavaScript files from Sphinx _static directory to Hugo static/js directory."""
    source_js = os.path.join(source_dir, '_static')
    target_js = os.path.join(target_dir, 'static/js')
    
    # Create target directory if it doesn't exist
    os.makedirs(target_js, exist_ok=True)
    
    # Copy JavaScript files
    count = 0
    
    for root, _, files in os.walk(source_js):
        for file in files:
            if file.lower().endswith('.js'):
                source_path = os.path.join(root, file)
                # Preserve relative directory structure
                rel_path = os.path.relpath(source_path, source_js)
                target_path = os.path.join(target_js, rel_path)
                
                # Create subdirectories if needed
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                
                # Copy the file
                shutil.copy2(source_path, target_path)
                count += 1
                print(f"Copied: {rel_path}")
    
    print(f"Copied {count} JavaScript files to {target_js}")

def copy_fonts(source_dir, target_dir):
    """Copy font files from Sphinx _static directory to Hugo static/fonts directory."""
    source_fonts = os.path.join(source_dir, '_static')
    target_fonts = os.path.join(target_dir, 'static/fonts')
    
    # Create target directory if it doesn't exist
    os.makedirs(target_fonts, exist_ok=True)
    
    # Copy font files
    font_extensions = ['.woff', '.woff2', '.ttf', '.eot', '.otf']
    count = 0
    
    for root, _, files in os.walk(source_fonts):
        for file in files:
            if any(file.lower().endswith(ext) for ext in font_extensions):
                source_path = os.path.join(root, file)
                # Preserve relative directory structure
                rel_path = os.path.relpath(source_path, source_fonts)
                target_path = os.path.join(target_fonts, rel_path)
                
                # Create subdirectories if needed
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                
                # Copy the file
                shutil.copy2(source_path, target_path)
                count += 1
                print(f"Copied: {rel_path}")
    
    print(f"Copied {count} font files to {target_fonts}")

def copy_other_static_files(source_dir, target_dir):
    """Copy other static files that might be useful."""
    source_static = os.path.join(source_dir, '_static')
    target_static = os.path.join(target_dir, 'static')
    
    # Create target directory if it doesn't exist
    os.makedirs(target_static, exist_ok=True)
    
    # Copy favicon and other root static files
    favicon_files = ['favicon.ico', 'robots.txt', 'sitemap.xml']
    count = 0
    
    for file in favicon_files:
        source_path = os.path.join(source_static, file)
        if os.path.exists(source_path):
            target_path = os.path.join(target_static, file)
            shutil.copy2(source_path, target_path)
            count += 1
            print(f"Copied: {file}")
    
    print(f"Copied {count} other static files to {target_static}")

def copy_all_svg_files(source_dir, target_dir):
    """Copy all SVG files from the entire source directory to Hugo static/images directory."""
    target_images = os.path.join(target_dir, 'static/images')
    
    # Create target directory if it doesn't exist
    os.makedirs(target_images, exist_ok=True)
    
    # Copy SVG files
    count = 0
    
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith('.svg'):
                source_path = os.path.join(root, file)
                
                # Skip files in _static directory as they're already handled by copy_images
                if '/_static/' in source_path:
                    continue
                
                # Skip files in components directory as they're already handled by copy_component_images
                if '/components/' in source_path:
                    continue
                
                # Preserve relative directory structure
                rel_path = os.path.relpath(source_path, source_dir)
                target_path = os.path.join(target_images, rel_path)
                
                # Create subdirectories if needed
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                
                # Copy the file
                shutil.copy2(source_path, target_path)
                count += 1
                print(f"Copied SVG: {rel_path}")
    
    print(f"Copied {count} additional SVG files to {target_images}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Copy static assets from Sphinx to Hugo')
    parser.add_argument('source_dir', help='Source directory containing Sphinx documentation')
    parser.add_argument('target_dir', help='Target directory for Hugo site')
    args = parser.parse_args()
    
    if not os.path.isdir(args.source_dir):
        print(f"Error: Source directory '{args.source_dir}' does not exist")
        sys.exit(1)
    
    if not os.path.isdir(args.target_dir):
        print(f"Error: Target directory '{args.target_dir}' does not exist")
        sys.exit(1)
    
    copy_images(args.source_dir, args.target_dir)
    copy_component_images(args.source_dir, args.target_dir)
    copy_all_svg_files(args.source_dir, args.target_dir)
    copy_css(args.source_dir, args.target_dir)
    copy_js(args.source_dir, args.target_dir)
    copy_fonts(args.source_dir, args.target_dir)
    copy_other_static_files(args.source_dir, args.target_dir)
    
    print("Asset copying complete!")
