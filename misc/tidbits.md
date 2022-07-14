
## Observation: Attribute names don't have to be valid python identifiers.

You can have attributes that are not valid python identifiers. 
They need to be strings, but surprisingly, they don’t need to be valid identifier 
(as in `str.isidentifier(attribute) == True`). 
But you won’t be able to access these attributes via “dot access”. But you can access them via `getattr` 
(and, well, will probably have to set them with `getattr`!).

Why? Well...
* https://stackoverflow.com/questions/26534634/attributes-which-arent-valid-python-identifiers/44689108#44689108
* And more generally, see this: https://stackoverflow.com/questions/72984800/why-does-unpacking-non-identifier-strings-work-on-a-function-call



In the screenshot below, an example with `pandas`: 
`pandas` dataframes will accept all kinds of things (anything hashable basically) as a key (columns, index…). 
And as long as it doesn’t clash with a dataframe’s “personal” attributes (method names etc.), 
it will add your keys as attributes of the dataframe. 
Even if the attribute is a string with spaces, special characters, etc.

![image](https://user-images.githubusercontent.com/1906276/179066540-a39719a9-30f0-44e3-8668-055725729bde.png)

