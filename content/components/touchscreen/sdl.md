---
description: "SDL2 Touch Screen Emulator"
title: "SDL2 Touch Screen Emulator"
---

{{< seo description="" image="" >}}

{{< anchor "sdl_touchscreen" >}}

The `sdl` touchscreen platform allows emulating a touch screen by using the mouse with the `sdl` display driver.
The `sdl` display component must be configured to use this.

## Base Touchscreen Configuration

```yaml
# Example configuration entry
touchscreen:
  platform: sdl

```
## Configuration variables:

- **id** (*Optional*, [ID]({{< ref "guides/configuration-types#config-id" >}})): Manually set the ID of this touchscreen.

- All other options from [Base Touchscreen Configuration]({{< ref "components/touchscreen/_index#config-touchscreen" >}}).


## See Also

- [Usage]({{< ref "components/display/sdl#sdl" >}})
- :apiref:`sdl/sdl_touchscreen.h`
- [Edit this page on GitHub](https://github.com/clydebarrow/esphome-docs-hugo/blob/current/content/components/touchscreen/sdl.md)
