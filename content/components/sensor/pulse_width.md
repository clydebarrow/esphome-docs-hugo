---
description: "Instructions for setting up pulse width sensors in ESPHome"
title: "Pulse Width Sensor"
params:
  seo:
    description: Instructions for setting up pulse width sensors in ESPHome
    image: pulse.svg
---


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

- **pin** (*Optional*, [Pin Schema](guides/configuration-types#config-pin_schema)): The pin to observe for the
  pulse width.
- **update_interval** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the sensor.
  Defaults to `60s`.

- **id** (*Optional*, [ID]({{< ref "guides/configuration-types#config-id" >}})): Set the ID of this sensor for use in lambdas.
- All other options from [Sensor](components/sensor/_index#config-sensor).

## See Also

- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- {{< apiref "pulse_width/pulse_width.h" "pulse_width/pulse_width.h" >}}


