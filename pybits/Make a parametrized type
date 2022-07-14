## Problem: Make a parametrized type

Say I want to make a type that specifies that an object is a factory, that is, 
that the object is a `Callable` that returns a specific type. 
I would do it like so:

```python
from typing import Callable, NewType

ListFactory = NewType('ListFactory', Callable[..., list])
DictFactory = NewType('DictFactory', Callable[..., dict])
```

But what I'd rather do is have a Factory type that is "parametrizable", so I could just use Factory[list] and Factory[dict] instead?

## Answer: Use a generic.

Do this:

```python
from typing import T, Callable
Factory = Callable[..., T]
```

and now you have what you want:

```python
>>> Factory[int]
typing.Callable[..., int]
>>> Factory[dict]
typing.Callable[..., dict]
```
