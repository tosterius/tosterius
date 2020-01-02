---
layout: note
title: Random Forests
category: ML
index: 4
headline:
picture:
---

In simple words, Random Forest uses bagging to build a collection of decision trees and then averages them.

Let us denote $$B$$ as a number of tree we are going to create.
$$p$$ is the number of features.

__Random Fores algorithm__:

1. For $$b = 1$$ to $$b = B$$:
   1. create bootstrapped data set $$Z$$ from the training data
   2. create decision tree using this new data set by recursively repeating the following steps
   for each terminal node:
   - Randomly select $$m$$ variables from the $$p$$ variables
   - Pick the best variable and split point among the $$m$$
   - Split the node into two child sub-nodes
  
2. output the ensemble of trees $${T}^B$$

Prediction for Regression trees:
\\[
\begin{equation}
f(x) = \frac{1}{B}\sum_{b=1}^{B}T_b(x)
\end{equation}
\\]

Prediction for Classification trees:
\\[
\begin{equation}
c(x) = majorityvote(\\{c_b for\;b = 1\; to\; b = B\\})
\end{equation}
\\]

<br>
#### Links
[StatQuest: Random Forests Part 1 - Building, Using and Evaluating](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF&index=38)