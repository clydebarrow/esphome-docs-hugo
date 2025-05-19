---
description: "Home Assistant Time Source"
title: "Home Assistant Time Source"
---


The preferred way to get time in ESPHome is using Home Assistant.
With the `homeassistant` time platform, the [native API ]({{< relref "/components/api" >}}) connection
to Home Assistant will be used to periodically synchronize the current time.

{{< note >}}
Although you might not plan to *export* states from the node and you do not need an entity of the node
in Home Assistant, this component still requires you to register the node under Home Assistant. See:
[Connecting your device to Home Assistant]({{< ref "guides/getting_started_hassio#connecting-your-device-to-home-assistant" >}}).

```yaml
```
# Example configuration entry
time:
    - platform: homeassistant
        id: homeassistant_time

{{< /note >}}
## Configuration variables

- All options from [Base Time Configuration]({{< ref "components/time/_index#base_time_config" >}}).


## See Also

- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/time/homeassistant.md)
