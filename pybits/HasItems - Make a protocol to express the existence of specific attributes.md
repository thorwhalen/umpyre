# Problem: You want to make a bunch protocols just to validate the existence of specific attributes

[Python Protocols](https://www.python.org/dev/peps/pep-0544/) are a way to be able to do "behavior typing" (my bad terminology).
Basically, if you want your static analyzer (the swingles in your IDE, or linter validation process...) to check if you're manipulating the expected types, except the types (classes, subclasses, ABCs, abstract classes...) are too restrictive (they are!), you can use Protocols to fill the gap.

Except writing them can sometimes be verbose.

Here's a trick to get some base cases covered...

# Solution: HasAttrs (a little thing I wrote just for you)

I use [class getitem here](https://www.python.org/dev/peps/pep-0560/).

Check out the examples, I think you'll find them useful.

```python
>>> assert isinstance(dict(), HasAttrs["items"])
>>> assert not isinstance(list(), HasAttrs["items"])
>>> assert not isinstance(dict(), HasAttrs["append"])
>>>
>>> SizedAndAppendable = HasAttrs["__len__", "append"]
>>> assert isinstance(list(), SizedAndAppendable)
>>> assert not isinstance(tuple(), SizedAndAppendable)
>>> assert not isinstance(dict(), SizedAndAppendable)
>>>
>>>
>>> class A:
...     prop = 2
...
...     def method(self):
...         pass
...
>>>
>>> a = A()
>>> assert isinstance(a, HasAttrs["method"])
>>> assert isinstance(a, HasAttrs["method", "prop"])
>>> assert not isinstance(a, HasAttrs["method", "prop", "this_attr_does_not_exist"])
```

The code:

```python
class HasAttrs:
    """
    Make a protocol to express the existence of specific attributes.
    """
    def __class_getitem__(self, *attr_names):
        annotations = {attr: Any for attr in attr_names}
        return type('HasAttrs', (Protocol,), {'__annotations__': annotations})

```

