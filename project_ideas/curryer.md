
```python
from functools import partial, wraps

class Curryer:
    def __init__(self, func):
        self.func = func
        try:
            wraps(func)(self)  # TODO: copy all attrs, or just signature, using functools.update_wrapper?
        except:
            pass

    def __call__(self, *args, **kwargs):
        return partial(self.func, *args, **kwargs)
    
import random
randint_curryer = Curryer(random.randint)

# What you do with it is this (what you do with partial, but with the function fixed)
get_randint = randint_curryer(2, 4)
assert get_randint() in {2, 3, 4}

# But the real point of using Curryer is that the curryer has the same docs and signature as the function 
# that is being curried, so it's easier to choose the arguments you're binding
from inspect import signature
assert signature(randint_curryer) == signature(random.randint)
assert randint_curryer.__doc__ == random.randint.__doc__

import pandas as pd
data_frame_curryer = Curryer(pd.DataFrame)

# What you do with it is this (what you do with partial, but with the function fixed)
df_maker = data_frame_curryer(columns=['earth', 'and', 'fire'])
df_maker([(1, 2, 3), (4, 5, 6)])

# But the real point of using Curryer is to be able to 
from inspect import signature
assert signature(data_frame_curryer) == signature(pd.DataFrame)
assert data_frame_curryer.__doc__ == pd.DataFrame.__doc__
```

