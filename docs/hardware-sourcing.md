# Hardware Sourcing Tracker

This tracker records robot-specific parts as they are ordered, received, checked, and eventually installed.

## Status Summary

- Printing phase: complete, including optional TPU foot bottoms.
- Hardware sourcing: in progress, with the main motion hardware and battery-pack electronics now received.
- First received robot-specific electronics: foot micro switches.
- Motion hardware now includes all 14 STS3215 serial bus servos, two Waveshare serial bus servo driver boards, and the SG90 micro servos; the BNO055 IMU has also arrived.
- Power hardware now includes the charger, cells, 5V UBEC, BMS boards, main power switch, XT30 connectors, DC adapters, red/black wire, and compact replacement 2S holder.
- The compact holder, BMS, rocker switch, USB-C charging board, UBEC, switched 5V output, and raw 7.4V branch are now assembled and tested as a power-pack subassembly.
- The power pack is not yet connected to the full robot; USB-C charging still needs a controlled test before regular use.
- Next planned electronics task: bench-power one Waveshare servo controller from the switched 7.4V rail, connect it to a laptop by USB, and program/check one STS3215 servo ID at a time.

## Parts Tracker

| Group | Item | Qty | Status | Last Updated | Notes |
| --- | --- | ---: | --- | --- | --- |
| Foot sensors | SS-10 style micro switch, pin plunger, SPDT, 10A 250V AC | 4 | Received | 2026-08-19 | Intended for foot contact sensing. Verify COM/NO/NC terminals with a multimeter before wiring. |
| Motion | Feetech STS3215 serial bus servos, 7.4V, 1:345 | 14 | Received | 2026-08-24 | Main robot servos. Arrival photo confirms 14 units; each came with its cable, horn/disc and mounting screws. Keep each servo's accessories together and do not permanently fit horns until the servos are centred. |
| Electronics | Waveshare serial bus servo driver board | 2 | Received / bench setup planned | 2026-09-06 | Interface between a laptop or Raspberry Pi and the STS3215 servo bus. Only one board is needed to program the 14 servos one at a time; the second board is a spare or future second bus. Planned first use is laptop over USB plus switched 7.4V servo power into the controller power input. |
| Brain | Raspberry Pi Zero 2 W | 1 | Received | 2026-09-20 | Needed for the stock runtime. Keep the initial servo-ID work on the laptop; set up the Pi after the controller bench test. Do not substitute a Pico for the main computer. |
| Storage | 64GB SanDisk microSD card | 1 | Ordered / awaiting delivery | 2026-08-19 | Storage for Raspberry Pi OS and robot runtime. |
| Sensors | BNO055 IMU breakout | 1 | Received | 2026-08-25 | Orientation sensor received with header pins. Verify pinout and I2C wiring before mounting or soldering headers. |
| Motion | SG90 9g micro servos | 2 required | Received | 2026-08-21 | Multi-pack received with horns and mounting hardware. Bench-test direction and travel before installation. |
| Power | Nitecore Intellicharger NEW i2 battery charger | 1 | Received | 2026-08-19 | External charger for loose cells. Store and charge lithium cells safely. |
| Power | P30B 18650 Li-ion cells, 3000mAh, 30A, 3.7V | 2 | Installed / tested in pack | 2026-08-29 | Main battery cells. Each cell measured approximately 3.5V during pack testing; total series voltage measured approximately 7V. Remove cells when the unfinished robot is not being worked on. |
| Power | 2S 18650 battery holders with leads | 2 | Received - not selected for final fit | 2026-08-21 | The outer casing does not fit the rear-panel mounting area. Retain as spares or bench items; do not insert cells for the robot build. |
| Power | Compact replacement 2S 18650 battery holder | 1 | Installed / tested | 2026-08-29 | Fits the reprinted rear panel and is used in the completed 2S pack. Contact issue during testing was resolved by reseating the cell; midpoint access is confirmed. |
| Power | UBEC, 2-7S input, regulated 5V 5A output | 1 | Installed / tested | 2026-08-29 | Intended for the 5V electronics rail only. Output tested at approximately 5V with the switch ON and 0V with the switch OFF. |
| Power | 2S BMS/protection boards, labelled 4.2V / 8.4V and 20A | 4 | Installed / tested | 2026-08-29 | One board wired to 0V, 4.2V midpoint, 8.4V positive, and P+/P- output rails. Pack protection is wired; USB-C charging controlled test still pending. Spare boards remain. |
| Power | Panel-mount ON/OFF main power switch with supplied leads/connectors | 1 | Installed / tested | 2026-08-29 | Installed in the protected negative rail after BMS P-. Continuity verified: ON = continuity, OFF = open circuit. |
| Bench power | UK mains DC barrel power adapter | 1 | Received | 2026-08-23 | Output label is not visible in the arrival photo. Measure voltage, polarity, connector size, and current capability before connecting it to anything. |
| Raspberry Pi support | GeekPi 40-pin header kit | 13-piece kit | Received | 2026-08-23 | Includes GPIO header/extension options. Confirm the required orientation and whether soldering is needed once the Raspberry Pi arrives. |
| Bench setup | 4K/UHD HDMI cable | 1 | Received | 2026-08-23 | Available for Raspberry Pi display and setup work. |
| Mechanical | 8 x 22 x 7 mm bearings | 20 | Received | 2026-08-21 | Check quantity, free rotation, and fit against the printed parts and official BOM. |
| Mechanical | Remaining robot-specific hardware | Per BOM | To order / confirm | 2026-08-21 | Check outstanding fasteners and other mechanical parts against the official BOM. |
| Assembly | Loctite 243 medium-strength threadlocker, 5 ml | 1 | Received | 2026-08-21 | Use sparingly on final metal-to-metal threaded joints; avoid contact with plastic parts. |
| Wiring | XT30 connector pairs with heat-shrink tubing | 12 pairs | Received | 2026-08-21 | Confirm polarity before soldering and insulate every joint. |
| Wiring | DC barrel plug/socket screw-terminal adapters | 1 kit | Received | 2026-08-21 | Confirm connector size, centre polarity, voltage, and current suitability before use. |
| Wiring | Red and black power wire | 2 rolls | Received | 2026-08-21 | Confirm conductor gauge and current capacity before assigning it to the battery or servo power path. |
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
| Raspberry Pi Zero 2 W arrival | [raspberry-pi-zero-2w-arrival-2026-09-20.jpg](../photos/hardware/raspberry-pi-zero-2w-arrival-2026-09-20.jpg), [raspberry-pi-zero-2w-arrival-2026-09-20-2.jpg](../photos/hardware/raspberry-pi-zero-2w-arrival-2026-09-20-2.jpg) |

