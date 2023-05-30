"""
Scan/Discovery
--------------
Example showing how to scan for BLE devices.
Updated on 2019-03-25 by hbldh <henrik.blidh@nedomkull.com>
"""

import argparse
import asyncio

from bleak import BleakClient, BleakScanner

address = "b1:21:81:2b:a0:1c"


async def main(args: argparse.Namespace):
    print("scanning for 5 seconds, please wait...")
    scanner = BleakScanner()

    devices = await scanner.discover(return_adv=True)

    for d, a in devices.values():
        print()
        print(d)
        print("-" * len(str(d)))
        print(a)

        if a and "DitooPro" in a.local_name:
            async with BleakClient(d.address) as client:
                test = await client.read_gatt_char("00001101-0000-1000-8000-00805f9b34fb")
                print(test)
                for s in client.services:
                    print(s.uuid)
                    for c in s.characteristics:
                        print(c)
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--macos-use-bdaddr",
        action="store_true",
        help="when true use Bluetooth address instead of UUID on macOS",
    )

    args = parser.parse_args()

    asyncio.run(main(args))