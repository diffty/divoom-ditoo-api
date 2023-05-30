import asyncio

from bleak import BleakClient, BleakScanner

address = "b1:21:81:2b:a0:1c"


async def main():
    async with BleakClient("B1:21:81:2B:A0:1C") as client:
        for s in client.services:
            print(s)


if __name__ == "__main__":
    asyncio.run(main())
