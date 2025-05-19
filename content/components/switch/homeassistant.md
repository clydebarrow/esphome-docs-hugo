---
description: "Home Assistant Switch"
title: "Home Assistant Switch"
---

{{< seo description="" image="" >}}

The `homeassistant` Switch platform allows you to create Switch that **import**
states and allow **control** via your Home Assistant instance using the {{< docref "/components/api" "native API" >}}.

{{< note >}}
Although you might not plan to *export* states from the node and you do not need an entity of the node
in Home Assistant, this component still requires you to register the node under Home Assistant. See:
[Connecting your device to Home Assistant]({{< ref "guides/getting_started_hassio#connecting-your-device-to-home-assistant" >}}).

```yaml
```
# Example configuration entry
switch:
    - platform: homeassistant
        id: my_cool_switch_from_ha
        entity_id: switch.my_cool_switch

{{< /note >}}
## Configuration variables:

- **entity_id** (**Required**, string): The entity ID to import / control from Home Assistant.
- All other options from [Base Switch Configuration]({{< ref "components/switch/_index#config-switch" >}}).

## Supported domains

The following entity domains from Home Assistant are supported by this platform.

- `automation`
- `fan`
- `humidifier`
- `input_boolean`
- `light`
- `remote`
- `siren`
- `switch`

## See Also

- [Automation]({{< ref "automations/_index#automation" >}})
- :apiref:`homeassistant/switch/homeassistant_switch.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/switch/homeassistant.md)
