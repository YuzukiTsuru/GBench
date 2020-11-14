import os
from utils.command_runner import command_runner
from utils.core_count import core_count


class gcc:
    def __init__(self):
        self.package_name = 'gcc-9.3.0'
        self.core_num = core_count()
        self.prepare_code()

    def prepare_code(self):
        os.system('sudo apt install -y build-essential libgmp-dev libmpfr-dev libmpc-dev')
        if not os.path.exists('{}.tar.gz'.format(self.package_name)):
            os.system('wget http://nginx.org/download/{}.tar.gz'.format(self.package_name))
        os.system('tar xvzf {}.tar.gz'.format(self.package_name))
        os.system('cd {} && ./configure'.format(self.package_name))

    def build_code(self):
        command_runner('make -C {}/ -j{}'.format(self.package_name, self.core_num))
