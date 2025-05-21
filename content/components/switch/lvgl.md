---
description: "LVGL Switch"
title: "LVGL Switch"
---

{{< seo description="" image="" >}}

The `lvgl` switch platform creates a switch from an LVGL widget
and requires {{< docref "/components/lvgl/index" "LVGL" >}} to be configured.

Supported widgets are [`checkbox`]({{< ref "components/lvgl/widgets#lvgl-widget-checkbox" >}}) (with `checkable` option enabled), [`switch`]({{< ref "components/lvgl/widgets#lvgl-widget-switch" >}}) and [`button`]({{< ref "components/lvgl/widgets#lvgl-widget-button" >}}). A single switch supports only a single widget; in other words, it's not possible to have multiple widgets associated with a single ESPHome switch component.

## Configuration variables:

- **widget** (**Required**): The ID of a supported widget configured in LVGL, which will reflect the state of the switch.
- All other variables from [Switch]({{< ref "components/switch/_index#config-switch" >}}).

Example:

```yaml
switch:
  - platform: lvgl
    widget: checkbox_id
    name: LVGL switch

```
## See Also
- {{< docref "/components/lvgl/index" "LVGL Main component" >}}
- [Button widget]({{< ref "components/lvgl/widgets#lvgl-widget-button" >}})
- [Switch widget]({{< ref "components/lvgl/widgets#lvgl-widget-switch" >}})
- [Checkbox widget]({{< ref "components/lvgl/widgets#lvgl-widget-checkbox" >}})
- {{< docref "/components/binary_sensor/lvgl" >}}
- {{< docref "/components/sensor/lvgl" >}}
- {{< docref "/components/number/lvgl" >}}
- {{< docref "/components/select/lvgl" >}}
- {{< docref "/components/light/lvgl" >}}
- {{< docref "/components/text/lvgl" >}}
- {{< docref "/components/text_sensor/lvgl" >}}
- {{< docref "/components/output/index" >}}
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/switch/lvgl.md)

