---
description: "DHT12 Temperature+Humidity Sensor"
title: "DHT12 Temperature+Humidity Sensor"
---

{{< seo description="" image="" >}}

The `dht12` Temperature+Humidity sensor allows you to use your DHT12
([datasheet](http://www.robototehnika.ru/file/DHT12.pdf),
`electrodragon`_) I²C-based sensor with ESPHome. This sensor is also called AM2320 by some sellers.

![DHT12 Temperature & Humidity Sensor.](../images/dht12-full.jpg)
*DHT12 Temperature & Humidity Sensor.*


.. _electrodragon: http://www.electrodragon.com/product/dht12/

![.. code-block:: yaml](../images/temperature-humidity.png)
*.. code-block:: yaml*


    # Example configuration entry
    sensor:
      - platform: dht12
        temperature:
          name: "Living Room Temperature"
        humidity:
          name: "Living Room Humidity"
        update_interval: 60s

## Configuration variables:

- **temperature** (**Required**): The information for the temperature sensor.

  - All options from [Base Sensor Configuration]({{< ref "components/sensor/_index#config-sensor" >}}).

- **humidity** (**Required**): The information for the humidity sensor

  - All options from [Base Sensor Configuration]({{< ref "components/sensor/_index#config-sensor" >}}).

- **update_interval** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the sensor. Defaults to `60s`.


## See Also

- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [absolute_humidity]({{< ref "absolute_humidity/" >}})
- [dht]({{< ref "dht/" >}})
- [hdc1080]({{< ref "hdc1080/" >}})
- [htu21d]({{< ref "htu21d/" >}})
- [sht3xd]({{< ref "sht3xd/" >}})
- :apiref:`dht12/dht12.h`
- [DHT12 Library](https://github.com/dplasa/dht) by [Daniel Plasa](https://github.com/dplasa)
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/dht12.md)
