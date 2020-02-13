---
layout: note
title: Support Vector Machines
category: ML
index: 3
headline:
picture:
---

### Linear SVM

Support Vector Machine performs classification by finding the _optimal separating hyperplane_
 that maximizes the _margin_ between the two classes (OSH is as far as possible from the data points of each category).

We are given a set of data points $\\{(\mathbf{x}_1, y_1), \dots (\mathbf{x}_n, y_n)\\}$, where $y_i \in \\{-1, 1\\}$ and
$\mathbf{x}_i$ are vectors (usually normalized). 

A hyperplane can be defined by
\\[
\begin{equation}
\mathbf{w}^T\mathbf{x} - b = 0 \tag{0}\label{0}
\end{equation}
\\]

![svm_0]({{ site.baseurl }}/assets/img/notes/svm.png)

where $\mathbf{w}$ is the normal vector to the hyperplane. $\frac{b}{\Arrowvert \mathbf{w} \Arrowvert}$ is the distance from the origin to the hyperplane
(proof: $\mathbf{z} = (x_{10}, x_{20})$, $d = proj_{\mathbf{w}}\mathbf{z} = \frac{\mathbf{w} \cdot \mathbf{z}}{\Arrowvert \mathbf{w} \Arrowvert} = \frac{b}{\Arrowvert \mathbf{w} \Arrowvert}$).


#### Linearly separable data (hard-margin)
To find optimal separating hyperplane we can select to parallel hyperplanes that separate two categories,
so that the distance between them as large as possible
\\[
\begin{split}
\mathbf{w}^T \mathbf{x} - b &= 1 \\\\\\
\mathbf{w}^T \mathbf{x} - b &= -1
\end{split} \tag{1}\label{eq1}
\\]

The distance between these two hyperplane is $\frac{2}{\Arrowvert \mathbf{w} \Arrowvert}$.

(proof: $d = proj_{\mathbf{w}}\mathbf{c} = \frac{\mathbf{w} \cdot \mathbf{c}}{\Arrowvert \mathbf{w} \Arrowvert} = \frac{(\mathbf{B} - \mathbf{A})\cdot \mathbf{w}}{\Arrowvert \mathbf{w} \Arrowvert} = \frac{(\mathbf{B}\mathbf{w} - \mathbf{A}\mathbf{w})}{\Arrowvert \mathbf{w} \Arrowvert} = \frac{b+1 -b+1}{\Arrowvert \mathbf{w} \Arrowvert} = \frac{2}{\Arrowvert \mathbf{w} \Arrowvert}$)

Now we can define an optimization problem to find optimal margin classifier:

\\[
\begin{split}
&\Arrowvert \mathbf{w} \Arrowvert \rightarrow min \\\\\\
&y(\mathbf{w}^T \mathbf{x}-b) \geqslant 1
\end{split} \tag{2}\label{eq2}
\\]

####  Linearly inseparable data (soft-margin)

### Nonlinear classification. Kernel trick