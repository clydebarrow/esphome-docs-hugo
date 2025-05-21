---
description: "LVGL Text"
title: "LVGL Text"
---

{{< seo description="" image="" >}}

The `lvgl` text platform creates an editable text component from an LVGL textual widget and requires {{< docref "/components/lvgl/index" "LVGL" >}} to be configured.

Supported widgets are :ref:`lvgl-widget-label` and :ref:`lvgl-widget-textarea`. A single text supports only a single widget; in other words, it's not possible to have multiple widgets associated with a single ESPHome text component.

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
Widget-specific actions (`lvgl.label.update`, `lvgl.textarea.update`) will trigger correspponding component updates to be sent to Home Assistant.

{{< /note >}}
## See Also
- {{< docref "/components/lvgl/index" "LVGL Main component" >}}
- [Label widget]({{< ref "components/lvgl/widgets#lvgl-widget-label" >}})
- [Textarea widget]({{< ref "components/lvgl/widgets#lvgl-widget-textarea" >}})
- {{< docref "/components/binary_sensor/lvgl" >}}
- {{< docref "/components/sensor/lvgl" >}}
- {{< docref "/components/number/lvgl" >}}
- {{< docref "/components/switch/lvgl" >}}
- {{< docref "/components/light/lvgl" >}}
- {{< docref "/components/select/lvgl" >}}
- {{< docref "/components/text_sensor/lvgl" >}}
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/text/lvgl.md)

