---
description: "WiFi Signal Sensor"
title: "WiFi Signal Sensor"
---

{{< seo description="" image="" >}}

The `wifi_signal` sensor platform allows you to read the signal
strength of the currently connected {{< docref "/components/wifi" "WiFi Access Point" >}}.

The sensor value is the ["Received signal strength indication"](https://en.wikipedia.org/wiki/Received_signal_strength_indication)
measured in decibel-milliwatts (dBm). These values are always negative and the closer they are to zero, the better the signal is.

{{< img src="wifi_signal-ui.png" alt="Image" width="80.0%" class="center" >}}

```yaml
# Example configuration entry
sensor:
  - platform: wifi_signal
    name: "WiFi Signal Sensor"
    update_interval: 60s

```
To additionally display signal strength in percentage use the [Copy Sensor]({{< ref "components/copy#copy-sensor" >}}) (it's not possible to add the same sensor twice, because it has a static `uniqueid` reported to Home Assistant):

```yaml
# Example configuration entry with 2 sensors and filter
sensor:
  - platform: wifi_signal # Reports the WiFi signal strength/RSSI in dB
    name: "WiFi Signal dB"
    id: wifi_signal_db
    update_interval: 60s
    entity_category: "diagnostic"

  - platform: copy # Reports the WiFi signal strength in %
    source_id: wifi_signal_db
    name: "WiFi Signal Percent"
    filters:
      - lambda: return min(max(2 * (x + 100.0), 0.0), 100.0);
    unit_of_measurement: "Signal %"
    entity_category: "diagnostic"
    device_class: ""

```
## Configuration variables:

- **update_interval** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval
  to check the sensor. Defaults to `60s`.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

{{< warning >}}
Signal strength readings are only available when WiFi is in station mode. Readings are not valid
if the device is acting as an access point without any station mode connection.

{{< /warning >}}
## See Also

- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- {{< docref "/components/wifi" >}}
- {{< docref "/components/text_sensor/wifi_info" >}}
- :apiref:`wifi_signal/wifi_signal_sensor.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/wifi_signal.md)

