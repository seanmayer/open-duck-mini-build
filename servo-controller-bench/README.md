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

To centre a loose servo before fitting its horn/disc, remove the horn/linkage or make sure the output shaft is completely free, then run:

```bash
python servo_center.py --port /dev/cu.usbmodem5B790149151 --id 1 --yes
```

The default midpoint is position 2048 at a cautious speed. This is the raw electrical midpoint, not a universal mechanical centre for an assembled Open Duck Mini joint. Do not run this command on an installed joint whose linkage may hit a stop; the servo controller does not know the joint geometry. The upstream project’s motor-configuration guide is the reference for setting a loose motor to zero before fitting the horn. This command changes position only; it does not change the servo ID.

For a read-only diagnostic of torque, position, voltage, and error status:

```bash
python servo_status.py --port /dev/cu.usbmodem5B790149151 --id 3
```

For a complete read-only chain check, with the battery charged and torque still disabled:

```bash
for id in $(seq 1 14); do
  echo "===== Servo ID $id ====="
  python servo_status.py \
    --port /dev/cu.usbmodem5B790149151 \
    --id "$id"
done
```

Do not enable torque on the assembled robot until the joint is supported, clear of obstructions, and its safe target range is known. A stalled joint can make the battery voltage sag and may be damaged even when the serial error status is zero.

## Bench notes

Current build status (2026-10-19): the initial bench work is complete. All 14 servos are assembled and daisy chained, with IDs verified, joint locations recorded, horns aligned before fitting, and cable slack confirmed. The next work is Pi GPIO header soldering and runtime setup. The loose-servo centring instructions above are not the next step for this assembled robot. Review runtime mapping and startup movement before powered integration; S09's collision has not established a need to redo alignment or configuration.

- Keep one STS3215 servo connected for the first test.
- Keep the servo horn/disc off until the ID and centre position are confirmed.
- Use the laptop for initial ID programming; set up the Raspberry Pi later.
