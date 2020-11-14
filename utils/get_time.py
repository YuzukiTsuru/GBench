import time


def get_time() -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def get_timestamp() -> int:
    return time.time()
