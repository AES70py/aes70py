"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaprotoport import IOcaProtoPort, OcaProtoPort


class IOcaProtoSignalPath:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Source proto-port (i.e. output port) of the proto-signal path.
    SourceProtoPort: IOcaProtoPort
    # Sink proto-port (i.e. input port) of the proto-signal path.
    SinkProtoPort: IOcaProtoPort


class OcaProtoSignalPath(IOcaProtoSignalPath):
    """
    # Proto-signal path between two proto-member ports in a factory.
    @class OcaProtoSignalPath
    """
    def __init__(self, SourceProtoPort: OcaProtoPort, SinkProtoPort: OcaProtoPort):
        # Source proto-port (i.e. output port) of the proto-signal path.
        self.SourceProtoPort: OcaProtoPort = SourceProtoPort
        # Sink proto-port (i.e. input port) of the proto-signal path.
        self.SinkProtoPort: OcaProtoPort = SinkProtoPort