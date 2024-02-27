import struct


class ICMPEchoReply:
    def __init__(self, reply):
        self.bytes_reply = reply
        self.ttl = int(struct.unpack("B", reply[0][8:9])[0])
        self.type = int(struct.unpack("B", reply[0][20:21])[0])
        self.code = int(struct.unpack("B", reply[0][21:22])[0])
