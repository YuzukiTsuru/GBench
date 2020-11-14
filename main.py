import time
import shlex
import os
import subprocess


def get_time() -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def command_runner(shell_cmd: str):
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(
        cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = str(line.strip())
        if line:
            if len(line) > 50:
                line = line[:50] + '...'
                
            print('{}: [{}]'.format(get_time(), line))
    if p.returncode is 0:
        print('Subprogram success')
        return 0
    else:
        print('Subprogram failed')
        return -1


def prepare_code():
    os.system(
        'sudo apt install -y libgmp-dev libmpfr-dev libmpc-dev build-essential')
    os.system(
        'git clone https://mirrors.bfsu.edu.cn/git/gcc.git' +
        '&& cd gcc ' +
        '&& chmod 777 configure ' +
        '&& ./configure --enable-checking=release --enable-languages=c,c++ --disable-multilib')
    return os.popen('grep -c ^processor /proc/cpuinfo 2>/dev/null').read()


if __name__ == '__main__':
    print(
        "GCCBench V1.0\n\nTime: [{}]\n\nStarting Prepare Code".format(get_time()))
    core_count = prepare_code()
    build_start = get_time()
    print("Start Build Time: [{}]".format(build_start))
    command_runner('make -C gcc -j{}'.format(core_count))
    end_time = get_time()
    print("End Build Time: [{}]".format(end_time))
