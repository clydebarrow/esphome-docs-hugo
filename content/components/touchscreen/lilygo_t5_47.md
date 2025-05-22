---
description: "Lilygo T5 4.7\" Touchscreen"
title: "Lilygo T5 4.7\" Touchscreen"
---

{{< seo description="" image="" >}}

The `liygo_t5_47` touchscreen platform allows using the touchscreen controller
for the Lilygo T5 4.7" e-Paper Display with ESPHome.
The [I²C]({{< ref "components/i2c#i2c" >}}) is required to be set up in your configuration for this touchscreen to work.

```yaml
# Example configuration entry
touchscreen:
  - platform: lilygo_t5_47
    interrupt_pin: GPIOXX


```
## Configuration variables:

- **id** (*Optional*, [ID]({{< ref "guides/configuration-types#config-id" >}})): Manually set the ID of this touchscreen.
- **interrupt_pin** (*Optional*, [Pin Schema]({{< ref "guides/configuration-types#config-pin_schema" >}})): The touch detection pin. Must be `GPIO13`.
- All other options from [Base Touchscreen Configuration]({{< ref "components/touchscreen/_index#config-touchscreen" >}}).

## See Also

- {{< docref "index/" "Touchscreen" >}}
- {{< apiref "lilygo_t5_47/touchscreen/lilygo_t5_47_touchscreen.h" "lilygo_t5_47/touchscreen/lilygo_t5_47_touchscreen.h" >}}


