"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaMediaCoding:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # ID of coding scheme to use.
    CodingSchemeID: int
    # Coding parameters. Content is coding-scheme-dependent.
    CodecParameters: str
    # Object number of OcaMediaClock3 object to use for this coding scheme. May
    # be zero if no OcaMediaClock3 object is used.
    ClockONo: int


class OcaMediaCoding(IOcaMediaCoding):
    """
    # Codec ID + Coding parameters
    @class OcaMediaCoding
    """
    def __init__(self, CodingSchemeID: int, CodecParameters: str, ClockONo: int):
        # ID of coding scheme to use.
        self.CodingSchemeID: int = CodingSchemeID
        # Coding parameters. Content is coding-scheme-dependent.
        self.CodecParameters: str = CodecParameters
        # Object number of OcaMediaClock3 object to use for this coding scheme.
        # May be zero if no OcaMediaClock3 object is used.
        self.ClockONo: int = ClockONo