# /*
#  * This file has been generated.
#  */

from typing import Protocol

class IOcaGlobalTypeIdentifier(Protocol):
    # Unique identifier of organization that has authority over this reusable
    # block type. A zero value indicates a global type defined by the AES70
    # standard itself.
    Authority: bytearray

    # ID of library volume type defined by given Authority. Value is unique
    # within the given Authority.
    ID: int

class OcaGlobalTypeIdentifier(IOcaGlobalTypeIdentifier):
    # Globally unique identifier of something that belongs to an organization.
    def __init__(self, Authority: bytearray, ID: int) -> None:
        self.Authority = Authority
        self.ID = ID
