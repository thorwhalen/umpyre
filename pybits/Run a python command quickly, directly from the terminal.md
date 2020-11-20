# Problem: Run a python command quickly, directly from the terminal

This happens to me regularly when, for example, I want to know where a given module lives,
or what version my environment is actually using (not what I INFER it's using from my pip freeze).

# Solution: `python -c "..."`

Example that solves the "where does this module live" problem for omodel package/module:

```
python -c "import omodel; print(omodel)"
```
