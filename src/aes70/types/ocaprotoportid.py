"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaProtoPortID:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Enum that indicates whether the prototype port is an for input or output.
    Mode: int
    # Number of the proto port within input or output group. 1-based.
    Index: int


class OcaProtoPortID(IOcaProtoPortID):
    """
    # Unique identifier of prototype input or output port within a block
    # factory. Prototype port numbers are ordinals starting at 1, and there are
    # separate numbering spaces for input and output ports.
    @class OcaProtoPortID
    """
    def __init__(self, Mode: int, Index: int):
        # Enum that indicates whether the prototype port is an for input or
        # output.
        self.Mode: int = Mode
        # Number of the proto port within input or output group. 1-based.
        self.Index: int = Index