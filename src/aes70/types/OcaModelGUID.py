"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaModelGUID:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # 8 reserved bits.
    Reserved: bytes
    # IEEE Manufacturer code. Unique worldwide.
    MfrCode: bytes
    # Model code. Unique within the given manufacturer's products. May be set
    # freely by the manufacturer.
    ModelCode: bytes


class OcaModelGUID(IOcaModelGUID):
    """
    # 64 bit device type GUID.
    @class OcaModelGUID
    """
    def __init__(self, Reserved: bytes, MfrCode: bytes, ModelCode: bytes):
        # 8 reserved bits.
        self.Reserved: bytes = Reserved
        # IEEE Manufacturer code. Unique worldwide.
        self.MfrCode: bytes = MfrCode
        # Model code. Unique within the given manufacturer's products. May be
        # set freely by the manufacturer.
        self.ModelCode: bytes = ModelCode