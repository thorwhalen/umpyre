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

Here, the objective is to use an existing base (`dol.Files`) but add transformers to get a subset of all keys, and 
change the way you get the data (values) and the way the keys present themselves.

* Use `dol.Files` to make a raw "bytes" store
* Use `dol.filt_iter` to get a subset of the files (say, only files with a given extension)
* Use `dol.wrap_kvs` with the `obj_of_data` argument to get a store that gives you python objects (from the raw bytes). For example, dicts (from `.json` files) or lists (from `.wav` files) or pandas data frames (from `.csv` or `.xls` etc.). 
* Use `dol.wrap_kvs` with the `key_of_id` and `id_of_key` arguments (BOTH, and both should be inverse of each other) to get something else than the base "string key" path your base store gives you.


### Make your own base store

Technically, "store" really means `Mapping` (if you do read only) or `MutableMapping` (if you add an delete and setitem). 
As you'll see, all you need to do is define a class that subclasses `dol.KvReader` (for the `Mapping`s) or `dol.KvPersister` (for `MutableMapping`s), specifying a few required methods (`__iter__` and `__getitem__` for `dol.KvReader`, and additionally, `__delitem__` and `__setitem__` to make a mutable mapping version).  

Here are some examples:
* [A (very simple, read only) store to get image objects of emojis]([SimpleFilePersister](https://github.com/i2mint/py2store#a-little-py2store-exercise-a-store-to-get-image-objects-of-emojis))
* [A complete (though simple) file store: SimpleFilePersister](https://github.com/i2mint/py2store#but-how-do-you-change-the-persister). You can try the (working, but more involved) ones like 
[mongodol](https://www.github.com/i2mint/mongodol) and [s3dol](https://www.github.com/i2mint/s3dol)), or simpler (since weren't developed further than the basics -- which may be more appropriate to start with):
* Any of the existing "dol" packages, dealing with various storage systems:
    * [sqldol](https://www.github.com/i2mint/sqldol)
    * [dynamodol](https://www.github.com/i2mint/dynamodol)
    * [redisdol](https://www.github.com/i2mint/redisdol)
    * [aiofiledol](https://www.github.com/i2mint/aiofiledol)
    * [dropboxdol](https://www.github.com/i2mint/dropboxdol)
    * [ftpdol](https://www.github.com/i2mint/ftpdol)
    * [arangodol](https://www.github.com/i2mint/arangodol)
    * [couchdol](https://www.github.com/i2mint/couchdol)
    * [odbcdol](https://www.github.com/i2mint/odbcdol)
    * [pydrivedol](https://www.github.com/i2mint/pydrivedol)
    * [sshdol](https://www.github.com/i2mint/sshdol)


