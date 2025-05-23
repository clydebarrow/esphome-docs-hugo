---
description: "Binary Light"
title: "Binary Light"
---

{{< seo description="" image="" >}}

The `binary` light platform creates a simple ON/OFF-only light from a
[binary output component]({{< ref "components/output/_index#output" >}}).

{{< img src="binary-ui.png" alt="Image"  width="40.0%" class="center" >}}

```yaml
# Example configuration entry
light:
  - platform: binary
    name: "Desk Lamp"
    output: light_output


```
## Configuration variables:

- **output** (**Required**, [Output Component]({{< ref "components/output/_index#output" >}})): The id of the binary [ID]({{< ref "guides/configuration-types#config-id" >}}) to use for this light.
- All other options from [Light]({{< ref "components/light/_index#config-light" >}}).

## See Also

- {{< docref "/components/output" >}}
- {{< docref "/components/light" >}}
- {{< docref "/components/output/gpio" >}}
- {{< docref "/components/power_supply" >}}
- {{< apiref "binary/light/binary_light_output.h" "binary/light/binary_light_output.h" >}}


