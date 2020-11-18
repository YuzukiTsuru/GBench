class Score:
    def __init__(self, start_time_stamp: int, end_time_stamp: int, build_type: str):
        self.start_time = start_time_stamp
        self.end_time = end_time_stamp
        self.time_diff_str = None
        self.build_type = build_type
        print(self.decode_time())

        self.print_socre()

    def print_socre(self):
        print('\n\nIt took {} to compile and build {}'.format(self.time_diff_str, self.build_type))

    def decode_time(self):
        in_day = self.end_time - self.start_time
        day = in_day / 86400
        in_hour = in_day % 86400
        hour = in_hour / 3600
        in_min_ = in_hour % 3600
        min_ = in_min_ / 60
        in_sec = min_ % 60
        sec = in_sec % 60
        self.time_diff_str = '{:d} Day, {:d} Hours, {:d} Minutes, {:d} Second'.format(int(day), int(hour), int(min_), int(sec))
        return day, hour, min_, sec
