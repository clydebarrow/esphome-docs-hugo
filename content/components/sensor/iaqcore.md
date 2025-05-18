---
description: "AMS iAQ-Core Indoor Air Quality Sensor"
title: "AMS iAQ-Core Indoor Air Quality Sensor"
---

{{< seo description="" image="" >}}

The AMS iAQ-Core sensor allows you to use your
([datasheet](https://www.sciosense.com/wp-content/uploads/documents/iaQ-Core-Datasheet.pdf))
sensors with ESPHome.

![AMS iAQ-Core Indoor Air Quality Sensor.](../images/iaqcore.jpg)
*AMS iAQ-Core Indoor Air Quality Sensor.*


The iAQ-Core sensor module is used to measure VOC levels and provide CO2 equivalent and TVOC equivalent predictions. The data is available via I²C bus.

To use the sensor, first set up an [I²C Bus]({{< ref "components/i2c#i2c" >}}) and connect the sensor to the specified pins.

```yaml
# Example configuration entry
sensor:
  - platform: iaqcore
    address: 0x5A
    update_interval: 60s
    co2:
        name: "iAQ Core CO2 Sensor"
    tvoc:
        name: "iAQ Core TVOC Sensor"

```
## Configuration variables:

- **i2c_id** (*Optional*, ID): The id of the I²C Bus.
- **address** (*Optional*, int): Manually specifiy the I²C address of the sensor. Defaults to `0x5A`.
- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the sensor. Defaults to `60s`.
- **co2** (*Optional*): The configuration for the CO2 sensor. All options from
  [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).
- **tvoc** (*Optional*): The configuration for the TVOC sensor. All options from
  [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## See Also

- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [/components/sensor/index]({{< ref "/components/sensor/index" >}})
- :ghedit:`Edit`
