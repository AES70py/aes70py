"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaport import IOcaPort, OcaPort


class IOcaSignalPath:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Source port (i.e. output port) of the signal path.
    SourcePort: IOcaPort
    # Sink port (i.e. input port) of the signal path.
    SinkPort: IOcaPort


class OcaSignalPath(IOcaSignalPath):
    """
    # Signal path between two object ports in the same device.
    @class OcaSignalPath
    """
    def __init__(self, SourcePort: OcaPort, SinkPort: OcaPort):
        # Source port (i.e. output port) of the signal path.
        self.SourcePort: OcaPort = SourcePort
        # Sink port (i.e. input port) of the signal path.
        self.SinkPort: OcaPort = SinkPort