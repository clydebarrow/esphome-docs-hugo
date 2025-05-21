---
description: "Status LED Light"
title: "Status LED Light"
---

{{< seo description="" image="" >}}

The `status_led` light platform allows to share a single LED for indicating the status of
the device (when on error/warning state) or as binary light (when on OK state).
This is useful for devices with only one LED available.
You can also use a binary :ref:`output`.

It provides the combined functionality of {{< docref "/components/status_led" "status_led component" >}} and a
{{< docref "/components/light/binary" "binary light component" >}} over a single shared GPIO led.

When the device is on error/warning state, the function of `status_led` will take precedence and control the blinking of the LED.
When the device is in OK state, the LED will be restored to the state of the `binary light` function and can be controlled as such.

```yaml
# Example configuration entry
light:
  - platform: status_led
    name: "Switch state"
    pin: GPIOXX

```
{{< note >}}
When using this platform the high level `status_led` component should not be included (at least over the same pin),
as its functionality is directly provided by this platform.

The only difference is that the platform won't be loaded in OTA safe mode, while the component would be.

{{< /note >}}
## Configuration variables:

- **pin** (*Optional*, [Pin Schema]({{< ref "guides/configuration-types#config-pin_schema" >}})): The GPIO pin to operate the LED on.
- **output** (*Optional*, :ref:`config-id`): The id of the binary :ref:`output` to use for this light.
- All other options from [Light]({{< ref "components/light/_index#config-light" >}}).

{{< note >}}
If your Status LED is in an active-LOW mode (such as with the D1 Mini ESP8266 boards), use the
`inverted` option of the [Pin Schema]({{< ref "guides/configuration-types#config-pin_schema" >}}):

```yaml
pin:
  number: GPIOXX
  inverted: true
```



{{< /note >}}
## See Also

- {{< docref "/components/status_led" >}}
- {{< docref "/components/light/binary" >}}
- {{< docref "/components/light/index" >}}
- :apiref:`status_led/light/status_led_light.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/light/status_led.md)

