"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaLibVolData_ParamSet:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Block type to which this paramset applies. A block's type is a the object
    # number of its factory or, for factory-defined blocks, a unique identifier
    # set at time of manufacture
    TargetBlockType: int
    # ParamSet payload
    ParData: bytes


class OcaLibVolData_ParamSet(IOcaLibVolData_ParamSet):
    """
    # Library volume data for a Parset (short for Parameter Set) volume. A
    # Parset is a collection of operating parameter settings that can be applied
    # to a block. Each Parset is associated with a specific block type, but not
    # with a specific instance of that type. A Parset may be applied to any
    # block instance of the associated type. A block's type is a the object
    # number of its factory or, for factory-defined blocks, a unique identifier
    # set at time of manufacture.
    @class OcaLibVolData_ParamSet
    """
    def __init__(self, TargetBlockType: int, ParData: bytes):
        # Block type to which this paramset applies. A block's type is a the
        # object number of its factory or, for factory-defined blocks, a unique
        # identifier set at time of manufacture
        self.TargetBlockType: int = TargetBlockType
        # ParamSet payload
        self.ParData: bytes = ParData