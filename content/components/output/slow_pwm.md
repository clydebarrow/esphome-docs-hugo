---
description: "Slow PWM Output"
title: "Slow PWM Output"
---

{{< seo description="" image="" >}}

Similar to PWM, the Slow PWM Output platform allows you to control GPIO pins by
pulsing them on/off over a longer time period. It could be used to control a
heating element through a relay where a fast PWM update cycle would not be appropriate.

{{< note >}}
This is for **slow** PWM output. For fast-switching PWM outputs (for example,
lights), see these outputs:

- ESP32: :doc:`ledc`
- ESP8266: :doc:`esp8266_pwm`

{{< /note >}}
```yaml
# Example configuration entry
output:
  - platform: slow_pwm
    pin: GPIOXX
    id: my_slow_pwm
    period: 15s


```
## Configuration variables:

- **id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The id to use for this output component.
- **period** (**Required**, [Time]({{< ref "guides/configuration-types#config-time" >}})): The duration of each cycle. (i.e. a 10s
  period at 50% duty would result in the pin being turned on for 5s, then off for 5s)
- **pin** (*Optional*, [Pin Schema]({{< ref "guides/configuration-types#config-pin_schema" >}})): The pin to pulse.
- **state_change_action** (*Optional*, [Automation]({{< ref "automations/_index#automation" >}})): An automation to perform when the load is switched. If a lambda is used the boolean `state` parameter holds the new status.
- **turn_on_action** (*Optional*, [Automation]({{< ref "automations/_index#automation" >}})): An automation to perform when the load is turned on. Can be used to control for example a switch or output component.
- **turn_off_action** (*Optional*, [Automation]({{< ref "automations/_index#automation" >}})): An automation to perform when the load is turned off. `turn_on_action` and `turn_off_action` must be configured together.
- **restart_cycle_on_state_change** (*Optional*, boolean): Restart a timer of a cycle
  when new state is set. Defaults to `false`.

- All other options from [Base Output Configuration]({{< ref "components/output/_index#config-output" >}}).


{{< note >}}
- If ``pin`` is defined the GPIO pin state is writen before any action is executed.
- ``state_change_action`` and ``turn_on_action``/``turn_off_action`` can be used togther. ``state_change_action`` is called before ``turn_on_action``/``turn_off_action``. It's recommended to use either ``state_change_action`` or ``turn_on_action``/``turn_off_action`` to change the state of an output. Using both automations together is only recommended for monitoring.


{{< /note >}}
## Example:

```yaml
output:
  - platform: slow_pwm
    id: my_slow_pwm
    period: 15s
    turn_on_action:
      - lambda: |-
          auto *out1 = id(output1);
          out1->turn_on();
    turn_off_action:
      - output.turn_off: output1


```
{{< note >}}
If the duty cycle is not constrained to a maximum value, the
:doc:`/components/output/sigma_delta_output` component offers faster updates and
greater control over the switching frequency. This is better for loads that
need some time to fully change between on and off, like eletric thermal
actuator heads or fans.

{{< /note >}}
## See Also

- [/components/output/index]({{< ref "/components/output/index" >}})
- [/components/output/esp8266_pwm]({{< ref "/components/output/esp8266_pwm" >}})
- [/components/output/ledc]({{< ref "/components/output/ledc" >}})
- [/components/output/sigma_delta_output]({{< ref "/components/output/sigma_delta_output" >}})
- [/components/light/monochromatic]({{< ref "/components/light/monochromatic" >}})
- [/components/fan/speed]({{< ref "/components/fan/speed" >}})
- [/components/power_supply]({{< ref "/components/power_supply" >}})
- :apiref:`slow_pwm/slow_pwm_output.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/output/slow_pwm.md)
