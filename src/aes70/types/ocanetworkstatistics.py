"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaNetworkStatistics:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # The number of receiver packet errors.
    rxPacketErrors: int
    # The number of transmitter packet errors.
    txPacketErrors: int


class OcaNetworkStatistics(IOcaNetworkStatistics):
    """
    # Historical statistics of the network.
    @class OcaNetworkStatistics
    """
    def __init__(self, rxPacketErrors: int, txPacketErrors: int):
        # The number of receiver packet errors.
        self.rxPacketErrors: int = rxPacketErrors
        # The number of transmitter packet errors.
        self.txPacketErrors: int = txPacketErrors