
from redlib.api.system import sys_command


def internet():
    r, _ = sys_command("ping -n 1 8.8.8.8")
    return r == 0

