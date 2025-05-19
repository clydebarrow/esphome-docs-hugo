---
description: "Audio ADC Core"
title: "Audio ADC Core"
---

{{< seo description="" image="" >}}

The `audio_adc` component allows your ESPHome devices to use audio ADC hardware components, allowing the
capture/recording of audio via the microcontroller from a range of sources.

```yaml
# Example configuration entry
audio_adc:
  - platform: ...

```
## Platforms

{{< anchor "config-audio_adc" >}}

## Configuration variables:

- **id** (*Optional*, [ID]({{< ref "guides/configuration-types#config-id" >}})): Manually specify the ID used for code generation.

{{< anchor "automations-audio_adc" >}}

## Automations

#### ``audio_adc.set_mic_gain`` Action

This action sets the (microphone) gain of the ADC.

Configuration variables:

- **id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The ID of the `audio_adc` platform.
- **mic_gain** (**Required**, percentage, [templatable]({{< ref "automations/templates#config-templatable" >}})): The desired gain level in decibels
  for the input.

## See Also

- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/audio_adc/index.md)
