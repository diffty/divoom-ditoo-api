
import asyncio
from bleak import BleakClient, BleakScanner

address = "b1:21:81:2b:a0:1c"
name = "DitooPro-Light"
uuid = "B37D3FFD-3A14-B4D7-39F8-0C3D2989887A"

async def main(address):
    device = await BleakScanner.find_device_by_name("DitooPro-Audio")
    async with BleakClient(device) as client:
        srvs = await client.get_services()

        for s in srvs:
            for c in s.characteristics:
                print(c)


asyncio.run(main(address))
