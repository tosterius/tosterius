---
layout: note
title: "Recurrent neural networks"
category: DL
index: 5
headline: ""
picture: 
---

The reason why we use RNNs is processing sequential data like texts, voice and music records, video records etc.
We can think of RNNs that they have a memory which captures information what has been calculated so far. In other words
when RNNs process an element in the sequence the output depends on the calculations performed on the previous elements in the
sequence.


<!-- ![rnn_0]({{ site.baseurl }}/assets/img/notes/rnn_0.png) -->

\\[
\begin{split}
&a^{(t)} = W_{hh} h^{(t-1)} + W_{xh}x^{(t)} + b_h \\\\\\\\
&o^{(t)} = W_{hz} a^{(t)} + b_z \\\\\\\\ \
&h^{(t)} = f(a^{(t)}) \\\\\\\\
&z^{(t)} = g(o^{(t)})
\end{split}
\tag{1}\label{eq1}
\\]

Where
- $x^{(t)}$ is the input at time step $t$
- $h^{(t)}$ is the hidden state at time step $t$
- $o^{(t)}$ is the intermediate term. Used to calculate $z^{(t)}$
- $z^{(t)}$ is the prediction at the time step $t$ 

<br>
#### Backpropagation
In RNNs loss is calculated for each output $z^t$. To account with multiple losses RNNs
Backpropagation through time is used.

Let $L(\cdot)$ be the chosen loss function and the objective function is expressed as
\\[
\begin{equation}
L(x,y) = \sum_{t=1}^{T} L(y^t, z^t).
\end{equation}
\\]
We start with its derivative with respect to $W_{hz}$ and bias $b_z$:

\\[
\begin{equation}
\frac{\partial L}{\partial W_{hz}} = \sum_{t=1}^{T}\frac{\partial L}{\partial z^t} \frac{\partial z^t}{\partial W_{hz}}
\end{equation}
\\]

\\[
\begin{equation}
\frac{\partial L}{\partial b_z} = \sum_{t=1}^{T}\frac{\partial L}{\partial z^t} \frac{\partial z^t}{\partial b_z}
\end{equation}
\\]

Now let us derive the derivative w.r.t. $W_{hh}$.
\\[
\begin{equation}
\frac{\partial L^{t}}{\partial W_{hh}} = \sum_{k=1}^{t}\frac{\partial L^{t}}{\partial z^{t}} \frac{\partial z^{t}}{\partial h^{t}} \frac{\partial h^{t}}{\partial h^{k}} \frac{\partial h^{k}}{\partial W_{hh}}
\end{equation}
\\]

\\[
\begin{equation}
\frac{\partial L}{\partial W_{hh}} = \sum_{t=1}^{T}\sum_{k=1}^{t}\frac{\partial L^{t}}{\partial z^{t}} \frac{\partial z^{t}}{\partial h^{t}} \frac{\partial h^{t}}{\partial h^{k}} \frac{\partial h^{k}}{\partial W_{hh}}
\end{equation}
\\]

Now we turn to derive the gradient w.r.t.$W_{xh}$. (We consider just the time step $t$).
Since $h^{t-1}$ and $x^t$ both make a contribution to $h^t$ and we  get:
\\[
\begin{equation}
\frac{\partial L^{t}}{\partial W_{xh}} = \frac{\partial L^{t}}{\partial h^t} \frac{\partial h^t}{\partial W_{xh}} + \frac{\partial L^{t}}{\partial h^t} \frac{\partial h^t}{\partial h^{t-1}} \frac{\partial h^{t-1}}{\partial W_{xh}}
\end{equation}
\\]

Finally we get
\\[
\begin{equation}
\frac{\partial L}{\partial W_{xh}} = \sum_{t=1}^{T} \sum_{k=1}^{t}\frac{\partial L^{t}}{\partial z^{t}} \frac{\partial z^{t}}{\partial h^{t}} \frac{\partial h^{t}}{\partial h^{k}} \frac{\partial h^{k}}{\partial W_{xh}}
\end{equation}
\\]

#### Links

1. [Recurrent Neural Networks cheatsheet](https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks#overview)
2. [Recurrent Neural Networks Tutorial](http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)
3. [On the difficulty of training recurrent neural networks](http://proceedings.mlr.press/v28/pascanu13.pdf)
4. [A Gentle Tutorial of Recurrent Neural Network with Error Backpropagation](https://arxiv.org/pdf/1610.02583.pdf)