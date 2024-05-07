import os
import sys


def get_root_dir() -> str:
    return os.path.dirname(sys.modules['__main__'].__file__)
