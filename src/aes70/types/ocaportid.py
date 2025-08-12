"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaPortID:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Enum that indicates whether the port is for input or output.
    Mode: int
    # Index of port within given input or output set of specified object.
    Index: int


class OcaPortID(IOcaPortID):
    """
    # Unique identifier of input or output port within a given worker or block
    # class. Port numbers are ordinals starting at 1, and there are separate
    # numbering spaces for input and output ports.
    @class OcaPortID
    """
    def __init__(self, Mode: int, Index: int):
        # Enum that indicates whether the port is for input or output.
        self.Mode: int = Mode
        # Index of port within given input or output set of specified object.
        self.Index: int = Index