# Problem: Make python into a system script.md

I have the `my_script.py` python file, which has a `if __main__ == "__name__":` section that makes it into a convenient script. 

But I have to call the script by doing

```
python .../path_to/my_script.py ... options
```

I'd rather just have a script that my system (shell/terminal) will recognize without my having to say "python ...".

# Solution


Note: [These instructions](https://openbookproject.net/thinkcs/python/english3e/app_c.html#making-a-python-script-executable-and-runnable-from-anywhere)
having to do with adding a "#!/usr/bin/env python3" header didn't work for me. 

What worked for me:

(1) `cd` to where you want your script to live -- needs to be a place that is on the system "path". 
You can find this list by doing this in your terminal:

```
echo $PATH
```

You can also add to this path, of course. But that's different concern.

(2) In that folder, create a file called `my_script` (*):

```
python .../path_to/my_script.py "$@"
```

The name can be anything you want, but nicer to have it be the same name of the python file, minus the extension.

(3) Make the file executable. For example:

```
chmod 
```

See [this post](https://askubuntu.com/questions/229589/how-to-make-a-file-e-g-a-sh-script-executable-so-it-can-be-run-from-a-termi) 
for more about making a file executable.






