"""
This file is part of aes70py.
This file has been generated.
"""
from .ocapropertydescriptor import IOcaPropertyDescriptor, OcaPropertyDescriptor


class IOcaProperty:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Object number
    ONo: int
    # Property descriptor.
    Descriptor: IOcaPropertyDescriptor


class OcaProperty(IOcaProperty):
    """
    # Template for complete identification of an OCA property instance,
    # including object number, property ID, Get and Set method IDs, and
    # datatype.
    @class OcaProperty
    """
    def __init__(self, ONo: int, Descriptor: OcaPropertyDescriptor):
        # Object number
        self.ONo: int = ONo
        # Property descriptor.
        self.Descriptor: OcaPropertyDescriptor = Descriptor