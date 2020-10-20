---
layout: note
cdate: "Dec 21, 2019"
title: Logistic Regression
category: ML
index: 2
headline: 
picture:
---

### Data and goal

Given a dataset of $N$ observations $\\{\mathbf{x}_n, y_n\\},\; y_n \in C_k, n = 1,\dots,N$.
Where $C_k$ is the set of $K$ discrete classes. 

The goal is to take an input vector $x$ and to assign it to one of these $K$ classes.
For binary classification $C_k = \\{-1, +1\\}$.


### Intuition behind Logistic Regression

Let us think of predicting the probability of object to belong to positive class 
$p_+ = p\left(y_i = 1 \mid \mathbf{x}\right)$.

We can not use linear regression directly to predict this value 
since the probability is a  real number between 0 and 1.

A few observations:

- $\frac{p_+}{1 - p_+} \in \[0, +\infty)$ is the chance of assigning an example to the class "+"
- $\log(\frac{p_+}{1 - p_+}) \in (-\infty, +\infty)$

It means we can predict the value of $\log(\frac{p_+}{1 - p_+})$ using linear regression model.

Combining this expression with the equation of linear regression we get
\\[
\begin{equation}
\log(\frac{p_+}{1 - p_+}) = \mathbf{w}^T\mathbf{x}
\end{equation}
\\]
and
\\[
\begin{equation}
p_{+} = \frac{1}{1 + \exp^{-\mathbf{w}^T\mathbf{x} }} = \sigma(\mathbf{w}^T\mathbf{x})
\end{equation}
\\]

More general, we rewrite last expression as the following:

\\[
\begin{equation}
p\left(y = y_i \mid \mathbf{x}_i, \mathbf{w}\right) = \sigma(y_i\mathbf{w}^T\mathbf{x}_i)
\end{equation}
\\]

###  Maximum Likelihood Estimation

Assuming that the objects in our data set are i.i.d. the likelihood of the data set can be written
\\[
\begin{equation}
P\left(\mathbf{y} \mid \mathbf{X}, \mathbf{w}\right) = \prod_{i=1}^{N} p\left(y = y_i \mid \mathbf{x}_{i}, \mathbf{w}\right),
\end{equation}
\\]


\\[
\begin{split}
\log P(\mathbf{y} \mid \mathbf{X}, \mathbf{w}) &= \log \prod_{i=1}^{N} p(y = y_i \mid \mathbf{x}_{i}, \mathbf{w}) \\\\\\
 &= \log \prod\_{i=1}^{N} \sigma(y\_i\mathbf{w}^{T}\mathbf{x}\_i) \\\\\\
 &= \sum\_{i=1}^{N} \log \sigma(y\_i\mathbf{w}^{T}\mathbf{x}\_i) \\\\\\
 &= \sum\_{i=1}^{N} \log \frac{1}{1 + \exp^{-y\_i\mathbf{w}^{T}\mathbf{x}_i }} \\\\\\
  &= -\sum\_{i=1}^{N} \log (1 + \exp^{-y\_i\mathbf{w}^{T}\mathbf{x}_i }) \\\\\\
\end{split}
\\]

That gives us the logistic loss

\\[
\begin{equation}
E_{\text{logistic}} = \sum\_{i=1}^{N} \log (1 + \exp^{-y\_i\mathbf{w}^{T}\mathbf{x}_i })
\end{equation}
\\]
where $y\_i \in \\{-1, +1\\}$.


Note: Logistic regression model predicts calibrated probabilities.
Predicted probabilities that match the expected distribution of probabilities for each class are referred to as calibrated. 


### Metrics
[Link](/notes/ml_fundamentals.html)

<br>
#### Links
