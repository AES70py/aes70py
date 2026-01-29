from __future__ import annotations
from typing import List, Union
import traceback
import inspect
import asyncio

from .client_connection import ClientConnection
from ..events import Events
from .object_base import ObjectBase
from .control_classes.ocadevicemanager import OcaDeviceManager
from .control_classes.ocasubscriptionmanager import OcaSubscriptionManager
from  .control_classes.ocablock import OcaBlock
from .tree_to_rolemap import tree_to_rolemap
from ..types.ocamanagerdefaultobjectnumbers import OcaManagerDefaultObjectNumbers
from ..types.ocanotificationdeliverymode import OcaNotificationDeliveryMode
import aes70.controller.control_classes as RemoteControlClasses
import logging

logger = logging.getLogger(__name__)

# Type definitions
DeviceTreeNode = Union[ObjectBase, List["DeviceTreeNode"]]
DeviceTree = List[DeviceTreeNode]

"""
Controller class for a remote OCA device.

This is the entry point for any interaction with a remote device.
Can be used to query the available object tree, or interact with the manager
classes.
"""

def eventToKey(event):
    ono = event.EmitterONo
    id_val = event.EventID
    return ",".join([str(ono), str(id_val.DefLevel), str(id_val.EventIndex)])


subscriberMethod = {
    "ONo": 1055,
    "MethodID": {
        "DefLevel": 1,
        "MethodIndex": 1,
    },
}

class EventSubscription:
    """Wrapper for managing callbacks for a single event subscription."""
    def __init__(self, event, cb):
        self.event = event
        self.callbacks = []
        self.cb = cb
        self.subscribing = None
        self.version = 0  # Track which AddSubscription API version (0=not subscribed, 1=v1, 2=v2)
    
    def add_callback(self, cb):
        self.callbacks.append(cb)
    
    def delete_callback(self, cb):
        self.callbacks = [c for c in self.callbacks if c != cb]
    
    def emit(self, ok, notification):
        """Emit notification to all callbacks."""
        for cb in self.callbacks:
            try:
                cb(ok, notification)
            except Exception as e:
                logger.error(f"Event handler threw exception: {e}")
    
    def emit_error(self, error):
        """Emit error to all callbacks."""
        self.emit(False, error)
    
    def has_subscribers(self):
        return len(self.callbacks) > 0

modules = []

"""
Controller class for a remote OCA device.

This is the entry point for any interaction with a remote device.
Can be used to query the available object tree, or interact with the manager
classes.

@param {ClientConnection} connection
     The connection to use.
"""
        #
        # """
        # The device manager object. An instance of :class:`OcaDeviceManager`.
        # """
        # self.DeviceManager = OcaDeviceManager(OcaManagerDefaultObjectNumbers.DeviceManager, self)
        # """
        # The Security manager object. An instance of :class:`OcaSecurityManager`
        # """
        # self.SecurityManager = OcaSecurityManager(OcaManagerDefaultObjectNumbers.SecurityManager, self)
        # """
        # The Firmware manager object. An instance of :class:`OcaFirmwareManager`
        # """
        # self.FirmwareManager = OcaFirmwareManager(OcaManagerDefaultObjectNumbers.FirmwareManager, self)
        # """
        # The Subscription manager object. An instance of :class:`OcaSubscriptionManager`
        # """
        # self.SubscriptionManager = OcaSubscriptionManager(OcaManagerDefaultObjectNumbers.SubscriptionManager, self)
        # """
        # The Power manager object. An instance of :class:`OcaPowerManager`
        # """
        # self.PowerManager = OcaPowerManager(OcaManagerDefaultObjectNumbers.PowerManager, self)
        # """
        # The Network manager object. An instance of :class:`OcaNetworkManager`
        # """
        # self.NetworkManager = OcaNetworkManager(OcaManagerDefaultObjectNumbers.NetworkManager, self)
        # """
        # The MediaClock manager object. An instance of :class:`OcaMediaClockManager`
        # """
        # self.MediaClockManager = OcaMediaClockManager(OcaManagerDefaultObjectNumbers.MediaClockManager, self)
        # """
        # The Library manager object. An instance of :class:`OcaLibraryManager`
        # """
        # self.LibraryManager = OcaLibraryManager(OcaManagerDefaultObjectNumbers.LibraryManager, self)
        # """
        # The AudioProcessing manager object. An instance of :class:`OcaAudioProcessingManager`
        # """
        # self.AudioProcessingManager = OcaAudioProcessingManager(OcaManagerDefaultObjectNumbers.AudioProcessingManager,
        #                                                         self)
        # """
        # The DeviceTime manager object. An instance of :class:`OcaDeviceTimeManager`
        # """
        # self.DeviceTimeManager = OcaDeviceTimeManager(OcaManagerDefaultObjectNumbers.DeviceTimeManager, self)
        # """
        # The Task manager object. An instance of :class:`OcaTaskManager`
        # """
        # self.TaskManager = OcaTaskManager(OcaManagerDefaultObjectNumbers.TaskManager, self)
        # """
        # The Coding manager object. An instance of :class:`OcaCodingManager`
        # """
        # self.CodingManager = OcaCodingManager(OcaManagerDefaultObjectNumbers.CodingManager, self)
        # """
        # The Diagnostic manager object. An instance of :class:`OcaDiagnosticManager`
        # """
        # self.DiagnosticManager = OcaDiagnosticManager(OcaManagerDefaultObjectNumbers.DiagnosticManager, self)
        #

