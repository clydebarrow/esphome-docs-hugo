---
description: "Shutdown Switch"
title: "Shutdown Switch"
---

{{< seo description="" image="" >}}

The `shutdown` switch platform allows you to shutdown your node remotely
through Home Assistant. It does this by putting the node into deep sleep mode with no
wakeup source selected. After enabling, the only way to startup the ESP again is by
pressing the reset button or restarting the power supply.

![.. code-block:: yaml](../images/shutdown-ui.png)
*.. code-block:: yaml*


    # Example configuration entry
    switch:
      - platform: shutdown
        name: "Living Room Shutdown"

## Configuration variables:

- All options from [Switch]({{< ref "components/switch/_index#config-switch" >}}).

## See Also

- [restart]({{< ref "restart/" >}})
- [safe_mode]({{< ref "safe_mode/" >}})
- [factory_reset]({{< ref "factory_reset/" >}})
- [/components/button/shutdown]({{< ref "/components/button/shutdown" >}})
- [template]({{< ref "template/" >}})
- :apiref:`shutdown/shutdown_switch.h`
- :ghedit:`Edit`
