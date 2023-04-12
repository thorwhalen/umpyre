# Problem: Make a copy of a function

# Solution

Didn't find an easy builtin way. 
The best I found was `boltons.funcutils.copy_function`, but it didn't handle keyword-only defaults, and broke on custom callables. 
All `copy_function` does is make a `FunctionType` instance with attributes taken from the function to be copied. 
So I made a function called `copy_func` that takes care of the problems mentioned. 
I didn't extend it completely to all kinds of callables, but the version below is a bit less brittle.

I put this in [i2](http://github.com/i2mint/i2).


```python
def copy_func(func: Callable, copy_dict: bool=True):
    from types import FunctionType

    code = code or getattr(func, "__code__", None)
    if not isinstance(code, types.CodeType):
        raise TypeError(
            f"Expected a types.CodeType object, but got {type(code)=}"
        )
    globals_ = globals_ or getattr(func, "__globals__", {})
    new_func = FunctionType(
        code,  # if your func doesn't have a __code__ attr, can't make a copy!
        globals_,
        name=getattr(func, "__name__", None),
        argdefs=getattr(func, "__defaults__", None),
        closure=getattr(func, "__closure__", None)
    )
    if hasattr(func, "__kwdefaults__"):
        new_func.__kwdefaults__ = func.__kwdefaults__
    if copy_dict:
        new_func.__dict__.update(func.__dict__)
    return new_func
```

Try it out:

```python
f = lambda x, *, y=2: x * y

f.an_attr = 42

f_copy = copy_func(f)

assert f_copy(3) == f(3) == 6
assert f_copy.an_attr == f.an_attr == 42

# verify that making an attribute in one won't create an attribute in the other!
f.another_attr = 42
assert not hasattr(f_copy, 'another_attr')
f_copy.yet_another_attr = 84
assert not hasattr(f, 'yet_another_attr')
```


## What NOT to do: `copy.deepcopy`

It's a lie! The `deepcopy` of a function isn't even a copy!

```python
import copy

f = lambda x: x * 2
f.an_attr = 42

f_copy = copy.deepcopy(f)

assert f_copy(3) == f(3) == 6
assert f_copy.an_attr == f.an_attr == 42

# attributes in one will appear in the other
f.another_attr = 42
assert f_copy.another_attr == f.another_attr == 42
f_copy.yet_another_attr = 84
assert f.yet_another_attr == f_copy.yet_another_attr == 84

# This is because f_copy is actually NOT a copy. It's the same object:

assert id(f_copy) == id(f)
```
