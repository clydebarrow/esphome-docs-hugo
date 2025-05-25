---
description: "LVGL Text Sensor"
title: "LVGL Text Sensor"
---

{{< seo description="" image="" >}}

The `lvgl` text sensor platform creates a Text Sensor from an LVGL textual widget
and requires {{< docref "/components/lvgl/index" "LVGL" >}} to be configured.

Supported widgets are [`label`]({{< ref "components/lvgl/widgets#lvgl-widget-label" >}}) and [`textarea`]({{< ref "components/lvgl/widgets#lvgl-widget-textarea" >}}). A single text sensor supports only a single widget; in other words, it's not possible to have multiple widgets associated with a single ESPHome text sensor component.

## Configuration variables:

- **widget** (**Required**): The ID of a `textarea` widget configured in LVGL, which will reflect the state of the text sensor.
- All other variables from [Text Sensor](components/text_sensor/_index#config-text_sensor).

Example:

```yaml
text_sensor:
  - platform: lvgl
    widget: textarea_id
    name: "Textarea 1 text"

```
{{< note >}}
Widget-specific actions (`lvgl.label.update`, `lvgl.textarea.update`) will trigger correspponding component updates to be sent to Home Assistant.

{{< /note >}}
## See Also
- {{< docref "/components/lvgl/index" "LVGL Main component" >}}
- [Label widget](components/lvgl/widgets#lvgl-widget-label)
- [Textarea widget](components/lvgl/widgets#lvgl-widget-textarea)
- {{< docref "/components/binary_sensor/lvgl" >}}
- {{< docref "/components/sensor/lvgl" >}}
- {{< docref "/components/number/lvgl" >}}
- {{< docref "/components/switch/lvgl" >}}
- {{< docref "/components/light/lvgl" >}}
- {{< docref "/components/select/lvgl" >}}
- {{< docref "/components/text/lvgl" >}}


