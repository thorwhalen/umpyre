# Pros and Cons of DAGs versus code

When and why should I use a DAG versus just writing code. 
By DAG (Direct Acyclic Graph) we really mean any computation component that that manages smaller components in an explicit way, 
contrasting with code that usually needs to be parsed to achieve the same.

For example: 

```python
# just code
def func(x):
    y = foo(x)
    z = bar(x)
    return baz(y, z)

# or even (still code example)
def func(x):
    return baz(foo(x), bar(x))

# using a DAG
func = DAG((foo, bar), baz)
```

Now... of course, what ever pros and cons are to be taken with a grain of salt. 
For one, we didn't carefully define what we mean by DAG and by code, 
but this list should still be useful, to a constructive-attitude reader, to seed some useful reflection.


## Pros

* A DAG is operable. You can do things like
  * Add logging, caching, error handling to sub-components
  * Edit (add, remove, replace components)
* View the components and their connections


