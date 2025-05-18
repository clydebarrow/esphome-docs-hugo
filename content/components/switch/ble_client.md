---
description: "BLE Client Switch"
title: "BLE Client Switch"
---

{{< seo description="" image="" >}}

The `ble_client` component is a switch platform that is used to enable and disable a `ble_client`. This has
several uses, such as minimizing battery usage or for allowing other clients (Eg phone apps) to connect to the device.

For more information on BLE services and characteristics, see [/components/ble_client]({{< ref "/components/ble_client" >}}).

{{< warning >}}
The BLE software stack on the ESP32 consumes a significant amount of RAM on the device.

**Crashes are likely to occur** if you include too many additional components in your device's
configuration. Memory-intensive components such as [/components/voice_assistant]({{< ref "/components/voice_assistant" >}}) and other
audio components are most likely to cause issues.

{{< /warning >}}
```yaml
esp32_ble_tracker:

ble_client:
  - mac_address: XX:XX:XX:XX:XX:XX
    id: itag_black

switch:
  - platform: ble_client
    ble_client_id: itag_black
    name: "Enable iTag"

```
## Configuration variables:

- **ble_client_id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): ID of the associated BLE client.
- All other options from [Base Switch Configuration]({{< ref "components/switch/_index#config-switch" >}}).

## See Also

- [/components/ble_client]({{< ref "/components/ble_client" >}})
- :apiref:`ble_client/switch/ble_switch.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/switch/ble_client.md)
