# Problem: Give classes sub-scripting abilities

# Solution: Since 3.7, `__class_getitem__`

```python
class A:
    filt = None
    def __class_getitem__(cls, filt):
        cls.filt = filt
        return cls  # (1) 

assert A.filt is None
AA = A[{'a': 2}]
assert AA.filt == {'a': 2}
aa = AA()
assert aa.filt == {'a': 2}
```

Note in (1) that anything can be returned. Perhaps information about the class, a random joke, etc.

It seems like the original intent was typing (see [PEP 560](https://www.python.org/dev/peps/pep-0560/)), 
but personally I'm hoping to apply it to be able to make specialized subclasses with an intuitive (?) concise language. 

Imagine a (py2store) store that points to dimensioned data source (think SQL table, mongo collection, or even files with parametrized paths). 
Right now, if we wanted to create a sub-store (class) from a more general store, we'd do something like:

```python
@wrap_kvs(...)
@cached_keys(...)
@filt_iter(...)
class SubStore(SourceStore):
    """Will filter for kind='tags' and provide values with only the fields ('bt', 'tt', 'tag')"""
```

If you want to reuse that mechanism often, you might make a decorator factory and use it when ever you need to make such a thing:

```python
def mk_sub_store(...filter_kwargs, ...wrap_kvs_kwargs, ...):
    ...

SubStore = mk_sub_store(SourceStore)

```

But maybe (just maybe) it's more natural to put the `mk_sub_store` logic in the `__class_getitem__` of the `SourceStore` (or higher) and do it this way:

```python
SubStore = SourceStore[...filter_kwargs, ...wrap_kvs_kwargs]
```

To a data scientist that is used to working with multi-dimensional arrays/tables, the `sub_stable = table[:, 2:8, :]` notation is a no-brainer on instances of tables.
Therefore the notation `MyTable = Table[:, 2:8, :]` on classes (that then just need to be instantiated to get the desired subtable from any source) should be natural.



