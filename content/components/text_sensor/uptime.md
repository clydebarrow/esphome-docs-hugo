---
description: "Uptime Text Sensor"
title: "Uptime Text Sensor"
---

{{< seo description="" image="" >}}

The `uptime` text sensor provides a human-readable representation the time since. The
elements can be separated by a custom string, and more significant elements will be omitted if they are zero. For example,
if the uptime is 1 day, 2 hours, 3 minutes, and 4 seconds, the sensor will report `1d2h3m4s` with the default
configuration. By default leading zero elements will be trimmed from the output, e.g. if the uptime is 0 days, 0 hours, 3 minutes, and 0 seconds, the sensor will report `3m0s`.
This can be disabled by setting `expand` to `true`.

```yaml
# Example configuration entry
text_sensor:
  - platform: uptime
    name: Uptime
    format:
      separator: " "
      days: "D"

```
## Configuration variables:

- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The sensor reporting interval. Defaults to `30s`.
- **expand** (*Optional*, boolean): If set, the text will always include all elements, even if they are zero. Defaults to `false`.
- **format** (*Optional*, list): Allows the customization of the output format. The following options are available:

    - **days** (*Optional*, string): The string to use for the days element. Defaults to `d`.
    - **hours** (*Optional*, string): The string to use for the hours element. Defaults to `h`.
    - **minutes** (*Optional*, string): The string to use for the minutes element. Defaults to `m`.
    - **seconds** (*Optional*, string): The string to use for the seconds element. Defaults to `s`.
    - **separator** (*Optional*, string): The separator to use between the uptime values. Defaults to the empty string.
- All other options from [Text Sensor]({{< ref "components/text_sensor/_index#config-text_sensor" >}}).

The resolution of the reported uptime will be determined by the update interval. For example, if the update interval is set to 30 seconds (the default), the uptime will be reported in minutes. More frequent updates will result in seconds being reported.



## See Also
- [/components/sensor/uptime]({{< ref "/components/sensor/uptime" >}})
- [text_sensor-filters]({{< ref "components/text_sensor/_index#text_sensor-filters" >}})
- :apiref:`uptime/uptime_text_sensor.h`
- :ghedit:`Edit`
