---
description: "Duty Cycle Sensor"
title: "Duty Cycle Sensor"
---

{{< seo description="" image="" >}}

The duty cycle sensor allows you to measure for what percentage of time a signal
on a GPIO pin is HIGH or LOW.

For example, you can measure if a status LED of a pool controller is permanently active
(indicating that the pump is on) or blinking.

{{< img src="duty_cycle-ui.png" alt="Image" width="80.0%" class="center" >}}

```yaml
# Example configuration entry
sensor:
  - platform: duty_cycle
    pin: D0
    name: Duty Cycle Sensor

```
## Configuration variables:

- **pin** (*Optional*, :ref:`Pin Schema <config-pin_schema>`): The pin to observe for the duty
  cycle.
- **update_interval** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the sensor. Defaults to `60s`.

- **id** (*Optional*, [ID]({{< ref "guides/configuration-types#config-id" >}})): Set the ID of this sensor for use in lambdas.
- All other options from :ref:`Sensor <config-sensor>`.

## See Also

- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- {{< apiref "duty_cycle/duty_cycle_sensor.h" "duty_cycle/duty_cycle_sensor.h" >}}


