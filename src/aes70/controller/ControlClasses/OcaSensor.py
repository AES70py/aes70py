from aes70.OCP1.OcaSensorReadingState import OcaSensorReadingState
from ..make_control_class import make_control_class
from .OcaWorker import OcaWorker

# /*w*
#  * Abstract base class for all sensor classes.
#  * @extends OcaWorker
#  * @class OcaSensor
#  */
OcaSensor = make_control_class(
  'OcaSensor',
  3,
  '\x01\x01\x02',
  2,
  OcaWorker,
  [['GetReadingState', 3, 1, [], [OcaSensorReadingState]]],
  [['ReadingState', [OcaSensorReadingState], 3, 1, False, False, None]],
  []
)

# /**
#  * Gets the current reading state of the sensor. The return value indicates
#  * whether the state was successfully retrived.
#  *
#  * @method OcaSensor#GetReadingState
#  * @returns {Promise<OcaSensorReadingState>}
#  *   A promise which resolves to a single value of type :class:`OcaSensorReadingState`.
#  */
# /**
#  * This event is emitted when the property ``ReadingState`` changes in the remote object.
#  * The property ``ReadingState`` is described in the AES70 standard as follows.
#  * Enum that describes whether current reading value is valid and if not, why
#  * not. Readonly.
#  *
#  * @member {PropertyEvent<OcaSensorReadingState>} OcaSensor#OnReadingStateChanged
#  */
