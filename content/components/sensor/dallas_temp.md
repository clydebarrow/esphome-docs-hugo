---
description: "Dallas Temperature Sensor"
title: "Dallas Temperature Sensor"
---

{{< seo description="" image="" >}}

The `dallas_temp` component allows you to use 
[DS18B20](https://www.adafruit.com/product/374)
([datasheet](https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf))
and similar 1-Wire temperature sensors.  A [1-Wire bus]({{< ref "components/one_wire#one_wire" >}}) is
required to be set up in your configuration for this sensor to work.

```yaml
# Example configuration entry
sensor:
  - platform: dallas_temp
    address: 0x1234567812345628
    name: temperature
    update_interval: 120s

```
### Configuration variables:

- **address** (*Optional*, int): The address of the sensor. Required if there is more than one device on the bus.
- **resolution** (*Optional*, int): An optional resolution from 9 to 12. Higher means more accurate.
  Defaults to the maximum for most Dallas temperature sensors: 12.
- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The interval that the sensors should be checked.
  Defaults to 60 seconds.
- **one_wire_id** (*Optional*, [one_wire]({{< ref "components/one_wire#one_wire" >}})): The ID of the 1-Wire bus to use.
  Required if there is more than one bus.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## See Also

- [Arduino DallasTemperature library](https://github.com/milesburton/Arduino-Temperature-Control-Library)
  by [Miles Burton](https://github.com/milesburton)
- :apiref:`dallas_temp/dallas_temp.h`
- :ghedit:`Edit`
