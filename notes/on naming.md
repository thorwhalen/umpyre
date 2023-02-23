

# On measuring naming clarity

I was reviewing some code and bumped into this:

<img width="627" alt="image" src="https://user-images.githubusercontent.com/1906276/221005986-2731ef6c-de49-44e2-bcce-30169fc994d9.png">

Of course, my first reaction was “what’s `ctor`?!?“. 

But instead of immediately opening a debate about the cost and benefits of introducing a new shorthand, 
to decide if it’s useful enough to welcome it, I asked myself if ctor is a common abbreviation. 

I google/chatGPTed it.

Just the word didn’t bring anything, but “what does ctor mean in python” did bring me straight to the answer. 

This brought me to the thought that perhaps we can (possibly automatically) rank the clarity of a term, especially short hand ones, according to what google/chatGPT responds to the patterns:

```
What does {term} stand for in {domain}?
```

Or

```
What does the abbreviation {abbr} stand for in {domain}?
```

If the domain expertise of current/future readers of our code is clear (is it software development, python, machine learning?) we shouldn’t 
penalize otherwise clear, or a google-away, terminology. 

This strategy will allow us to minimize the short-hands for our specific, internal domain (`chk`, `fv`, etc.) while allowing a bit more leniency 
in using terminology that should be clear to software developers in general, or more specifically python, unix, or machine learning ones. 

Both google and chatGPT clearly respond to the “what does the abbreviation ctor stand for in software development?” request, 
saying that it’s typically used to me “constructor”. 

Essentially, when we say "the code should be readable", we should be clear on who the reader might be, and how much effort we should be putting in 
to expand our readership or tailor the lazy. 



