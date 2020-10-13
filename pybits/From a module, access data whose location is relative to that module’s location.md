## Problem: From a module, access data whose location is relative to that module’s location

## Solution: importlib_resources

(importlib_resources)[https://importlib-resources.readthedocs.io/] is in standard lib.

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

```
from importlib_resources import files
# Reads contents with UTF-8 encoding and returns str.
eml = files('email.tests.data').joinpath('message.eml').read_text()
```
