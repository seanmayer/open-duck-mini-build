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
- SG90 micro servos and 8 x 22 x 7 mm bearings have arrived.
- Two 2S battery holders, a 5V 5A UBEC, XT30 connectors, DC barrel adapters, and red/black wire have arrived.
- Loctite 243 is ready for final metal fasteners.
- In-robot BMS/protection and main switching still need to be confirmed before the cells are connected.
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
