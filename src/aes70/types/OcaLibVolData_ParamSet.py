# This file has been generated.
from typing import Protocol

# Export declare interface IOcaLibVolData_ParamSet
class IOcaLibVolData_ParamSet(Protocol):
    # /**
    #  * Block type to which this paramset applies. A block's type is a the object
    #  * number of its factory or, for factory-defined blocks, a unique identifier
    #  * set at time of manufacture
    #  * @type number
    #  */
    TargetBlockType: int

    # /**
    #  * ParamSet payload
    #  * @type Uint8Array
    #  */
    ParData: bytearray


# Export declare class OcaLibVolData_ParamSet implements IOcaLibVolData_ParamSet
class OcaLibVolData_ParamSet(IOcaLibVolData_ParamSet):
    # /**
    #  * Block type to which this paramset applies. A block's type is a the object
    #  * number of its factory or, for factory-defined blocks, a unique identifier
    #  * set at time of manufacture
    #  * @type number
    #  */
    TargetBlockType: int

    # /**
    #  * ParamSet payload
    #  * @type Uint8Array
    #  */
    ParData: bytearray

    # /**
    #  * Library volume data for a Parset (short for Parameter Set) volume. A Parset
    #  * is a collection of operating parameter settings that can be applied to a
    #  * block. Each Parset is associated with a specific block type, but not with a
    #  * specific instance of that type. A Parset may be applied to any block
    #  * instance of the associated type. A block's type is a the object number of
    #  * its factory or, for factory-defined blocks, a unique identifier set at time
    #  * of manufacture.
    #  * @class OcaLibVolData_ParamSet
    #  */
    def __init__(self, TargetBlockType: int, ParData: bytearray) -> None:
        self.TargetBlockType = TargetBlockType
        self.ParData = ParData
