from ..make_control_class import make_control_class
from .OcaActuator import OcaActuator

# Abstract base class for weakly typed actuators.
# @extends OcaActuator
# @class OcaBasicActuator
OcaBasicActuator = make_control_class(
    'OcaBasicActuator',
    4,
    '\u0001\u0001\u0001\u0001',
    2,
    OcaActuator,
    [],
    [],
    []
)

