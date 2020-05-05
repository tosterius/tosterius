---
layout: note
title: Fundamentals
category: ML
index: 0
headline:
picture:
---

### Classification metrics
#### Confusion matrix

![confusion_matrix]({{ site.baseurl }}/assets/img/notes/confusion_matrix.png)

### Accuracy, Recall(Sensitivity), Specificity
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


#### F1

\begin{equation}
F_1 =\frac{2}{precision^{-1} + recall^{-1}} = 2 \frac{precision \; recall}{precision + recall}
\end{equation}

#### $F_\beta$ in case of different ratio of precision and recall

\begin{equation}
F_\beta = (1 + \beta^2) \frac{precision \; recall}{\beta^2 precision + recall}
\end{equation}

#### ROC, AUC

![roc_auc]({{ site.baseurl }}/assets/img/notes/roc_auc.png)

Here is an example how Logistic Regression curve. Changing the threshold
leads to different Confusion Matrices and respectively to different FPR and TPR.

#### Mean Average Precision (mAP)

_mAP_ is popular metric in object detection and instance segmentation problems.

_Average Precision_ is the area under precision-recall curve. To get multiple precision-recall
pairs in case of instance segmentation and object detection IoU is calculated using different thresholds.
mAP is AP values averaged over different categories.


<br>
#### Links

- [The Confusing Metrics of AP and mAP for Object Detection](https://mc.ai/the-confusing-metrics-of-ap-and-map-for-object-detection/)
