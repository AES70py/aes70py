from .ocapropertyid import OcaPropertyID
from .ocapropertychangetype import OcaPropertyChangeType
from .restwithoffset import RestWithOffset

from .tuple import Tuple

OcaPropertyChangedEventData = Tuple(OcaPropertyID, RestWithOffset(1), OcaPropertyChangeType)
