---
description: "BLE Client Text Sensor"
title: "BLE Client Text Sensor"
---

{{< seo description="" image="" >}}

The `ble_client` component is a text sensor platform that can
query BLE devices for specific values of service characteristics.

For more information on BLE services and characteristics, see
{{< docref "/components/ble_client" >}}.

```yaml
esp32_ble_tracker:

ble_client:
  - mac_address: XX:XX:XX:XX:XX:XX
    id: itag_black

text_sensor:
  - platform: ble_client
    ble_client_id: itag_black
    name: "Sensor Location"
    service_uuid: '180d'
    characteristic_uuid: '2a38'

```
## Configuration variables:

- **ble_client_id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): ID of the associated BLE client.
- **service_uuid** (**Required**, UUID): UUID of the service on the device.
- **characteristic_uuid** (**Required**, UUID): UUID of the service's characteristic to query.
- **descriptor_uuid** (*Optional*, UUID): UUID of the characteristic's descriptor to query.
- **notify** (*Optional*, boolean): Instruct the server to send notifications for this
  characteristic. Defaults to `false`.
- **update_interval** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval to poll the device. Defaults to `60s`.
- All other options from [Text Sensor]({{< ref "components/text_sensor/_index#config-text_sensor" >}}).

Automations:

- **on_notify** (*Optional*, [Automation]({{< ref "automations/_index#automation" >}})): An automation to
  perform when a notify message is received from the device. See [``on_notify``]({{< ref "components/text_sensor/ble_client#ble_text_sensor-on_notify" >}}).


## BLE Sensor Automation

{{< anchor "ble_text_sensor-on_notify" >}}

### ``on_notify``

This automation is triggered when the device/server sends a notify message for
a characteristic. The config variable *notify* must be true or this will have
no effect.
A variable `x` of type `std::string` is passed to the automation for use in lambdas.

## See Also

- {{< docref "/components/ble_client" >}}
- {{< docref "/components/sensor/ble_client" >}}
- [Sensor Filters]({{< ref "components/sensor/_index#sensor-filters" >}})
- :apiref:`ble_text_sensor/ble_text_sensor.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/text_sensor/ble_client.md)

