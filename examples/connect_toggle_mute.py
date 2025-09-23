import asyncio
from aes70.controller import tcp_connection
from aes70.controller.remote_device import RemoteDevice
from aes70.types.ocamutestate import OcaMuteState

class Main:
  device: RemoteDevice

  def connect(self):
      client = tcp_connection.connect(host="206.189.103.173", port=65000) # IP for an emulated device running in the cloud with All Classes see https://aes70x.net/
      self.device = RemoteDevice(client)
      self.device.set_keepalive_interval(10)

  async def toggle_mymute(self):
      self.connect()
      y = await self.device.get_role_map() # AES70py is asynchronous. We use 'await' in this example to make it run synchronously.

      mute_obj = y.get("MyActuators/MyMute") 

      val = OcaMuteState.Muted # Mute has a specific Oca state, it is not a true/false boolean but `Muted` or `Unmuted` see: https://docs.deuso.de/AES70-OCC/
      val = await mute_obj.GetState() # Getter method
      if val == OcaMuteState.Muted:
        val = OcaMuteState.Unmuted
      else:
        val = OcaMuteState.Muted

      await mute_obj.SetState(val) # Setter method

      print(f'MyActuators/MyMute to {val}')
      self.device.close()

if __name__ == '__main__':
    obj = Main()
    asyncio.run(obj.toggle_mymute())
