---
description: "UDP Packet Transport Platform"
title: "UDP Packet Transport Platform"
---

{{< seo description="" image="" >}}

The :ref:`packet-transport` platform allows ESPHome nodes to directly communicate with each over a communication channel.
The UDP implementation of the platform uses UDP as a communication medium. See the :ref:`packet-transport` and :ref:`udp` for more information.

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

- :ref:`packet-transport`
- {{< docref "/components/udp" >}}
- {{< docref "/components/binary_sensor/packet_transport" >}}
- {{< docref "/components/sensor/packet_transport" >}}
- :ref:`automation`
- :apiref:`packet_transport/packet_transport.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/packet_transport/udp.md)

