# Hardware Sourcing Tracker

This tracker records robot-specific parts as they are ordered, received, checked, and eventually installed.

## Status Summary

- Printing phase: complete, including optional TPU foot bottoms.
- Hardware sourcing: in progress, with the main motion hardware and battery-pack electronics now received.
- First received robot-specific electronics: foot micro switches.
- Motion hardware now includes all 14 STS3215 serial bus servos, two Waveshare serial bus servo driver boards, and the SG90 micro servos; the BNO055 IMU has also arrived.
- Power hardware now includes the charger, cells, 5V UBEC, BMS boards, main power switch, XT30 connectors, DC adapters, red/black wire, and compact replacement 2S holder.
- The compact holder, BMS, rocker switch, USB-C charging board, UBEC, switched 5V output, and raw battery-voltage branch are assembled. Pack voltages, switched output, and UBEC output have been checked; USB-C charging still needs a controlled test before regular use.
- The switched raw battery branch is connected to the Waveshare controller and all 14 main servos have responded to both laptop and Pi status checks. On 2026-11-09, all reported torque disabled, error status 0, and 7.9–8.0V. Loaded supply testing and final Pi/sensor power integration remain outstanding.
- The replacement Pi Zero 2 W with a pre-soldered GPIO header has arrived. It boots from the existing microSD card and accepts SSH; the existing v2 runtime installation passes its dependency check.
- The USB OTG adapter/data cable is received and tested. Pi USB enumeration, Python serial-port access, and read-only servo communication are complete. The BNO055 is still unconnected; its wiring and sensor checks are next. See the [current checkpoint](build-log.md#2026-11-09---pi-to-servo-communication-confirmed).

## Parts Tracker

| Group | Item | Qty | Status | Last Updated | Notes |
| --- | --- | ---: | --- | --- | --- |
| Foot sensors | SS-10 style micro switch, pin plunger, SPDT, 10A 250V AC | 4 | Received | 2026-08-19 | Intended for foot contact sensing. Verify COM/NO/NC terminals with a multimeter before wiring. |
| Motion | Feetech STS3215 serial bus servos, 7.4V, 1:345 | 14 | Assembled / Pi read-only checks passed | 2026-11-09 | Persistent S01–S14 IDs and full-chain ping/status responses verified from the Pi. All torque disabled, error status 0, and 7.9–8.0V reported. Joint limits and coordinated motion remain unverified. |
| Electronics | Waveshare serial bus servo driver board | 2 | Received / Pi communication verified | 2026-11-09 | One board connects the full servo chain to the Pi over USB with separate switched battery power. USB detection, serial access, and read-only checks passed. The second remains available as a spare/future bus. |
| Brain | Original Raspberry Pi Zero 2 W | 1 | Header damaged / replaced for this build | 2026-11-07 | Originally received 2026-09-20. GPIO header damaged during beginner soldering/desoldering; the board still booted and accepted SSH, but damaged header connections were not validated. |
| Brain | Replacement Raspberry Pi Zero 2 W with pre-soldered GPIO header | 1 | Boot, SSH, and servo communication verified | 2026-11-09 | Existing Debian 12 / aarch64 installation and v2 runtime dependency check retained. USB serial access at 1,000,000 baud and read-only checks of all 14 servos passed. Sensor integration and full runtime operation are pending. |
| Storage | 64GB SanDisk microSD card | 1 | Installed / boot verified | 2026-11-07 | Existing OS and runtime environment retained on the replacement Pi; no fresh clone or reinstallation was needed for this checkpoint. |
| Sensors | BNO055 IMU breakout | 1 | Received / not connected | 2026-11-09 | Confirmed still unconnected at the Pi-to-servo checkpoint. Verify the actual breakout labels, supply requirements, and mounting orientation before wiring; I2C detection and sensor readings are not yet tested. |
| Motion | SG90 9g micro servos | 2 required | Received | 2026-08-21 | Multi-pack received with horns and mounting hardware. Bench-test direction and travel before installation. |
| Power | Nitecore Intellicharger NEW i2 battery charger | 1 | Received | 2026-08-19 | External charger for loose cells. Store and charge lithium cells safely. |
| Power | P30B 18650 Li-ion cells, 3000mAh, 30A, 3.7V | 2 | Installed / tested in pack | 2026-08-29 | Main battery cells. Each cell measured approximately 3.5V during pack testing; total series voltage measured approximately 7V. Remove cells when the unfinished robot is not being worked on. |
| Power | 2S 18650 battery holders with leads | 2 | Received - not selected for final fit | 2026-08-21 | The outer casing does not fit the rear-panel mounting area. Retain as spares or bench items; do not insert cells for the robot build. |
| Power | Compact replacement 2S 18650 battery holder | 1 | Installed / tested | 2026-08-29 | Fits the reprinted rear panel and is used in the completed 2S pack. Contact issue during testing was resolved by reseating the cell; midpoint access is confirmed. |
| Power | UBEC, 2-7S input, regulated 5V 5A output | 1 | Installed / tested | 2026-08-29 | Intended for the 5V electronics rail only. Output tested at approximately 5V with the switch ON and 0V with the switch OFF. |
| Power | 2S BMS/protection boards, labelled 4.2V / 8.4V and 20A | 4 | Installed / tested | 2026-08-29 | One board wired to 0V, 4.2V midpoint, 8.4V positive, and P+/P- output rails. Pack protection is wired; USB-C charging controlled test still pending. Spare boards remain. |
| Power | Panel-mount ON/OFF main power switch with supplied leads/connectors | 1 | Installed / tested | 2026-08-29 | Installed in the protected negative rail after BMS P-. Continuity verified: ON = continuity, OFF = open circuit. |
| Bench power | UK mains DC barrel power adapter | 1 | Received | 2026-08-23 | Output label is not visible in the arrival photo. Measure voltage, polarity, connector size, and current capability before connecting it to anything. |
| Raspberry Pi support | GeekPi 40-pin header kit | 13-piece kit | Received | 2026-11-07 | Previously sourced GPIO header/extension options. The replacement Pi already has its header soldered, so fitting one is no longer required for that board. |
| Bench setup | 4K/UHD HDMI cable | 1 | Received | 2026-08-23 | Available for Raspberry Pi display and setup work. |
| Mechanical | 8 x 22 x 7 mm bearings | 20 | Received | 2026-08-21 | Check quantity, free rotation, and fit against the printed parts and official BOM. |
| Mechanical | Remaining robot-specific hardware | Per BOM | To order / confirm | 2026-08-21 | Check outstanding fasteners and other mechanical parts against the official BOM. |
| Assembly | Loctite 243 medium-strength threadlocker, 5 ml | 1 | Received | 2026-08-21 | Use sparingly on final metal-to-metal threaded joints; avoid contact with plastic parts. |
| Wiring | XT30 connector pairs with heat-shrink tubing | 12 pairs | Received | 2026-08-21 | Confirm polarity before soldering and insulate every joint. |
| Wiring | DC barrel plug/socket screw-terminal adapters | 1 kit | Received | 2026-08-21 | Confirm connector size, centre polarity, voltage, and current suitability before use. |
| Wiring | Red and black power wire | 2 rolls | Received | 2026-08-21 | Confirm conductor gauge and current capacity before assigning it to the battery or servo power path. |
| Wiring | Micro-USB OTG adapter and USB data cable for Waveshare USB-C | 1 set | Received / communication tested | 2026-11-09 | Connects the Pi's USB data port to the controller. Detected as USB 1a86:55d3 and /dev/ttyACM0; stable by-id link and successful servo checks recorded in the build log. |
| Wiring | Remaining leads and cable management | As needed | To order / confirm | 2026-08-21 | Final connector and cable-routing requirements still need confirming during assembly. |

## Received Photos

| Item | Photo |
| --- | --- |
| Foot micro switches | [micro-switches-2026-08-19.jpeg](../photos/hardware/micro-switches-2026-08-19.jpeg) |
| Nitecore i2 battery charger | [nitecore-i2-charger-2026-08-19.jpeg](../photos/hardware/nitecore-i2-charger-2026-08-19.jpeg) |
| P30B 18650 battery cells | [18650-cells-2026-08-19.jpeg](../photos/hardware/18650-cells-2026-08-19.jpeg) |
| 2S 18650 battery holders | [18650-battery-holders-2026-08-21.jpeg](../photos/hardware/18650-battery-holders-2026-08-21.jpeg) |
| 5V 5A UBEC regulator | [5v-ubec-regulator-2026-08-21.jpeg](../photos/hardware/5v-ubec-regulator-2026-08-21.jpeg) |
| 8 x 22 x 7 mm bearings | [bearings-8x22x7-2026-08-21.jpeg](../photos/hardware/bearings-8x22x7-2026-08-21.jpeg) |
| DC barrel adapters | [dc-barrel-adapters-2026-08-21.jpeg](../photos/hardware/dc-barrel-adapters-2026-08-21.jpeg) |
| Loctite 243 threadlocker | [loctite-243-2026-08-21.jpeg](../photos/hardware/loctite-243-2026-08-21.jpeg) |
| Red and black power wire | [red-black-wire-2026-08-21.jpeg](../photos/hardware/red-black-wire-2026-08-21.jpeg) |
| SG90 micro servos | [sg90-servos-2026-08-21.jpeg](../photos/hardware/sg90-servos-2026-08-21.jpeg) |
| XT30 connector pairs | [xt30-connectors-2026-08-21.jpeg](../photos/hardware/xt30-connectors-2026-08-21.jpeg) |
| 2S BMS/protection boards | [2s-bms-protection-boards-2026-08-23.jpeg](../photos/hardware/2s-bms-protection-boards-2026-08-23.jpeg) |
| DC barrel power adapter | [dc-barrel-power-adapter-2026-08-23.jpeg](../photos/hardware/dc-barrel-power-adapter-2026-08-23.jpeg) |
| 4K/UHD HDMI cable | [hdmi-cable-4k-2026-08-23.jpeg](../photos/hardware/hdmi-cable-4k-2026-08-23.jpeg) |
| GeekPi 40-pin header kit | [raspberry-pi-40-pin-header-kit-2026-08-23.jpeg](../photos/hardware/raspberry-pi-40-pin-header-kit-2026-08-23.jpeg) |
| Completed 2S power-pack subassembly | [power-pack-complete-2026-08-29.jpg](../photos/hardware/power-pack-complete-2026-08-29.jpg) |
| Servo-controller 7.4V branch voltage test | [servo-controller-7v-branch-test-2026-09-16.jpg](../photos/hardware/servo-controller-7v-branch-test-2026-09-16.jpg) |
| Servo controller connected | [servo-controller-connected-2026-09-18.jpg](../photos/hardware/servo-controller-connected-2026-09-18.jpg) |
| STS3215 servos labelled | [sts3215-servos-labelled-2026-09-22.jpeg](../photos/hardware/sts3215-servos-labelled-2026-09-22.jpeg) |
| Raspberry Pi Zero 2 W arrival | [raspberry-pi-zero-2w-arrival-2026-09-20.jpg](../photos/hardware/raspberry-pi-zero-2w-arrival-2026-09-20.jpg), [raspberry-pi-zero-2w-arrival-2026-09-20-2.jpg](../photos/hardware/raspberry-pi-zero-2w-arrival-2026-09-20-2.jpg) |
| Replacement Raspberry Pi Zero 2 W with pre-soldered header | [raspberry-pi-zero-2w-presoldered-2026-11-07.jpg](../photos/hardware/raspberry-pi-zero-2w-presoldered-2026-11-07.jpg) |
| Pi-to-Waveshare servo communication setup | [pi-servo-communication-checkpoint-2026-11-09.jpg](../photos/hardware/pi-servo-communication-checkpoint-2026-11-09.jpg) |

## Next Checks

- Verify USB-C charging operation in a controlled test before relying on onboard charging.
- Keep the 18650 cells removed whenever the unfinished robot is not being worked on.
- Connect and test the BNO055 IMU next, confirming the breakout pinout and orientation first. Shut down the Pi and disconnect all power before GPIO wiring changes.
- Keep servo power off during I2C/sensor setup; USB detection and read-only servo communication have already passed.
- Recheck supply voltage and polarity after power-wiring changes. The existing switched battery branch is already connected to the controller; it is not a new splice task.
- Preserve the verified S01–S14 IDs and recorded joint mapping. Review runtime limits/startup behaviour and S09 clearance before any movement; successful read-only checks do not establish safe mechanical targets.
- Do not use the UBEC 5V output connector to power the STS3215 servos or the servo controller's motor-power rail.
- Connect the regulated 5V output to the appropriate electronics only after checking polarity and voltage.
- Bench-test the SG90 servos and test-fit the 8 x 22 x 7 mm bearings.
- Test-fit the switches in the feet and confirm COM/NO/NC terminals.
- Measure the DC barrel adapter output voltage and polarity before use; do not rely on the photo or connector shape.
- Confirm XT30 polarity before building final leads.
- Update this tracker as each ordered electronics package arrives.
