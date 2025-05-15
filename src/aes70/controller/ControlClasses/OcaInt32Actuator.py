from ...OCP1.OcaInt32 import OcaInt32
from ..make_control_class import make_control_class
from .OcaBasicActuator import OcaBasicActuator

# Basic int32 actuator.
# @extends OcaBasicActuator
# @class OcaInt32Actuator
OcaInt32Actuator = make_control_class(
    'OcaInt32Actuator',
    5,
    '\u0001\u0001\u0001\u0001\u0004',
    2,
    OcaBasicActuator,
    [
        ['GetSetting', 5, 1, [], [OcaInt32, OcaInt32, OcaInt32]],
        ['SetSetting', 5, 2, [OcaInt32], []],
    ],
    [
      ['Setting', [OcaInt32], 5, 1, False, False, None],
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
# @method OcaInt32Actuator#GetSetting
# @returns {Promise<Arguments[int,int,int]>}
# Sets the** Setting** property. The return value indicates whether the property
# was successfully set.
#
# @method OcaInt32Actuator#SetSetting
# @param {int} Setting
#
# @returns {Promise<None>}
# This event is emitted when the property ``Setting`` changes in the remote object.
# The property ``Setting`` is described in the AES70 standard as follows.
# Int32 setting.
#
# @member {PropertyEvent<int>} OcaInt32Actuator#OnSettingChanged
