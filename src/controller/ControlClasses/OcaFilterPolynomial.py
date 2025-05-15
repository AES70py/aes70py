from ....aes70.OCP1.OcaFloat32 import OcaFloat32
from ....aes70.OCP1.OcaList import OcaList
from ....aes70.OCP1.OcaUint8 import OcaUint8
from ....aes70.controller.make_control_class import make_control_class
from .OcaActuator import OcaActuator

# A generic Z-domain rational polynomial filter section: A(0) + A(1)z + A(2)z^2
# + A(3)z^3 + ... B(0) + B(1)z + B(2)z^2 + B(3)z^3 + ...
# @extends OcaActuator
# @class OcaFilterPolynomial
OcaFilterPolynomial = make_control_class(
  'OcaFilterPolynomial',
  4,
  '\u0001\u0001\u0001\u000b',
  2,
  OcaActuator,
  [
    ['GetCoefficients', 4, 1, [], [OcaList(OcaFloat32), OcaList(OcaFloat32)]],
    ['SetCoefficients', 4, 2, [OcaList(OcaFloat32), OcaList(OcaFloat32)], []],
    ['GetSampleRate', 4, 3, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
    ['SetSampleRate', 4, 4, [OcaFloat32], []],
    ['GetMaxOrder', 4, 5, [], [OcaUint8]],
  ],
  [
    ['A', [OcaList(OcaFloat32)], 4, 1, false, false, null
    , {"get":{"name":"GetCoefficients","index":0},"set":{"name":"SetCoefficients","index":0}}],
    ['B', [OcaList(OcaFloat32)], 4, 2, false, false, null
    , {"get":{"name":"GetCoefficients","index":1},"set":{"name":"SetCoefficients","index":1}}],
    ['SampleRate', [OcaFloat32], 4, 3, false, false, null
    ],
    ['MaxOrder', [OcaUint8], 4, 4, true, false, null
    ],
  ],
  []
);

# Returns the polynomial coefficients used.
# The return values of this method are
#
# - A of type ``list[int]``
# - B of type ``list[int]``
#
# @method OcaFilterPolynomial#GetCoefficients
# @returns {Promise<Arguments[list[int],list[int]]>}
# Sets the polynomial coefficients.
#
# @method OcaFilterPolynomial#SetCoefficients
# @param {list[int]} A
# @param {list[int]} B
#
# @returns {Promise<None>}
# Gets the filter sampling rate.
# The return values of this method are
#
# - Rate of type ``int``
# - minRate of type ``int``
# - maxRate of type ``int``
#
# @method OcaFilterPolynomial#GetSampleRate
# @returns {Promise<Arguments[int,int,int]>}
# Sets the filter sampling rate.
#
# @method OcaFilterPolynomial#SetSampleRate
# @param {int} Rate
#
# @returns {Promise<None>}
# Gets the maximum allowable order (= max number of array elements in numerator
# and for denominator arrays)
#
# @method OcaFilterPolynomial#GetMaxOrder
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# This event is emitted when the property ``A`` changes in the remote object.
# The property ``A`` is described in the AES70 standard as follows.
# Numerator - "A"
#
# @member {PropertyEvent<list[int]>} OcaFilterPolynomial#OnAChanged
# This event is emitted when the property ``B`` changes in the remote object.
# The property ``B`` is described in the AES70 standard as follows.
# Denominator - "B"
#
# @member {PropertyEvent<list[int]>} OcaFilterPolynomial#OnBChanged
# This event is emitted when the property ``SampleRate`` changes in the remote object.
# The property ``SampleRate`` is described in the AES70 standard as follows.
# Sample rate inside the filter. We can't assume it's the same as the device
# input or output rate.
#
# @member {PropertyEvent<int>} OcaFilterPolynomial#OnSampleRateChanged
