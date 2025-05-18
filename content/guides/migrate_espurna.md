---
description: "Migrating from ESPurna"
title: "Migrating from ESPurna"
---

{{< seo description="" image="" >}}

Migrating from previous ESPurna setups is very easy. You just need to have
ESPHome create a binary for you and then upload that in the ESPurna web interface.

## Getting Binary

First follow the guides for the [different supported devices]({{< ref "components/_index#devices" >}}) and create a configuration
file. Then, generate and download the binary:

- **Using the Home Assistant add-on/dashboard**: Just click the `COMPILE`
  button, wait for the compilation to end and press the `DOWNLOAD BINARY`
  button.

![- **Using the command line**: run ``esphome compile livingroom.yaml`` (replacing](../images/download_binary.png)
*- **Using the command line**: run ``esphome compile livingroom.yaml`` (replacing*

  `livingroom.yaml` with your configuration file of course) and navigate to the
  `<NODE_NAME>/.pioenvs/<NODE_NAME>/` folder. There you will find a `firmware.bin` file,
  this is the binary you will upload.

## Uploading Binary

To upload the binary, navigate to the ESPurna web interface and enter the
"General " section.

![In the "Upgrade" section, choose the binary you previously downloaded and press "Upgrade".](../images/espurna_ota.png)
*In the "Upgrade" section, choose the binary you previously downloaded and press "Upgrade".*

If everything succeeds, you should now have ESPHome on your node 🎉

{{< note >}}
with ESPHome, you in most cases won't need to worry about the available flash size, as
the binary only ever includes the code that you are actually using.

{{< /note >}}
![Happy Hacking!](../images/espurna_upload.png)
*Happy Hacking!*


## See Also

- [/components/esp8266]({{< ref "/components/esp8266" >}})
- [/components/esp32]({{< ref "/components/esp32" >}})
- [migrate_espeasy]({{< ref "migrate_espeasy/" >}})
- [migrate_sonoff_tasmota]({{< ref "migrate_sonoff_tasmota/" >}})
- :ghedit:`Edit`
