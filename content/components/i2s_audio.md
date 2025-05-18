---
description: "I²S Audio Component"
title: "I²S Audio Component"
---

{{< seo description="" image="" >}}

The `i2s_audio` component allows for sending and receiving audio via I²S.
This component only works on ESP32 based chips.

```yaml
# Example configuration entry
i2s_audio:
  i2s_lrclk_pin: GPIOXX
  i2s_bclk_pin: GPIOXX

```
## Configuration variables:

- **i2s_lrclk_pin** (**Required**, [Pin]({{< ref "guides/configuration-types#config-pin" >}})): The GPIO pin to use for the I²S `LRCLK` *(Left/Right Clock)* signal, also referred to as `WS` *(Word Select)* or `FS` *(Frame Sync)*.
- **i2s_bclk_pin** (*Optional*, [Pin]({{< ref "guides/configuration-types#config-pin" >}})): The GPIO pin to use for the I²S `BCLK` *(Bit Clock)* signal, also referred to as `SCK` *(Serial Clock)*.
- **i2s_mclk_pin** (*Optional*, [Pin]({{< ref "guides/configuration-types#config-pin" >}})): The GPIO pin to use for the I²S `MCLK` *(Master Clock)* signal.
- **id** (*Optional*, [ID]({{< ref "guides/configuration-types#config-id" >}})): Manually specify the ID for this I²S bus if you need multiple.
- **use_legacy** (*Optional, boolean*): Use the legacy I²S driver when using esp-idf framework version 5.x.x. Not valid for Arduino framework or esp-idf version < 5. All `i2s_audio` components need to use the same setting. Defaults to `false`.

## See also

- [microphone/i2s_audio]({{< ref "microphone/i2s_audio" >}})
- [media_player/i2s_audio]({{< ref "media_player/i2s_audio" >}})
- [speaker/i2s_audio]({{< ref "speaker/i2s_audio" >}})
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/i2s_audio.md)
