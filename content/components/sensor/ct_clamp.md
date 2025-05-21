---
description: "CT Clamp Current Sensor"
title: "CT Clamp Current Sensor"
---

{{< seo description="" image="" >}}

The Current Transformer Clamp (`ct_clamp`) sensor allows you to hook up a CT Clamp to an analog
voltage sensor (like the {{< docref "adc/" "ADC sensor" >}}) and convert the readings to measured single phase AC current.

First, you need to set up a voltage sensor source ({{< docref "adc/" "ADC sensor" >}}, but for example also
{{< docref "ads1115/" "ADS1115" >}}) and pass it to the CT clamp sensor with the `sensor` option.

Please also see [this guide ](https://learn.openenergymonitor.org/electricity-monitoring/ct-sensors/introduction)
as an introduction to the working principle of CT clamp sensors and how to hook them up to your device.

{{< img src="ct_clamp-ui.png" alt="Image" width="80.0%" class="center" >}}

```yaml
# Example configuration entry
sensor:
  - platform: ct_clamp
    sensor: adc_sensor
    name: "Measured Current"
    update_interval: 60s

  # Example source sensor
  - platform: adc
    pin: A0
    id: adc_sensor

```
## Configuration variables:

- **sensor** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The source sensor to measure voltage values from.
- **sample_duration** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The time duration to sample the current clamp
  with. Higher values can increase accuracy. Defaults to `200ms` which would be 10 whole cycles on a 50Hz system.
- **update_interval** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval
  to check the sensor. Defaults to `60s`. The **update_interval** for `ct_clamp` has to be greater than **sample_duration**.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## Calibration

This sensor needs calibration to show correct values, for this you can use the
[calibrate_linear]({{< ref "#sensor-filter-calibrate_linear" >}}) sensor filter. First, hook up a known
current load like a lamp that uses a known amount of current.

Then switch it on and see what value the CT clamp sensor reports. For example in the configuration below
a 4.0 A device is showing a value of 0.1333 in the logs. Now go into your configuration file

```yaml
# Example configuration entry
sensor:
  - platform: ct_clamp
    sensor: adc_sensor
    name: "Measured Current"
    update_interval: 60s
    filters:
      - calibrate_linear:
          # Measured value of 0 maps to 0A
          - 0 -> 0
          # Known load: 4.0A
          # Value shown in logs: 0.1333A
          - 0.1333 -> 4.0

```
Recompile and upload, now your CT clamp sensor is calibrated!

## See Also

- [EMonLib ](https://github.com/openenergymonitor/EmonLib)
- [CT Clamp Guide ](https://learn.openenergymonitor.org/electricity-monitoring/ct-sensors/introduction)
- {{< docref "adc/" >}}
- {{< docref "ads1115/" >}}
- :apiref:`sensor/ct_clamp_sensor.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/ct_clamp.md)

