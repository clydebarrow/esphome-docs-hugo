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

- All options from :ref:`Button <config-button>`.

## See Also

- {{< docref "/automations/index" >}}
- {{< docref "/components/button/index" >}}


