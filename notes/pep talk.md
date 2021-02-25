
# PEP 637 -- Support for indexing with keyword arguments

https://www.python.org/dev/peps/pep-0637/

This is going to make py2store an even better place. It’s a limitation of indexing that really annoyed me, 
which has had a PEP for awhile (opened in 2014 rejected in 2019, revived in 2020 because... 
it just makes sense in data science (amongst others)).


Right now, if you want to use multi-dimensional indexing/querying with `[...]` (to talk to parametrized files, or sql tables, 
or mongo collections), you can do it as `store['this', 2:8,...]` . This is fine when there's a "linear/rectangular" fixed schema. 
But if you want to be explicit about the dimensions, or you want/need flexible dimensionality (as in mongo), the dict is the current hack (as in `store[dict(kind='this', time=slice(2,8),...)]` which looks scary and ugly. 
With 637, we'll be able to write that as `store[kind='this', time=2:8]`, as naturally as a function call. 

(Actually, even more conveniently than a function, since slicing with : will be supported. 
A function call would look like this: `store.get_data(kind='this', time=slice(2,8))` ).
