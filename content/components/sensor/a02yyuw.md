---
description: "A02YYUW Waterproof Ultrasonic Sensor"
title: "A02YYUW Waterproof Ultrasonic Sensor"
---

{{< seo description="" image="" >}}

This sensor allows you to use A02YYUW waterproof ultrasonic sensor by DFRobot
([datasheet](https://wiki.dfrobot.com/_A02YYUW_Waterproof_Ultrasonic_Sensor_SKU_SEN0311))
with ESPHome to measure distances. This sensor can measure
ranges between 3 centimeters and 450 centimeters with a resolution of 1 milimeter.

Since this sensor reads multiple times per second, [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}}) are highly recommended.

To use the sensor, first set up an [uart]({{< ref "components/uart#uart" >}}) with a baud rate of 9600 and connect the sensor to the specified pin.

![A02YYUW Waterproof Ultrasonic Distance Sensor.](../images/a02yyuw-full.jpg)
*A02YYUW Waterproof Ultrasonic Distance Sensor.*


```yaml
# Example configuration entry
sensor:
  - platform: "a02yyuw"
    name: "Distance"


```
## Configuration variables:

- **uart_id** (*Optional*, [UART bus]({{< ref "components/uart#uart" >}})): The ID of the [config-id]({{< ref "guides/configuration-types#config-id" >}}) you wish to use for this sensor.
  Use this if you want to use multiple UART buses at once.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

{{< note >}}
`PWM and RS485 <https://www.dypcn.com/uploads/A02-Datasheet.pdf>`__ versions of the A02YYUW are not supported by this component.

{{< /note >}}
## See Also

- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [uart]({{< ref "components/uart#uart" >}})
- :apiref:`a02yyuw/a02yyuw.h`
- [Edit this page on GitHub](https://github.com/esphome/esphome-docs/blob/current/content/components/sensor/a02yyuw.md)
