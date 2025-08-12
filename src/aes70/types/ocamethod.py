"""
This file is part of aes70py.
This file has been generated.
"""
from .ocamethodid import IOcaMethodID, OcaMethodID


class IOcaMethod:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # The object number. For Null Method Identifier, value shall be zero.
    ONo: int
    # The method ID. For Null Method Identifier, value of all subfields shall be
    # zero.
    MethodID: IOcaMethodID


class OcaMethod(IOcaMethod):
    """
    # Representation of an OCA method, i.e. the unique combination of an ONo and
    # a MethodID. To denote the absence of a method, all field values shall be
    # zero. Such a value is called the *Null Method Identifier*.
    @class OcaMethod
    """
    def __init__(self, ONo: int, MethodID: OcaMethodID):
        # The object number. For Null Method Identifier, value shall be zero.
        self.ONo: int = ONo
        # The method ID. For Null Method Identifier, value of all subfields
        # shall be zero.
        self.MethodID: OcaMethodID = MethodID