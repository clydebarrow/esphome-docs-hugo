---
description: "Captive Portal"
title: "Captive Portal"
---

{{< seo description="" image="" >}}

The captive portal component in ESPHome is a fallback mechanism for when connecting to the
configured {{< docref "wifi/" "WiFi" >}} fails.

After 1 minute of unsuccessful WiFi connection attempts, the ESP will start a WiFi hotspot
(with the credentials from your configuration)

{{< img src="captive_portal-ui.png" alt="Image" width="70.0%" class="center" >}}

In this web interface, you can manually override the WiFi settings of the device (please note
this will be overwritten by any subsequent serial upload so make sure to also update your YAML configuration).

Additionally, you can upload a new firmware file.

When you connect to the fallback network, the web interface should open automatically (see also
login to network notifications). If that does not work, you can also navigate to http://192.168.4.1/
manually in your browser.

```yaml
# Example configuration entry
wifi:
  # ...
  ap:
    ssid: "Livingroom Fallback Hotspot"
    password: !secret wifi_ap_password

captive_portal:


```
No configuration variables.


## See Also

- {{< docref "wifi/" >}}
- {{< docref "improv_serial/" >}}
- {{< docref "esp32_improv/" >}}
- :apiref:`captive_portal/captive_portal.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/captive_portal.md)
