from collections.abc import Iterable

def mychain(*args):
    for arg in args:
        if isinstance(arg, Iterable):
            for i in arg:
                yield i
        else:
            yield arg
