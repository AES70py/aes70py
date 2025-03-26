from aes70.OCP1.OcaUint16 import OcaUint16
from aes70.OCP1.struct import Struct

from ..types.OcaEventId import OcaEventId as type

OcaEventId = Struct({'def_level': OcaUint16, 'event_index': OcaUint16}, type)
