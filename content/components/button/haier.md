---
description: "Haier Climate Buttons"
title: "Haier Climate Buttons"
---

{{< seo description="" image="" >}}

Additional buttons for Haier AC cleaning. **These buttons are supported only by the hOn protocol**.

```yaml
# Example configuration entry
button:
  - platform: haier
    haier_id: haier_ac
    self_cleaning:
      name: Haier start self cleaning
    steri_cleaning:
      name: Haier start 56°C steri-cleaning

```
## Configuration variables:

- **haier_id** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The id of Haier climate component
- **self_cleaning** (*Optional*): A button that starts Haier climate self cleaning.
  All options from [Base Button Configuration]({{< ref "components/button/_index#config-button" >}}).
- **steri_cleaning** (*Optional*): A button that starts Haier climate 56°C Steri-Clean.
  All options from [Base Button Configuration]({{< ref "components/button/_index#config-button" >}}).

## See Also

- {{< docref "/components/climate/haier" "Haier Climate" >}}
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/button/haier.md)
