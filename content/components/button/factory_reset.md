---
description: "Factory Reset Button"
title: "Factory Reset Button"
---

{{< seo description="" image="" >}}

The `factory_reset` button allows you to remotely invalidate (reset) all ESPHome [Adjusting flash writes]({{< ref "components/esphome#preferences-flash_write_interval" >}}) stored in flash memory and reboot your node.
After reboot all states, parameters and variables will be reinitialized with their default values. This is useful:

- for devices preflashed with ESPHome to reset behavior back to factory state
- in case of moving a device to a new environment or starting a new use-case (e.g. reset counters or state)
- for privacy concerns when giving away a device

{{< note >}}
**USE WITH GREAT CAUTION!** All credentials, global variables, counters and saved states stored in non-volatile memory will be lost with no chance of recovering them.
Even raw reading of flash memory with `esptool` will not help, since data is physically erased from flash memory.

For devices configured using [captive portal ]({{< relref "/components/captive_portal" >}}), this will reset WiFi settings as well, thus making such devices offline.
You'll need to be in close proximity to your device to configure it again using a built-in WiFi access point and captive portal.


{{< /note >}}
{{< img src="factory-rst-ui.png" alt="Image" caption=".. code-block:: yaml" width="80.0%" class="center" >}}

    # Example configuration entry
    button:
      - platform: factory_reset
        name: Restart with Factory Default Settings

## Configuration variables:

- All options from [Base Button Configuration]({{< ref "components/button/_index#config-button" >}}).

## See Also

- [shutdown]({{< ref "shutdown/" >}})
- [restart]({{< ref "restart/" >}})
- [safe_mode]({{< ref "safe_mode/" >}})
- [/components/switch/factory_reset]({{< ref "/components/switch/factory_reset" >}})
- [template]({{< ref "template/" >}})
- :apiref:`factory_reset/factory_reset_button.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/button/factory_reset.md)
