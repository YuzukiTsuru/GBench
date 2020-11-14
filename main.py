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
        line = str(line.strip())[2:]
        if line:
            print('{}: [{}]'.format(get_time(), line))
    if p.returncode is 0:
        print('Subprogram success')
        return 0
    else:
        print('Subprogram failed')
        return -1

    
def prepare_code_gcc():
    os.system('sudo apt install -y build-essential libgmp-dev libmpfr-dev libmpc-dev')
    os.system('wget https://mirrors.aliyun.com/gnu/gcc/gcc-9.3.0/gcc-9.3.0.tar.gz')
    

def prepare_code_nginx():
    os.system(
        'sudo apt install -y libtool build-essential libpcre3 libpcre3-dev zlib1g-dev openssl wget')
    os.system(
        'wget http://nginx.org/download/nginx-1.19.4.tar.gz' +
        '&& tar xvzf nginx-1.19.4.tar.gz'
        '&& cd nginx-1.19.4 ' +
        '&& chmod 777 configure ' +
        '&& ./configure')
    return os.popen('grep -c ^processor /proc/cpuinfo 2>/dev/null').read()


if __name__ == '__main__':
    print(
        "GCCBench V1.0\n\nTime: [{}]\n\nStarting Prepare Code".format(get_time()))
    core_count = prepare_code()
    build_start = get_time()
    print("Start Build Time: [{}], Thread: {}".format(build_start, core_count))
    command_runner('make -C nginx-1.19.4/ -j{}'.format(core_count))
    end_time = get_time()
    print("End Build Time: [{}]".format(end_time))
    print("Summary: \n\t Build with [{}] thread\n\t Start time: {} \n\t End time: {}".format(core_count, build_start, end_time))
    
