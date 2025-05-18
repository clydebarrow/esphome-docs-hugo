---
description: "Tuya Sensor"
title: "Tuya Sensor"
---

{{< seo description="" image="" >}}

The `tuya` sensor platform creates a sensor from a tuya component
and requires [/components/tuya]({{< ref "/components/tuya" >}}) to be configured.

```text
[13:46:01][C][tuya:023]: Tuya:
[13:46:01][C][tuya:032]:   Datapoint 1: switch (value: OFF)
[13:46:01][C][tuya:032]:   Datapoint 2: switch (value: OFF)
[13:46:01][C][tuya:034]:   Datapoint 3: int value (value: 19)
[13:46:01][C][tuya:034]:   Datapoint 4: int value (value: 17)
[13:46:01][C][tuya:034]:   Datapoint 5: int value (value: 0)
[13:46:01][C][tuya:036]:   Datapoint 7: enum (value: 1)
[13:46:01][C][tuya:046]:   Product: '{"p":"ynjanlglr4qa6dxf","v":"1.0.0","m":0}'

```
On this controller, the datapoint 5 represents the countdown timer in minutes
which is what we are interested in reading using this platform.

Based on this, you can create the sensor as follows:

```yaml
# Create a sensor
sensor:
  - platform: "tuya"
    name: "MySensor"
    sensor_datapoint: 5

```
## Configuration variables:

- **sensor_datapoint** (**Required**, int): The datapoint id number of the sensor.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## See Also

- [/components/tuya]({{< ref "/components/tuya" >}})
- [/components/sensor/index]({{< ref "/components/sensor/index" >}})
- :apiref:`tuya/sensor/tuya_sensor.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/tuya.md)
