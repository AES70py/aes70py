from aes70.types.Enum import Enum

# Enumeration of the types of level detector characteristics. Used in dynamics
# classes and for sensors.
# @class OcaLevelDetectionLaw
OcaLevelDetectionLaw = Enum ({
    'None': 0,
    'RMS':  1,
    'Peak': 2,
})

# Singleton object corresponding to the entry with value ``0``.
# @type OcaLevelDetectionLaw
# @member None
# @memberof OcaLevelDetectionLaw
# @static

# Singleton object corresponding to the entry with value ``1``.
# @type OcaLevelDetectionLaw
# @member RMS
# @memberof OcaLevelDetectionLaw
# @static

# Singleton object corresponding to the entry with value ``2``.
# @type OcaLevelDetectionLaw
# @member Peak
# @memberof OcaLevelDetectionLaw
# @static
