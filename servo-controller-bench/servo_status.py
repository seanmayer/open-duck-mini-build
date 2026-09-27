#!/usr/bin/env python3
"""Read-only status check for a Feetech ST/SC servo."""

import argparse
import serial


def checksum(values: list[int]) -> int:
    return (~sum(values)) & 0xFF


def read_register(port: serial.Serial, servo_id: int, address: int, size: int) -> int:
    values = [servo_id, 0x04, 0x02, address, size]
    port.reset_input_buffer()
    port.write(bytes([0xFF, 0xFF, *values, checksum(values)]))
    port.flush()
    response = port.read(6 + size)
    if len(response) < 6 + size or response[0:2] != b"\xff\xff" or response[2] != servo_id:
        raise RuntimeError(f"No valid response reading address {address}")
    data_start = 5
    data = response[data_start:data_start + size]
    return int.from_bytes(data, byteorder="little")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", required=True)
    parser.add_argument("--id", type=int, required=True, dest="servo_id")
    parser.add_argument("--baud", type=int, default=1_000_000)
    args = parser.parse_args()

    with serial.Serial(args.port, args.baud, timeout=0.3) as port:
        torque = read_register(port, args.servo_id, 40, 1)
        position = read_register(port, args.servo_id, 56, 2)
        voltage = read_register(port, args.servo_id, 62, 1) / 10
        error = read_register(port, args.servo_id, 65, 1)

    print(f"ID: {args.servo_id}")
    print(f"Torque: {'enabled' if torque else 'disabled'} ({torque})")
    print(f"Position: {position}")
    print(f"Voltage: {voltage:.1f} V")
    print(f"Error status: {error}")


if __name__ == "__main__":
    main()
