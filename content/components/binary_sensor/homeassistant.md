---
description: "Home Assistant Binary Sensor"
title: "Home Assistant Binary Sensor"
---

{{< seo description="" image="" >}}

The `homeassistant` binary sensor platform allows you to create binary sensors that **import**
states from your Home Assistant instance using the [native API ]({{< relref "/components/api" >}}).

{{< note >}}
Although you might not plan to *export* states from the node and you do not need an entity of the node
in Home Assistant, this component still requires you to register the node under Home Assistant. See:
:ref:`connecting-your-device-to-home-assistant`.

{{< /note >}}
```yaml
# Example configuration entry
binary_sensor:
  - platform: homeassistant
    name: "Input Boolean From Home Assistant"
    entity_id: input_boolean.state_home

```
With Home Assistant 2021.6 or newer, entity state attributes can also be imported.

```yaml
# Example configuration entry
binary_sensor:
  - platform: homeassistant
    id: muted
    entity_id: media_player.mega_speakers
    attribute: is_volume_muted

```
## Configuration variables:

- **entity_id** (**Required**, string): The entity ID to import from Home Assistant.
- **attribute** (*Optional*, string): The name of the state attribute to import from the
  specified entity. The entity state is used when this option is omitted.
- All other options from [Base Binary Sensor Configuration]({{< ref "components/binary_sensor/_index#config-binary_sensor" >}}).

## See Also

- [Automation]({{< ref "automations/_index#automation" >}})
- :apiref:`homeassistant/binary_sensor/homeassistant_binary_sensor.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/binary_sensor/homeassistant.md)
