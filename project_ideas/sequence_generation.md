# Objective

This package offers tools for generating sequences. Finite ones like lists and arrays, or infinite ones like streams. 

The items of the sequences can be anything and often one sequence produced will be used to produce another (see further design notes). 
The target (i.e. final) sequence items would be samples of a signal (like sound, image, or other data from some sensor source) or typical time-series. 

For starters, our main focus will be generating sound -- that is, servicing the [hum](https://github.com/otosense/hum) package. 

Our main tools will be taken from [creek](https://github.com/i2mint/creek). 

[Project name candidates](#project-name-candidates)



# Design

Our running examples will be taken from audio production. 
We'll use `wf` to denote a waveform object (usually a list or array of numbers -- a.k.a. samples or frames). 

To get a waveform, you specify some `params` (including, say, the kind, 
or the actual function that the params should be called with to produce the result), 
and you get a waveform `wf`.

![image](https://user-images.githubusercontent.com/1906276/129167933-b1cdba31-0e8c-46b9-b789-c89732d06ce3.png)

This `wf` could be a fixed-size object like an array, or could be a source of unbounded amounts of data, 
like a generator, a stream object, a or a `creek.InfiniteSeq` which gives you the array-like ability to slice (i.e. `wf[i:j]`). 


# Appendices

## Project name candidates

```
--- slink ---
0: walk stealthily (slink.v.01)
--- rill ---
0: a small stream (rivulet.n.01)
1: a small channel (as one formed by soil erosion) (rill.n.02)
--- jaunt ---
0: a journey taken for pleasure (excursion.n.01)
1: make a trip for pleasure (travel.v.03)
--- amble ---
0: a leisurely walk (usually in some public place) (amble.n.01)
1: walk leisurely (amble.v.01)

--- burble ---
0: flow in an irregular current with a bubbling noise (ripple.v.02)
--- educe ---
0: deduce (a principle) or construe (a meaning) (educe.v.01)
1: develop or evolve from a latent or potential state (derive.v.04)

--- phase ---
0: any distinct time period in a sequence of events (phase.n.01)
1: (physical chemistry) a distinct state of matter in a system; matter that is identical in chemical composition and physical state and separated from other material by the phase boundary (phase.n.02)
2: a particular point in the time of a cycle; measured from some arbitrary zero and expressed as an angle (phase.n.03)
--- strand ---
0: a pattern forming a unity within a larger structural whole (strand.n.01)
1: line consisting of a complex of fibers or filaments that are twisted together to form a thread or a rope or a cable (strand.n.02)
2: a necklace made by a stringing objects together (chain.n.10)
--- genic ---
0: of or relating to or produced by or being a gene (genic.a.01)
```
