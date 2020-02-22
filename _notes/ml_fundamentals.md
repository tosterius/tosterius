---
layout: note
title: Fundamentals
category: ML
index: 0
headline:
picture:
---
#### Confusion matrix. Accuracy, Recall(Sensitivity), Specificity

![confusion_matrix]({{ site.baseurl }}/assets/img/notes/confusion_matrix.png)

\begin{equation}
Accuracy = \frac{Tp + Tn}{P + N}
\end{equation}

\begin{equation}
Precision = \frac{Tp}{Tp + Fp}
\end{equation}

\begin{equation}
Recall = TruePositiveRate = Sensitivity = \frac{Tp}{Tp + Fn}
\end{equation}

\begin{equation}
Specificity = \frac{Tn}{Tn + Fp}
\end{equation}

\begin{equation}
FalsePositiveRate = 1 - Specificity = \frac{Fp}{Tn + Fp}
\end{equation}

#### ROC, AUC

![roc_auc]({{ site.baseurl }}/assets/img/notes/roc_auc.png)

Here is an example how Logistic Regression curve. Changing the threshold
leads to different Confusion Matrices and respectively to different FPR and TPR.


<br>
#### Links

- [Implementing Decision Tree From Scratch in Python](https://medium.com/@penggongting/implementing-decision-tree-from-scratch-in-python-c732e7c69aea)

- [Decision Tree Flavors: Gini Index and Information Gain](http://www.learnbymarketing.com/481/decision-tree-flavors-gini-info-gain/)