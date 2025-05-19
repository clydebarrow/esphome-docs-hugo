---
description: "LibreTiny Text Sensor"
title: "LibreTiny Text Sensor"
---

{{< seo description="" image="" >}}

The `libretiny` text sensor platform exposes various LibreTiny core
information via text sensors.

```yaml
# Example configuration entry
text_sensor:
  - platform: libretiny
    version:
      name: LibreTiny Version

```
## Configuration variables:

- **version** (*Optional*): Expose the version of LibreTiny core as a text sensor. All options from
  [Base Text Sensor Configuration]({{< ref "components/text_sensor/_index#config-text_sensor" >}}).


## See Also

- {{< docref "/components/libretiny" >}}
- :apiref:`libretiny/lt_component.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/text_sensor/libretiny.md)
