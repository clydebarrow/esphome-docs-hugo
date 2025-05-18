---
description: "Internal Temperature Sensor"
title: "Internal Temperature Sensor"
---

{{< seo description="" image="" >}}

The `internal_temperature` sensor platform allows you to use the integrated
temperature sensor of the ESP32, RP2040 and BK72XX chip.

{{< note >}}
Some ESP32 variants return a large amount of invalid temperature
values, including 53.3°C which equates to a raw value of 128. Invalid measurements are ignored by this component.

{{< /note >}}
![.. code-block:: yaml](../images/internal_temperature-ui.png)
*.. code-block:: yaml*


    # Example configuration entry
    sensor:
      - platform: internal_temperature
        name: "Internal Temperature"

## Configuration variables:

- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The interval
  to check the sensor. Defaults to `60s`.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## See Also

- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- :ghedit:`Edit`
