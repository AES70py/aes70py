"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaStreamConnectorIdentification import IOcaStreamConnectorIdentification, OcaStreamConnectorIdentification
from .OcaStreamStatus import OcaStreamStatus
from .OcaStreamType import OcaStreamType


class IOcaStream:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Index of most recent error encountered.
    ErrorNumber: int
    # Public identifier of this stream.
    IDAdvertised: bytes
    # Index of this stream. Unique within owner OcaNetwork2 object.
    Index: int
    # Arbitrary user-settable name for this stream.
    Label: str
    # Object number of **OcaStreamConnector** object to which this stream is
    # connected. A value of zero means the stream is not connected to any
    # connector in this device.
    LocalConnectorONo: int
    # Traffic priority of stream. Values are network implementation dependant.
    Priority: int
    # Full identifier of the connector at the far end of this stream.
    RemoteConnectorIdentification: IOcaStreamConnectorIdentification
    # True iff connection is secure.
    Secure: bool
    # Current status of the stream.
    Status: OcaStreamStatus
    # Stream parameters (encoding, sampling, etc). Details TBD
    StreamParameters: bytes
    # Unicast or multicast
    StreamType: OcaStreamType


class OcaStream(IOcaStream):
    """
    # A single-channel or multichannel signal flow between a local stream
    # connector (i.e. **OcaStreamConnector** instance) of an
    # **OcaStreamNetwork** object in this node and another ("remote") stream
    # connector. Normally, the remote stream connector is in another node. Each
    # stream is unidirectional. With respect to the **OcaStreamNetwork** object
    # in question, a stream is either:
    #
    #  - *Outbound: * A signal flow from an output connector port in the
    #    **OcaStreamNetwork** object to an external destination; or
    #
    #  - *Inbound: * A signal flow from an external source to an *input*
    #    connector in the **OcaStreamNetwork** object.
    #
    #
    # An **OcaStream** object may represent either a unicast or a multicast
    # stream. Any given **OcaStreamConnector** object may support multiple
    # outbound flows, but not multiple inbound flows.
    @class OcaStream
    """
    def __init__(self, ErrorNumber: int, IDAdvertised: bytes, Index: int, Label: str, LocalConnectorONo: int, Priority: int, RemoteConnectorIdentification: OcaStreamConnectorIdentification, Secure: bool, Status: OcaStreamStatus, StreamParameters: bytes, StreamType: OcaStreamType):
        # Index of most recent error encountered.
        self.ErrorNumber: int = ErrorNumber
        # Public identifier of this stream.
        self.IDAdvertised: bytes = IDAdvertised
        # Index of this stream. Unique within owner OcaNetwork2 object.
        self.Index: int = Index
        # Arbitrary user-settable name for this stream.
        self.Label: str = Label
        # Object number of **OcaStreamConnector** object to which this stream is
        # connected. A value of zero means the stream is not connected to any
        # connector in this device.
        self.LocalConnectorONo: int = LocalConnectorONo
        # Traffic priority of stream. Values are network implementation
        # dependant.
        self.Priority: int = Priority
        # Full identifier of the connector at the far end of this stream.
        self.RemoteConnectorIdentification: OcaStreamConnectorIdentification = RemoteConnectorIdentification
        # True iff connection is secure.
        self.Secure: bool = Secure
        # Current status of the stream.
        self.Status: OcaStreamStatus = Status
        # Stream parameters (encoding, sampling, etc). Details TBD
        self.StreamParameters: bytes = StreamParameters
        # Unicast or multicast
        self.StreamType: OcaStreamType = StreamType