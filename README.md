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

Phase 1 workshop setup is complete enough to move forward. The build is now in the printing and fit-check stage.

Printed so far: PLA feet, leg spacers, knee-to-ankle sheets, roll motor mounts, roll-to-pitch parts, trunk top/bottom pieces, neck sheets, several head linkage/support parts, and the main head shell. The PLA feet have been dry-fitted without the optional TPU bottoms.

The next milestone is continuing through the upper-body prints, then sourcing the actual robot hardware such as servos, Raspberry Pi, IMU, servo controller, batteries, bearings, and wiring.

## Project Progress

Updated: 2026-08-15

Progress is tracked as a practical build estimate rather than an exact percentage. Printing progress is counted from the required printed part quantities in [docs/printing-progress.md](docs/printing-progress.md). Optional TPU foot bottoms are not counted in the required print total yet.

```text
Overall build progress   [###-------] 31%
Printing progress        [#######---] 67%  33 / 49 required printed parts
```

| Area | Progress | Status |
| --- | ---: | --- |
| Workshop setup | 100% | Core tools, soldering setup, fasteners, inserts, wire, and consumables are ready. |
| 3D printing and fit checks | 67% | Feet, leg spacers, knee-to-ankle sheets, roll motor mounts, roll-to-pitch parts, trunk top/bottom pieces, neck sheets, several head linkage/support parts, and the main head shell are printed; PLA feet have been dry-fitted. |
| Hardware sourcing | 0% | Robot-specific servos, controller, Raspberry Pi, IMU, power parts, and sensors still need sourcing. |
| Mechanical assembly | 5% | Early dry fitting has started; final assembly waits on servos, switches, TPU bottoms, and remaining parts. |
| Electronics and power | 0% | Not started. |
| Calibration and first motion | 0% | Not started. |
| Software and runtime experiments | 0% | Not started. |

Current next step: print `left_antenna_holder.stl` x1, `right_antenna_holder.stl` x1, `left_eye.stl` x1, and `right_eye.stl` x1.

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
│   ├── phase-1-tools/
│   └── printing/
└── scripts/
```

## Documentation

- [Phase 1 Workshop Setup](docs/phase-1-workshop.md)
- [Printing Progress Tracker](docs/printing-progress.md)
- [Build Log](docs/build-log.md)
- [Roadmap](docs/roadmap.md)
- [Phase 1 BOM Checklist](bom/phase-1.csv)

## Principles

- Keep attribution clear and link back to the upstream project.
- Document the build process honestly, including mistakes and fixes.
- Avoid copying upstream files unless I am intentionally modifying or extending them.
- Keep purchases phased so the project stays manageable.
- Prefer small, useful commits that show the engineering journey.
