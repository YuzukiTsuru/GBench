import shlex
import subprocess

from .get_time import get_time
from utils.color_static import *


def command_runner(shell_cmd: str, stage=PROCESS) -> int:
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # Main stdout
    while p.poll() is None:
        line = p.stdout.readline()
        line = str(line.strip(), encoding="utf-8")
        if line:
            print('{} | {} |: [{}]\r'.format(get_time(), stage, line))
    if p.returncode is 0:
        print('Subprogram success')
        return 0
    else:
        print('Subprogram failed')
        return -1
