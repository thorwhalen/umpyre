Problem: Define types, and use them in type annotations as well as in `isinstance` checks

Solution: Search for it online (perhaps `typing` or `mypy` have some tricks?), but here are my hacks:

```python
from typing import Union, Optional, Callable, Iterable, Awaitable  # etc.

assert isinstance(lambda x: x, Callable)
assert isinstance([1,2,3], Iterable)
```
This unfortunately doesn't work:
`assert isinstance(None, Union[Iterable, None])` 

Indeed: `isinstance(Union[Iterable, None], type) == False  !!`

Alternative 1:
```python
IterableOrNone = (Iterable, type(None))

assert isinstance([1,2,3], IterableOrNone)
assert isinstance(None, IterableOrNone)
assert not isinstance(3.14, IterableOrNone)
```
Alternative 2:
```python
IterableOrNone = Union[Iterable, None]  # equivalent to Optional[Iterable]
assert isinstance([1,2,3], IterableOrNone.__args__)
assert isinstance(None, IterableOrNone.__args__)
assert not isinstance(3.14, IterableOrNone.__args__)
```
