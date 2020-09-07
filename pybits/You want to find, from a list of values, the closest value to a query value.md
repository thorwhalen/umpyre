# Problem: You want to find, from a list of values, the closest value to a query value

# Solution: Use builtin `min` with `key` argument
```python
min(search_this, key=lambda x: abs(x - query))
```
Builtins did it again! O the magic of the `key` argument in functions like `min`, `max`, `sort`!

This is a simple 1D (and k=1) version of what is called "k nearest neighbors" (also known as KNN). You could of course extend the above trick to more dimensions, and use builtin `heapq` (<https://docs.python.org/3/library/heapq.html>) if you need `k>1` .

But at some point, especially if you have a big and stable search set, you'll want to use more grownup ML (search for KNN) -- those methods actually index the search set to be able to search it more efficiently.
