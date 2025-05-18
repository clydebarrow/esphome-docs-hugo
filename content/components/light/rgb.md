---
description: "RGB Light"
title: "RGB Light"
---

{{< seo description="" image="" >}}

The `rgb` light platform creates an RGB light from 3 [Output Component]({{< ref "components/output/_index#output" >}})
(one for each color channel).

![Example of an RGB LED strip that can be used with this component.](../images/rgb-strip.jpg)
*Example of an RGB LED strip that can be used with this component.*


![.. code-block:: yaml](../images/rgb-ui.png)
*.. code-block:: yaml*


    # Example configuration entry
    light:
      - platform: rgb
        name: "Living Room Lights"
        red: output_component1
        green: output_component2
        blue: output_component3


## Color Correction

It is often favourable to calibrate/correct the color produced by an LED strip light as the
perceived intensity of different colors will generally vary. This can be done by using
[Base Output Configuration]({{< ref "components/output/_index#config-output" >}}) on individual output channels:

```yaml
# Example configuration entry
light:
  - platform: rgb
    name: "Living Room Lights"
    red: output_component1
    green: output_component2
    blue: output_component3

# Example output entry
output:
  - platform: ...
    id: output_component1
    max_power: 80%
  # Repeat for green and blue output

```
{{< note >}}
Remember that ``gamma_correct`` is enabled by default (``γ=2.8``), and you may want take it into account for the calibration. For instance if you command a light to *50%* brightness and want it to be the new maximum: ``max_PWM_power = max_light_power^2.8 = 0.5^2.8 = 0.144``, then you would set ``max_power`` to *14.4%*.

{{< /note >}}
## Configuration variables:

- **red** (**Required**, [Output Component]({{< ref "components/output/_index#output" >}})): The id of the float [ID]({{< ref "guides/configuration-types#config-id" >}}) to use for the red channel.
- **green** (**Required**, [Output Component]({{< ref "components/output/_index#output" >}})): The id of the float [ID]({{< ref "guides/configuration-types#config-id" >}}) to use for the green channel.
- **blue** (**Required**, [Output Component]({{< ref "components/output/_index#output" >}})): The id of the float [ID]({{< ref "guides/configuration-types#config-id" >}}) to use for the blue channel.
- All other options from [Base Light Configuration]({{< ref "components/light/_index#config-light" >}}).

## See Also

![- :doc:`/components/output/index`](../images/rgb-detail.jpg)
*- :doc:`/components/output/index`*

- [/components/light/index]({{< ref "/components/light/index" >}})
- [/components/light/rgbw]({{< ref "/components/light/rgbw" >}})
- [/components/light/rgbww]({{< ref "/components/light/rgbww" >}})
- [/components/light/rgbct]({{< ref "/components/light/rgbct" >}})
- [/components/power_supply]({{< ref "/components/power_supply" >}})
- [/components/output/ledc]({{< ref "/components/output/ledc" >}})
- [/components/output/esp8266_pwm]({{< ref "/components/output/esp8266_pwm" >}})
- [/components/output/pca9685]({{< ref "/components/output/pca9685" >}})
- [/components/output/tlc59208f]({{< ref "/components/output/tlc59208f" >}})
- [/components/output/my9231]({{< ref "/components/output/my9231" >}})
- [/components/output/sm16716]({{< ref "/components/output/sm16716" >}})
- :apiref:`rgb/rgb_light_output.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/light/rgb.md)
