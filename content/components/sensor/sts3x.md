---
description: "STS3X Temperature Sensor"
title: "STS3X Temperature Sensor"
---

{{< seo description="" image="" >}}

The `sts3x` sensor platform Temperature sensor allows you to use your Sensirion STS30-DIS, STS31-DIS or STS35-DIS
([datasheet](https://sensirion.com/media/documents/1DA31AFD/61641F76/Sensirion_Temperature_Sensors_STS3x_Datasheet.pdf),
[Sensirion STS3x](https://www.sensirion.com/sts3x/)) sensors with
ESPHome. The [I²C Bus]({{< ref "components/i2c#i2c" >}}) is
required to be set up in your configuration for this sensor to work.

{{< img src="temperature.png" alt="Image" width="80.0%" class="center" >}}

```yaml
# Example configuration entry
sensor:
  - platform: sts3x
    name: "Living Room Temperature"
    address: 0x4A
    update_interval: 60s

```
## Configuration variables:

- **address** (*Optional*, int): Manually specify the I²C address of the sensor.
  Defaults to `0x4A`.
- **update_interval** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the
  sensor. Defaults to `60s`.
- All other options from [Base Sensor Configuration]({{< ref "components/sensor/_index#config-sensor" >}}).

## See Also

- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- {{< docref "dht/" >}}
- {{< docref "dht12/" >}}
- {{< docref "hdc1080/" >}}
- {{< docref "htu21d/" >}}
- {{< docref "sht3xd/" >}}
- :apiref:`sts3x/sts3x.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/sts3x.md)
