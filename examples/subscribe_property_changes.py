import asyncio
import sys

from aes70.controller import tcp_connection
from aes70.controller.remote_device import RemoteDevice
from aes70.types.ocamutestate import OcaMuteState

async def main():
    client = tcp_connection.connect(host="192.168.1.38", port=65000)

    device = RemoteDevice(client)
    device.set_keepalive_interval(1)
    
    try:
        role_map = await device.get_role_map()

        mute_obj = role_map["Channels/Mute"]
        
        if not mute_obj:
            print("Channels/Mute not found in device tree")
            return
        
        print(f"Subscribing to state changes on {mute_obj.ClassName}...")
       # print(mute_obj)

    #    current_state = await mute_obj.get_properties().find_property("State").getter(mute_obj)()
    #    print(f"Current state: {current_state}")
        
        def on_state_changed(value, change_type, prop_id):
            state_name = "Muted" if value == OcaMuteState.Muted else "Unmuted"
            print(f"[EVENT] Mute state changed to: {state_name} (change_type: {change_type})")
        
        def on_error(error):
            print(f"[ERROR] Subscription error: {error}")

        unsubscribe = mute_obj.OnStateChanged.subscribe(on_state_changed, on_error)

        current_state = await mute_obj.GetState()
        print(f"Current state: {current_state}")
        
        print("\nWaiting for state changes (will toggle state every 5 seconds)...")
        print("Press Ctrl+C to exit\n")
        
        for i in range(4):
            await asyncio.sleep(1)
            
            current_state = await mute_obj.GetState()
            new_state = OcaMuteState.Unmuted if current_state == OcaMuteState.Muted else OcaMuteState.Muted

            print(f"[ACTION] Toggling state to: {new_state}")
            await mute_obj.SetState(new_state)

        print("\nCleaning up...")
        unsubscribe()

    except Exception as error:
        print("Error2 ", error)
    finally:
        device.close()
        print("Connection closed")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user")
