---
description: "SDP3x / SDP800 Series Differential Pressure Sensor"
title: "SDP3x / SDP800 Series Differential Pressure Sensor"
---

{{< seo description="" image="" >}}

The SDP3x Differential Pressure sensor allows you to use your SDP3x
([datasheet](https://sensirion.com/media/documents/4D045D69/6375F34F/DP_DS_SDP3x_digital_D1.pdf),
[sparkfun](https://www.sparkfun.com/products/17874)) or SDP800 Series ([datasheet](https://sensirion.com/media/documents/90500156/6167E43B/Sensirion_Differential_Pressure_Datasheet_SDP8xx_Digital.pdf))
sensors with ESPHome.

{{< img src="sdp31.jpg" alt="Image" caption="SDP31 Differential Pressure Sensor. (Credit: [Sparkfun](https://www.sparkfun.com/products/17874), image cropped and compressed)" width="30.0%" class="center" >}}

[Sparkfun](https://www.sparkfun.com/products/17874)

To use the sensor, set up an [I²C Bus]({{< ref "components/i2c#i2c" >}}) and connect the sensor to the specified pins.

```yaml
# Example configuration entry
- platform: sdp3x
  name: "HVAC Filter Pressure drop"
  id: filter_pressure

```
## Configuration variables:

- **address** (*Optional*, int): The I²C address of the sensor. Defaults to `0x21`.
- **measurement_mode** (*Optional*): The measurement mode of the sensor. Valid options are `differential_pressure` and `mass_flow`. Defaults to `differential_pressure`.
- **update_interval** (*Optional*, :ref:`config-time`): The interval to check the sensor. Defaults to `60s`.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## See Also

- :ref:`sensor-filters`
- :apiref:`sdp3x/sdp3x.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/sdp3x.md)

