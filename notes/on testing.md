

# Main ideas

- Testing is probabilistic
  - 100% goal is a bad use of resources
  - Defined and measure what's important
  - Cost/benefit can be measured with mathematical expectation
- Code is interrelational: Use to our advantage
- Unit tests
  - What's the unit? "_The smallest piece of code that can be logically isolated in a system_".
  - What effect do unit tests and functional granularity (many small functions) have on each other?
  - Measure unit test value according to effect on user story tests

![image](https://user-images.githubusercontent.com/1906276/118561127-6f0e2800-b71f-11eb-876f-525d6b6cf3e3.png)

# Unit tests

In short: Don't be dogmatic about unit tests; be smart instead. Consider the cost-benefit. 

A unit is: "_The smallest piece of code that can be logically isolated in a system_", which in most languages means the function, method, property, etc.

Note that this definition is not tied into the behavior of the code, but it's structure. 

From an effort point of view, these goals are contrary
- more unit (test) coverage 
- small units (Unvle Bob ("Clean Code") _The first rule of functions is that they should be small. The second rule of functions is that they should be smaller than that._)

Devil's Advocate; perhaps a full coverage policy/goal might oblige people to write testible units, therefore better ones (ones with better separation of concerns, etc.)

Effort is not uniform: Some tests are easier to write than others. 


## Unit tests are great

[The importance of unit tests](https://fortegrp.com/the-importance-of-unit-testing/)
[The three rules of TDD](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd)
[Unit testing guide](https://www.guru99.com/unit-testing-guide.html)

![image](https://user-images.githubusercontent.com/1906276/118562928-7f73d200-b722-11eb-83eb-b1c0514e698b.png)


## But also, unit tests are...

![image](https://user-images.githubusercontent.com/1906276/118562417-80f0ca80-b721-11eb-9a08-878b87a5d174.png)
