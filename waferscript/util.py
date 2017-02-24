
from . import config


def dbg_print(s):
    if config.debug:
        print('DEBUG: ' + s)