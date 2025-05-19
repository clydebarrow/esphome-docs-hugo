---
description: "b-parasite"
title: "b-parasite"
---

{{< seo description="" image="" >}}

[b-parasite](https://github.com/rbaron/b-parasite) is an open source soil moisture and ambient temperature/humidity/light sensor.

The `b_parasite` sensor platform tracks b-parasite's Bluetooth Low Energy (BLE) advertisement packets. These packets contain soil moisture, air temperature/humidity and battery voltage data. Some b-parasite versions have light sensors, in which case the ambient illuminance is also present in the BLE advertisement data.

{{< img src="b_parasite.jpg" alt="Image" width="80.0%" class="center" >}}

```yaml
# Example configuration.

# Required.
esp32_ble_tracker:

sensor:
  - platform: b_parasite
    mac_address: XX:XX:XX:XX:XX:XX
    humidity:
      name: 'b-parasite Air Humidity'
    temperature:
      name: 'b-parasite Air Temperature'
    moisture:
      name: 'b-parasite Soil Moisture'
    battery_voltage:
      name: 'b-parasite Battery Voltage'
    illuminance:
      name: 'b-parasite Illuminance'

```
## Configuration variables

- **mac_address** (**Required**): The MAC address of the device.
- **temperature** (*Optional*): Air temperature in Celsius.

  - All options from [Base Sensor Configuration]({{< ref "components/sensor/_index#config-sensor" >}}).

- **humidity** (*Optional*): Relative air humidity in %.

  - All options from [Base Sensor Configuration]({{< ref "components/sensor/_index#config-sensor" >}}).

- **moisture** (*Optional*): Soil moisture in %.

  - All options from [Base Sensor Configuration]({{< ref "components/sensor/_index#config-sensor" >}}).

- **battery_voltage** (*Optional*): Battery voltage in volts.

  - All options from [Base Sensor Configuration]({{< ref "components/sensor/_index#config-sensor" >}}).

- **illuminance** (*Optional*): Illuminance in lux.

  - All options from [Base Sensor Configuration]({{< ref "components/sensor/_index#config-sensor" >}}).

## See Also

- [b-parasite on GitHub](https://github.com/rbaron/b-parasite)
- {{< docref "/components/esp32_ble_tracker" >}}
- {{< docref "absolute_humidity/" >}}
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/b_parasite.md)
