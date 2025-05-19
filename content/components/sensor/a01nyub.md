---
description: "A01NYUB Waterproof Ultrasonic Sensor"
title: "A01NYUB Waterproof Ultrasonic Sensor"
---

{{< seo description="" image="" >}}

This sensor allows you to use A01NYUB waterproof ultrasonic sensor by DFRobot
([datasheet](https://wiki.dfrobot.com/A01NYUB%20Waterproof%20Ultrasonic%20Sensor%20SKU:%20SEN0313))
with ESPHome to measure distances. This sensor can measure
ranges between 28 centimeters and 750 centimeters with a resolution of 1 milimeter.

Since this sensor reads multiple times per second, [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}}) are highly recommended.

To use the sensor, first set up an [UART Bus]({{< ref "components/uart#uart" >}}) with a baud rate of 9600 and connect the sensor to the specified pin.

{{< img src="a01nyub-full.jpg" alt="Image" caption="A01NYUB Waterproof Ultrasonic Distance Sensor." width="50.0%" class="center" >}}

```yaml
# Example configuration entry
sensor:
  - platform: "a01nyub"
    name: "Distance"


```
## Configuration variables:

- **uart_id** (*Optional*, [UART bus]({{< ref "components/uart#uart" >}})): The ID of the [ID]({{< ref "guides/configuration-types#config-id" >}}) you wish to use for this sensor.
  Use this if you want to use multiple UART buses at once.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## See Also

- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [UART Bus]({{< ref "components/uart#uart" >}})
- :apiref:`a01nyub/a01nyub.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/a01nyub.md)
