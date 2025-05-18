---
description: "Haier Climate Switches"
title: "Haier Climate Switches"
---

{{< seo description="" image="" >}}

Additional switches to support additional features for Haier AC.

```yaml
# Example configuration entry
switch:
  - platform: haier
    beeper:
      name: Haier beeper
    health_mode:
      name: Haier health mode
    display:
      name: Haier display
    quiet_mode:
      name: Haier quiet mode

```
## Configuration variables:

- **haier_id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The id of Haier climate component
- **beeper** (*Optional*): (supported only by hOn) A switch that enables or disables Haier climate sound feedback.
  All options from [Switch]({{< ref "components/switch/_index#config-switch" >}}).
- **health_mode** (*Optional*): A switch that enables or disables Haier climate health mode ([UV light sterilization](https://www.haierhvac.eu/en/node/1809)).
  All options from [Switch]({{< ref "components/switch/_index#config-switch" >}}).
- **display** (*Optional*): A switch that enables or disables Haier climate led display.
  All options from [Switch]({{< ref "components/switch/_index#config-switch" >}}).
- **quiet_mode** (*Optional*): (supported only by hOn) A switch that enables or disables Haier climate quiet mode. Quiet mode not supported in Fan only mode.
  All options from [Switch]({{< ref "components/switch/_index#config-switch" >}}).

## See Also

- [Haier Climate ]({{< relref "/components/climate/haier" >}})
- :ghedit:`Edit`
