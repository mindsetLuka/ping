import array
import binascii
import os
import socket
import struct


class ICMPEchoRequest:
    DEFAULT_DATA = b"\xa5\x39\x0b\x00\x00\x00\x00\x00" \
                   b"\x10\x11\x12\x13\x14\x15\x16\x17" \
                   b"\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f" \
                   b"\x20\x21\x22\x23\x24\x25\x26\x27" \
                   b"\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f" \
                   b"\x30\x31\x32\x33\x34\x35\x36\x37"
    ICMP_ECHO_REQUEST = 8

    def __init__(self, data=DEFAULT_DATA, custom_id=None):
        self.data = data
        self.encoded_data = str(binascii.hexlify(data))

        if custom_id is None:
            self.id = os.getpid()
        else:
            self.id = custom_id

    def __bytes__(self):
        header_without_checksum = struct.pack(
            'bbHHh',
            self.ICMP_ECHO_REQUEST,
            0,
            0,
            self.id,
            1
        )
        request_without_checksum = header_without_checksum + self.data
        checksum = self.get_checksum(request_without_checksum)
        header = struct.pack(
            'bbHHh',
            self.ICMP_ECHO_REQUEST,
            0,
            socket.htons(checksum),
            self.id,
            1
        )
        request = header + self.data
        return request

    @staticmethod
    def get_checksum(request):
        if len(request) & 1:
            request += '\\0'
        words = array.array('h', request)
        words.byteswap()
        checksum = 0
        for word in words:
            checksum += (word & 0xffff)
        checksum = (checksum >> 16) + (checksum & 0xffff)
        checksum += (checksum >> 16)
        return (~checksum) & 0xffff
