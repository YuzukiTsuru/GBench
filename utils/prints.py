from tqdm import tqdm

from .get_time import get_time


def color_thread_stdout(color_thread_str: str, print_str: str) -> str:
    return '{} | {}'.format(color_thread_str, print_str)


class Prints:
    def __init__(self, stage):
        self.tqdm = tqdm(bar_format='{postfix[0]} | {postfix[1]} | {postfix[2]}', postfix=[None, stage, None])

    def prints(self, print_str: str, color_thread=None):
        if color_thread is None:
            self.tqdm.postfix[0] = get_time()
            self.tqdm.postfix[2] = print_str
            self.tqdm.update()
        else:
            self.tqdm.postfix[0] = get_time()
            self.tqdm.postfix[2] = color_thread_stdout(color_thread, print_str)
            self.tqdm.update()

    def new_prints(self, print_str: str):
        self.tqdm.postfix[0] = get_time()
        self.tqdm.postfix[1] = print_str
        self.tqdm.update()
