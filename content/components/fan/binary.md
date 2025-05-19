---
description: "Binary Fan"
title: "Binary Fan"
---

{{< seo description="" image="" >}}

The `binary` fan platform lets you represent any binary [Output Component]({{< ref "components/output/_index#output" >}}) as a fan.

{{< img src="fan-ui.png" alt="Image" caption=".. code-block:: yaml" width="80.0%" class="center" >}}

    # Example configuration entry
    fan:
      - platform: binary
        output: fan_output
        name: "Living Room Fan"




## Configuration variables:

- **output** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The id of the
  binary output component to use for this fan.
- **oscillation_output** (*Optional*, [ID]({{< ref "guides/configuration-types#config-id" >}})): The id of the
  [Output Component]({{< ref "components/output/_index#output" >}}) to use for the oscillation state of this fan. Default is empty.
- **direction_output** (*Optional*, [ID]({{< ref "guides/configuration-types#config-id" >}})): The id of the
  [Output Component]({{< ref "components/output/_index#output" >}}) to use for the direction state of the fan. Default is empty.
- All other options from [Base Fan Configuration]({{< ref "components/fan/_index#config-fan" >}}).

## See Also

- [/components/output/index]({{< ref "/components/output/index" >}})
- [/components/output/gpio]({{< ref "/components/output/gpio" >}})
- [/components/fan/index]({{< ref "/components/fan/index" >}})
- :apiref:`fan/fan_state.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/fan/binary.md)
