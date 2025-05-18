---
description: "LVGL Switch"
title: "LVGL Switch"
---

{{< seo description="" image="" >}}

The `lvgl` switch platform creates a switch from an LVGL widget
and requires [LVGL ]({{< relref "/components/lvgl/index" >}}) to be configured.

Supported widgets are [lvgl-widget-checkbox]({{< ref "components/lvgl/widgets#lvgl-widget-checkbox" >}}) (with `checkable` option enabled), [lvgl-widget-switch]({{< ref "components/lvgl/widgets#lvgl-widget-switch" >}}) and [lvgl-widget-button]({{< ref "components/lvgl/widgets#lvgl-widget-button" >}}). A single switch supports only a single widget; in other words, it's not possible to have multiple widgets associated with a single ESPHome switch component.

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
- [LVGL Main component ]({{< relref "/components/lvgl/index" >}})
- [Button widget]({{< ref "components/lvgl/widgets#lvgl-widget-button" >}})
- [Switch widget]({{< ref "components/lvgl/widgets#lvgl-widget-switch" >}})
- [Checkbox widget]({{< ref "components/lvgl/widgets#lvgl-widget-checkbox" >}})
- [/components/binary_sensor/lvgl]({{< ref "/components/binary_sensor/lvgl" >}})
- [/components/sensor/lvgl]({{< ref "/components/sensor/lvgl" >}})
- [/components/number/lvgl]({{< ref "/components/number/lvgl" >}})
- [/components/select/lvgl]({{< ref "/components/select/lvgl" >}})
- [/components/light/lvgl]({{< ref "/components/light/lvgl" >}})
- [/components/text/lvgl]({{< ref "/components/text/lvgl" >}})
- [/components/text_sensor/lvgl]({{< ref "/components/text_sensor/lvgl" >}})
- [/components/output/index]({{< ref "/components/output/index" >}})
- [Edit this page on GitHub](https://github.com/esphome/esphome-docs/blob/current/content/components/switch/lvgl.md)
