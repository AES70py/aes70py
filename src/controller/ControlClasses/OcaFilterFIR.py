from ....aes70.OCP1.OcaFloat32 import OcaFloat32
from ....aes70.OCP1.OcaList import OcaList
from ....aes70.OCP1.OcaUint32 import OcaUint32
from ....aes70.controller.make_control_class import make_control_class
from .OcaActuator import OcaActuator

# A finite impulse response (FIR) filter.
# @extends OcaActuator
# @class OcaFilterFIR
OcaFilterFIR = make_control_class(
  'OcaFilterFIR',
  4,
  '\u0001\u0001\u0001\f',
  2,
  OcaActuator,
  [
    ['GetLength', 4, 1, [], [OcaUint32, OcaUint32, OcaUint32]],
    ['GetCoefficients', 4, 2, [], [OcaList(OcaFloat32)]],
    ['SetCoefficients', 4, 3, [OcaList(OcaFloat32)], []],
    ['GetSampleRate', 4, 4, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
    ['SetSampleRate', 4, 5, [OcaFloat32], []],
  ],
  [
    ['Length', [OcaUint32], 4, 1, false, false, null
    ],
    ['Coefficients', [OcaList(OcaFloat32)], 4, 2, false, false, null
    ],
    ['SampleRate', [OcaFloat32], 4, 3, false, false, null
    ],
  ],
  []
);

# Gets the length of the FIR filter. The return value indicates whether the
# value was successfully retrieved.
# The return values of this method are
#
# - Length of type ``int``
# - minLength of type ``int``
# - maxLength of type ``int``
#
# @method OcaFilterFIR#GetLength
# @returns {Promise<Arguments[int,int,int]>}
# Gets the coefficients of the FIR filter. The return value indicates whether
# the coefficients were successfully retrieved.
#
# @method OcaFilterFIR#GetCoefficients
# @returns {Promise<list[int]>}
#   A promise which resolves to a single value of type ``list[int]``.
# Sets the value of the properties of the FIR filter. The return value indicates
# whether the properties were successfully set.
#
# @method OcaFilterFIR#SetCoefficients
# @param {list[int]} Coefficients
#
# @returns {Promise<None>}
# Gets the sample rate of the FIR filter. The return value indicates whether the
# data was successfully retrieved.
# The return values of this method are
#
# - Rate of type ``int``
# - minRate of type ``int``
# - maxRate of type ``int``
#
# @method OcaFilterFIR#GetSampleRate
# @returns {Promise<Arguments[int,int,int]>}
# Sets the sample rate of the FIR filter. The return value indicates whether the
# rate was successfully set.
#
# @method OcaFilterFIR#SetSampleRate
# @param {int} Rate
#
# @returns {Promise<None>}
# This event is emitted when the property ``Length`` changes in the remote object.
# The property ``Length`` is described in the AES70 standard as follows.
# Length of the filter, in samples. Readonly. Value is set when
# SetCoefficients(...) method executes.
#
# @member {PropertyEvent<int>} OcaFilterFIR#OnLengthChanged
# This event is emitted when the property ``Coefficients`` changes in the remote object.
# The property ``Coefficients`` is described in the AES70 standard as follows.
# Array of FIR Coefficients. The size of the array (number of entries) is equal
# to the Order property plus 1.
#
# @member {PropertyEvent<list[int]>} OcaFilterFIR#OnCoefficientsChanged
# This event is emitted when the property ``SampleRate`` changes in the remote object.
# The property ``SampleRate`` is described in the AES70 standard as follows.
# Sample rate inside the filter. We can't assume it's the same as the device
# input or output rate.
#
# @member {PropertyEvent<int>} OcaFilterFIR#OnSampleRateChanged
