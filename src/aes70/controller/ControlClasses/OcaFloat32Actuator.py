# Basic float32 actuator.
# @extends OcaBasicActuator
# @class OcaFloat32Actuator
from ..make_control_class import make_control_class
from aes70.OCP1.OcaFloat32 import OcaFloat32
from .OcaBasicActuator import  OcaBasicActuator

OcaFloat32Actuator = make_control_class(
    'OcaFloat32Actuator',
    5,
    '\u0001\u0001\u0001\u0001\n',
    2,
    OcaBasicActuator,
    [
        ['GetSetting', 5, 1, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetSetting', 5, 2, [OcaFloat32], []],
    ],
    [['Setting', [OcaFloat32], 5, 1, False, False, None]],
    []
)

# Event documentation:
#
# This event is emitted when the property ``Setting`` changes in the remote object.
# The property ``Setting`` is described in the AES70 standard as follows.
# Float32 setting.
#
# @member {PropertyEvent<number>} OcaFloat32Actuator#OnSettingChanged
