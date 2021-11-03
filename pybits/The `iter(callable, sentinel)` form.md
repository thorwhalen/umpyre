# The `iter(callable, sentinel)` form.

More about this in [python docs](https://docs.python.org/3/library/functions.html#iter) 
and [this useful blog post](https://amir.rachum.com/blog/2013/11/10/python-tips-iterate-with-a-sentinel-value/)

We all know `iter(iterable)` to get an iterator (i.e. has a next) from an iterable (i.e. you can loop on it). 

But we (I at least) often forget the `iter(callable, sentinel)` form. 
For reason, it's a strange interface choice: If you mention the second argument (sentinel), 
your first argument is now expected to be a different type; no longer an iterable, but a callable!! (??!!?)

The idea of the sentinel is to stop "iterating" (read "calling that callable") as soon as it encounters that sentinel value.

But this doesn't work (raises `TypeError: iter(v, w): v must be callable`):

```python
list(iter([1, 2, 3, None, 4], None))
```

Instead, you need to transform your `[1, 2, 3, None, 4]` into a callable returning successive 
values of the iterable. In python, that is `functools. partial(next, iter([1,2,3, None, 4])`. 
So:

```python
from functools import partial
list(iter(partial(next, iter([1, 2, 3, None, 4])), None))
```

They (the python gods) could have made `iter` form be `iter(iterable, callable_sentinel)`, but I guess 
they figured that this is equivalent to `iter(filter(callable_sentinel, iterable))`?
I guess?

Anyway, this code might be useful for creeking:

```python
from functools import partial

no_sentinel = object()

def iterable_to_reader(iterable, sentinel=no_sentinel):
    """Makes an argument-less function that will give you the next iterm of an iterable when called"""
    if sentinel is no_sentinel:
        return partial(next, iter(iterable))
    else:
        return partial(next, iter(iterable), sentinel)
    
def finite_list(iterable, max_items=5):
    from itertools import islice
    return list(islice(iterable, max_items))

read = iterable_to_reader([1, 2, 3])
assert read() == 1
assert read() == 2
assert read() == 3
# Calling walker() again would raise StopIteration

# Use of iter(callable, sentinel)

# Here we'll ask that the reader not raise a StopIteration, but yield 'no_more_items' when there's no more data.

# If your reader uses the 'no_more_items' sentinel too, you'll get only the data
read = iterable_to_reader([1, 2, 3], sentinel='no_more_items')
assert finite_list(iter(read, 'no_more_items')) == [1, 2, 3]

# If your reader uses a different sentinel too, you'll get what ever that reader is giving you...
read = iterable_to_reader([1, 2, 3], sentinel='my_sentinel')
assert finite_list(iter(read, 'no_more_items')) == [1, 2, 3, 'my_sentinel', 'my_sentinel']
```
