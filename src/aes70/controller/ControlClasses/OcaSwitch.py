from ...OCP1.OcaBoolean import OcaBoolean
from ...OCP1.OcaList import OcaList
from ...OCP1.OcaString import OcaString
from ...OCP1.OcaUint16 import OcaUint16
from ..make_control_class import make_control_class
from .OcaActuator import OcaActuator

# (n)-position single-pole switch.
# @extends OcaActuator
# @class OcaSwitch
OcaSwitch = make_control_class(
    'OcaSwitch',
    4,
    '\u0001\u0001\u0001\u0004',
    2,
    OcaActuator,
    [
        ['GetPosition', 4, 1, [], [OcaUint16, OcaUint16, OcaUint16]],
        ['SetPosition', 4, 2, [OcaUint16], []],
        ['GetPositionName', 4, 3, [OcaUint16], [OcaString]],
        ['SetPositionName', 4, 4, [OcaUint16, OcaString], []],
        ['GetPositionNames', 4, 5, [], [OcaList(OcaString)]],
        ['SetPositionNames', 4, 6, [OcaList(OcaString)], []],
        ['GetPositionEnabled', 4, 7, [OcaUint16], [OcaBoolean]],
        ['SetPositionEnabled', 4, 8, [OcaUint16, OcaBoolean], []],
        ['GetPositionEnableds', 4, 9, [], [OcaList(OcaBoolean)]],
        ['SetPositionEnableds', 4, 10, [OcaList(OcaBoolean)], []],
    ],
    [
      ['Position', [OcaUint16], 4, 1, False, False, None],
      ['PositionNames', [OcaList(OcaString)], 4, 2, False, False, None],
      ['PositionEnableds', [OcaList(OcaBoolean)], 4, 3, False, False, None],
    ],
    []
)

# Gets the value of the Position property and, optionally, its implementation
# min and max. The return value indicates whether the data was successfully
# retrieved.
# The return values of this method are
#
# - position of type ``int``
# - minPosition of type ``int``
# - maxPosition of type ``int``
#
# @method OcaSwitch#GetPosition
# @returns {Promise<Arguments[int,int,int]>}
# Sets the value of the Position property. The return value indicates whether
# the property was successfully set.
#
# @method OcaSwitch#SetPosition
# @param {int} position
#
# @returns {Promise<None>}
# Gets the name assigned to a given switch position. The return value indicates
# whether the name was successfully retrieved.
#
# @method OcaSwitch#GetPositionName
# @param {int} Index
#
# @returns {Promise<str>}
#   A promise which resolves to a single value of type ``str``.
# Assigns a name to a given switch position. The return value indicates whether
# the name was successfully assigned.
#
# @method OcaSwitch#SetPositionName
# @param {int} Index
# @param {str} Name
#
# @returns {Promise<None>}
# Gets list of names assigned to the switch's positions. The return value
# indicates whether the names were successfully retrieved.
#
# @method OcaSwitch#GetPositionNames
# @returns {Promise<list[str]>}
#   A promise which resolves to a single value of type ``list[str]``.
# Assigns names to the switch's positions. The return value indicates whether
# the names were successfully assigned.
#
# @method OcaSwitch#SetPositionNames
# @param {list[str]} Names
#
# @returns {Promise<None>}
# Gets the Enabled flag assigned to a given switch position. The return value
# indicates whether the flag was successfully retrieved.
#
# @method OcaSwitch#GetPositionEnabled
# @param {int} Index
#
# @returns {Promise<bool>}
#   A promise which resolves to a single value of type ``bool``.
# Sets the Enabled flag assigned to a given switch position. The return value
# indicates whether the flag was successfully set.
#
# @method OcaSwitch#SetPositionEnabled
# @param {int} Index
# @param {bool} enabled
#
# @returns {Promise<None>}
# Gets list of Enabled flags assigned to the switch's positions. The return
# value indicates whether the flags were successfully retrieved.
#
# @method OcaSwitch#GetPositionEnableds
# @returns {Promise<list[bool]>}
#   A promise which resolves to a single value of type ``list[bool]``.
# Sets list of Enabled flags for the switch's positions. The return value
# indicates whether the flags were successfully set.
#
# @method OcaSwitch#SetPositionEnableds
# @param {list[bool]} enableds
#
# @returns {Promise<None>}
# This event is emitted when the property ``Position`` changes in the remote object.
# The property ``Position`` is described in the AES70 standard as follows.
# The current position of the switch. Positions shall be numbered from
# minPosition to (including) maxPosition. If the object does not return the
# optional parameters minPosition and maxPosition in its GetPosition method the
# positions shall be numbered from 1 to n.
#
# @member {PropertyEvent<int>} OcaSwitch#OnPositionChanged
# This event is emitted when the property ``PositionNames`` changes in the remote object.
# The property ``PositionNames`` is described in the AES70 standard as follows.
# Vector of switch position names. Supplied by controller.
#
# @member {PropertyEvent<list[str]>} OcaSwitch#OnPositionNamesChanged
# This event is emitted when the property ``PositionEnableds`` changes in the remote object.
# The property ``PositionEnableds`` is described in the AES70 standard as follows.
# Vector of booleans which enable or disable corresponding switch positions.
# Default values are a construction parameter. The usual default value is True.
#
# @member {PropertyEvent<list[bool]>} OcaSwitch#OnPositionEnabledsChanged
