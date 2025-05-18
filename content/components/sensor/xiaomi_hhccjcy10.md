---
description: "HHCCJCY10 Xiaomi MiFlora (Pink version)"
title: "HHCCJCY10 Xiaomi MiFlora (Pink version)"
---

{{< seo description="" image="" >}}

MiFlora, tuya (pink) version, measures temperature, moisture, ambient light and nutrient levels in the soil.

![.. code-block:: yaml](../images/xiaomi_hhccjcy10.jpg)
*.. code-block:: yaml*


    sensor:
      - platform: xiaomi_hhccjcy10
        mac_address: XX:XX:XX:XX:XX:XX
        temperature:
          name: "Xiaomi HHCCJCY10 Temperature"
        moisture:
          name: "Xiaomi HHCCJCY10 Moisture"
        illuminance:
          name: "Xiaomi HHCCJCY10 Illuminance"
        conductivity:
          name: "Xiaomi HHCCJCY10 Soil Conductivity"
        battery_level:
          name: "Xiaomi HHCCJCY10 Battery Level"

## Configuration variables:

- **mac_address** (**Required**, string): The MAC address of the device.
- **temperature** (*Optional*): The temperature sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).
- **moisture** (*Optional*): The moisture sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).
- **illuminance** (*Optional*): The illuminance sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).
- **conductivity** (*Optional*): The conductivity sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).
- **battery_level** (*Optional*): The battery level sensor.
  All options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).


## See Also

- [ble_client]({{< ref "ble_client/" >}})
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/xiaomi_hhccjcy10.md)
