# Subject: Awesome `functools.partial` recipes

## Command pattern

[Wikipedia says](https://en.wikipedia.org/wiki/Command_pattern) _In object-oriented programming, the command pattern is 
a [behavioral design pattern](https://en.wikipedia.org/wiki/Behavioral_pattern)
in which an object is used to encapsulate all information needed to perform an action or 
trigger an event at a later time_

I've written and used a `Command` class to do this. It's really short and left as an exercise. 
(Hint: two one liner methods only). 

If you did the exercise above you might feel as clever as I did. So now to burst that bubble:

It so happens that by replacing `Command` with `partial` you get exactly the same thing. 

```python
>>> from functools import partial
>>> command = partial(sum, [1, 2, 3])
>>> command()
6
>>> command = partial(print, 'hello', 'world', sep=', ')
>>> command()
hello, world
```

## A source reader

### Problem: You have an iterator, but need to consume it with a function call

Some interfaces ask you to provide a function to iterate through some data. 
Don't blame them, they're right. 
If they only need to iterate through some data, 
it's better to ask you to provide that data as an iterable, iterator, or a function which when called, gives you the next item.

Like a `read()` or `readline()` method of some io source readers.

So how can you get such a reader from an `iterable` or `iterator`?

```python
partial(next, iterator)
# or
partial(next, iter(iterable))
```

Example:

```python
>>> from functools import partial
>>> read = partial(next, iter(range(10)))
>>> read()
0
>>> read()
1
```
