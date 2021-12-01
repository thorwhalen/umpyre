# Problem: Copy/pasting in python console doesn't work

You copy/paste code in a python console to be able to get some doctests to copy (with the >>> and all). 
But you get SyntaxErrors!!

# Solution(s)

It seems to be a problem that runs deep. 
Here's one of the places that rabbit hole brought me to: https://github.com/Homebrew/homebrew-core/issues/68193

In a nutshell, the python distribution (3.8 at least) uses readline which uses rlwrap which...

The

```
set enable-bracketed-paste off
```

solution I found there, and in many other places didn't do it for me.

What DID work for me was to make sure I didn't have tabs between the end of a function definition and the rest of the code!

So copying this:

```
def foo():
    return 1
<include_tab_here>
foo()
```

to the python console will lead to

```python
>>> def foo():
...     return 1
...
... foo()
  File "<input>", line 5
    foo()
    ^
SyntaxError: invalid syntax
```

Remove the tab, and all goes well.
