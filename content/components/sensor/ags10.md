---
description: "AGS10 Volatile Organic Compound (VOC) Sensor"
title: "AGS10 Volatile Organic Compound (VOC) Sensor"
---

{{< seo description="" image="" >}}

The `ags10` sensor platform VOC sensor allows you to use your ASAIR AGS10
([datasheet](http://www.aosong.com/userfiles/files/Datasheet%20AGS10.pdf),
`ASAIR`_ ) sensors with
ESPHome. The [I²C Bus]({{< ref "components/i2c#i2c" >}}) is
required to be set up in your configuration for this sensor to work.

{{< note >}}
The sensor supports up to 15kHz operation, so you should specify up to `frequency: 15kHz` in your `i2c` configuration.


{{< /note >}}
[ASAIR](http://www.aosong.com/en/products-86.html)

{{< img src="ags10.jpg" alt="Image" caption="AGS10 VOC Sensor" width="30.0%" class="center" >}}

```yaml
# Example configuration entry
sensor:
  - platform: ags10
    tvoc:
      name: TVOC

```
## Configuration variables:

- **tvoc** (**Required**): The information for the total Volatile Organic Compounds sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).
- **address** (*Optional*, int): Manually specify the I²C address of
  the sensor. Defaults to `0x1A`.
- **update_interval** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the
  sensor. Defaults to `60s`.
- **version** (*Optional*): The firmware version of the sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).
- **resistance** (*Optional*): The initial value of the sensor resistance.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## Actions:

{{< anchor "sensor-AGS10SetZeroPointAction" >}}

## ``ags10.set_zero_point`` Action

Zero-point of AGS10 has been calibrated before leaving factory. User can re-calibrate the zero-point as
needed.

```yaml
# Example configuration entry
sensor:
  - platform: ags10
    id: ags10_1_id
    # ...

# in some trigger
on_...:
  - ags10.set_zero_point:
      id: ags10_1_id
      mode: CURRENT_VALUE

```
Configuration option:

- **id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The ID of the AGS10 sensor.
- **mode** (**Required**, enum): One of supported modes:

  - `FACTORY_DEFAULT` - reset to the factory zero-point
  - `CURRENT_VALUE` - set zero-point calibration with current resistance
  - `CUSTOM_VALUE` - set zero-point calibration with resistance pointed with `value` option

- **value** (*Optional*, int): nominated resistance value to set (unit: 0.1 kΩ).


{{< anchor "sensor-AGS10NewI2cAddressAction" >}}

## ``ags10.new_i2c_address`` Action

I2C address of AGS10 can be modified, and it is possible to use multiple AGS10 sensors on one bus.
After sending the command for address changing, the new address is saved and takes effect immediately even
after power-off.

```yaml
# Example configuration entry
sensor:
  - platform: ags10
    id: ags10_1_id
    # ...

# in some trigger
on_...:
  - ags10.new_i2c_address:
      id: ags10_1_id
      address: 0x1E

```
Configuration options:

- **id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The ID of the AGS10 sensor.
- **address** (**Required**, int): New I2C address.

  
## See Also

- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- :apiref:`ags10/ags10.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/ags10.md)

