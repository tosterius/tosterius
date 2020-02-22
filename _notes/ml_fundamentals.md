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

#### Mean Average Precision (mAP)

_mAP_ is popular metric in object detection and instance segmentation problems.

_Average Precision is the area under precision-recall curve. To get multiple precision-recall
pairs in case of instance segmentation and object detection IoU is calculated using different thresholds.
mAP is just AP values averaged over different categories.


<br>
#### Links

- [The Confusing Metrics of AP and mAP for Object Detection](https://mc.ai/the-confusing-metrics-of-ap-and-map-for-object-detection/)
