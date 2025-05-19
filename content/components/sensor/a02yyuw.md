---
description: "A02YYUW Waterproof Ultrasonic Sensor"
title: "A02YYUW Waterproof Ultrasonic Sensor"
---

{{< seo description="" image="" >}}

This sensor allows you to use A02YYUW waterproof ultrasonic sensor by DFRobot
([datasheet](https://wiki.dfrobot.com/_A02YYUW_Waterproof_Ultrasonic_Sensor_SKU_SEN0311))
with ESPHome to measure distances. This sensor can measure
ranges between 3 centimeters and 450 centimeters with a resolution of 1 milimeter.

Since this sensor reads multiple times per second, [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}}) are highly recommended.

To use the sensor, first set up an [UART Bus]({{< ref "components/uart#uart" >}}) with a baud rate of 9600 and connect the sensor to the specified pin.

{{< img src="a02yyuw-full.jpg" alt="Image" caption="A02YYUW Waterproof Ultrasonic Distance Sensor." width="50.0%" class="center" >}}

```yaml
# Example configuration entry
sensor:
  - platform: "a02yyuw"
    name: "Distance"


```
## Configuration variables:

- **uart_id** (*Optional*, [UART Bus]({{< ref "components/uart#uart" >}})): The ID of the [ID]({{< ref "guides/configuration-types#config-id" >}}) you wish to use for this sensor.
  Use this if you want to use multiple UART buses at once.
- All other options from [Base Sensor Configuration]({{< ref "components/sensor/_index#config-sensor" >}}).

{{< note >}}
[PWM and RS485](https://www.dypcn.com/uploads/A02-Datasheet.pdf) versions of the A02YYUW are not supported by this component.

{{< /note >}}
## See Also

- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [UART Bus]({{< ref "components/uart#uart" >}})
- :apiref:`a02yyuw/a02yyuw.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/a02yyuw.md)
