---
description: "Pulse Width Sensor"
title: "Pulse Width Sensor"
---

{{< seo description="" image="" >}}

The `pulse_width` sensor allows you to measure how long a given digital signal
is HIGH. For example this can be used to measure PWM signals to transmit some
value over a simple protocol. The unit of measurement for this sensor is seconds.

{{< note >}}
This component is intended for measurements in the microsecond to seconds range! 
The largest period this component can measure is just over 70 minutes.

{{< /note >}}
```yaml
# Example configuration entry
sensor:
  - platform: pulse_width
    pin: D0
    name: Pulse Width Sensor

```
## Configuration variables:

- **pin** (*Optional*, [Pin Schema]({{< ref "guides/configuration-types#config-pin_schema" >}})): The pin to observe for the
  pulse width.
- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the sensor.
  Defaults to `60s`.

- **id** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): Set the ID of this sensor for use in lambdas.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## See Also

- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- :apiref:`pulse_width/pulse_width.h`
- :ghedit:`Edit`
