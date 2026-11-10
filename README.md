# open-duck-mini-build

Building an open-source humanoid robot while exploring robotics, embedded systems, and AI.

This repository is my build journal for the Open Duck Mini v2: sourcing parts, printing and assembling the robot, documenting calibration, and eventually experimenting with the software stack.

## Build Preview

The main body, leg, neck, and head servo assemblies are complete. These photos follow the build from early servo fitting to the assembled structure:

![Assembly progress](photos/assembly/assembly-progress-0918-2026-09-23.jpeg)

![Assembly progress](photos/assembly/assembly-progress-0920-2026-09-23.jpeg)

![Assembly progress](photos/assembly/assembly-progress-0960-2026-09-27.jpeg)

![Full servo assembly progress](photos/assembly/full-servo-assembly-2026-10-03.jpg)

Replacement Pi checkpoint: the Raspberry Pi Zero 2 W with a pre-soldered GPIO header arrived and was verified over SSH.

![Replacement Raspberry Pi Zero 2 W with pre-soldered header, microSD card, and power connected](photos/hardware/raspberry-pi-zero-2w-presoldered-2026-11-07.jpg)

Latest checkpoint (2026-11-09): all 14 servos now respond to read-only checks from the Pi through the Waveshare controller. Every servo reported torque disabled, error status 0, and 7.9–8.0V. The BNO055 IMU is not connected yet.

![Pi-to-Waveshare servo communication bench setup beside the assembled robot](photos/hardware/pi-servo-communication-checkpoint-2026-11-09.jpg)

