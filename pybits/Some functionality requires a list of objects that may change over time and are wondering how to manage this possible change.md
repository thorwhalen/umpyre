## Problem: Some functionality requires a list of objects that may change over time and are wondering how to manage this possible change

## Solution: Proposing several

Well... the first two I'm not really proposing (unless in very static cases)...

### Solution A

```python
def do_this(x):
    return x * 2
    
def do_that(y):
    return f"'{y}' means something."

def data_prep(data):
    data = do_this(data)
    data = do_that(data)
    return data
        
assert data_prep('tora ') == "'tora tora ' means something."
```

### Solution B

```python
def do_this(x):
    return x * 2
    
def do_that(y):
    return f"'{y}' means something."

prep_funcs = [do_this, do_that]

def data_prep(data):
    for proc_func in prep_funcs:
        data = proc_func(data)
    return data
        
assert data_prep('tora ') == "'tora tora ' means something."
```
Those solutions are what I usually find in people's code, and it's fine. It's even more readable for a stranger as long as the list isn't too big.

But it isn't robust to changes since the addition of a new object (here function) requires changing code.
The two solutions below don't.

### Solution C: Using a registering decorator

```python
# What you need
prep_funcs = list()

def append_to_prep_funcs(func):
    prep_funcs.append(func)
    return func

# The way you'd use it
@append_to_prep_funcs
def do_this(x):
    return x * 2
    
@append_to_prep_funcs
def do_that(y):
    return f"'{y}' means something."

def data_prep(data):
    for proc_func in prep_funcs:
        data = proc_func(data)
    return data
        
assert data_prep('tora ') == "'tora tora ' means something."
```

### Solution D : Using a class to group the objects

```python
# What you need
def non_underscored_attrs(cls):
    for k in cls.__dict__.keys():
        if not k.startswith('_'):
            yield cls.__dict__[k]

# The way you'd use it
class prep_funcs:
    def do_this(x):
        return x * 2

    def do_that(y):
        return f"'{y}' means something."

def data_prep(data):
    for proc_func in non_underscored_attrs(prep_funcs):
        data = proc_func(data)
    return data
        
assert data_prep('tora ') == "'tora tora ' means something."
```
