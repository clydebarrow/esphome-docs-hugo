---
description: "Template Output"
title: "Template Output"
---

{{< seo description="" image="" >}}

The `template` output component can be used to create templated binary and float outputs in ESPHome.

```yaml
# Example configuration entry
output:
  - platform: template
    id: outputsplit
    type: float
    write_action:
      - output.set_level:
          id: output1
          level: !lambda return state;
      - output.set_level:
          id: output2
          level: !lambda return state;

  - platform: ...
    id: output1
  - platform: ...
    id: output2



```
## Configuration variables:

- **id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The id to use for this output component.
- **type** (**Required**, string): The type of output. One of `binary` and `float`.
- **write_action** (**Required**, [Automation]({{< ref "automations/_index#automation" >}})): An automation to perform
  when the state of the output is updated.
- All other options from [Output]({{< ref "components/output/_index#config-output" >}}).

See :apiclass:`output::BinaryOutput` and :apiclass:`output::FloatOutput`.

{{< warning >}}
This is an **output component** and will not be visible from the frontend. Output components are intermediary
components that can be attached to for example lights.

{{< /warning >}}

## ``write_action`` Trigger

When the state for this output is updated, the `write_action` is triggered.
It is possible to access the state value inside Lambdas:

```yaml
- platform: template
    id: my_output
    type: float
    write_action:
      - if:
          condition:
            lambda: return ((state > 0) && (state < .4));
          then:
            - output.turn_on: button_off
            - delay: 500ms
            - output.turn_off: button_off


```
Complete example: [Sonoff Dual Light Switch](https://devices.esphome.io/devices/Sonoff-Dual-DIY-light).

## See Also

- [/components/output/index]({{< ref "/components/output/index" >}})
- [automation]({{< ref "automations/_index#automation" >}})
- [Edit this page on GitHub](https://github.com/esphome/esphome-docs/blob/current/content/components/output/template.md)
