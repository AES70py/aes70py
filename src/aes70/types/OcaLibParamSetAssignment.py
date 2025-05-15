"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaLibVolIdentifier import IOcaLibVolIdentifier, OcaLibVolIdentifier


class IOcaLibParamSetAssignment:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Identifier of the library volume that holds the paramset.
    ParamSetIdentifier: IOcaLibVolIdentifier
    # Object number of the block to which the paramset assignment applies.
    TargetBlockONo: int


class OcaLibParamSetAssignment(IOcaLibParamSetAssignment):
    """
    # A ParamSet assigment is the description of a binding of a ParamSet to a
    # block instance.
    @class OcaLibParamSetAssignment
    """
    def __init__(self, ParamSetIdentifier: OcaLibVolIdentifier, TargetBlockONo: int):
        # Identifier of the library volume that holds the paramset.
        self.ParamSetIdentifier: OcaLibVolIdentifier = ParamSetIdentifier
        # Object number of the block to which the paramset assignment applies.
        self.TargetBlockONo: int = TargetBlockONo