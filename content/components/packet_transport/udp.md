---
description: "UDP Packet Transport Platform"
title: "UDP Packet Transport Platform"
---

{{< seo description="" image="" >}}

The [packet-transport]({{< ref "components/packet_transport/_index#packet-transport" >}}) platform allows ESPHome nodes to directly communicate with each over a communication channel.
The UDP implementation of the platform uses UDP as a communication medium. See the [udp]({{< ref "components/udp#udp" >}}) and [packet-transport]({{< ref "components/packet_transport/_index#packet-transport" >}}) for more information.

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

- [packet-transport]({{< ref "components/packet_transport/_index#packet-transport" >}})
- [/components/udp]({{< ref "/components/udp" >}})
- [/components/binary_sensor/packet_transport]({{< ref "/components/binary_sensor/packet_transport" >}})
- [/components/sensor/packet_transport]({{< ref "/components/sensor/packet_transport" >}})
- [automation]({{< ref "automations/_index#automation" >}})
- :apiref:`packet_transport/packet_transport.h`
- :ghedit:`Edit`
