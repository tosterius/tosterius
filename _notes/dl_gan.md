---
layout: note
cdate: "Dec 20, 2020"
mdate: "Dec 20, 2020"
title: "Generative Adversarial Networks"
category: DL
index: 6
headline: ""
picture: 
---

| Discriminative models | Generative models |
| --------------------- | ----------------- |
|$X\rightarrow Y$, $p(X\|Y)$              |$\xi, Y\rightarrow X$,  $p(\xi, Y\|X)$   |


### Autoencoders

Autoencoders are used to reduce an input into smaller representation. They consist of three parts

- encoder:  $\mathbf{z} = E(\mathbf{x}, \mathbf{\theta}_E)$
- latent representation of data
- decoder: $\mathbf{\hat{x}} = D(\mathbf{z}, \mathbf{\theta}_D)$

Optimal parameters learned w.r.t. loss f-n $L$:
\\[
\begin{equation}
\[\mathbf{\theta}_E, \mathbf{\theta}_D\] = \arg\min L(\mathbf{\hat{x}}, \mathbf{x})
\end{equation}
\\]

Our input data is converted into an encoding vector. Dimensions of the vector represent
some learned attribute about the data: single value for each encoded feature. That is why autoencoders can
not be used for data generation.


### Variational Autoencoders (VAE)

<!-- ![rnn_0]({{ site.baseurl }}/assets/img/notes/rnn_0.png) -->

\\[
\begin{split}
&a^{(t)} = W_{hh} h^{(t-1)} + W_{xh}x^{(t)} + b_h \\\\\\\\
&h^{(t)} = f(a^{(t)}) \\\\\\\\ \
&o^{(t)} = W_{hz} h^{(t)} + b_z \\\\\\\\
&z^{(t)} = g(o^{(t)})
\end{split}
\tag{1}\label{eq1}
\\]



#### Links

1. [Recurrent Neural Networks cheatsheet](https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks#overview)
2. [Recurrent Neural Networks Tutorial](http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)
3. [On the difficulty of training recurrent neural networks](http://proceedings.mlr.press/v28/pascanu13.pdf)
4. [A Gentle Tutorial of Recurrent Neural Network with Error Backpropagation](https://arxiv.org/pdf/1610.02583.pdf)