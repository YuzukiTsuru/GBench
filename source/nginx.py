import os
from utils.command_runner import command_runner
from utils.core_count import core_count
from utils.color_static import *


class nginx:
    def __init__(self):
        self.package_name = 'nginx-1.19.4'
        self.core_num = core_count()
        self.prepare_code()

    def prepare_code(self):
        command_runner('sudo apt-get install -y libtool build-essential libpcre3 libpcre3-dev zlib1g-dev openssl wget')
        if not os.path.exists('{}.tar.gz'.format(self.package_name)) or not os.path.exists(self.package_name):
            command_runner('wget http://nginx.org/download/{}.tar.gz'.format(self.package_name), DOWNLOAD)
            command_runner('tar xvzf {}.tar.gz'.format(self.package_name), DECOMPRESS)
        command_runner('./configure'.format(self.package_name, self.package_name), CONFIGURE, cwd_dir=self.package_name)

    def build_code(self):
        command_runner('make clean', CLEAN)
        command_runner('make -C {}/ -j{}'.format(self.package_name, self.core_num), BUILD, thread_num=self.core_num)

    def get_core_count(self) -> int:
        return self.core_num
