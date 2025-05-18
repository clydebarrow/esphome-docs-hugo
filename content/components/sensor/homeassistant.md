---
description: "Home Assistant Sensor"
title: "Home Assistant Sensor"
---

{{< seo description="" image="" >}}

The `homeassistant` sensor platform allows you to create sensors that import
states from your Home Assistant instance using the [native API ]({{< relref "/components/api" >}}).

{{< note >}}
Although you might not plan to *export* states from the node and you do not need an entity of the node
in Home Assistant, this component still requires you to register the node under Home Assistant. See:
:ref:`connecting-your-device-to-home-assistant`.

{{< /note >}}
```yaml
# Example configuration entry
sensor:
  - platform: homeassistant
    name: "Temperature Sensor From Home Assistant"
    entity_id: sensor.temperature_sensor

```
Entity state attributes can also be imported:

```yaml
# Example configuration entry
sensor:
  - platform: homeassistant
    id: current_temperature
    entity_id: climate.living_room
    attribute: current_temperature

```
{{< note >}}
This component is only for numeral states. If you want to import arbitrary text states
from Home Assistant, use the :doc:`Home Assistant Text Sensor </components/text_sensor/homeassistant>`.


{{< /note >}}
## Configuration variables:

- **entity_id** (**Required**, string): The entity ID to import from Home Assistant.
- **attribute** (*Optional*, string): The name of the state attribute to import from the
  specified entity. The entity state is used when this option is omitted.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).


{{< note >}}
The sensors implemented by this component are by default ``internal``, to avoid exporting them back to
Home Assistant. Should you still want to do that (eg. because you use ESPHome's very efficient filters
on them) you need to specifically configure ``internal: false``. Also, ``state_class``, ``unit_of_measurement``
are not inherited from the imported sensor so you need to set them manually.


{{< /note >}}
## See Also

- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [automation]({{< ref "automations/_index#automation" >}})
- :apiref:`homeassistant/sensor/homeassistant_sensor.h`
- [Edit this page on GitHub](https://github.com/esphome/esphome-docs/blob/current/content/components/sensor/homeassistant.md)
