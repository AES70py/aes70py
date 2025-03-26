from aes70.OCP1.OcaEventId import OcaEventId
from aes70.OCP1.OcaUint32 import OcaUint32
from aes70.OCP1.struct import Struct

from ..types.OcaEvent import OcaEvent as type

OcaEvent = Struct({'emitter_o_no': OcaUint32, 'event_id': OcaEventId}, type)
