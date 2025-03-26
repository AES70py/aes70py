from typing import Protocol

# Export declare interface IOcaClassIdentification
class IOcaClassIdentification(Protocol):
    # /**
    #  * @type string
    #  */
    ClassID: str

    # /**
    #  * Version number of the class.
    #  * @type number
    #  */
    ClassVersion: int

# Export declare class OcaClassIdentification implements IOcaClassIdentification
class OcaClassIdentification(IOcaClassIdentification):
    # /**
    #  * @class OcaClassIdentification
    #  */
    def __init__(self, ClassID: str, ClassVersion: int) -> None:
        self.ClassID = ClassID
        self.ClassVersion = ClassVersion
        #print("-> ClassID: ", len(self.ClassID))

    # /**
    #  * @type string
    #  */
    # The public property 'ClassID' is assigned via the constructor.

    # /**
    #  * Version number of the class.
    #  * @type number
    #  */
    # The public property 'ClassVersion' is assigned via the constructor.
