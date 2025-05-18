---
description: "LVGL Text Sensor"
title: "LVGL Text Sensor"
---

{{< seo description="" image="" >}}

The `lvgl` text sensor platform creates a Text Sensor from an LVGL textual widget
and requires [LVGL ]({{< relref "/components/lvgl/index" >}}) to be configured.

Supported widgets are [``textarea``]({{< ref "components/lvgl/widgets#lvgl-widget-textarea" >}}) and [``label``]({{< ref "components/lvgl/widgets#lvgl-widget-label" >}}). A single text sensor supports only a single widget; in other words, it's not possible to have multiple widgets associated with a single ESPHome text sensor component.

## Configuration variables:

- **widget** (**Required**): The ID of a `textarea` widget configured in LVGL, which will reflect the state of the text sensor.
- All other variables from [Base Text Sensor Configuration]({{< ref "components/text_sensor/_index#config-text_sensor" >}}).

Example:

```yaml
text_sensor:
  - platform: lvgl
    widget: textarea_id
    name: "Textarea 1 text"

```
{{< note >}}
Widget-specific actions (``lvgl.label.update``, ``lvgl.textarea.update``) will trigger correspponding component updates to be sent to Home Assistant.

{{< /note >}}
## See Also
- [LVGL Main component ]({{< relref "/components/lvgl/index" >}})
- [``label``]({{< ref "components/lvgl/widgets#lvgl-widget-label" >}})
- [``textarea``]({{< ref "components/lvgl/widgets#lvgl-widget-textarea" >}})
- [/components/binary_sensor/lvgl]({{< ref "/components/binary_sensor/lvgl" >}})
- [/components/sensor/lvgl]({{< ref "/components/sensor/lvgl" >}})
- [/components/number/lvgl]({{< ref "/components/number/lvgl" >}})
- [/components/switch/lvgl]({{< ref "/components/switch/lvgl" >}})
- [/components/light/lvgl]({{< ref "/components/light/lvgl" >}})
- [/components/select/lvgl]({{< ref "/components/select/lvgl" >}})
- [/components/text/lvgl]({{< ref "/components/text/lvgl" >}})
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/text_sensor/lvgl.md)
