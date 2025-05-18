---
description: "LVGL Select"
title: "LVGL Select"
---

{{< seo description="" image="" >}}

The `lvgl` select platform creates a select from an LVGL widget
and requires [LVGL ]({{< relref "/components/lvgl/index" >}}) to be configured.

Supported widgets are [lvgl-widget-roller]({{< ref "components/lvgl/widgets#lvgl-widget-roller" >}}) and [lvgl-widget-dropdown]({{< ref "components/lvgl/widgets#lvgl-widget-dropdown" >}}). A single select supports only a single widget; in other words, it's not possible to have multiple widgets associated with a single ESPHome select component.

## Configuration variables:

- **widget** (**Required**): The ID of a supported widget configured in LVGL, which will reflect the state of the select.
- **restore_value**: (*Optional*, bool) Restore the value of the select from non-volatile memory when the device is restarted. Defaults to `false`.
- All other variables from [Select]({{< ref "components/select/_index#config-select" >}}).

Example:

```yaml
select:
  - platform: lvgl
    widget: dropdown_id
    name: LVGL Dropdown

```
{{< note >}}
Widget-specific actions (``lvgl.dropdown.update``, ``lvgl.roller.update``) will trigger correspponding component updates to be sent to Home Assistant.

{{< /note >}}
## See Also
- [LVGL Main component ]({{< relref "/components/lvgl/index" >}})
- [Roller widget]({{< ref "components/lvgl/widgets#lvgl-widget-roller" >}})
- [Dropdown widget]({{< ref "components/lvgl/widgets#lvgl-widget-dropdown" >}})
- [/components/binary_sensor/lvgl]({{< ref "/components/binary_sensor/lvgl" >}})
- [/components/sensor/lvgl]({{< ref "/components/sensor/lvgl" >}})
- [/components/number/lvgl]({{< ref "/components/number/lvgl" >}})
- [/components/switch/lvgl]({{< ref "/components/switch/lvgl" >}})
- [/components/light/lvgl]({{< ref "/components/light/lvgl" >}})
- [/components/text/lvgl]({{< ref "/components/text/lvgl" >}})
- [/components/text_sensor/lvgl]({{< ref "/components/text_sensor/lvgl" >}})
- :ghedit:`Edit`
