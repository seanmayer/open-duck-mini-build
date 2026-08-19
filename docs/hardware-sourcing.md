# Hardware Sourcing Tracker

This tracker records robot-specific parts as they are ordered, received, checked, and eventually installed.

## Status Summary

- Printing phase: complete, including optional TPU foot bottoms.
- Hardware sourcing: started.
- First received robot-specific electronics: foot micro switches.
- Power hardware has started arriving: charger and 18650 cells are received, with the in-robot protection/regulation path still to confirm.

## Parts Tracker

| Group | Item | Qty | Status | Last Updated | Notes |
| --- | --- | ---: | --- | --- | --- |
| Foot sensors | SS-10 style micro switch, pin plunger, SPDT, 10A 250V AC | 4 | Received | 2026-08-19 | Intended for foot contact sensing. Verify COM/NO/NC terminals with a multimeter before wiring. |
| Motion | Feetech STS3215 serial bus servos | 14 | Ordered / awaiting delivery | 2026-08-19 | Main robot servos. Verify model, voltage, horns, and included hardware on arrival. |
| Electronics | Serial bus servo driver board | 1 | Ordered / awaiting delivery | 2026-08-19 | Interface between the Raspberry Pi and STS3215 servo bus. |
| Brain | Raspberry Pi Zero 2 W | 1 | To order / confirm | 2026-08-19 | Needed for the stock runtime. Do not substitute a Pico for the main computer. |
| Storage | 64GB SanDisk microSD card | 1 | Ordered / awaiting delivery | 2026-08-19 | Storage for Raspberry Pi OS and robot runtime. |
| Sensors | BNO055 IMU breakout | 1 | Ordered / awaiting delivery | 2026-08-19 | Orientation sensor. Verify pinout and I2C wiring before mounting. |
| Motion | SG90 micro servos | 2 | To order / confirm | 2026-08-19 | Used for smaller actuation if following the full upstream build. |
| Power | Nitecore Intellicharger NEW i2 battery charger | 1 | Received | 2026-08-19 | External charger for loose cells. Store and charge lithium cells safely. |
| Power | P30B 18650 Li-ion cells, 3000mAh, 30A, 3.7V | 2 | Received | 2026-08-19 | Main battery cells. Check voltage before first use and do not wire into the robot until the BMS, regulator, and power path are confirmed. |
| Power | 2S holder, BMS/protection, regulator, switch, and power wiring | 1 set | To order / confirm | 2026-08-19 | Required before connecting batteries to servos or electronics. |
| Mechanical | Bearings and remaining robot-specific hardware | Per BOM | To order / confirm | 2026-08-19 | Check against the official BOM and printed part fit. |
| Wiring | Connectors, leads, and cable management | As needed | To order / confirm | 2026-08-19 | Phase 1 wire and heat shrink are available, but final connector requirements still need confirming. |

## Received Photos

| Item | Photo |
| --- | --- |
| Foot micro switches | [micro-switches-2026-08-19.jpeg](../photos/hardware/micro-switches-2026-08-19.jpeg) |
| Nitecore i2 battery charger | [nitecore-i2-charger-2026-08-19.jpeg](../photos/hardware/nitecore-i2-charger-2026-08-19.jpeg) |
| P30B 18650 battery cells | [18650-cells-2026-08-19.jpeg](../photos/hardware/18650-cells-2026-08-19.jpeg) |

## Next Checks

- Test-fit the switches in the feet.
- Confirm which switch terminals are common, normally open, and normally closed.
- Check the initial voltage of each 18650 cell with a multimeter and store the cells safely.
- Do not connect the cells to the robot until the BMS/protection, regulator, switch, and wiring plan are confirmed.
- Update this tracker as each ordered electronics package arrives.
