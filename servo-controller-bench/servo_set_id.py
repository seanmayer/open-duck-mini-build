#!/usr/bin/env python3
"""Change one Feetech ST/SC servo ID, then verify the new ID."""

import argparse
import time

import serial


def checksum(values: list[int]) -> int:
    return (~sum(values)) & 0xFF


def request(port: serial.Serial, packet: bytes, response_id: int) -> bool:
    port.reset_input_buffer()
    port.write(packet)
    port.flush()
    response = port.read(6)
    return len(response) >= 5 and response[0:2] == b"\xff\xff" and response[2] == response_id


def ping(port: serial.Serial, servo_id: int) -> bool:
    values = [servo_id, 0x02, 0x01]
    return request(port, bytes([0xFF, 0xFF, *values, checksum(values)]), servo_id)


def write_byte(port: serial.Serial, servo_id: int, address: int, value: int) -> bool:
    # WRITE instruction is 0x03; values are one-byte control-table entries.
    values = [servo_id, 0x04, 0x03, address, value]
    packet = bytes([0xFF, 0xFF, *values, checksum(values)])
    return request(port, packet, servo_id)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", required=True)
    parser.add_argument("--old-id", type=int, required=True)
    parser.add_argument("--new-id", type=int, required=True)
    parser.add_argument("--baud", type=int, default=1_000_000)
    parser.add_argument("--yes", action="store_true", help="confirm the EEPROM ID change")
    args = parser.parse_args()

    if not 0 <= args.old_id <= 253 or not 0 <= args.new_id <= 253:
        raise SystemExit("IDs must be between 0 and 253.")
    if args.old_id == args.new_id:
        raise SystemExit("Old and new IDs are identical; no change is needed.")
    if not args.yes:
        raise SystemExit("Add --yes to confirm this ID change.")

    with serial.Serial(args.port, args.baud, timeout=0.2) as port:
        if not ping(port, args.old_id):
            raise SystemExit(f"No response from servo ID {args.old_id}; nothing changed.")
        if ping(port, args.new_id):
            raise SystemExit(f"Servo ID {args.new_id} already responds; refusing to create a duplicate.")
        # Address 55 is the SRAM EEPROM-lock register: 0 unlocks, 1 locks.
        # The ID itself is address 5 and is persistent only while unlocked.
        if not write_byte(port, args.old_id, 55, 0):
            raise SystemExit("Could not unlock the servo EEPROM.")
        if not write_byte(port, args.old_id, 5, args.new_id):
            raise SystemExit("The ID write was not acknowledged.")
        if not write_byte(port, args.new_id, 55, 1):
            raise SystemExit("The ID changed, but the EEPROM could not be locked again.")
        time.sleep(0.1)
        if not ping(port, args.new_id):
            raise SystemExit("Write sent, but the new ID did not respond; stop and inspect wiring.")

    print(f"Confirmed servo ID changed from {args.old_id} to {args.new_id}.")


if __name__ == "__main__":
    main()
