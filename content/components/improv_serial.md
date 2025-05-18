---
description: "Improv via Serial"
title: "Improv via Serial"
---

{{< seo description="" image="" >}}

The [improv_serial` component in ESPHome implements the open `Improv standard](https://www.improv-wifi.com/)
for configuring Wi-Fi on an ESPHome device by using a serial connection to the device, eg. USB.

The `improv_serial` component requires the serial `logger` to be configured.

The `improv_serial` component will use the project name and version instead of ESPHomes version whenever it's available.


```yaml
# Example configuration entry
wifi:
  # ...

improv_serial:


```
## Configuration variables

- **next_url** (*Optional*, url): A URL that can be used to forward the user to after setting credentials with improv.

## Next URL

Substitutions can be inserted into the URL, such as project name and version and there are some special substitutions
that can be performed by ESPHome when wrapped in double braces `{{ }}`:

- **device_name**: This will substitute the device name including the mac address suffix.
- **ip_address**: This will substitute the IP address of the device.
- **esphome_version**: This will substitute the version of ESPHome that is running on the device.

```yaml
# Example next_url
improv_serial:
  next_url: http://example.com/?device_name={{device_name}}&ip_address={{ip_address}}&esphome_version={{esphome_version}}

```
## See Also

- [wifi]({{< ref "wifi/" >}})
- [captive_portal]({{< ref "captive_portal/" >}})
- [esp32_improv]({{< ref "esp32_improv/" >}})
- [Improv Wi-Fi](https://www.improv-wifi.com/)
- :apiref:`improv_serial/improv_serial_component.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/improv_serial.md)
