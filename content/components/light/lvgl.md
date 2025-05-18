---
description: "LVGL Light"
title: "LVGL Light"
---

{{< seo description="" image="" >}}

The `lvgl` light platform creates a light from an LVGL widget
and requires [LVGL ]({{< relref "/components/lvgl/index" >}}) to be configured.

Supported widget is [lvgl-widget-led]({{< ref "components/lvgl/widgets#lvgl-widget-led" >}}). A single light supports only a single widget; in other words, it's not possible to have multiple widgets associated with a single ESPHome light component.

## Configuration variables:

- **widget** (**Required**): The ID of a `led` widget configured in LVGL, which will reflect the state of the light.
- All other options from [light]({{< ref "components/light/_index#config-light" >}}).


Example:

```yaml
light:
  - platform: lvgl
    widget: led_id
    name: LVGL light

```
{{< note >}}
To have linear brightness control, ``gamma_correct`` of the light is set by default to ``0``.

{{< /note >}}
## See Also
- [LVGL Main component ]({{< relref "/components/lvgl/index" >}})
- [LED widget]({{< ref "components/lvgl/widgets#lvgl-widget-led" >}})
- [/components/binary_sensor/lvgl]({{< ref "/components/binary_sensor/lvgl" >}})
- [/components/sensor/lvgl]({{< ref "/components/sensor/lvgl" >}})
- [/components/number/lvgl]({{< ref "/components/number/lvgl" >}})
- [/components/switch/lvgl]({{< ref "/components/switch/lvgl" >}})
- [/components/select/lvgl]({{< ref "/components/select/lvgl" >}})
- [/components/text/lvgl]({{< ref "/components/text/lvgl" >}})
- [/components/text_sensor/lvgl]({{< ref "/components/text_sensor/lvgl" >}})
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/light/lvgl.md)
