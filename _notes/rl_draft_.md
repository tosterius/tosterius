---
layout: note
cdate: "Dec 9, 2020"
cdate: "Dec 9, 2020"
title: "Notes on RL"
category: RL
index: 0
headline: 
picture: 
---

### Decision Process

- Markov assumption: 
\\[
\begin{equation}
P(s_{t + 1} \| s_t, a_t, s_{t-1}, a_{t-1}) = P(s_{t+1}\|s_t, a_t),
\end{equation}
\\]
where $s \in S$ - environment states, $a \in A$ - agent actions, $r \in R$ - rewards.

- Total reward $R=\sum_t r_t$ , agent's policy: $\pi(a\|s) = P(\text{take action a}\|\text{in state s})$

- The problem is to find the policy maximizing reward:
\\[
\begin{equation}
\pi(a\|s): E_{\pi}\[R\] \rightarrow max
\end{equation}
\\]