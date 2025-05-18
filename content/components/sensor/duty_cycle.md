---
description: "Duty Cycle Sensor"
title: "Duty Cycle Sensor"
---

{{< seo description="" image="" >}}

The duty cycle sensor allows you to measure for what percentage of time a signal
on a GPIO pin is HIGH or LOW.

For example, you can measure if a status LED of a pool controller is permanently active
(indicating that the pump is on) or blinking.

![.. code-block:: yaml](../images/duty_cycle-ui.png)
*.. code-block:: yaml*


    # Example configuration entry
    sensor:
      - platform: duty_cycle
        pin: D0
        name: Duty Cycle Sensor

## Configuration variables:

- **pin** (*Optional*, [Pin Schema]({{< ref "guides/configuration-types#config-pin_schema" >}})): The pin to observe for the duty
  cycle.
- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the sensor. Defaults to `60s`.

- **id** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): Set the ID of this sensor for use in lambdas.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## See Also

- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- :apiref:`duty_cycle/duty_cycle_sensor.h`
- [Edit this page on GitHub](https://github.com/esphome/esphome-docs/blob/current/content/components/sensor/duty_cycle.md)
