## Problem: Counting things and operating on counts of things

## Solution: from collections import Counter
You know it. If you don't: Do. It's simple and so powerful.
I mention this today because I discovered (or rediscovered) that `Counter`, though it's a dict, has also some extra dunders that just make sense (never noticed, but you don't see dunders when you tab-complete!).

You can make one from an iterable (even if not in memory), and update an existing one, just like a dict.
But also:
You can use `+, -, & and |`.
For mathematicians here: It's a multiset, simply put.

```python
>>> from collections import Counter
>>>
>>> Counter.mro()  # Counter is a dict!
[<class 'collections.Counter'>, <class 'dict'>, <class 'object'>]
>>>
>>> set(dir(Counter)) - set(dir(dict))  # but has more!
{'__missing__', '__isub__', '__add__', '__module__', '__ior__', 'most_common', '__sub__', '__pos__', 'subtract', '__iadd__', '__and__', '__dict__', '_keep_positive', '__iand__', '__weakref__', '__neg__', '__or__', 'elements'}
>>>
>>> t = Counter('aaaaabbbc')
>>> tt = Counter('bbccccdddddd')
>>>
>>> t + tt
Counter({'d': 6, 'a': 5, 'b': 5, 'c': 5})
>>> t - tt
Counter({'a': 5, 'b': 1})
>>> t & tt
Counter({'b': 2, 'c': 1})
>>> t | tt
Counter({'d': 6, 'a': 5, 'c': 4, 'b': 3})
```
