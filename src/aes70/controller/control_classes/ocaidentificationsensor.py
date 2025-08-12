from ..make_control_class import make_control_class
from .OcaSensor import OcaSensor

# Sensor for device identification mechanism. The idea of this mechanism is that
# there is some kind of control -- a pushbutton, for instance -- that the user
# depresses to send a device identification event to the controller. Such
# mechanisms aid in the setup of networks.
# @extends OcaSensor
# @class OcaIdentificationSensor
OcaIdentificationSensor = make_control_class(
    'OcaIdentificationSensor',
    4,
    '\u0001\u0001\u0002\u0006',
    2,
    OcaSensor,
    [],
    [],
    [
      ['Identify', 4, 1, [] ],
    ]
)

# Event that is emitted when someone actuates the device identification control.
# @member OcaIdentificationSensor#OnIdentify {Event}
