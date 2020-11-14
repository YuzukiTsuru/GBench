from colorama import Fore

BUILD = Fore.YELLOW + "Build" + Fore.WHITE

DOWNLOAD = Fore.CYAN + 'Download file' + Fore.WHITE
DECOMPRESS = Fore.CYAN + 'Decompress file' + Fore.WHITE
CONFIGURE = Fore.CYAN + 'Configure Build Script' + Fore.WHITE

PROCESS = Fore.RED + 'Processing' + Fore.WHITE

DEFAULT = Fore.WHITE

SUCCESS = Fore.LIGHTYELLOW_EX + "\n\nSubprogram Success\n\n" + Fore.WHITE
FAIL = Fore.LIGHTYELLOW_EX + "\n\nSubprogram Fail\n\n" + Fore.WHITE


def add_colior_thread(num: int) -> str:
    return Fore.LIGHTGREEN_EX + 'Compile Thread: ' + str(num) + Fore.WHITE
