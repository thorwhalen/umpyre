# Problem: You have a powerful flexible function, but want to offer use-case specific versions of it.

This can happen when function has many many arguments, and you'd like a few use-case specific facades. 
It also happens with few, but quite high level interfaces that could use a few specific versions. 

# Solution: Use `functools.partial` and function attributes.

The pros and cons of what I'm proposing aren't completely clear (at the time of writing this), but it has been convenient at times. 

The idea is: Use partial to fix some of the arguments, and function attributes to give the combo a name. For example

```python
from functools import partial
def foo(a, b=None, c=42, **kwargs):
    return a, b, c, kwargs

foo.hello = partial(foo, b='world', c=1984)
foo.using_kwargs = partial(foo, b='world', see='how', i='can', just='add', keyword_args='freely?')
```

Usage:

```python
>>> foo.hello('world')
('world', 'world', 1984, {})
>>> foo.using_kwargs('now')
('now', 'world', 42, {'see': 'how', 'i': 'can', 'just': 'add', 'keyword_args': 'freely?'})
```

But you don't have to have a lot of arguments for this to make sense. 
Sometimes you just have one or two general arguments, but want to help the user out by showing them how to use it. 

See below some code I wrote to analyze dependencies (you can find it in 
[py2store.ext.module_imports](https://github.com/i2mint/py2store/blob/78afb14057cee59dee402aebb9d0445996c64b40/py2store/ext/module_imports.py).
In effect, it scans the code and yields a bunch of names recursively. Most of the time I just want the unique names, so I want to post-process with `set`. 
But what if I want to also get a count of their use (postprocess with `collections.Counter`), or only get third-party names 
(useful to list requirements when packaging)? See (reduced version) of how I did it below:

```python
import itertools
from py2store.ext.module_imports import ModuleImports

def imports_for(root, post=set):
    """Names imported (recursively) by `root`.
    
    >>> import wave
    >>> assert imports_for(wave) == {'warnings', 'builtins', 'sys', 'audioop', 'chunk', 'struct', 'collections'}
    """
    import itertools

    m = ModuleImports(root)
    imports_gen = itertools.chain.from_iterable(tuple(v) for v in m.values())
    if callable(post):
        return post(imports_gen)
    else:
        return imports_gen


from functools import partial
from collections import Counter

imports_for.set = partial(imports_for, post=set)
imports_for.set.__doc__ = "Set (so unordered and unique) imported names"

imports_for.most_common = partial(
    imports_for, post=lambda x: Counter(x).most_common()
)
imports_for.set.__doc__ = "imported names and their counts, ordered by most common"

imports_for.third_party = partial(
    imports_for,
    post=lambda module: set(
        xx.split(".")[0]
        for xx in module
        if xx.split(".")[0] not in python_names
    ),
)
imports_for.set.__doc__ = "imported names that are not builtin names (most probably third party packages)"
```

# Known limitations

First, if you use decorators, take care to decorate functions "correctly" ([see this article about that](https://hynek.me/articles/decorators/)): Decorators don't automatically copy "everything" over, not even when you use `functools.wraps` out of the box. Namely, they don't copy function attributes (unless you tell your decorator too!

Second, there's limitations of partial itself. But that's just a small limitation; you can easily write your own version of `partial` that does what you want.

