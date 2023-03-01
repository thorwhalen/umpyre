## Problem: From a module, access data whose location is relative to that module’s location

## Solution: importlib_resources

[importlib_resources](https://importlib-resources.readthedocs.io/) is in standard lib.

Note that [importlib_resources](https://importlib-resources.readthedocs.io/)
is a backport for a new feature in Python 3.9: 
[importlib.resources](https://docs.python.org/3/library/importlib.html#module-importlib.resources)
   
See example [here](https://importlib-resources.readthedocs.io/en/latest/using.html#example).

I used to (this will end today!) do it this way:

```python
data_dir = os.path.join(os.path.dirname(__file__), 'tests', 'data')
data_path = os.path.join(data_dir, 'message.eml')
with open(data_path, encoding='utf-8') as fp:
    eml = fp.read()
```

That works if you never package things it won’t always work (example, if package comes as a zip).

The better way used to be:

```python
from pkg_resources import resource_string as resource_bytes
eml = resource_bytes('email.tests.data', 'message.eml').decode('utf-8')
```

But now there’s better AND faster:

```python
from importlib_resources import files
# Reads contents with UTF-8 encoding and returns str.
eml = files('email.tests.data').joinpath('message.eml').read_text()
```

## Future proof it

If you're in 3.9, just use builtin `importlib.resource` instead.

If you're in versions lower than 3.9, but want to future proof it to use the builtin when available, 
you can do something like this:
```python
try:
    from importlib.resources import files  # ... and any other things you want to get
except ImportError:
    from importlib_resources import files  # pip install importlib_resources
```


## Example usage

You can put this in a `__init__.py` module (warning -- it won't work in any modules, just "package" ones (that is, named `__init__.py`. 

From this, you get a function that will give you a `PosixPath` to give you access to files relative to the location of that `__init__.py`. 

```python
import sys

try:
    from importlib.resources import files  # ... and any other things you want to get
except ImportError:
    from importlib_resources import files  # pip install importlib_resources

module_path = files(sys.modules[__name__])
ppath = module_path.joinpath

## explanation:
# current_module = sys.modules[__name__]
# module_path = files(current_module)

```

