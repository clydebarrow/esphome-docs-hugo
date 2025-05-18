---
description: "Generic Output Lock"
title: "Generic Output Lock"
---

{{< seo description="" image="" >}}

The `output` lock platform allows you to use any output component as a lock.

![.. code-block:: yaml](../images/output-ui.png)
*.. code-block:: yaml*


    # Example configuration entry
    output:
      - platform: gpio
        pin: GPIOXX
        id: 'generic_out'
    lock:
      - platform: output
        name: "Generic Output"
        output: 'generic_out'

## Configuration variables:

- **output** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The ID of the output component to use.
- All other options from [Lock]({{< ref "components/lock/_index#config-lock" >}}).

## See Also

- [/components/output/index]({{< ref "/components/output/index" >}})
- :apiref:`output/lock/output_lock.h`
- :ghedit:`Edit`
