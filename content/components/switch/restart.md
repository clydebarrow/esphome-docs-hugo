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

- All options from [Switch]({{< ref "components/switch/_index#config-switch" >}}).

## See Also

- {{< docref "shutdown/" >}}
- {{< docref "safe_mode/" >}}
- {{< docref "factory_reset/" >}}
- {{< docref "/components/button/restart" >}}
- {{< docref "template/" >}}
- :apiref:`restart/switch/restart_switch.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/switch/restart.md)

