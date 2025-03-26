# Basic float64 actuator.
# @extends OcaBasicActuator
# @class OcaFloat64Actuator
from ..make_control_class import make_control_class
from aes70.OCP1.OcaFloat64 import OcaFloat64
from .OcaBasicActuator import  OcaBasicActuator

OcaFloat64Actuator = make_control_class(
    'OcaFloat64Actuator',
    5,
    '\u0001\u0001\u0001\u0001\u000b',
    2,
    OcaBasicActuator,
    [
        ['GetSetting', 5, 1, [], [OcaFloat64, OcaFloat64, OcaFloat64]],
        ['SetSetting', 5, 2, [OcaFloat64], []],
    ],
    [['Setting', [OcaFloat64], 5, 1, False, False, None]],
    []
)

# Event documentation:
#
# This event is emitted when the property ``Setting`` changes in the remote object.
# The property ``Setting`` is described in the AES70 standard as follows.
# Float64 setting.
#
# @member {PropertyEvent<number>} OcaFloat64Actuator#OnSettingChanged
