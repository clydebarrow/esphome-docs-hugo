---
description: "LVGL Number"
title: "LVGL Number"
---

{{< seo description="" image="" >}}

The `lvgl` number platform creates a number component from an LVGL widget
and requires [LVGL ]({{< relref "/components/lvgl/index" >}}) to be configured.

Supported widgets are [lvgl-widget-spinbox]({{< ref "components/lvgl/widgets#lvgl-widget-spinbox" >}}), [lvgl-widget-slider]({{< ref "components/lvgl/widgets#lvgl-widget-slider" >}}), [lvgl-widget-bar]({{< ref "components/lvgl/widgets#lvgl-widget-bar" >}}) and [lvgl-widget-arc]({{< ref "components/lvgl/widgets#lvgl-widget-arc" >}}). A single number supports only a single widget; in other words, it's not possible to have multiple widgets associated with a single ESPHome number component.

## Configuration variables:

- **widget** (**Required**): The ID of a supported widget configured in LVGL, which will reflect the state of the number.
- **animated** (*Optional*, boolean): Whether to set the value of the widget with an animation (if supported by the widget). Defaults to `true`.
- **update_on_release** (*Optional*, boolean): By default the number will publish a new value each time the value of the associated widget changes. If this option is `true` then the value will only be published when touch is released.
- **restore_value**: (*Optional*, bool) Restore the value of the number from non-volatile memory when the device is restarted. Defaults to `false`.
- All other variables from [Number]({{< ref "components/number/_index#config-number" >}}).

Example:

```yaml
number:
  - platform: lvgl
    widget: slider_id
    name: LVGL Slider

```
{{< note >}}
Widget-specific actions (``lvgl.arc.update``, ``lvgl.bar.update``, ``lvgl.slider.update``, ``lvgl.spinbox.update``, ``lvgl.spinbox.decrement``, ``lvgl.spinbox.increment``) will trigger correspponding component updates to be sent to Home Assistant.

{{< /note >}}
## See Also
- [LVGL Main component ]({{< relref "/components/lvgl/index" >}})
- [Arc widget]({{< ref "components/lvgl/widgets#lvgl-widget-arc" >}})
- [Bar widget]({{< ref "components/lvgl/widgets#lvgl-widget-bar" >}})
- [Slider widget]({{< ref "components/lvgl/widgets#lvgl-widget-slider" >}})
- [Spinbox widget]({{< ref "components/lvgl/widgets#lvgl-widget-spinbox" >}})
- [/components/binary_sensor/lvgl]({{< ref "/components/binary_sensor/lvgl" >}})
- [/components/sensor/lvgl]({{< ref "/components/sensor/lvgl" >}})
- [/components/switch/lvgl]({{< ref "/components/switch/lvgl" >}})
- [/components/select/lvgl]({{< ref "/components/select/lvgl" >}})
- [/components/light/lvgl]({{< ref "/components/light/lvgl" >}})
- [/components/text/lvgl]({{< ref "/components/text/lvgl" >}})
- [/components/text_sensor/lvgl]({{< ref "/components/text_sensor/lvgl" >}})
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/number/lvgl.md)
