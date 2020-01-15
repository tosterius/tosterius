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
- E is the cost function

> 
__The goal of backpropagation is to minimize the cost function $$E$$ by computing the partial derivatives 
$$\frac{\partial E}{\partial w}$$ and $$\frac{\partial E}{\partial b}$$ with respect to any weight and 
bias in the network.__

![backpropagation_0]({{ site.baseurl }}/assets/img/notes/backpropagation_0.png)

The activation of a neuron in the $$l$$-th layer depends on activations of neurons in the layer $$l-1$$
\\[
\begin{equation}
a_j^l = \sigma(\sum_{k \in layer_{l-1} } w_{jk}^l a_k^{l-1} + b_j^l),
\end{equation}
\\]
or 
\\[
\begin{equation}
a_j^l = \sigma(z_j^l), \; z_j^l = \sum_{k \in layer_{l-1} } w_{jk}^l a_k^{l-1} + b_j^l \tag{1}\label{eq1}
\end{equation}
\\]

We define a error of $$j$$-th neuron on the $$l$$-th layer:

\\[
\begin{equation}
\delta^l_j = \frac{\partial E}{\partial z^l_j} \tag{2}\label{eq2}
\end{equation}
\\]

__An equation for the error in the output layer__

\\[
\begin{equation}
\boxed{\delta^L_j = \frac{\partial E}{\partial z^L_j} = \frac{\partial E}{\partial a^L_j} \frac{\partial a^L_j}{\partial z^L_j} 
= \frac{\partial E}{\partial a^L_j} \sigma'(z_j^L)} \tag{3}\label{eq3}
\end{equation}
\\]

__Now we reformulate the expression $$(\ref{eq2})$$ for $$\delta^l_j$$ in terms of the error
in the next layer $$l+1$$__:

\\[
\begin{split}
\delta^l_j &= & \frac{\partial E}{\partial z^l_j} \\\\\\
&= & \sum_k \frac{\partial E}{\partial z^{l+1}_k} \frac{\partial z^{l+1}_k}{\partial z^l_j} \\\\\\
&= & \sum_k \frac{\partial z^{l+1}_k}{\partial z^l_j} \delta^{l+1}_k
\end{split} \tag{4}\label{eq4}
\\]

Note that:
\\[
\begin{equation}
z_k^{l+1} = \sum_{j} w_{kj}^{l+1} \sigma(z_j^l) + b_k^{l+1} \tag{5}\label{eq5}
\end{equation}
\\]

Putting $$(\ref{eq5})$$ to $$(\ref{eq4})$$ we get :

\\[
\begin{equation}
\boxed{\delta^l_j = \sum_{k} \delta_k^{l+1} w_{kj}^{l+1} \sigma'(z_j^l)} \tag{6}\label{eq6}
\end{equation}
\\]

__Rate of change of the cost function with respect to a weight in network:__
\\[
\begin{equation}
\boxed{\frac{\partial E}{\partial w_{jk}^l} = \frac{\partial E}{\partial z_j^l} \frac{\partial z_j^l}{\partial w_{jk}^l} = \delta_j^l a_k^{l-1}}\tag{7}\label{eq7}
\end{equation}
\\]


__Rate of change of the cost function with respect to a bias in network:__
\\[
\begin{equation}
\boxed{\frac{\partial E}{\partial b_j^l} = \frac{\partial E}{\partial z_j^l} \frac{\partial z_j^l}{\partial b_j^l} = \delta_j^l }\tag{8}\label{eq8}
\end{equation}
\\]

Equations $$(\ref{eq3})$$, $$(\ref{eq6})$$, $$(\ref{eq7})$$, $$(\ref{eq8})$$ are fundamental equations of backpropagation.