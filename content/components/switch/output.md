---
description: "Generic Output Switch"
title: "Generic Output Switch"
---

{{< seo description="" image="" >}}

The `output` switch platform allows you to use any output component as a switch.

{{< img src="output-ui.png" alt="Image" caption=".. code-block:: yaml" width="80.0%" class="center" >}}

    # Example configuration entry
    output:
      - platform: gpio
        pin: GPIOXX
        id: 'generic_out'
    switch:
      - platform: output
        name: "Generic Output"
        output: 'generic_out'

## Configuration variables:

- **output** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The ID of the output component to use.
- All other options from [Base Switch Configuration]({{< ref "components/switch/_index#config-switch" >}}).

## See Also

- [/components/output/index]({{< ref "/components/output/index" >}})
- :apiref:`output/switch/output_switch.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/switch/output.md)
