---
description: "BLE Client Sensor"
title: "BLE Client Sensor"
---

{{< seo description="" image="" >}}

The `ble_client` component is a sensor platform that can query BLE devices for RSSI or specific
values of service characteristics.

For more information on BLE services and characteristics, see {{< docref "/components/ble_client" >}}.

{{< warning >}}
The BLE software stack on the ESP32 consumes a significant amount of RAM on the device.

**Crashes are likely to occur** if you include too many additional components in your device's
configuration. Memory-intensive components such as {{< docref "/components/voice_assistant" >}} and other
audio components are most likely to cause issues.

{{< /warning >}}
```yaml
esp32_ble_tracker:

ble_client:
  - mac_address: XX:XX:XX:XX:XX:XX
    id: itag_black

sensor:
  - platform: ble_client
    type: characteristic
    ble_client_id: itag_black
    name: "iTag battery level"
    service_uuid: '180f'
    characteristic_uuid: '2a19'
    icon: 'mdi:battery'
    unit_of_measurement: '%'

  - platform: ble_client
    type: rssi
    ble_client_id: itag_black
    name: "iTag RSSI"

```
## Configuration variables:

- **type** (**Required**): One of `rssi`, `characteristic`.

rssi options:

- **update_interval** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval to poll the device.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

characteristic options:

- **ble_client_id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): ID of the associated BLE client.
- **service_uuid** (**Required**, UUID): UUID of the service on the device.
- **characteristic_uuid** (**Required**, UUID): UUID of the service's characteristic to query.
- **descriptor_uuid** (*Optional*, UUID): UUID of the characteristic's descriptor to query.
- **id** (*Optional*, [ID]({{< ref "guides/configuration-types#config-id" >}})): The ID to use for code generation, and for reference by dependent components.
- **lambda** (*Optional*, [lambda]({{< ref "automations/templates#config-lambda" >}})): The lambda to use for converting a raw data
  reading to a sensor value. See [Raw Data Parsing Lambda]({{< ref "components/sensor/ble_client#ble-sensor-lambda" >}}) for more information.
- **notify** (*Optional*, boolean): Instruct the server to send notifications for this
  characteristic.
- **update_interval** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval to poll the device.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

Automations:

- **on_notify** (*Optional*, [Automation]({{< ref "automations/_index#automation" >}})): An automation to
  perform when a notify message is received from the device. See [``on_notify``]({{< ref "components/sensor/ble_client#ble_sensor-on_notify" >}}).

{{< anchor "ble-sensor-lambda" >}}

## Raw Data Parsing Lambda

By default only the first byte of each message received on the service's characteristic is used
for the sensor reading. For more complex messages, this behavior can be overridden by a custom
lambda function to parse the raw data. The received data bytes are passed to the lambda as a
variable `x` of type `std::vector<uint8_t>`. The function must return a single `float` value.

```yaml
...

sensor:
  - platform: ble_client
    type: characteristic
    ble_client_id: t_sensor
    name: "Temperature Sensor 32bit float"
    ...
    device_class: "temperature"
    lambda: |-
      return *((float*)(&x[0]));


```
## BLE Sensor Automation

{{< anchor "ble_sensor-on_notify" >}}

### ``on_notify``

This automation is triggered when the device/server sends a notify message for
a characteristic. The config variable *notify* must be true or this will have
no effect.
A variable `x` of type `float` is passed to the automation for use in lambdas.

## Example UUIDs
The UUIDs available on a device are dependent on the type of
device and the functionality made available. Check the ESPHome
device logs for those that are found on the device.

Some common ones:

| Service | Characteristic | Description |
| --- | --- | --- |
| 180F | 2A19 | Battery level |
| 181A | 2A6F | Humidity |


## See Also

- {{< docref "/components/ble_client" >}}
- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- :apiref:`ble_sensor/ble_sensor.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/sensor/ble_client.md)
