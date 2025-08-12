from ...ocp1.ocastring import OcaString
from ...ocp1.ocauint16 import OcaUint16
from ..make_control_class import make_control_class
from .ocabasicactuator import OcaBasicActuator

# String actuator.
# @extends OcaBasicActuator
# @class OcaStringActuator
OcaStringActuator = make_control_class(
    'OcaStringActuator',
    5,
    '\u0001\u0001\u0001\u0001\f',
    2,
    OcaBasicActuator,
    [
        ['GetSetting', 5, 1, [], [OcaString]],
        ['SetSetting', 5, 2, [OcaString], []],
        ['GetMaxLen', 5, 3, [], [OcaUint16]],
    ],
    [
      ['Setting', [OcaString], 5, 1, False, False, None],
      ['MaxLen', [OcaUint16], 5, 2, True, False, None],
    ],
    []
)

# Gets the value and max length of the Value property. The return value
# indicates whether the data was successfully retrieved.
#
# @method OcaStringActuator#GetSetting
# @returns {Promise<str>}
#   A promise which resolves to a single value of type ``str``.
# Sets the value of the Value property. The return value indicates whether the
# property was successfully set.
#
# @method OcaStringActuator#SetSetting
# @param {str} Value
#
# @returns {Promise<None>}
# Gets the maximum string length that this object can handle.
#
# @method OcaStringActuator#GetMaxLen
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# This event is emitted when the property ``Setting`` changes in the remote object.
# The property ``Setting`` is described in the AES70 standard as follows.
# Value.
#
# @member {PropertyEvent<str>} OcaStringActuator#OnSettingChanged
