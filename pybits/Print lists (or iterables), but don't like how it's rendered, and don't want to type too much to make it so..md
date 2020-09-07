3# Problem: Print lists (or iterables), but don't like how it's rendered, and don't want to type too much to make it so.

## Solution: Know your print function better (and string formatting, which can go a long way)

The examples talk for themselves...

```python
>>> this = ['is', 'something', 'I', 'wish', 'I', 'knew', 'earlier']
>>> print(this)
['is', 'something', 'I', 'wish', 'I', 'knew', 'earlier']
>>>
>>> print(*this)
is something I wish I knew earlier

>>> print(*this, sep='\n')
is
something
I
wish
I
knew
earlier

>>> for x in this:
...     print(x)
...
is
something
I
wish
I
knew
earlier

>>> for x in this:
...     print(x, end=', ')
is, something, I, wish, I, knew, earlier, 

>>> for x in this:
...     print(x, end='')
issomethingIwishIknewearlier
```
```python
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```
