---
layout: note
cdate: "Dec 19, 2019"
title: "Problem solving approach: stack and queue"
category: 'Algorithms'
index: 1
headline: 
---

In this note I wanted to collect some interesting problems from leetcode
which can be solved using stack.

<br>
#### [739. Daily Temperatures (leetcode)](https://leetcode.com/problems/daily-temperatures/)

Given a list of daily temperatures $T$, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures $T = [73, 74, 75, 71, 69, 72, 76, 73]$, your output should be $[1, 1, 4, 2, 1, 1, 0, 0]$.

Note: The length of temperatures will be in the range $[1, 30000]$. Each temperature will be an integer in the range $[30, 100]$.

{% highlight cpp %}
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& t) {
        std::vector<int> ret(t.size(), 0);
        std::stack<int> stk;
        for (int i = 0; i < t.size(); i++)
        {
            while (!stk.empty() && t[stk.top()] < t[i])
            {
                int prev = stk.top();
                ret[prev] = i - prev;
                stk.pop();
            }
            stk.push(i);
        }
        return ret;
    }
};
{% endhighlight %}

<br>
#### Links
