## Problem: Where are my virtual envs again? How do I activate them

If you’re like me (I hope not), you’re really annoyed by having to do

```bash
source ~/.virtualenvs/ENVNAME/bin/activate
```

to activate your `ENVNAME`.
Or

```bash
ls ~/.virtualenvs/
```

to remember which ones you have.


## Solution

Put this in your .bash_profile or .bashrc or where ever you put your environment variables:

```bash
alias VENV_FOLDER="whereever that is for you"
vact ()
{
    if test "$1" == ""; then
        ls $VENV_FOLDER;
    else
        source $VENV_FOLDER/$1/bin/activate;
    fi
}
```

**Example use:**

```bash
$ vact
382	clean	http	p37	p38	p3test	scrap	tmotors
$
$ vact p3test
(p3test) $ 
``` 
