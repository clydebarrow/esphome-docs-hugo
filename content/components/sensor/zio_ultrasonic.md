---
description: "Zio Ultrasonic Distance Sensor"
title: "Zio Ultrasonic Distance Sensor"
---

{{< seo description="" image="" >}}

The Zio Ultrasonic Distance sensor allows you to use your compatible
([datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf),
[sparkfun](https://www.sparkfun.com/products/17777))
sensors with ESPHome. 

![Zio Ultrasonic Distance Sensor.](../images/zio_ultrasonic.jpg)
*Zio Ultrasonic Distance Sensor.*

    (Credit: [Sparkfun](https://www.sparkfun.com/products/17777), image cropped and compressed)

.. _Sparkfun: https://www.sparkfun.com/products/17777

The Zio Ultrasonic Distance Sensor is an ultrasonic distance sensor based on the HC-SR04 sensor. Unlike the [Ultrasonic Distance Sensor component ]({{< relref "/components/sensor/ultrasonic" >}}), measurements are read over the I²C bus.

To use the sensor, first set up an [I²C Bus]({{< ref "components/i2c#i2c" >}}) and connect the sensor to the specified pins.

```yaml
# Example configuration entry
sensor:
  - platform: zio_ultrasonic
    name: "Distance"
    update_interval: 60s

```
## Configuration variables:

- **address** (*Optional*, int): Manually specifiy the I²C address of the sensor. Defaults to `0x00`.
- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the sensor. Defaults to `60s`.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## See Also

- [Ultrasonic Sensor Component ]({{< relref "/components/sensor/ultrasonic" >}})
- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [template]({{< ref "template/" >}})
- [Edit this page on GitHub](https://github.com/esphome/esphome-docs/blob/current/content/components/sensor/zio_ultrasonic.md)
