from colorama import Fore

BUILD = Fore.YELLOW + "Build" + Fore.WHITE

DOWNLOAD = Fore.CYAN + 'Download Source file' + Fore.WHITE
DECOMPRESS = Fore.CYAN + 'Decompress file' + Fore.WHITE
CONFIGURE = Fore.CYAN + 'Configure Build Script' + Fore.WHITE
CLEAN = Fore.CYAN + 'Clean last build file' + Fore.WHITE

PROCESS = Fore.RED + 'Processing' + Fore.WHITE

DEFAULT = Fore.WHITE

SUCCESS = Fore.LIGHTYELLOW_EX + "Subprogram Success" + Fore.WHITE
FAIL = Fore.LIGHTRED_EX + "Subprogram Fail" + Fore.WHITE


def add_colior_thread(num: int) -> str:
    return Fore.LIGHTGREEN_EX + 'Compile Thread: ' + str(num) + Fore.WHITE


def add_color_time(time_str: str) -> str:
    return Fore.LIGHTCYAN_EX + time_str + Fore.WHITE
