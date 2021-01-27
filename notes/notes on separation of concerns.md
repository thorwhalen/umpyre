
From [Wikipedia article on SOC](https://en.wikipedia.org/wiki/Separation_of_concerns) this:

In computer science, separation of concerns (SoC) is a design principle for separating a computer program into 
distinct sections 
such that each section addresses a separate concern. 
A concern is a 
set of information that affects the code of a computer program. 
A concern can be as general as "the details of the hardware for an application", or as specific as "the name of which class to instantiate". 
A program that embodies SoC well is called a modular[1] program.
Modularity, and hence separation of concerns, is achieved by encapsulating information inside a section of code that has a well-defined interface. 
Encapsulation is a means of information hiding.[2] Layered designs in information systems are another embodiment of separation of concerns (e.g., presentation layer, business logic layer, data access layer, persistence layer).[3]


Separation of concerns is an important design principle in many other areas as well, such as **urban planning, architecture and information design.** 

Common examples include 
- separating a space into rooms, so that activity in one room does not affect people in other rooms (this example shows encapsulation, where information inside one room, such as how messy it is, is not available to the other rooms, except through the interface, which is the door).
- Keeping the stove on one circuit and the lights on another, so that overload by the stove does not turn the lights off (this demonstrates that activity inside one module, which is a circuit with consumers of electricity attached, does not affect activity in a different module, so each module is not concerned with what happens in the other)


The mechanisms for modular or object-oriented programming that are provided by a programming language are mechanisms that allow developers to provide SoC.[4] 
For example, 
- object-oriented programming languages such as C#, C++, Delphi, and Java can separate concerns into objects, and
- architectural design patterns like MVC or MVP can separate content from presentation and the data-processing (model) from content. 
- Service-oriented design can separate concerns into services. 
- Procedural programming languages such as C and Pascal can separate concerns into procedures or functions. 
- Aspect-oriented programming languages can separate concerns into aspects and objects.


The term separation of concerns was probably coined by Edsger W. Dijkstra in his 1974 paper "On the role of scientific thought".[6]

_Let me try to explain to you, what to my taste is characteristic for all intelligent thinking. 
It is, that one is willing to study in depth an aspect of one's subject matter in isolation for the sake of its own consistency, 
all the time knowing that one is occupying oneself only with one of the aspects. 
We know that a program must be correct and we can study it from that viewpoint only; 
we also know that it should be efficient and we can study its efficiency on another day, so to speak. 
In another mood we may ask ourselves whether, and if so: why, the program is desirable. 
But nothing is gained —on the contrary!— by tackling these various aspects simultaneously. 
It is what I sometimes have called "the separation of concerns", which, 
even if **not perfectly possible**, 
is yet the only available technique for effective ordering of one's thoughts, that I know of. 
This is what I mean by "focusing one's attention upon some aspect": 
it does not mean ignoring the other aspects, it is just doing justice to the fact that from this aspect's point of view, the other is irrelevant. 
It is being one- and multiple-track minded simultaneously._


