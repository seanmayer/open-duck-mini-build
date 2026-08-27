# Roadmap

This roadmap keeps the build phased so purchases and work stay manageable.

## Phase 1 - Workshop And Core Tools

Status: Complete enough to move forward.

Goal: Prepare the tools and consumables needed for 3D printing, mechanical assembly, soldering, and basic electronics work.

Key outputs:

- Core workshop tools purchased.
- Soldering setup ready.
- Mechanical fasteners and heat-set inserts ready.
- Basic wiring consumables ready.
- Phase 1 BOM checklist documented.

## Phase 2 - Source Robot Hardware

Status: In progress.

Goal: Build a reliable shopping list from the official Open Duck Mini BOM, then source parts in sensible batches.

Planned groups:

- Motion: STS3215 serial servos, SG90 servos, and any required servo programming tools.
- Brain: Raspberry Pi Zero 2 W, microSD card, and setup notes.
- Electronics: servo controller, IMU, contact switches, wiring, and connectors.
- Power: cells, battery holder, BMS, regulators, charger board, switch, and connectors.
- Mechanical extras: bearings and any missing fasteners not covered by the starter assortment.

Current progress:

- Foot micro switches have arrived.
- Battery charger and 18650 cells have arrived.
- All 14 Feetech STS3215 main servos have arrived with their cables, horns/discs, and mounting screws. Mechanical dry fitting can begin; servo centring and final horn installation wait for the verified power and controller setup.
- The BNO055 IMU breakout and its header pins have arrived. Keep it unmounted until its orientation, pinout, and I2C wiring are confirmed.
- SG90 micro servos and 8 x 22 x 7 mm bearings have arrived.
- Two 2S battery holders, a 5V 5A UBEC, XT30 connectors, DC barrel adapters, and red/black wire have arrived.
- The original battery holders did not fit the rear-panel mounting area. A compact replacement holder has arrived and fits the reprinted rear panel; its wiring and BMS connections still need verifying before cells are installed.
- Four 2S BMS/protection boards marked for 4.2V / 8.4V packs and labelled 20A have arrived; their wiring and verified current capability still need checking before use.
- A DC barrel power adapter, 4K HDMI cable, and GeekPi 40-pin GPIO header kit are ready for later bench setup.
- Loctite 243 is ready for final metal fasteners.
- The main power switch has arrived; its terminal mapping, mounting fit, and wiring still need to be confirmed. The BMS wiring/specification must also be verified before the cells are connected.
- Remaining robot-specific hardware is tracked in [Hardware Sourcing Tracker](hardware-sourcing.md).

## Phase 3 - Print And Fit Check

Goal: Print the robot parts, clean them up, and check fit before committing expensive electronics to the assembly.

Planned work:

- Download official files from upstream sources.
- Record slicer settings.
- Photograph successful and failed prints.
- Check critical tolerances with calipers.
- Test heat-set insert installation on scrap or non-critical parts.

## Phase 4 - Assembly

Goal: Assemble the robot mechanically and electrically.

Planned work:

- Assign servo IDs before final installation.
- Assemble legs, torso, and head.
- Route wiring neatly.
- Install Raspberry Pi and controller electronics.
- Perform power checks before first boot.

## Phase 5 - Calibration And First Motion

Goal: Bring the robot up safely and get repeatable baseline movement.

Planned work:

- Calibrate servos.
- Test IMU readings.
- Validate contact switches.
- Run basic pose and balance checks.
- Document first stand and first walk attempts.

## Phase 6 - Software Experiments

Goal: Extend the build beyond the stock assembly once the robot is mechanically stable.

Possible work:

- Runtime setup scripts.
- Calibration helpers.
- Telemetry logging.
- Computer vision experiments.
- Voice or AI interaction experiments.
- Custom behavior demos for portfolio use.
