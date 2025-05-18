---
description: "Uptime Sensor"
title: "Uptime Sensor"
---

{{< seo description="" image="" >}}

The `uptime` sensor allows you to track the time the ESP has stayed up for in seconds.
Time rollovers are automatically handled.

```yaml
# Example configuration entry
sensor:
  - platform: uptime
    type: seconds
    name: Uptime Sensor

```
## Configuration variables:

- **type** (*Optional*): Either:

  - `seconds` (*default*): A simple counter.
  - `timestamp`: presents the time ESPHome last booted up. Requires a [/components/time/index]({{< ref "/components/time/index" >}}).

- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The sensor reporting interval. Defaults to `60s`.
  Valid only with `type: seconds`.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## See Also

- [/components/text_sensor/uptime]({{< ref "/components/text_sensor/uptime" >}})
- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- :apiref:`uptime/uptime_sensor.h`
- :ghedit:`Edit`
