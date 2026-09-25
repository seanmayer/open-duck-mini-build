# Servo-controller bench

This folder contains the laptop-based bench tests for the Waveshare serial bus servo controller and Feetech STS3215 servos.

## Setup

Activate the local virtual environment from the project root:

```bash
source servo-controller-bench/.venv/bin/activate
```

`pyserial` is installed in this environment. The `.venv` directory is ignored by Git.

## First test

With the controller powered from the switched 7.4 V branch and connected to the laptop by USB, run:

```bash
python servo_port_check.py /dev/cu.usbmodem5B790149151
```

This only opens the serial port and closes it again. It does not transmit servo commands or change any settings.

To perform a read-only ping of the default servo ID:

```bash
python servo_ping.py --port /dev/cu.usbmodem5B790149151 --id 1
```

To scan IDs 0 through 20 without changing anything:

```bash
python servo_ping.py --port /dev/cu.usbmodem5B790149151 --scan
```

To change an individual servo ID, connect only that servo and use the explicit confirmation flag:

```bash
python servo_set_id.py --port /dev/cu.usbmodem5B790149151 --old-id 1 --new-id 2 --yes
```

The script unlocks the servo EEPROM, writes the ID, locks the EEPROM again, and refuses to write if the old ID does not respond or if the new ID already responds. Always power-cycle and ping the new ID before accepting the change.

To centre a servo before fitting its horn/disc, keep it unloaded and run:

```bash
python servo_center.py --port /dev/cu.usbmodem5B790149151 --id 1 --yes
```

The default midpoint is position 2048 at a cautious speed. This changes position only; it does not change the servo ID.

## Bench notes

- Keep one STS3215 servo connected for the first test.
- Keep the servo horn/disc off until the ID and centre position are confirmed.
- Use the laptop for initial ID programming; set up the Raspberry Pi later.
