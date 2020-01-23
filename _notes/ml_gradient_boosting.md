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

1. Let $F_0(X)$ be value $\nu$ minimizing $L(y_i, \nu)$ across all observations
2. For $m = 1 \dots M $:
    1. Compute the 
    \\[
    \begin{equation}
    r_{im} = -\left[\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}\right], \; F(x)=F_{m-1}(x)
    \end{equation}
    \\]

<br>
#### Links

- [Gradient boosting](https://explained.ai/gradient-boosting)
- [Complete Guide to Parameter Tuning in XGBoost with codes in Python](https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/)
- [Tune Learning Rate for Gradient Boosting with XGBoost in Python](https://machinelearningmastery.com/tune-learning-rate-for-gradient-boosting-with-xgboost-in-python/)
