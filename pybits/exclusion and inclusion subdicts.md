# Problem: Get a subdict

You want to extract part of a dict by specifying field you want (inclusion) or don't want (exclusion) from a source dict (or mapping)

# Solution: Use dict.keys() with set operators

If you search this problem, you'll probably most of the time see the suggestion to use dict comprehension. 

But as it so happens, there's a faster solution (if that matters to you). At least in general, and at least in python 3.8.

```python
# with keys() and set operations

def inclusive_subdict(d, include):
    return {k: d[k] for k in d.keys() & include}

def exclusive_subdict(d, exclude):
    return {k: d[k] for k in d.keys() - exclude}

# with dict comprehension

def inclusive_subdict_2(d, include):
    return {k: d[k] for k in d if k in include}

def exclusive_subdict_2(d, exclude):
    return {k: d[k] for k in d if k not in exclude}
```


![image](https://user-images.githubusercontent.com/1906276/112191970-c383a400-8bc3-11eb-930e-ee17b45291cf.png)


## The code:

Test with a small dict.

```python
d = dict.fromkeys(range(7))

assert inclusive_subdict_2(d, [1, 2, 'not_even_an_int']) == inclusive_subdict_2(d, [1, 2, 'not_even_an_int']) == {1: None, 2: None}
assert exclusive_subdict(d, [1,2,3,4,5]) == exclusive_subdict_2(d, [1,2,3,4,5]) == {0: None, 6: None}
```

```python
%timeit t = inclusive_subdict(d, [1,2,3,4,5])

%timeit t = inclusive_subdict_2(d, [1,2,3,4,5])

%timeit t = exclusive_subdict(d, [1,2,3,4,5])

%timeit t = exclusive_subdict_2(d, [1,2,3,4,5])
```


Test with a bigger dict

```python
d = dict.fromkeys(range(2000))
special_keys = list(range(1800, 2200))

%timeit t = inclusive_subdict(d, special_keys)

%timeit t = inclusive_subdict_2(d, special_keys)

%timeit t = exclusive_subdict(d, special_keys)

%timeit t = exclusive_subdict_2(d, special_keys)
```


But, note that the difference is less extreme if your exclusion "list" has been converted to a set prior to running the function

```python
special_keys = set(range(1800, 2200))

%timeit t = inclusive_subdict(d, special_keys)

%timeit t = inclusive_subdict_2(d, special_keys)

%timeit t = exclusive_subdict(d, special_keys)

%timeit t = exclusive_subdict_2(d, special_keys)
```
