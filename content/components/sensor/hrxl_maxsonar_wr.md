---
description: "HRXL/XL MaxSonar WR Series"
title: "HRXL/XL MaxSonar WR Series"
---

{{< seo description="" image="" >}}

This sensor allows you to use HRXL MaxSonar WR series ultrasonic sensors by MaxBotix
([datasheet](https://www.maxbotix.com/documents/HRXL-MaxSonar-WR_Datasheet.pdf))
or the XL MaxSonar WR series
([datasheet](https://www.maxbotix.com/documents/XL-MaxSonar-WR_Datasheet.pdf))
with ESPHome to measure distances. Depending on the model, these sensors can measure
in a range between 30 centimeters and 10 meters.

This sensor platform works with the **TTL versions** of those sensors and expects the
sensor's TTL pin to be wired to one of the ESP's input pins. Since these sensors read
multiple times per second, filtering is highly recommended.


{{< img src="hrxl_maxsonar_wr-full.jpg" alt="Image" caption="MB7388 HRXL-MaxSonar-WRMLT Ultrasonic Distance Sensor." width="50.0%" class="center" >}}

```yaml
# Example configuration entry
sensor:
  - platform: "hrxl_maxsonar_wr"
    name: "Rainwater Tank"


```
## Configuration variables:

- All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

Advanced options:

- **uart_id** (*Optional*, [UART bus]({{< ref "components/uart#uart" >}})): The ID of the [ID]({{< ref "guides/configuration-types#config-id" >}}) you wish to use for this sensor.
  Use this if you want to use multiple UART buses at once.


## See Also

- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [UART Bus]({{< ref "components/uart#uart" >}})
- {{< docref "template/" >}}
- :apiref:`hrxl_maxsonar_wr/hrxl_maxsonar_wr.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/hrxl_maxsonar_wr.md)
