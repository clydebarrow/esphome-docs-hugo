---
description: "uFire ISE pH sensor"
title: "uFire ISE pH sensor"
---

{{< seo description="" image="" >}}

The `ufire_ise` sensor platform allows you to use your uFire ISE pH sensor with
ESPHome. The [I²C Bus]({{< ref "components/i2c#i2c" >}}) is
required to be set up in your configuration for this sensor to work.
It required also to have an temperature sensor in the liquid tank; this can
be on the same board or external sensor linked to the uFire ISE pH configuration.

{{< img src="ufire_ise.png" alt="Image" width="100.0%" class="center" >}}

```yaml
# Example configuration entry
sensor:
  - platform: ufire_ise
    id: ufire_ise_board
    temperature:
      id: temperature_liquid
      name: Temperature
    ph:
      name: pH


```
## Configuration variables:

- **address** (*Optional*, int): Specify the I²C address of the sensor. Defaults to `0x3f`.
- **update_interval** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the
  sensor. Defaults to `60s`.
- **id** (*Optional*, [ID]({{< ref "guides/configuration-types#config-id" >}})): Set the ID of this sensor for use in lambdas.
- **temperature_sensor** (*Optional*, [ID]({{< ref "guides/configuration-types#config-id" >}})): Set the ID of the temperature
  sensor. Only needed if the onboard temperature sensor is not used.
- **ph** (*Optional*, [Sensor]({{< ref "components/sensor/_index#config-sensor" >}})): Set the pH sensor configuration. All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).
- **temperature** (*Optional*, [Sensor]({{< ref "components/sensor/_index#config-sensor" >}})): Set the onboard temperature sensor configuration. All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).
  Can't be used together with `temperature_sensor`.

{{< anchor "sensor-ufire_ise-calibrate_probe_high_action" >}}

## `ufire_ise.calibrate_probe_high` Action

The pH probe have to be calibrated. For this you need know the pH reference value and temperature
of the calibration high solution.

```yaml
# Example configuration entry
sensor:
  - platform: ufire_ise
    id: ufire_ise_board
    # ...

# in some trigger
on_...:
  - sensor.ufire_ise_board.calibrate_probe_high:
      id: ufire_ise_board
      solution: 7.0
      temperature: !lambda "return id(temperature_liquid).state;"

```
Configuration options:

- **id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The ID of the ufire pH sensor.
- **solution** (**Required**, float): Solution reference pH value.

{{< anchor "sensor-ufire_ise-calibrate_probe_low_action" >}}

## `ufire_ise.calibrate_probe_low` Action

The pH probe have to be calibrated. For this you need know the pH reference value and temperature
of the calibration low solution.

```yaml
# Example configuration entry
sensor:
  - platform: ufire_ise
    id: ufire_ise_board
    # ...

# in some trigger
on_...:
  - sensor.ufire_ise_board.calibrate_probe_low:
      id: ufire_ise_board
      solution: 4.0
      temperature: !lambda "return id(temperature_liquid).state;"

```
Configuration options:

- **id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The ID of the ufire pH sensor.
- **solution** (**Required**, float): Solution reference pH value.

{{< anchor "sensor-ufire_ise-reset_action" >}}

## `ufire_ise.reset` Action

Reset the current calibration on the sensor.

```yaml
# Example configuration entry
sensor:
  - platform: ufire_ise
    id: ufire_ise_board
    # ...

# in some trigger
on_...:
  - sensor.ufire_ise_board.reset:
      id: ufire_ise_board

```
Configuration options:

- **id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The ID of the ufire pH sensor.

## See Also

- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- :apiref:`ufire_ise/ufire_ise.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/ufire_ise.md)

