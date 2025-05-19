---
description: "Restart Switch"
title: "Restart Switch"
---

{{< seo description="" image="" >}}

The `restart` switch platform allows you to restart your node remotely
through Home Assistant.

{{< img src="restart-ui.png" alt="Image" width="80.0%" class="center" >}}

```yaml
# Example configuration entry
switch:
  - platform: restart
    name: "Living Room Restart"

```
## Configuration variables:

- All options from [Base Switch Configuration]({{< ref "components/switch/_index#config-switch" >}}).

## See Also

- [shutdown]({{< ref "shutdown/" >}})
- [safe_mode]({{< ref "safe_mode/" >}})
- [factory_reset]({{< ref "factory_reset/" >}})
- [/components/button/restart]({{< ref "/components/button/restart" >}})
- [template]({{< ref "template/" >}})
- :apiref:`restart/switch/restart_switch.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/switch/restart.md)
