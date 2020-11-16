import os
from utils.command_runner import command_runner
from utils.core_count import core_count
from utils.color_static import *


class gcc:
    def __init__(self):
        self.package_name = 'gcc-9.3.0'
        self.core_num = core_count()
        self.prepare_code()

    def prepare_code(self):
        command_runner('sudo apt-get install -y build-essential libgmp-dev libmpfr-dev libmpc-dev')
        if not os.path.exists('{}.tar.gz'.format(self.package_name)) or not os.path.exists(self.package_name):
            command_runner('wget https://mirrors.aliyun.com/gnu/gcc/{}/{}.tar.gz'.format(self.package_name, self.package_name), DOWNLOAD)
            command_runner('tar xvzf {}.tar.gz'.format(self.package_name), DECOMPRESS)
        command_runner('./configure', CONFIGURE, cwd_dir=self.package_name)

    def build_code(self):
        command_runner('make clean', CLEAN, cwd_dir=self.package_name)
        command_runner('make -j{}'.format(self.core_num), BUILD, thread_num=self.core_num, cwd_dir=self.package_name)

    def get_core_count(self) -> int:
        return self.core_num
