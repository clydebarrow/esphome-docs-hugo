---
description: "ESP32 Bluetooth Low Energy Scanner"
title: "ESP32 Bluetooth Low Energy Scanner"
---

{{< seo description="" image="" >}}

The `ble_scanner` text sensor platform lets you track reachable BLE devices.

See the [Configuration variables:]({{< ref "components/esp32_ble_tracker#config-esp32_ble_tracker" >}}) for instructions for setting up scan parameters.

The sensor platform is similar to [/components/sensor/ble_rssi]({{< ref "/components/sensor/ble_rssi" >}}) but in contrast to that platform, this text
sensor sends out all raw BLE scan information and does not filter devices.

The data this sensor publishes is intended to be processed by the remote (for example an MQTT client) and sends
the data in JSON format.

{{< warning >}}
The BLE software stack on the ESP32 consumes a significant amount of RAM on the device.

**Crashes are likely to occur** if you include too many additional components in your device's
configuration. Memory-intensive components such as [/components/voice_assistant]({{< ref "/components/voice_assistant" >}}) and other
audio components are most likely to cause issues.

```yaml
```
# Example configuration entry
esp32_ble_tracker:

text_sensor:
    - platform: ble_scanner
        name: "BLE Devices Scanner"

{{< /warning >}}
Example json log:

```json
{
    "timestamp":1578254525,
    "address": "XX:XX:XX:XX:XX:XX",
    "rssi":"-80",
    "name":"MI Band 2"
}

```
## Configuration variables:

- All options from [Base Text Sensor Configuration]({{< ref "components/text_sensor/_index#config-text_sensor" >}}).

## See Also

- [/components/esp32_ble_tracker]({{< ref "/components/esp32_ble_tracker" >}})
- [/components/text_sensor/index]({{< ref "/components/text_sensor/index" >}})
- :apiref:`ble_scanner/ble_scanner.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/text_sensor/ble_scanner.md)
