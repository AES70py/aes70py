"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaNetworkSystemInterfaceDescriptor:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Parameters for the operating system interface the network uses to do I/O.
    SystemInterfaceParameters: bytes
    # The data network address that corresponds to this system interface.
    MyNetworkAddress: bytes


class OcaNetworkSystemInterfaceDescriptor(IOcaNetworkSystemInterfaceDescriptor):
    """
    # Descriptor of a system interface used by a network. Format is data network
    # type dependent.
    @class OcaNetworkSystemInterfaceDescriptor
    """
    def __init__(self, SystemInterfaceParameters: bytes, MyNetworkAddress: bytes):
        # Parameters for the operating system interface the network uses to do
        # I/O.
        self.SystemInterfaceParameters: bytes = SystemInterfaceParameters
        # The data network address that corresponds to this system interface.
        self.MyNetworkAddress: bytes = MyNetworkAddress