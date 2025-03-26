class PDU:
    @property
    def message_type(self):
        return type(self).message_type
