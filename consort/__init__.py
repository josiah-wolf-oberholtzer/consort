# -*- encoding: utf-8 -*-
from consort.tools import *


DEBUG = False


def debug(message):
    r'''Prints `message` in red when `consort.DEBUG` is true.

    Returns none.
    '''
    RED = '\033[91m'
    END = '\033[0m'
    if DEBUG:
        print(RED + str(message) + END)


from abjad.tools import lilypondparsertools
lilypondparsertools.LilyPondParser.register_markup_function('vstrut', [])