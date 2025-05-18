---
description: "RGBCT Light"
title: "RGBCT Light"
---

{{< seo description="" image="" >}}

The `rgbct` light platform creates an RGBWT (color temperature + white brightness)
light from 5 [float output components]({{< ref "components/output/_index#output" >}}) (one for each channel).

```yaml
# Example configuration entry
light:
  - platform: rgbct
    name: "Livingroom Lights"
    red: output_component1
    green: output_component2
    blue: output_component3
    color_temperature: output_component4
    white_brightness: output_component5
    cold_white_color_temperature: 153 mireds
    warm_white_color_temperature: 500 mireds

```
## Configuration variables:

- **red** (**Required**, [output]({{< ref "components/output/_index#output" >}})): The id of the float [config-id]({{< ref "guides/configuration-types#config-id" >}}) to use for the red channel.
- **green** (**Required**, [output]({{< ref "components/output/_index#output" >}})): The id of the float [config-id]({{< ref "guides/configuration-types#config-id" >}}) to use for the green channel.
- **blue** (**Required**, [output]({{< ref "components/output/_index#output" >}})): The id of the float [config-id]({{< ref "guides/configuration-types#config-id" >}}) to use for the blue channel.
- **color_temperature** (**Required**, [output]({{< ref "components/output/_index#output" >}})): The id of the float [config-id]({{< ref "guides/configuration-types#config-id" >}}) to use for the
  color temperature channel.
- **white_brightness** (**Required**, [output]({{< ref "components/output/_index#output" >}})): The id of the float [config-id]({{< ref "guides/configuration-types#config-id" >}}) to use for the brightness
  of the white leds.
- **cold_white_color_temperature** (**Required**, float): The coldest color temperature supported by this light. This
  is the lowest value when expressed in [mireds](https://en.wikipedia.org/wiki/Mired), or the highest value when
  expressed in Kelvin.
- **warm_white_color_temperature** (**Required**, float): The warmest color temperature supported by this light. This
  is the highest value when expressed in [mireds](https://en.wikipedia.org/wiki/Mired), or the lowest value when
  expressed in Kelvin.
- **color_interlock** (*Optional*, boolean): When enabled, this will prevent white leds being on at the same
  time as RGB leds. See [rgbw_color_interlock]({{< ref "components/light/rgbw#rgbw_color_interlock" >}}) for more information. Defaults to `false`.
- All other options from [Light]({{< ref "components/light/_index#config-light" >}}).

## See Also

- [/components/output/index]({{< ref "/components/output/index" >}})
- [/components/light/index]({{< ref "/components/light/index" >}})
- [/components/light/rgb]({{< ref "/components/light/rgb" >}})
- [/components/light/rgbw]({{< ref "/components/light/rgbw" >}})
- [/components/light/rgbww]({{< ref "/components/light/rgbww" >}})
- [/components/power_supply]({{< ref "/components/power_supply" >}})
- [/components/output/ledc]({{< ref "/components/output/ledc" >}})
- [/components/output/esp8266_pwm]({{< ref "/components/output/esp8266_pwm" >}})
- [/components/output/pca9685]({{< ref "/components/output/pca9685" >}})
- [/components/output/tlc59208f]({{< ref "/components/output/tlc59208f" >}})
- [/components/output/my9231]({{< ref "/components/output/my9231" >}})
- [/components/output/sm16716]({{< ref "/components/output/sm16716" >}})
- :apiref:`rgbct/rgbct_light_output.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/light/rgbct.md)
