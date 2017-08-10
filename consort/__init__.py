# -*- encoding: utf-8 -*-
from consort._version import __version_info__, __version__
del _version

from consort.tools import *

from abjad.tools import lilypondparsertools
lilypondparsertools.LilyPondParser.register_markup_function('vstrut', [])
del lilypondparsertools


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
