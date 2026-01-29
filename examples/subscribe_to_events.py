import asyncio
from aes70.controller import tcp_connection
from aes70.controller.remote_device import RemoteDevice

async def main():
    client = tcp_connection.connect(host="206.189.103.173", port=65000)
    device = RemoteDevice(client)
    device.set_keepalive_interval(10)
    
    unsubscribe_funcs = []
    
    try:
        print("Discovering device objects...")
        tree = await device.get_device_tree()
        
        def flatten_tree(tree_items, depth=0):
            objects = []
            for item in tree_items:
                if isinstance(item, list):
                    objects.extend(flatten_tree(item, depth + 1))
                else:
                    objects.append(item)
            return objects
        
        all_objects = flatten_tree(tree)
        print(f"Found {len(all_objects)} objects in device tree\n")
        
        subscribed_count = 0
        
        for obj in all_objects[:10]:
            if hasattr(obj, 'OnPropertyChanged'):
                role = await obj.GetRole() if hasattr(obj, 'GetRole') else "Unknown"
                print(f"Subscribing to PropertyChanged events on: {obj.ClassName} (Role: {role})")
                
                def make_callback(obj_name, obj_role):
                    def on_property_changed(prop_id, data_view, change_type):
                        print(f"[EVENT] {obj_name} ({obj_role}): Property {prop_id.DefLevel}.{prop_id.PropertyIndex} changed (type: {change_type})")
                    return on_property_changed
                
                def on_error(error):
                    print(f"[ERROR] Subscription error: {error}")
                
                unsubscribe = obj.OnPropertyChanged.subscribe(
                    make_callback(obj.ClassName, role),
                    on_error
                )
                unsubscribe_funcs.append(unsubscribe)
                subscribed_count += 1
        
        print(f"\nSubscribed to {subscribed_count} objects")
        print("Listening for property change events for 30 seconds...")
        print("Press Ctrl+C to exit\n")
        
        await asyncio.sleep(30)
        
        print("\nCleaning up subscriptions...")
        for unsubscribe in unsubscribe_funcs:
            unsubscribe()
        
    finally:
        device.close()
        print(">Connection closed")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user")
