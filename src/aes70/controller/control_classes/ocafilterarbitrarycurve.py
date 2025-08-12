from ...ocp1.ocafloat32 import OcaFloat32
from ...ocp1.ocatransferfunction import OcaTransferFunction
from ...ocp1.ocauint16 import OcaUint16
from ..make_control_class import make_control_class
from .ocaactuator import OcaActuator

# An arbitrary-curve filter, with transfer function specified as amplitude and
# phase versus frequency.
# @extends OcaActuator
# @class OcaFilterArbitraryCurve
OcaFilterArbitraryCurve = make_control_class(
    'OcaFilterArbitraryCurve',
    4,
    '\u0001\u0001\u0001\r',
    2,
    OcaActuator,
    [
        ['GetTransferFunction', 4, 1, [], [OcaTransferFunction]],
        ['SetTransferFunction', 4, 2, [OcaTransferFunction], []],
        ['GetSampleRate', 4, 3, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetSampleRate', 4, 4, [OcaFloat32], []],
        ['GetTFMinLength', 4, 5, [], [OcaUint16]],
        ['GetTFMaxLength', 4, 6, [], [OcaUint16]],
    ],
    [
      ['TransferFunction', [OcaTransferFunction], 4, 1, False, False, None],
      ['SampleRate', [OcaFloat32], 4, 2, False, False, None],
      ['TFMinLength', [OcaUint16], 4, 3, False, False, None],
      ['TFMaxLength', [OcaUint16], 4, 4, False, False, None],
    ],
    []
)

# Returns the complex transfer function.
#
# @method OcaFilterArbitraryCurve#GetTransferFunction
# @returns {Promise<OcaTransferFunction>}
#   A promise which resolves to a single value of type :class:`OcaTransferFunction`.
# Sets the complex transfer function.
#
# @method OcaFilterArbitraryCurve#SetTransferFunction
# @param {IOcaTransferFunction} TransferFunction
#
# @returns {Promise<None>}
# Gets the filter sampling rate.
# The return values of this method are
#
# - Rate of type ``int``
# - minRate of type ``int``
# - maxRate of type ``int``
#
# @method OcaFilterArbitraryCurve#GetSampleRate
# @returns {Promise<Arguments[int,int,int]>}
# Sets the filter sampling rate.
#
# @method OcaFilterArbitraryCurve#SetSampleRate
# @param {int} Rate
#
# @returns {Promise<None>}
# Returns the minimum number of required points in the specified transfer
# function.
#
# @method OcaFilterArbitraryCurve#GetTFMinLength
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Returns the maximum number of allowed points in the specified transfer
# function.
#
# @method OcaFilterArbitraryCurve#GetTFMaxLength
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# This event is emitted when the property ``TransferFunction`` changes in the remote object.
# The property ``TransferFunction`` is described in the AES70 standard as follows.
# Transfer function of the filter.
#
# @member {PropertyEvent<OcaTransferFunction>} OcaFilterArbitraryCurve#OnTransferFunctionChanged
# This event is emitted when the property ``SampleRate`` changes in the remote object.
# The property ``SampleRate`` is described in the AES70 standard as follows.
# Sample rate inside the filter. We can't assume it's the same as the device
# input or output rate.
#
# @member {PropertyEvent<int>} OcaFilterArbitraryCurve#OnSampleRateChanged
# This event is emitted when the property ``TFMinLength`` changes in the remote object.
# The property ``TFMinLength`` is described in the AES70 standard as follows.
# Minimum number of points that transfer function must specify
#
# @member {PropertyEvent<int>} OcaFilterArbitraryCurve#OnTFMinLengthChanged
# This event is emitted when the property ``TFMaxLength`` changes in the remote object.
# The property ``TFMaxLength`` is described in the AES70 standard as follows.
# Maximum number of points that transfer function may specify
#
# @member {PropertyEvent<int>} OcaFilterArbitraryCurve#OnTFMaxLengthChanged
