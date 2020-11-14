import time
from utils.color_static import *


def get_time() -> str:
    return add_color_time(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def get_timestamp() -> float:
    return time.time()
