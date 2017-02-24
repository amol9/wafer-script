
from .stack import Stack


class Script:

    def __init__(self, filepath=None, script=None, stack_name=None):
        # read from stdin if possible

        self.script = None

        if filepath is not None:
            self.script = self.read_script_from_file(filepath)
        elif script is not None:
            self.script = script
        else:
            self.script = self.get_script_from_stack(stack_name)

        self.py_script = None


    def read_script_from_file(self, filepath):
        try:
            with open(filepath, 'r') as f:
                return f.read()
        except (OSError, IOError) as e:
            raise ScriptError(e.message)


    def get_script_from_stack(self, name):
        stack = Stack()
        return self.read_script_from_file(stack.load_script(name))
