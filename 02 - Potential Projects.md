
# py2store

- [repository](https://github.com/i2mint/py2store)
- [video presentation](https://www.youtube.com/watch?v=6lx0A6oVM5E)

## Build py2store readers/persisters

By writing your own py2store reader and/or persister, you'll necessarily put a toe in the world of dunders, 
which will enhance your modeling abilities more than you'll realize immediately. 

## Data prep

Let's get some data, and bring it to the footsteps of modeling, building reusable data prep tools on the way.

# slang

https://github.com/thorwhalen/slang

Slang is new, promissing, and quite different approach to sound recognitiion in particular, 
and potentially to signal or time series ML in general.

Learn to use it, and then build components for it. Could be:
- **Chunkers**: (e.g. release chunk on threshold volume, or on impulse)
- **Featurizers**: (go crazy exploring off-the-shelf signal or audio features, or build your own (with ANNs if you want))
- **Quantizers**: Explore space partitioining models: clusering, tree methods, ANNs for space partitioning?
- **Ledgers**: Enter the world of structural machine learning, text mining, and NLP, 
and use it to solve sound recognitiion problems!
- **Accumulators**: And excuse to learn about streaming/incremental algorithms, finiite state machines, topic analysis, etc

# Markov and Bayes

## Hyp (to be rebranded)

https://github.com/thorwhalen/hyp

Tools to get from data to operable count/probability/likelihood tables, and perform bayesian analysis, close to the data.

## (Drug use) trajectory behavioral analysis

https://github.com/thorwhalen/odus

Data and tools that demo (using py2store and hypy) how to build a layer over tabular data that produces, on demand, 
operable perspectives of subsets of variables allowing Markovian and Bayesian analysis to be carried out seamlessly. 


