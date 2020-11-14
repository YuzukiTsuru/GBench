import time
import shlex
import os
import subprocess

from .get_time import get_time


def command_runner(shell_cmd: str) -> int:
    log_time = time.time()
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(
        cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = str(line.strip())[2:len(line)]
        if line:
            print('{}: [{}]'.format(get_time(), line))
            os.system('echo "{}" >> GCCBench_{}.log'.format(line, log_time))
    if p.returncode is 0:
        print('Subprogram success')
        return 0
    else:
        print('Subprogram failed')
        return -1
