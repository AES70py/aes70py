"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaMediaConnection:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # True iff connection is secure.
    Secure: bool
    # Stream parameters (encoding, sampling, etc). Format is media network type
    # dependent.
    StreamParameters: bytes
    # Unicast or multicast
    StreamCastMode: int
    # Number of channels in connected stream
    StreamChannelCount: int


class OcaMediaConnection(IOcaMediaConnection):
    """
    # A single-channel or multichannel connection between a local media
    # connector (i.e. **OcaMedia(Source/Sink)Connector** instance) of an
    # **OcaMediaTransportNetwork** object in this node and another ("remote")
    # media source or sink. Normally, the remote source or sink is in another
    # node. The remote end may or may not be an OCA-compliant device. A
    # connection is unidirectional. Its direction is determined by the connector
    # that owns the connection. Its direction is either:
    #
    #  - *Outbound: * A signal flow from a **source** connector to an external
    #    destination; or
    #
    #  - *Inbound: * A signal flow from an external source to a **sink**
    #    connector.
    #
    #
    # An **OcaMediaConnection** object may represent a connection to either a
    # unicast or a multicast stream. Any given
    # **OcaMedia(Source/Sink)Connector** object will only have one media
    # connection. In non-OCA documents, connections are sometimes referred to as
    # *streams* or *flows.*
    @class OcaMediaConnection
    """
    def __init__(self, Secure: bool, StreamParameters: bytes, StreamCastMode: int, StreamChannelCount: int):
        # True iff connection is secure.
        self.Secure: bool = Secure
        # Stream parameters (encoding, sampling, etc). Format is media network
        # type dependent.
        self.StreamParameters: bytes = StreamParameters
        # Unicast or multicast
        self.StreamCastMode: int = StreamCastMode
        # Number of channels in connected stream
        self.StreamChannelCount: int = StreamChannelCount