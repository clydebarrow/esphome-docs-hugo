---
description: "Switch Binary Sensor"
title: "Switch Binary Sensor"
---

{{< seo description="" image="" >}}

The Switch Binary Sensor platform allows you to view the state of any switch component as a
read-only binary sensor.

```yaml
# Example configuration entry
binary_sensor:
  - platform: switch
    name: "Output state"
    source_id: relay1

switch:
  - platform: gpio
    id: relay1
    pin: GPIOXX

```
## Configuration variables:

- **source_id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The source switch to observe.
- All other options from [Binary Sensor]({{< ref "components/binary_sensor/_index#config-binary_sensor" >}}).

## See Also

- {{< docref "/components/binary_sensor/index" >}}
- :apiref:`switch/binary_sensor/switch_binary_sensor.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/binary_sensor/switch.md)

