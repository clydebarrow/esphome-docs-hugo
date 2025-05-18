---
description: "Speaker Components"
title: "Speaker Components"
---

{{< seo description="" image="" >}}

The `speaker` domain contains common functionality shared across the
speaker platforms.


## Base Speaker Configuration

```yaml
speaker:
  - platform: ...


```
Configuration variables:

- **audio_dac** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})):[audio DAC ]({{< relref "/components/audio_dac/index" >}})dex>` to use for volume control.


## Speaker Actions

All `speaker` actions can be used without specifying an `id` if you have only one `speaker` in
your configuration YAML.


`speaker.play` Action
^^^^^^^^^^^^^^^^^^^^^^^

This action will start playing raw audio data from the speaker.

```yaml
on_...:
  # Static raw audio data
  - speaker.play: [...]

  # Templated, return type is std::vector<uint8_t>
  - speaker.play: !lambda return {...};

  # in case you need to specify the speaker id
  - speaker.play:
      id: my_speaker
      data: [...]

```
Configuration variables:

- **id** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The speaker to control. Defaults to the only one in YAML.
- **data** (**Required**, list of bytes): The raw audio data to play.


`speaker.stop` Action
^^^^^^^^^^^^^^^^^^^^^^^

This action will stop playing audio data from the speaker and discard the unplayed data.

Configuration variables:

- **id** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The speaker to control. Defaults to the only one in YAML.


`speaker.finish` Action
^^^^^^^^^^^^^^^^^^^^^^^^^

This action will stop playing audio data from the speaker after all data **is** played.

Configuration variables:

- **id** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The speaker to control. Defaults to the only one in YAML.


`speaker.mute_on` Action
^^^^^^^^^^^^^^^^^^^^^^^^^^

This action will mute the speaker.

Configuration variables:

- **id** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The speaker to control. Defaults to the only one in YAML.


`speaker.mute_off` Action
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This action will unmute the speaker.

Configuration variables:

- **id** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The speaker to control. Defaults to the only one in YAML.


`speaker.volume_set` Action
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This action will set the volume of the speaker.

```
on_...:
  # Simple
  - speaker.volume_set: 50%

  # Full
  - speaker.volume_set:
      id: speaker_id
      volume: 50%

  # Simple with lambda
  -  speaker.volume_set: !lambda "return 0.5;"

```
Configuration variables:

**volume** (**Required**, percentage): The volume to set the speaker to.


## Speaker Conditions

All `speaker` conditions can be used without specifying an `id` if you have only one `speaker` in
your configuration YAML.


`speaker.is_playing` Condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This condition will check if the speaker is currently playing audio data.

Configuration variables:

- **id** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The speaker to check. Defaults to the only one in YAML.


`speaker.is_stopped` Condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This condition will check if the speaker is fully stopped audio data and is in idle mode.

.. note:

Between the time `speaker.is_playing` is false and `speaker.is_stopped` is true the 'speaker' component is closing down structures that where used to play the data correctly. *It better to check if the speaker is stopped then that if it plays.*

Configuration variables:

- **id** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The speaker to check. Defaults to the only one in YAML.


## Platforms

## See Also

- [/guides/audio_clips_for_i2s]({{< ref "/guides/audio_clips_for_i2s" >}})
- [/components/speaker/i2s_audio]({{< ref "/components/speaker/i2s_audio" >}})
- :ghedit:`Edit`
