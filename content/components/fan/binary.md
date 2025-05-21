---
description: "Binary Fan"
title: "Binary Fan"
---

{{< seo description="" image="" >}}

The `binary` fan platform lets you represent any binary :ref:`output` as a fan.

{{< img src="fan-ui.png" alt="Image" width="80.0%" class="center" >}}

```yaml
# Example configuration entry
fan:
  - platform: binary
    output: fan_output
    name: "Living Room Fan"




```
## Configuration variables:

- **output** (**Required**, :ref:`config-id`): The id of the
  binary output component to use for this fan.
- **oscillation_output** (*Optional*, :ref:`config-id`): The id of the
  [output]({{< ref "components/output/_index#output" >}}) to use for the oscillation state of this fan. Default is empty.
- **direction_output** (*Optional*, :ref:`config-id`): The id of the
  [output]({{< ref "components/output/_index#output" >}}) to use for the direction state of the fan. Default is empty.
- All other options from [Fan Component]({{< ref "components/fan/_index#config-fan" >}}).

## See Also

- {{< docref "/components/output/index" >}}
- {{< docref "/components/output/gpio" >}}
- {{< docref "/components/fan/index" >}}
- :apiref:`fan/fan_state.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/fan/binary.md)

