---
description: "BLE Component"
title: "BLE Component"
---

{{< seo description="" image="" >}}

The `esp32_ble` component in ESPHome sets up the Bluetooth LE stack on the device so that a [esp32_ble_server]({{< ref "esp32_ble_server/" >}})
can run.

{{< warning >}}
The BLE software stack on the ESP32 consumes a significant amount of RAM on the device.

**Crashes are likely to occur** if you include too many additional components in your device's
configuration. Memory-intensive components such as :doc:`/components/voice_assistant` and other
audio components are most likely to cause issues.

{{< /warning >}}
```yaml
# Example configuration

esp32_ble:
  io_capability: keyboard_only

```
## Configuration variables:

- **io_capability** (*Optional*, enum): The IO capability of this ESP32, used for securely connecting to other BLE devices. Defaults to `none`.

    - `none` - No IO capability (Connections that require PIN code authentication will fail)
    - `keyboard_only` - Only a keyboard to enter PIN codes (or a fixed PIN code)
    - `display_only` - Only a display to show PIN codes
    - `keyboard_display` - A keyboard and a display
    - `display_yes_no` - A display to show PIN codes and buttons to confirm or deny the connection

- **enable_on_boot** (*Optional*, boolean): If enabled, the BLE interface will be enabled on boot. Defaults to `true`.

- **name** (*Optional*, string): The name of the BLE device.
    - Defaults to the hostname of the device.
    - Must be 20 characters or less.
    - Must be 13 characters or less when using `name_add_mac_suffix: true` - [esphome-mac_suffix]({{< ref "components/esphome#esphome-mac_suffix" >}}).

## ``ble.disable`` Action

This action turns off the BLE interface on demand.

```yaml
on_...:
  then:
    - ble.disable:

```
{{< note >}}
The configuration option ``enable_on_boot`` can be set to ``false`` if you do not want BLE to be enabled on boot.


{{< /note >}}
## ``ble.enable`` Action

This action turns on the BLE interface on demand.

```yaml
on_...:
  then:
    - ble.enable:

```
{{< note >}}
The configuration option ``enable_on_boot`` can be set to ``false`` if you do not want BLE to be enabled on boot.


{{< /note >}}

## ``ble.enabled`` Condition

This [Condition]({{< ref "automations/actions#config-condition" >}}) checks if BLE is currently enabled or not.

```yaml
on_...:
  - if:
      condition: ble.enabled
      then:
        - ble.disable:
      else:
        - ble.enable:


```
The lambda equivalent for this is `id(ble_id).is_active()`.


## See Also

- [esp32_ble_server]({{< ref "esp32_ble_server/" >}})
- [esp32_improv]({{< ref "esp32_improv/" >}})
- :apiref:`esp32_ble/ble.h`
- :ghedit:`Edit`
