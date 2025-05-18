---
description: "H-bridge Switch"
title: "H-bridge Switch"
---

{{< seo description="" image="" >}}

The `hbridge` switch platform allows you to drive an *h-bridge* controlled latching relay.

![Omron G6CK-2117P relay module.](../images/hbridge-relay.png)
*Omron G6CK-2117P relay module.*


```yaml
# Example configuration entry
switch:
  - platform: hbridge
    id: my_relay
    name: "Relay"
    on_pin: GPIOXX
    off_pin: GPIOXX
    pulse_length: 50ms
    wait_time: 50ms

```
## Configuration variables:

- **on_pin** (**Required**, [config-pin_schema]({{< ref "guides/configuration-types#config-pin_schema" >}})): The GPIO pin to pulse to turn on the switch.
- **off_pin** (**Required**, [config-pin_schema]({{< ref "guides/configuration-types#config-pin_schema" >}})): The GPIO pin to pulse to turn off the switch.
- **pulse_length** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The length in milliseconds of the pulse sent on `on_pin` and `off_pin` to change switch state. Defaults to `100 ms`.
- **wait_time** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The time in milliseconds to delay between pulses on `off_pin` and `on_pin`. Defaults to no delay.
- **optimistic** (*optional*, boolean): Whether to operate in optimistic mode - when in this mode,
  any command sent to the switch will immediately update the reported state. Defaults to `false`, and the reported state updates only at the end of the pulse.

- All other options from [Switch Component]({{< ref "components/switch/_index#config-switch" >}}).

## See Also

- [/components/output/index]({{< ref "/components/output/index" >}})
- [/components/switch/index]({{< ref "/components/switch/index" >}})
- :apiref:`hbridge/switch/hbridge_switch.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/switch/hbridge.md)
