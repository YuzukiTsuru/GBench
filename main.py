import argparse
import source
import utils

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="GBench v1.0")
    parser.add_argument('-n', '--name', default='gcc')
    args = parser.parse_args()

    timer_main = utils.timer()

    if 'gcc' in args.name:
        timer_main.timer_start()
        gcc_build = source.gcc()
        gcc_build.build_code()
        timer_main.timer_end()
    elif 'nginx' in args.name:
        timer_main.timer_start()
        nginx_build = source.nginx()
        nginx_build.build_code()
        timer_main.timer_end()
    else:
        raise 'The test of {} is not supported yet'.format(args.name)
