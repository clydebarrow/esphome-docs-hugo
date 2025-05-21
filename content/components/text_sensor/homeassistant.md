---
description: "Home Assistant Text Sensor"
title: "Home Assistant Text Sensor"
---

{{< seo description="" image="" >}}

The `homeassistant` text sensor platform allows you to create sensors that import
states from your Home Assistant instance using the {{< docref "/components/api" "native API" >}}.

{{< note >}}
Although you might not plan to *export* states from the node and you do not need an entity of the node
in Home Assistant, this component still requires you to register the node under Home Assistant. See:
[Connecting your device to Home Assistant]({{< ref "guides/getting_started_hassio#connecting-your-device-to-home-assistant" >}}).

{{< /note >}}
```yaml
# Example configuration entry
text_sensor:
  - platform: homeassistant
    id: weather_fom_ha
    entity_id: sensor.weather_forecast

```
Entity state attributes can also be imported:

```yaml
# Example configuration entry
text_sensor:
  - platform: homeassistant
    id: effect
    entity_id: light.led_strip
    attribute: effect

```
## Configuration variables:

- **entity_id** (**Required**, string): The entity ID to import from Home Assistant.
- **attribute** (*Optional*, string): The name of the state attribute to import from the
  specified entity. The entity state is used when this option is omitted.
- All other options from :ref:`Text Sensor <config-text_sensor>`.

## See Also

- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [Automation]({{< ref "automations/_index#automation" >}})
- {{< apiref "homeassistant/text_sensor/homeassistant_text_sensor.h" "homeassistant/text_sensor/homeassistant_text_sensor.h" >}}
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/text_sensor/homeassistant.md)

