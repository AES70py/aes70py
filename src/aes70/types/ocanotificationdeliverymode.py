"""
This file is part of aes70py.
This file has been generated.
"""
from aes70.types.enum import Enum

# Enum for subscriptions that specifies whether its notification messages are to
# be delivered by reliable means (e.g. TCP) or fast means (e.g. UDP).
# @class OcaNotificationDeliveryMode
OcaNotificationDeliveryMode = Enum({
    'Reliable': 1,
    'Fast': 2,
})
