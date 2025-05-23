---
description: "Status Binary Sensor"
title: "Status Binary Sensor"
---

{{< seo description="" image="" >}}

The Status Binary Sensor exposes the node state (if it's connected to via MQTT/native API)
for Home Assistant.

{{< img src="status-ui.png" alt="Image" width="80.0%" class="center" >}}

```yaml
# Example configuration entry
binary_sensor:
  - platform: status
    name: "Living Room Status"

```
## Configuration variables:

- All options from [Binary Sensor]({{< ref "components/binary_sensor/_index#config-binary_sensor" >}}). (Inverted mode is not supported)

## See Also

- {{< docref "/components/binary_sensor" >}}
- {{< docref "/components/mqtt" >}}
- {{< apiref "status/status_binary_sensor.h" "status/status_binary_sensor.h" >}}


