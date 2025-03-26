from aes70.types.Enum import Enum

# Enumeration of level meter laws.
# @class OcaLevelMeterLaw
OcaLevelMeterLaw = Enum ({
    # Singleton object corresponding to the entry with value ``1``.
    # @type OcaLevelMeterLaw
    # @member VU
    # @memberof OcaLevelMeterLaw
    # @static
    'VU': 1,

    # Singleton object corresponding to the entry with value ``2``.
    # @type OcaLevelMeterLaw
    # @member StandardVU
    # @memberof OcaLevelMeterLaw
    # @static
    'StandardVU': 2,

    # Singleton object corresponding to the entry with value ``3``.
    # @type OcaLevelMeterLaw
    # @member PPM1
    # @memberof OcaLevelMeterLaw
    # @static
    'PPM1': 3,

    # Singleton object corresponding to the entry with value ``4``.
    # @type OcaLevelMeterLaw
    # @member PPM2
    # @memberof OcaLevelMeterLaw
    # @static
    'PPM2': 4,

    # Singleton object corresponding to the entry with value ``5``.
    # @type OcaLevelMeterLaw
    # @member LKFS
    # @memberof OcaLevelMeterLaw
    # @static
    'LKFS': 5,

    # Singleton object corresponding to the entry with value ``6``.
    # @type OcaLevelMeterLaw
    # @member RMS
    # @memberof OcaLevelMeterLaw
    # @static
    'RMS': 6,

    # Singleton object corresponding to the entry with value ``7``.
    # @type OcaLevelMeterLaw
    # @member Peak
    # @memberof OcaLevelMeterLaw
    # @static
    'Peak': 7,

    # Singleton object corresponding to the entry with value ``128``.
    # @type OcaLevelMeterLaw
    # @member ProprietaryValueBase
    # @memberof OcaLevelMeterLaw
    # @static
    'ProprietaryValueBase': 128
})