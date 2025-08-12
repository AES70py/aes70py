from ...ocp1.ocaint64 import OcaInt64
from ..make_control_class import make_control_class
from .ocabasicactuator import OcaBasicActuator

# Basic int64 actuator.
# @extends OcaBasicActuator
# @class OcaInt64Actuator
OcaInt64Actuator = make_control_class(
    'OcaInt64Actuator',
    5,
    '\u0001\u0001\u0001\u0001\u0005',
    2,
    OcaBasicActuator,
    [
        ['GetSetting', 5, 1, [], [OcaInt64, OcaInt64, OcaInt64]],
        ['SetSetting', 5, 2, [OcaInt64], []],
    ],
    [
      ['Setting', [OcaInt64], 5, 1, False, False, None],
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
# @method OcaInt64Actuator#GetSetting
# @returns {Promise<Arguments[int,int,int]>}
# Sets the **Setting** property. The return value indicates whether the property
# was successfully set.
#
# @method OcaInt64Actuator#SetSetting
# @param {int} Value
#
# @returns {Promise<None>}
# This event is emitted when the property ``Setting`` changes in the remote object.
# The property ``Setting`` is described in the AES70 standard as follows.
# Int64 setting.
#
# @member {PropertyEvent<int>} OcaInt64Actuator#OnSettingChanged
