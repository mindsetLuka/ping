import time


class Timer:
    def __init__(self):
        self._start = None
        self._stop = None

    def start(self):
        self._start = time.time()

    def stop(self):
        self._stop = time.time()

    def get_ms(self):
        if self._stop is None or self._start is None:
            raise ValueError('You need to start the timer and then stop it')

        seconds = self._stop - self._start
        return 1000 * seconds

    def get_ms_str(self):
        return f'{round(self.get_ms(), 1)} ms'
