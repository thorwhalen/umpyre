# Problem: Function to read data from files

# Solution

Of course there's many ways, but I want to mention this one for it's elegance.

```python
from pathlib import Path
from operator import methodcaller
from i2 import Pipe

read_text = Pipe(Path, methodcaller('read_text'))
read_bytes = Pipe(Path, methodcaller('read_bytes'))
```
