
We have a stream/sequence of values and we'd like to get a stream/sequence of window statistics of these numbers. 
Typical examples is "moving average", which boils down to a moving sum if we assume (we do!) the window is of fixed size.

We'll look at two possibilities here: 
- `Specialized`: Update some internal stats. In the case of moving sum, we need to add the new value and subtract the old one (the value going out of the window's range). 
- `General`: Just carry out the full sum every time.


Obviously, the first `Specialized` solution is bound to be more efficient (for large enough window size at least). 
I mean, it's basically 2 sums versus an unbounded number of sums (proportional to window size).

But the second "General" one has huge advantages that are not to be ignored. 
The main one being that it is, well, general. 
But it's also simpler. 
And if you have to reuse the pattern you'll notice all those architectural goodies such as separation of concerns, open-closed principle, DRY, etc.

Indeed, you'll need a different `Specialized` logic every time you want a different kind of statistic. 
For means, it's what we said, but for variance you'll need to accumulate both the sum and the sum of the squares of the values. If you're wondering how that last one works, then I've made my point. 

But just to make sure the point comes across: Not only you have to find or come up with a streaming version of your statistics, but you don't even know if it's possible!

Then again, your specialized version will be (at least in potential, with some effort) more efficient (in time and often space too). 
But **how much** more efficient? Is it really worth the complexity and inflexibility price we need to pay?

That's what we want to investigate here, using the moving sum as a proxy (or proof by one example).

The answer is: No, specialization isn't worth it a priori.

```python
from collections import deque

class SpecializedSum:
    def __init__(self, maxlen, minlen=1):
        self.maxlen = maxlen
        self.minlen = minlen
        self.fifo = deque(maxlen=maxlen)
        self.cumul = 0
        
    def __call__(self, new_val):
        if len(self.fifo) >= self.minlen:
            old_val = self.fifo[0]  # remember the old_val (it will disappear the next step)
            self.fifo.append(new_val)  # append the new value
            self.cumul += new_val - old_val  # add new_val and subtract old val
            return self.cumul
        else:
            self.fifo.append(new_val)  # just append the new value
            return 0

    
    
class GeneralWindowStats(deque):
    def __init__(self, maxlen, func=sum, minlen=1):
        super().__init__(maxlen=maxlen)
        self.func = func
        self.minlen = minlen

        
    def __call__(self, new_val):
        self.append(new_val)  # append the new value
        if len(self) >= self.minlen:
            return self.func(self)
```

Let's have a look at the respective performance of these two choices.

```python

from functools import partial
from lag import time_arg_combinations


def func(maxlen=3, stream_size=10, windower_cls=GeneralWindowStats, repetitions=1):
    windower = windower_cls(maxlen)
    for i in range(repetitions):
        results = list(map(windower, range(stream_size)))
    return results


def gen(funcs=(SpecializedSum, GeneralWindowStats), 
        args_base=([2048], 
                   [2048, 2048 * 5, 2048 * 10, 2048 * 20, 2048 * 50, 2048 * 100]),
        return_func_args=True, include_func_output=False):
    for windower_cls in (SpecializedSum, GeneralWindowStats):
        f = partial(func, windower_cls=GeneralWindowStats)
        result = time_arg_combinations(f, args_base,
                                       return_func_args=return_func_args, include_func_output=include_func_output)
        yield windower_cls.__name__, result


t = dict(gen())

df = pd.DataFrame({k: v[0] for k, v in t.items()})
df['stream_size'] = [list(zip(*v[1]))[1] for v in t.values()][0]
df = df.set_index('stream_size')
df.plot(style='-o', figsize=(16, 5), grid=True);

```


![image](https://user-images.githubusercontent.com/1906276/100796093-fddaf280-33d4-11eb-842b-d50403146a43.png)


