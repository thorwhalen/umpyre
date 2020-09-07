# Problem: Custom module object access
Customize a module's object access (for example to raise deprecation warnings).

# Solution
Simply define a `__getattr__(name: str): -> Any` function and it will take over the `module.name` or `from module import name` , and define a `__dir()__: -> List` function and it will override the normal `dir(module)` call.

This is <https://www.python.org/dev/peps/pep-0562/>

Only since 3.7, but there's a backport here: <https://pypi.org/project/pep562/>
