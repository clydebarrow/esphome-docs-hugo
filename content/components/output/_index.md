---
description: "Output Component"
title: "Output Component"
---

{{< seo description="" image="" >}}

Each platform of the `output` domain exposes some output to
ESPHome. These are grouped into two categories: `binary` outputs
(that can only be ON/OFF) and `float` outputs (like PWM, can output
any rational value between 0 and 1).


## Base Output Configuration

Each output platform extends this configuration schema.

```yaml
# Example configuration entry
output:
  - platform: ...
    id: my_output_id
    power_supply: power_supply_id
    inverted: false
    min_power: 0.01
    max_power: 0.75

```
Configuration variables:

- **id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The id to use for this output component.
- **power_supply** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The :doc:`power
  supply </components/power_supply>` to connect to
  this output. When the output is enabled, the power supply will
  automatically be switched on too.
- **inverted** (*Optional*, boolean): If the output should be treated
  as inverted. Defaults to `false`.

Float outputs only:

- **min_power** (*Optional*, float): Sets the minimum output value of this output platform.
  Must be in range from 0 to max_power. Defaults to `0`.  If zero_means_zero is `false` this will be output value when the entity is turned off.
- **max_power** (*Optional*, float): Sets the maximum output value of this output platform.
  Must be in range from min_power to 1. Defaults to `1`.
- **zero_means_zero** (*Optional*, boolean): Sets the output to use actual 0 instead of `min_power`.
  Defaults to `false`.



`output.turn_on` Action
*************************

This action turns the output with the given ID on when executed.

```yaml
on_...:
  then:
    - output.turn_on: light_1

```
{{< note >}}
This action can also be expressed in :ref:`lambdas <config-lambda>`:

.. code-block:: cpp

    id(light_1).turn_on();

{{< /note >}}

`output.turn_off` Action
**************************

This action turns the output with the given ID off when executed.

```yaml
on_...:
  then:
    - output.turn_off: light_1

```
{{< note >}}
This action can also be expressed in :ref:`lambdas <config-lambda>`:

.. code-block:: cpp

    id(light_1).turn_off();

{{< /note >}}

`output.set_level` Action
***************************

This action sets the float output to the given level when executed. Note: This only
works with floating point outputs like [/components/output/slow_pwm]({{< ref "/components/output/slow_pwm" >}}), [/components/output/sigma_delta_output]({{< ref "/components/output/sigma_delta_output" >}}), [/components/output/ledc]({{< ref "/components/output/ledc" >}}), [/components/output/esp8266_pwm]({{< ref "/components/output/esp8266_pwm" >}}).

```yaml
on_...:
  then:
    - output.set_level:
        id: light_1
        level: 50%

```
{{< note >}}
This action can also be expressed in :ref:`lambdas <config-lambda>`:

.. code-block:: cpp

    // range is 0.0 (off) to 1.0 (on)
    id(light_1).set_level(0.5);

{{< /note >}}
## Full Output Index

- [/components/switch/output]({{< ref "/components/switch/output" >}})
- [/components/power_supply]({{< ref "/components/power_supply" >}})
- [/components/light/binary]({{< ref "/components/light/binary" >}})
- [/components/light/monochromatic]({{< ref "/components/light/monochromatic" >}})
- [/components/light/rgb]({{< ref "/components/light/rgb" >}})
- [/components/fan/binary]({{< ref "/components/fan/binary" >}})
- [/components/fan/speed]({{< ref "/components/fan/speed" >}})
- :apiref:`binary_output.h <output/binary_output.h>`,
  :apiref:`float_output.h <output/float_output.h>`

- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/output/index.md)


