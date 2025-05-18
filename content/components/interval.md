---
description: ""
title: ""
---

## Interval Component

This component allows you to run actions at fixed time intervals. For example, if you want to toggle a switch every
minute, you can use this component. Please note that it's possible to achieve the same thing with the
[``on_time`` Trigger]({{< ref "components/time/_index#time-on_time" >}}) trigger, but this technique is more light-weight and user-friendly.

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

- **interval** (**Required**, [Time]({{< ref "guides/configuration-types#config-time" >}})): The interval to execute the action with.
- **startup_delay** (*Optional*, [Time]({{< ref "guides/configuration-types#config-time" >}})): An optional startup delay - defaults to zero.
- **then** (**Required**, [All Actions]({{< ref "automations/actions#config-action" >}})): The action to perform.

## See Also

- [index]({{< ref "index/" >}})
- [/automations/actions]({{< ref "/automations/actions" >}})
- [/automations/templates]({{< ref "/automations/templates" >}})
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/interval.md)
