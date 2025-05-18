---
description: "LVGL Binary Sensor"
title: "LVGL Binary Sensor"
---

{{< seo description="" image="" >}}

The `lvgl` binary sensor platform creates a binary sensor from an LVGL widget
and requires [LVGL ]({{< relref "/components/lvgl/index" >}}) to be configured.

Supported widget is [lvgl-widget-button]({{< ref "components/lvgl/widgets#lvgl-widget-button" >}}). A single binary sensor supports only a single widget; in other words, it's not possible to have multiple widgets associated with a single ESPHome binary sensor component.

## Configuration variables:

- **widget** (**Required**): The ID of a supported widget configured in LVGL, which will reflect the state of the binary sensor.
- All other variables from [Binary Sensor]({{< ref "components/binary_sensor/_index#config-binary_sensor" >}}).

Example:

```yaml
binary_sensor:
  - platform: lvgl
    widget: btn_id
    name: LVGL push button

```
## See Also
- [LVGL Main component ]({{< relref "/components/lvgl/index" >}})
- [Button widget]({{< ref "components/lvgl/widgets#lvgl-widget-button" >}})
- [/components/sensor/lvgl]({{< ref "/components/sensor/lvgl" >}})
- [/components/number/lvgl]({{< ref "/components/number/lvgl" >}})
- [/components/switch/lvgl]({{< ref "/components/switch/lvgl" >}})
- [/components/select/lvgl]({{< ref "/components/select/lvgl" >}})
- [/components/light/lvgl]({{< ref "/components/light/lvgl" >}})
- [/components/text/lvgl]({{< ref "/components/text/lvgl" >}})
- [/components/text_sensor/lvgl]({{< ref "/components/text_sensor/lvgl" >}})
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/binary_sensor/lvgl.md)
