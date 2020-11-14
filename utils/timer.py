from .get_time import get_time, get_timestamp


class timer:
    def __init__(self):
        self.start_time = ''
        self.start_timestamp = 0
        self.end_time = ''
        self.end_timestamp = 0

    def timer_start(self):
        self.start_time = get_time()
        self.start_timestamp = get_timestamp()
        print('Timer Started: ', self.start_time)

    def timer_end(self):
        self.end_time = get_time()
        self.end_timestamp = get_timestamp()
        print('Timer Ended: ', self.end_time)
