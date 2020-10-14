# Problem: Where do I put user app data

You know the deal. You're writing some program, and you need to persist some stuff. 
You probably put it somewhere in the home folder...

But guess what? There's a standard. And yes, it's in the home folder, but where?

# Solution

See [this QT docs page](https://doc.qt.io/qt-5/qstandardpaths.html) which contains a huge list of standard paths. 
Great work QT: Thanks!

So here's an implementation of this in python
```python
import sys
import pathlib

def get_datadir() -> pathlib.Path:

    """
    Returns a parent directory path
    where persistent application data can be stored.

    # linux: ~/.local/share
    # macOS: ~/Library/Application Support
    # windows: C:/Users/<USER>/AppData/Roaming
    """

    home = pathlib.Path.home()
    platform = sys.platform
    
    if platform.startswith("linux"):
        return str(home / ".local/share")
    elif platform.startswith("darwin"):
        return str(home / "Library/Application Support")
    elif platform.startswith("win"):
        return str(home / "AppData/Roaming")
    else:
        raise ValueError(f"Unrecognized system: {platform}")
```

