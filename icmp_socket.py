import socket
from ipaddress import ip_address, IPv6Address


class ICMPSocket:
    def __init__(self, wait_response_time=None):
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_RAW,
            socket.IPPROTO_ICMP
        )
        self.socket.settimeout(wait_response_time)

    def send_to(self, icmp_echo_request, host, port=80):
        if ':' in host and type(ip_address(host)) is IPv6Address:
            host = socket.getnameinfo((host, 0), 0)[0]
            host = socket.gethostbyname(host)

        self.socket.sendto(bytes(icmp_echo_request), (host,  port))
        return self.socket.recvfrom(2 ** 12)

    def close(self):
        self.socket.close()
