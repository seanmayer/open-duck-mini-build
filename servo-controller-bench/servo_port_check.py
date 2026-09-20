#!/usr/bin/env python3
"""Safely verify that a serial servo controller port can be opened."""

import argparse

import serial


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("port", help="macOS serial device, e.g. /dev/cu.usbmodem...")
    parser.add_argument("--baud", type=int, default=1_000_000)
    args = parser.parse_args()

    with serial.Serial(args.port, args.baud, timeout=1) as connection:
        print(f"Opened: {connection.name} at {args.baud} baud")
    print("Closed safely; no bytes were transmitted.")


if __name__ == "__main__":
    main()
