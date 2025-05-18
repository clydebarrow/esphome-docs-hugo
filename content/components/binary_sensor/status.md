---
description: "Status Binary Sensor"
title: "Status Binary Sensor"
---

{{< seo description="" image="" >}}

The Status Binary Sensor exposes the node state (if it's connected to via MQTT/native API)
for Home Assistant.

![.. code-block:: yaml](../images/status-ui.png)
*.. code-block:: yaml*


    # Example configuration entry
    binary_sensor:
      - platform: status
        name: "Living Room Status"

## Configuration variables:

- All options from [Binary Sensor]({{< ref "components/binary_sensor/_index#config-binary_sensor" >}}). (Inverted mode is not supported)

## See Also

- [/components/binary_sensor/index]({{< ref "/components/binary_sensor/index" >}})
- [/components/mqtt]({{< ref "/components/mqtt" >}})
- :apiref:`status/status_binary_sensor.h`
- [Edit this page on GitHub](https://github.com/esphome/esphome-docs/blob/current/content/components/binary_sensor/status.md)
