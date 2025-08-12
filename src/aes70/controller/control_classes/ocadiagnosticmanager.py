from ...OCP1.OcaString import OcaString
from ...OCP1.OcaUint32 import OcaUint32
from ..make_control_class import make_control_class
from .OcaManager import OcaManager

# Optional manager that provides application diagnostic aids. Unlike other
# manager classes, OcaDiagnosticManager may be subclassed to provide proprietary
# application diagnostic enhancements.
#
#  - May be instantiated once in any device.
#
#  - If instantiated, object number must be 13.
#
#
# @extends OcaManager
# @class OcaDiagnosticManager
OcaDiagnosticManager = make_control_class(
    'OcaDiagnosticManager',
    3,
    '\u0001\u0003\r',
    1,
    OcaManager,
    [
        ['GetLockStatus', 3, 1, [OcaUint32], [OcaString]],
    ],
    [],
    []
)

# Retrieves a text description of the given object's lock status. Return value
# indicates success of the retrieval.
#
# @method OcaDiagnosticManager#GetLockStatus
# @param {int} ONo
#
# @returns {Promise<str>}
#   A promise which resolves to a single value of type ``str``.
