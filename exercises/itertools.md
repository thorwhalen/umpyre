
# Fan-out

## Problem

Write a function `kv_fanout` that has this behavior: given "adjacency lists" of a digraph, it iterates over edges.

```python
>>> adjacencies = {2: {11},
...                9: {11, 8, 10},
...                10: {11, 3},
...                11: {},
...                8: {7, 3}}
>>>
>>> assert list(kv_fanout(adjacencies)) == [(2, 11), (9, 8), (9, 10), (9, 11), (10, 3), (10, 11), (8, 3), (8, 7)]
```

## Solution

```python
from itertools import starmap, product, chain

# This would be the one liner:
def kv_fanout(mapping):
    return chain.from_iterable(
        starmap(lambda k, v: product([k], v), 
                adjacencies.items()))

# But perhaps this would allow one to break it down a bit more
def fanout_v(k, v):
    return product([k], v)

def mapkv(kvfunc, mapping):
    return starmap(kvfunc, mapping.items())

def kv_fanout(mapping):
    return chain.from_iterable(mapkv(fanout_v, adjacencies))
```
