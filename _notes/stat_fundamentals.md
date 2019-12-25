---
layout: note
title: "Refresher notes: Probability distributions"
category: "Statistics"
index: 7
headline:
picture:
---

### Combinatorics reminder

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
#### 1. Bernoulli Distribution
The Bernoulli distribution is the discrete probability distribution of a random variable which takes a binary output:
 $$1$$ with probability $$p$$, and $$0$$ with probability $$(1-p)$$. 

\\[
\begin{equation}
p(x) = p^x (1-p)^x, where\; x = \\{0, 1\\}
\end{equation}
\\]
\\[
\begin{equation}
E(x) = p, \; V(x) = p(1 - p)
\end{equation}
\\]

Example: flipping a coin one time.

<br>
#### 2. Binomial distribution

- $$n$$ independent experiments are performed
- each experiment results in $$1$$ with probability $$p$$ and $$0$$ with probability $$1 − p$$. 
- the total number of successes, $$k$$, is a binomial random variable with parameters $$n$$ and $$p$$
\\[
\begin{equation}
p(k) = C_k^n p^k (1-p)^{n-k}
\end{equation}
\\]
\\[
\begin{equation}
E(x) = np, \; V(x) = np(1 - p)
\end{equation}
\\]

Example: flipping a coin $$n$$ times. What is the probability of getting $$k$$ heads?

<br>
#### 3. Poisson distribution and Poisson process

The Poisson distribution can be derived as the limit of a binomial distribution as
the number of trials, $$n$$, approaches infinity and the probability of success on each trial,
$$p$$, approaches zero in such a way that $$np = \lambda$$.

\\[
\begin{equation}
p(k) = -\frac{\lambda^k}{k!}e^{\lambda}
\end{equation}
\\]
\\[
\begin{equation}
E(k) = \lambda, \; V(x) = \lambda
\end{equation}
\\]

A Poisson Process is a model for a series of discrete event where the average time between events is known,
but the exact timing of events is random. The arrival of an event is independent of the event before.
(Poisson random variable also applies to disjoint regions of space.)

We observe $$k$$ events in a time period given the length of the period and the average events per time
$$\lambda$$ is an expacted number of events in interval (or region of space):

\\[
\begin{equation}
p(k_{events\\_in\\_interval}) = -\frac{\lambda^k}{k!}e^{\lambda}
\end{equation}
\\]
\\[
\begin{equation}
\lambda = \frac{events}{time}interval
\end{equation}
\\]

Examples:

- the requests for individual documents on a web server
- failure of a machine in one month
- number of typing errors on a page

<br>
#### 4. Gaussian distribution

Probability density function:

\\[
\begin{equation}
f(x) = \frac{1} {\sigma\sqrt{2\pi}} e^{-(x - \mu)^{2}/(2\sigma^{2}) }
\end{equation}
\\]

\\[
\begin{equation}
E(x) = \mu, \; V(x) = \sigma
\end{equation}
\\]
The notation $$N(\mu, \sigma^2)$$ means normally distributed with mean $$\mu$$ and variance $$\sigma$$.


- Many classical statistical tests are based on the assumption that the data follow a normal distribution. This assumption should be tested before applying these tests.
- In modeling applications, such as linear and non-linear regression, the error term is often assumed to follow a normal distribution with fixed location and scale.
- The normal distribution is used to find significance levels in many hypothesis tests and confidence intervals. 


<br>
#### Links
- [The Poisson Distribution and Poisson Process Explained](https://towardsdatascience.com/the-poisson-distribution-and-poisson-process-explained-4e2cb17d459)
- [Wiki. Poisson Distribution](https://en.wikipedia.org/wiki/Poisson_distribution)
- [Normal Distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm)