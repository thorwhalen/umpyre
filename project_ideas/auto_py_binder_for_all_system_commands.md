It would work as follows:

```python
import commands
commands.ls(...)
commands.cd(...)
```

Some commands have equivalents in `sys` or `os`, 
but we're talking here about scanning what's in a local computer's system path, 
and providing an as 

The functions would 
- be auto populated by manpages transformed to fit python docs formats
- as much as possible have signatures **useful signatures**.

It might not always be possible to extract enough information from manapges to (or at least not with enough confidence to)
be able to create useful signatures, but we would like to do our best to avoid resorting to a blanket `**kwargs`. 
Ideally, we would like the signature to contain appropriate arg names, defaults, annotations 
(probably only `bool`, `str`, `float`, `int` (or nothing)), and kinds (if there are too many arguments, would want to make 
them keyword-only, and we should probably always include a `**kwargs` at the end to handle cases our parser may not have 
caught.

 

# Resources:

- [blog about manpage parser](https://robertodip.com/blog/memories-writing-parser-man-pages/)
- [About manpage parser](https://github.com/h5bp/lazyweb-requests/issues/114)
- [parse man page to find program option info](https://stackoverflow.com/questions/14151173/how-would-i-parse-through-a-man-page-to-quickly-find-info-about-a-program-option)
- [pypi argparse-manpage](https://pypi.org/project/argparse-manpage/) (to generate troff?)


# Name ideas

- For manpage parsing (if needed): `proff` -- wink to [jroff](https://github.com/roperzh/jroff) (Java Roff), 
which is a wink to [troff](https://www.troff.org/), 
which is the markup that manpages use.

