# /*
#  * This file has been generated.
#  */

from typing import Protocol
from .OcaClassIdentification import IOcaClassIdentification, OcaClassIdentification

class IOcaObjectIdentification(Protocol):
    """
    Object number of referenced object.
    @type number
    """
    ONo: int

    """
    Class identification of referenced object.
    @type OcaClassIdentification
    """
    ClassIdentification: IOcaClassIdentification

class OcaObjectIdentification(IOcaObjectIdentification):
    """
    Object identification. Composite of object number and object's class. Used
    mainly in discovery processes.
    @class OcaObjectIdentification
    """
    def __init__(self, ONo: int, ClassIdentification: OcaClassIdentification) -> None:
        # Object number of referenced object.
        # @type number
        self.ONo: int = ONo

        # Class identification of referenced object.
        # @type OcaClassIdentification
        self.ClassIdentification: OcaClassIdentification = ClassIdentification
