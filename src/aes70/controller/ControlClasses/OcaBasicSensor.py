from ..make_control_class import make_control_class
from .OcaSensor import OcaSensor

# Abstract base class for weakly typed sensors.
# @extends OcaSensor
# @class OcaBasicSensor
OcaBasicSensor = make_control_class(
    'OcaBasicSensor',
    4,
    '\u0001\u0001\u0002\u0001',
    2,
    OcaSensor,
    [],
    [],
    []
)
