---
description: "GPIO Output"
title: "GPIO Output"
---

{{< seo description="" image="" >}}

The GPIO output component is quite simple: It exposes a single GPIO pin
as an output component. Note that output components are **not** switches and
will not show up in Home Assistant. See {{< docref "/components/switch/gpio" >}}.

```yaml
# Example configuration entry
output:
  - platform: gpio
    pin: GPIOXX
    id: gpio_d1

```
## Configuration variables:

- **pin** (**Required**, :ref:`Pin Schema <config-pin_schema>`): The pin to turn on and off.
- **id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The id to use for this output component.
- All other options from :ref:`Output <config-output>`.

{{< warning >}}
This is an **output component** and will not be visible from the frontend. Output components are intermediary
components that can be attached to for example lights. To have a GPIO pin in the Home Assistant frontend, please
see the {{< docref "/components/switch/gpio" >}}.

{{< /warning >}}
## See Also

- {{< docref "/components/switch/gpio" >}}
- {{< docref "/components/output/index" >}}
- {{< docref "/components/output/esp8266_pwm" >}}
- {{< docref "/components/output/ledc" >}}
- {{< docref "/components/light/binary" >}}
- {{< docref "/components/fan/binary" >}}
- {{< docref "/components/power_supply" >}}
- {{< apiref "gpio/output/gpio_binary_output.h" "gpio/output/gpio_binary_output.h" >}}
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/output/gpio.md)

