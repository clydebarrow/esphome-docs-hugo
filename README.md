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

### `code-block`
Creates a syntax-highlighted code block with a language indicator and copy button.
```
{{< code-block "yaml" >}}
name: example
platform: gpio
pin: D1
{{< /code-block >}}
```

### `collapse`
Creates a collapsible section with a title that can be clicked to show/hide content.
```
{{< collapse "Optional Configuration" >}}
This content will be hidden by default and can be expanded by clicking the header.
You can include any Markdown content here, including lists, code blocks, etc.
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

## Conversion Scripts

A Python script is included to help with the conversion process from RST:

`convert_rst_to_md.py` - Converts Sphinx RST files to Hugo Markdown format
 ```
   python convert_rst_to_md.py /path/to/sphinx/docs /path/to/hugo/content
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
