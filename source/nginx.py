import os
from utils.command_runner import command_runner
from utils.core_count import core_count


class nginx:
    def __init__(self):
        self.package_name = 'nginx-1.19.4'
        self.core_num = core_count()
        self.prepare_code()

    def prepare_code(self):
        os.system(
            'sudo apt install -y libtool build-essential libpcre3 libpcre3-dev zlib1g-dev openssl wget')
        os.system(
            'wget http://nginx.org/download/{}.tar.gz'.format(self.package_name))
        os.system('tar xvzf {}.tar.gz'.format(self.package_name))
        os.system('cd {} && ./configure'.format(self.package_name))

    def build_code(self):
        command_runner(
            'make -C {}/ -j{}'.format(self.package_name, self.core_num))
