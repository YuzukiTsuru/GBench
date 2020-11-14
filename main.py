import argparse
import source.gcc as gcc
import source.nginx as nginx

import utils.timer as timer

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="GCCBench v1.0")
    parser.add_argument('-n', '--name', default='gcc')
    args = parser.parse_args()

    timer = timer.timer()

    if 'gcc' in args.name:
        timer.timer_start()
        gcc_build = gcc.gcc()
        gcc_build.build_code()
        timer.timer_end()
    elif 'nginx' in args.name:
        timer.timer_start()
        nginx_build = nginx.nginx()
        nginx_build.build_code()
        timer.timer_end()
    else:
        raise 'The test of {} is not yet supported'.format(args.name)
