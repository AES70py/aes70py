from typing import Protocol
from ..types.OcaPortId import IOcaPortID, OcaPortID

# export declare interface IOcaPort {
class IOcaPort(Protocol):
    # /**
    #  * Object number of the object that owns the port.
    #  * @type number
    #  */
    Owner: int

    # /**
    #  * ID of the port.
    #  * @type OcaPortID
    #  */
    ID: IOcaPortID

    # /**
    #  * Port ID of the port.
    #  * @type string
    #  */
    Name: str
# }

# export declare class OcaPort implements IOcaPort {
class OcaPort(IOcaPort):
    # /**
    #  * Representation of an OCA (input or output) port that is used in the signal
    #  * path representation of an OCA device.
    #  * @class OcaPort
    #  */
    def __init__(self, Owner: int, ID: OcaPortID, Name: str) -> None:
        self.Owner = Owner
        self.ID = ID
        self.Name = Name

    # /**
    #  * Object number of the object that owns the port.
    #  * @type number
    #  */
    Owner: int

    # /**
    #  * ID of the port.
    #  * @type OcaPortID
    #  */
    ID: OcaPortID

    # /**
    #  * Port ID of the port.
    #  * @type string
    #  */
    Name: str
# }
