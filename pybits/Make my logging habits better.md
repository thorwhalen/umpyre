# Problem: Make my logging habits better.md

# Solution: Use decorators, and make them well

## Newborn

```python
def f(a, b=3):
    print(a, b)
    return a + b
```

## Toddler

```python
from logging import ...

logger = ...

def f(a, b=3):
    logger(a, b)
    return a + b
```

(Note: And in everything that follows, we'll say `print` to be connected with our inner newborns, 
but in real life we should consider using the `logging` module or such)

### Child

```python
def add_log(func, logger=print):
    def _func(*args, **kwargs):
        logger(args, kwargs)
        return func(*args, **kwargs)
    return _func
 ```
 
 ### Teen

Child's critique: Would be better if:
* the function didn't looses it's signature (use wraps for that) and
* the function could be pickalable
* the decorator could be used both as a "decorator factory" and a decorator.

So we give you this:

 ```python
 from functools import wraps, partial

def add_log(func=None, *, logger=print):
    if func is None:
        return partial(add_log, logger=logger)
    else:
        @wraps(func)
        def _func(*args, **kwargs):
            func_name = getattr(func, '__name__', '')
            logger(func_name, args, kwargs)
            return func(*args, **kwargs)
        return _func
```

![image](https://user-images.githubusercontent.com/1906276/138531425-da8aed2f-7394-4a25-921d-4ed3c5c9dff0.png)

#### Test code


```python
######################################################################
# You can just be quick and...

@add_log
def f(a, b=3):
    return a + b

f(10, b=42)

######################################################################
# You can also specify a different logger

def more_involved_logger(func_name, args, kwargs, log_call=print):
    args_str = ', '.join(map(str, args))
    kwargs_str = ', '.join(map(lambda kv: f"{kv[0]}={kv[1]}", kwargs.items()))
    log_call(f"{func_name}({args_str}, {kwargs_str})")

@add_log(logger=more_involved_logger)
def f(a, b=3):
    return a + b

f(10, b=42)

######################################################################
# you can also use like this

def f(a, b=3):
    return a + b

f = add_log(f, logger=more_involved_logger)

f(10, b=42)

######################################################################
# and you can pickle!

import pickle

unpickled_f = pickle.loads(pickle.dumps(f))

unpickled_f(10, b=42)

```
 

