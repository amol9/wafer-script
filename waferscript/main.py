import re
from importlib import import_module

from redcmd.api import execute_commandline

from .cli import WaferCli
from . import config
from . import version


def main():
    execute_commandline(prog='wafer', description=config.prog_description, version=version.version)
