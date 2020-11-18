import time


class Score:
    def __init__(self, start_time_stamp: int, end_time_stamp: int, build_type: str):
        self.start_time = start_time_stamp
        self.end_time = end_time_stamp
        self.time_diff_str = None
        self.build_type = build_type
        self.print_socre()

    def print_socre(self):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.start_time)))
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.end_time)))
