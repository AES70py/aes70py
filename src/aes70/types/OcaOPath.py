"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaOPath:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Host ID of device that contains the referenced object.
    HostID: bytes
    # Object number of referenced object.
    ONo: int


class OcaOPath(IOcaOPath):
    """
    # Object address. Composite of network address in which object resides, and
    # object number.
    @class OcaOPath
    """
    def __init__(self, HostID: bytes, ONo: int):
        # Host ID of device that contains the referenced object.
        self.HostID: bytes = HostID
        # Object number of referenced object.
        self.ONo: int = ONo