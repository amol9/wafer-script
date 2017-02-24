

from redcmd.api import Subcommand, subcmd

from .runner import Runner
from .script import Script
from . import config


class WaferCli(Subcommand):

    @subcmd
    def eat(filepath=None, code=None, stack_name=None, debug=False):
        '''
        Execute a wafer script.

        filepath:   path to the script file
        code:       script as a command line argument
        stack_name: name of the wafer on the stack
        '''
        config.debug = debug

        script = Script(filepath=filepath, script=code, stack_name=stack_name)
        runner = Runner()
        runner.run(script)


    @subcmd
    def stack(name, filepath=None, code=None):
        '''
        Put wafer script on the stack with a name.

        name:       identifier for the script
        filepath:   path to the script file
        code:       script as a command line argument
        '''

        pass


    @subcmd
    def dump():
        '''
        List all the wafers on the stack.
        '''

        pass
