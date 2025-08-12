"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaclassidentification import IOcaClassIdentification, OcaClassIdentification


class IOcaObjectIdentification:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Object number of referenced object.
    ONo: int
    # Class identification of referenced object.
    ClassIdentification: IOcaClassIdentification


class OcaObjectIdentification(IOcaObjectIdentification):
    """
    # Object identification. Composite of object number and object's class. Used
    # mainly in discovery processes.
    @class OcaObjectIdentification
    """
    def __init__(self, ONo: int, ClassIdentification: OcaClassIdentification):
        # Object number of referenced object.
        self.ONo: int = ONo
        # Class identification of referenced object.
        self.ClassIdentification: OcaClassIdentification = ClassIdentification