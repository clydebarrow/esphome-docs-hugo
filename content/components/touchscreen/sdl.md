---
description: "SDL2 Touch Screen Emulator"
title: "SDL2 Touch Screen Emulator"
---

{{< seo description="" image="" >}}


The `sdl` touchscreen platform allows emulating a touch screen by using the mouse with the `sdl` display driver.
The `sdl` display component must be configured to use this.

## Base Touchscreen Configuration

```yaml
# Example configuration entry
touchscreen:
  platform: sdl

```
Configuration variables:
************************

- **id** (*Optional*, [config-id]({{< ref "guides/configuration-types#config-id" >}})): Manually set the ID of this touchscreen.

- All other options from [Touchscreen]({{< ref "components/touchscreen/_index#config-touchscreen" >}}).


## See Also

- [SDL display]({{< ref "components/display/sdl#sdl" >}})
- :apiref:`sdl/sdl_touchscreen.h`
- :ghedit:`Edit`
