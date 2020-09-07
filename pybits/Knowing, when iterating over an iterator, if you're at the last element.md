*# Problem: Knowing, when iterating over an iterator, if you're at the last element*

*# Solution*

```python
from typing import Iterable, Any, Tuple
def signal_last(it:Iterable[Any]) -> Iterable[Tuple[bool, Any]]:
    iterable = iter(it)
    ret_var = next(iterable)
    for val in iterable:
        yield False, ret_var
        ret_var = val
    yield True, ret_var
```
```python
>>> t = [1,2,3,4]
>>> for is_last, x in signal_last(t):
...     if is_last:
...         print(f"The last element was {x}")
The last element was 4
```
Found <https://medium.com/better-programming/is-this-the-last-element-of-my-python-for-loop-784f5ff90bb5|here>.