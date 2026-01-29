
class EncodedArguments:
    encoders = {}

    # encoders are the argument types, data is the actual argument values
    def __init__(self, encoders, data):
        self.encoders = encoders
        self.data = data
        self._byte_length = -1

    @property
    def byte_length(self):
        if self._byte_length == -1:
            x = zip(self.encoders, self.data)
#            print("x", x)
            s = 0
            for encoder,data in x:
                s+=encoder.encoded_length(data);
            self._byte_length = s
#            self._byte_length = sum(encoder.encoded_length(data) for encoder, data in x)

        return self._byte_length

    def encode_to(self, data: bytearray, pos=0):
        pos = pos | 0
        #print("data ", self.data)
        #print("encoders ", self.encoders)
        for encoder, arg in zip(self.encoders, self.data):
            pos = encoder.encode_to(data, pos, arg)
        return pos

