# Knowing dol

Note that `dol` is the core of what used to be called `py2store`. 


## Poke around the knowledge base

### Watch the py2store presentation (2019)

[py2store presentation at pybay 2019](https://youtu.be/6lx0A6oVM5E)


### Know ALL dict methods well

Look for recipes and advanced uses of `dict`. Examples (off of the top of my google):
* [python dictionaries](https://www.dataquest.io/blog/python-dictionaries/)
* [7 advanced techniques](https://towardsdatascience.com/7-advanced-python-dictionary-techniques-you-should-know-416194d82d2c)
* [advanced dict operations](https://www.python-engineer.com/courses/advancedpython/03-dict/)


### Poke around some py2store and dol docs

* [py2store readme](https://github.com/i2mint/py2store/blob/master/README.md)
* [dol readme](https://github.com/i2mint/dol/blob/master/README.md)
* [dol documentation](https://i2mint.github.io/dol/)


## Do stuff

### Make a local files store

* Use `dol.Files` to make a raw "bytes" store
* Use `dol.filt_iter` to get a subset of the files (say, only files with a given extension)
* Use `dol.wrap_kvs` with the `obj_of_data` argument to get a store that gives you python objects (from the raw bytes). For example, dicts (from `.json` files) or lists (from `.wav` files) or pandas data frames (from `.csv` or `.xls` etc.). 
* Use `dol.wrap_kvs` with the `key_of_id` and `id_of_key` arguments (BOTH, and both should be inverse of each other) to get something else than the base "string key" path your base store gives you.


