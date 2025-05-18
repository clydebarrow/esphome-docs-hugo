---
description: "SHT3X-D Temperature+Humidity Sensor"
title: "SHT3X-D Temperature+Humidity Sensor"
---

{{< seo description="" image="" >}}

The `sht3xd` sensor platform Temperature+Humidity sensor allows you to use your Sensirion SHT31-D/SHT3x
([datasheet](https://cdn-shop.adafruit.com/product-files/2857/Sensirion_Humidity_SHT3x_Datasheet_digital-767294.pdf),
[Adafruit`_ ) and SHT85 (`datasheet](https://sensirion.com/media/documents/4B40CEF3/640B2346/Sensirion_Humidity_Sensors_SHT85_Datasheet.pdf),
`Sensirion`_ ) sensors with Esphome.
The [I²C Bus]({{< ref "components/i2c#i2c" >}}) is required to be set up in your configuration for this sensor to work.

.. _Adafruit: https://www.adafruit.com/product/2857
.. _Sensirion: https://sensirion.com/products/catalog/SHT85/

![.. code-block:: yaml](../images/temperature-humidity.png)
*.. code-block:: yaml*


    # Example configuration entry
    sensor:
      - platform: sht3xd
        temperature:
          name: "Living Room Temperature"
        humidity:
          name: "Living Room Humidity"
        address: 0x44
        update_interval: 60s

## Configuration variables:

- **temperature** (*Optional*): The information for the temperature sensor.

  - All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **humidity** (*Optional*): The information for the humidity sensor.

  - All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **address** (*Optional*, int): Manually specify the I²C address of the sensor.
  Defaults to `0x44`. For SHT3x, an alternate address can be `0x45` while SHT85 supports only address `0x44`
- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the
  sensor. Defaults to `60s`.
- **heater_enabled** (*Optional*, bool): Turn on/off heater at boot.
  This may help provide [more accurate readings in condensing conditions](https://forum.arduino.cc/t/atmospheric-sensors-in-condensing-conditions/412167),
  but can also increase temperature readings and decrease humidity readings as a side effect.
  Defaults to `false`.

## I²C Configuration when using Higher I²C Frequencies

When using the **IDF framework** and **I²C frequencies greater than 50-100kHz**, the I²C configuration needs to include a **timeout** option.
On an ESP32, the Arduino framework has a default I²C timeout of 50ms whereas on IDF framework, the default timeout is 100us.
At these higher I²C frequencies, the default I²C timeout on IDF framework causes a "Communication with SHT3xD failed" error on setup.
A solution that has been tested on ESP32 at 800kHz, is to increase the I²C timeout to 10ms as per the following example.

```yaml
# Example I²C configuration
i2c:
  sda: 21
  scl: 22
  scan: true
  frequency: 800kHz
  timeout: 10ms

```
## See Also

- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [absolute_humidity]({{< ref "absolute_humidity/" >}})
- [dht]({{< ref "dht/" >}})
- [dht12]({{< ref "dht12/" >}})
- [hdc1080]({{< ref "hdc1080/" >}})
- [htu21d]({{< ref "htu21d/" >}})
- :apiref:`sht3xd/sht3xd.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/sht3xd.md)
