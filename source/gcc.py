import os
from colorama import Fore
from utils.command_runner import command_runner
from utils.core_count import core_count


class gcc:
    def __init__(self):
        self.package_name = 'gcc-9.3.0'
        self.core_num = core_count()
        self.prepare_code()

    def prepare_code(self):
        command_runner('sudo apt install -y build-essential libgmp-dev libmpfr-dev libmpc-dev')
        if not os.path.exists('{}.tar.gz'.format(self.package_name)) or not os.path.exists(self.package_name):
            command_runner('wget https://mirrors.aliyun.com/gnu/gcc/gcc-9.3.0/{}.tar.gz'.format(self.package_name), (Fore.CYAN + 'Download file'))
            command_runner('tar xvzf {}.tar.gz'.format(self.package_name), (Fore.CYAN + 'Decompress file'))
        command_runner('./{}/configure'.format(self.package_name), (Fore.CYAN + 'Configure Build Script'))

    def build_code(self):
        command_runner('make -C {}/ -j{}'.format(self.package_name, self.core_num), (Fore.YELLOW + "Build"))

    def get_core_count(self) -> int:
        return self.core_num
