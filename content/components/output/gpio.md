---
description: "GPIO Output"
title: "GPIO Output"
---

{{< seo description="" image="" >}}

The GPIO output component is quite simple: It exposes a single GPIO pin
as an output component. Note that output components are **not** switches and
will not show up in Home Assistant. See [/components/switch/gpio]({{< ref "/components/switch/gpio" >}}).

```yaml
# Example configuration entry
output:
  - platform: gpio
    pin: GPIOXX
    id: gpio_d1

```
## Configuration variables:

- **pin** (**Required**, [Pin Schema]({{< ref "guides/configuration-types#config-pin_schema" >}})): The pin to turn on and off.
- **id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The id to use for this output component.
- All other options from [Base Output Configuration]({{< ref "components/output/_index#config-output" >}}).

{{< warning >}}
This is an **output component** and will not be visible from the frontend. Output components are intermediary
components that can be attached to for example lights. To have a GPIO pin in the Home Assistant frontend, please
see the [/components/switch/gpio]({{< ref "/components/switch/gpio" >}}).

{{< /warning >}}
## See Also

- [/components/switch/gpio]({{< ref "/components/switch/gpio" >}})
- [/components/output/index]({{< ref "/components/output/index" >}})
- [/components/output/esp8266_pwm]({{< ref "/components/output/esp8266_pwm" >}})
- [/components/output/ledc]({{< ref "/components/output/ledc" >}})
- [/components/light/binary]({{< ref "/components/light/binary" >}})
- [/components/fan/binary]({{< ref "/components/fan/binary" >}})
- [/components/power_supply]({{< ref "/components/power_supply" >}})
- :apiref:`gpio/output/gpio_binary_output.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/output/gpio.md)
