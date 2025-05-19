---
description: "Monochromatic Light"
title: "Monochromatic Light"
---

{{< seo description="" image="" >}}

The `monochromatic` light platform creates a simple brightness-only light from an
[Output Component]({{< ref "components/output/_index#output" >}}).

{{< img src="monochromatic-strip.jpg" alt="Image" caption="Example of a brightness-only LED strip that can be used with this component." width="75.0%" class="center" >}}

{{< img src="kitchen-lights.png" alt="Image" caption=".. code-block:: yaml" width="40.0%" class="center" >}}

    # Example configuration entry
    light:
      - platform: monochromatic
        name: "Kitchen Lights"
        output: output_component1


## Configuration variables:

- **output** (**Required**, [Output Component]({{< ref "components/output/_index#output" >}})): The id of the float [ID]({{< ref "guides/configuration-types#config-id" >}}) to use for this light.
- All other options from [Base Light Configuration]({{< ref "components/light/_index#config-light" >}}).

## See Also

{{< img src="monochromatic-detail.jpg" alt="Image" caption="- :doc:`/components/output/index`" width="75.0%" class="center" >}}

- [/components/light/index]({{< ref "/components/light/index" >}})
- [/components/light/binary]({{< ref "/components/light/binary" >}})
- [/components/power_supply]({{< ref "/components/power_supply" >}})
- [/components/output/ledc]({{< ref "/components/output/ledc" >}})
- [/components/output/esp8266_pwm]({{< ref "/components/output/esp8266_pwm" >}})
- [/components/output/pca9685]({{< ref "/components/output/pca9685" >}})
- [/components/output/tlc59208f]({{< ref "/components/output/tlc59208f" >}})
- [/components/output/my9231]({{< ref "/components/output/my9231" >}})
- :apiref:`monochromatic/monochromatic_light_output.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/light/monochromatic.md)
