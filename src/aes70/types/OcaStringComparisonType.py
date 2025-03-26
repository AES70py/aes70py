from typing import Union, Literal

# /*
#  * This file has been generated.
#  */
# /**
#  * Type of string comparison.
#  * @class OcaStringComparisonType
#  */
class OcaStringComparisonType:
    # /**
    #  * Singleton object corresponding to the entry with value ``0``.
    #  */
    Exact = None  # Will be initialized after the class definition
    # /**
    #  * Singleton object corresponding to the entry with value ``1``.
    #  */
    Substring = None  # Will be initialized after the class definition
    # /**
    #  * Singleton object corresponding to the entry with value ``2``.
    #  */
    Contains = None  # Will be initialized after the class definition
    # /**
    #  * Singleton object corresponding to the entry with value ``3``.
    #  */
    ExactCaseInsensitive = None  # Will be initialized after the class definition
    # /**
    #  * Singleton object corresponding to the entry with value ``4``.
    #  */
    SubstringCaseInsensitive = None  # Will be initialized after the class definition
    # /**
    #  * Singleton object corresponding to the entry with value ``5``.
    #  */
    ContainsCaseInsensitive = None  # Will be initialized after the class definition

    def __init__(self, value: int, name: str) -> None:
        self._value = value
        self._name = name

    # /**
    #  * Returns the numeric value of this enum entry.
    #  */
    def valueOf(self) -> int:
        return self._value

    # /**
    #  * Returns the string representation of this enum entry.
    #  */
    def toString(self) -> str:
        return self._name

    # /**
    #  * Returns the name of an enum entry.
    #  */
    @staticmethod
    def getName(value: int) -> str:
        for obj in (OcaStringComparisonType.Exact,
                    OcaStringComparisonType.Substring,
                    OcaStringComparisonType.Contains,
                    OcaStringComparisonType.ExactCaseInsensitive,
                    OcaStringComparisonType.SubstringCaseInsensitive,
                    OcaStringComparisonType.ContainsCaseInsensitive):
            if obj.valueOf() == value:
                return obj.toString()
        raise ValueError(f"No enum entry with value {value}")

    # /**
    #  * Returns the value of an enum entry name.
    #  */
    @staticmethod
    def getValue(name: str) -> int:
        for obj in (OcaStringComparisonType.Exact,
                    OcaStringComparisonType.Substring,
                    OcaStringComparisonType.Contains,
                    OcaStringComparisonType.ExactCaseInsensitive,
                    OcaStringComparisonType.SubstringCaseInsensitive,
                    OcaStringComparisonType.ContainsCaseInsensitive):
            if obj.toString() == name:
                return obj.valueOf()
        raise ValueError(f"No enum entry with name {name}")

# Initialize the static singleton objects
OcaStringComparisonType.Exact = OcaStringComparisonType(0, "Exact")
OcaStringComparisonType.Substring = OcaStringComparisonType(1, "Substring")
OcaStringComparisonType.Contains = OcaStringComparisonType(2, "Contains")
OcaStringComparisonType.ExactCaseInsensitive = OcaStringComparisonType(3, "ExactCaseInsensitive")
OcaStringComparisonType.SubstringCaseInsensitive = OcaStringComparisonType(4, "SubstringCaseInsensitive")
OcaStringComparisonType.ContainsCaseInsensitive = OcaStringComparisonType(5, "ContainsCaseInsensitive")

# Define the type alias for IOcaStringComparisonType
IOcaStringComparisonType = Union[
    OcaStringComparisonType,
    Literal['Exact'],
    Literal['Substring'],
    Literal['Contains'],
    Literal['ExactCaseInsensitive'],
    Literal['SubstringCaseInsensitive'],
    Literal['ContainsCaseInsensitive'],
    Literal[0, 1, 2, 3, 4, 5]
]
