---
description: "UDP Packet Transport Platform"
title: "UDP Packet Transport Platform"
---

{{< seo description="" image="" >}}

The [Packet Transport Component]({{< ref "components/packet_transport/_index#packet-transport" >}}) platform allows ESPHome nodes to directly communicate with each over a communication channel.
The UDP implementation of the platform uses UDP as a communication medium. See the [UDP Component]({{< ref "components/udp#udp" >}}) and [Packet Transport Component]({{< ref "components/packet_transport/_index#packet-transport" >}}) for more information.

## Example Configuration

```yaml
# Example configuration entry
packet_transport:
  platform: udp
  sensors:
    - dht_temp

udp:

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
- [/components/udp]({{< ref "/components/udp" >}})
- [/components/binary_sensor/packet_transport]({{< ref "/components/binary_sensor/packet_transport" >}})
- [/components/sensor/packet_transport]({{< ref "/components/sensor/packet_transport" >}})
- [Automation]({{< ref "automations/_index#automation" >}})
- :apiref:`packet_transport/packet_transport.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/packet_transport/udp.md)
