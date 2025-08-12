from ...ocp1.ocafloat32 import OcaFloat32
from ..make_control_class import make_control_class
from .ocabasicactuator import OcaBasicActuator

# Basic float32 actuator.
# @extends OcaBasicActuator
# @class OcaFloat32Actuator
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
    [
      ['Setting', [OcaFloat32], 5, 1, False, False, None],
    ],
    []
)

# Gets the value and limits of the **Setting** property. The return value
# indicates whether the data was successfully retrieved.
# The return values of this method are
#
# - Setting of type ``int``
# - minSetting of type ``int``
# - maxSetting of type ``int``
#
# @method OcaFloat32Actuator#GetSetting
# @returns {Promise<Arguments[int,int,int]>}
# Sets the **Setting** property. The return value indicates whether the property
# was successfully set.
#
# @method OcaFloat32Actuator#SetSetting
# @param {int} Setting
#
# @returns {Promise<None>}
# This event is emitted when the property ``Setting`` changes in the remote object.
# The property ``Setting`` is described in the AES70 standard as follows.
# Float32 setting.
#
# @member {PropertyEvent<int>} OcaFloat32Actuator#OnSettingChanged
