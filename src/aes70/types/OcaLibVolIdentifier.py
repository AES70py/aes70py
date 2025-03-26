# /*
#  * This file has been generated.
#  */

from typing import Protocol

class IOcaLibVolIdentifier(Protocol):
    """
    /**
     * Library that holds the LibVol in question.
     * @type number
     */
    """
    Library: int

    """
    /**
     * ID of LibVol within the given library.
     * @type number
     */
    """
    ID: int


class OcaLibVolIdentifier(IOcaLibVolIdentifier):
    """
    /**
     * Unique identifier of a library volume within the device.
     * @class OcaLibVolIdentifier
     */
    """
    def __init__(self, Library: int, ID: int):
        # /**
        #  * Library that holds the LibVol in question.
        #  * @type number
        #  */
        self.Library: int = Library

        # /**
        #  * ID of LibVol within the given library.
        #  * @type number
        #  */
        self.ID: int = ID
