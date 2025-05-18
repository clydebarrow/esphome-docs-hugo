---
description: "Audio DAC Core"
title: "Audio DAC Core"
---

{{< seo description="" image="" >}}

The `audio_dac` component allows your ESPHome devices to use audio DAC hardware components, allowing the playback of
audio via the microcontroller from a range of sources via [/components/media_player/index]({{< ref "/components/media_player/index" >}}).

```yaml
# Example configuration entry
audio_dac:
  - platform: ...

```
## Platforms


## Configuration variables:

- **id** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): Manually specify the ID used for code generation.


## Automations

`audio_dac.mute_off` Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This action unmutes the output of the DAC.

Configuration variables:

- **id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The ID of the `audio_dac` platform.

`audio_dac.mute_on` Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This action mutes the output of the DAC.

Configuration variables:

- **id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The ID of the `audio_dac` platform.

`audio_dac.set_volume` Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This action sets the output volume of the DAC.

Configuration variables:

- **id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The ID of the `audio_dac` platform.
- **volume** (**Required**, percentage, [templatable]({{< ref "automations/templates#config-templatable" >}})): The desired volume level for the
  output from 0% to 100%.

## See Also

- [Edit this page on GitHub](https://github.com/esphome/esphome-docs/blob/current/content/components/audio_dac/index.md)
