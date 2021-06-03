# Problem: When I unpickle my object in at/in a different time/place, I get something different

# Solution: Functions and classes are pickled by (module, name) reference 

Think of pickles as a `object_reference + obj_data` representation. 

Another way to think about it is that the information that the serialization actually encodes is 
`reference_to_constructor`, `arguments_to_constructor`, and unpickling gets you the `constructor` 
(through the reference) and calls `constructor(arguments_to_constructor)` to get the desired instance.

Take the illustration above with a grain of salt. Things happen a bit differently. 
See [this section of the pickle documentation](https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled) 
for details.

An example:

```python
class Foo:
    attr = 'iam'
    
foo = Foo()
foo.bar = 'biturates'

pickle_bytes = pickle.dumps(foo)
unpickled_foo = pickle.loads(pickle_bytes)
assert unpickled_foo.attr == 'iam'
assert unpickled_foo.bar == 'biturates'

# ------- some other place, or time, Foo's attr has changed -------------------------------------

class Foo:
    attr = 'groot'

another_unpickled_foo = pickle.loads(pickle_bytes)
assert another_unpickled_foo.attr == 'groot'  # See? a different value! Because new environment has different class
assert another_unpickled_foo.bar == 'biturates'  # You do get your instance data though.
```

And by the way, if you try to pickle foo again now, you'll get that `PicklingError` (that you've probably seen before):

```python
>>> pickle.dumps(foo)
---------------------------------------------------------------------------
PicklingError                             Traceback (most recent call last)
...
PicklingError: Can't pickle <class '__main__.Foo'>: it's not the same object as __main__.Foo
```

Let's get a fresh instance of (this new) `Foo` now, and pickle again (with no problems this time), using `protocol=0` so we can "read" the pickle bytes...

```python
>>> foo = Foo()
>>> foo.bar = 'biturates'
>>> print(pickle.dumps(foo, protocol=0).decode())
ccopy_reg
_reconstructor
p0
(c__main__
Foo
p1
c__builtin__
object
p2
Ntp3
Rp4
(dp5
Vbar
p6
Vbiturates
p7
sb.
```

What you need to observe here is that you can find the string `"biturates"`  (towards the end), but you cannot find the string `"groot"`.
Why? Because `"biturates"` was **instance data**, but `"groot"` was a **class attribute**, and therefore is not represented explicitly, 
but rather through a reference to the class (through the module `__main__` and name `Foo`, which you'll spot in the beginning of the print out.


