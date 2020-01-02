---
layout: note
title: Decision Trees
category: ML
index: 3
headline:
picture:
---

There are two types of decision trees:

- **Classification tree** solves classification problems. Predicted outcome is the category of the object it belongs to.
  In a classification tree each leaf has discrete category.
- **Regression tree** solves regression problems. Predicted outcome is real number.
  In a regression tree each leaf represents a numeric value. 

<br>
### 1. Decision tree building. Classification tree.
<br>
Decision tree algorithms transforms raw data to rule based decision tree.
The decision of making data splits heavily affects a tree's accuracy. There are several algorithms to decide how to split a node in
two or more subnodes. Splitting criteria (metric) is different for classification and regression trees.

##### Information Gain (based on Entropy)
<br>
*Shannon's entropy* is defined as:
\\[
\begin{equation}
S = -\sum_{i}^C p_i log_2(p_i),
\end{equation}
\\]
where $$C$$ is the number of classes, $$p_i$$ is the probability to pick an element of class $$i$$.
It can be interpreted as measure of uncertainty or randomness in data.


*Information gain* is the reduction in entropy (or another impurity criteria) of the system :
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

<br>
##### Gini index (or Gini impurity)

Another splitting criteria is based on Gini Index. It is used in the CART algorithm.
Gini index is a measure of particular element being wrongly classified when it is randomly chosen.
\\[
\begin{equation}
G = 1 - \sum^{C}_{i=1}p_i^2
\end{equation}
\\]
where $$p_i$$ is the probability of object being classified to a particular class.
It is easy to see that $$G=0$$ if all observations belong to the same class (label).
Gini Index and Entropy can be used interchangeably.

Gini based splitting favors larger partitions. Entropy  that have small counts but many distinct values.

<br>

##### How to work with different types of features
__Common notes__:
- if chosen splitting feature does not give us a reduction in impurity score, we do not use
  this feature
- to handle with overfitting we could have used a threshold such that impurity reduction has to be large enough
  
__Numeric feature type__:
- sort elements by feature value
- calculate the average feature value for all adjacent elements
- calculate splitting criteria value for each average feature values
- choose the best splitting criteria value

__Categorical data, ranked data__:
- calculate splitting criteria for each  feature value
- choose the best splitting criteria value

### 2. Regression tree.

Let us consider, as an example how the amount of fertilizers influence growth rate of vegetables.
![decision_tree_3]({{ site.baseurl }}/assets/img/notes/decision_tree_explanation_3.png)

Consider very simple decision tree that splits our measurements into two groups based on
whether or not $$x < 1.5$$. The average growth rate on the left is $$2$$. The average growth rate on the right side is $$6$$.
These two values are the predictions that our decision tree will make.

To quantify the quality of these predictions we will calculate the sum of squared residuals
(differences between the observed and the predicted values).

On the next picture we can see that our new decision bound results in a smaller sum of squared residuals.

![decision_tree_4]({{ site.baseurl }}/assets/img/notes/decision_tree_explanation_4.png)

We continue moving our decision boundary
until we have calculated the sum of squared residuals for all remaining thresholds. And then threshold resulting
in smallest sum of squared residuals is used as the root of our tree:
\\[
\begin{equation}
\sum (y_i - F(x_i))^2 \rightarrow min
\end{equation}
\\]

Model's prediction is:

\\[
\begin{equation}
F(x) = \sum_{m-1}^{M}c_m I(x \in R_m)
\end{equation}
\\]

where $$c_m$$ is the response in $$m$$-th region. $$I$$ indicates that $$x$$ belongs to the region $$R_m$$.

To build regression tree we recursively apply the same procedure for observations that ended up in the node to the left and right of the root.


<!-- In other words algorithm decides on the splitting variables and split points. So if we have
 a partition in $$M$$ regions $$R_1, R_2, \dots, R_M$$  -->

#### How to prevent overfitting. Prunining regression trees.

- do splitting only if number of observations more than some minimum number
- pruning

##### Cost complexity pruning
We can prune a tree by removing some of the leaves and replacing the parent node with a leaf that is the average of removed nodes.
We define _cost complexity)_ criteria or _tree score_:

\\[
\begin{equation}
C(T) = SSR + \alpha |T|
\end{equation}
\\]
where $$SSR$$ is the sum of squared residuals, $$\alpha >= 0$$ - tunning parameter (we
find it using cross-validation).
$$|T|$$ - the number of terminal nodes or leaves in tree $$T$$.

The idea is to find, for each $$\alpha$$ a subtree to minimize $$C(T)$$.

To do that do the following steps:

1. build the full sized regression tree by fitting it on all of the data (not just the training data).
   (increase $$\alpha$$ until pruning leaves will give us a lower _tree score_ and use the resulting subtree) $$\times N$$.
   In the end different values of $$\alpha$$ give us a sequence of trees, from full sized to just a leaf
2. split data into training and validation data sets. Just using the training data use the $$\alpha$$ values we found before to build a full
   tree and a sequence of sub-trees that minimize the _tree score_. Use the validation data to calculate the $$SSR$$s for each new tree. 
   10-fold cross-validation. The __final__ value of $$\alpha$$, on average, gives us the lowest $$SSR$$ with the validation data.
3. go back to the trees from 1 and pick the tree that corresponds to the final value from 2

<br>
#### Links

- [Implementing Decision Tree From Scratch in Python](https://medium.com/@penggongting/implementing-decision-tree-from-scratch-in-python-c732e7c69aea)

- [Decision Tree Flavors: Gini Index and Information Gain](http://www.learnbymarketing.com/481/decision-tree-flavors-gini-info-gain/)