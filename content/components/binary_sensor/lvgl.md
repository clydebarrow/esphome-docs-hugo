---
description: "LVGL Binary Sensor"
title: "LVGL Binary Sensor"
---

{{< seo description="" image="" >}}

The `lvgl` binary sensor platform creates a binary sensor from an LVGL widget
and requires {{< docref "/components/lvgl" "LVGL" >}} to be configured.

Supported widget is [`button`]({{< ref "components/lvgl/widgets#lvgl-widget-button" >}}). A single binary sensor supports only a single widget; in other words, it's not possible to have multiple widgets associated with a single ESPHome binary sensor component.

## Configuration variables:

- **widget** (**Required**): The ID of a supported widget configured in LVGL, which will reflect the state of the binary sensor.
- All other variables from :ref:`Binary Sensor <config-binary_sensor>`.

Example:

```yaml
binary_sensor:
  - platform: lvgl
    widget: btn_id
    name: LVGL push button

```
## See Also
- {{< docref "/components/lvgl" "LVGL Main component" >}}
- :ref:`Button widget <lvgl-widget-button>`
- {{< docref "/components/sensor/lvgl" >}}
- {{< docref "/components/number/lvgl" >}}
- {{< docref "/components/switch/lvgl" >}}
- {{< docref "/components/select/lvgl" >}}
- {{< docref "/components/light/lvgl" >}}
- {{< docref "/components/text/lvgl" >}}
- {{< docref "/components/text_sensor/lvgl" >}}


