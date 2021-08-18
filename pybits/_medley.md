
# negating a function, methodcaller, and not_

```python
from functools import partial
from operator import methodcaller, not_
from lined import Pipe


def negate(func):
    "returns a negated version of the func"
    return Pipe(func, not_)


startswith_caller = partial(methodcaller, 'startswith')
startswith_osdot = startswith_caller('os.')

assert startswith_osdot('os.path')
assert not startswith_osdot('ostentatious')

not_startswith_osdot = negate(startswith_osdot)  # the opposite of startswith_osdot

assert not not_startswith_osdot('os.path')
assert not_startswith_osdot('ostentatious')
```