IMU preparation (2026-11-10): added a [BNO055 reference photo and connector notes](docs/build-log.md#2026-11-10---bno055-imu-reference-photo). The board matches the STEMMA QT/Qwiic version, with pre-fitted cable sockets and loose headers; it remains unconnected and untested.

## Attribution

Open Duck Mini is an open-source robotics project by the original project maintainers at [apirrone/Open_Duck_Mini](https://github.com/apirrone/Open_Duck_Mini). This repository is not a fork of the upstream project and does not duplicate the upstream source files. It is a personal build log, workshop notes, shopping tracker, and place for my own modifications or scripts as the build progresses.

Useful upstream links:

- [Open Duck Mini repository](https://github.com/apirrone/Open_Duck_Mini)
- [Open Duck Mini Runtime](https://github.com/apirrone/Open_Duck_Mini_Runtime)
- [Open Duck Mini v2 project listing](https://robotics.growbotics.ai/projects/hardware/open-duck-mini-v2)

## Current Status

Workshop setup and printing are complete enough to move forward. The main servo structure is assembled, and read-only checks of the complete servo chain have passed from both the laptop and the Raspberry Pi. The build is paused before BNO055 IMU wiring and sensor integration.

Printed so far: all required STL prints and optional TPU foot bottoms are complete. The PLA feet have been dry-fitted, and the TPU foot bottoms are ready for final fit checks.

Hardware sourcing is well underway. The foot micro switches, main STS3215 servos, SG90 servos, BNO055 IMU, Waveshare serial bus servo driver boards, main power switch, battery charger, 18650 cells, 8 x 22 x 7 mm bearings, 5V UBEC, XT30 connectors, DC barrel adapters, red/black wire, Loctite 243, 2S BMS/protection boards, a DC barrel power adapter, a 4K HDMI cable, Raspberry Pi support parts, and a Raspberry Pi Zero 2 W have arrived. A compact replacement 2S battery holder has also arrived, fits the reprinted rear panel, and is now wired into a completed 2S power-pack subassembly. Pack voltages, switch operation, the UBEC's switched 5V output, and the raw battery-voltage branch have been checked with a multimeter. The USB-C charging board is wired, but charging still needs a controlled test before regular use.

The servo-controller bench milestone is now complete: the switched 7.4 V branch was measured before connection, the Waveshare controller was connected to the laptop, all 14 STS3215 servo IDs were programmed and power-cycle verified, and the complete S01–S14 chain has responded to read-only status checks. The servos were centred and their horns aligned before fitting; the physical joint-to-ID mapping is recorded and the cables have slack. S09's collision during an assembled centre command has not established an alignment or configuration fault; its cause still needs to be understood before further powered movement.

The replacement Pi Zero 2 W with a pre-soldered header is now working over SSH using the existing microSD installation: Debian 12 (Bookworm), `aarch64`. The existing upstream `v2` runtime checkout and Python 3.11 virtual environment were checked: `mini-bdx-runtime` version `0.0.1` is installed in editable mode and `pip check` reports no broken requirements. Soldering/desoldering the original header was a difficult beginner lesson and damaged it; buying a pre-soldered replacement avoids further header repair for this build.

The Pi is now connected to the Waveshare controller through the USB OTG adapter and data cable. Linux detected `/dev/ttyACM0`, Python opened the serial port at 1,000,000 baud, and all 14 servos passed ping/status checks with torque disabled, error status 0, and 7.9–8.0V reported. These results verify communication, not movement, loaded supply performance, calibration, or full runtime operation. The BNO055 is still unconnected. See the [communication checkpoint, full readings, and photo](docs/build-log.md#2026-11-09---pi-to-servo-communication-confirmed).

## Project Progress

Updated: 2026-11-10

Progress is tracked as a practical build estimate rather than an exact percentage. Printing progress is counted from the required printed part quantities in [docs/printing-progress.md](docs/printing-progress.md). The optional TPU foot bottoms are complete as an upgrade to the PLA feet.

```text
Overall build progress   [#######---] 63%
Printing progress        [##########] 100%  49 / 49 required printed parts + TPU feet
```

| Area | Progress | Status |
| --- | ---: | --- |
| Workshop setup | 100% | Core tools, soldering setup, fasteners, inserts, wire, and consumables are ready. |
| 3D printing and fit checks | 100% | All required STL prints and optional TPU foot bottoms are complete. PLA feet have been dry-fitted. |
| Hardware sourcing | 85% | Main hardware is received, including the replacement Pi, installed microSD card, and now-tested USB OTG adapter/data cable. The BNO055 is received but not connected. |
| Mechanical assembly | 60% | The main body, leg, neck, and head servo assemblies are fitted and the S01–S14 servo chain is routed. Final cable dressing, clearances, joint limits, and calibration remain. |
| Electronics and power | 55% | Pack wiring and Pi-to-controller communication are checked; all 14 servos reported 7.9–8.0V with torque disabled. IMU/remaining sensor wiring, final power integration, controlled USB-C charging, and supply behaviour under safe mechanical loads remain unverified. |
| Calibration and first motion | 5% | IDs are programmed and read-only status checks are working. Per-joint zero offsets, safe limits, torque tests, and coordinated motion have not yet been completed. |
| Software and runtime experiments | In progress | Pi boot/SSH, existing v2 installation/dependency checks, USB detection, Python serial access, and read-only communication with all 14 servos are verified. IMU integration and full runtime operation remain untested. |

Current next steps:

1. With servo battery power off, prepare BNO055 IMU integration. Review the [actual board and connector options](docs/build-log.md#2026-11-10---bno055-imu-reference-photo), choose a suitable cable or header connection, and confirm its pin labels and mounting orientation against the [v2 wiring diagram](https://github.com/apirrone/Open_Duck_Mini/blob/v2/docs/open_duck_mini_v2_wiring_diagram.png). Shut down the Pi and disconnect all power before GPIO wiring changes.
2. Connect the IMU, enable/check I2C, and verify sensor readings and orientation without starting the motor runtime or powering the servo chain.
3. Review the runtime's S01–S14 joint mapping, reference positions, offsets, limits, and any automatic torque/pose commands. Read-only communication is now verified; a movement demo is not the next test.
4. Complete remaining foot-switch/electronics wiring, final board mounting and cable dressing, power integration, and controlled USB-C charging checks. Leave covers accessible while checks are outstanding.
5. Plan supported movement only after the startup pose, supply under load, and S09's clearance are understood; do not repeat bulk centring or arbitrary individual midpoint commands on the assembled robot.

These are verification steps, not a decision to redo horn alignment or change servo IDs. The Pi itself does not prevent mechanical collisions, and smaller movement increments cannot make an unreachable target safe.

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
