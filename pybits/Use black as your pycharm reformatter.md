# Problem: Use black as your pycharm reformatter.md

# Solution

In terminal:

`pip install black` (or `axblack` if you are one of those who wants to control the line length).

`which black`, and copy the "Program" path it gives you.

In Pycharm [do this](https://godatadriven.com/blog/partial-python-code-formatting-with-black-pycharm/#:~:text=To%20use%20Black%20in%20PyCharm,%3E%20External%20Tools%20%2D%3E%20Black.)

In my words:

Go to `Preferences>External Tools`, add a new tool, paste that path in "Program", and do something like in the screenshot below:

![image](https://user-images.githubusercontent.com/1906276/119029612-b2ee7080-b95d-11eb-8aff-7f161bc96724.png)

Then, replace your default reformat-shortcut with black:

![image](https://user-images.githubusercontent.com/1906276/119030373-a880a680-b95e-11eb-8f05-91fac777946e.png)

