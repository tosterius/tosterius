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
&o^{(t)} = W_{hy} a^{(t)} + b_y \\\\\\\\ \
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


#### Links

1. [Recurrent Neural Networks cheatsheet](https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks#overview)
2. [IRecurrent Neural Networks Tutorial](http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)
3. [On the difficulty of training recurrent neural networks](http://proceedings.mlr.press/v28/pascanu13.pdf)