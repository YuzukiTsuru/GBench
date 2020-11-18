import shlex
import subprocess

from utils.color_static import *
from .prints import *


def command_runner(shell_cmd: str, stage=PROCESS, thread_num=0, cwd_dir=None) -> int:
    prints = Prints(stage)
    cmd = shlex.split(shell_cmd)
    if cwd_dir is not None:
        p = subprocess.Popen(cmd, shell=False, cwd=cwd_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    else:
        p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # Main stdout
    while p.poll() is None:
        line = p.stdout.readline()
        line = str(line.strip(), encoding="utf-8")
        if line:
            if thread_num is 0:
                prints.prints(print_str=line)
            else:
                prints.prints(print_str=line, color_thread=add_colior_thread(thread_num))
    if p.returncode is 0:
        print(SUCCESS)
        return 0
    else:
        print(FAIL)
        return -1
