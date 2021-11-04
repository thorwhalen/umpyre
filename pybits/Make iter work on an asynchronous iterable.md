# Problem: Make iter "work" on an asynchronous iterable

When you use iter, you loose your asynchornicity!

# Solution: Use aiter (new in python 3.10!)

So if you're reading this from 3.10, just: 
https://docs.python.org/3/library/functions.html#aiter.

If not (meanwhile)...

I've hacked my why through with my own iterator (using while loop, next, and sentinel).
I then found the ecosystem of stackoverflow, BPO and PEP "complaints". 

Here's two good ones:

```python
from collections.abc import AsyncIterable, AsyncIterator


_NOT_PROVIDED = object()  # sentinel object to detect when a kwarg was not given


def aiter(obj, sentinel=_NOT_PROVIDED):
    """aiter(async_iterable) -> async_iterator
    aiter(async_callable, sentinel) -> async_iterator
    Like the iter() builtin but for async iterables and callables.
    """
    if sentinel is _NOT_PROVIDED:
        if not isinstance(obj, AsyncIterable):
            raise TypeError(f'aiter expected an AsyncIterable, got {type(obj)}')
        if isinstance(obj, AsyncIterator):
            return obj
        return (i async for i in obj)

    if not callable(obj):
        raise TypeError(f'aiter expected an async callable, got {type(obj)}')

    async def ait():
        while True:
            value = await obj()
            if value == sentinel:
                break
            yield value

    return ait()
```

and 

```python
# assuming you have a queue: asyncio.Queue...
while (val := await queue.get()) is not None:
    queue.task_done()
    print(val)
```

Note: it is mentioned in a few place that the two-argument sentinel use cases are often better replaced by this "while walrus" pattern. 

## References

* https://www.python.org/dev/peps/pep-0492/#asynchronous-iterators-and-async-for
* https://www.python.org/dev/peps/pep-0525/
* https://bugs.python.org/issue31861
* https://stackoverflow.com/questions/56377402/why-is-asyncio-queue-await-get-blocking
