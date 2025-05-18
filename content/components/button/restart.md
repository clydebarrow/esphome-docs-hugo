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

- [shutdown]({{< ref "shutdown/" >}})
- [safe_mode]({{< ref "safe_mode/" >}})
- [factory_reset]({{< ref "factory_reset/" >}})
- [/components/switch/restart]({{< ref "/components/switch/restart" >}})
- [template]({{< ref "template/" >}})
- :apiref:`restart/button/restart_button.h`
- :ghedit:`Edit`
