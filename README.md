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
├── static/            # Static files
│   └── images/        # Image files
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

## Markdown

Hugo uses Markdown files as input. The Markdown processor in use is Goldmark.

## Shortcodes

The following custom shortcodes are available for use in your Markdown content:

### `anchor`
Creates an HTML anchor point that can be linked to with fragment identifiers.
```
{{< anchor "my-anchor-id" >}}
```

### `button`
Creates a button with an image that links to a URL.
```
{{< button href="https://example.com" img="/images/button.png" alt="Example Button" target="_self" >}}
```

### `collapse`
Creates a collapsible section with a title that can be clicked to show/hide content.
```
{{< collapse "title" true >}}
This content will be hidden by default and can be expanded by clicking the header.
You can include any Markdown content here, including lists, code blocks, etc.
the second parameter, if true, will have the content initially opened.
{{< /collapse >}}
```

### `docref`
Creates a link to another page in the documentation with proper handling of anchors.
```
{{< docref "components/sensor/dht" >}}                     <!-- Uses the target page title as link text -->
{{< docref "components/sensor/dht" "DHT Sensor Guide" >}}  <!-- Uses custom text for the link -->
{{< docref "components/sensor/dht#configuration" >}}       <!-- Links to a specific anchor on the page -->
```

### `img`
Displays an image with optional caption, width, height, and CSS class.
```
{{< img src="example.jpg" alt="Example image" caption="This is an example" width="500" class="center" >}}
```

### `imgtable`
Creates a component card with an image, title, and optional description that links to another page.
```
{{< imgtable "DHT Sensor" "/components/sensor/dht" "dht.png" "Temperature and humidity sensor" "sensor-icon" >}}
```

### `note`
Creates a note admonition box to highlight important information.
```
{{< note >}}
This is important information that the reader should pay attention to.
You can include **Markdown** formatting within the note.
{{< /note >}}
```

### `seo`
Adds SEO metadata tags to the page for better search engine optimization and social media sharing.
```
{{< seo description="Detailed guide for setting up the DHT sensor with ESPHome" image="dht-sensor.jpg" >}}
```

### `tip`
Creates a tip admonition box to highlight helpful advice or best practices.
```
{{< tip >}}
For best results, place the sensor away from heat sources.
You can include **Markdown** formatting within the tip.
{{< /tip >}}
```

### `warning`
Creates a warning admonition box to highlight important cautions or potential issues.
```
{{< warning >}}
Incorrect wiring may damage your device. Double-check connections before powering on.
You can include **Markdown** formatting within the warning.
{{< /warning >}}
```

### `apiref`
Creates a link to a C++ API header file.
```
{{< apiref "Component" "esphome/core/component.h" >}}
```

### `apiclass`
Creates a link specifically to a C++ class in the API documentation.
```
{{< apiclass "ClimateDevice" "esphome::climate::ClimateDevice" >}}
{{< apiclass "WiFiComponent" "esphome::wifi::WiFiComponent" >}}
```

### `apistruct`
Creates a link specifically to a C++ struct in the API documentation.
```
{{< apistruct "SensorStateClass" "esphome::sensor::SensorStateClass" >}}
{{< apistruct "GPIOOutputPin" "esphome::output::GPIOOutputPin" >}}
```

### `api-key-input`
Creates an input field with a randomly generated API key and a copy button.
```
{{< api-key-input >}}
```

### `ghuser`
Creates a link to a GitHub user profile.
```
{{< ghuser name="octocat" >}}                <!-- Links to @octocat -->
{{< ghuser name="octocat" text="GitHub" >}}  <!-- Links to @octocat but displays "GitHub" -->
```

### `html_file`
Reads a file from the static directory and inserts it as HTML.
```
{{< html_file file="example.html" class="example-class" >}}
```

### `option`
Creates an option block for documenting command-line options or configuration parameters.
```
{{< option "--help|-h" >}}
This is the help option.
{{< /option >}}
```

### `pr`
Creates a link to a GitHub pull request.
```
{{< pr number="123" >}}                <!-- Links to esphome/esphome#123 -->
{{< pr number="123" repo="docs" >}}    <!-- Links to esphome/docs#123 -->
```

### `redirect`
Creates a page that automatically redirects to another URL.
```
{{< redirect url="/some/path" >}}
```

## Conversion Scripts

A Python script is included to help with the conversion process from RST:

`convert_rst_to_md.py` - Converts Sphinx RST files to Hugo Markdown format
 ```
   python convert_rst_to_md.py /path/to/sphinx/docs /path/to/hugo/content
 ```

Available options for convert_rst_to_md.py:

```
positional arguments:
  input_dir             Input directory containing RST files
  output_dir            Output directory for Markdown files

optional arguments:
  --single FILENAME     Process a single file (relative to input_dir)
  --no-images           Skip image processing
```

Examples:

```bash
# Convert all RST files in a directory
python convert_rst_to_md.py /path/to/sphinx/docs /path/to/hugo/content

# Convert a single RST file
python convert_rst_to_md.py /path/to/sphinx/docs /path/to/hugo/content --single components/sensor/dht.rst

# Convert without processing images
python convert_rst_to_md.py /path/to/sphinx/docs /path/to/hugo/content --no-images
```

The script performs the following operations:
- Builds an anchor map to maintain internal links
- Converts RST formatting to Markdown
- Processes special directives like notes, warnings, and tips
- Converts RST tables to Markdown format
- Handles image references and copies images to appropriate locations
- Processes inline markup and references

## Development

To run the site locally:

1. Install Hugo: https://gohugo.io/installation/
2. Install NodeJS (simplest way to run pagefind)
2. Clone this repository
3. Navigate to the repository directory
4. Run `make live-html`
5. Open your browser to http://localhost:1313/

## Building for Production

See the GitHub workflows in `.github/workflows`

The built site will be in the `public` directory.

## Contributing

Contributions to improve the documentation are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes
4. Submit a pull request

## License

The ESPHome documentation is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
