# Problem: (re)Chunking a stream of chunks

We know how to chunk a stream/list/iterable of samples of a waveform.
But sometimes (in fact often) this stream comes in the form of chunks themselves. 
For example, we might signal off of the sensors to the tune of 1024 samples, but need to chunk the signal to the tune of 40000 samples. 

# Solution: Use itertools.chain.from_iterable

Your rechunker function that takes the chunker and the stream of chks you need to (re)chunk, could literally be one short line:
yield from chunker(chain.from_iterable(chks))

It's separation of concerns saves us here. We separated chunking and flattening of the input, and can now reuse our chunker. 

If you didn't do that, this could lead you to something like the 180 lines that someone wrote when they were still a junior programmer. 
Great complex code that needs to manage the possible misalignments of chunk sizes, etc.
See that scary list_chunker (now replaced with the itertools.chain trick) 
[here](http://git.otosense.ai/thor/span/-/blob/9444b020d4b049b3fa95dec3254501fe05f6c2fa/chunking/utils/simplified_list_iterator_chunker.py).

Here's some complete code that implements a chunker and rechunker. 
Understanding how it works will increase your python, no doubt:

```python
def simple_chunker(a: Iterable,
                   chk_size: int):
    """Generate fixed sized non-overlapping chunks of an iterable ``a``."""
    return zip(*([iter(a)] * chk_size))


def rechunker(chks: Iterable[Iterable],
              chunker: Union[Callable, int]):
    """Generate fixed sized non-overlapping chunks of an iterable of chunks.
    That is, the rechunker applies a chunker to an unraveled stream of chunks,
    or more generally of iterables since they can be of varied sizes and types.
    """
    if isinstance(chunker, int):  # if chunker is an int, take it to be a the chk_size of a simple_chunker
        chk_size = chunker
        chunker = partial(simple_chunker, chk_size)
    yield from chunker(chain.from_iterable(chks))
```

Examples:

```python
>>> from functools import partial
>>> chunker = partial(simple_chunker, chk_size=3)
>>> list(chunker(range(7)))
[(0, 1, 2), (3, 4, 5)]
```

Note, the type of the chunks is always tuples, but you can easily change that using ``map``.
For example, to change the type to be list:

```
>>> list(map(list, chunker(range(7))))
[[0, 1, 2], [3, 4, 5]]
```

And rechunking:

```
>>> from functools import partial
>>> chunker = partial(simple_chunker, chk_size=3)
>>> chks = [[0], (1, 2, 3), [4, 5], iter((6, 7))]  # iterable of (different types of) iterables
>>> list(rechunker(chks, chunker))
[(0, 1, 2), (3, 4, 5)]
```
