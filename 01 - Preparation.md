
This is your first project. A project that is meant for you to get familiar with some resources that we'll be using during
your learning sessions -- and well, that you'll probably use for a good part of your career (until you find newer and better 
ways to acheive the same thing).

This project has a deliverable that is there to give you a goal that will assert the fact that you know how to use the tools.

# The deliverable

A project, published on github, that contains a 
- `README.md` written in markdown, using at least once each of the 
[basic syntax](https://www.markdownguide.org/cheat-sheet/#basic-syntax). 
- A jupyter notebook, with a bit of markdown, and a bit of code
- At least one python module (that the jupyter notebook will import and use)
- One to three kaggle dataset that you've downloaded and kicked around in your github project
- A version of this "01 - Preparation.md" text you're currently reading, allong with enhancements 
such as more detailed instructions once you figured things out, links that where helpful, etc.

# Notes

## Misc
- `.md` is the usual file extension for markdown, and the one that github will spot and create a "preview" 
of rendered markdown for you
- _Call the project `{name}_01_scrap`, where {name} is your last name or pseudo you'll be consistently using._

## Github + Markdown
- Get a github account if you don't have one.
- Make sure you know a minimum on how to use a jupyter notebook. 
- Learn a minimum of markdown
- Spend at least 10-15 minutes reading about git if you don't know what it is.

## Kaggle
- Get a kaggle account if you don't have one and familiarize yourself with their data and competition search.
- Get a kaggle API token.
- Explore datasets or competitions (that come with their datasets) and come up with three that you're interested in exploring

# Extras:

## py2store
Install and poke around [py2store](https://github.com/i2mint/py2store/blob/master/README.md). 
Know that a some of the `README` may be obsolete, but you'll get enough to play with. 
And one of the tasks you'll be able to "give back" is to help me make more documentation and tutorials for py2store -- 
while using it yourself for your data preperation needs. 

You can just `pip install py2store` to get the latest packaged version. Or...

## py2store dev branch
But in the long run, you'll probably want to work directly with the source, on the dev branch, 
so you can always get the latest stuff I'll commit. For this, you'll need to clone directly 
from [https://github.com/i2mint/py2store] in a place that's on your python path and switch to the dev branch. 

I suggest you make a folder where you'll keep your projects, and any other projects that you might be usinig "from the source". 
These could be separate if you prefer. 

Let's assume the full path of this folder is called `$PYPROJ` 
(notation indicates that you've created an 
[environment variable](https://medium.com/chingu/an-introduction-to-environment-variables-and-how-to-use-them-f602f66d15fa)
that contains the actual path string). 

You're steps to use py2store from dev branch could look like this:
1. Make that $PYPROJ project directory
2. Make sure it's on your python path (look it up -- there's many ways to do it)
3. Go to that directory, which in a terminal looks like this:
```
cd $PYPROJ
```
4. Clone py2store from github (if you don't have git, get git!)
```
git clone https://github.com/i2mint/py2store
```
5. Switch to dev branch
```
git checkout dev
```
6. Make sure you're on that dev branch. The following should print out something that should convince you:
```
git branch
```
7. Make sure you have the latest
```
git pull
```
