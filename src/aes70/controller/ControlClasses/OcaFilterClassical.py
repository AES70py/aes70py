from ...OCP1.OcaClassicalFilterShape import OcaClassicalFilterShape
from ...OCP1.OcaFilterPassband import OcaFilterPassband
from ...OCP1.OcaFloat32 import OcaFloat32
from ...OCP1.OcaParameterMask import OcaParameterMask
from ...OCP1.OcaUint16 import OcaUint16
from ..make_control_class import make_control_class
from .OcaActuator import OcaActuator

# A classical analog-style filter - highpass, lowpass, bandpass, etc., with
# shape characteristics such as Butterworth, Chebyshev, Bessel, and
# Linkwitz-Riley. Frequently used in loudspeaker crossover networks.
# @extends OcaActuator
# @class OcaFilterClassical
OcaFilterClassical = make_control_class(
    'OcaFilterClassical',
    4,
    '\u0001\u0001\u0001\t',
    2,
    OcaActuator,
    [
        ['GetFrequency', 4, 1, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetFrequency', 4, 2, [OcaFloat32], []],
        ['GetPassband', 4, 3, [], [OcaFilterPassband]],
        ['SetPassband', 4, 4, [OcaFilterPassband], []],
        ['GetShape', 4, 5, [], [OcaClassicalFilterShape]],
        ['SetShape', 4, 6, [OcaClassicalFilterShape], []],
        ['GetOrder', 4, 7, [], [OcaUint16, OcaUint16, OcaUint16]],
        ['SetOrder', 4, 8, [OcaUint16], []],
        ['GetParameter', 4, 9, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetParameter', 4, 10, [OcaFloat32], []],
        ['SetMultiple', 4, 11, [OcaParameterMask, OcaFloat32, OcaFilterPassband, OcaClassicalFilterShape, OcaUint16, OcaFloat32], []],
    ],
    [
      ['Frequency', [OcaFloat32], 4, 1, False, False, None],
      ['Passband', [OcaFilterPassband], 4, 2, False, False, None],
      ['Shape', [OcaClassicalFilterShape], 4, 3, False, False, None],
      ['Order', [OcaUint16], 4, 4, False, False, None],
      ['Parameter', [OcaFloat32], 4, 5, False, False, None],
    ],
    []
)

# Gets the value of the Frequency property. The return value indicates if the
# property was successfully retrieved.
# The return values of this method are
#
# - Frequency of type ``int``
# - minFrequency of type ``int``
# - maxFrequency of type ``int``
#
# @method OcaFilterClassical#GetFrequency
# @returns {Promise<Arguments[int,int,int]>}
# Sets the value of the Frequency property. The return value indicates if the
# property was successfully set.
#
# @method OcaFilterClassical#SetFrequency
# @param {int} frequency
#
# @returns {Promise<None>}
# Returns the passband specification of the filter object. The return value
# indicates if the specification was successfully retrieved.
#
# @method OcaFilterClassical#GetPassband
# @returns {Promise<OcaFilterPassband>}
#   A promise which resolves to a single value of type :class:`OcaFilterPassband`.
# Sets the passband specification of the filter object. The return value
# indicates if the specification was successfully set.
#
# @method OcaFilterClassical#SetPassband
# @param {OcaFilterPassband} Passband
#
# @returns {Promise<None>}
# Returns the Shape property of the filter. The return value indicates if the
# property was successfully retrieved.
#
# @method OcaFilterClassical#GetShape
# @returns {Promise<OcaClassicalFilterShape>}
#   A promise which resolves to a single value of type :class:`OcaClassicalFilterShape`.
# Sets the Shape property of the filter. The return value indicates if the
# property was successfully set.
#
# @method OcaFilterClassical#SetShape
# @param {OcaClassicalFilterShape} Shape
#
# @returns {Promise<None>}
# Returns the order of the filter. The return value indicates if the property
# was successfully retrieved.
# The return values of this method are
#
# - Order of type ``int``
# - minOrder of type ``int``
# - maxOrder of type ``int``
#
# @method OcaFilterClassical#GetOrder
# @returns {Promise<Arguments[int,int,int]>}
# Sets the order of the filter. The return value indicates if the property was
# successfully set.
#
# @method OcaFilterClassical#SetOrder
# @param {int} Order
#
# @returns {Promise<None>}
# Returns the filter parameter. The return value indicates if the property was
# successfully retrieved.
# The return values of this method are
#
# - Parameter of type ``int``
# - minParameter of type ``int``
# - maxParameter of type ``int``
#
# @method OcaFilterClassical#GetParameter
# @returns {Promise<Arguments[int,int,int]>}
# Sets the filter parameter. The return value indicates if the parameter was
# successfully set.
#
# @method OcaFilterClassical#SetParameter
# @param {int} Parameter
#
# @returns {Promise<None>}
# Sets some or all filter parameter. The return value indicates if the
# parameters were successfully set. The action of this method is atomic - if any
# of the value changes fails, none of the changes are made.
#
# @method OcaFilterClassical#SetMultiple
# @param {int} Mask
# @param {int} Frequency
# @param {OcaFilterPassband} Passband
# @param {OcaClassicalFilterShape} Shape
# @param {int} Order
# @param {int} Parameter
#
# @returns {Promise<None>}
# This event is emitted when the property ``Frequency`` changes in the remote object.
# The property ``Frequency`` is described in the AES70 standard as follows.
# The frequency of the filter.
#
# @member {PropertyEvent<int>} OcaFilterClassical#OnFrequencyChanged
# This event is emitted when the property ``Passband`` changes in the remote object.
# The property ``Passband`` is described in the AES70 standard as follows.
# Lowpass, highpass, bandpass, bandreject
#
# @member {PropertyEvent<OcaFilterPassband>} OcaFilterClassical#OnPassbandChanged
# This event is emitted when the property ``Shape`` changes in the remote object.
# The property ``Shape`` is described in the AES70 standard as follows.
# Shape family - Butterworth, Bessell, etc.
#
# @member {PropertyEvent<OcaClassicalFilterShape>} OcaFilterClassical#OnShapeChanged
# This event is emitted when the property ``Order`` changes in the remote object.
# The property ``Order`` is described in the AES70 standard as follows.
# Filter order
#
# @member {PropertyEvent<int>} OcaFilterClassical#OnOrderChanged
# This event is emitted when the property ``Parameter`` changes in the remote object.
# The property ``Parameter`` is described in the AES70 standard as follows.
# Ripple or other filter parameter, depending on shape. Not used by some shapes.
#
# @member {PropertyEvent<int>} OcaFilterClassical#OnParameterChanged
