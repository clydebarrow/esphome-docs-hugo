---
description: "Create audio clip files for use with I²S Speakers"
title: "Create audio clip files for use with I²S Speakers"
---

.. audio_clips_for_i2s:


It is possible to create sound clips to include in your build to use with I²S speakers. No need for a media player component!  

- Using [Audacity](https://github.com/audacity/audacity), convert audio to WAV, mono, 16kHz, Unsigned 8bit PCM

{{< img src="save_as_wav.png" alt="Audacity export dialog" caption="- Convert again, this time with `SOX <https://github.com/chirlu/sox>`__." height="200" class="center" >}}

```console
sox startup.wav --bits 8 --encoding signed-integer --endian little startup_again.raw

```
- Now convert it into a hexadecimal string using [xxd](https://github.com/ckormanyos/xxd) into a C++ file.

```console
xxd -i startup_again.raw startup.c

```
- The resulting file needs a modification in the start line:
  Open in an editor and change
  `unsigned char startup_again_raw[] = {…[SNIP]…}`
  to
  `std::vector<unsigned char> startup_raw = {…[SNIP]…}`.

Now you can rename the file to startup.h, put it inside the esphome configuration directory and put it in a include in your device config like this:

```yaml
esphome:
  includes:
    - startup.h

```
Now you can define using the audio clip using the following:

```yaml
- speaker.play:
    id: speaker
    data: !lambda return startup_raw;

```
Enjoy!

HowTo by [NUT].

## See also

- [/components/speaker/index]({{< ref "/components/speaker/index" >}})
- [/components/speaker/i2s_audio]({{< ref "/components/speaker/i2s_audio" >}})
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/guides/audio_clips_for_i2s.md)
