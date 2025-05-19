---
description: "M5Stack KMeterISO I2C K-Type probe temperature sensor"
title: "M5Stack KMeterISO I2C K-Type probe temperature sensor"
---

{{< seo description="" image="" >}}

The `kmeteriso` sensor platform allows you to use your KMeterISO
([product](https://docs.m5stack.com/en/unit/KMeterISO%20Unit),
`M5Stack`_) K-Type thermocouple temperature sensor with ESPHome.
The [I²C]({{< ref "components/i2c#i2c" >}}) is required to be set up in your configuration
for this sensor to work.

{{< img src="kmeteriso.jpg" alt="Image" caption="M5Stack KMeterISO temperature sensor." width="50.0%" class="center" >}}

.. _M5Stack: https://docs.m5stack.com/en/unit/KMeterISO%20Unit

```yaml
# Example configuration entry
sensor:
- platform: kmeteriso
  temperature:
    name: Temperature
  internal_temperature:
    name: Internal temperature

```
## Configuration variables:

- **temperature** (*Optional*): The information for the temperature sensor. All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).
- **internal_temperature** (*Optional*): The information for the temperature sensor inside the probe. All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).
- **update_interval** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the
  sensor. Defaults to `5s`.

## See Also

- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- {{< docref "absolute_humidity/" >}}
- :apiref:`kmeteriso/kmeteriso.h`
- [M5Stack Unit code](https://github.com/m5stack/M5Unit-KMeterISO) by [M5Stack](https://m5stack.com/)
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/kmeteriso.md)
