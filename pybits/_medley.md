
# `gzip.compress` not deterministic

`gzip.compress` does not always produce a deterministic output. The output of `gzip.compress` can vary because it includes metadata such as timestamps in the compressed data. 
If you compress the same data at different times, the timestamps will be different, which will result in different compressed data.

Consider this:

```python
import gzip
import time
data = b'hello'
compressed_data_1 = gzip.compress(data)
compressed_data_2 = gzip.compress(data)
time.sleep(1)
compressed_data_3 = gzip.compress(data)
assert compressed_data_1 == compressed_data_2
assert compressed_data_1 != compressed_data_3
```

If you need to produce deterministic compressed data, you might need to use a lower-level function that allows you to control the metadata. For example, you can use the `gzip.GzipFile` class to create a gzip file without a timestamp:

```python
import gzip
import io

def deterministic_gzip_compress(data):
    buf = io.BytesIO()
    with gzip.GzipFile(mode='wb', fileobj=buf, mtime=0) as f:
        f.write(data)
    return buf.getvalue()

# Test the function
data = b'hello'
compressed_data = deterministic_gzip_compress(data)
print(compressed_data)
```

In this code, `deterministic_gzip_compress` creates a gzip file with a fixed timestamp (`mtime=0`), which makes the output deterministic. If you compress the same data multiple times with this function, you will get the same compressed data every time.


# negating a function, methodcaller, and not_

```python
from functools import partial
from operator import methodcaller, not_
from lined import Pipe


def negate(func):
    "returns a negated version of the func"
    return Pipe(func, not_)


startswith_caller = partial(methodcaller, 'startswith')
startswith_osdot = startswith_caller('os.')

assert startswith_osdot('os.path')
assert not startswith_osdot('ostentatious')

not_startswith_osdot = negate(startswith_osdot)  # the opposite of startswith_osdot

assert not not_startswith_osdot('os.path')
assert not_startswith_osdot('ostentatious')
```

