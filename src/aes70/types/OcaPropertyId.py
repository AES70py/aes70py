#!/usr/bin/env python3
"""
/*
 * This file has been generated.
 */
"""

from typing import Protocol

# Export declare interface IOcaPropertyID
class IOcaPropertyID(Protocol):
    # /**
    #  * Level in tree of class which defines this property (1=root)
    #  * @type number
    #  */
    DefLevel: int

    # /**
    #  * Index of the property (in the class description).
    #  * @type number
    #  */
    PropertyIndex: int

# Export declare class OcaPropertyID implements IOcaPropertyID
class OcaPropertyID(IOcaPropertyID):
    # /**
    #  * Representation of an OCA property ID. A class may define at most 255
    #  * properties of its own. Additional properties may be inherited, so the total
    #  * number may exceed 255.
    #  * @class OcaPropertyID
    #  */
    def __init__(self, DefLevel: int, PropertyIndex: int):
        # /**
        #  * Level in tree of class which defines this property (1=root)
        #  * @type number
        #  */
        self.DefLevel: int = DefLevel
        # /**
        #  * Index of the property (in the class description).
        #  * @type number
        #  */
        self.PropertyIndex: int = PropertyIndex
