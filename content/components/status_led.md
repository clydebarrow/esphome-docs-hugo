---
description: "Status LED"
title: "Status LED"
---

{{< seo description="" image="" >}}

The `status_led` hooks into all ESPHome components and can indicate the status of
the device. Specifically, it will:

- Blink slowly (about every second) when a **warning** is active. Warnings are active when for
  example reading a sensor value fails temporarily, the WiFi/MQTT connections are disrupted, or
  if the native API component is included but no client is connected.
- Blink quickly (multiple times per second) when an **error** is active. Errors indicate that
  ESPHome has found an error while setting up. In most cases, ESPHome will still try to
  recover from the error and continue with all other operations.
- Stay off otherwise.

```yaml
# Example configuration entry
status_led:
  pin: GPIOXX

```
{{< note >}}
If your device has a single LED that needs to be shared use  :doc:`status_led light platform </components/light/status_led>` instead.

{{< /note >}}
## Configuration variables:

- **pin** (**Required**, [Pin Schema]({{< ref "guides/configuration-types#config-pin_schema" >}})): The
  GPIO pin to operate the status LED on.
- **id** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): Manually specify the ID used for code generation.

{{< note >}}
If your LED is in an active-LOW mode (when it's on if the output is enabled), use the
``inverted`` option of the :ref:`Pin Schema <config-pin_schema>`:

.. code-block:: yaml

    status_led:
      pin:
        number: GPIOXX
        inverted: true

{{< /note >}}
## See Also

- [/components/light/status_led]({{< ref "/components/light/status_led" >}})
- :apiref:`status_led/status_led.h`
- [Edit this page on GitHub](https://github.com/esphome/esphome-docs/blob/current/content/components/status_led.md)
