---
description: "Binary Light"
title: "Binary Light"
---

{{< seo description="" image="" >}}

The `binary` light platform creates a simple ON/OFF-only light from a
[binary output component]({{< ref "components/output/_index#output" >}}).

![.. code-block:: yaml](../images/binary-ui.png)
*.. code-block:: yaml*


    # Example configuration entry
    light:
      - platform: binary
        name: "Desk Lamp"
        output: light_output


## Configuration variables:

- **output** (**Required**, [output]({{< ref "components/output/_index#output" >}})): The id of the binary [config-id]({{< ref "guides/configuration-types#config-id" >}}) to use for this light.
- All other options from [Light]({{< ref "components/light/_index#config-light" >}}).

## See Also

- [/components/output/index]({{< ref "/components/output/index" >}})
- [/components/light/index]({{< ref "/components/light/index" >}})
- [/components/output/gpio]({{< ref "/components/output/gpio" >}})
- [/components/power_supply]({{< ref "/components/power_supply" >}})
- :apiref:`binary/light/binary_light_output.h`
- :ghedit:`Edit`
