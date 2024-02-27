class Printer:
    @staticmethod
    def start(host):
        print(f'PING {host} 48 bytes of data')

    @staticmethod
    def print_success_ping(host, port, seq, ttl, ms):
        print(f'Connected to {host}[:{port}]: seq={seq} ttl={ttl} time={ms}')

    @staticmethod
    def print_unexpected_type(_type):
        print(f'Unexpected type={_type}, should have been 0')

    @staticmethod
    def print_unexpected_code(code):
        print(f'Unexpected type={code}, should have been 0')

    @staticmethod
    def print_timelimit():
        print(f"Reply didn't have time to come")

    @staticmethod
    def print_incorrect_host():
        print(f"Host is incorrect")

    @staticmethod
    def print_statistics(host, times):
        n = len(times)
        n_received = sum([0 if time is None else 1 for time in times])
        n_loss = n - n_received
        new_times = []
        for time in times:
            if time is not None:
                new_times.append(time)
        if len(new_times) == 0:
            print(f'\n--- {host} ping statistics---')
            print(f'{n} packets transmitted, 0 received, '
                  f'100% packet loss')
            return
        loss = int(n_loss / n * 100)
        total_time = round(sum(new_times), 1)
        min_times = round(min(new_times), 1)
        avg_times = round(sum(new_times) / n_received, 1)
        max_times = round(max(new_times), 1)
        print(f'\n--- {host} ping statistics---')
        print(f'{n} packets transmitted, {n_received} received, '
              f'{loss}% packet loss, time {total_time} ms')
        print(f'rtt min/avg/max = {min_times}/{avg_times}/{max_times} ms')
