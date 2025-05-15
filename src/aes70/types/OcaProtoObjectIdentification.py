"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaClassIdentification import IOcaClassIdentification, OcaClassIdentification


class IOcaProtoObjectIdentification:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Prototype object number of referenced prototype object.
    POno: int
    # Class identification of referenced object.
    ClassIdentification: IOcaClassIdentification


class OcaProtoObjectIdentification(IOcaProtoObjectIdentification):
    """
    # Prototype object identification. Composite of prototype object number and
    # prototype object's class identification. Used in **OcaBlockFactory**.
    @class OcaProtoObjectIdentification
    """
    def __init__(self, POno: int, ClassIdentification: OcaClassIdentification):
        # Prototype object number of referenced prototype object.
        self.POno: int = POno
        # Class identification of referenced object.
        self.ClassIdentification: OcaClassIdentification = ClassIdentification