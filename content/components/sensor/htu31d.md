---
description: "HTU31D Temperature & Humidity Sensor"
title: "HTU31D Temperature & Humidity Sensor"
---

{{< seo description="" image="" >}}

The HTU31D Temperature & Humidity component allows you to use HTU31D sensors with
ESPHome. The [I²C Bus]({{< ref "components/i2c#i2c" >}}) is required to be set up in your configuration for this sensor to work.


Example sensors:

- ([Adafruit](https://www.adafruit.com/product/4832))

![HTU31D Temperature & Humidity Sensor. Image by `Adafruit`_.](../images/htu31d.jpg)
*HTU31D Temperature & Humidity Sensor. Image by `Adafruit`_.*


.. _Adafruit: https://www.adafruit.com/product/4832

![.. code-block:: yaml](../images/temperature-humidity.png)
*.. code-block:: yaml*


    # Example configuration entry
    sensor:
      - platform: htu31d
        temperature:
          name: "Temperature"
        humidity:
          name: "Humidity"

## Configuration variables:

- **temperature** (*Optional*): The information for the temperature sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **humidity** (*Optional*): The information for the humidity sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the sensor. Defaults to `60s`.

## See Also

- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [absolute_humidity]({{< ref "absolute_humidity/" >}})
- [htu21d]({{< ref "htu21d/" >}})
- [dht]({{< ref "dht/" >}})
- [dht12]({{< ref "dht12/" >}})
- [hdc1080]({{< ref "hdc1080/" >}})
- [sht3xd]({{< ref "sht3xd/" >}})
- :apiref:`htu31d/htu31d.h`
- [i2cdevlib](https://github.com/jrowberg/i2cdevlib) by [Jeff Rowberg](https://github.com/jrowberg)
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/htu31d.md)
