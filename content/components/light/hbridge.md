---
description: "H-bridge Light"
title: "H-bridge Light"
---

{{< seo description="" image="" >}}

The `hbridge` light platform creates a dual color brightness controlled light from two
[float output component]({{< ref "components/output/_index#output" >}}).

{{< img src="hbridge-ui.png" alt="Image" width="40.0%" class="center" >}}

H-bridge lights are very common for Christmas lighting and they use 2 wires for a bunch of LEDs.
The pins are switched alternatively to allow two sets of lights to operate.

```yaml
# Example configuration entry
light:
  - platform: hbridge
    id: mainlight
    name: "Hbridge Lights"
    pin_a: pina
    pin_b: pinb

```
Internally, H-bridge lights are implemented as cold/warm white lights. This means that the brightness of the two colors
is mapped to the cold white and warm white values, even if the colors aren't actually white in reality. To individually
control the colors in the [light control actions]({{< ref "components/light/_index#light-turn_on_action" >}}), you need to use the `cold_white` and
`warm_white` options.


## Configuration variables:

- **pin_a** (**Required**, [Output Component]({{< ref "components/output/_index#output" >}})): The id of the first float [ID]({{< ref "guides/configuration-types#config-id" >}}) to use for this light.
- **pin_b** (**Required**, [Output Component]({{< ref "components/output/_index#output" >}})): The id of the second float [ID]({{< ref "guides/configuration-types#config-id" >}}) to use for this light.
- All other options from [Light]({{< ref "components/light/_index#config-light" >}}).

{{< note >}}
As we are switching the H-bridge in software, the light may glitch every so often when other tasks run on the MCU.

{{< /note >}}
## See Also

- {{< docref "/components/light/index" >}}
- {{< docref "/components/output/esp8266_pwm" >}}
- :apiref:`hbridge/light/hbridge_light.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/light/hbridge.md)
