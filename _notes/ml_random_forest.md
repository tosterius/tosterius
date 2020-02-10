---
layout: note
title: Random Forests
category: ML
index: 5
headline:
picture:
---

In simple words, Random Forest uses bagging to build a collection of decision trees and then averages them.

Let us denote $B$ as a number of tree we are going to create.
$p$ is the number of features.

__Random Fores algorithm__:

1. For $b = 1$ to $b = B$:
   1. create bootstrapped data set $Z$ from the training data
   2. create decision tree using this new data set by recursively repeating the following steps
   for each terminal node:
   - Randomly select $m$ variables from the $p$ variables
   - Pick the best variable and split point among the $m$
   - Split the node into two child sub-nodes
  
2. output the ensemble of trees $\\{T_1, T_2, \dots, T_B\\}$

Prediction for Regression trees:
\\[
\begin{equation}
f(x) = \frac{1}{B}\sum_{b=1}^{B}T_b(x)
\end{equation}
\\]

Prediction for Classification trees:
\\[
\begin{equation}
c(x) = majority\\_vote(\\{c_b for\;b = 1\; to\; b = B\\})
\end{equation}
\\]

#### Out of bag error

Since we create bootstrapped data sets with duplicate entries, some entities
will not be included to these data sets. These entities form an out of bag data set.
To estimate out of bag error we calculate the average prediction error on all
entities $x_i$ using only the trees that do not have $x_i$ in their training data set.

#### Typical parameter values

For classification typical value of $m$ is $m = \lfloor\sqrt p \rfloor$ and the minimum node size is $1$.

For regression typical value of $m$ is $m = \lfloor\frac{p}{3} \rfloor$ and the minimum node size is $5$.

Since we know how to estimate the accuracy of Random Forest we can use this knowledge to find the optimal parameter $m$.
(Just by comparing the accuracies of different RFs created using different $m$ values)

#### Missing data in the training dataset
Probably the easiest way to fill in a table with missing data is to use median, mean or mode's values of the feature.
It is a good initial guess. RF allows us to refine that initial guess until it is a good guess. To do this
we first determine which samples are similar to the one with missing data. So here we go.

1. First we need to fill in our data table with initial guesses
2. We repeatedly do the following until the missing values converge:
   1. Build a Random Forest
   2. Run all of the data
   3. Fill in Proximity Matrix. Proximity Matrix is a $M \times M$ matrix $P$ with a row and a column for each sample.
   Each cell contains a similarity measure: there is a similarity between two samples if running them down a tree ends up in the same node.
   If $i$-th and $j$-th samples are similar $P[i,j]$ is incremented. Finally we divide each proximity value by the total number of 
   trees in RF.
   4. Recalculate the missing values using proximity matrix (as a weighted average, or weighted frequency)

#### Missing data in the dataset that we want to categorize
TODO

#### Variable importance
TODO

#### Key features
- there is no need to use validation data set to estimate the quality of trained model
- additional usage case: RF can be used for identifying the most informative features
  
<br>
#### Links
[StatQuest: Random Forests Part 1 - Building, Using and Evaluating](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF&index=38)