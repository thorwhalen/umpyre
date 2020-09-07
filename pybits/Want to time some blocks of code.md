## Problem: Want to time some blocks of code

## Solution: Use a context manager

## Problem: Want to time blocks of code, but also print (or log) feedback on entering and/or exiting this block

## Solution: Use a context manager (like I said)

Here's an example that solves that problem, but you can make it even more light weight if you need,
Here I give control over what "print" actually means (could mean `logging.log` for example).
Can also use a `verbose` flag to control.
By default, will only print elapsed times.

```python
class TimerAndFeedback:
    """Context manager that will serve as a timer, with custom feedback prints (or logging, or any callback)"""

    def __init__(self, start_msg="", end_msg="", verbose=True, print_func=print):
        self.start_msg = start_msg
        if end_msg:
            end_msg += '\n'
        self.end_msg = end_msg
        self.verbose = verbose
        self.print_func = print_func  # change print_func if you want to log, etc. instead

    def print_if_verbose(self, *args, **kwargs):
        if self.verbose:
            if len(args) > 0 and len(args[0]) > 0:
                return self.print_func(*args, **kwargs)

    def __enter__(self):
        self.print_if_verbose(self.start_msg)
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        self.print_if_verbose(self.end_msg + f"Took {self.elapsed:0.1f} seconds")

    def __repr__(self):
        return f"elapsed={self.elapsed} (start={self.start}, end={self.end})"
```
Example:
```python
    >>> with TimerAndFeedback():
    ...     time.sleep(0.5)
    Took 0.5 seconds
    >>> with TimerAndFeedback("doing something...", "... finished doing that thing"):
    ...     time.sleep(1)
    doing something...
    ... finished doing that thing
    Took 1.0 seconds
    >>> with TimerAndFeedback(verbose=False) as feedback:
    ...     time.sleep(1)
    >>> # but you still have access to some stats through feedback object (like elapsed, started, etc.)
```
Answer to <@U9PRQB5Q8>’s request.

Not sure I understand what you want, but according to my understanding, you can do this:

*# Problem: A decorator to "inject" arguments*

*# Solution: Use functools.partial* 
You could do it from scratch, of course:
```python
def inject_args(*args, **kwargs):
    def _func(func):
        def __func():
            return func(*args, **kwargs)
        return __func
    return _func
```
But this might look cooler (as long as your function doesn't have position only arguments)
```python
from functools import partial

def inject_args(**kwargs):
    return lambda func: partial(func, **kwargs)
```
Both produce this behavior:

```python
@inject_my_args
def prod_of_my_args(a, b):
    return a * b

@inject_my_args
def sum_of_my_args(a, b):
    return a + b

assert prod_of_my_args() == 6
assert sum_of_my_args() == 5
```
I prefer the one using `partial` because with it you can... well, specify the arguments partially only:

You wouldn't be able to do the following with the custom one I mentioned:

```python
@inject_args(b=3)
def sub_of_my_args(a, b):
    return a - b

assert sub_of_my_args(5) == sub_of_my_args(a=5) == 2

@inject_args(a=5)
def sub_of_my_args(a, b):
    return a - b

assert sub_of_my_args(b=2) == 3
# but you wouldn't be able to do sub_of_my_args(2) (name "b" needs to be specified)
```

Finally, if you want to do something like this, but will a "pool of arguments to inject, IF AND WHEN they're required", you could do this:

```python
def inject_args(**kwargs):
    def inject_args_in_func(func):
        to_inject = {k: kwargs[k] for k in signature(func).parameters.keys() & kwargs}
        return partial(func, **to_inject)
    return inject_args_in_func
```
Example use:

```
my_injector = inject_args(a=2, b=3, var_that_no_one_uses='decoy')

@my_injector
def formula(a, b, c=1):
    return (a - b) * c

assert formula() == -1
assert formula(c=10) == -10
```
