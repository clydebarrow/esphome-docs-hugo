---
description: "Restart Button"
title: "Restart Button"
---

{{< seo description="" image="" >}}

The `restart` button platform allows you to restart your node remotely
through Home Assistant.

```yaml
# Example configuration entry
button:
  - platform: restart
    name: "Living Room Restart"

```
## Configuration variables:

- All options from [Button]({{< ref "components/button/_index#config-button" >}}).

## See Also

- {{< docref "shutdown/" >}}
- {{< docref "safe_mode/" >}}
- {{< docref "factory_reset/" >}}
- {{< docref "/components/switch/restart" >}}
- {{< docref "template/" >}}
- :apiref:`restart/button/restart_button.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/button/restart.md)

