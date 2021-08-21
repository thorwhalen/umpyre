

# Decorator to handle the item -> iterable of items case and generalizations

*Use Case*: Want to handle an iterable of items, but want to allow the user to specify a single item (because it's a frequent case). 

*Example*: 

```python
def greet_people(names, greeting='Hello'):
    if isinstance(names, str):
        names = (names,)
    for name in names:
        print(f"{greeting} {name}!")
```

Would be nice to be able to write something like:

```python
@ensure_iterable_args(names=str)  # meaning the names argument should be wrapped in tuple if an instance of str
def greet_people(names, greeting='Hello'):
    for name in names:
        print(f"{greeting} {name}!")
```

This is especially useful if you have several functions with several arguments that need this treatment.

