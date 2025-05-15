from ....aes70.controller.make_control_class import make_control_class
from .OcaActuator import OcaActuator

# Actuator with no control parameters, used as a simple node to represent
# summations in block signal flows.
# @extends OcaActuator
# @class OcaSummingPoint
OcaSummingPoint = make_control_class(
  'OcaSummingPoint',
  4,
  '\u0001\u0001\u0001\u0016',
  1,
  OcaActuator,
  [],
  [],
  []
);

