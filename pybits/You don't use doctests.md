## Problem: You don't use doctests
## Solution: Use doctests

## Problem: Doctests are fiddly (exceptions, differences in white space, etc.)
## Solution: Read the man page
Okay, I agree, doctests could be a lot lot easier to use.
And I don't read man pages much either. But there are solutions to some of the most annoying things.
Like:
```python
# doctest: +NORMALIZE_WHITESPACE
```
which I mentioned before.
But also, check out [this](https://docs.python.org/2.4/lib/doctest-options.html) and [that](https://docs.python.org/3/library/doctest.html).

A useful sample:

For example, this test passes:
```python
>>> print range(20) #doctest: +NORMALIZE_WHITESPACE
[0,   1,  2,  3,  4,  5,  6,  7,  8,  9,
10,  11, 12, 13, 14, 15, 16, 17, 18, 19]
```
Without the directive it would fail, both because the actual output doesn't have two blanks before the single-digit list elements, and because the actual output is on a single line. This test also passes, and also requires a directive to do so:
```python
>>> print range(20) # doctest:+ELLIPSIS
[0, 1, ..., 18, 19]
```
Multiple directives can be used on a single physical line, separated by commas:
```python
>>> print range(20) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
[0,    1, ...,   18,    19]
```
If multiple directive comments are used for a single example, then they are combined:
```python
>>> print range(20) # doctest: +ELLIPSIS
...                 # doctest: +NORMALIZE_WHITESPACE
[0,    1, ...,   18,    19]
```
As the previous example shows, you can add "..." lines to your example containing only directives. This can be useful when an example is too long for a directive to comfortably fit on the same line:
```python
>>> print range(5) + range(10,20) + range(30,40) + range(50,60)
... # doctest: +ELLIPSIS
[0, ..., 4, 10, ..., 19, 30, ..., 39, 50, ..., 59]
```
You want to assert errors will happen. Use
```python
# doctest: +IGNORE_EXCEPTION_DETAIL
```
and ellipses.
```python
>>> 0/0. # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```
For those of you who are not afraid of the big bad R word (regular expressions), know that in pycharm, you can use them easily:
