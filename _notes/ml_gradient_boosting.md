---
layout: note
title: Gradient Boosting Machine
category: ML
index: 7
headline:
picture:
---

- gradient boosting (GB) is an ensembling technique that gradually moves an approximate model to
a good model, by adding _weak models_ to composite model
- GB itself does not specify how to choose the weak models, but in practice almost always Decision Trees are used
- GB adds one weak model at a time
- each next weak model is designed to reconstruct the residual 

<br>
#### Gradient boosting for Regression

We are given a $n$-element data set $\{(x_i, y_i)\}, i = 0 \dots n$ and differentiable loss function $L(y_i, F(x_i))$.
$F_m$ is some imperfect model at the stage $m$.

1. Let $F_0(X)$ be value $\gamma$ minimizing $L(y_i, \gamma)$ across all observations:
\\[
\begin{equation}
F_0(X) = \arg\min_{\gamma}\sum_{i=1}^{n} L(y_i, \gamma)
\end{equation}
\\]
If our loss function is SSR then $\gamma$ is just the mean of $y_1,\dots y_n$.

2. For $m = 1 \dots M $:
    1. Compute the 
    \\[
    \begin{equation}
    r_{im} = -\left[\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}\right]\_{F(x)=F_{m-1}(x)}, i = 1\dots n
    \end{equation}
    \\]
    where $r_{im}$ is _pseudo_ residuals

    2. Fit the regression tree to predict the residuals $r_{im}$ giving terminal regions $R_{jm}, j=1 \dots J_m$,
    where $j$ is the index for each leaf in the tree

    3. For $j = 1 \dots J_m$ compute
    \\[
    \begin{equation}
    \gamma_{jm} = \arg\min_{\gamma} \sum_{x_i \in R_{jm}} L(y_i, f_{m-1}(x_i) + \gamma)
    \end{equation}
    \\]
    4. Update
    \\[
    \begin{equation}
    F_m(x) = F_{m-1}(x) + \sum_{j=1}^{J_m} \gamma_{jm}I(x \in R_{jm})
    \end{equation}
    \\]
3. Output $F(x) = F_M(x)$


<br>
#### Links

- [The Elements of Statistical Learning. 2nd Edition by Trevor Hastie, Robert Tibshirani, Jerome Friedman](https://web.stanford.edu/~hastie/Papers/ESLII.pdf)
- [Gradient boosting](https://explained.ai/gradient-boosting)
- [Complete Guide to Parameter Tuning in XGBoost with codes in Python](https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/)
- [Tune Learning Rate for Gradient Boosting with XGBoost in Python](https://machinelearningmastery.com/tune-learning-rate-for-gradient-boosting-with-xgboost-in-python/)
- [Gradient Boost Part 2: Regression Details](https://www.youtube.com/watch?v=2xudPOBz-vs&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF&index=45)
