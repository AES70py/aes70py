"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaNetworkSystemInterfaceID:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Operating system handle for the interface the network uses to do I/O.
    SystemInterfaceHandle: bytes
    # The data network address that corresponds to this system interface.
    MyNetworkAddress: bytes


class OcaNetworkSystemInterfaceID(IOcaNetworkSystemInterfaceID):
    """
    # ID of a system interface used by a network. Format is data network type
    # dependent.
    @class OcaNetworkSystemInterfaceID
    """
    def __init__(self, SystemInterfaceHandle: bytes, MyNetworkAddress: bytes):
        # Operating system handle for the interface the network uses to do I/O.
        self.SystemInterfaceHandle: bytes = SystemInterfaceHandle
        # The data network address that corresponds to this system interface.
        self.MyNetworkAddress: bytes = MyNetworkAddress