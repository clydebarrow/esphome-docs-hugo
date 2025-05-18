---
description: "Generic Output Button"
title: "Generic Output Button"
---

{{< seo description="" image="" >}}

The `output` button platform allows you to use any output component as a button. This can for example be used to
momentarily set a GPIO pin using a button.

![.. code-block:: yaml](../images/generic-ui.png)
*.. code-block:: yaml*


    # Example configuration entry
    output:
      - platform: gpio
        pin: GPIOXX
        id: output1

    button:
      - platform: output
        name: "Generic Output"
        output: output1
        duration: 500ms

## Configuration variables:

- **output** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The ID of the output component to use.
- **duration** (**Required**, [Time]({{< ref "guides/configuration-types#config-time" >}})): How long the output should be set when the button is pressed.
- All other options from [Base Button Configuration]({{< ref "components/button/_index#config-button" >}}).

{{< note >}}
When used with a :doc:`/components/output/gpio`, the pin will be low by default and pulled high when the button is
pressed. To invert this behaviour and have the pin pulled low when the button is pressed, set the `inverted` option
in the :ref:`config-pin_schema`.

{{< /note >}}
## See Also

- [/components/output/index]({{< ref "/components/output/index" >}})
- :apiref:`output/button/output_button.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/button/output.md)
