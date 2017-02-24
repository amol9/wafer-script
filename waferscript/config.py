import os
from os.path import join as joinpath, expanduser

from redlib.api.system import is_windows

def get_home_dir_parent():
    if is_windows():
        return os.environ['APPDATA']
    else:
        return expanduser('~')

home_dir_name = 'wafer' if is_windows() else '.wafer'
home_dir_path = joinpath(get_home_dir_parent(), home_dir_name)

prog_description = "A thin wrapper script around python to provide scripting facility for a python application."

debug = False
