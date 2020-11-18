# TODO: Score Display

class Score:
    def __init__(self, start_time_stamp: int, end_time_stamp: int, build_type: str):
        self.start_time = start_time_stamp
        self.end_time = end_time_stamp
        self.time_diff_str = None
        self.build_type = build_type
        self.print_socre()

    def print_socre(self):
        print('\n\nIt took {} time to compile and build {}'.format(self.time_diff_str, self.build_type))

    def decode_time(self):
        in_day = self.start_time - self.end_time
        day = in_day / 86400
        in_hour = in_day % 86400
        hour = in_hour / 3600
        in_min_ = in_hour % 3600
        min_ = in_min_ / 60
        in_sec = min_ % 60
        sec = in_sec % 60
        self.time_diff_str = '{} Day, {} Hours, {} Minutes, {} Second'.format(day, hour, min_, sec)
        return day, hour, min_, sec
