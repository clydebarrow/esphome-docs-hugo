---
description: "Speed Fan"
title: "Speed Fan"
---

{{< seo description="" image="" >}}

The `speed` fan platform lets you represent any float [output]({{< ref "components/output/_index#output" >}}) as a fan that
supports speed settings.

![.. code-block:: yaml](../images/fan-ui.png)
*.. code-block:: yaml*


    # Example configuration entry
    fan:
      - platform: speed
        output: my_output_1
        name: "Living Room Fan"

## Configuration variables:

- **output** (**Required**, [float output]({{< ref "components/output/_index#output" >}})): The id of the [config-id]({{< ref "guides/configuration-types#config-id" >}}) to use for this fan.
- **oscillation_output** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The id of the
  [output]({{< ref "components/output/_index#output" >}}) to use for the oscillation state of this fan. Default is empty.
- **direction_output** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The id of the
  [output]({{< ref "components/output/_index#output" >}}) to use for the direction state of the fan. Default is empty.
- **speed_count** (*Optional*, int): Set the number of supported discrete speed levels. The value is used
  to calculate the percentages for each speed. E.g. `2` means that you have 50% and 100% while `100`
  will allow 1% increments in the output. Defaults to `100`.
- **preset_modes** (*Optional*): A list of preset modes for this fan. Preset modes can be used in automations (i.e. `on_preset_set`).
- All other options from [Fan Component]({{< ref "components/fan/_index#config-fan" >}}).

## See Also

- [/components/output/index]({{< ref "/components/output/index" >}})
- [/components/fan/index]({{< ref "/components/fan/index" >}})
- [/components/output/ledc]({{< ref "/components/output/ledc" >}})
- [/components/output/esp8266_pwm]({{< ref "/components/output/esp8266_pwm" >}})
- [/components/output/pca9685]({{< ref "/components/output/pca9685" >}})
- :apiref:`fan/fan_state.h`
- :ghedit:`Edit`
