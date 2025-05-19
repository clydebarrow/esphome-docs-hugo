---
description: "Shutdown Button"
title: "Shutdown Button"
---

{{< seo description="" image="" >}}

The `shutdown` button platform allows you to shutdown your node remotely
through Home Assistant. It does this by putting the node into deep sleep mode with no
wakeup source selected. After enabling, the only way to startup the ESP again is by
pressing the reset button or restarting the power supply.

{{< img src="shutdown-ui.png" alt="Image" width="80.0%" class="center" >}}

```yaml
# Example configuration entry
button:
  - platform: shutdown
    name: "Living Room Shutdown"

```
## Configuration variables:

- All options from [Base Button Configuration]({{< ref "components/button/_index#config-button" >}}).

## See Also

- [restart]({{< ref "restart/" >}})
- [safe_mode]({{< ref "safe_mode/" >}})
- [factory_reset]({{< ref "factory_reset/" >}})
- [/components/switch/shutdown]({{< ref "/components/switch/shutdown" >}})
- [template]({{< ref "template/" >}})
- :apiref:`shutdown/shutdown_button.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/button/shutdown.md)