## Next Checks

- Verify USB-C charging operation in a controlled test before relying on onboard charging.
- Keep the 18650 cells removed whenever the unfinished robot is not being worked on.
- Connect the spliced switched 7.4V branch to the Waveshare controller power input, preferably the green screw terminal for the first bench test.
- Verify correct polarity and about 7.0-8.4V at the Waveshare controller input with a multimeter before connecting any servo. The free branch measured 7.03V on 2026-09-16 and is now connected to the controller.
- Connect the Waveshare controller to a laptop over USB for the first servo ID/programming tests; leave the Raspberry Pi setup for later.
- Confirm the Raspberry Pi Zero 2 W and microSD card contents, then begin Pi OS/runtime setup after the laptop servo-controller test.
- Connect only one STS3215 servo at a time for ID checking/programming, then label each servo before moving to the next.
- Do not use the UBEC 5V output connector to power the STS3215 servos or the servo controller's motor-power rail.
- Connect the regulated 5V output to the appropriate electronics only after checking polarity and voltage.
- Bench-test the SG90 servos and test-fit the 8 x 22 x 7 mm bearings.
- Test-fit the switches in the feet and confirm COM/NO/NC terminals.
- Measure the DC barrel adapter output voltage and polarity before use; do not rely on the photo or connector shape.
- Confirm XT30 polarity before building final leads.
- Update this tracker as each ordered electronics package arrives.
