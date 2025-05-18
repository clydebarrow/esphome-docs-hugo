---
description: "LVGL Sensor"
title: "LVGL Sensor"
---

{{< seo description="" image="" >}}

The `lvgl` sensor platform creates a sensor component from an LVGL widget
and requires [LVGL ]({{< relref "/components/lvgl/index" >}}) to be configured.

Supported widgets are [``spinbox``]({{< ref "components/lvgl/widgets#lvgl-widget-spinbox" >}}), [``slider``]({{< ref "components/lvgl/widgets#lvgl-widget-slider" >}}), [``bar``]({{< ref "components/lvgl/widgets#lvgl-widget-bar" >}}) and [``arc``]({{< ref "components/lvgl/widgets#lvgl-widget-arc" >}}). A single sensor supports only a single widget; in other words, it's not possible to have multiple widgets associated with a single ESPHome sensor.

## Configuration variables:

- **widget** (**Required**): The ID of a supported widget configured in LVGL, which will reflect the state of the sensor.
- All other variables from [Base Sensor Configuration]({{< ref "components/sensor/_index#config-sensor" >}}).

Example:

```yaml
sensor:
  - platform: lvgl
    widget: slider_id
    name: LVGL Slider

```
{{< note >}}
Widget-specific actions (``lvgl.arc.update``, ``lvgl.bar.update``, ``lvgl.slider.update``, ``lvgl.spinbox.update``, ``lvgl.spinbox.decrement``, ``lvgl.spinbox.increment``) will trigger corresponding component updates to be sent to Home Assistant.

{{< /note >}}
## See Also
- [LVGL Main component ]({{< relref "/components/lvgl/index" >}})
- [``arc``]({{< ref "components/lvgl/widgets#lvgl-widget-arc" >}})
- [``bar``]({{< ref "components/lvgl/widgets#lvgl-widget-bar" >}})
- [``slider``]({{< ref "components/lvgl/widgets#lvgl-widget-slider" >}})
- [``spinbox``]({{< ref "components/lvgl/widgets#lvgl-widget-spinbox" >}})
- [/components/binary_sensor/lvgl]({{< ref "/components/binary_sensor/lvgl" >}})
- [/components/switch/lvgl]({{< ref "/components/switch/lvgl" >}})
- [/components/select/lvgl]({{< ref "/components/select/lvgl" >}})
- [/components/light/lvgl]({{< ref "/components/light/lvgl" >}})
- [/components/number/lvgl]({{< ref "/components/number/lvgl" >}})
- [/components/text/lvgl]({{< ref "/components/text/lvgl" >}})
- [/components/text_sensor/lvgl]({{< ref "/components/text_sensor/lvgl" >}})
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/lvgl.md)
