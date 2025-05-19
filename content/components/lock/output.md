---
description: "Generic Output Lock"
title: "Generic Output Lock"
---

{{< seo description="" image="" >}}

The `output` lock platform allows you to use any output component as a lock.

{{< img src="output-ui.png" alt="Image" width="80.0%" class="center" >}}

```yaml
# Example configuration entry
output:
  - platform: gpio
    pin: GPIOXX
    id: 'generic_out'
lock:
  - platform: output
    name: "Generic Output"
    output: 'generic_out'

```
## Configuration variables:

- **output** (**Required**, [ID]({{< ref "guides/configuration-types#config-id" >}})): The ID of the output component to use.
- All other options from [Lock]({{< ref "components/lock/_index#config-lock" >}}).

## See Also

- {{< docref "/components/output/index" >}}
- :apiref:`output/lock/output_lock.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/lock/output.md)
