Goal: Being able to write back-compatible code as seamlessly as possible.

Those "if python version" bits uglify code. 

Those "try...except ImportError" are not much better. 

If we had an `fallbacks` mapping between object references (e.g. `(functools, 'cached_property'`) and fallback alternatives, 
we could make a function that fallsback on these alternatives if objects are not found. 

Something like this:

```python
not_found = None

# why module AFTER obj_name? So that we can curry module out if needed (i.e. fix it with partial)
def get_obj(obj_name, module, fallbacks): 
    obj = getattr(module, obj_name, fallbacks.get((module, obj_name), not_found))
    if obj is not_found:
        raise ImportError("Couldn't import {obj_name} from {module}")
    return obj
```

Example:

```python

import functools


def compose_two_functions(f, g):
    return lambda *args, **kwargs: g(f(*args, **kwargs))

my_fallbacks = {
    (functools, 'cached_property'): compose_two_functions(functools.lru_cache, property),
    (functools, 'compose'): compose_two_functions,  # I wish functools had a compose!
}

my_obj_getter = functools.partial(get_obj, fallbacks=my_fallbacks)

assert my_obj_getter('cached_property', functools) == functools.cached_property
assert my_obj_getter('compose', functools) == compose_two_functions
```

Now, the question is, how do we make it as easy as possible for someone to use this?

Sure, they can already use this `get_obj` as is, but it would be nice to achieve the same results while changing the user code minimially, if at all.

For example, we could have the user just change where he gets the objects they want to have fallbacks for. Say replacing this:

```python
from original_place import obj
```

to

```
from my_fallback_place import obj
```

There must be a better way...

If we could intercept the access to `original_place` from outside the module where `from original_place import obj` is, 
we can do this doctoring externally.

But how?


