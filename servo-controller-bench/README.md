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

## Bench notes

- Keep one STS3215 servo connected for the first test.
- Keep the servo horn/disc off until the ID and centre position are confirmed.
- Use the laptop for initial ID programming; set up the Raspberry Pi later.
