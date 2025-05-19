---
description: "Binary Light"
title: "Binary Light"
---

{{< seo description="" image="" >}}

The `binary` light platform creates a simple ON/OFF-only light from a
[Output Component]({{< ref "components/output/_index#output" >}}).

{{< img src="binary-ui.png" alt="Image" caption=".. code-block:: yaml" width="40.0%" class="center" >}}

    # Example configuration entry
    light:
      - platform: binary
        name: "Desk Lamp"
        output: light_output


## Configuration variables:

- **output** (**Required**, [Output Component]({{< ref "components/output/_index#output" >}})): The id of the binary [ID]({{< ref "guides/configuration-types#config-id" >}}) to use for this light.
- All other options from [Base Light Configuration]({{< ref "components/light/_index#config-light" >}}).

## See Also

- [/components/output/index]({{< ref "/components/output/index" >}})
- [/components/light/index]({{< ref "/components/light/index" >}})
- [/components/output/gpio]({{< ref "/components/output/gpio" >}})
- [/components/power_supply]({{< ref "/components/power_supply" >}})
- :apiref:`binary/light/binary_light_output.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/light/binary.md)
