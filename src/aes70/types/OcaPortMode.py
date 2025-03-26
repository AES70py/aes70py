from typing import Union

# /*
#  * This file has been generated.
#  */
# /**
#  * Enum that describes whether a port is for input or output.
#  * @class OcaPortMode
#  */
class OcaPortMode:
    # /**
    #  * Singleton object corresponding to the entry with value ``1``.
    #  */
    # Static member Input will be initialized after class declaration

    # /**
    #  * Singleton object corresponding to the entry with value ``2``.
    #  */
    # Static member Output will be initialized after class declaration

    def __init__(self, value: int, name: str) -> None:
        self._value = value
        self._name = name

    # /**
    #  * Returns the numeric value of this enum entry.
    #  */
    def value_of(self) -> int:
        return self._value

    # /**
    #  * Returns the string representation of this enum entry.
    #  */
    def str(self) -> str:
        return self._name

    # /**
    #  * Returns the name of an enum entry.
    #  */
    @staticmethod
    def name(value: int) -> str:
        if value == 1:
            return "Input"
        elif value == 2:
            return "Output"
        else:
            raise ValueError(f"Invalid value for OcaPortMode: {value}")

    # /**
    #  * Returns the value of an enum entry name.
    #  */
    @staticmethod
    def get_value(name: str) -> int:
        if name == "Input":
            return 1
        elif name == "Output":
            return 2
        else:
            raise ValueError(f"Invalid name for OcaPortMode: {name}")

    @staticmethod
    def values() -> map:
        return {"Input": 1, "Output": 2}

# Initialize static members
OcaPortMode.Input = OcaPortMode(1, "Input")
OcaPortMode.Output = OcaPortMode(2, "Output")

IOcaPortMode = Union[OcaPortMode, str, int]  # In Python, this Union allows OcaPortMode, 'Input', 'Output', 1, or 2.
