# -*- encoding: utf-8 -*-
from consort.tools import *


DEBUG = False


def debug(*message):
    r'''Prints `message` in red when `consort.DEBUG` is true.

    Returns none.
    '''
    RED = '\033[91m'
    END = '\033[0m'
    if DEBUG:
        if len(message) == 1:
            message = message[0]
        else:
            message = ' '.join(str(_) for _ in message)
        print(RED + str(message) + END)