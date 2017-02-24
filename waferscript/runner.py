
from .parser import Parser
from .lib import *

class Runner:

    def __init__(self):
        self._parser = None


    def run(self, script):
        self._parser = Parser(script)

        self._parser.parse()

        for i in self._parser.imports:
            exec(i, globals())

        exec(self._parser.script.py_script, globals())
