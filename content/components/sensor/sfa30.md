---
description: "SFA30 Formaldehyde Sensor"
title: "SFA30 Formaldehyde Sensor"
---

{{< seo description="" image="" >}}

The `sfa30` sensor platform  allows you to use your Sensirion SFA30 Formaldehyde
([datasheet](https://sensirion.com/media/documents/DEB1C6D6/63D92360/Sensirion_formaldehyde_sensors_datasheet_SFA30.pdf)) sensors with ESPHome.
The [I²C Bus]({{< ref "components/i2c#i2c" >}}) is required to be set up in your configuration for this sensor to work.
This sensor supports both UART and I²C communication. However, at the moment only I²C communication is implemented.

![.. code-block:: yaml](../images/sfa30.jpg)
*.. code-block:: yaml*


    # Example configuration entry
    sensor:
      - platform: sfa30
        formaldehyde:
          name: "Formaldehyde"
        temperature:
          name: "Temperature"
        humidity:
          name: "Humidity"


## Configuration variables:

- **formaldehyde** (*Optional*): The information for the Formaldehyde sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

- **temperature** (*Optional*): The information for the Temperature sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).


- **humidity** (*Optional*): The information for the Humidity sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).


- **address** (*Optional*, int): Manually specify the I²C address of the sensor.
  Defaults to `0x5D`.

- **update_interval** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The interval to check the
  sensor. Defaults to `60s`.


## See Also

- [sensor-filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- [absolute_humidity]({{< ref "absolute_humidity/" >}})
- :apiref:`sfa30/sfa30.h`
- :ghedit:`Edit`
