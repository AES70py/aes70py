from aes70.OCP1.OcaInt16 import OcaInt16
from ..make_control_class import make_control_class
from .OcaBasicSensor import OcaBasicSensor

"""
Basic int16 sensor.
@extended OcaBasicSensor
@class OcaInt16Sensor
"""
OcaInt16Sensor = make_control_class(
    'OcaInt16Sensor',
    5,
    '\u0001\u0001\u0002\u0001\u0003',
    2,
    OcaBasicSensor,
    [['GetReading', 5, 1, [], [OcaInt16, OcaInt16, OcaInt16]]],
    [['Reading', [OcaInt16], 5, 1, False, False, None]],
    []
)

"""
Gets the value and limits of the **Reading** property. The return value
indicates whether the data was successfully retrieved.
The return values of this method are

- Reading of type number
- minReading of type number
- maxReading of type number

@method OcaInt16Sensor#GetReading
@returns Promise<Arguments<number,number,number>>
"""

"""
This event is emitted when the property ``Reading`` changes in the remote object.
The property ``Reading`` is described in the AES70 standard as follows.
Int16 reading.

@member PropertyEvent<number> OcaInt16Sensor#OnReadingChanged
"""
