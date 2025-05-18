---
description: "Haier Climate Binary Sensors"
title: "Haier Climate Binary Sensors"
---

{{< seo description="" image="" >}}

Additional sensors for Haier Climate device. **These sensors are supported only by the hOn protocol**.


![.. code-block:: yaml](../images/haier-climate.jpg)
*.. code-block:: yaml*


    # Example configuration entry
    binary_sensor:
      - platform: haier
        haier_id: haier_ac
        compressor_status:
          name: Haier Outdoor Compressor Status
        defrost_status:
          name: Haier Defrost Status
        four_way_valve_status:
          name: Haier Four Way Valve Status
        indoor_electric_heating_status:
          name: Haier Indoor Electric Heating Status
        indoor_fan_status:
          name: Haier Indoor Fan Status
        outdoor_fan_status:
          name: Haier Outdoor Fan Status

## Configuration variables:

- **haier_id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The id of haier climate component
- **compressor_status** (*Optional*): A binary sensor that indicates Haier climate compressor activity.
  All options from [Binary Sensor]({{< ref "components/binary_sensor/_index#config-binary_sensor" >}}).
- **defrost_status** (*Optional*): A binary sensor that indicates defrost procedure activity.
  All options from [Binary Sensor]({{< ref "components/binary_sensor/_index#config-binary_sensor" >}}).
- **four_way_valve_status** (*Optional*): A binary sensor that indicates four way valve status.
  All options from [Binary Sensor]({{< ref "components/binary_sensor/_index#config-binary_sensor" >}}).
- **indoor_electric_heating_status** (*Optional*): A binary sensor that indicates electrical heating system activity.
  All options from [Binary Sensor]({{< ref "components/binary_sensor/_index#config-binary_sensor" >}}).
- **indoor_fan_status** (*Optional*): A binary sensor that indicates indoor fan activity.
  All options from [Binary Sensor]({{< ref "components/binary_sensor/_index#config-binary_sensor" >}}).
- **outdoor_fan_status** (*Optional*): A binary sensor that indicates outdoor fan activity.
  All options from [Binary Sensor]({{< ref "components/binary_sensor/_index#config-binary_sensor" >}}).

## See Also

- [Haier Climate ]({{< relref "/components/climate/haier" >}})
- :ghedit:`Edit`
