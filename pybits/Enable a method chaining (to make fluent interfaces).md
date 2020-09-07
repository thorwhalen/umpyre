# Problem: Enable a method chaining (to make fluent interfaces)

# Solution: Have methods return self

You do:
```python
class MyFluentInterface:
    def transform(self, a, b=1, c=0):
        ...
        return self
    def crop(self, bt, tt):
        ...
        return self
```
So you can:
```python
obj = MyFluentInterface()
obj.transform(1).crop(3,4)
```
