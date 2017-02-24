
class Stack:

    def __init__(self, path):
        self._path = path
        self._map = None


    def load_map(self):
        pass


    def save_map(self):
        pass

    
    def load(self, name):
        script_path = self._map.get(name, None)

        if script_path is not None:
            return script_path
        else:
            raise StackError('script not found')


    def save(self, name):
        pass
        