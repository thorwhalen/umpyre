## Problem: Feel like doing boolean operator acrobatics, to the expense of a novice reader
You like the `x = x or {}` way of expressing the `if not bool(x): x = DFLT_X` but are wondering how you would do it if you needed a more complex condition than `bool` : Like, a way to perform `if not is_so(x): x = make_it_so(x)` logic?

## Solution
`x = (is_so(x) and x) or make_it_so(x)`
Think about it.

For example, instead of
```python
from typing import Iterable
if not isinstance(x, Iterable):  # if not iterable
    x = (x,)  # make it so
```
you could write:
```python
from typing import Iterable
x = (isinstance(x, Iterable) and x) or (x,)
```
But in all seriousness, it's probably better to do it this way:

```python
from typing import Iterable
def ensure_iterable(x):
    if isinstance(x, Iterable): 
        return x
    else:  # if not iterable, make it so...
        return (x,)

x = ensure_iterable(x)
```
So that (1) It's readable, (2) the function self documents itself, and (3) you can reuse a function call instead of a pattern!
