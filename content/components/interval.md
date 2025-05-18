---
description: ""
title: ""
---

## Interval Component

This component allows you to run actions at fixed time intervals. For example, if you want to toggle a switch every
minute, you can use this component. Please note that it's possible to achieve the same thing with the
[time.on_time]({{< ref "components/time/_index#time-on_time" >}}) trigger, but this technique is more light-weight and user-friendly.

```yaml
# Example configuration entry
interval:
  - interval: 1min
    then:
      - switch.toggle: relay_1


```
If a startup delay is configured, the first execution of the actions will not occur before at least that time after boot.

Configuration variables:
************************

- **interval** (**Required**, [config-time]({{< ref "guides/configuration-types#config-time" >}})): The interval to execute the action with.
- **startup_delay** (*Optional*, [config-time]({{< ref "guides/configuration-types#config-time" >}})): An optional startup delay - defaults to zero.
- **then** (**Required**, [Action]({{< ref "automations/actions#config-action" >}})): The action to perform.

## See Also

- [index]({{< ref "index/" >}})
- [/automations/actions]({{< ref "/automations/actions" >}})
- [/automations/templates]({{< ref "/automations/templates" >}})
- [Edit this page on GitHub](https://github.com/esphome/esphome-docs/blob/current/content/components/interval.md)
