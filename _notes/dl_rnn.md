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
&s^{(t)} = W_{aa} a^{(t-1)} + W_{aw}x^t + b_a \\\\\\\\
&o^{(t)} = W_{ay} a^{(t)} + b_y \\\\\\\\ \
&a^{(t)} = f(s^{(t)}) \\\\\\\\
&y^{(t)} = g(o^{(t)})
\end{split}
\tag{1}\label{eq1}
\\]


#### Links

1. [Recurrent Neural Networks cheatsheet](https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks#overview)
2. [IRecurrent Neural Networks Tutorial](http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/)