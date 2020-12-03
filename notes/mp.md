# 2020-12-03

https://github.com/thorwhalen/umpyre/issues/8
settings/store-and-retrieve-app-data

* AoC: https://github.com/mjpieters/adventofcode

Configuration projects:

* https://pypi.org/project/dynaconf/
* https://pypi.org/project/python-decouple/

Formats:

* https://en.wikipedia.org/wiki/TOML -- has a nice comparison table with other Formats

Places to put configuration managed by  tool:

* `~/.config`: -- XDG freedesktop userdata standard
  * https://stackoverflow.com/questions/1024114/location-of-ini-config-files-in-linux-unix
  * https://unix.stackexchange.com/questions/33943/what-config-refers-to-and-how-to-put-files-there
  * https://www.freedesktop.org/wiki/Software/xdg-user-dirs/



see what pipx does for windows

* Windows env vars: https://docs.microsoft.com/en-us/windows/deployment/usmt/usmt-recognized-environment-variables
* MS's own standards on this: https://docs.microsoft.com/en-us/windows/uwp/design/app-s

# 2020-11-19

Questions?

* `__subclasscheck__` and `__instancecheck__` are methods on the **meta class**, not on the class itself.
* `isinstance(a, B)` and `issubclass(A, B)` ask `type(B)` to verify for a virtual instance or subclass check.

## Links

* Special method lookup rules: https://docs.python.org/3/reference/datamodel.html#special-method-lookup
  * `repr(instance)` vs `repr(type(instance))`. Where will you find the `__repr__` method?
  * standard rule: if the instance has the attribute, _use that directly_, don't go to the class.
  * doesn't work for `__repr__`, because `Class.__repr__(self)` should only work for instances.
  * Special methods, instead of `instance.__special__()`, always `type(instance).__special__(instance)`
  * Normal rule: if `instance.foo` doesn't exist, look for `type(instance).foo`, then perhaps bind that with `__get__(instance)`.

* `dict.__missing__`, if defined on subclass: https://github.com/python/cpython/blob/87c87b5bd6f6a5924b485398f353308410f9d8c1/Objects/dictobject.c#L2147-L2161

```c
        if (!PyDict_CheckExact(mp)) {
            /* Look up __missing__ method if we're a subclass. */
            PyObject *missing, *res;
            _Py_IDENTIFIER(__missing__);
            missing = _PyObject_LookupSpecial((PyObject *)mp, &PyId___missing__);
            if (missing != NULL) {
                res = PyObject_CallOneArg(missing, key);
                Py_DECREF(missing);
                return res;
            }
            else if (PyErr_Occurred())
                return NULL;
        }
        _PyErr_SetKeyError(key);
        return NULL;
```

* Chained exceptions, `raise KeyError(k)` **in the context of `except ...:` handler** will attach the old exception
   as `NewException().__context__`, the _implicit context_ of the exception. 

  ```python
  try:
    try:
      42/0
    except:
      raise KeyError("You dummy")
  except Exception as e:
    print(e.__context__)  # prints `ZeroDivisioError`.
  ```

* Explicit chaining: `raise Exception from other_exception`. That's explicitly connecting the two,
  then `NewException().__cause__` is set.

* Covered in https://docs.python.org/3/library/exceptions.html

* https://stackoverflow.com/questions/24752395/python-raise-from-usage


## Thor's notes

Q: Difference between `o.__class__` and `type(o)`
A: type is the API -- more "purist" to use that.

```python
  try:
    0/0
  except Exception as e:
    e.__context__
```


# 2020-11-12

## Links

### Parsing python
* https://github.com/palantir/python-language-server
* https://github.com/davidhalter/jedi

### Parsing docs:
* https://github.com/boisgera/pandoc
* https://github.com/bebraw/pypandoc

### controlling isinstance(obj, type) (without subclassing type)
* https://docs.python.org/3/reference/datamodel.html#customizing-instance-and-subclass-checks




## Review

https://github.com/i2mint/i2/blob/master/i2/io_trans.py

- look at singledispatch for type-based routing
- mapping proxy type (in types module): `types.MappingProxyType`


# 2020-10-29

## Single dispatch

Instead of

```python
def function(foo, ...):
    if isinstance(foo, Type1):
        return handle_type1(...)
    elif isinstance(foo, Type2):
        return handle_type2(...)
   ...
```

use `functools.singledispatch()`:

```python
from functools import singledispatch

@singledispatch
def function(foo, ...):
    # general case, not a specific type

@function.register
def _type1_handler(foo: Type1, ...):
    ...

@function.register
def _type2_handler(foo: Type2, ...):
    ...
```

See https://docs.python.org/3/library/functools.html#functools.singledispatch

## on Duck typing and testing vs exceptions.

* Python Forgiveness vs. Permission and Duck Typing
  https://softwareengineering.stackexchange.com/a/175663/55400

## Python 3.10 pattern matching

* https://www.python.org/dev/peps/pep-0634/
* https://www.python.org/dev/peps/pep-0635/
* https://www.python.org/dev/peps/pep-0636/

## Documentation consistency

* Sphinx substitutions: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#substitutions



# 2020-10-13

- `__future__`?
- resources with code: https://importlib-resources.readthedocs.io/en/latest/ is the backport for a new feature in Python 3.9:
   https://docs.python.org/3/library/importlib.html#module-importlib.resources


## Thor's Notes

https://stackoverflow.com/questions/64015729/python-when-you-don-t-want-to-require-a-third-party

package_resources




# 2020-10-06

- Using `__init__.py` in a package.
  - Short mention of dev needs vs. API user needs
  - `__init__.py` is always loaded when traversing a package
  - `def __getattr__(name): ...` (and `def __dir__(): ...`) in a module,
    https://docs.python.org/3/reference/datamodel.html#customizing-module-attribute-access

- annotations on new extensions
  - Zope Component Architecture: https://zopecomponent.readthedocs.io/en/latest/narr.html
  - Type hinting
    - https://instagram-engineering.com/let-your-code-type-hint-itself-introducing-open-source-monkeytype-a855c7284881
  





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
