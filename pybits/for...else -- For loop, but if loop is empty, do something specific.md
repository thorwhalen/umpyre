# Problem: For loop, but if loop is empty, do something specific

You know sometimes you want to go through some stuff and do things.
But if that stuff is empty, you want to do something else.

If stuff has a length you might say if `len(stuff) == 0: ...` or in most cases just `if not stuff: ...` .

But what if stuff doesn't have a length? What if it's an iterator, like a DB cursor or such.

You might also use a flag:

```python
did_something = False
for x in stuff:
    do_something(s)
    did_something = True
if not did_something:
    do_something_else()
```

Well... there's more elegant than that.

# Solution: `for..else`

Yes, if is not the only one with an else.

for has one too.

And this is what it was made for! That same flag code above can be performed like this:

```python
for x in stuff:
    do_something(s)
else:
    do_something_else()
```

Less code; less bugs.
