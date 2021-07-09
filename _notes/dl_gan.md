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

Discriminative models try to model the probability of class $Y$ given a set of features $X$.
Generative models learn how to make a realistic representation of some class. Generative models
take some additional input represented as a noise here.

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



#### Links

