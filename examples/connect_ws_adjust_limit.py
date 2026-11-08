import asyncio
from aes70.controller import ws_connection
from aes70.controller.remote_device import RemoteDevice

class Main:
  device: RemoteDevice
# ws://aes70x.net:1058
# tcp://206.189.103.173:65000
  def connect(self):
      client = ws_connection.connect(host="aes70x.net", port=1058) # IP for an emulated device running in the cloud with All Classes see https://aes70x.net/
      self.device = RemoteDevice(client)
      self.device.set_keepalive_interval(10)

  async def toggle_limit(self):
      self.connect()
      y = await self.device.get_role_map() # AES70py is asynchronous. We use 'await' in this example to make it run synchronously.

      # This device doesn't expose an OcaMute object, so instead of muting we
      # toggle an OcaGain actuator between its minimum gain (effectively
      # limiting the signal) and 0 dB (normal/unity gain).
      gain_obj = y.get("Slot 1/DSP/Zones/1/LimiterOutputGain")

      gain, min_gain, max_gain = (await gain_obj.GetGain()).values # Getter method
      if gain <= min_gain:
        new_gain = 0.0
      else:
        new_gain = min_gain

      await gain_obj.SetGain(new_gain) # Setter method

      print(f'Slot 1/DSP/Zones/1/LimiterOutputGain to {new_gain} dB')
      self.device.close()

if __name__ == '__main__':
    obj = Main()
    asyncio.run(obj.toggle_limit())
