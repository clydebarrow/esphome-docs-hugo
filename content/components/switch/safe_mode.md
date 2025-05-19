---
description: "Safe Mode Switch"
title: "Safe Mode Switch"
---

{{< seo description="" image="" >}}

The `safe_mode` switch allows you to remotely reboot your node into [/components/safe_mode]({{< ref "/components/safe_mode" >}}). This is useful in certain situations where a misbehaving component, or low memory state is preventing Over-The-Air updates from completing successfully.

This component requires [/components/safe_mode]({{< ref "/components/safe_mode" >}}) to be configured.

{{< img src="safemode-ui.png" alt="Image" caption=".. code-block:: yaml" width="80.0%" class="center" >}}

    # Example configuration entry
    switch:
      - platform: safe_mode
        name: "Living Room Restart (Safe Mode)"

## Configuration variables:

- All options from [Base Switch Configuration]({{< ref "components/switch/_index#config-switch" >}}).

## See Also

- [shutdown]({{< ref "shutdown/" >}})
- [restart]({{< ref "restart/" >}})
- [factory_reset]({{< ref "factory_reset/" >}})
- [/components/button/safe_mode]({{< ref "/components/button/safe_mode" >}})
- [template]({{< ref "template/" >}})
- :apiref:`safe_mode/safe_mode_switch.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/switch/safe_mode.md)
