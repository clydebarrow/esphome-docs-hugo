---
description: "UART Packet Transport Platform"
title: "UART Packet Transport Platform"
---

{{< seo description="" image="" >}}

The [Packet Transport Component]({{< ref "components/packet_transport/_index#packet-transport" >}}) platform allows ESPHome nodes to directly communicate with each over a communication channel.
The UART implementation of the platform uses a serial port as a communication medium. See the [UART Bus]({{< ref "components/uart#uart" >}}) and [Packet Transport Component]({{< ref "components/packet_transport/_index#packet-transport" >}}) for more information.

## Example Configuration

```yaml
# Example configuration entry
packet_transport:
  platform: uart
  sensors:
    - dht_temp

uart:
  tx_pin: GPIOXX
  rx_pin: GPIOXX
  baud_rate: 9600

sensor:
  - platform: dht
      id: dht
      pin: GPIOXX
      temperature:
        name: "Temperature"
        id: dht_temp


```
## See Also

- [Packet Transport Component]({{< ref "components/packet_transport/_index#packet-transport" >}})
- [/components/uart]({{< ref "/components/uart" >}})
- [/components/binary_sensor/packet_transport]({{< ref "/components/binary_sensor/packet_transport" >}})
- [/components/sensor/packet_transport]({{< ref "/components/sensor/packet_transport" >}})
- [Automation]({{< ref "automations/_index#automation" >}})
- :apiref:`packet_transport/packet_transport.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/packet_transport/uart.md)
