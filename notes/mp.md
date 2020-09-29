



# 2020-09-29

- areas for questions
  - documentation generation
  - packaging (pip installable)
    - projects that can help:
      - poetry: https://python-poetry.org/
      - flit: https://flit.readthedocs.io/en/latest/
    
## project examples:

- https://github.com/mjpieters/aiolimiter

## Decorators and names

```python
from functools import wraps


def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper


@decorator
def foobar():
    pass

# simplified explanation
def foobar():
    pass

# bytecode FUNCTION name codeobject -> push on the stack
# decorator(TOS) -> pushed to stack

# SET sets name in the current namespace to the TOS
# foobar exists
```

## Thor's notes
```python
from foo import Bar

Bar2 = deco(Bar)
Bar2.__name__ == Bar.__name__  # problem?
```

```python
# I am in bar.py
from foo import A
B = deco(__module__=__name__)(A)
<class deco.<local>.inner.A at <...>>```

import sys
sys._getframe(1)  # https://docs.python.org/3/library/sys.html#sys._getframe
```

```python
class Decorator:
    def __init__(self, args):
        self.arg = args
    def __call__(self, f):
        @wraps(f)
        def wrapper(..):
            ...
        return wrapper


foo.<locals>.wrapper
```


# 2020-02-04

## Thor's notes
Try out using __init_subclass__ to create classes (when more flexibility is needed) instead of functions.


### Meta and 
How to use in my context?

https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__
https://stackoverflow.com/a/45400561/100297
()
### Enable and control tab-completion for custom mappings
And the pros/cons of exposing mapping keys as attributes.
Relevant: https://stackoverflow.com/questions/42771236/tab-complete-key-for-getitem-in-python-class

### type(name, bases, attr_dict)
`MyClass = type(name='MyClass', bases, attr_dict)`
The name specification annoyingly redundant. Safe ways to avoid this?
Class statement does two things:
* Creates a class
* Assigns to name

### List of attributes needed to compute a function/method
Marshmallow: Simplified serialization? Not nearly simple enough.
What I would have expected, is a (semi-)auto generation of the schema. 
But do I need `deserialize(serialize(obj)) == obj`?
Absolute `==` is nearly impossible, and not even necessary. 
What is NEEDED is for the deserialized obj to be **functionally equivalent** over a specific set of functions. 

See for example
https://stackoverflow.com/questions/57083061/python-get-a-list-of-attributes-used-by-a-method


### signature calculus 


### Infinite string that works with re


### what to do with __module__ of stores and make them picklable?


### pickle repairing
zope has some stuff for this


## MP

## use case: configure wrapper for *instances* of a kvstore


```python
# configuration
class FooBar(KVStoreWrapper):
    key_handler = FooBarKeyHandler
    value_handler = CSVHandler(sep="\t", encoding="shiftjs")
```

```python
# using the configured class
instance_of_kvstore = SomeKindOfKVStore(arg1, arg2)
wrapped = FooBar(instance_of_kvstore)
isistance(wrapped, SomeKindOfKVStore)  # False

instance_of_kvstore_subclass = SomeOtherKindOfKVStore(arg1, arg2)
wrapped2 = FooBar(instance_of_kvstore_subclass)
```
#

# use case: configure a class you instantiate directly

```python
# configuration
class FooBar(SomeKindOfKVStore, KVStoreWrapper):
    key_handler = FooBarKeyHandler()
    value_handler = FoobBarKey()
```

```python
# using the configured class
wrapped = FooBar(arg1, arg2)
isistance(wrapped, SomeKindOfKVStore)  # True
```


# 2020-01-28

* Question on SO: https://stackoverflow.com/questions/59904817/extending-wrapping-python-collections

## projects that use "class Meta"

* Django's Model and Form definitions
* WTForm
* Marshmallow

## Techniques

* https://docs.python.org/3/reference/datamodel.html#customizing-class-creation

## Mapping adapter definitions

* Audience: Data scientist / data engineer

Mappings consist 

## Example

```python
class FilenameMapper(Translator):
    def private(self, public, context):
        # filename -> full path
        return os.path.join(context.base, public)

    def public(self, private, context):
        return os.path.relative(...)


class MyKVStore(KVStore):
    class Meta:
        store = FilesystemStore("/path/to/something")
        keys = FilenameMapper()
        values = TextMapper(encoding="utf8")


print(MyKVStore)
# MyKVStore(store=<default>


class MoreComplex(KVStore):
    class Meta:
        store = ....
        keys = SpecialisedKeyValueTransformer(store)
        values = keys.valuetranformer()
```

-------

## Thor

```python
def wrap_kvs(
  store, name, *,
  key_of_id=None, id_of_key=None, obj_of_data=None, data_of_obj=None, postget=None)
```


```python
class MyStore(Store):
  def _id_of_key(self, k):
    return _id
```


# 2019-09-25

# Session notes

Projects:

* https://github.com/i2mint/py2store (https://pybay.com/speaker/thor-whalen/)
* https://github.com/thorwhalen/py2api
* https://github.com/thorwhalen/py2dash

## Issues / subjects

* Sense of a feature not fitting with the architecture
* Pythonic API design?

## links

### Tools

* https://pre-commit.com/

  Example: https://github.com/psf/black/blob/master/.pre-commit-config.yaml

* black: https://github.com/psf/black
* flake8: http://flake8.pycqa.org/en/latest/

* example project using the above: https://github.com/mjpieters/collegial



## Thor's scrap

```python
  def __contains__(self, k) -> bool:
      return self.store.__contains__(self._id_of_key(k))
```
