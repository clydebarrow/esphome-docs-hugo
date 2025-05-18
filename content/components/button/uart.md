---
description: "UART Button"
title: "UART Button"
---

{{< seo description="" image="" >}}

The `uart` button platform allows you to send a pre-defined sequence of bytes on a
[UART bus ]({{< relref "/components/uart" >}}) when triggered.

```yaml
# Example configuration entry
button:
  - platform: uart
    name: "UART String Output"
    data: 'DataToSend'
  - platform: uart
    name: "UART Bytes Output"
    data: [0xDE, 0xAD, 0xBE, 0xEF]

```
## Configuration variables:

- **data** (**Required**, string or list of bytes): The data to send via UART. Either an ASCII string
  or a list of bytes.
- **uart_id** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): Manually specify the ID of the UART hub.
- All other options from [Button]({{< ref "components/button/_index#config-button" >}}).

## See Also

- [/components/uart]({{< ref "/components/uart" >}})
- :apiref:`uart/button/uart_button.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/button/uart.md)
