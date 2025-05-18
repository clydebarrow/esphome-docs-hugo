---
description: "LVGL Text"
title: "LVGL Text"
---

{{< seo description="" image="" >}}

The `lvgl` text platform creates an editable text component from an LVGL textual widget and requires [LVGL ]({{< relref "/components/lvgl/index" >}}) to be configured.

Supported widgets are [lvgl-widget-textarea]({{< ref "components/lvgl/widgets#lvgl-widget-textarea" >}}) and [lvgl-widget-label]({{< ref "components/lvgl/widgets#lvgl-widget-label" >}}). A single text supports only a single widget; in other words, it's not possible to have multiple widgets associated with a single ESPHome text component.

## Configuration variables:

- **widget** (**Required**): The ID of a `textarea` widget configured in LVGL, which will reflect the state of the text component.
- All other variables from [Text]({{< ref "components/text/_index#config-text" >}}).

Example:

```yaml
text:
  - platform: lvgl
    widget: textarea_id
    name: "Textarea 1 text"

```
{{< note >}}
Widget-specific actions (``lvgl.label.update``, ``lvgl.textarea.update``) will trigger correspponding component updates to be sent to Home Assistant.

{{< /note >}}
## See Also
- [LVGL Main component ]({{< relref "/components/lvgl/index" >}})
- [Label widget]({{< ref "components/lvgl/widgets#lvgl-widget-label" >}})
- [Textarea widget]({{< ref "components/lvgl/widgets#lvgl-widget-textarea" >}})
- [/components/binary_sensor/lvgl]({{< ref "/components/binary_sensor/lvgl" >}})
- [/components/sensor/lvgl]({{< ref "/components/sensor/lvgl" >}})
- [/components/number/lvgl]({{< ref "/components/number/lvgl" >}})
- [/components/switch/lvgl]({{< ref "/components/switch/lvgl" >}})
- [/components/light/lvgl]({{< ref "/components/light/lvgl" >}})
- [/components/select/lvgl]({{< ref "/components/select/lvgl" >}})
- [/components/text_sensor/lvgl]({{< ref "/components/text_sensor/lvgl" >}})
- :ghedit:`Edit`
