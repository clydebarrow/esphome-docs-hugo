---
description: "A01NYUB Waterproof Ultrasonic Sensor"
title: "A01NYUB Waterproof Ultrasonic Sensor"
---

{{< seo description="" image="" >}}

This sensor allows you to use A01NYUB waterproof ultrasonic sensor by DFRobot
([datasheet](https://wiki.dfrobot.com/A01NYUB%20Waterproof%20Ultrasonic%20Sensor%20SKU:%20SEN0313))
with ESPHome to measure distances. This sensor can measure
ranges between 28 centimeters and 750 centimeters with a resolution of 1 milimeter.

Since this sensor reads multiple times per second, [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}}) are highly recommended.

To use the sensor, first set up an [uart]({{< ref "components/uart#uart" >}}) with a baud rate of 9600 and connect the sensor to the specified pin.

![A01NYUB Waterproof Ultrasonic Distance Sensor.](../images/a01nyub-full.jpg)
*A01NYUB Waterproof Ultrasonic Distance Sensor.*


```yaml
# Example configuration entry
sensor:
  - platform: "a01nyub"
    name: "Distance"


```
## Configuration variables:

- **uart_id** (*Optional*, [UART bus]({{< ref "components/uart#uart" >}})): The ID of the [config-id]({{< ref "guides/configuration-types#config-id" >}}) you wish to use for this sensor.
  Use this if you want to use multiple UART buses at once.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## See Also

- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [uart]({{< ref "components/uart#uart" >}})
- :apiref:`a01nyub/a01nyub.h`
- [Edit this page on GitHub](https://github.com/esphome/esphome-docs/blob/current/content/components/sensor/a01nyub.md)
