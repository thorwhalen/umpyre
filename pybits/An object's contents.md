*# Problem: An object's contents*
See what attributes one object has, that another doesn't.
This comes up when you want to see what's particular about an object (that not all objects have, or that a superclass doesn't have).

# Solution
```python
>>> attr_diff = lambda o, oo: set(dir(o)) - set(dir(oo))
>>> attr_diff.__doc__ = "Attributes that o has but oo doesn't"
>>>
>>> sdir = lambda o: attr_diff(o, object)
>>> sdir.__doc__ = "Attributes of o, not including those that every object has"
>>>
>>> from collections.abc import Collection, Mapping, MutableMapping
>>> print(sdir(Collection))
{'__len__', '__iter__', '_abc_impl', '__module__', '__slots__', '__abstractmethods__', '__contains__'}
>>> print(attr_diff(Mapping, Collection))
{'__reversed__', 'items', 'values', 'get', 'keys', '__getitem__'}
>>> print(attr_diff(MutableMapping, Mapping))
{'_MutableMapping__marker', 'pop', 'clear', '__setitem__', 'setdefault', '__delitem__', 'popitem', 'update'}
```
--> These are all real problems that I try to solve (*An object's contents)* or find a solution for (*Custom module object access*)
Posting here so both as my own personal notes, and so that it has a chance to be useful to a wider audience.
I encourage you to do the same. If possible, using the Problem/Solution template.
*# Discovery: python ignores spaces in dot paths!!!*
```python
>>> os.   path    .   join
<function posixpath.join(a, *p)>
```
Why is that useful?
When you have an object that that uses a <https://en.wikipedia.org/wiki/Fluent_interface|fluent interface> it can be practical to surround a long chain of transformations with parentheses, and... separate the steps with newlines:

```python
import ffmpeg
(
    ffmpeg
    .input('test_input.mp4')  # which, by the way, also allows you to comment!!
    .hflip()
    .output('test_output.mp4')
    .run()
)
```