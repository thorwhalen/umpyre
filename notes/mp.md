# Upcoming

Littles:
- [unbox](https://github.com/i2mint/unbox/blob/247fe856c446061ea982b359105f113e7756ae16/unbox/base.py#L119) builtin_module_names not at all builtin module names
- [config store](https://github.com/i2mint/py2store/blob/master/py2store/slib/s_configparser.py) tests not working anymore
- [supressing ModuleNotFound and ImportError](https://github.com/i2mint/py2store/blob/master/py2store/__init__.py#L120) sanity check
- [bolton's make sentinel](https://boltons.readthedocs.io/en/latest/modules/boltons/typeutils.html#make_sentinel) review and commentary
- [Make aix configurable](https://github.com/thorwhalen/aix/issues/1)
- [Recursive subpackage/submodule walk](https://github.com/thorwhalen/aix/issues/2)


# 2021-05-06

https://github.com/search?l=&o=desc&q=user%3Athorwhalen+user%3Ai2mint+user%3Aotosense&s=updated&type=Issues

## WriteBackChainMap

* ChainMap `__getitem__` implementation: https://github.com/python/cpython/blob/611aa39142f156508945ac312724474c493a6691/Lib/collections/__init__.py#L935-L941

```python
from collections import ChainMap, deque
from collections.abc import MutableMapping

class WriteBackChainMap(ChainMap):
    max_key_search_depth = 0
    
    def __getitem__(self, key):
        q = deque([])
        for mapping in self.maps:
            try:
                v = mapping[key]             # can't use 'key in mapping' with defaultdict
                for d in q:
                    d[key] = v
                return v
            except KeyError:
                q.append(mapping)
        return self.__missing__(key)  
    
    def __len__(self):
        return len(set().union(*self.maps[:self.max_key_search_depth]))     # reuses stored hash values if possible

    def __iter__(self):
        d = {}
        for mapping in reversed(self.maps[:self.max_key_search_depth]):
            d.update(dict.fromkeys(mapping))    # reuses stored hash values if possible
        return iter(d)

    def __contains__(self, key):
        return any(key in m for m in self.maps[:self.max_key_search_depth])
    
```

## Templated project generator

[Populate based on folder templates](https://github.com/i2mint/wads/issues/3)
 
See cookiecutter: https://cookiecutter.readthedocs.io


## Fluid interface for py2store wrappers

* SQLAlchemy and Fluent APIs: https://stackoverflow.com/a/44649390/100297
* https://stackoverflow.com/questions/57040151/how-is-precedence-grouping-implemented-in-sqlalchemy
* https://stackoverflow.com/a/65773908/100297

TW: Fluent: https://github.com/dwt/fluent

# 2021-04-01

https://github.com/i2mint/mongodol/blob/d4e65280c660e1f40dae2933cfdfadcb3c91ec3e/mongodol/tracking_methods.py


## Proxying with special methods

Werkzeug had to solve this too:

https://github.com/pallets/werkzeug/blob/c4d85cb9e0e78c2d5786baad649100d42526c399/src/werkzeug/local.py#L467-L656

Part of https://werkzeug.palletsprojects.com/en/1.0.x/local/


# 2021-03-25

* Clearing methods, variants

  Base classes, mixins:

  ```python
  class DisabledClear:
      def clear(self):
          raise NotImplementedError(...)
  ```

  and then LBYL (Look Before You Leap):

  ```python
  # (not) isinstance(..., DisabledClear)
  ```
  
  
  or just not use `ininstance()` or the above mixin, just:

  ```python
  try:
      object.clear()
  except (AttributeError, NotImplementedError):
      pass
  ```

* Another option: descriptor that raises `AttributeError`:

  ```python
  class AttributeErrorAttribute:
      _name = "unnamed"
      def __set_name__(self, owner, name):
          self._name = name
      def __get__(self, *args):
          raise AttributeError(self._name)
  ```

  ```python
  try:
      object.clear
  except AttributeError:
      pass
  ```

* Cachetools feature request: https://github.com/tkem/cachetools/issues/176

* Avoiding sharing a cache between instances of a generated class, want to use a decorator

  Sol: have the decorator accept a *callback*, which creates the cache on first use.

  ```python
  def decorator_factory(cache_factory):   # callback == factory for the cache
      def decorator(f):
          @wraps(f)
          def wrapper_method(self, *args, **kwargs):
              try:
                  cache = self._memioze__cache
              except AttributeError:
                  cache = self._memioze__cache = cache_factory()

              if k not in cache:
                  val = method(self, k)
                  cache[k] = val  # cache it
                  return val
              else:
                  return cache[k]

          return wrapper
      return decorator

  class FooBar:
      @decorator_factory(dict)
      def decorated_function(self, foo, bar):
          # ...
  ```


# 2021-03-18

* Python steering council: https://github.com/python/steering-council

## Context managers

The `with` context manager can deal with up to 3 components:

1. The expression after `with` but before `as ...:` or `:`
2. The context manager, an object with `__enter__` and `__exit__` methods.
3. The return value from `__enter__`.

1 and 2 are _usualy the same object_, the original object can be used as a 
context manager. 3. is often the same as 2, when `__enter__` returns `self`. 
E.g. file objects do this.

```python
with open(...) as f:
    # (1) `open()` is not a context manager, the return value is, which is a file object, which is (2)
    # `f` is (3), but is also the same object as (2)
```

can be rewritten as

```python
f = open(...)
with f:
   # ... this is the same because `f.__enter__()` has returned `f`.
```
or

```python
f = open(...)
with f as f1:
   assert f is f1
   # ... this is the same because `f.__enter__()` has returned `f`.
```


## Further notes

For context managers, think of iterable vs iterator. 
- Iterator has a state: If we both have the same iterator, we share that state (the cursor).
- If instead I give you an iterable, you can make your own iterator with independent state


### Choices for behavior of bulk writes and context managers

- Passing on s has effect of independent s 
- Passing on s has effect of being same s (operations accumulate from different sources)

## Mapping View wrapping

Use factory methods to create the view classes instead (Gang of Four design patterns, not
suprisingly, calls this the : *Factory method pattern*):

```python
class BaseMapping:
    # factories for mapping view objects
    # that subclasses can replace
    KeysView = BaseKeysView
    ValuesView = BaseValuesView
    ItemsView = BaseItemsView

    def keys(self):
        # each of these methods use the factory method on self,
        # here that's self.KeysView(), and expect it to take specific arguments.
        return self.KeysView(self)

    def values(self):
        return self.ValuesView(self)

    def items(self):
        return self.ItemsView(self)


class SpecialKeysView(BaseMapping.KeysView):   # or SpecialKeysView(BaseKeysView)
    def extra_method(self):
        # ...


class SpecialMapping:
    KeysView = SpecialKeysView
    # ...


sm = SpecialMapping()
type(sm.keys())  # will be SpecialKeysView
```

If your subclassed factories need to accept extra arguments, you could use a `partial()`, or have the `__init__` method pull
in more information from the standard context that is passed in (in the above examples, `BaseMapping.keys()` passes in the
mapping object, `self`, to each factory call).


# 2021-03-11

Problem: https://github.com/thorwhalen/umpyre/issues/35

* AST example: https://stackoverflow.com/a/66582895/100297

   Core: `ast.get_source_segment(source, node)`
   https://docs.python.org/3/library/ast.html#ast.AST.lineno
   https://docs.python.org/3/library/ast.html#ast.get_source_segment


Problem: https://github.com/thorwhalen/umpyre/issues/31

* call a method on an arbitrary object with given arguments. "Call .method(arg1, arg2, kw=kwargval)"
  https://docs.python.org/3/library/operator.html#operator.methodcaller
  `methodcaller("startswith", "__")("__foo") =-> True`


## My Notes

Problem: https://github.com/thorwhalen/umpyre/issues/32

Try different solutions for the following (Inject the methods inside the class itself?)

- metaclasses
- decorator
- using locals()

https://github.com/otosense/linkup/blob/master/linkup/base.py

```python

# TODO: Inject the methods inside the class itself?
class OperableMappingNoDflts(dict):
    """OperableMapping with ALL operators of operator module (but without defaults)
    >>> from linkup.base import *
    >>> d = OperableMappingNoDflts({'a': 8, 'b': 4, 'c': 3})
    >>> dd = OperableMappingNoDflts(b=2, c=1, d=0)  # you can make one this way too
    >>>
    >>> d + 1
    {'a': 9, 'b': 5, 'c': 4}
    >>> d / dd
    {'b': 2.0, 'c': 3.0}
    >>> (d + 1) / dd
    {'b': 2.5, 'c': 4.0}
    """


def _binary_operator_method_template(self, y, op, factory):
    """"""
    if isinstance(y, Mapping):
        return key_aligned_val_op(self, y, op, empty_mapping_factory=factory)
    else:
        return map_op_val(self, y, op, factory)


# TODO: Make unary tools and inject to OperableMappingNoDflts
# for name, func in operator_name_funcs_1:
#     setattr(OperableMappingNoDflts, name, partialmethod(_binary_operator_method_template,
#                                                         op=func, factory=OperableMappingNoDflts))

for name, func in operator_name_funcs_2:
    setattr(
        OperableMappingNoDflts,
        name,
        partialmethod(
            _binary_operator_method_template,
            op=func,
            factory=OperableMappingNoDflts,
        ),
    )
```

# 2021-03-04

```python
class Number:
    ...

Number.foo = ...(Number)
```

* `property` answer: https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work-in-python/17330273#17330273
  Shows that `__get__` differentiates between access on the class and on an instance.


```python
from functools import partial
import functools

wraps = partial(functools.wraps, assigned=...., updated=...)

## Naming generated classes

* takes module and qualname arguments (first argument is class name) https://docs.python.org/3/library/enum.html#functional-api
* counter example: https://docs.python.org/3/library/dataclasses.html#dataclasses.make_dataclass
* counter counter example: https://docs.python.org/3/library/collections.html#collections.namedtuple takes module!

Proposed alternative syntax without decorator:

```python
class MyGraze(SourcedStore, store=LocalGrazed, source=Internet(), return_data_source=True):
    # perhaps
    # return_data_source = True
    # ...
    pass


# if you can reference keyword arguments on the generated class, use attributes 
# instead of keyword arguments.
print(MyGraze.return_data_source)  # True or AttributeError?
```

## My Notes

Look into separating __name__ etc. assignment in separate decorator


# 2021-02-25

- [Mapping views][1], quite simple collection objects that are live views.
- `__length_hint__` is never called if `__len__` is available. It is there purely for *unsized* objects,
  so `list()` and other such methods can pre-allocate memory (and so perform better).

- Attribute delegation on classes? -> MetaClass with `__getattr__`.

[1]: https://github.com/python/cpython/blob/f82578ace103ec977cec3424b20e0b5f19cf720e/Lib/_collections_abc.py#L797-L872

# 2021-02-18

## Parametric attribute generating in a class

```python
# preexisting:
# decorator() (a decorator)
# attributes (a sequence of existing attributes of Bar)
# Bar, a base class.

class Foo(Bar):
    for _name in attributes:
        locals()[name] = decorator(getattr(Bar, name))

    del _name
```

What happens? Everything under `class [name](...):` is *executable code*.

Take a class statement:

```python
class Foo:
    bar = "baz"
```

Python does this:

```python
def class_body():
    bar = "baz"
    return locals()

Foo = type("Foo", (object,), class_body())
```

## Counting an iterator as something else exhausts it

```python
from itertools import count
from operator import itemgetter

c = count()
countingiter = map(itemgetter(0), zip(origiter, c))

# use countingiter
# ask c for its next number
length = next(c)
```

## Threading primitives

Locks: https://docs.python.org/3/library/threading.html#lock-objects. Can be used as context managers.

```python
class Foo:
  def __init__(self):
    self._lock = Lock()

  def bar(self):
    with self._lock:
      # guarded section, only one thread at a time.
```

# 2021-02-04

Sentinels: Use object() instead of None. Use `typing.cast` if you need to pretend it's a specific type.

- Pickling uses multiple hooks, deque defines [`__reduce__()`](https://docs.python.org/3/library/pickle.html#object.__reduce__).

  Specifically, deques make use of the optional 4th return value, *Optionally, an iterator
  (and not a sequence) yielding successive items.*

- Low-level pickle understanding: [`pickletools`](https://docs.python.org/3/library/pickletools.html)
- Other low-level mechanisms involved: the [`copyreg` module](https://docs.python.org/3/library/copyreg.html)
- Enforcing type hints at runtime: Recommendations by [Real Python](https://realpython.com/python-type-checking/#using-types-at-runtime)

Inspecting a pickle dump for dependencies:
https://stackoverflow.com/questions/64850179/inspecting-a-pickle-dump-for-dependencies/64850705#64850705

Compare buffer stats and accumulate: https://docs.python.org/3/library/itertools.html#itertools.accumulate



# 2020-12-17

## Timeout on code execution:

* https://stackoverflow.com/questions/492519/timeout-on-a-function-call
  (https://pypi.org/project/func-timeout/, untried)

## Python and functional programming

The advice from the core team on how to do functional programming in Python:

* https://docs.python.org/3/howto/functional.html



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
