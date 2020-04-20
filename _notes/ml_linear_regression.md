---
layout: note # You can ommit this if you've set it as a default
title: Linear Regression
category: ML
index: 1
headline:
picture:
---

Given a dataset of $N$ observations $\\{\mathbf{x}_n, t_n\\},\; n = 1,\dots,N$.

The goal to find a function $y: \mathbb{R}^D \rightarrow \mathbb{R}$ such that $t \approx y(\mathbf{x}, \mathbf{w})$. Simply speaking
we need to predict the target value $t$ by input $\mathbf{x}$.

The linear regression model has the form:
\\[
\begin{equation}
y = \mathbf{w}^T\mathbf{x}, \; \mathbf{x} \in \mathbb{R}^D\tag{0}\label{0}
\end{equation}
\\]

### Maximum likelihood and least squares

We assume that the target variable $t$ is given by a function $y(\mathbf{x}, \mathbf{w})$ with additive Gaussian noise:
\\[
\begin{equation}
t = y(\mathbf{x}, \mathbf{w}) + \epsilon, \; \epsilon \sim \mathcal{N}(0, \sigma^2)  \tag{1}\label{1}
\end{equation}
\\]
In other words:
\\[
\begin{equation}
p(t|\mathbf{x}, \mathbf{w}, \sigma^2) = \mathcal{N} (t|y(\mathbf{x}, \mathbf{w}),\sigma^2).  \tag{2}\label{2}
\end{equation}
\\]

Making the assumption that our data points are drawn independently from the distribution (\ref{2}), we obtain the
following expression for the likelihood function
\\[
p(t|\mathbf{\mathcal{X}}, \mathbf{w}, \sigma^2) = \prod^{N}_{n = 1}\mathcal{N} (t_n|\mathbf{w}^T \mathbf{x}_n,\sigma^2)
\\]

Recall Gaussian distribution function:
\\[
\begin{equation}
p(x|\mu, \sigma) = \frac{1}{\sigma \sqrt{2 \pi}}\exp{-\frac{(x - \mu)^2}{2\sigma^2}}.  \tag{3}\label{3}
\end{equation}
\\]

Let us substitute it to likelihood expression and take a logarithm:

\\[
\begin{equation}
ln (p(t|\mathbf{w}, \sigma^2)) = -\frac{N}{2} ln(2\pi\sigma^2) - \frac{1}{2\sigma^2} \sum_{i = 1}^{N} (t_i - \mathbf{w}^T \mathbf{x}_i)^2.  \tag{4}\label{4}
\end{equation}
\\]
Here we can see that maximization of the likelihood function  is equivalent to minimizing
a sum-of-squares error function. 


### Analytical solution

We can write the residual sum-of-squares as:

\\[
\begin{equation}
RSS(\mathbf{w}) = (t − \mathbf{X}\mathbf{w})^T (t − \mathbf{X}\mathbf{w}) \tag{5}\label{5}
\end{equation}
\\]

Setting the first derivative to zero:

\\[
\begin{equation}
\frac{\partial RSS(\mathbf{w})}{\partial \mathbf{w}} = −2\mathbf{X}^T (t − \mathbf{X}\mathbf{w}) \tag{6}\label{6}
\end{equation}
\\]

we get the solution:

\\[
\begin{equation}
\mathbf{\hat w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T t \tag{7}\label{7}
\end{equation}
\\]


Here are the problems:
- what if $\mathbf{X}^T \mathbf{X}$ is singular (number of observations greater than number of features
  or two or more features are linearly dependent) ?
- what if the dimensions of $\mathbf{X}$ are too large


### Regularization

- MSE (sensitive to noise)
- MAE (non-diff)

#### Ridge regression model

