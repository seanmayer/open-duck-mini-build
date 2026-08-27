# Hardware Sourcing Tracker

This tracker records robot-specific parts as they are ordered, received, checked, and eventually installed.

## Status Summary

- Printing phase: complete, including optional TPU foot bottoms.
- Hardware sourcing: in progress, with a third batch of power-protection and Raspberry Pi support parts received.
- First received robot-specific electronics: foot micro switches.
- Motion hardware now includes all 14 STS3215 serial bus servos and the SG90 micro servos; the BNO055 IMU has also arrived.
- Power hardware now includes the charger, cells, 5V UBEC, BMS boards, main power switch, XT30 connectors, DC adapters, red/black wire, and a compact replacement 2S holder that fits the reprinted rear panel.
- The in-robot battery path is not complete until the BMS wiring/specification and full switched wiring path are confirmed.

## Parts Tracker

| Group | Item | Qty | Status | Last Updated | Notes |
| --- | --- | ---: | --- | --- | --- |
| Foot sensors | SS-10 style micro switch, pin plunger, SPDT, 10A 250V AC | 4 | Received | 2026-08-19 | Intended for foot contact sensing. Verify COM/NO/NC terminals with a multimeter before wiring. |
| Motion | Feetech STS3215 serial bus servos, 7.4V, 1:345 | 14 | Received | 2026-08-24 | Main robot servos. Arrival photo confirms 14 units; each came with its cable, horn/disc and mounting screws. Keep each servo's accessories together and do not permanently fit horns until the servos are centred. |
| Electronics | Serial bus servo driver board | 1 | Ordered / awaiting delivery | 2026-08-19 | Interface between the Raspberry Pi and STS3215 servo bus. |
| Brain | Raspberry Pi Zero 2 W | 1 | To order / confirm | 2026-08-19 | Needed for the stock runtime. Do not substitute a Pico for the main computer. |
| Storage | 64GB SanDisk microSD card | 1 | Ordered / awaiting delivery | 2026-08-19 | Storage for Raspberry Pi OS and robot runtime. |
| Sensors | BNO055 IMU breakout | 1 | Received | 2026-08-25 | Orientation sensor received with header pins. Verify pinout and I2C wiring before mounting or soldering headers. |
| Motion | SG90 9g micro servos | 2 required | Received | 2026-08-21 | Multi-pack received with horns and mounting hardware. Bench-test direction and travel before installation. |
| Power | Nitecore Intellicharger NEW i2 battery charger | 1 | Received | 2026-08-19 | External charger for loose cells. Store and charge lithium cells safely. |
| Power | P30B 18650 Li-ion cells, 3000mAh, 30A, 3.7V | 2 | Received | 2026-08-19 | Main battery cells. Check voltage before first use and do not wire into the robot until the BMS, regulator, and power path are confirmed. |
| Power | 2S 18650 battery holders with leads | 2 | Received - not selected for final fit | 2026-08-21 | The outer casing does not fit the rear-panel mounting area. Retain as spares or bench items; do not insert cells for the robot build. |
| Power | Compact replacement 2S 18650 battery holder | 1 | Received / fit checked | 2026-08-26 | Fits the reprinted rear panel. Confirm contact quality, series layout, and access to the BMS midpoint before installing cells or starting power wiring. |
| Power | UBEC, 2-7S input, regulated 5V 5A output | 1 | Received | 2026-08-21 | Intended for the 5V electronics rail only. Verify output and current requirements before connecting the Raspberry Pi or other electronics. |
| Power | 2S BMS/protection boards, labelled 4.2V / 8.4V and 20A | 4 | Received | 2026-08-23 | Verify the exact wiring, protection features, and safe continuous-current rating before use. The board label is 20A, not 200A. |
| Power | Panel-mount ON/OFF main power switch with supplied leads/connectors | 1 | Received | 2026-08-25 | Verify terminal function, switch rating, mounting fit, and polarity before wiring it into the protected battery path. |
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

## Next Checks

- Test-fit the switches in the feet.
- Confirm which switch terminals are common, normally open, and normally closed.
- Check the initial voltage of each 18650 cell with a multimeter and store the cells safely.
- Check the battery-holder polarity and series wiring without installing the cells.
- Verify the UBEC produces a stable 5V output before connecting any electronics.
- Identify the BMS terminals from its documentation and verify it is suitable for the intended 2S pack before connecting cells or a load.
- Measure the DC barrel adapter output voltage and polarity before use; do not rely on the photo or connector shape.
- Bench-test the SG90 servos and test-fit the 8 x 22 x 7 mm bearings.
- Confirm the wire gauge, DC barrel dimensions/polarity, and XT30 polarity before building leads.
- Do not connect the cells to the robot until the BMS wiring/specification, switch terminal mapping, and complete wiring plan are confirmed.
- Update this tracker as each ordered electronics package arrives.
