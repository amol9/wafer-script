
from redlib.api.http import Cache as RedlibCache
from redlib.api.py23 import pickledumps, pickleloads

from .. import config


class Cache:

    def __init__(self):
        self._entries = {}
        self._cache = RedlibCache(config.home_dir_path)
        self.load()


    def add(self, key, value, pickle=False):
        self._entries[key] = value if not pickle else pickledumps(value)
        self.save()


    def get(self, key, pickle=False):
        value = self._entries.get(key, None)
        return pickleloads(value) if pickle and value is not None else value


    def save(self):
        self._cache.add('wafer', self._entries, 'never', pickle=True)


    def load(self):
        e = self._cache.get('wafer')
        self._entries = e or {}


cache = Cache()
