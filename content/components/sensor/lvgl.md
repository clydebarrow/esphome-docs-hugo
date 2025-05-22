---
description: "LVGL Sensor"
title: "LVGL Sensor"
---

{{< seo description="" image="" >}}

The `lvgl` sensor platform creates a sensor component from an LVGL widget
and requires {{< docref "/components/lvgl" "LVGL" >}} to be configured.

Supported widgets are [`spinbox`]({{< ref "components/lvgl/widgets#lvgl-widget-spinbox" >}}), [`slider`]({{< ref "components/lvgl/widgets#lvgl-widget-slider" >}}), [`bar`]({{< ref "components/lvgl/widgets#lvgl-widget-bar" >}}) and [`arc`]({{< ref "components/lvgl/widgets#lvgl-widget-arc" >}}). A single sensor supports only a single widget; in other words, it's not possible to have multiple widgets associated with a single ESPHome sensor.

## Configuration variables:

- **widget** (**Required**): The ID of a supported widget configured in LVGL, which will reflect the state of the sensor.
- All other variables from :ref:`Sensor <config-sensor>`.

Example:

```yaml
sensor:
  - platform: lvgl
    widget: slider_id
    name: LVGL Slider

```
{{< note >}}
Widget-specific actions (`lvgl.arc.update`, `lvgl.bar.update`, `lvgl.slider.update`, `lvgl.spinbox.update`, `lvgl.spinbox.decrement`, `lvgl.spinbox.increment`) will trigger corresponding component updates to be sent to Home Assistant.

{{< /note >}}
## See Also
- {{< docref "/components/lvgl" "LVGL Main component" >}}
- :ref:`Arc widget <lvgl-widget-arc>`
- :ref:`Bar widget <lvgl-widget-bar>`
- :ref:`Slider widget <lvgl-widget-slider>`
- :ref:`Spinbox widget <lvgl-widget-spinbox>`
- {{< docref "/components/binary_sensor/lvgl" >}}
- {{< docref "/components/switch/lvgl" >}}
- {{< docref "/components/select/lvgl" >}}
- {{< docref "/components/light/lvgl" >}}
- {{< docref "/components/number/lvgl" >}}
- {{< docref "/components/text/lvgl" >}}
- {{< docref "/components/text_sensor/lvgl" >}}


