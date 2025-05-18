---
description: "Honeywell HumidIcon (I2C HIH series) Temperature & Humidity Sensor"
title: "Honeywell HumidIcon (I2C HIH series) Temperature & Humidity Sensor"
---

{{< seo description="" image="" >}}

Honeywell HumidIcon (I2C HIH series) Temperature & Humidity sensors with ESPHome ([website](https://sps.honeywell.com/us/en/products/advanced-sensing-technologies/healthcare-sensing/humidity-with-temperature-sensors),
[datasheet](https://prod-edam.honeywell.com/content/dam/honeywell-edam/sps/siot/en-us/products/sensors/humidity-with-temperature-sensors/common/documents/sps-siot-humidity-sensors-line-guide-009034-7-en-ciid-54931.pdf?download=false)).
The [I²C Bus]({{< ref "components/i2c#i2c" >}}) is required to be set up in your configuration for this sensor to work.

Example sensors:

```yaml
# Example configuration entry
sensor:
  - platform: honeywell_hih_i2c
    temperature:
      name: "Living Room Temperature"
    humidity:
      name: "Living Room Humidity"

```
## Configuration variables:

- **temperature** (**Required**): The information for the temperature sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **humidity** (**Required**): The information for the humidity sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the sensor. Defaults to `60s`.


## See Also

- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- :apiref:`honeywell_hih_i2c/honeywell_hih.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/honeywell_hih_i2c.md)
