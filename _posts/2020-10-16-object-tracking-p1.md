---
layout: post
title: Object Tracking [Part I]
subtitle : Realtime object tracking algorithms
tags: [CV]
author: Arthur
comments : False
---


#### 1. SORT: Simple online and realtime tracking ([link](http://cs231n.github.io/convolutional-networks/#convert))

The idea is super easy to understand.

We need
1. **Object detector** framework (YOLO, SSD, Faster RCNN etc.)

2. **Object motion model**.
The authors approximate the inter-frame displacements of
each object with a linear constant velocity model. The state of each target is modeled as
\\[
\begin{equation}
x_k = \[u, v, s, r, \dot{u}, \dot{v}, \dot{s}\]
\end{equation}
\\]
where $u$ and $v$ represent the horizontal and vertical pixel location of the centre of the target, 
while the scale $s$ and $r$ represent the scale (area) and the aspect ratio of the target’s bounding box respectively.

Kalman filter is used to correct velocity components.

3. **The way to assign detections to existing targets**
The problem of assigning detected bounding boxes to existing objects is solved as linear assignment 
problem using the [Hungarian algorithm](https://en.wikipedia.org/wiki/Hungarian_algorithm).



<br>
#### Links

1. [Simple online and realtime tracking](https://arxiv.org/pdf/1602.00763.pdf)




