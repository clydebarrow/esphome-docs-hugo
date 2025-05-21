---
description: "Command Line Interface"
title: "Command Line Interface"
---

{{< seo description="" image="" >}}

## Base Usage

ESPHome's command line interface always has the following format

```console
esphome [OPTIONS] <COMMAND> <CONFIGURATION...> [ARGUMENTS]

```
{{< note >}}
You can specify multiple configuration files in the command line interface for some commands,
just list all files after the <COMMAND> like so:

```console
esphome run livingroom.yaml kitchen.yaml
```

{{< /note >}}
## `--help` Option

{{< option "-h|--help" >}}
Output possible <commands> and [arguments].
Note: you can also use `--help` for any command to get arguments specific to that command.
{{< /option >}}
```console
esphome <some_command> --help

```
## `--verbose` Option

{{< option "-v|--verbose" >}}
Enable verbose esphome logs.
Can also be enabled via environment variable `ESPHOME_VERBOSE=true`.

{{< /option >}}
## `--quiet` Option

{{< option "-q|--quiet" >}}
Disable all esphome logs.

{{< /option >}}
## `--substitution` Option

*(can be issued multiple times)*

{{< option "-s|--substitution KEY VALUE" >}}
Defines or overrides substitution KEY with value VALUE.

{{< /option >}}
Please see [command line substitutions]({{< ref "components/substitutions#command-line-substitutions" >}}) for details.

## `run` Command

The `esphome run <CONFIG>` command is the most common command for ESPHome. It

* Validates the configuration
* Compiles a firmware
* Uploads the firmware (over OTA or USB)
* Starts the log view


{{< option "--device UPLOAD_PORT" >}}
Manually specify the upload port/IP to use. For example `/dev/cu.SLAB_USBtoUART`, or `192.168.1.176`
to perform an OTA.

{{< /option >}}
{{< option "--upload_speed BAUD_RATE" >}}
The upload speed for serial flashing defaults to 460800 or as set with the environment variable `ESPHOME_UPLOAD_SPEED`.
This can be overridden in the platformio options on a per-config
basis, or set with this option at the time of uploading.

{{< /option >}}
{{< option "--no-logs" >}}
Disable starting log view.

{{< /option >}}
{{< option "--topic TOPIC" >}}
Manually set the topic to subscribe to for MQTT logs (defaults to the one in the configuration).

{{< /option >}}
{{< option "--username USERNAME" >}}
Manually set the username to subscribe with for MQTT logs (defaults to the one in the configuration).

{{< /option >}}
{{< option "--password PASSWORD" >}}
Manually set the password to subscribe with for MQTT logs (defaults to the one in the configuration).

{{< /option >}}
{{< option "--client-id CLIENT_ID" >}}
Manually set the client ID to subscribe with for MQTT logs (defaults to a randomly chosen one).

{{< /option >}}
{{< option "--host-port HOST_PORT" >}}
Specify the host port to use for legacy Over the Air uploads.

{{< /option >}}
{{< option "--reset" >}}
If set, reset the device before starting the logs. May also be configured with the environment variable
`ESPHOME_SERIAL_LOGGING_RESET=true`.

{{< /option >}}
## `config` Command


The `esphome config <CONFIG>` validates the configuration and displays the validation result.


## `compile` Command


The `esphome compile <CONFIG>` validates the configuration and compiles the firmware.

{{< option "--only-generate" >}}
If set, only generates the C++ source code and does not compile the firmware.

{{< /option >}}
## `upload` Command


The `esphome upload <CONFIG>` validates the configuration and uploads the most recent firmware build.

{{< option "--device UPLOAD_PORT" >}}
Manually specify the upload port/IP address to use. For example `/dev/cu.SLAB_USBtoUART`, or `192.168.1.176`
to perform an OTA.

