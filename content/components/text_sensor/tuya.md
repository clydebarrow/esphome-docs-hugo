---
description: "Tuya Text Sensor"
title: "Tuya Text Sensor"
---

{{< seo description="" image="" >}}

The `tuya` text sensor platform creates a sensor from a tuya component
and requires [/components/tuya]({{< ref "/components/tuya" >}}) to be configured.

You can create the text sensor as follows:

```yaml
# Create a sensor
text_sensor:
  - platform: "tuya"
    name: "MyTextSensor"
    sensor_datapoint: 18

```
## Configuration variables:

- **sensor_datapoint** (**Required**, int): The datapoint id number of the sensor.
- All other options from [Base Text Sensor Configuration]({{< ref "components/text_sensor/_index#config-text_sensor" >}}).

## See Also

- [/components/tuya]({{< ref "/components/tuya" >}})
- [/components/text_sensor/index]({{< ref "/components/text_sensor/index" >}})
- :apiref:`tuya/text_sensor/tuya_text_sensor.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/text_sensor/tuya.md)
