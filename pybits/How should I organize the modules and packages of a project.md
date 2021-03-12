# Problem: How should I organize the modules and packages of a project?

# Solution

I've been asked this a few times -- and of course there are many ways that makes sense. 
I'd be good though if we can come up with some basic protocols that we can try keeping consistent between us.
This post is really an invitation to consider a seed proposal, and discuss the pros/cons of this, and other protocols you may have found useful yourself, or that some python blogger has...

![image](https://user-images.githubusercontent.com/1906276/110873655-0fab1c00-8287-11eb-8107-30ad136133e5.png)

## `__init__.py`
You import here any objects you deem should be the main interface/functionality of the project/package.
Avoid doing any `from project_root import blah` imports though in other modules, since this could create some entanglements.
Python deals with circular references well in general -- but they still happen.

## `constants.py`
Module to centralize constants used throughout project.
This includes enums, aliases, defaults, types, etc.
This module shouldn't import anything else from the project

## `util.py`
Module containing objects that are useful throughout the project. 
Can import from constants, but no other modules of the project.
If there's many util modules that need to have their separate files, use a package (folder) named utils (plural -- note that 'util.py' is singular).

## `base.py`
Base objects that are usually extended in other modules.
Can import from constants and utils but no other modules.

## etc.

And then there's the rest... tests/ folder for tests, tools.py module that contain util functions that USE (not "ARE USED") the projects objects, etc.


# Appendix

Diagram created by doing this:

```python
from ut import dgdisp

dgdisp("""
constants -> util
constants, util -> base
[constants], [util], [base] -> [other_modules]
constants [label="constants.py"]
util [label="util.py"]
base [label="base.py"]
other_modules [label="other_modules..."]

utils [label="utils/" shape="folder"]
tests [label="tests/" shape="folder"]
""")
```
