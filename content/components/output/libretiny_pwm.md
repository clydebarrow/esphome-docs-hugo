---
description: "LibreTiny PWM Output"
title: "LibreTiny PWM Output"
---

{{< seo description="" image="" >}}

The LibreTiny PWM platform allows you to use a hardware PWM on BK72xx and RTL87xx chips.
Refer to [LibreTiny/Boards](https://docs.libretiny.eu/link/boards) to find your board
and which PWM pins it supports.

```yaml
# Example configuration entry
output:
  - platform: libretiny_pwm
    pin: P8
    frequency: 1000 Hz
    id: pwm_output

# Example usage in a light
light:
  - platform: monochromatic
    output: pwm_output
    name: "Kitchen Light"

```
## Configuration variables:

- **pin** (**Required**, [Pin Schema]({{< ref "guides/configuration-types#config-pin_schema" >}})): The pin to use PWM on.
- **id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The id to use for this output component.
- **frequency** (*Optional*, frequency): The frequency to run the PWM with. Lower frequencies
  have more visual artifacts, but can represent much more colors. Defaults to `1000 Hz`.
- All other options from [Output]({{< ref "components/output/_index#config-output" >}}).


## ``output.libretiny_pwm.set_frequency`` Action

This [Action]({{< ref "automations/actions#config-action" >}}) allows you to manually change the frequency of a LibreTiny PWM
channel at runtime. Use cases include controlling a passive buzzer (for pitch control).

```yaml
on_...:
  - output.libretiny_pwm.set_frequency:
      id: pwm_output
      frequency: 100Hz

```
Configuration variables:

- **id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The ID of the PWM output to change.
- **frequency** (**Required**, [templatable]({{< ref "automations/templates#config-templatable" >}}), float): The frequency
  to set in hertz.

## See Also

- [/components/libretiny]({{< ref "/components/libretiny" >}})
- [/components/output/index]({{< ref "/components/output/index" >}})
- [/components/light/monochromatic]({{< ref "/components/light/monochromatic" >}})
- [/components/fan/speed]({{< ref "/components/fan/speed" >}})
- [/components/power_supply]({{< ref "/components/power_supply" >}})
- :apiref:`libretiny_pwm/libretiny_pwm.h`
- :ghedit:`Edit`
