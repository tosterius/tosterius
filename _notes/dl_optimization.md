---
layout: note
title: "Gradient descent and optimization in neural networks"
category: DL
index: 1
headline: 
picture: 
---
### SGD
\\[
\begin{equation}
\theta_{t + 1} = \theta_{t} - \alpha \Delta \theta_{t}
\end{equation}
\\]

- Memory: $memory(\text{forward path})$
  
### Momentum
\\[
\begin{split}
u_{t + 1} &= \mu u_{t} +  \alpha \nabla E(\theta_{t}) \\\\\\
\theta_{t + 1} &= \theta_{t} - u_{t + 1} \\\\\\
\end{split}
\\]

- Memory: $memory(\text{forward path}) + memory(u)$
  
### Nesterov Momentum
Momentum allows to avoid some of local minimums, speeds up the convergence in some cases
\\[
\begin{split}
u_{t + 1} &= \mu u_{t} +  \alpha \nabla E(\theta_{t} - \mu u_{t}) \\\\\\
\theta_{t + 1} &= \theta_{t} - u_{t + 1} \\\\\\
\end{split}
\\]

- Memory: $memory(\text{forward path}) + memory(u)$
 
### Adagarad
Adagarad adaptively tunes the learning rate per parameter.

\\[
\begin{split}
cache_{t + 1} &= cache_{t} +  (\nabla E(\theta_{t}))^2 \\\\\\
\theta_{t + 1} &= \theta_{t} - \alpha \frac{\nabla E(\theta_{t})}{\sqrt{cache_{t + 1}} + \epsilon} \\\\\\
\end{split}
\\]

- Weights that receive high gradients will have their effective learning rate reduced,
  while weights that receive small or infrequent updates will have their effective learning rate increased. 
- The downside is that this squared gradient grows (over the course of training) and the update step becomes smaller and smaller.
- If we get a saddle point we might get stuck
- Memory: $memory(\text{forward path}) + memory(cache)$
  
### RMSProp
RMSProp is slight variation of Adagrad.
The difference between them is that RMSProp let that squared gradient estimate decay.

\\[
\begin{split}
cache_{t + 1} &= \beta cache_{t} + (1 - \beta) (\nabla E(\theta_{t}))^2 \\\\\\
\theta_{t + 1} &= \theta_{t} - \alpha \frac{\nabla E(\theta_{t})}{\sqrt{cache_{t + 1}} + \epsilon} \\\\\\
\end{split}
\\]

- Memory: $memory(\text{forward path}) + memory(cache)$

### Adam

\\[
\begin{split}
u_{t + 1} &= \gamma u_{t} +  (1 - \gamma) \nabla E(\theta_{t}) \\\\\\
cache_{t + 1} &= \beta cache_{t} + (1 - \beta) (\nabla E(\theta_{t}))^2 \\\\\\
\theta_{t + 1} &= \theta_{t} - \alpha \frac{u_{t + 1})}{\sqrt{cache_{t + 1}} + \epsilon} \\\\\\
\end{split}
\\]

- Memory: $memory(\text{forward path}) + memory(u) + memory(cache)$


## Links

[Stanford CS231n](https://cs231n.github.io/neural-networks-3/)