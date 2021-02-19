# Problem: You always forget the difference between a generator, an iterator, and an iterable

# Solution: Ask python itself (namely the typing module

And have code speak to you, while asserting the truth of what it's speaking:

```python
from typing import Generator, Iterator, Iterable

a_list = [1, 2, 3]
assert not isinstance(a_list, Generator)
assert not isinstance(a_list, Iterator)
assert isinstance(a_list, Iterable)

assert not isinstance(iter(a_list), Generator)
assert isinstance(iter(a_list), Iterator)
assert isinstance(iter(a_list), Iterable)

def gen():
    yield 1
    yield 2
    yield 3
    
assert not isinstance(gen, Generator)
assert isinstance(gen(), Generator)
assert isinstance(gen(), Iterator)
assert isinstance(gen(), Iterable)
```
