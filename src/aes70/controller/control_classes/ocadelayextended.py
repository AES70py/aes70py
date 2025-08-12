from ...OCP1.OcaDelayUnit import OcaDelayUnit
from ...OCP1.OcaDelayValue import OcaDelayValue
from ..make_control_class import make_control_class
from .OcaDelay import OcaDelay

# Signal delay - extended version. Allows setting delay value in various units.
# Note that the inherited property 04p01 DelayTime is also supported by this
# class and reflects actual achieved delay in seconds.
# @extends OcaDelay
# @class OcaDelayExtended
OcaDelayExtended = make_control_class(
    'OcaDelayExtended',
    5,
    '\u0001\u0001\u0001\u0007\u0001',
    2,
    OcaDelay,
    [
        ['GetDelayValue', 5, 1, [], [OcaDelayValue, OcaDelayValue, OcaDelayValue]],
        ['SetDelayValue', 5, 2, [OcaDelayValue], []],
        ['GetDelayValueConverted', 5, 3, [OcaDelayUnit], [OcaDelayValue]],
    ],
    [
      ['DelayValue', [OcaDelayValue], 5, 1, False, False, None],
    ],
    []
)

# Gets the value of the DelayValue property. The return value indicates whether
# the property was successfully retrieved.
# The return values of this method are
#
# - Value of type ``IOcaDelayValue``
# - minValue of type ``IOcaDelayValue``
# - maxValue of type ``IOcaDelayValue``
#
# @method OcaDelayExtended#GetDelayValue
# @returns {Promise<Arguments[OcaDelayValue,OcaDelayValue,OcaDelayValue]>}
# Sets the value of the DelayValue property. The return value indicates whether
# the property was successfully set.
#
# @method OcaDelayExtended#SetDelayValue
# @param {IOcaDelayValue} Value
#
# @returns {Promise<None>}
# Return current delay setting, converted to given units. The return value
# indicates whether the method has succeeded.
#
# @method OcaDelayExtended#GetDelayValueConverted
# @param {int} UoM
#
# @returns {Promise<OcaDelayValue>}
#   A promise which resolves to a single value of type :class:`OcaDelayValue`.
# This event is emitted when the property ``DelayValue`` changes in the remote object.
# The property ``DelayValue`` is described in the AES70 standard as follows.
# Delay value.
#
# @member {PropertyEvent<OcaDelayValue>} OcaDelayExtended#OnDelayValueChanged
