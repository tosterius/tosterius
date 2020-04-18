---
layout: note # You can ommit this if you've set it as a default
title: Linear Regression
category: ML
index: 1
headline:
picture:
---

Given training dataset of $N$ observations $\{\mathbf{x}_n\}$ with corresponding 
target values $t_n$. The goal of regression is to predict the target value $t$ by input $\mathbf{x}$.

The response of the model is modeled as linear combination of predictors:
\\[
\begin{equation}
y = \mathbf{w}^T\mathbf{x}, \; \mathbf{x} \in R^D\tag{0}\label{0}
\end{equation}
\\]

##### Maximum likelihood and least squares

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
p(t|\mathbf{\mathcal{X}}, \mathbf{w}, \sigma^2) = \prod^{N}_{n = 1}\mathcal{N} (t|\mathbf{w}^T \mathbf{x}_n,\sigma^2)
\\]

Gaussian distribution formula:
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