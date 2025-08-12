from ...OCP1.OcaFloat32 import OcaFloat32
from ...OCP1.OcaParameterMask import OcaParameterMask
from ...OCP1.OcaParametricEQShape import OcaParametricEQShape
from ..make_control_class import make_control_class
from .OcaActuator import OcaActuator

# A parametric equalizer section with various shape options.
# @extends OcaActuator
# @class OcaFilterParametric
OcaFilterParametric = make_control_class(
    'OcaFilterParametric',
    4,
    '\u0001\u0001\u0001\n',
    2,
    OcaActuator,
    [
        ['GetFrequency', 4, 1, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetFrequency', 4, 2, [OcaFloat32], []],
        ['GetShape', 4, 3, [], [OcaParametricEQShape]],
        ['SetShape', 4, 4, [OcaParametricEQShape], []],
        ['GetWidthParameter', 4, 5, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetWidthParameter', 4, 6, [OcaFloat32], []],
        ['GetInbandGain', 4, 7, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetInbandGain', 4, 8, [OcaFloat32], []],
        ['GetShapeParameter', 4, 9, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetShapeParameter', 4, 10, [OcaFloat32], []],
        ['SetMultiple', 4, 11, [OcaParameterMask, OcaFloat32, OcaParametricEQShape, OcaFloat32, OcaFloat32, OcaFloat32], []],
    ],
    [
      ['Frequency', [OcaFloat32], 4, 1, False, False, None],
      ['Shape', [OcaParametricEQShape], 4, 2, False, False, None],
      ['WidthParameter', [OcaFloat32], 4, 3, False, False, ['Q']],
      ['InbandGain', [OcaFloat32], 4, 4, False, False, None],
      ['ShapeParameter', [OcaFloat32], 4, 5, False, False, None],
    ],
    []
)

# Gets the equalizer frequency setpoint. The return value indicates whether the
# data was successfully retrieved.
# The return values of this method are
#
# - Frequency of type ``int``
# - minFrequency of type ``int``
# - maxFrequency of type ``int``
#
# @method OcaFilterParametric#GetFrequency
# @returns {Promise<Arguments[int,int,int]>}
# Sets the equalizer frequency. The return value indicates whether the value was
# successfully set.
#
# @method OcaFilterParametric#SetFrequency
# @param {int} Frequency
#
# @returns {Promise<None>}
# Gets the curve shape of the equalizer. The return value indicates whether the
# data was successfully retrieved.
#
# @method OcaFilterParametric#GetShape
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets the curve shape shape of the equalizer. The return value indicates
# whether the shape was successfully set.
#
# @method OcaFilterParametric#SetShape
# @param {int} type
#
# @returns {Promise<None>}
# Gets the width parameter property of the equalizer. The return value indicates
# whether the data was successfully retrieved.
# The return values of this method are
#
# - Width of type ``int``
# - minWidth of type ``int``
# - maxWidth of type ``int``
#
# @method OcaFilterParametric#GetWidthParameter
# @returns {Promise<Arguments[int,int,int]>}
# Sets the width parameter property of the equalizer. The return value indicates
# whether the Q was successfully set.
#
# @method OcaFilterParametric#SetWidthParameter
# @param {int} Width
#
# @returns {Promise<None>}
# Returns the in-band gain of the equalizer. The return value indicates whether
# the data was successfully retrieved.
# The return values of this method are
#
# - gain of type ``int``
# - minGain of type ``int``
# - maxGain of type ``int``
#
# @method OcaFilterParametric#GetInbandGain
# @returns {Promise<Arguments[int,int,int]>}
# Sets the in-band gain of the equalizer. The return value indicates whether the
# gain was successfully set.
#
# @method OcaFilterParametric#SetInbandGain
# @param {int} gain
#
# @returns {Promise<None>}
# Returns the shape parameter of the equalizer. The return value indicates
# whether the data was successfully retrieved.
# The return values of this method are
#
# - shape of type ``int``
# - minShape of type ``int``
# - maxShape of type ``int``
#
# @method OcaFilterParametric#GetShapeParameter
# @returns {Promise<Arguments[int,int,int]>}
# Sets the shape parameter of the equalizer. The return value indicates whether
# the parameter was successfully set.
#
# @method OcaFilterParametric#SetShapeParameter
# @param {int} shape
#
# @returns {Promise<None>}
# Sets some or all filter parameters. The return value indicates if the
# parameters were successfully set. The action of this method is atomic - if any
# of the value changes fails, none of the changes are made.
#
# @method OcaFilterParametric#SetMultiple
# @param {int} Mask
# @param {int} Frequency
# @param {int} Shape
# @param {int} WidthParameter
# @param {int} InBandGain
# @param {int} ShapeParameter
#
# @returns {Promise<None>}
# This event is emitted when the property ``Frequency`` changes in the remote object.
# The property ``Frequency`` is described in the AES70 standard as follows.
# The frequency setpoint of the parametric filter.
#
# @member {PropertyEvent<int>} OcaFilterParametric#OnFrequencyChanged
# This event is emitted when the property ``Shape`` changes in the remote object.
# The property ``Shape`` is described in the AES70 standard as follows.
# The shape of the parametric filter - peak, shelf, etc.
#
# @member {PropertyEvent<int>} OcaFilterParametric#OnShapeChanged
# This event is emitted when the property ``WidthParameter`` changes in the remote object.
# The property ``WidthParameter`` is described in the AES70 standard as follows.
# Width parameter. For normal parametric implementations, this is the Q of the
# filter.
#
# @member {PropertyEvent<int>} OcaFilterParametric#OnWidthParameterChanged
# An alias for OnWidthParameterChanged
#
# @member {PropertyEvent<int>} OcaFilterParametric#OnQChanged
# This event is emitted when the property ``InbandGain`` changes in the remote object.
# The property ``InbandGain`` is described in the AES70 standard as follows.
# In-band gain of the parametric filter.
#
# @member {PropertyEvent<int>} OcaFilterParametric#OnInbandGainChanged
# This event is emitted when the property ``ShapeParameter`` changes in the remote object.
# The property ``ShapeParameter`` is described in the AES70 standard as follows.
# Width parameter. For certain filter types, this parameter may be used to
# represent extra information about the shape of the transfer function.
#
# @member {PropertyEvent<int>} OcaFilterParametric#OnShapeParameterChanged
