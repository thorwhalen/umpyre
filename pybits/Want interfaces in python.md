


# Problem: Want interfaces in python

That is:
- You come from a language with interfaces (Go, Java,...) and miss them.
- You feel limited by python's typing
- You feel limited (and obliged to subclass)
- You like duck typing, but want it to be static, explicit, verifiable
- You like the looks of [zope.interfaces](https://pypi.org/project/zope.interface/), but want less scary builtin kind

# Solution: `typing.Protocol` (3.8+): Structural subtyping (static duck typing)

[The python docs](https://docs.python.org/3.9/library/typing.html#typing.Protocol)

[A blog post](https://andrewbrookins.com/technology/building-implicit-interfaces-in-python-with-protocol-classes/)

[The PEP](https://www.python.org/dev/peps/pep-0544/)


```python
from typing import Protocol, runtime_checkable, Iterable

@runtime_checkable  # Optional decorator: you still get typing checks without it (see later for what this adds!)
class Fittable(Protocol):
    def fit(self, x: Iterable):
        pass

class SomeClassWithAFitMethod:
    def fit(self):
        pass

class SomeClassWithoutAFit:
    def this_is_not_a_fit(self, x: Iterable):
        pass

def fit_with_data(learner: Fittable, data: int):
    learner.fit(data)  # static analysis (example, linter) will complain since data is not (declared to be) iterable


def learn_stuff(learner: SomeClassWithoutAFit, data: Iterable):
    learner.fit(data)  # static analysis (example, linter) will complain since SomeClassWithoutAFit doesn't have a fit
    
# additional (runtime validation) provided by @runtime_checkable:
assert issubclass(SomeClassWithAFitMethod, Fittable)  # Yet not an ACTUAL subclass -- just satisfies the protocol
instance = SomeClassWithAFitMethod()
assert isinstance(instance, Fittable)  # Yet not an ACTUAL instance  -- just satisfies the protocol

```

See what linter does:

![image](https://user-images.githubusercontent.com/1906276/116764915-9783eb80-a9d7-11eb-8033-459b75d580d9.png)
