---
description: "Copy Component"
title: "Copy Component"
---

{{< seo description="" image="" >}}

The `copy` component can be used to copy an existing component (like a sensor, switch, etc.)
and create a duplicate mirroring the source's state and forwarding actions such as turning on to the source.

For each of the supported platforms, the configuration consists of the required configuration
variable `source_id`, which is used to indicate the source of the object being mirorred.

## Copy Binary Sensor

```yaml
# Example configuration entry
binary_sensor:
  - platform: copy
    source_id: source_binary_sensor
    name: "Copy of source_binary_sensor"

```
Configuration variables:
************************

- **source_id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The binary sensor that should be mirrored.
- All other options from [Binary Sensor]({{< ref "components/binary_sensor/_index#config-binary_sensor" >}}).

## Copy Button

```yaml
# Example configuration entry
button:
  - platform: copy
    source_id: source_button
    name: "Copy of source_button"

```
Configuration variables:
************************

- **source_id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The button that should be mirrored.
- All other options from [Button]({{< ref "components/button/_index#config-button" >}}).

## Copy Cover

```yaml
# Example configuration entry
cover:
  - platform: copy
    source_id: source_cover
    name: "Copy of source_cover"

```
Configuration variables:
************************

- **source_id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The cover that should be mirrored.
- All other options from [Cover]({{< ref "components/cover/_index#config-cover" >}}).

## Copy Fan

```yaml
# Example configuration entry
fan:
  - platform: copy
    source_id: source_fan
    name: "Copy of source_fan"

```
Configuration variables:
************************

- **source_id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The fan that should be mirrored.
- All other options from [Fan]({{< ref "components/fan/_index#config-fan" >}}).

## Copy Lock

```yaml
# Example configuration entry
lock:
  - platform: copy
    source_id: source_lock
    name: "Copy of source_lock"

```
Configuration variables:
************************

- **source_id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The lock that should be mirrored.
- All other options from [Lock]({{< ref "components/lock/_index#config-lock" >}}).

## Copy Number

```yaml
# Example configuration entry
number:
  - platform: copy
    source_id: source_number
    name: "Copy of source_number"

```
Configuration variables:
************************

- **source_id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The number that should be mirrored.
- All other options from [Number]({{< ref "components/number/_index#config-number" >}}).

## Copy Select

```yaml
# Example configuration entry
select:
  - platform: copy
    source_id: source_select
    name: "Copy of source_select"

```
Configuration variables:
************************

- **source_id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The select that should be mirrored.
- All other options from [Select]({{< ref "components/select/_index#config-select" >}}).


## Copy Sensor

```yaml
# Example configuration entry
sensor:
  - platform: copy
    source_id: source_sensor
    name: "Copy of source_sensor"

```
Configuration variables:
************************

- **source_id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The sensor that should be mirrored.
- All other options from [Sensor]({{< ref "components/sensor/_index#config-sensor" >}}).

## Copy Switch

```yaml
# Example configuration entry
switch:
  - platform: copy
    source_id: source_switch
    name: "Copy of source_switch"

```
Configuration variables:
************************

- **source_id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The switch that should be mirrored.
- All other options from [Switch]({{< ref "components/switch/_index#config-switch" >}}).

## Copy Text Sensor

```yaml
# Example configuration entry
text_sensor:
  - platform: copy
    source_id: source_text_sensor
    name: "Copy of source_text_sensor"

```
Configuration variables:
************************

- **source_id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The text sensor that should be mirrored.
- All other options from [Text Sensor]({{< ref "components/text_sensor/_index#config-text_sensor" >}}).

## Copy Text

```yaml
# Example configuration entry
text:
  - platform: copy
    source_id: source_text
    name: "Copy of source_text"

```
Configuration variables:
************************

- **source_id** (**Required**, [config-id]({{< ref "guides/configuration-types#config-id" >}})): The text that should be mirrored.
- All other options from [Text]({{< ref "components/text/_index#config-text" >}}).

## See Also

- :ghedit:`Edit`
