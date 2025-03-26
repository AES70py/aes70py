# Required dependencies and imports
import enum
from typing import Protocol

# Translated import from './OcaPortMode'
# Since external implementation is not provided, we include a complete definition.
class OcaPortMode(enum.Enum):
    INPUT = 1
    OUTPUT = 2

IOcaPortMode = OcaPortMode

# Export declare interface IOcaPortID
class IOcaPortID(Protocol):
    # /**
    #  * Enum that indicates whether the port is for input or output.
    #  * @type OcaPortMode
    #  */
    Mode: IOcaPortMode

    # /**
    #  * Index of port within given input or output set of specified object.
    #  * @type number
    #  */
    Index: int

# Export declare class OcaPortID implements IOcaPortID
class OcaPortID(IOcaPortID):
    # /**
    #  * Unique identifier of input or output port within a given worker or block
    #  * class. Port numbers are ordinals starting at 1, and there are separate
    #  * numbering spaces for input and output ports.
    #  * @class OcaPortID
    #  */
    def __init__(self, Mode: OcaPortMode, Index: int) -> None:
        self.Mode = Mode
        self.Index = Index

    # /**
    #  * Enum that indicates whether the port is for input or output.
    #  * @type OcaPortMode
    #  */
    # (The property is defined in the constructor.)

    # /**
    #  * Index of port within given input or output set of specified object.
    #  * @type number
    #  */
    # (The property is defined in the constructor.)
