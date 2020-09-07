## Problem: You work with ipython would like to have tab completion to show you the keys of your store

## Solution: Add a `_ipython_key_completions_` method to your object class (or inject one in your instance) that returns an iterable of all valid keys.

 Note: ipython already adds local path listing automatically, so you'll still get those along with your valid store keys.

See `py2store.trans.add_ipython_key_completions` decorator for an example of how to do it.
Which brings me to...
