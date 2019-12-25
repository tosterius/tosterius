---
layout: note
title: "Statistics fundamentals: Probability distributions"
category: Statistics
index: 7
headline:
picture:
---

### Combinatorics remainder

#### Permutations
Permutations are all the possible ways elements in a set can be arranged, where the order
is important.
The number of permutations of subsets of size $$k$$ drawn from a set of size $$n$$ is given by
\\[
    A_k^n = nPk = \frac{n!}{(n-k)!}
\\]

#### Combinations
The number of combinations of subsets of size $$k$$ drawn from a set of size $$n$$ is given by:
\\[
    C_k^n = nCk = \binom{n}{k} = \frac{n!}{k!(n-k)!}
\\]

#### Binominal distribution

- $$n$$ independent experiments, or trials, are performed
- each experiment results in a “success” with probability $$p$$ and a
“failure” with probability $$1 − p$$. 
- the total number of successes, $$k$$, is a binomial random variable with parameters $$n$$ and $$p$$
\\[
\begin{equation}
p(k) = C_n^k p^k (1-p)^k
\end{equation}
\\]

#### Poisson distribution

The Poisson distribution can be derived as the limit of a binomial distribution as
the number of trials, $$n$$, approaches infinity and the probability of success on each trial,
$$p$$, approaches zero in such a way that $$np = \lambda$$.

<br>

이 포스팅은 놀라운 Markdown 기술들로 만들어진 결과물입니다.

`_utility.html`에서 스타일을 변경할 수 있으며, 서식 샘플은 아래와 같습니다.

<br>

<h2>1. HTML headings</h2>
{% highlight html %}
<h1>This is heading 1</h1>
<h2>This is heading 2</h2>
<h3>This is heading 3</h3>
<h4>This is heading 4</h4>
<h5>This is heading 5</h5>
<h6>This is heading 6</h6>
{% endhighlight %}
<h1>This is heading 1</h1>
<h2>This is heading 2</h2>
<h3>This is heading 3</h3>
<h4>This is heading 4</h4>
<h5>This is heading 5</h5>
<h6>This is heading 6</h6>

<br>

<h2>2. bold text</h2>
{% highlight html %}
<p>This is normal text - <b>and this is bold text</b>.</p>
{% endhighlight %}
<p>This is normal text - <b>and this is bold text</b>.</p>

<br>

<h2>3. list</h2>
<h3>a. unordered list</h3>
{% highlight html %}
- Coffee
- Tea
- Milk
{% endhighlight %}
- Coffee
- Tea
- Milk

<h3>b. ordered list</h3>
{% highlight html %}
1. Coffee
2. Tea
3. Milk
{% endhighlight %}
1. Coffee
2. Tea
3. Milk

<br>

<h2>4. hyperlink</h2>
{% highlight html %}
[naye0ng's blog](https://naye0ng.github.io)
{% endhighlight %}
[naye0ng's blog](https://naye0ng.github.io)

<br>

<h2>5. image</h2>
{% highlight html %}
![sample image]({{ site.baseurl }}/assets/img/koreaSunset.jpg)
{% endhighlight %}
![sample image]({{ site.baseurl }}/assets/img/koreaSunset.jpg)

<br>

<h2>5. table</h2>
{% highlight html %}
| Header 1  | Header 2 | Header 3 |
| :------- | :-------: | -------: |
| Content 1  | Content 2 | Content 3 |
| Content 1  | Content 2 | Content 3 |
{% endhighlight %}
| Header 1  | Header 2 | Header 3 |
| :------- | :-------: | -------: |
| Content 1 | Content 2 | Content 3 |
| Content 1 | Content 2 | Content 3 |
