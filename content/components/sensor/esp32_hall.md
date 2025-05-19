---
description: "ESP32 Hall Sensor"
title: "ESP32 Hall Sensor"
---

{{< seo description="" image="" >}}

The `esp32_hall` sensor platform allows you to use the integrated
[hall effect sensor](https://en.wikipedia.org/wiki/Hall_effect_sensor) of the
ESP32 chip to measure the magnitude and direction of magnetic field around the
chip (with quite poor accuracy).

{{< warning >}}
Espressif has [removed support](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/migration-guides/release-5.x/5.0/peripherals.html?highlight=hall_sensor_read#api-changes)
for the ESP32's Hall sensor in IDF 5; for this reason, support for this component is
likely to be removed in a future release.

{{< /warning >}}
Please make sure that nothing is connected to pins `GPIO36` and `GPIO39` if this
component is enabled, as those pins are used for the internal low-noise amplifier used
by the hall sensor.

{{< img src="esp32_hall-ui.png" alt="Image" width="80.0%" class="center" >}}

```yaml
# Example configuration entry
sensor:
  - platform: esp32_hall
    name: "ESP32 Hall Sensor"
    update_interval: 60s

```
## Configuration variables:

- **update_interval** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval
  to check the sensor. Defaults to `60s`.
- All other options from [Base Sensor Configuration]({{< ref "components/sensor/_index#config-sensor" >}}).

{{< warning >}}
The values this sensor outputs were only calibrated with a few magnets and no real "truth" sensor.
Therefore the values could very well be off by orders of magnitude. Besides, this sensor should
only be used to detect sudden high changes in the magnetic field.

If you have a real magnetic field calibration setup and want to contribute your values to ESPHome,
please feel free to do so 😺.

{{< /warning >}}
## See Also

- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [adc]({{< ref "adc/" >}})
- [/components/esp32]({{< ref "/components/esp32" >}})
- :apiref:`esp32_hall/esp32_hall.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/esp32_hall.md)