{{< /option >}}
{{< option "--upload_speed BAUD_RATE" >}}
The upload speed for serial flashing defaults to 460800 or as set with the environment variable `ESPHOME_UPLOAD_SPEED`.
This can be overridden in the platformio options on a per-config
basis, or set with this option at the time of uploading.

{{< /option >}}
{{< option "--host-port HOST_PORT" >}}
Specify the host port to use for legacy Over the Air uploads.

{{< /option >}}
## `clean-mqtt` Command


The `esphome clean-mqtt <CONFIG>` cleans retained MQTT discovery messages from the MQTT broker.
See [Using with Home Assistant MQTT entities]({{< ref "components/mqtt#mqtt-using_with_home_assistant_entities" >}}).

{{< option "--topic TOPIC" >}}
Manually set the topic to clean retained messages from (defaults to the MQTT discovery topic of the
node).

{{< /option >}}
{{< option "--username USERNAME" >}}
Manually set the username to subscribe with.

{{< /option >}}
{{< option "--password PASSWORD" >}}
Manually set the password to subscribe with.

{{< /option >}}
{{< option "--client-id CLIENT_ID" >}}
Manually set the client ID to subscribe with.

{{< /option >}}
## `wizard` Command


The `esphome wizard <CONFIG>` command starts the ESPHome configuration creation wizard.

## `mqtt-fingerprint` Command


The `esphome mqtt-fingerprint <CONFIG>` command shows the MQTT SSL fingerprints of the remote used
for SSL MQTT connections. See [SSL Fingerprints]({{< ref "components/mqtt#mqtt-ssl_fingerprints" >}}).

## `version` Command


The `esphome version` command shows the current ESPHome version and exits.

## `clean` Command


The `esphome clean <CONFIG>` command cleans all build files and can help with some build issues.

## `dashboard` Command


The `esphome dashboard <CONFIG>` command starts the ESPHome dashboard server for using ESPHome
through a graphical user interface. This command accepts a configuration directory instead of a
single configuration file.

{{< option "--address ADDRESS" >}}
Manually set the address to bind to (defaults to 0.0.0.0)

{{< /option >}}
{{< option "--port PORT" >}}
Manually set the HTTP port to open connections on (defaults to 6052)

{{< /option >}}
{{< option "--socket SOCKET" >}}
Manually set the unix socket to bind to. If specified along with `--address` or `--port` the values
for those parameters will be ignored. Cannot be used along with `--systemd-socket`.

{{< /option >}}
{{< option "--username USERNAME" >}}
The optional username to require for authentication.

{{< /option >}}
{{< option "--password PASSWORD" >}}
The optional password to require for authentication.

{{< /option >}}
{{< option "--open-ui" >}}
If set, opens the dashboard UI in a browser once the server is up and running. Does not work when using
`--socket`.

{{< /option >}}
## `logs` Command


The `esphome logs <CONFIG>` command validates the configuration and shows all logs.

{{< option "--topic TOPIC" >}}
Manually set the topic to subscribe to.

{{< /option >}}
{{< option "--username USERNAME" >}}
Manually set the username.

{{< /option >}}
{{< option "--password PASSWORD" >}}
Manually set the password.

{{< /option >}}
{{< option "--client-id CLIENT_ID" >}}
Manually set the client id.

{{< /option >}}
{{< option "--device SERIAL_PORT" >}}
Manually specify a serial port/IP to use. For example `/dev/cu.SLAB_USBtoUART`.

{{< /option >}}
{{< option "--reset" >}}
If set, reset the device before starting the logs. May also be configured with the environment variable
`ESPHOME_SERIAL_LOGGING_RESET=true`.

{{< /option >}}
## Using Bash or ZSH auto-completion

ESPHome's command line interface provides the ability to use auto-completion features provided by Bash or ZSH.

You can register ESPHome for auto-completion by adding the following to your ~/.bashrc file:

```console
eval "$(register-python-argcomplete esphome)"

```
For more information, see [argcomplete ](https://kislyuk.github.io/argcomplete/) documentation.

