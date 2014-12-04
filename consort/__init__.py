# -*- encoding: utf-8 -*-
from consort.tools import *


DEBUG = True


def debug(message):
    r'''Prints `message` in red when `consort.DEBUG` is true.

    Returns none.
    '''
    RED = '\033[91m'
    END = '\033[0m'
    if DEBUG:
        print(RED + message + END)