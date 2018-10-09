# Decision Tree Example

A decision tree is a tree where each node represents a feature(attribute), each link(branch) represents a decision(rule) and each leaf represents an outcome(categorical or continues value).

This is a very simple implementation of it, in python, from scratch. Works for all discrete valued variables only.

For example, following is a decision tree to approve or reject loans:
![](https://cdn-images-1.medium.com/max/600/1*2jnsFCe0YmRjb8EvVAo93w.gif)

This example code takes this following table, containing data about whether or not people play in a given weather condition(and we wish to make a decision tree on the same data):

![](https://cdn-images-1.medium.com/max/600/1*Bn3d4Z62sof3K4U1_0pSlQ.jpeg)

Here is what the result looks like:
![](https://cdn-images-1.medium.com/max/800/1*TlTzgt8I_5dUSbMZmRKyqQ.jpeg)

# Future Plan
* Incorporate for continuous variables also, using Kmeans clustering
* Forest Implementation based on the same
# Reference
https://medium.com/deep-math-machine-learning-ai/chapter-4-decision-trees-algorithms-b93975f7a1f1
