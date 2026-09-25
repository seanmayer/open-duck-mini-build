#!/usr/bin/env python3
"""Move one STS3215 to its neutral midpoint at a cautious speed."""

import argparse

import serial


def checksum(values: list[int]) -> int:
    return (~sum(values)) & 0xFF


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", required=True)
    parser.add_argument("--id", type=int, required=True, dest="servo_id")
    parser.add_argument("--position", type=int, default=2048)
    parser.add_argument("--speed", type=int, default=200)
    parser.add_argument("--acceleration", type=int, default=50)
    parser.add_argument("--baud", type=int, default=1_000_000)
    parser.add_argument("--yes", action="store_true", help="confirm the movement")
    args = parser.parse_args()

    if not args.yes:
        raise SystemExit("Add --yes after confirming the horn is removed and the servo is clear.")
    if not 0 <= args.position <= 4095:
        raise SystemExit("Position must be between 0 and 4095.")
    if not 0 <= args.speed <= 3400 or not 0 <= args.acceleration <= 254:
        raise SystemExit("Speed or acceleration is outside the STS3215 range.")

    # STS3215 WritePosEx: acceleration, position, time=0, speed.
    params = [
        args.servo_id, 0x0A, 0x03, 42,
        args.acceleration,
        args.position & 0xFF, (args.position >> 8) & 0xFF,
        0, 0,
        args.speed & 0xFF, (args.speed >> 8) & 0xFF,
    ]
    packet = bytes([0xFF, 0xFF, *params, checksum(params)])

    with serial.Serial(args.port, args.baud, timeout=0.25) as port:
        port.reset_input_buffer()
        port.write(packet)
        port.flush()
        response = port.read(6)

    if len(response) < 5 or response[0:2] != b"\xff\xff" or response[2] != args.servo_id:
        raise SystemExit("No acknowledgement received from the servo.")
    print(f"Centre command sent to ID {args.servo_id}: position {args.position}, speed {args.speed}.")


if __name__ == "__main__":
    main()
