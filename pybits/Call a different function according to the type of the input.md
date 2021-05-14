

# Problem: Call a different function according to the type of the input

You know... you ex-javaist and ex-C(NoClueWhatTheDemonymMightBe) know and maybe miss it in python.

# Solution: singledispatch

Another functools goodie.
docs: https://docs.python.org/3/library/functools.html#functools.singledispatch

```python
from functools import singledispatch

@singledispatch
def process(response: str):
    print(f"base {response}")
    
@process.register
def _(response: int):
    print(f"int {response}")
    
@process.register
def _(response: bytes):
    print(f"bytes {response}")
    
@process.register
def _(response: None):
    print(f"None {response}")
```

Try it:

```python
process('hi')
process(42)
process(b'hi')
process(None);
```

Gives you:
```
base hi
int 42
bytes b'hi'
None None
```

Now, annoyingly, it's SINGLE dispatch, so only works on the first argument (the functional programming obsession).
That said for methods, there's [singledispatchmethod](https://docs.python.org/3/library/functools.html#functools.singledispatchmethod).

And if you need multiple dispatch, there's pypi libraries out there. Example: https://pypi.org/project/multipledispatch/
