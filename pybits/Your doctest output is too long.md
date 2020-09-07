## Problem: Your doctest output is too long

## Solution: Use directives
<https://docs.python.org/2/library/doctest.html#directives>

For example

Too long vertically: Use `...`
```python
ValueError                                Traceback (most recent call last)
...
ValueError: This error is expected
```
This allows you to both (1) not to have to display the whole traceback and (2) not have your doctest try to compare system particulars (such as the file paths that show up in the traceback.

Too long horizontally: Use `# doctest: +NORMALIZE_WHITESPACE`:
Without would make you'd have to do this:
```python
>>> s.kinds 
{'w': <_ParameterKind.POSITIONAL_ONLY: 0>, 'x': <_ParameterKind.POSITIONAL_OR_KEYWORD: 1>, 'y': <_ParameterKind.POSITIONAL_OR_KEYWORD: 1>, 'z': <_ParameterKind.KEYWORD_ONLY: 3>}
```
With it, you can do this:
```python
>>> s.kinds  # doctest: +NORMALIZE_WHITESPACE
{'w': <_ParameterKind.POSITIONAL_ONLY: 0>,
'x': <_ParameterKind.POSITIONAL_OR_KEYWORD: 1>,
'y': <_ParameterKind.POSITIONAL_OR_KEYWORD: 1>,
'z': <_ParameterKind.KEYWORD_ONLY: 3>}
```
