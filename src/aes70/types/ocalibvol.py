"""
This file is part of aes70py.
This file has been generated.
"""
from .ocalibvolmetadata import IOcaLibVolMetadata, OcaLibVolMetadata


class IOcaLibVol:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Descriptor of library volume
    Metadata: IOcaLibVolMetadata
    # Contents of library volume. Type depends on template parameter.
    Data: bytes


class OcaLibVol(IOcaLibVol):
    """
    # Library volume. template. Template parameter is datatype of the volume.
    # See **03 OcaLibrary** for explanation.
    @class OcaLibVol
    """
    def __init__(self, Metadata: OcaLibVolMetadata, Data: bytes):
        # Descriptor of library volume
        self.Metadata: OcaLibVolMetadata = Metadata
        # Contents of library volume. Type depends on template parameter.
        self.Data: bytes = Data