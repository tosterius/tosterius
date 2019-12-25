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
    A_k^n = nPk = \frac{n!}{(n-k)!}
\\]

##### Combinations
The number of combinations of subsets of size $$k$$ drawn from a set of size $$n$$ is given by:
\\[
    C_k^n = nCk = \binom{n}{k} = \frac{n!}{k!(n-k)!}
\\]


<br>
#### 1. Expectation and variance
If $$X$$ is discrete random variable:
\\[
\begin{equation}
E(X) = \sum_{x} x \, p_X(x)
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


<br>
#### Links
- [https://en.wikipedia.org/wiki/Pearson_correlation_coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)


