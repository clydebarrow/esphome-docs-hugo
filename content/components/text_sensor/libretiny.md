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
  [Text Sensor]({{< ref "components/text_sensor/_index#config-text_sensor" >}}).


## See Also

- [/components/libretiny]({{< ref "/components/libretiny" >}})
- :apiref:`libretiny/lt_component.h`
- :ghedit:`Edit`
