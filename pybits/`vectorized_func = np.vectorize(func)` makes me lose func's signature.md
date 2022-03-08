
# Problem: `vectorized_func = np.vectorize(func)` makes me lose func's signature!

Here `np.vectorize`, but happens with some other annoying decorators as well.

# Solution

Without even using i2.wrapper (we could, but below is simpler and already setup to be pickalable).

```python
from i2 import Sig

def wrap_keeping_original_signature(wrapped, wrapper):
    return Sig(wrapped)(wrapper(wrapped))

def foo(x, y=1):
    return x + y

f = wrap_keeping_original_signature(foo, np.vectorize)
assert str(Sig(f)) == str(Sig(foo)) == '(x, y=1)'
assert list(f([1, 2, 3]) == [2, 3, 4])
assert list(f([1, 2, 3], 10) == [12, 13, 14])

# But if you're going to reuse this vectorize version a lot, better call partial
from functools import partial
my_vectorize = partial(wrap_keeping_original_signature, wrapper=np.vectorize)
f = my_vectorize(foo)
assert str(Sig(f)) == str(Sig(foo)) == '(x, y=1)'
assert list(f([1, 2, 3]) == [2, 3, 4])
assert list(f([1, 2, 3], 10) == [12, 13, 14])
```
