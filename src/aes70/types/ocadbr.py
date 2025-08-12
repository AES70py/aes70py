"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaDBr:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Absolute level in decibels relative to value of **Ref** property.
    Value: int
    # Reference level in dBz. See the definition of OcaDBz for an explanation of
    # the dBz unit.
    Ref: int


class OcaDBr(IOcaDBr):
    """
    # An absolute level expressed in dB above the given absolute reference
    # level.
    @class OcaDBr
    """
    def __init__(self, Value: int, Ref: int):
        # Absolute level in decibels relative to value of **Ref** property.
        self.Value: int = Value
        # Reference level in dBz. See the definition of OcaDBz for an
        # explanation of the dBz unit.
        self.Ref: int = Ref