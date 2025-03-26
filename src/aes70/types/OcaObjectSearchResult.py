
from abc import ABC
from typing import List, Protocol


# Begin of dependency: OcaClassIdentification definitions
class IOcaClassIdentification(Protocol):
    pass


class OcaClassIdentification:
    def __init__(self) -> None:
        pass


# End of dependency: OcaClassIdentification definitions

# Begin of IOcaObjectSearchResult interface definition
class IOcaObjectSearchResult(Protocol):
    """
    ONo of object found
    @type number
    """
    ONo: int

    """
    Class identification (class ID + class version) of object found
    @type OcaClassIdentification
    """
    ClassIdentification: OcaClassIdentification

    """
    Chain of ONos leading from root to this object's container
    @type number[]
    """
    ContainerPath: List[int]

    """
    Object role in device
    @type string
    """
    Role: str

    """
    Object user-specified label
    @type string
    """
    Label: str


# End of IOcaObjectSearchResult interface definition

# Begin of OcaObjectSearchResult class definition
class OcaObjectSearchResult(IOcaObjectSearchResult):
    """
    Result of object search via the Find...() methods of **OcaBlock**. Dynamic
    format, form used depends on type of search and options. The FieldMap
    parameter of the Find...() methods specifies which optional fields should
    be returned as nonnull.
    @class OcaObjectSearchResult
    """

    def __init__(
            self,
            ONo: int,
            ClassIdentification: OcaClassIdentification,
            ContainerPath: List[int],
            Role: str,
            Label: str
    ) -> None:
        """
        Constructor for OcaObjectSearchResult

        @param ONo: ONo of object found (type number)
        @param ClassIdentification: Class identification (class ID + class version) of object found (type OcaClassIdentification)
        @param ContainerPath: Chain of ONos leading from root to this object's container (type number[])
        @param Role: Object role in device (type string)
        @param Label: Object user-specified label (type string)
        """
        # ONo of object found
        self.ONo: int = ONo

        # Class identification (class ID + class version) of object found
        self.ClassIdentification: OcaClassIdentification = ClassIdentification

        # Chain of ONos leading from root to this object's container
        self.ContainerPath: List[int] = ContainerPath

        # Object role in device
        self.Role: str = Role

        # Object user-specified label
        self.Label: str = Label
# End of OcaObjectSearchResult class definition
