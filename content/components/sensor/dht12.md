---
description: "DHT12 Temperature+Humidity Sensor"
title: "DHT12 Temperature+Humidity Sensor"
---

{{< seo description="" image="" >}}

The `dht12` Temperature+Humidity sensor allows you to use your DHT12
([datasheet](http://www.robototehnika.ru/file/DHT12.pdf),
`electrodragon`_) I²C-based sensor with ESPHome. This sensor is also called AM2320 by some sellers.

{{< img src="dht12-full.jpg" alt="Image" caption="DHT12 Temperature & Humidity Sensor." width="50.0%" class="center" >}}

[electrodragon](http://www.electrodragon.com/product/dht12/)

{{< img src="temperature-humidity.png" alt="Image" width="80.0%" class="center" >}}

```yaml
# Example configuration entry
sensor:
  - platform: dht12
    temperature:
      name: "Living Room Temperature"
    humidity:
      name: "Living Room Humidity"
    update_interval: 60s

```
## Configuration variables:

- **temperature** (**Required**): The information for the temperature sensor.

  - All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **humidity** (**Required**): The information for the humidity sensor

  - All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **update_interval** (*Optional*, :ref:`config-time`): The interval to check the sensor. Defaults to `60s`.


## See Also

- :ref:`sensor-filters`
- {{< docref "absolute_humidity/" >}}
- {{< docref "dht/" >}}
- {{< docref "hdc1080/" >}}
- {{< docref "htu21d/" >}}
- {{< docref "sht3xd/" >}}
- :apiref:`dht12/dht12.h`
- [DHT12 Library](https://github.com/dplasa/dht) by [Daniel Plasa](https://github.com/dplasa)
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/dht12.md)

