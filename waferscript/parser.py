import re

from .util import dbg_print


class Parser:

    def __init__(self, script):
        self.script = script

        self.imports = []
        self._ws_use_regex = re.compile("^ws:use\s+(.*)")


    def parse(self):
        self.parse_use()

        self.strip_ws_statements()


    def parse_use(self):
        matches = self._ws_use_regex.finditer(self.script.script)

        for m in matches:
            module = m.group(1)
            dbg_print('module: %s'%module)

        self.imports.append('from %s.wafer import *'%module)


    def parse_arg(script):
        ws_arg_regex = None


    def strip_ws_statements(self):
        temp = None
        temp = self._ws_use_regex.sub('', self.script.script)

        self.script.py_script = temp
