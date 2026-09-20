#!/usr/bin/env python3
"""Read-only ping tool for Feetech ST/SC serial-bus servos."""

import argparse
import serial


def checksum(values: list[int]) -> int:
    return (~sum(values)) & 0xFF


def ping(port: serial.Serial, servo_id: int) -> bool:
    # ST/SC protocol: header, ID, packet length, PING instruction, checksum.
    packet = bytes([0xFF, 0xFF, servo_id, 0x02, 0x01,
                    checksum([servo_id, 0x02, 0x01])])
    port.reset_input_buffer()
    port.write(packet)
    port.flush()
    response = port.read(6)
    return len(response) >= 5 and response[0:2] == b"\xff\xff" and response[2] == servo_id


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", required=True)
    parser.add_argument("--baud", type=int, default=1_000_000)
    parser.add_argument("--id", type=int, default=1, dest="servo_id")
    parser.add_argument("--scan", action="store_true", help="ping IDs 0 through 20")
    args = parser.parse_args()

    ids = range(0, 21) if args.scan else [args.servo_id]
    with serial.Serial(args.port, args.baud, timeout=0.15) as port:
        found = [servo_id for servo_id in ids if ping(port, servo_id)]

    if found:
        print("Responding servo ID(s):", ", ".join(map(str, found)))
    else:
        print("No servo response received; no settings were changed.")


if __name__ == "__main__":
    main()
