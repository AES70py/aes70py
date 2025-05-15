"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaBaseDataType import OcaBaseDataType
from .OcaMethodID import IOcaMethodID, OcaMethodID
from .OcaPropertyID import IOcaPropertyID, OcaPropertyID


class IOcaPropertyDescriptor:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    #
    PropertyID: IOcaPropertyID
    # The base datatype of the property. Chosen from an enum datatype that
    # represents the available set of basedatatypes**.**
    BaseDataType: OcaBaseDataType
    # Method ID of GET method
    GetterMethodID: IOcaMethodID
    # Method ID of SET method
    SetterMethodID: IOcaMethodID


class OcaPropertyDescriptor(IOcaPropertyDescriptor):
    """
    # Description of an OCA property, including property ID, Get and Set method
    # IDs, and datatype.
    @class OcaPropertyDescriptor
    """
    def __init__(self, PropertyID: OcaPropertyID, BaseDataType: OcaBaseDataType, GetterMethodID: OcaMethodID, SetterMethodID: OcaMethodID):
        #
        self.PropertyID: OcaPropertyID = PropertyID
        # The base datatype of the property. Chosen from an enum datatype that
        # represents the available set of basedatatypes**.**
        self.BaseDataType: OcaBaseDataType = BaseDataType
        # Method ID of GET method
        self.GetterMethodID: OcaMethodID = GetterMethodID
        # Method ID of SET method
        self.SetterMethodID: OcaMethodID = SetterMethodID