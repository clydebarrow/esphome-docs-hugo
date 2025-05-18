---
description: "SHTCx Temperature+Humidity Sensors"
title: "SHTCx Temperature+Humidity Sensors"
---

{{< seo description="" image="" >}}

The `shtcx` sensor platform Temperature+Humidity sensor allows you to use your Sensirion SHTC1
([datasheet](https://sensirion.com/media/documents/21BF77EA/63A5A411/Datasheet_SHTC1.pdf),
[Sensirion STHC1](https://www.sensirion.com/en/environmental-sensors/humidity-sensors/digital-humidity-sensor-for-consumer-electronics-and-iot/)) and
the newer SHTC3
([datasheet](https://sensirion.com/media/documents/643F9C8E/63A5A436/Datasheet_SHTC3.pdf),
`SparkFun`_ ) sensors with
ESPHome. The [I²C Bus]({{< ref "components/i2c#i2c" >}}) is
required to be set up in your configuration for this sensor to work.

.. _SparkFun: https://www.sparkfun.com/products/15074

![.. code-block:: yaml](../images/temperature-humidity.png)
*.. code-block:: yaml*


    # Example configuration entry
    sensor:
      - platform: shtcx
        temperature:
          name: "Temperature"
        humidity:
          name: "Humidity"

## Configuration variables:

- **temperature** (*Optional*): The information for the temperature sensor.

  - All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **humidity** (*Optional*): The information for the humidity sensor.

  - All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **address** (*Optional*, int): Manually specify the I²C address of the sensor.
  Defaults to `0x70`.
- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the
  sensor. Defaults to `60s`.

## See Also

- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [absolute_humidity]({{< ref "absolute_humidity/" >}})
- [dht]({{< ref "dht/" >}})
- [dht12]({{< ref "dht12/" >}})
- [hdc1080]({{< ref "hdc1080/" >}})
- [htu21d]({{< ref "htu21d/" >}})
- [sht3xd]({{< ref "sht3xd/" >}})
- :apiref:`shtcx/shtcx.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/shtcx.md)
