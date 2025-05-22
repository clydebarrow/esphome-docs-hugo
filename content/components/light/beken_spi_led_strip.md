---
description: "Beken SPI LED Strip"
title: "Beken SPI LED Strip"
---

{{< seo description="" image="" >}}

This is a component using the Beken SPI DMA interface to drive addressable LED strips.

{{< warning >}}
Only works on pin P16, which is not available on many tuya modules.

{{< /warning >}}
```yaml
light:
  - platform: beken_spi_led_strip
    rgb_order: GRB
    pin: P16
    num_leds: 30
    chipset: ws2812
    name: "My Light"

```
## Configuration variables

- **pin** (**Required**, [Pin]({{< ref "guides/configuration-types#config-pin" >}})): The pin for the data line of the light.
- **num_leds** (**Required**, int): The number of LEDs in the strip.
- **chipset** (**Required**, enum): The chipset to apply known timings from.
    - `WS2812`
    - `SK6812`
    - `APA106`
    - `SM16703`

- **rgb_order** (**Required**, string): The RGB order of the strip.
    - `RGB`
    - `RBG`
    - `GRB`
    - `GBR`
    - `BGR`
    - `BRG`

- **is_rgbw** (*Optional*, boolean): Set to `true` if the strip is RGBW. Defaults to `false`.
- **is_wrgb** (*Optional*, boolean): Set to `true` if the strip is WRGB. Defaults to `false`.
- **max_refresh_rate** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})):
  A time interval used to limit the number of commands a light can handle per second. For example
  16ms will limit the light to a refresh rate of about 60Hz. Defaults to sending commands as quickly as
  changes are made to the lights.

- All other options from [Light]({{< ref "components/light/_index#config-light" >}}).


## See Also

- {{< docref "/components/light" >}}
- {{< docref "/components/power_supply" >}}
- {{< apiref "beken_spi_led_strip/beken_spi_led_strip.h" "beken_spi_led_strip/beken_spi_led_strip.h" >}}


