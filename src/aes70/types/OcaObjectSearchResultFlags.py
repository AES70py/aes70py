from enum import IntFlag


#  * Bitset that describes the contents of an **OcaSearchResult**
#  * @enum {number}
#  * @readonly

class OcaObjectSearchResultFlags(IntFlag):
    # /**
    #  * Entry with value ``1``.
    #  */
    ONo: int = 1

    # /**
    #  * Entry with value ``2``.
    #  */
    ClassIdentification: int = 2

    # /**
    #  * Entry with value ``4``.
    #  */
    ContainerPath: int = 4

    # /**
    #  * Entry with value ``8``.
    #  */
    Role: int = 8

    # /**
    #  * Entry with value ``16``.
    #  */
    Label: int = 16

# export declare type IOcaObjectSearchResultFlags = number;
IOcaObjectSearchResultFlags = int
