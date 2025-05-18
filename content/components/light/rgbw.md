---
description: "RGBW Light"
title: "RGBW Light"
---

{{< seo description="" image="" >}}

The `rgbw` light platform creates an RGBW light from 4 [float output components]({{< ref "components/output/_index#output" >}}) (one for each channel).

```yaml
# Example configuration entry
light:
  - platform: rgbw
    name: "Livingroom Lights"
    red: output_component1
    green: output_component2
    blue: output_component3
    white: output_component4

```
## Color Correction

It is often favourable to calibrate/correct the color produced by an LED strip light as the
perceived intensity of different colors will generally vary. This can be done by using
[max_power]({{< ref "components/output/_index#config-output" >}}) on individual output channels:

```yaml
# Example configuration entry
light:
  - platform: rgbw
    name: "Livingroom Lights"
    red: output_component1
    green: output_component2
    blue: output_component3
    white: output_component4

# Example output entry
output:
  - platform: ...
    id: output_component1
    max_power: 80%

```
{{< note >}}
Remember that ``gamma_correct`` is enabled by default (``γ=2.8``), and you may want take it into account for the calibration. For instance if you command a light to *50%* brightness and want it to be the new maximum: ``max_PWM_power = max_light_power^2.8 = 0.5^2.8 = 0.144``, then you would set ``max_power`` to *14.4%*.

{{< /note >}}
{{< anchor "rgbw_color_interlock" >}}

## Color Interlock

With some LED bulbs, it is not possible to enable the RGB leds at the same time as the white leds, or setting
the RGB channels to maximum whilst wanting a white light will have an undesired hue effect. For these cases a
configuration variable is available that prevents the RGB leds and white leds from being turned on at the same
time: `color_interlock`.

Setting this option to `true` will result in the light having two color modes available, `RGB` and `WHITE`.
When the `RGB` color mode is active, the white leds are turned off, and when the `WHITE` color mode is active,
the RGB leds are turned off. Switching between these modes can be done from the Home Assistant interface, or by using
the `color_mode` option of the [light control actions]({{< ref "components/light/_index#light-turn_on_action" >}}).

## Configuration variables:

- **red** (**Required**, [output]({{< ref "components/output/_index#output" >}})): The id of the float [config-id]({{< ref "guides/configuration-types#config-id" >}}) to use for the red channel.
- **green** (**Required**, [output]({{< ref "components/output/_index#output" >}})): The id of the float [config-id]({{< ref "guides/configuration-types#config-id" >}}) to use for the green channel.
- **blue** (**Required**, [output]({{< ref "components/output/_index#output" >}})): The id of the float [config-id]({{< ref "guides/configuration-types#config-id" >}}) to use for the blue channel.
- **white** (**Required**, [output]({{< ref "components/output/_index#output" >}})): The id of the float [config-id]({{< ref "guides/configuration-types#config-id" >}}) to use for the white channel.
- **color_interlock** (*Optional*, boolean): When enabled, this will prevent white leds being on at the same
  time as RGB leds. See [rgbw_color_interlock]({{< ref "components/light/rgbw#rgbw_color_interlock" >}}) for more information. Defaults to `false`.
- All other options from [Light]({{< ref "components/light/_index#config-light" >}}).

## See Also

- [/components/output/index]({{< ref "/components/output/index" >}})
- [/components/light/index]({{< ref "/components/light/index" >}})
- [/components/light/cwww]({{< ref "/components/light/cwww" >}})
- [/components/light/color_temperature]({{< ref "/components/light/color_temperature" >}})
- [/components/light/rgb]({{< ref "/components/light/rgb" >}})
- [/components/light/rgbww]({{< ref "/components/light/rgbww" >}})
- [/components/light/rgbct]({{< ref "/components/light/rgbct" >}})
- [/components/power_supply]({{< ref "/components/power_supply" >}})
- [/components/output/ledc]({{< ref "/components/output/ledc" >}})
- [/components/output/esp8266_pwm]({{< ref "/components/output/esp8266_pwm" >}})
- [/components/output/pca9685]({{< ref "/components/output/pca9685" >}})
- [/components/output/tlc59208f]({{< ref "/components/output/tlc59208f" >}})
- [/components/output/my9231]({{< ref "/components/output/my9231" >}})
- [/components/output/sm16716]({{< ref "/components/output/sm16716" >}})
- :apiref:`rgbw/rgb_light_output.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/light/rgbw.md)
