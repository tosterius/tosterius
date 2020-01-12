---
layout: note
title: "Backpropagation in neural networks"
category: DL
index: 0
headline: 
picture: 
---

Let us start with a notation which we will use in the explanation.

- $$w_{jk}^l$$ is the weight for node $$k$$ in the layer $$l$$ for incoming node $$j$$
- $$b_j^l$$ is the bias for node $$j$$ in the layer $$l$$
- $$a_j^l$$ is the activation of $$j$$-th neuron in the layer $$l$$

![backpropagation_0]({{ site.baseurl }}/assets/img/notes/backpropagation_0.png)

The activation of a neuron in the $$l$$-th layer depends on activations of neurons in the layer $$l-1$$
\\[
\begin{equation}
a_j^l = \sigma(\sum_{k \in layer_{l-1} } w_{jk}^l a_k^{l-1} + b_j^l),
\end{equation}
\\]
or vectorized form
\\[
\begin{equation}
a^{l} = \sigma(w^l a^{l-1}+b^l).
\end{equation}
\\]

