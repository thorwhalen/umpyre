# Problem: Simple input-output Logging without changing inner code of function

You're debugging some code and want calls to specific functions to be printed (input and output).

You know you it's better to avoid writing debug prints in the code. 

# Solution: Logger decorator

```python
from functools import wraps


def args_kwargs_sequence(args, kwargs):
    return f"{', '.join(map(str, a))}, {', '.join(f'{k}={v}' for k, v in k.items())}"


def io_logger(func):
    @wraps(func)
    def _func(*args, **kwargs):
        print(f"{func.__name__}({args_kwargs_sequence(args, kwargs)})")
        out = func(*args, **kwargs)
        print(f"\t-> {out}")
        return out
    return _func
```

Demo of use:

```python
@io_logger
def foo(a, b=0):
    return a + b

@io_logger
def bar(a, b=2):
    return a * b

def baz(a, b=1):
    return foo(a, b) / bar(a, b)

```

```python
>>> baz(3,0)
foo(1, 2, asd=3, df=df)
	-> 3
bar(1, 2, asd=3, df=df)
	-> 0
```

Many extensions possible: Adding function call (count/index) tracking, tabulation with inner calls, etc.
