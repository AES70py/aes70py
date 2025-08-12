"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaclassidentification import IOcaClassIdentification, OcaClassIdentification


class IOcaObjectSearchResult:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # ONo of object found
    ONo: int
    # Class identification (class ID + class version) of object found
    ClassIdentification: IOcaClassIdentification
    # Chain of ONos leading from root to this object's container
    ContainerPath: list[int]
    # Object role in device
    Role: str
    # Object user-specified label
    Label: str


class OcaObjectSearchResult(IOcaObjectSearchResult):
    """
    # Result of object search via the Find...() methods of **OcaBlock**. Dynamic
    # format, form used depends on type of search and options. The FieldMap
    # parameter of the Find...() methods specifies which optional fields should
    # be returned as nonnull.
    @class OcaObjectSearchResult
    """
    def __init__(self, ONo: int, ClassIdentification: OcaClassIdentification, ContainerPath: list[int], Role: str, Label: str):
        # ONo of object found
        self.ONo: int = ONo
        # Class identification (class ID + class version) of object found
        self.ClassIdentification: OcaClassIdentification = ClassIdentification
        # Chain of ONos leading from root to this object's container
        self.ContainerPath: list[int] = ContainerPath
        # Object role in device
        self.Role: str = Role
        # Object user-specified label
        self.Label: str = Label