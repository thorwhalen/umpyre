## Subject: Performance comparison: bool, None, callable, isinstance...

Say you have an optional callable parameter `f` in a class (assuming you'll be using instances of it often so that init overhead is negligible wrt use).

Should you check for "callability" in the init, replacing with a transparent function? 
And if you check at usage time, should you check if `f`,  if `f is not None`, if `callable(f)` or `isinstance(f, Callable)`?

Personally, from a readability point of view, I prefer the transparent function. 

Below is what the performance point of view says.

Take aways:
- `isinstance(f, Callable)` has a significant overhead over `callable(f)`
- `if f` wins slightly (and surprisingly) over `if is not None` -- though the latter is more precise.

![image](https://user-images.githubusercontent.com/1906276/139739091-ced6d8ef-7f0d-4b1b-a87a-246813c749c9.png)
