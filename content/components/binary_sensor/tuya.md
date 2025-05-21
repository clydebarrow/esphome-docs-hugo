---
description: "Tuya Binary Sensor"
title: "Tuya Binary Sensor"
---

{{< seo description="" image="" >}}

The `tuya` binary sensor platform creates a binary sensor from a
tuya component and requires {{< docref "/components/tuya" >}} to be configured.

You can create the binary sensor as follows:

```yaml
# Create a binary sensor
binary_sensor:
  - platform: "tuya"
    name: "MyBinarySensor"
    sensor_datapoint: 1

```
## Configuration variables:

- **sensor_datapoint** (**Required**, int): The datapoint id number of the binary sensor.
- All other options from :ref:`Binary Sensor <config-binary_sensor>`.

## See Also

- {{< docref "/components/tuya" >}}
- {{< docref "/components/binary_sensor/index" >}}
- {{< apiref "tuya/binary_sensor/tuya_binary_sensor.h" "tuya/binary_sensor/tuya_binary_sensor.h" >}}
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/binary_sensor/tuya.md)

