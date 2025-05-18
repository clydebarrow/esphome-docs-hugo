---
description: "Template Button"
title: "Template Button"
---

{{< seo description="" image="" >}}

The `template` button platform allows you to create simple buttons out of just actions. Once defined,
it will automatically appear in Home Assistant as a button and can be controlled through the frontend.

```yaml
# Example configuration entry
button:
  - platform: template
    name: "Template Button"
    on_press:
      - logger.log: Button Pressed

```
## Configuration variables:

- All options from [Button]({{< ref "components/button/_index#config-button" >}}).

## See Also

- [/automations/index]({{< ref "/automations/index" >}})
- [/components/button/index]({{< ref "/components/button/index" >}})
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/button/template.md)
