# ESPHome Documentation - Hugo Version

This repository contains the Hugo version of the ESPHome documentation, converted from the original Sphinx documentation.

## Project Structure

The project follows the standard Hugo directory structure:

```
esphome-docs-hugo/
├── archetypes/        # Content templates
├── assets/            # Source files for CSS, JS, etc.
├── content/           # Markdown content files
├── data/              # Data files for templates
├── layouts/           # HTML templates
├── static/            # Static files (images, CSS, JS)
├── themes/            # Custom theme for ESPHome
│   └── esphome-theme/ # The ESPHome custom theme
├── hugo.yaml          # Hugo configuration
└── README.md          # This file
```

## Custom Theme

The site uses a custom theme called `esphome-theme` which is designed to match the look and feel of the original ESPHome documentation. The theme includes:

- Responsive design for mobile and desktop
- Dark mode support
- Custom shortcodes for documentation features
- Navigation sidebar
- Search functionality

## Shortcodes

The following custom shortcodes are available:

- `{{</* imgtable */>}}` - For displaying image tables
- `{{</* note */>}}` - For note admonitions
- `{{</* warning */>}}` - For warning admonitions
- `{{</* collapse */>}}` - For collapsible sections
- `{{</* seo */>}}` - For SEO metadata
- `{{</* code-block */>}}` - For code blocks with syntax highlighting

## Conversion Scripts

Two Python scripts are included to help with the conversion process:

1. `convert_rst_to_md.py` - Converts Sphinx RST files to Hugo Markdown format
   ```
   python convert_rst_to_md.py /path/to/sphinx/docs /path/to/hugo/content
   ```

2. `copy_static_assets.py` - Copies static assets from Sphinx to Hugo
   ```
   python copy_static_assets.py /path/to/sphinx/docs /path/to/hugo
   ```

## Development

To run the site locally:

1. Install Hugo: https://gohugo.io/installation/
2. Clone this repository
3. Navigate to the repository directory
4. Run `hugo server -D`
5. Open your browser to http://localhost:1313/

## Building for Production

To build the site for production:

```
hugo --minify
```

The built site will be in the `public` directory.

## Contributing

Contributions to improve the documentation are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes
4. Submit a pull request

## License

The ESPHome documentation is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
