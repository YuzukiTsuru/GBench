import shlex
import sys
import subprocess

from .get_time import get_time


def command_runner(shell_cmd: str, flush=False) -> int:
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    i = 0
    strarrs = ['/', '|', '\\']

    # Main stdout
    while p.poll() is None:
        line = p.stdout.readline()
        line = str(line.strip())[2:len(line) + 1]
        if line:
            if flush:
                sys.stdout.write(strarrs[i % 3] + ' {}: [{}]\r'.format(get_time(), line))
                sys.stdout.write('')
                sys.stdout.flush()
                i += 1
            else:
                print('{}: [{}]'.format(get_time(), line))
    if p.returncode is 0:
        print('Subprogram success')
        return 0
    else:
        print('Subprogram failed')
        return -1
