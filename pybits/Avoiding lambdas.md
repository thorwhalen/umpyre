# Problem 1: You can't pickle because of lambdas

# Problem 2: You want to use lined, but everything needs to be a function, and you want to avoid Problem 1.

# Solution (elements):

The (builtin) modules [operator](https://docs.python.org/3/library/operator.html) has a lot of elements to use
(`itemgetter`, `methodcaller`, `attrgetter`, and all the "abstract operators" (addition, concatination, identity etc.)
and [functools](https://docs.python.org/3/library/functools.html) tools to use them to your needs 
(e.g. `partial`, `partialmethod`, `cached_property`, `lru_cache`, `wraps`...)

