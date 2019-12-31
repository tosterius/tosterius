---
layout: note
title: Decision Trees
category: ML
index: 3
headline:
picture:
---

There are two types of decision trees:

- **Classification tree** solves classification problems. Predicted outcome is the category of the object it belongs to
- **Regression tree** solves regression problems. Predicted outcome is real number

#### Decision tree building
Decision tree algorithms transforms raw data to rule based decision tree.
The decision of making data splits heavily affects a tree's accuracy. There are several algorithms to decide how to split a node in
two or more subnodes. Splitting criteria (metric) is different for classification and regression trees.

###### Information Gain (based on Entropy)
**Shannon's entropy** is defined as:
\\[
\begin{equation}
S = -\sum_{i}^C p_i log_2(p_i),
\end{equation}
\\]
where $$C$$ is the number of classes, $$p_i$$ is the probability to pick an element of class $$i$$.
It can be interpreted as measure of uncertainty or randomness in data.

**Information gain** is the reduction in entropy (or another impurity criteria) of the system :
\\[
\begin{equation}
IG = S_0 - \sum_{g=1}^{g=Groups} \frac{N_g}{N}S_g
\end{equation}
\\]

For example, consider a coin toss: the probability to get a head is 0.5 and it is equal to the probability to get a tail.
It means the uncertainty takes its maximum value 1, since there is no chance to precisely determine the outcome.

Another toy example. Circles color in dependence on their coordinates:
![decision_tree_0]({{ site.baseurl }}/assets/img/notes/decision_tree_explanation_0.png)
There are 17 circles: 9 red and 8 green.
The entropy of inital state is equal to

\\[
\begin{equation}
S_0 = - \frac{9}{17}log_2\frac{9}{17} - \frac{8}{17}log_2\frac{8}{17} = 0.9975025463691153
\end{equation}
\\]

Let us split our circles into two groups as folows:
![decision_tree_1]({{ site.baseurl }}/assets/img/notes/decision_tree_explanation_1.png)
The entropy of these two groups:
\\[
\begin{equation}
S_l = - \frac{3}{10}log_2\frac{3}{10} - \frac{7}{10}log_2\frac{7}{10} = 0.8812908992306927
\end{equation}
\\]
\\[
\begin{equation}
S_r = - \frac{6}{7}log_2\frac{6}{7} - \frac{1}{7}log_2\frac{1}{7} = 0.5916727785823275
\end{equation}
\\]
The entropy value has decreased in both groups. It means our strategy of splitting results in
two more ordered groups.
Information gain:
\\[
\begin{equation}
IG = S_0- \frac{10}{17}S_l - \frac{7}{17}S_r = 0.23546616740539644.
\end{equation}
\\]
We can continue to split the dataset into groups in the way in which we are until
the circles in each group are all of the same color.

Usially we deal with multicategorial data represented as table(s). In each step ID3 algorithm
choses the attribute with the largest information gain as the decision node.


###### Gini index (or Gini impurity)

Another splitting criteria is based on Gini Index. It is used in the CART algorithm.
Gini index is a measure of particular element being wrongly classified when it is randomly chosen.
\\[
\begin{equation}
G = 1 - \sum^{C}_{i=1}p_i
\end{equation}
\\]
where $$p_i$$ is the probability of object being classified to a particular class.
It is easy to see that $$G=0$$ if all observations belong to the same class (label).
Gini Index and Entropy can be used interchangeably.

Gini based splitting favors larger partitions. Entropy  that have small counts but many distinct values.

###### How to work with different types of features

__Numeric feature type__:
- sort elements by feature value
- calculate the average feature value for all adjacent elements
- calculate splitting criteria value for each average feature values
- choose the best splitting criteria value

__Categorical data, ranked data__:
- calculate splitting criteria for each  feature value
- choose the best splitting criteria value


<br>
#### Links

- [Implementing Decision Tree From Scratch in Python](https://medium.com/@penggongting/implementing-decision-tree-from-scratch-in-python-c732e7c69aea)

- [Decision Tree Flavors: Gini Index and Information Gain](http://www.learnbymarketing.com/481/decision-tree-flavors-gini-info-gain/)