"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaStreamConnectorIdentification:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Public name or binary ID of host in which this connector resides.
    HostID: bytes
    # Network address of host in which this connector resides.
    NetworkAddress: bytes
    # Public name or binary ID of node within the host to which this connector
    # belongs.
    NodeID: bytes
    # Public name or binary ID of this stream connector.
    StreamConnectorID: bytes


class OcaStreamConnectorIdentification(IOcaStreamConnectorIdentification):
    """
    # A signal source or sink connector at the far end of a stream - normally,
    # in another device. Not all of the fields of this datatype need be used.
    # The fields used will depend on remote device type, media transport network
    # type, and media transport implementation. Normal usage scenarios are:
    #
    #  - **Unicast input or output**: The **OcaStream** object is instantiated
    #    in an **OcaStreamConnector** object in the local device, and it links
    #    to an **OcaStreamConnector** object in a remote device.
    #
    #  - **Multicast input**: The **OcaStream** object is instantiated in an
    #    **OcaStreamConnector** object in the local device, and, it may or may
    #    not link to an **OcaStreamConnector** object in a remote device.
    #
    #  - **Multicast output**: The **OcaStream** object is instantiated in an
    #    **OcaStreamConnector** object in the local device, but in this case
    #    does not link to any specific remote connector object.
    #
    #
    @class OcaStreamConnectorIdentification
    """
    def __init__(self, HostID: bytes, NetworkAddress: bytes, NodeID: bytes, StreamConnectorID: bytes):
        # Public name or binary ID of host in which this connector resides.
        self.HostID: bytes = HostID
        # Network address of host in which this connector resides.
        self.NetworkAddress: bytes = NetworkAddress
        # Public name or binary ID of node within the host to which this
        # connector belongs.
        self.NodeID: bytes = NodeID
        # Public name or binary ID of this stream connector.
        self.StreamConnectorID: bytes = StreamConnectorID