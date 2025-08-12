from ..make_control_class import make_control_class
from .ocaworker import OcaWorker

# Abstract base class for all actuators (i.e. devices that affect the routing
# and/or content of the audio signal, or provide ancillary functions such as
# power).
# @extends OcaWorker
# @class OcaActuator
OcaActuator = make_control_class(
    'OcaActuator',
    3,
    '\u0001\u0001\u0001',
    2,
    OcaWorker,
    [],
    [],
    []
)

