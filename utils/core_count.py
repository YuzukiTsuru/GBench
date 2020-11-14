import os


def core_count() -> int:
    return int(os.popen('grep -c ^processor /proc/cpuinfo 2>/dev/null').read())
