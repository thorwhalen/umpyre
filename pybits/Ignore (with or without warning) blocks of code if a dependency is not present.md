# Problem: Ignore (with or without warning) blocks of code if a dependency is not present.

# Solution: A context manager

Note (after the fact): In fact there's a much simpler way for the simple base (but common) case: https://docs.python.org/3.5/library/contextlib.html#contextlib.suppress

Example:
```python

with suppress(ZeroDivisionError, TypeError):  # enter number of comma separated error classes you want to ignore
    print('about to divide by zero...')
    0/0
    print('this line will not be executed')
# Will print "about to divide by zero...", but no error is raised.
```

So the ModuleNotFoundIgnore I wrote all over code since this summer can be replaced by:

```python
from functools import partial
from contextlib import suppress

ModuleNotFoundIgnore = partial(suppress, ModuleNotFoundError) 
```

Older:
A spelled out version of a context manager that ignores `ModuleNotFoundError` (only), but will also print a message...

```python
class ModuleNotFoundManager:
    """(Context) managing ModuleNotFoundErrors (ignore, log, or other creative uses...)

    Specifying no arguments will result in ignoring whole block silently

    >>> with ModuleNotFoundManager():
    ...     import i_do_not_exist

    Specifying a message will result in calling the log_func (default is ``print``) with msg as the argument.

    >>> with ModuleNotFoundManager("That module does not exist"):
    ...     import i_do_not_exist.either
    That module does not exist

    """

    def __init__(self, msg=None, log_func=print):
        self.msg = msg
        self.log_func = log_func

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ModuleNotFoundError:
            if self.msg is not None:
                self.log_func(self.msg)
        return True
```
