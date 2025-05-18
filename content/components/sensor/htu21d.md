---
description: "HTU21D | Si7021 | SHT21 Temperature & Humidity Sensor"
title: "HTU21D | Si7021 | SHT21 Temperature & Humidity Sensor"
---

{{< seo description="" image="" >}}

The HTU21D Temperature & Humidity component allows you to use HTU21D, Si7021 and SHT21 sensors with
ESPHome. The [I²C Bus]({{< ref "components/i2c#i2c" >}}) is required to be set up in your configuration for this sensor to work.


Example sensors:

- ([Adafruit](https://www.adafruit.com/product/1899))

![HTU21D Temperature & Humidity Sensor.](../images/htu21d-full.jpg)
*HTU21D Temperature & Humidity Sensor.*


.. _Adafruit: https://learn.adafruit.com/adafruit-htu21d-f-temperature-humidity-sensor/overview

![.. code-block:: yaml](../images/temperature-humidity.png)
*.. code-block:: yaml*


    # Example configuration entry
    sensor:
      - platform: htu21d
        model: htu21d
        temperature:
          name: "Temperature"
        humidity:
          name: "Humidity"
        heater:
          name: "Heater"

## Configuration variables:

- **temperature** (*Optional*): The information for the temperature sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **humidity** (*Optional*): The information for the humidity sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **heater** (*Optional*): The information for the heater sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the sensor. Defaults to `60s`.

- **model** (*Optional*): Possible values are HTU21D, SI7021, SHT21. Defaults to HTU21D.

The heater may be enabled to help correct the reading; see the datasheet for more information.

## See Also

- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [absolute_humidity]({{< ref "absolute_humidity/" >}})
- [dht]({{< ref "dht/" >}})
- [dht12]({{< ref "dht12/" >}})
- [hdc1080]({{< ref "hdc1080/" >}})
- [sht3xd]({{< ref "sht3xd/" >}})
- :apiref:`htu21d/htu21d.h`
- [i2cdevlib](https://github.com/jrowberg/i2cdevlib) by [Jeff Rowberg](https://github.com/jrowberg)
- :ghedit:`Edit`
