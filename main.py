import asyncio

from aes70.controller import tcp_connection
from aes70.controller.remote_device import RemoteDevice
import sys

class Main:
    device: RemoteDevice

    def connect(self):
        client = tcp_connection.connect(host="192.168.1.117", port=65000)
        print("demo: connected")
        self.device = RemoteDevice(client)

        # keep the connection alive
        self.device.set_keepalive_interval(10)

    async def walkTree(self, y):
        for x in y:
            if isinstance(x, list):
                await self.walkTree(x)
            else:
                print("-> ", await x.GetRole())
                print("      ", x)

    async def main(self):
       # connect to the OCA device
       self.connect()

       y = await self.device.DeviceManager.GetModelDescription()

       print("A fine device from ", y.Manufacturer.strip(), "!")

       print("Let's walk to the tree the hard way!")
       await self.walkTree(await self.device.get_device_tree())

       print("Getting role to object map")

       y = await self.device.get_role_map()

       print("Objects in device:\n")
       for x in y:
           print(x, ": ", y[x])

       print("getting Status/CPU Temp")
       z = await y["Status/CPU Temp"].GetReading()
       print("==> reading: ", z)

       print("getting Channels/ChannelName")
       z = y["Channels/ChannelName"]
       print("=> current setting: ", await z.GetSetting())

       print("Changing setting to 'Foo'")
       await z.SetSetting("Foo")
       print("=> new setting: ", await z.GetSetting())

       print("getting Status/Identify")
       z = y["Status/Identify"]
       val = await z.GetSetting()
       print("=> current setting: ", val)

       await z.SetSetting(not val)
       print("=> new setting: ", await z.GetSetting())

       self.device.close()
       print("demo: exiting")

if __name__ == '__main__':
    sys.path.append(r'/Users/hww3/aes70.py')

    obj = Main()
    asyncio.run(obj.main())
