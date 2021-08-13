# Problem: You want to use cached_property before 3.8

`cached_property`, which some of you might recognize as `lazyprop` is very useful. 
It's one of those "could always do without it, but once you start using it you realize how much complexity it frees you from". 

Before `python` decided to include it in it's standard lib (as `functools.cached_property`) I copy pasted my own
(based on Based on code from David Beazley's "Python Cookbook") everywhere. 
Then, I imported `cached_property` when available, with a fall back to `lazyprop` when not.
Then I said **to the hell with encouraging people to live in the past** and just assumed everyone is in `3.8+`. 

# Solution: It's just the composition of `lru_cache` and `func`

I just discovered that `cached_property` is **nearly equivalent** to the compositon of `functools.lru_cache` and `property`.
So now, enabling the <3.8 folk can be done even more simply:

```python
try:
    from functools import cached_property
except ImportError:
    from functools import lru_cache
    def cached_property(func):
        return property(lru_cache(func))
```

Or for those functional-style lovers who use `lined`, checkout this one-liner beauty:

```
import functools
from lined import Pipe

cached_property = getattr(functools, 'cached_property', Pipe(functools.lru_cache, property))
```

And okay, we don't need `lined` for that (that was just marketing). We can do this with builtins only:

```
import functools

compose_two_functions = lambda f, g: lambda *args, **kwargs: g(f(*args, **kwargs))
cached_property = getattr(functools, 'cached_property', compose_two_functions(functools.lru_cache, property))
```

Here's some code to test your `cached_property`:

```python
class MyClass:
    @cached_property
    def foo(self):
        print("The first time I encounter foo, I need to compute it...")
        return 21 * 2


t = MyClass()
t.foo, t.foo
# The first time I encounter foo, I need to compute it...
# (42, 42)
```
