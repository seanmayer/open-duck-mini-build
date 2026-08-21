# Hardware Sourcing Tracker

This tracker records robot-specific parts as they are ordered, received, checked, and eventually installed.

## Status Summary

- Printing phase: complete, including optional TPU foot bottoms.
- Hardware sourcing: in progress, with a second batch of motion, mechanical, wiring, and power parts received.
- First received robot-specific electronics: foot micro switches.
- Motion hardware now includes the SG90 micro servos; the main STS3215 servo order is still awaiting delivery.
- Power hardware now includes the charger, cells, 2S holders, 5V UBEC, XT30 connectors, DC adapters, and red/black wire.
- The in-robot battery path is not complete until the BMS/protection and main power switch are confirmed.

## Parts Tracker

| Group | Item | Qty | Status | Last Updated | Notes |
| --- | --- | ---: | --- | --- | --- |
| Foot sensors | SS-10 style micro switch, pin plunger, SPDT, 10A 250V AC | 4 | Received | 2026-08-19 | Intended for foot contact sensing. Verify COM/NO/NC terminals with a multimeter before wiring. |
| Motion | Feetech STS3215 serial bus servos | 14 | Ordered / awaiting delivery | 2026-08-19 | Main robot servos. Verify model, voltage, horns, and included hardware on arrival. |
| Electronics | Serial bus servo driver board | 1 | Ordered / awaiting delivery | 2026-08-19 | Interface between the Raspberry Pi and STS3215 servo bus. |
| Brain | Raspberry Pi Zero 2 W | 1 | To order / confirm | 2026-08-19 | Needed for the stock runtime. Do not substitute a Pico for the main computer. |
| Storage | 64GB SanDisk microSD card | 1 | Ordered / awaiting delivery | 2026-08-19 | Storage for Raspberry Pi OS and robot runtime. |
| Sensors | BNO055 IMU breakout | 1 | Ordered / awaiting delivery | 2026-08-19 | Orientation sensor. Verify pinout and I2C wiring before mounting. |
| Motion | SG90 9g micro servos | 2 required | Received | 2026-08-21 | Multi-pack received with horns and mounting hardware. Bench-test direction and travel before installation. |
| Power | Nitecore Intellicharger NEW i2 battery charger | 1 | Received | 2026-08-19 | External charger for loose cells. Store and charge lithium cells safely. |
| Power | P30B 18650 Li-ion cells, 3000mAh, 30A, 3.7V | 2 | Received | 2026-08-19 | Main battery cells. Check voltage before first use and do not wire into the robot until the BMS, regulator, and power path are confirmed. |
| Power | 2S 18650 battery holders with leads | 2 | Received | 2026-08-21 | Verify series wiring, polarity, contact tension, and fit before inserting cells. Holders do not provide battery protection. |
| Power | UBEC, 2-7S input, regulated 5V 5A output | 1 | Received | 2026-08-21 | Intended for the 5V electronics rail only. Verify output and current requirements before connecting the Raspberry Pi or other electronics. |
| Power | BMS/protection and main power switch | 1 set | To order / confirm | 2026-08-21 | Still required before the battery path can be assembled or energised. |
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

## Next Checks

- Test-fit the switches in the feet.
- Confirm which switch terminals are common, normally open, and normally closed.
- Check the initial voltage of each 18650 cell with a multimeter and store the cells safely.
- Check the battery-holder polarity and series wiring without installing the cells.
- Verify the UBEC produces a stable 5V output before connecting any electronics.
- Bench-test the SG90 servos and test-fit the 8 x 22 x 7 mm bearings.
- Confirm the wire gauge, DC barrel dimensions/polarity, and XT30 polarity before building leads.
- Do not connect the cells to the robot until the BMS/protection, main switch, and complete wiring plan are confirmed.
- Update this tracker as each ordered electronics package arrives.
