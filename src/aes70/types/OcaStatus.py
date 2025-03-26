
from aes70.types.Enum import Enum


OcaStatus = Enum ({
    'OK': 0,
    'ProtocolVersionError': 1,
    'DeviceError': 2,
    'Locked': 3,
    'BadFormat': 4,
    'BadONo': 5,
    'ParameterError': 6,
    'ParameterOutOfRange': 7,
    'NotImplemented': 8,
    'InvalidRequest': 9,
    'ProcessingFailed': 10,
    'BadMethod': 11,
    'PartiallySucceeded': 12,
    'Timeout': 13,
    'BufferOverflow': 14,
})

# The following are the singleton objects corresponding to each enum value.
# They are defined as static members of OcaStatus.
# @type OcaStatus
# @member OK
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member ProtocolVersionError
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member DeviceError
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member Locked
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member BadFormat
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member BadONo
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member ParameterError
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member ParameterOutOfRange
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member NotImplemented
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member InvalidRequest
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member ProcessingFailed
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member BadMethod
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member PartiallySucceeded
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member Timeout
# @memberof OcaStatus
# @static
#
# @type OcaStatus
# @member BufferOverflow
# @memberof OcaStatus
# @static
