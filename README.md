# open-duck-mini-build

Building an open-source humanoid robot while exploring robotics, embedded systems, and AI.

This repository is my build journal for the Open Duck Mini v2: sourcing parts, printing and assembling the robot, documenting calibration, and eventually experimenting with the software stack.

## Attribution

Open Duck Mini is an open-source robotics project by the original project maintainers at [apirrone/Open_Duck_Mini](https://github.com/apirrone/Open_Duck_Mini). This repository is not a fork of the upstream project and does not duplicate the upstream source files. It is a personal build log, workshop notes, shopping tracker, and place for my own modifications or scripts as the build progresses.

Useful upstream links:

- [Open Duck Mini repository](https://github.com/apirrone/Open_Duck_Mini)
- [Open Duck Mini Runtime](https://github.com/apirrone/Open_Duck_Mini_Runtime)
- [Open Duck Mini v2 project listing](https://robotics.growbotics.ai/projects/hardware/open-duck-mini-v2)

## Current Status

Phase 1 workshop setup is complete enough to move forward. The build is now past printing and into fit checks plus hardware sourcing.

Printed so far: all required STL prints and optional TPU foot bottoms are complete. The PLA feet have been dry-fitted, and the TPU foot bottoms are ready for final fit checks.

Hardware sourcing is well underway. The foot micro switches, battery charger, 18650 cells and holders, SG90 servos, 8 x 22 x 7 mm bearings, 5V UBEC, XT30 connectors, DC barrel adapters, red/black wire, Loctite 243, 2S BMS/protection boards, a DC barrel power adapter, a 4K HDMI cable, and a Raspberry Pi 40-pin GPIO header kit have arrived. The main STS3215 servos, controller, Raspberry Pi, IMU, and main power switch are still being tracked.

The next milestone is final fit checks, heat-set insert prep, and hardware/electronics preparation as parts arrive.

## Project Progress

Updated: 2026-08-23

Progress is tracked as a practical build estimate rather than an exact percentage. Printing progress is counted from the required printed part quantities in [docs/printing-progress.md](docs/printing-progress.md). The optional TPU foot bottoms are complete as an upgrade to the PLA feet.

```text
Overall build progress   [#####-----] 54%
Printing progress        [##########] 100%  49 / 49 required printed parts + TPU feet
```

| Area | Progress | Status |
| --- | ---: | --- |
| Workshop setup | 100% | Core tools, soldering setup, fasteners, inserts, wire, and consumables are ready. |
| 3D printing and fit checks | 100% | All required STL prints and optional TPU foot bottoms are complete. PLA feet have been dry-fitted. |
| Hardware sourcing | 45% | SG90 servos, foot switches, cells, holders, charger, bearings, UBEC, BMS boards, connectors, power accessories, and GPIO headers are received. Main servos, controller, Raspberry Pi, IMU, and switch remain outstanding. |
| Mechanical assembly | 5% | Early dry fitting has started; final assembly waits on servos, switches, and remaining hardware. |
| Electronics and power | 0% | Not started. |
| Calibration and first motion | 0% | Not started. |
| Software and runtime experiments | 0% | Not started. |

Current next step: fit the TPU bottoms and foot switches, test-fit the SG90 servos and bearings, verify the UBEC and DC adapter output/polarity with a multimeter, and keep the 18650 cells disconnected until the BMS wiring and main power switch are confirmed.

Progress notes: update this section whenever printing, sourcing, assembly, electronics, calibration, or software progress changes.

## Repository Layout

```text
.
├── README.md
├── bom/
│   └── phase-1.csv
├── cad/
│   └── modified-parts/
├── docs/
│   ├── build-log.md
│   ├── phase-1-workshop.md
│   ├── printing-progress.md
│   └── roadmap.md
├── photos/
│   ├── hardware/
│   ├── phase-1-tools/
│   └── printing/
└── scripts/
```

## Documentation

- [Phase 1 Workshop Setup](docs/phase-1-workshop.md)
- [Printing Progress Tracker](docs/printing-progress.md)
- [Build Log](docs/build-log.md)
- [Roadmap](docs/roadmap.md)
- [Hardware Sourcing Tracker](docs/hardware-sourcing.md)
- [Phase 1 BOM Checklist](bom/phase-1.csv)

## Principles

- Keep attribution clear and link back to the upstream project.
- Document the build process honestly, including mistakes and fixes.
- Avoid copying upstream files unless I am intentionally modifying or extending them.
- Keep purchases phased so the project stays manageable.
- Prefer small, useful commits that show the engineering journey.
