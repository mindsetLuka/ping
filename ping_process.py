import socket
from time import sleep
from timer import Timer
from icmp_echo_reply import ICMPEchoReply
from icmp_socket import ICMPSocket
from icmp_echo_request import ICMPEchoRequest

from printer import Printer


def run(hosts, port, count, interval, wait):
    for host in hosts:
        Printer.start(host)
        seq = 1
        times = []
        while True:
            try:
                time = ping(host, port, wait, seq, interval)
                times.append(time)
                if count == seq:
                    break
                seq += 1
            except KeyboardInterrupt:
                Printer.print_statistics(host, times)
                break
        if count:
            Printer.print_statistics(host, times)


def ping(host, port, wait, seq, interval):
    try:
        reply, timer = ping_process(host, port, wait)
        if interval is not None:
            sleep(interval)
        if reply.type != 0:
            Printer.print_unexpected_type(reply.type)
        elif reply.code != 0:
            Printer.print_unexpected_code(reply.code)
        else:
            Printer.print_success_ping(
                host, port, seq, reply.ttl, timer.get_ms_str())
        return timer.get_ms()
    except socket.timeout:
        Printer.print_timelimit()
    except (socket.gaierror, ValueError):
        Printer.print_incorrect_host()
        raise KeyboardInterrupt

    return None


def ping_process(host, port, wait):
    timer = Timer()
    timer.start()
    sock = ICMPSocket(wait)
    reply = sock.send_to(ICMPEchoRequest(), host, port)
    icmp_reply = ICMPEchoReply(reply)
    timer.stop()
    sock.close()

    return icmp_reply, timer
