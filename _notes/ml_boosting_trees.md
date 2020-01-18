---
layout: note
title: Boosting and Additive Trees. AdaBoost.
category: ML
index: 5
headline:
picture:
---

The general idea of boosting is to create a _strong_ classifier from a number of 
_weak_ classifiers. A weak classifier produces prediction that slightly better than random
guessing.

To make highly accurate model Adaboost combines many weak classifiers, so that 
weak classifier takes into account the errors of the previous weak classifier.

The most common weak learner algorithm used with Adaboost is Decision Tree with one level or
_decision stumps_ (just a node and two leaves).

<br>
##### The boosting algorithm Adaboost
<br>
The idea is to set weights to both classifiers and samples in a way that forces classifiers 
to focus on observations that are difficult to correctly classify.

1. Given the training set $$(x_0, y_0),\dots, (x_m, y_m)$$, where $$x_i \in X$$, $$y_i \in \{-1, 1\}$$
2. Initialize weights of samples $$D_1(i) = 1/m$$, for $$i=1,\dots, m$$
3. For $$t=1,\dots, T$$:
    1. Train a weak learner using distribution $$D_t$$
    2. Get weak hypothesis $$h_t \rightarrow \{-1, 1\}$$
    3. Aim: select $$h_t$$ with low weighted error: $$\epsilon_t = Pr_{i\sim D_t}(h_t(x_i) \neq y_i)$$.
    Formally, minimum misclassification error for the model is computed as follows:
    \\[
    \begin{equation}
    \epsilon_t = \frac{\sum_{i=1}^m D_t(i)I(y_i \neq h_t(x_i))}{\sum_{i=1}^m D_t(i)}
    \end{equation}
    \\]
4. Choose weight of hypothesis (classifier) $$\alpha_t = \frac{1}{2}\ln (\frac{1-\epsilon_t}{\epsilon_t})$$
5. Update weights of samples. For $$i=1,\dots, m$$:
\\[
\begin{equation}
D_{t+1}(i) = \frac{D_{t}(i)\exp(-\alpha_t y_i h_t(x_i))}{Z_t}
\end{equation}
\\]
where $$Z_t$$ is a normalization factor (chosen so that $$D_{t+1}$$ will be a distribution).
6. Final hyphotesis:
\\[
\begin{equation}
H(x) = sign(\sum_{t=1}^T \alpha_t h_t(x))
\end{equation}
\\]


<br>
#### Links

[Explaining AdaBoost, Robert E. Schapire](http://rob.schapire.net/papers/explaining-adaboost.pdf)