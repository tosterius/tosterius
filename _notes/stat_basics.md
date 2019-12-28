---
layout: note
title: "Basics of statistics"
category: "Statistics"
index: 6
headline:
picture:
---
### 1. Combinatorics reminder

##### Permutations
Permutations are all the possible ways elements in a set can be arranged, where the order
is important.
The number of permutations of subsets of size $$k$$ drawn from a set of size $$n$$ is given by
\\[
    A^k_n = nPk = \frac{n!}{(n-k)!}
\\]

##### Combinations
Combinations are all the possible ways to select items from a collection, such that (unlike permutations) the order of selection does not matter.
The number of combinations of subsets of size $$k$$ drawn from a set of size $$n$$ is given by:
\\[
    C^k_n = nCk = \binom{n}{k} = \frac{n!}{k!(n-k)!}
\\]


<br>
#### 1. Expectation and variance
If $$X$$ is discrete random variable:
\\[
\begin{equation}
E(X) = \sum_{x}^{\infty} x \, p_X(x)
\end{equation}
\\]
If $$X$$ is continuous random variable:
\\[
\begin{equation}
E(X) = \int_{-\infty}^{\infty} x \, f_X(x)\, dx\
\end{equation}
\\]

Variance:
\\[
\begin{equation}
Var(X)=E((X-E(X))^2) = E(X^2)-(E(X))^2
\end{equation}
\\]


<br>
#### 2. Covariance

Is a way to classify three types of __linear__ relationship:

- When $$Cov$$ is positive relationship has a positive slope
- When $$Cov$$ is negative relationship has a negative slope
- When $$Cov$$ is $$0$$ there is no relationship

###### Covariance of two jointly distributed real-valued random variables
\\[
\begin{equation}
Cov(X, Y) = E((X - E(X))(Y-E(Y)))
\end{equation}
\\]

###### Covariance of two datasamples
\\[
\begin{equation}
Cov(X, Y) = \frac{\sum_i(X-X_i)(Y-Y_i)}{n - 1}
\end{equation}
\\]

<br>
#### 3. Correlation

###### For population
Given a pair of random variables $$X,Y$$; 
\\[
\begin{equation}
Corr(X, Y) = \frac{Cov(X, Y)}{\sigma_X\sigma_Y}
\end{equation}
\\]

###### For sample
Given paired data $$\{(x_1, y_1), \dots , (x_n , y_n)\}$$  consisting of $$n$$ pairs;
\\[
\begin{equation}
r_{xy}= \frac{\sum_{i=1}^{n} (x_i - \overline{x})(y_i - \overline{y})}
{\sqrt{\sum_{i=1}^{n} (x_i - \overline{x})^2(y_i - \overline{y})^2}}
\end{equation}
\\]


#### 4. The law of large numbers
As the number of identicaly ditributed, randomly generated numbers increases, their sample mean approaches their theoretical mean.

> Theorem.
<br>
Let $$X_1, X_2, \dots X_i$$ be a sequence of independent random variables with $$E(X_i) = \mu$$ and $$Var(X_i) = \sigma^2$$.
Let $$\overline{X_n} = \frac{\sum_i^nX_i}{n}$$. Then for any $$\epsilon > 0$$
\\[
\begin{equation}
P(|\overline{X_n} - \mu| > \epsilon) \rightarrow 0, \; as \; n \rightarrow \infty
\end{equation}
\\]


<br>
#### Links
- [https://en.wikipedia.org/wiki/Pearson_correlation_coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)