class RemoteDevice(Events):
    # # The device manager object.
    # DeviceManager: OcaDeviceManager
    #
    # # The Security manager object.
    # SecurityManager: OcaSecurityManager
    #
    # # The Firmware manager object.
    # FirmwareManager: OcaFirmwareManager
    #
    # # The Subscription manager object.
    # SubscriptionManager: OcaSubscriptionManager
    #
    # # The Power manager object.
    # PowerManager: OcaPowerManager
    #
    # # The Network manager object.
    # NetworkManager: OcaNetworkManager
    #
    # # The MediaClock manager object.
    # MediaClockManager: OcaMediaClockManager
    #
    # # The Library manager object.
    # LibraryManager: OcaLibraryManager
    #
    # # The AudioProcessing manager object.
    # AudioProcessingManager: OcaAudioProcessingManager
    #
    # # The DeviceTime manager object.
    # DeviceTimeManager: OcaDeviceTimeManager
    #
    # # The Task manager object.
    # TaskManager: OcaTaskManager
    #
    # # The Coding manager object.
    # CodingManager: OcaCodingManager
    #
    # # The Diagnostic manager object.
    # DiagnosticManager: OcaDiagnosticManager

    # The Root block.
    Root: OcaBlock

    def __init__(self, connection: ClientConnection):
        super().__init__()
        self.objects = {}
        self.connection = connection
        self._stackDebug = False

        connection.on('error', lambda c, e: self.emit('error', e))
        connection.on('close', lambda c: self.emit('close'))

        self.modules = []
        #print("control classses ", list(vars(RemoteControlClasses).values()))
        self.add_control_classes(list(vars(RemoteControlClasses).values()))
        for m in modules:
            self.add_control_classes(m)
        self.DeviceManager = OcaDeviceManager(
            OcaManagerDefaultObjectNumbers["DeviceManager"], self)
        self.SubscriptionManager = OcaSubscriptionManager(
            OcaManagerDefaultObjectNumbers["SubscriptionManager"], self)
        self.Root = OcaBlock(100, self)
        self.subscriptions = {}
        self._supportsEV2 = None
        self._checkEV2Promise = None

    """
    Close the associated connection.
    """

    def close(self):
        self.connection.close()

    def send_command(self, cmd, returnType, callback):
        stack = traceback.format_stack() if self._stackDebug else None
        return self.connection.send_command(cmd, returnType, callback, stack)

    async def _doSubscribe(self, event):
        if self._checkEV2Promise:
            await self._checkEV2Promise
        if self._supportsEV2 is None or self._supportsEV2:
            p = self.SubscriptionManager.AddSubscription2(
                event,
                OcaNotificationDeliveryMode.Reliable,
                bytes()
            )

            try:
                if self._supportsEV2 is None:
                    self._checkEV2Promise = p
                await p
                if self._supportsEV2 is None:
                    self._supportsEV2 = True
                return 2
            except Exception as err:
                from .remote_error import RemoteError
                if not isinstance(err, RemoteError):
                    raise err
                self._supportsEV2 = False
            finally:
                if self._supportsEV2 is None:
                    self._checkEV2Promise = None
        
        await self.SubscriptionManager.AddSubscription(
            event,
            subscriberMethod,
            bytes(),
            OcaNotificationDeliveryMode.Reliable,
            bytes()
        )
        return 1

    def add_subscription(self, event, callback):
        if self.connection.is_closed():
            raise Exception('Connection was closed.')

        key = eventToKey(event)
        subscriptions = self.subscriptions

        info = subscriptions.get(key)
        if info:
            info.add_callback(callback)
            return

        def drop_subscribers():
            self.subscriptions.pop(key, None)
            self.connection._remove_subscriber(event)

        def cb(ok, notification):
            S = self.subscriptions.get(key)
            if not S:
                logger.warning('Subscription lost.')
                return
            S.emit(ok, notification)

            if not ok or (hasattr(notification, 'exception') and notification.exception):
                drop_subscribers()
            elif S.version > 0 and not S.has_subscribers():
                drop_subscribers()
                self._doUnsubscribe(S, event)

        self.connection._add_subscriber(event, cb)

        info = EventSubscription(event, cb)
        info.add_callback(callback)
        subscriptions[key] = info

        async def do_subscribe():
            try:
                version = await self._doSubscribe(event)
                info.version = version
            except Exception as err:
                info.emit_error(err)
                drop_subscribers()

        asyncio.create_task(do_subscribe())

    def remove_subscription(self, event, callback):
        key = eventToKey(event)

        info = self.subscriptions.get(key)
        if not info:
            raise Exception('Callback not registered.')

        info.delete_callback(callback)

    def _doUnsubscribe(self, info, event):
        async def do_unsubscribe():
            try:
                if info.version == 2:
                    await self.SubscriptionManager.RemoveSubscription2(
                        event,
                        OcaNotificationDeliveryMode.Reliable,
                        bytes()
                    )
                elif info.version == 1:
                    await self.SubscriptionManager.RemoveSubscription(event, subscriberMethod)
            except Exception as error:
                #logger.error(f'Unsubscribe failed: {error}')
                traceback = error.__traceback__
                while traceback:
                    print("{}: {}".format(traceback.tb_frame.f_code.co_filename, traceback.tb_lineno))
                    traceback = traceback.tb_next
                print("fail")
                raise error
            finally:
                print("end")
        
        if info.version > 0:
            asyncio.run(do_unsubscribe())


    def find_best_class(self, id):
        #print("class ID:", id)
        if hasattr(id, "ClassID"):
            #print("getting classID attribute")
            id = id.ClassID
        #print("class ID:", id)
        while len(id):
            #print("getting class by id")
            result = self.find_class_by_id(id)
            if result:
                return result
            id = id[:-1]
        return None

    """
    Add a set of control classes. When communicating with a device the
    objects created for remote control objects will be picked from the
    ones added. The standard control classes are always added by
    default.

    @param {Object|Array} module - The set of classes to add. Either an
       object contains the control classes with the classid as key, or
       an array of control classes.
    """

    def add_control_classes(self, mod, last = 0):
        if isinstance(mod, list):
            m = {}
            for i in range(len(mod)):

                if inspect.ismodule(mod[i]):
                    if(last == 0):
                        #print("+++++" + str(mod[i]))
                        self.add_control_classes(list(vars(mod[i]).values()), 1)
                elif inspect.isclass(mod[i]):
                    o = mod[i]
                    if hasattr(o, "ClassID"):
                        #print(">>>>" + str(mod[i]))
                        m[o.ClassID] = o
            mod = m
        elif not isinstance(mod, dict):
            raise Exception('Unsupported module.')
        #print("=> registering module ", mod)
        self.modules.append(mod)

    def find_class_by_id(self, id):
        if hasattr(id, "ClassID"):
            id = id.ClassID
        modules = self.modules
        #print("modules:", modules)
        for i in range(len(modules) - 1, -1, -1):
            ret = modules[i].get(id)
            if ret:
                return ret
        return None

    def allocate(self, c, ono):
        if isinstance(ono, object) and not isinstance(ono, int):
            ono = int(ono)
        objects = self.objects
        if ono not in objects:
            #print("creating object ", c, " with ono", ono)
            objects[ono] = c(ono, self)
        return objects.get(ono)

    def resolve_object(self, o):
        # OcaBlockMember
        #print("resolve object ", o)
        if hasattr(o, 'MemberObjectIdentification'):
            return self.resolve_object(getattr(o, "MemberObjectIdentification"))

        # OcaObjectIdentification
        if hasattr(o, 'ONo') and hasattr(o, 'ClassIdentification'):
            #print("ObjectIdentification")
            ono = getattr(o,"ONo")
            id_val = getattr(o, "ClassIdentification")
            return self.allocate(self.find_best_class(id_val), ono)

        raise TypeError('Expected OcaObjectIdentification or OcaBlockMember')

    async def GetDeviceTree(self):
        async def get_members(block):
            a = await block.GetMembers()
            ret = []
            #print("members ", a)
            a = list(map(self.resolve_object, a))
            for i in range(len(a)):
                ret.append(a[i])
                if hasattr(a[i], "ClassID") and a[i].ClassID.startswith(OcaBlock.ClassID):
                    ret.append(await get_members(a[i]))
            return ret

        return await get_members(self.Root)

    """
    Discovers the device object tree. This are all objects starting at the Root
    block.

    @returns {Promise} The object tree. A recursive tree structure consisting of arrays of objects.
                       Each block is followed by an array of it's children.
    """

    async def get_device_tree(self):
        return await self.GetDeviceTree()

    """
    Returns a map of role paths to objects. This is a convenience function
    which internally calls get_device_tree and then tree_to_rolemap.
    If more than one object has the same role name on the same tree level,
    their role names will be appended with numbers starting at 1.

    @param {String} [separator='/'] Optional argument used as a separator
                                   for levels in the tree.
    @returns {Promise<Map<string, Object>>} The map of role paths to control
                                           objects.
    """

    async def get_role_map(self, separator='/'):
        tree = await self.get_device_tree()
        return await tree_to_rolemap(tree, separator)

    async def discover_all_fallback(self):
        tree = await self.GetDeviceTree()
        ret = []

        def it(a):
            for i in range(len(a)):
                if isinstance(a[i], list):
                    it(a[i])
                else:
                    ret.append(a[i])

        it(tree)
        return ret

    """
    Discovers the complete object tree of this device starting
    from the root block. The root block itself will not be part
    of the resulting list.

    @deprecated Use :func:`get_device_tree` instead.
    @returns {Promise} The object list.
    """

    async def discover_all(self):
        try:
            res = await self.Root.GetMembersRecursive()
            return list(map(self.resolve_object, res))
        except Exception:
            return await self.discover_all_fallback()

    """
    Set the keepalive interval.
    @param {number} seconds - Keepalive interval in seconds.
    """

    def set_keepalive_interval(self, seconds):
        self.connection.set_keepalive_interval(seconds)

    """
    Enable or disable stack debug.
    """

    def enable_stack_debug(self, enable):
        self._stackDebug = bool(enable)


