# Problem: You need a sentinel that is not `None`, and you want it now.

A sentinel. [Wikipedia says](https://en.wikipedia.org/wiki/Sentinel_value): _In computer programming, a sentinel value (also referred to as a flag value, trip value, rogue value, signal value, or dummy data)[1] is a special value in the context of an algorithm which uses its presence as a condition of termination, typically in a loop or recursive algorithm._

The easiest is to use `None` of this, so we use it, and overuse it, and this can lead to problems. 

Believe me, or go get burnt and come back to read this.

But do you really want to spend time setting up a sentinel. Neither do I.

# Solution

You can make it a bit better by naming your `None` sentinels, so at least the code declares it's intent more clearly. 

It improves readability, but you're still using the `None` value. A almost-no-extra-work solution is to use `object()` instead.
This creates a unique empty object that will distinguish different sentinels not only in name, but in value!

Compare:

```python
def foo(arr, x=None):
    if x is None:
        return None
    else:
        return x * arr
   
```

versus

```python
arg_not_specified = object()
no_result = object()

def foo(arr, x=arg_not_specified):
    if x is arg_not_specified:
        return no_result
    else:
        return x * arr
```

Further, if you use type hinting and want to make the linter shutup, you can use `typing.cast`. 

Say for example, that you want to force someone to enter an int, need to specify a default arg (because a previous arg did, and you can't change the order).
Oh, and you also want/need to use type hinting. What you (I) would normally do is:

```python
from typing import Optional

def foo(arr=(), x: Optional[int]=None):
    if x is None:
        raise TypeError("You need to specify an x")
    ...
```

But that `x` isn't really optional right? And we're using None here. If we use `object()` the linter might complain. 
Instead we can do this:

```python
from typing import cast

arg_not_specified = cast(int, object())

def foo(arr=(), x: int=arg_not_specified):
    if x is None:
        raise TypeError("You need to specify an x")
    ...
```



# Appendix

## Defining a bunch of sentinels in one line
If you want to define a bunch of sentinels to be used in a module or package, you can also do it like this:

```python
(a_bunch,  of_sentinels,  that_have_different, roles) = map(lambda x: x(), 4 * [object])
 ```
 
 But you may be accused of being an extremist if you do so.
 
 ## Performance
 
 The following compares using `None`, `object()`, and `type('named_sentinel', (), {})()` as a sentinel. 
 
 Observation: `None` is twice faster to compare to itself. 
 No significant differences to compare "something" (in this case, a variable containing an int) to a sentinel. 
 
 ![image](https://user-images.githubusercontent.com/1906276/140366599-b36eb848-c300-477c-808d-83e15d1c477b.png)

