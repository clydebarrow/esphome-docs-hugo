---
description: "Binary Light"
title: "Binary Light"
---

{{< seo description="" image="" >}}

The `binary` light platform creates a simple ON/OFF-only light from a
:ref:`binary output component <output>`.

{{< img src="binary-ui.png" alt="Image" width="40.0%" class="center" >}}

```yaml
# Example configuration entry
light:
  - platform: binary
    name: "Desk Lamp"
    output: light_output


```
## Configuration variables:

- **output** (**Required**, [Output Component]({{< ref "components/output/_index#output" >}})): The id of the binary [ID]({{< ref "guides/configuration-types#config-id" >}}) to use for this light.
- All other options from :ref:`Light <config-light>`.

## See Also

- {{< docref "/components/output/index" >}}
- {{< docref "/components/light/index" >}}
- {{< docref "/components/output/gpio" >}}
- {{< docref "/components/power_supply" >}}
- {{< apiref "binary/light/binary_light_output.h" "binary/light/binary_light_output.h" >}}
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/light/binary.md)

