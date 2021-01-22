
# Problem

Would like `dataclasses` to be able to have a validation switch. 
Preferably at the field level (but `dataclasses.field` function doesn't have such arguments), 
or at the very least at the class level (but `dataclasses.dataclass` doesn't have such an argument either. 

In code:

```python
from dataclasses import dataclass, field, fields
from typing import Union, Iterable

@dataclass
class D:
    x: int
    y: Union[Iterable, str] = 'hello'
        
D(1.2)  # I want this to fail (because 1.2 is not an int
```

I had a stab at class decorator to do this:

```python
from dataclasses import dataclass, fields
from functools import wraps

def validating_dataclass(cls):
    """Simple (no dataclass args) validatig dataclass"""
    @dataclass
    @wraps(cls, updated=())  
    class _cls(cls):
        def __post_init__(self):
            super().__post_init__()
            for f in fields(self):
                v = getattr(self, f.name)
                if not isinstance(v, f.type):
                    raise TypeError(f"{f.name} needs to be a {f.type}: Was {type(v)}")
    _cls.__name__ = cls.__name__
    _cls.__qualname__ = cls.__qualname__
    return _cls
```

But this doesn't even work where it "should" (I get an `AttributeError: x`), and it will not work even if I get past the `x` because of the `Union[Iterable, str] ` (will get `TypeError: Subscripted generics cannot be used with class and instance checks`).


# Solution

Found answer here [https://stackoverflow.com/a/50622643/5758423].

```python
mport inspect
import typing
from functools import wraps


def _find_type_origin(type_hint):
    if isinstance(type_hint, typing._SpecialForm):
        # case of typing.Any, typing.ClassVar, typing.Final, typing.Literal,
        # typing.NoReturn, typing.Optional, or typing.Union without parameters
        yield typing.Any
        return

    actual_type = typing.get_origin(type_hint) or type_hint  # requires Python 3.8
    if isinstance(actual_type, typing._SpecialForm):
        # case of typing.Union[…] or typing.ClassVar[…] or …
        for origins in map(_find_type_origin, typing.get_args(type_hint)):
            yield from origins
    else:
        yield actual_type


def _check_types(parameters, hints):
    for name, value in parameters.items():
        type_hint = hints.get(name, typing.Any)
        actual_types = tuple(
                origin
                for origin in _find_type_origin(type_hint)
                if origin is not typing.Any
        )
        if actual_types and not isinstance(value, actual_types):
            raise TypeError(
                    f"Expected type '{type_hint}' for argument '{name}'"
                    f" but received type '{type(value)}' instead"
            )


def enforce_types(callable):
    def decorate(func):
        hints = typing.get_type_hints(func)
        signature = inspect.signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            parameters = dict(zip(signature.parameters, args))
            parameters.update(kwargs)
            _check_types(parameters, hints)

            return func(*args, **kwargs)
        return wrapper

    if inspect.isclass(callable):
        callable.__init__ = decorate(callable.__init__)
        return callable

    return decorate(callable)


def enforce_strict_types(callable):
    def decorate(func):
        hints = typing.get_type_hints(func)
        signature = inspect.signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()
            parameters = dict(zip(signature.parameters, bound.args))
            parameters.update(bound.kwargs)
            _check_types(parameters, hints)

            return func(*args, **kwargs)
        return wrapper

    if inspect.isclass(callable):
        callable.__init__ = decorate(callable.__init__)
        return callable

    return decorate(callable)
```
