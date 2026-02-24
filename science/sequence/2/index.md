# 数列提高 {#_1}

## 线性递推 {#_2}

### 概念 {#_3}

对于 []{.arithmatex}$k$ 阶线性递推式，[]{.arithmatex}$a_n$ 仅与 []{.arithmatex}$n$ 前面的 []{.arithmatex}$k$ 项有关。

对于常系数齐次线性递推，形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a_n=\sum\_{i=1}\^kf_i\times a\_{n-i}}
:::

$$\boxed{a_n=\sum_{i=1}^kf_i\times a_{n-i}}$$
::::

拓展：对于常系数非齐次线性递推，形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=P(n)+\sum\_{i=1}\^kf_i\times a\_{n-i}
:::

$$a_n=P(n)+\sum_{i=1}^kf_i\times a_{n-i}$$
::::

其中 []{.arithmatex}$P(x)$ 是一个 []{.arithmatex}$m$ 次多项式。

### 特征方程 {#_4}

形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=xa\_{n-1}+ya\_{n-2}
:::

$$a_n=xa_{n-1}+ya_{n-2}$$
::::

其特征方程可以表示为，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{q\^2=xq+y}\\ q\^2-xq-y=0
:::

$$\boxed{q^2=xq+y}\\
q^2-xq-y=0$$
::::

推导：

设有 []{.arithmatex}$q,t$ 满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n-qa\_{n-1}=t(a\_{n-1}-qa\_{n-2})\\ a_n=(q+t)a\_{n-1}-qta\_{n-2}
:::

$$a_n-qa_{n-1}=t(a_{n-1}-qa_{n-2})\\
a_n=(q+t)a_{n-1}-qta_{n-2}$$
::::

则，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} x=q+t\\ y=-qt \end{cases}
:::

$$\begin{cases}
x=q+t\\
y=-qt
\end{cases}$$
::::

得，

:::: {.arithmatex}
::: {.MathJax_Preview}
q=x-t=x+y/q\\ t=x-q=-y/q\\ q\^2=xq+y
:::

$$q=x-t=x+y/q\\
t=x-q=-y/q\\
q^2=xq+y$$
::::

或者用微分方程的思想，

:::: {.arithmatex}
::: {.MathJax_Preview}
q\^n=xa\^{n-1}+ya\^{n-2}
:::

$$q^n=xa^{n-1}+ya^{n-2}$$
::::

注意到 []{.arithmatex}$a^{n-2}\neq0$，化简得，

:::: {.arithmatex}
::: {.MathJax_Preview}
q\^2=xq+y
:::

$$q^2=xq+y$$
::::

易解得，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{q\_{1,2}={x\pm\sqrt{x\^2+4y}\over2}}
:::

$$\boxed{q_{1,2}={x\pm\sqrt{x^2+4y}\over2}}$$
::::

其中，[]{.arithmatex}$q_{1,2}$ 称为原线性递推式的特征根。

拓展到高阶线性递推式，对于，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\sum\_{i=1}\^kf_i\times a\_{n-i}
:::

$$a_n=\sum_{i=1}^kf_i\times a_{n-i}$$
::::

其特征方程为，

:::: {.arithmatex}
::: {.MathJax_Preview}
q\^k=\sum\_{i=1}\^kf_i\times q\^{k-i}
:::

$$q^k=\sum_{i=1}^kf_i\times q^{k-i}$$
::::

### 通项公式 {#_5}

我们记递推式

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=xa\_{n-1}+y\_{n-2}
:::

$$a_n=xa_{n-1}+y_{n-2}$$
::::

的两个特征根分别为，[]{.arithmatex}$q_1,q_2$，那么

通项公式，[]{.arithmatex}$a_n$ 一定可以表示为，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a_n=\alpha q_1\^n+\beta q_2\^n}
:::

$$\boxed{a_n=\alpha q_1^n+\beta q_2^n}$$
::::

特殊的，如果 []{.arithmatex}$q_1=q_2=q$，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=(\alpha+\beta)q\^n
:::

$$a_n=(\alpha+\beta)q^n$$
::::

其中，还可以进一步表示，

:::: {.arithmatex}
::: {.MathJax_Preview}
\alpha+\beta=\lambda n+\mu
:::

$$\alpha+\beta=\lambda n+\mu$$
::::

带入原式，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a_n=(\lambda n+\mu)q\^n}
:::

$$\boxed{a_n=(\lambda n+\mu)q^n}$$
::::

对于更高阶的，把 []{.arithmatex}$n$ 前面多加几项 []{.arithmatex}$n^2,n^3,\dots$ 即可。

特殊的，若，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_2/a_1=q
:::

$$a_2/a_1=q$$
::::

那么，原式继续退化，形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a_n=kq\^n}
:::

$$\boxed{a_n=kq^n}$$
::::

可以根据上面的结论，将一个常系数齐次线性递推式，直接化为等差、等比数列。

同时，容易发现 []{.arithmatex}$k_1,k_2$ 一定对于任意 []{.arithmatex}$n$ 成立，因此带入特殊值，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\begin{aligned} a_1=\alpha q_1+\beta q_2\\ a_2=\alpha q_1\^2+\beta q_2\^2 \end{aligned}}
:::

$$\boxed{\begin{aligned}
a_1=\alpha q_1+\beta q_2\\
a_2=\alpha q_1^2+\beta q_2^2
\end{aligned}}$$
::::

容易发现，只有 []{.arithmatex}$k_1,k_2$ 为未知量，可以直接解出来，得到通项公式。

拓展到高阶，理论类似，实际难算。

### 基础例题 {#_6}

#### 例题一：斐波那契数列 {#_7}

有递推式，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} a_1=a_2=1\\ a_n=a\_{n-1}+a\_{n-2}\\(n\>2) \end{cases}
:::

$$\begin{cases}
a_1=a_2=1\\
a_n=a_{n-1}+a_{n-2}\;(n>2)
\end{cases}$$
::::

有特征方程，

:::: {.arithmatex}
::: {.MathJax_Preview}
q\^2=q+1
:::

$$q^2=q+1$$
::::

解得，

:::: {.arithmatex}
::: {.MathJax_Preview}
q\_{1,2}={1\pm\sqrt5\over2}
:::

$$q_{1,2}={1\pm\sqrt5\over2}$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\lambda_1\left({1+\sqrt5\over2}\right)\^n+\lambda_2\left({1-\sqrt5\over2}\right)\^n
:::

$$a_n=\lambda_1\left({1+\sqrt5\over2}\right)^n+\lambda_2\left({1-\sqrt5\over2}\right)^n$$
::::

带入 []{.arithmatex}$a_1=a_2=1$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\qa#1{{a#1\sqrt5\over2}} \begin{aligned} a_1&=\lambda_1\qa++\lambda_2\qa-\\ a_2&=\lambda_1\left(\qa+\right)\^2+\lambda_2\left(\qa-\right)\^2 \end{aligned}
:::

$$\def\qa#1{{a#1\sqrt5\over2}}
\begin{aligned}
a_1&=\lambda_1\qa++\lambda_2\qa-\\
a_2&=\lambda_1\left(\qa+\right)^2+\lambda_2\left(\qa-\right)^2
\end{aligned}$$
::::

解得，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \lambda_1&={1\over\sqrt5}\\ \lambda_2&=-{1\over\sqrt5} \end{aligned}
:::

$$\begin{aligned}
\lambda_1&={1\over\sqrt5}\\
\lambda_2&=-{1\over\sqrt5}
\end{aligned}$$
::::

即，斐波那契数列通项公式，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a_n={1\over\sqrt5}\left\[\left({1+\sqrt5\over2}\right)\^n-\left({1-\sqrt5\over2}\right)\^n\right\]}
:::

$$\boxed{a_n={1\over\sqrt5}\left[\left({1+\sqrt5\over2}\right)^n-\left({1-\sqrt5\over2}\right)^n\right]}$$
::::

同时，我们有更简便的方法，考虑到，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\lambda_1q_1\^n+\lambda_2q_2\^n
:::

$$a_n=\lambda_1q_1^n+\lambda_2q_2^n$$
::::

也可以表示为，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\lambda_1q_1\^{n-1}+\lambda_2q_2\^{n-1}
:::

$$a_n=\lambda_1q_1^{n-1}+\lambda_2q_2^{n-1}$$
::::

于是，我们带入 []{.arithmatex}$a_1,a_2$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} a_1=\lambda_1+\lambda_2\\ a_2=\lambda_1q_1+\lambda_2q_2 \end{cases}
:::

$$\begin{cases}
a_1=\lambda_1+\lambda_2\\
a_2=\lambda_1q_1+\lambda_2q_2
\end{cases}$$
::::

会更方便解方程一点。

本题中，

:::: {.arithmatex}
::: {.MathJax_Preview}
\left\\\begin{aligned} \lambda_1+\lambda_2&=1\\ \lambda_1{1+\sqrt5\over2}+\lambda_2{1-\sqrt5\over2}&=1 \end{aligned}\right.
:::

$$\left\{\begin{aligned}
\lambda_1+\lambda_2&=1\\
\lambda_1{1+\sqrt5\over2}+\lambda_2{1-\sqrt5\over2}&=1
\end{aligned}\right.$$
::::

解得，

:::: {.arithmatex}
::: {.MathJax_Preview}
\left\\\begin{aligned} \lambda_1&={1+\sqrt5\over2\sqrt5}\\ \lambda_2&=-{1-\sqrt5\over2\sqrt5} \end{aligned}\right.
:::

$$\left\{\begin{aligned}
\lambda_1&={1+\sqrt5\over2\sqrt5}\\
\lambda_2&=-{1-\sqrt5\over2\sqrt5}
\end{aligned}\right.$$
::::

得，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} a_n&={1+\sqrt5\over2\sqrt5}\left({1+\sqrt5\over2}\right)\^{n-1}-{1-\sqrt5\over2\sqrt5}\left({1-\sqrt5\over2}\right)\^{n-1}\\ &={1\over\sqrt5}\left\[\left({1+\sqrt5\over2}\right)\^n-\left({1-\sqrt5\over2}\right)\^n\right\] \end{aligned}
:::

$$\begin{aligned}
a_n&={1+\sqrt5\over2\sqrt5}\left({1+\sqrt5\over2}\right)^{n-1}-{1-\sqrt5\over2\sqrt5}\left({1-\sqrt5\over2}\right)^{n-1}\\
&={1\over\sqrt5}\left[\left({1+\sqrt5\over2}\right)^n-\left({1-\sqrt5\over2}\right)^n\right]
\end{aligned}$$
::::

#### 例题二 {#_8}

求：

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}=3a_n-2a\_{n-1}
:::

$$a_{n+1}=3a_n-2a_{n-1}$$
::::

对于任意 []{.arithmatex}$a_1,a_2$ 的通项公式。

容易发现，这是一个二阶的常系数齐次线性递推式，考虑求出特征根，

:::: {.arithmatex}
::: {.MathJax_Preview}
q\^2=3q-2\\ q_1=1,q_2=2
:::

$$q^2=3q-2\\
q_1=1,q_2=2$$
::::

于是，有

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=x+y\cdot2\^n
:::

$$a_n=x+y\cdot2^n$$
::::

对于，解方程

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} a_1=x+2y\\ a_2=x+4y \end{cases}
:::

$$\begin{cases}
a_1=x+2y\\
a_2=x+4y
\end{cases}$$
::::

解得，

:::: {.arithmatex}
::: {.MathJax_Preview}
\left\\\begin{aligned} x&=2a_1-a_2\\ y&={a_2-a_1\over2} \end{aligned}\right.
:::

$$\left\{\begin{aligned}
x&=2a_1-a_2\\
y&={a_2-a_1\over2}
\end{aligned}\right.$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=2a_1-a_2+(a_2-a_1)2\^{n-1}
:::

$$a_n=2a_1-a_2+(a_2-a_1)2^{n-1}$$
::::

#### 例题三 {#_9}

求：

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}=6a_n-9a\_{n-1}
:::

$$a_{n+1}=6a_n-9a_{n-1}$$
::::

对于任意 []{.arithmatex}$a_1,a_2$ 的通项公式。

容易发现，这是一个二阶的常系数齐次线性递推式，考虑求出特征根，

:::: {.arithmatex}
::: {.MathJax_Preview}
q\^2=6q-9\\ q_1=q_2=3
:::

$$q^2=6q-9\\
q_1=q_2=3$$
::::

于是，有，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=(xn+y)3\^n
:::

$$a_n=(xn+y)3^n$$
::::

带入，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} a_1&=3x+3y\\ a_2&=18x+9y \end{aligned}
:::

$$\begin{aligned}
a_1&=3x+3y\\
a_2&=18x+9y
\end{aligned}$$
::::

那么，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} x&={a_2-3a_1\over9}\\ y&={6a_1-a_2\over9} \end{aligned}
:::

$$\begin{aligned}
x&={a_2-3a_1\over9}\\
y&={6a_1-a_2\over9}
\end{aligned}$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\[(a_2-3a_1)n+6a_1-a_2\]3\^{n-2}
:::

$$a_n=[(a_2-3a_1)n+6a_1-a_2]3^{n-2}$$
::::

#### 例题四 {#_10}

对于，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=4a\_{n-1}-3a\_{n-2}+1,a_1=1,a_2=2
:::

$$a_n=4a_{n-1}-3a_{n-2}+1,a_1=1,a_2=2$$
::::

注意到特征方程

:::: {.arithmatex}
::: {.MathJax_Preview}
x\^2=4x-3
:::

$$x^2=4x-3$$
::::

其特征根为，

:::: {.arithmatex}
::: {.MathJax_Preview}
x_1=1,x_2=3
:::

$$x_1=1,x_2=3$$
::::

我们考虑最原始的算法，两边同时减去 []{.arithmatex}$3a_{n-1}$，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n-3a\_{n-1}=a\_{n-1}-3a\_{n-2}+1
:::

$$a_n-3a_{n-1}=a_{n-1}-3a_{n-2}+1$$
::::

设，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=a_n-3a\_{n-1}
:::

$$b_n=a_n-3a_{n-1}$$
::::

则，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=b\_{n-1}+1,b_2=a_2-3a_1=-1
:::

$$b_n=b_{n-1}+1,b_2=a_2-3a_1=-1$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=n-3
:::

$$b_n=n-3$$
::::

则，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=3a\_{n-1}+n+3
:::

$$a_n=3a_{n-1}+n+3$$
::::

两边同时除以 []{.arithmatex}$3^n$ 即可，暴力求解即可。

但是还有更方便的算法，注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=4a\_{n-1}-3a\_{n-2}+1\\ a\_{n+1}=4a_n-3a\_{n-1}+1
:::

$$a_n=4a_{n-1}-3a_{n-2}+1\\
a_{n+1}=4a_n-3a_{n-1}+1$$
::::

下式减上式，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}-a_n=4a_n-3a\_{n-1}-4a\_{n-1}+3a\_{n-2}
:::

$$a_{n+1}-a_n=4a_n-3a_{n-1}-4a_{n-1}+3a_{n-2}$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}=5a_n-7a\_{n-1}+3a\_{n-2}
:::

$$a_{n+1}=5a_n-7a_{n-1}+3a_{n-2}$$
::::

于是，我们把一个非齐次的递推式，转化为了一个齐次的，特征根

:::: {.arithmatex}
::: {.MathJax_Preview}
q\^3=5q\^2-7q+3
:::

$$q^3=5q^2-7q+3$$
::::

首先，注意到 []{.arithmatex}$q=1$ 为一个可行解，于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
q\^3-5q\^2+7q-3=(q-1)(q\^2-4q+3)=(q-1)\^2(q-3)=0
:::

$$q^3-5q^2+7q-3=(q-1)(q^2-4q+3)=(q-1)^2(q-3)=0$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
q_1=q_2=1,q_3=3
:::

$$q_1=q_2=1,q_3=3$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\beta3\^{n-1}+\lambda n+\mu
:::

$$a_n=\beta3^{n-1}+\lambda n+\mu$$
::::

根据原递推式，得出，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_3=4a_2-3a_1+1=6
:::

$$a_3=4a_2-3a_1+1=6$$
::::

于是，列出方程，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} 1=\beta+\lambda+\mu\\ 2=3\beta+2\lambda+\mu\\ 6=9\beta+3\lambda+\mu \end{cases}
:::

$$\begin{cases}
1=\beta+\lambda+\mu\\
2=3\beta+2\lambda+\mu\\
6=9\beta+3\lambda+\mu
\end{cases}$$
::::

考虑解方程，具体的，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} 2\beta+\lambda=1\\ 6\beta+\lambda=4 \end{cases}
:::

$$\begin{cases}
2\beta+\lambda=1\\
6\beta+\lambda=4
\end{cases}$$
::::

解得，

:::: {.arithmatex}
::: {.MathJax_Preview}
\left\\\begin{aligned} \beta={3\over4}\\ \lambda=-{1\over2}\\ \mu={3\over4} \end{aligned}\right.
:::

$$\left\{\begin{aligned}
\beta={3\over4}\\
\lambda=-{1\over2}\\
\mu={3\over4}
\end{aligned}\right.$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n={3\^n\over4}-{1\over2}n+{3\over4}
:::

$$a_n={3^n\over4}-{1\over2}n+{3\over4}$$
::::

经检验，[]{.arithmatex}$a_1=1,a_2=2,a_3=6$​，符合题意，故，略。

类似，若特征方程无解，那么数列为一个周期数列，手模即可。

注意到，利用这个低阶化为高阶的方法，可以避免很多前面的题中类似的大量计算。

对于这一类的问题，我们把各种变形，转化为只需要解特征方程就可以的问题。

#### 例题五 {#_11}

求通项公式，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}=4a_n-3a\_{n-1}+n\\(n\ge2),a_1=1,a_2=2
:::

$$a_{n+1}=4a_n-3a_{n-1}+n\,(n\ge2),a_1=1,a_2=2$$
::::

考虑和上一题类似的做法，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=4a\_{n-1}-3a\_{n-2}+n-1
:::

$$a_n=4a_{n-1}-3a_{n-2}+n-1$$
::::

上式减下式，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}=5a_n-7a\_{n-1}+3a\_{n-2}+1
:::

$$a_{n+1}=5a_n-7a_{n-1}+3a_{n-2}+1$$
::::

继续运用上一题的思路，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=5a\_{n-1}-7a\_{n-2}+3a\_{n-3}+1
:::

$$a_n=5a_{n-1}-7a_{n-2}+3a_{n-3}+1$$
::::

上式减下式，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}=6a_n-12a\_{n-1}+10a\_{n-2}-3a\_{n-3}
:::

$$a_{n+1}=6a_n-12a_{n-1}+10a_{n-2}-3a_{n-3}$$
::::

解出特征方程，

:::: {.arithmatex}
::: {.MathJax_Preview}
q_1=q_2=q_3=1,q_4=3
:::

$$q_1=q_2=q_3=1,q_4=3$$
::::

设通项公式，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=a3\^{n-1}+b(n-1)\^2+c(n-1)+d
:::

$$a_n=a3^{n-1}+b(n-1)^2+c(n-1)+d$$
::::

带入即可，步骤略。

#### 例题六 {#_12}

已知数列 []{.arithmatex}$\{a\},\{b\}$ 满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=2,b_1=1\\ \begin{aligned} a\_{n+1}&=5a_n+3b_n+7\\ b\_{n+1}&=3a_n+5b_n \end{aligned}
:::

$$a_1=2,b_1=1\\
\begin{aligned}
a_{n+1}&=5a_n+3b_n+7\\
b_{n+1}&=3a_n+5b_n
\end{aligned}$$
::::

对于 []{.arithmatex}$n\in\mathbb N$，求 []{.arithmatex}$\{a\}$ 解析式。

容易发现，我们可以利用上式，用 []{.arithmatex}$a_{n+1},a_n$ 表示 []{.arithmatex}$b_n$。

然后带入下式，即可求得 []{.arithmatex}$a_n$ 的递推公式。

但是这么做很复杂，考虑原递推公式有什么优秀的结构。

容易发现，[]{.arithmatex}$5,3,3,5$ 存在有一种优美的形态，

于是，考虑两式做和、做差。

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} a\_{n+1}+b\_{n+1}=8a_n+8b_n+7\\ a\_{n+1}-b\_{n+1}=2a_n-2b_n+7 \end{cases}
:::

$$\begin{cases}
a_{n+1}+b_{n+1}=8a_n+8b_n+7\\
a_{n+1}-b_{n+1}=2a_n-2b_n+7
\end{cases}$$
::::

设，

:::: {.arithmatex}
::: {.MathJax_Preview}
c_n=a_n+b_n\\ d_n=a_n-b_n
:::

$$c_n=a_n+b_n\\
d_n=a_n-b_n$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} c\_{n+1}=8c_n+7\\ d\_{n+1}=2d_n+7 \end{cases}
:::

$$\begin{cases}
c_{n+1}=8c_n+7\\
d_{n+1}=2d_n+7
\end{cases}$$
::::

然后用通用方法，

:::: {.arithmatex}
::: {.MathJax_Preview}
c\_{n+1}+1=8c_n+8=8(c_n+1)\\ c_n=8\^{n-1}(c_1+1)-1=4\times8\^{n-1}-1
:::

$$c_{n+1}+1=8c_n+8=8(c_n+1)\\
c_n=8^{n-1}(c_1+1)-1=4\times8^{n-1}-1$$
::::

同理，

:::: {.arithmatex}
::: {.MathJax_Preview}
d\_{n+1}+7=2d_n+14=2(d_n+7)\\ d_n=2\^{n-1}(d_1+7)-7=8\times2\^{n-1}-7
:::

$$d_{n+1}+7=2d_n+14=2(d_n+7)\\
d_n=2^{n-1}(d_1+7)-7=8\times2^{n-1}-7$$
::::

则，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n={c_n+d_n\over2}=2\times8\^{n-1}+2\^{n+1}-4
:::

$$a_n={c_n+d_n\over2}=2\times8^{n-1}+2^{n+1}-4$$
::::

经检验，[]{.arithmatex}$a_1=2$，符合题意，故，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=2\times8\^{n-1}+2\^{n+1}-4
:::

$$a_n=2\times8^{n-1}+2^{n+1}-4$$
::::

#### 例题七 {#_13}

数列 []{.arithmatex}$\{a\}$ 满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=1,a_2=2,a\_{n+2}=6a\_{n+1}-a_n
:::

$$a_1=1,a_2=2,a_{n+2}=6a_{n+1}-a_n$$
::::

则，下列说法中，正确的是，

A. 数列 []{.arithmatex}$\{a_{n+1}^2-a_na_{n+2}\}$ 是常数数列。

B. 数列 []{.arithmatex}$\{8a_na_{n+1}-7\}$ 的各项为平方数。

C. 数列 []{.arithmatex}$\{4a_na_{n+1}-7\}$​ 的各项为平方数。

D. 任意 []{.arithmatex}$a_n$ 除以 []{.arithmatex}$9$ 的余数为 []{.arithmatex}$1$ 或 []{.arithmatex}$2$。

对于 A 选项，我们递推式两边同时乘上 []{.arithmatex}$a_n$，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_na\_{n+2}=6a_na\_{n+1}-a_n\^2
:::

$$a_na_{n+2}=6a_na_{n+1}-a_n^2$$
::::

则，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}\^2-a_na\_{n+2}=a\_{n+1}\^2+a_n\^2-6a_na\_{n+1}
:::

$$a_{n+1}^2-a_na_{n+2}=a_{n+1}^2+a_n^2-6a_na_{n+1}$$
::::

同理，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n\^2-a\_{n-1}a\_{n+1}=a_n\^2+a\_{n-1}\^2-6a\_{n-1}a_n
:::

$$a_n^2-a_{n-1}a_{n+1}=a_n^2+a_{n-1}^2-6a_{n-1}a_n$$
::::

两式右面相等，则，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}\^2-6a_na\_{n+1}=a\_{n-1}\^2-6a\_{n-1}a_n\\ a\_{n+1}(a\_{n+1}-6a_n)=a\_{n-1}(a\_{n-1}-6a_n)\\ -a\_{n+1}a\_{n-1}=-a\_{n-1}a\_{n+1}
:::

$$a_{n+1}^2-6a_na_{n+1}=a_{n-1}^2-6a_{n-1}a_n\\
a_{n+1}(a_{n+1}-6a_n)=a_{n-1}(a_{n-1}-6a_n)\\
-a_{n+1}a_{n-1}=-a_{n-1}a_{n+1}$$
::::

显然成立，因此，数列

:::: {.arithmatex}
::: {.MathJax_Preview}
\\a\_{n+1}\^2-a_na\_{n+2}\\
:::

$$\{a_{n+1}^2-a_na_{n+2}\}$$
::::

是常数数列。

对于 D 选项，容易发现，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1\equiv1\pmod 9\\ a_2\equiv2\pmod 9\\ a_3\equiv2\pmod 9\\ a_4\equiv1\pmod 9\\ a_5\equiv4\pmod 9
:::

$$a_1\equiv1\pmod 9\\
a_2\equiv2\pmod 9\\
a_3\equiv2\pmod 9\\
a_4\equiv1\pmod 9\\
a_5\equiv4\pmod 9$$
::::

在 []{.arithmatex}$a_5$ 出现问题，故命题不成立。

对于 BC 选项，由 A 选项知，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}\^2-a_na\_{n+2}=a\_{n+1}\^2+a_n\^2-6a_na\_{n+1}=-7
:::

$$a_{n+1}^2-a_na_{n+2}=a_{n+1}^2+a_n^2-6a_na_{n+1}=-7$$
::::

则，

:::: {.arithmatex}
::: {.MathJax_Preview}
6a_na\_{n+1}-7=a\_{n+1}\^2+a_n\^2
:::

$$6a_na_{n+1}-7=a_{n+1}^2+a_n^2$$
::::

两边同时，

:::: {.arithmatex}
::: {.MathJax_Preview}
\pm2a_na\_{n+1}
:::

$$\pm2a_na_{n+1}$$
::::

都可以使右边变为平方数，因此 BC 均成立。

故选：ABC。

## 极限 {#_14}

### 函数极限 {#_15}

极限的概念比较复杂，我们多方面的考虑。

若函数 []{.arithmatex}$f(x)$ 在 []{.arithmatex}$x_0$ 附近有定义，且存在有极限 []{.arithmatex}$L$，那么，

对于任意 []{.arithmatex}$\varepsilon>0$，一定存在 []{.arithmatex}$\delta>0$，使得当，

:::: {.arithmatex}
::: {.MathJax_Preview}
0\<\|x-x_0\|\<\delta
:::

$$0<|x-x_0|<\delta$$
::::

时，总有，

:::: {.arithmatex}
::: {.MathJax_Preview}
\|f(x)-L\|\<\varepsilon
:::

$$|f(x)-L|<\varepsilon$$
::::

则称 []{.arithmatex}$L$ 是函数在 []{.arithmatex}$x_0$ 的**极限**，记为，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{x\to x_0}f(x)=L
:::

$$\lim_{x\to x_0}f(x)=L$$
::::

特殊的，若对于 []{.arithmatex}$x>x_0$（[]{.arithmatex}$x-x_0<\delta$）满足上式，

则称函数在 []{.arithmatex}$x_0$​ 处存在**右极限**，表示为：

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{x\to x_0\^+}f(x)=L
:::

$$\lim_{x\to x_0^+}f(x)=L$$
::::

同样的，若对于 []{.arithmatex}$x<x_0$（[]{.arithmatex}$x_0-x<\delta$）满足上式，

则称函数在 []{.arithmatex}$x_0$​ 处存在**左极限**，表示为：

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{x\to x_0\^-}f(x)=L
:::

$$\lim_{x\to x_0^-}f(x)=L$$
::::

比较这三个定义我们会发现：

要想存在极限，那么必须同时存在相等的左极限和右极限。

### 数列极限 {#_16}

数列极限的定义和函数的不大一样，

对于任意 []{.arithmatex}$\varepsilon>0$，都存在 []{.arithmatex}$N\in\mathbb N^*$，使得对于任意 []{.arithmatex}$n>N$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\|a_n-L\|\<\varepsilon
:::

$$|a_n-L|<\varepsilon$$
::::

则称数列 []{.arithmatex}$a$ **收敛于** []{.arithmatex}$L$，记为，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}a_n=L
:::

$$\lim_{n\to\infty}a_n=L$$
::::

或，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n\to a
:::

$$a_n\to a$$
::::

用逻辑符号表示，

:::: {.arithmatex}
::: {.MathJax_Preview}
(\forall\varepsilon\>0)(\exist N\in\mathbb N\^+)(\forall n\in\mathbb N) \[(n\>N)\Rightarrow(\|a_n-L\|\<\varepsilon)\]
:::

$$(\forall\varepsilon>0)(\exist N\in\mathbb N^+)(\forall n\in\mathbb N) [(n>N)\Rightarrow(|a_n-L|<\varepsilon)]$$
::::

直观的讲，即无论误差范围 []{.arithmatex}$\varepsilon$ 多小，从某项 []{.arithmatex}$a_n$ 开始，每一项与 []{.arithmatex}$L$ 的差距都小于 []{.arithmatex}$\varepsilon$​。

或者，更直观的，当数列的下标越来越大的时候，数列的值也就越接近那个特殊值。

若不存在这样的数，则称该数列是**发散**的。

### 常见的极限 {#_17}

从这里开始，一般只讨论数列极限。

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\lim\_{x\to\infty}{1\over x\^n}=0,n\>0}\tag a
:::

$$\boxed{\lim_{x\to\infty}{1\over x^n}=0,n>0}\tag a$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\lim\_{x\to\infty}{1\over a\^n}=0,\|a\|\>1}\tag b
:::

$$\boxed{\lim_{x\to\infty}{1\over a^n}=0,|a|>1}\tag b$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\lim\_{x\to\infty}r\^n=0,\|r\|\<1}\tag c
:::

$$\boxed{\lim_{x\to\infty}r^n=0,|r|<1}\tag c$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\lim\_{x\to0\^+}{1\over x}=+\infty}\tag d
:::

$$\boxed{\lim_{x\to0^+}{1\over x}=+\infty}\tag d$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\lim\_{x\to0\^-}{1\over x}=-\infty}\tag e
:::

$$\boxed{\lim_{x\to0^-}{1\over x}=-\infty}\tag e$$
::::

特殊的，对于数列 []{.arithmatex}$a_n=n$，

当 []{.arithmatex}$n\to+\infty$ 时，[]{.arithmatex}$a_n\to+\infty$，这种**无界数列**，一般说其不存在极限。

同样，除了常数数列，其他的波动数列、周期数列，一般都不存在极限。

其中一个判断数列是否收敛的定理，称为**单调收敛定理**，和实数完备性相关：

单调有界数列必收敛（有上界的单调递增数列，或是有下界的单调递减数列）。

同时，判断数列是否收敛，还存在**两边夹定理**，

若两数列存在极限，那么其夹的数列存在极限，数学表示，

若 []{.arithmatex}$\lim\limits_{n\to\infty}a_n=\lim\limits_{n\to\infty}b_n=L$，且 []{.arithmatex}$a_n\le c_n\le b_n$，则 []{.arithmatex}$\lim\limits_{n\to\infty}c_n=L$​。

例如，

:::: {.arithmatex}
::: {.MathJax_Preview}
0\<{1\over\sqrt{n\^2+1}}\<{1\over n}
:::

$$0<{1\over\sqrt{n^2+1}}<{1\over n}$$
::::

且左右极限都是 []{.arithmatex}$0$，因此中间也收敛于 []{.arithmatex}$0$。

### 极限的性质 {#_18}

**唯一性**：若数列 []{.arithmatex}$\{a_n\}_{n\in\mathbb N}$ 存在极限，则极限是唯一的。

**有界性**：如果一个实数数列无界，则这个实数数列一定发散。

若数列 []{.arithmatex}$\{a_n\}_{n\in\mathbb N}$ 存在极限，那么一定存在 []{.arithmatex}$M>0$，使得所有 []{.arithmatex}$|a_n|\le M$。

注意到，并不是数列有界就一定存在极限，例如 []{.arithmatex}$a_n=(-1)^{n}$。

**保序性**：若两数列 []{.arithmatex}$\{a_n\}_{n\in\mathbb N},\{b_n\}_{n\in\mathbb N}$ 分别收敛于 []{.arithmatex}$A,B$，则，

:::: {.arithmatex}
::: {.MathJax_Preview}
(\exist N\in\mathbb N) \[(A\>B)\wedge(n\>N)\Rightarrow(a_n\>b_n)\]
:::

$$(\exist N\in\mathbb N) [(A>B)\wedge(n>N)\Rightarrow(a_n>b_n)]$$
::::

极限也存在四则运算：

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\lim\_{n\to\infty}(a_n\pm b_n)=\lim\_{n\to\infty}a_n\pm \lim\_{n\to\infty}b_n}\tag1
:::

$$\boxed{\lim_{n\to\infty}(a_n\pm b_n)=\lim_{n\to\infty}a_n\pm \lim_{n\to\infty}b_n}\tag1$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\lim\_{n\to\infty}xa_n=x\lim\_{n\to\infty}a_n}\tag2
:::

$$\boxed{\lim_{n\to\infty}xa_n=x\lim_{n\to\infty}a_n}\tag2$$
::::

由 []{.arithmatex}$(1)(2)$ 可得极限的**线性性**，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\lim\_{n\to\infty}(xa_n+yb_n)=x\lim\_{n\to\infty}a_n+y\lim\_{n\to\infty}b_n}\tag3
:::

$$\boxed{\lim_{n\to\infty}(xa_n+yb_n)=x\lim_{n\to\infty}a_n+y\lim_{n\to\infty}b_n}\tag3$$
::::

另外，极限也存在乘法和除法，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\lim\_{n\to\infty}(a_nb_n)=\lim\_{n\to\infty}a_n\times\lim\_{n\to\infty}b_n}\tag4
:::

$$\boxed{\lim_{n\to\infty}(a_nb_n)=\lim_{n\to\infty}a_n\times\lim_{n\to\infty}b_n}\tag4$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\tag5\boxed{\lim\_{n\to\infty}\left({a_n\over b_n}\right)={\lim\_{n\to\infty}a_n\over\lim\_{n\to\infty}b_n}}
:::

$$\tag5\boxed{\lim_{n\to\infty}\left({a_n\over b_n}\right)={\lim_{n\to\infty}a_n\over\lim_{n\to\infty}b_n}}$$
::::

注意到，被除数不能为零。

同时，如果要进行以上所有操作，都需要保证每一步的数列极限存在。

这样子，有一个性质，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}{a_1x\^{c_1}+a_2x\^{c_2}+\dots\over b_1x\^{c_1}+b_2x\^{c_2}+\dots}={a_1\over b_1},c_1\>c_2\>\dots
:::

$$\lim_{n\to\infty}{a_1x^{c_1}+a_2x^{c_2}+\dots\over b_1x^{c_1}+b_2x^{c_2}+\dots}={a_1\over b_1},c_1>c_2>\dots$$
::::

即，最高次项系数之比。

### 极限例题 {#_19}

#### 存在极限的组 {#_20}

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}{1\over4\^n}=0
:::

$$\lim_{n\to\infty}{1\over4^n}=0$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}{2\over n}+{1\over n\^2}=\lim\_{n\to\infty}{2\over n}+\lim\_{n\to\infty}{1\over n\^2}=0
:::

$$\lim_{n\to\infty}{2\over n}+{1\over n^2}=\lim_{n\to\infty}{2\over n}+\lim_{n\to\infty}{1\over n^2}=0$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}{1\over n}-{2\over n\^2}+3=\lim\_{n\to\infty}{1\over n}-\lim\_{n\to\infty}{2\over n\^2}+3=3
:::

$$\lim_{n\to\infty}{1\over n}-{2\over n^2}+3=\lim_{n\to\infty}{1\over n}-\lim_{n\to\infty}{2\over n^2}+3=3$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}{2+(1/3)\^n\over(1/3)\^n-5}={\lim\_{n\to\infty}2+(1/3)\^n\over\lim\_{n\to\infty}(1/3)\^n-5}={2+\lim\_{n\to\infty}(1/3)\^n\over\lim\_{n\to\infty}(1/3)\^n-5}=-{2\over5}
:::

$$\lim_{n\to\infty}{2+(1/3)^n\over(1/3)^n-5}={\lim_{n\to\infty}2+(1/3)^n\over\lim_{n\to\infty}(1/3)^n-5}={2+\lim_{n\to\infty}(1/3)^n\over\lim_{n\to\infty}(1/3)^n-5}=-{2\over5}$$
::::

注意在做每一步变形的时候，只有存在极限才能操作。

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}{3n+1\over2n+2}={3\over2}
:::

$$\lim_{n\to\infty}{3n+1\over2n+2}={3\over2}$$
::::

这里有很多种做法，例如，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}{3n+1\over2n+2}=\lim\_{n\to\infty}{3+1/n\over2+2/n}={\lim\_{n\to\infty}3+1/n\over\lim\_{n\to\infty}2+2/n}={3\over2}
:::

$$\lim_{n\to\infty}{3n+1\over2n+2}=\lim_{n\to\infty}{3+1/n\over2+2/n}={\lim_{n\to\infty}3+1/n\over\lim_{n\to\infty}2+2/n}={3\over2}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}{3n+1\over2n+2}=\lim\_{n\to\infty}{3(2n+2)/2-2\over2n+2}={3\over2}-\lim\_{n\to\infty}{2\over2n+2}={3\over2}
:::

$$\lim_{n\to\infty}{3n+1\over2n+2}=\lim_{n\to\infty}{3(2n+2)/2-2\over2n+2}={3\over2}-\lim_{n\to\infty}{2\over2n+2}={3\over2}$$
::::

或者，当 []{.arithmatex}$n\to\infty$ 时，

:::: {.arithmatex}
::: {.MathJax_Preview}
3n+1\sim3n,2n+2\sim2n
:::

$$3n+1\sim3n,2n+2\sim2n$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
{3n+1\over2n+2}\to{3n\over2n}={3\over2}
:::

$${3n+1\over2n+2}\to{3n\over2n}={3\over2}$$
::::

#### 不存在极限的组 {#_21}

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\sqrt n
:::

$$a_n=\sqrt n$$
::::

注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
n\to\infty,\sqrt n\to\infty
:::

$$n\to\infty,\sqrt n\to\infty$$
::::

当趋近于正无穷时，一般认为不存在极限。

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=n-{1\over n}
:::

$$a_n=n-{1\over n}$$
::::

注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
n\to\infty,1/n\to0
:::

$$n\to\infty,1/n\to0$$
::::

故，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n\to\infty
:::

$$a_n\to\infty$$
::::

同样不存在极限。

### 例题一 {#_22}

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n={1\over\sqrt{n\^2+n}}
:::

$$a_n={1\over\sqrt{n^2+n}}$$
::::

容易发现，

:::: {.arithmatex}
::: {.MathJax_Preview}
0\<{1\over\sqrt {n\^2+n}}\<{1\over n}
:::

$$0<{1\over\sqrt {n^2+n}}<{1\over n}$$
::::

且，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}{1\over n}=0
:::

$$\lim_{n\to\infty}{1\over n}=0$$
::::

根据两边夹定理，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}{1\over\sqrt{n\^2+n}}=0
:::

$$\lim_{n\to\infty}{1\over\sqrt{n^2+n}}=0$$
::::

#### 例题二 {#_23}

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n={\sin n\over n}
:::

$$a_n={\sin n\over n}$$
::::

容易发现，

:::: {.arithmatex}
::: {.MathJax_Preview}
-{1\over n}\le{\sin n\over n}\le{1\over n}
:::

$$-{1\over n}\le{\sin n\over n}\le{1\over n}$$
::::

且，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}-{1\over n}=\lim\_{n\to\infty}{1\over n}=0
:::

$$\lim_{n\to\infty}-{1\over n}=\lim_{n\to\infty}{1\over n}=0$$
::::

因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}{\sin n\over n}=0
:::

$$\lim_{n\to\infty}{\sin n\over n}=0$$
::::

#### 例题三 {#_24}

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\sqrt\[n\]2
:::

$$a_n=\sqrt[n]2$$
::::

注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sqrt\[n\]2\>0
:::

$$\sqrt[n]2>0$$
::::

而且，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sqrt\[n\]2\>\sqrt\[n+1\]2
:::

$$\sqrt[n]2>\sqrt[n+1]2$$
::::

证明：

:::: {.arithmatex}
::: {.MathJax_Preview}
(\sqrt\[n\]2)\^{n(n+1)}\>(\sqrt\[n+1\]2)\^{n(n+1)}\\ 2\^{n+1}\>2\^n
:::

$$(\sqrt[n]2)^{n(n+1)}>(\sqrt[n+1]2)^{n(n+1)}\\
2^{n+1}>2^n$$
::::

即，递减有下界，有极限。

设，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\sqrt\[n\]2\\ c_n=a_n-1
:::

$$a_n=\sqrt[n]2\\
c_n=a_n-1$$
::::

那么，

:::: {.arithmatex}
::: {.MathJax_Preview}
(c_n+1)\^n=2
:::

$$(c_n+1)^n=2$$
::::

用二项式定理展开，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sum\_{k=0}\^n{n\choose k}c_n\^k=2
:::

$$\sum_{k=0}^n{n\choose k}c_n^k=2$$
::::

展开前两项，

:::: {.arithmatex}
::: {.MathJax_Preview}
1+nc_n\<(c_n+1)\^n=2\\ c_n\<{1\over n}
:::

$$1+nc_n<(c_n+1)^n=2\\
c_n<{1\over n}$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
1\<a_n=c_n+1\<{1\over n}+1
:::

$$1<a_n=c_n+1<{1\over n}+1$$
::::

根据两边夹定理，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}a_n=1
:::

$$\lim_{n\to\infty}a_n=1$$
::::

#### 例题四 {#_25}

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=\sqrt\[n\]n
:::

$$b_n=\sqrt[n]n$$
::::

的极限。

类似上一题的似乎，设，

:::: {.arithmatex}
::: {.MathJax_Preview}
d_n=b_n-1\\ b_n=d_n+1\\ n=(d_n+1)\^n
:::

$$d_n=b_n-1\\
b_n=d_n+1\\
n=(d_n+1)^n$$
::::

展开，

:::: {.arithmatex}
::: {.MathJax_Preview}
1+nd_n+{n(n+1)\over2}d_n\^2+\dots=n
:::

$$1+nd_n+{n(n+1)\over2}d_n^2+\dots=n$$
::::

考虑到右面的 []{.arithmatex}$n$ 级别比较大，我们选用一三两项，

:::: {.arithmatex}
::: {.MathJax_Preview}
n\>1+{n(n+1)\over2}d_n\^2\\ n-1\>{n(n+1)\over2}d_n\^2\\ {n\over2}d_n\^2\<1\\ d_n\^2\<{2\over n}
:::

$$n>1+{n(n+1)\over2}d_n^2\\
n-1>{n(n+1)\over2}d_n^2\\
{n\over2}d_n^2<1\\
d_n^2<{2\over n}$$
::::

又因为，

:::: {.arithmatex}
::: {.MathJax_Preview}
d_n\>1
:::

$$d_n>1$$
::::

两边夹，得出，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}b_n=\lim\_{n\to\infty}d_n+1=1
:::

$$\lim_{n\to\infty}b_n=\lim_{n\to\infty}d_n+1=1$$
::::

#### 例题五：数学直觉做法 {#_26}

有数列，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=1,a\_{n+1}=a_n+{1\over\sqrt\[2n\]{a_n}}
:::

$$a_1=1,a_{n+1}=a_n+{1\over\sqrt[2n]{a_n}}$$
::::

判断 []{.arithmatex}$a$ 是否单调，是否有界。

我们充分发扬人类智慧：

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=1,a_2=2,\dots
:::

$$a_1=1,a_2=2,\dots$$
::::

观察原式，容易得出，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n\neq0,{1\over\sqrt\[2n\]{a_n}}\neq0
:::

$$a_n\neq0,{1\over\sqrt[2n]{a_n}}\neq0$$
::::

那么，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}\>a_n
:::

$$a_{n+1}>a_n$$
::::

而且不取等，那么一定是严格单调递增且无界的。

#### 例题六：初中重造组 {#_27}

求数列，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_0=1+2021\^{-1}\\ a_n=(1+2021\^{-2\^n})a\_{n-1}
:::

$$a_0=1+2021^{-1}\\
a_n=(1+2021^{-2^n})a_{n-1}$$
::::

的极限。

注意到两边取极限，会约去，因此不能不动点法（大雾）。

注意到幂运算的右结合性，

:::: {.arithmatex}
::: {.MathJax_Preview}
2021\^{-2\^n}=(2021\^{-2})\^n=\left({1\over2021}\right)\^{2\^{n}}
:::

$$2021^{-2^n}=(2021^{-2})^n=\left({1\over2021}\right)^{2^{n}}$$
::::

我们记，

:::: {.arithmatex}
::: {.MathJax_Preview}
x=2021\^{-1}
:::

$$x=2021^{-1}$$
::::

那么，原式化简为，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_0=1+x\\ a_n=(1+x\^{2\^n})a\_{n-1}
:::

$$a_0=1+x\\
a_n=(1+x^{2^n})a_{n-1}$$
::::

考虑累乘法，很自然，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=(1+x)(1+x\^2)(1+x\^4)+\dots+(1+x\^{2\^n})
:::

$$a_n=(1+x)(1+x^2)(1+x^4)+\dots+(1+x^{2^n})$$
::::

好好好，我们回归初中出现过的经典探究题，

:::: {.arithmatex}
::: {.MathJax_Preview}
(1-x)(1+x)=1-x\^2\\ (1-x\^2)(1+x\^2)=1-x\^4\\ \dots\\ (1-x\^{2\^n})(1+x\^{2\^n})=1-\left(x\^{2\^n}\right)\^2=1-x\^{2\^n\times2}=1-x\^{2\^{n+1}}
:::

$$(1-x)(1+x)=1-x^2\\
(1-x^2)(1+x^2)=1-x^4\\
\dots\\
(1-x^{2^n})(1+x^{2^n})=1-\left(x^{2^n}\right)^2=1-x^{2^n\times2}=1-x^{2^{n+1}}$$
::::

于是，原式两边同乘 []{.arithmatex}$1-x$，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
(1-x)a_n=1-x\^{2\^{n+1}}\\ a_n={1-x\^{2\^{n+1}}\over1-x}
:::

$$(1-x)a_n=1-x^{2^{n+1}}\\
a_n={1-x^{2^{n+1}}\over1-x}$$
::::

考虑极限，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}a_n={1-\lim\_{n\to\infty}x\^{2\^{n+1}}\over1-x}
:::

$$\lim_{n\to\infty}a_n={1-\lim_{n\to\infty}x^{2^{n+1}}\over1-x}$$
::::

我们知道，

:::: {.arithmatex}
::: {.MathJax_Preview}
n\to\infty\Rightarrow2\^{n+1}\to\infty\Rightarrow x\^{2\^{n+1}}\to0,\because\|x\|\<1
:::

$$n\to\infty\Rightarrow2^{n+1}\to\infty\Rightarrow x^{2^{n+1}}\to0,\because|x|<1$$
::::

因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}a_n={1\over1-x}={2021\over2020}
:::

$$\lim_{n\to\infty}a_n={1\over1-x}={2021\over2020}$$
::::

## 不动点法 {#_28}

### 不动点 {#_29}

对于函数 []{.arithmatex}$f$ ，若 []{.arithmatex}$x$ 满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)=x
:::

$$f(x)=x$$
::::

这个 []{.arithmatex}$x$​ 称为这个函数的**不动点**，或定点，是被这个函数映射到其自身一个点。

例如：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)=x\^{2}-3x+4
:::

$$f(x)=x^{2}-3x+4$$
::::

的不动点为，

:::: {.arithmatex}
::: {.MathJax_Preview}
x=f(x)\\ x\^2-4x+4=0\\ (x-2)\^2=0
:::

$$x=f(x)\\
x^2-4x+4=0\\
(x-2)^2=0$$
::::

即函数 []{.arithmatex}$f$ 的不动点为 []{.arithmatex}$2$，因为 []{.arithmatex}$f(2)=2$。

不是每一个函数都具有不动点，例如定义在实数上的函数 []{.arithmatex}$f(x)=x+1$ 就没有不动点。

因为对于任意的实数， []{.arithmatex}$x$ 永远不会等于 []{.arithmatex}$x+1$。

用画图的话来说，不动点意味着点 []{.arithmatex}$(x,f(x))$ 在直线 []{.arithmatex}$y=x$ 上，即图像存在交点。

上例 []{.arithmatex}$f(x)=x+1$ 的情况是，这个函数的图像与那根直线是一对平行线。

在函数的有限次迭代之后回到相同值的点叫做周期点；不动点是周期等于 1 的周期点。

### 不动点和数列 {#_30}

如果数列递推公式形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}=f(a_n)
:::

$$a_{n+1}=f(a_n)$$
::::

那么，[]{.arithmatex}$f$ 称为**迭代函数**（**生成函数**），则和上文一样，

:::: {.arithmatex}
::: {.MathJax_Preview}
x=f(x)
:::

$$x=f(x)$$
::::

的方程，称为**不动点方程**。

当我们解出一个不动点 []{.arithmatex}$x$，等式两边同时减去 []{.arithmatex}$x$，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}-x=f(a_n)-x
:::

$$a_{n+1}-x=f(a_n)-x$$
::::

左右都等于零，因此右面一定有因式，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n-x
:::

$$a_n-x$$
::::

这个过程称为**不动点改造**。

那么，左右就存在相同的结构，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=a_n-x
:::

$$b_n=a_n-x$$
::::

往往可以进而推导一些性质。

### 不动点法求极限 {#_31}

有数列形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=f(a\_{n-1})
:::

$$a_n=f(a_{n-1})$$
::::

假设这个数列存在极限，记为 []{.arithmatex}$a$，那么对两边同时取极限，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}a_n=\lim\_{n\to\infty}f(a\_{n-1})
:::

$$\lim_{n\to\infty}a_n=\lim_{n\to\infty}f(a_{n-1})$$
::::

一般默认 []{.arithmatex}$f$ 函数是光滑的，那么，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}f(a\_{n-1})=f(\lim\_{n\to\infty}a\_{n-1})
:::

$$\lim_{n\to\infty}f(a_{n-1})=f(\lim_{n\to\infty}a_{n-1})$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
a=f(a)
:::

$$a=f(a)$$
::::

解出这个解，那么如果存在极限，极限一定是这个方程的解中的一个。

原理为，只有当数列收敛到不动点，才能存在极限；不然也不会存在极限。

### 数列迭代：蛛网工作法 {#_32}

我们延续上面的观点，尝试使用一些新奇的技巧，

我们想要把数列 []{.arithmatex}$a_n\to a_{n+1}$ 这个过程直观的表示出来，我们知道，

:::: {.arithmatex}
::: {.MathJax_Preview}
f(a_n)=a\_{n+1}
:::

$$f(a_n)=a_{n+1}$$
::::

容易想到，我们在平面内做出 []{.arithmatex}$f(x)$ 的图像，那么这上面的点，

:::: {.arithmatex}
::: {.MathJax_Preview}
Q(a_n,f(a_n))=(a_n,a\_{n+1})
:::

$$Q(a_n,f(a_n))=(a_n,a_{n+1})$$
::::

就表示了一个递推的过程。

然后考虑数列运作的趋势是什么样的，显然我们只考虑递增和递减，

- []{.arithmatex}$f(a_n)>a_n$，数列在此处递增，对应点在 []{.arithmatex}$y=x$ 图像上方；
- []{.arithmatex}$f(a_n)<a_n$，数列在此处递减，对应点在 []{.arithmatex}$y=x$ 图像下方。

于是，我们考虑在平面内再做出 []{.arithmatex}$y=x$ 的图像，那么数列的趋势符合上文。

具体的，做点，

:::: {.arithmatex}
::: {.MathJax_Preview}
A_1(a_1,f(a_1))=(a_1,a_2)
:::

$$A_1(a_1,f(a_1))=(a_1,a_2)$$
::::

过 []{.arithmatex}$A_1$ 做 []{.arithmatex}$x$ 轴平行线，交 []{.arithmatex}$y=x$ 于，

:::: {.arithmatex}
::: {.MathJax_Preview}
A_2(a_2,a_2)
:::

$$A_2(a_2,a_2)$$
::::

过 []{.arithmatex}$A_2$ 做 []{.arithmatex}$y$ 轴平行线，交 []{.arithmatex}$y=f(x)$​ 于，

:::: {.arithmatex}
::: {.MathJax_Preview}
A_3(a_2,f(a_2))=(a_2,a_3)
:::

$$A_3(a_2,f(a_2))=(a_2,a_3)$$
::::

以此类推，形如，

<figure>
<p><img src="../3purusz5.avif" alt="蛛网" /></p>
<figcaption><p>蛛网工作法</p></figcaption>
</figure>

我们知道，按照顺序在 []{.arithmatex}$y=f(x)$​ 图像上的点，对应原数列。

根据这个图像，我们还能知道不动点 []{.arithmatex}$x=f(x)$ 其实是这两个图像的交点。

于是，如果我们这么做下去，能推到不动点附近，那么函数收敛。

![alt text](../image.avif){width="100%"}

与上文类似，指数函数、幂函数的线性组合，一般都是光滑的，那么有，

若 []{.arithmatex}$|f'(x_0)|<1$，不动点 []{.arithmatex}$x_0$​ 称为吸引不动点，数列迭代过程中会靠近吸引不动点。

若 []{.arithmatex}$|f'(x_0)|>1$，不动点 []{.arithmatex}$x_0$ 称为排斥不动点，数列迭代过程中会远离排斥不动点。

### 通项公式：例题 {#_33}

#### 一次函数形 {#_34}

例题：有数列，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=1,a_n={1\over2}a\_{n-1}+1
:::

$$a_1=1,a_n={1\over2}a_{n-1}+1$$
::::

求 []{.arithmatex}$a_n$ 的通项公式。

求出不动点 []{.arithmatex}$x$，满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
x={1\over2}x+1\\ x=2
:::

$$x={1\over2}x+1\\
x=2$$
::::

原式两边同时减二，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n-2={1\over2}a\_{n-1}-1={1\over2}(a\_{n-1}-2)
:::

$$a_n-2={1\over2}a_{n-1}-1={1\over2}(a_{n-1}-2)$$
::::

因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n-2={1\over2\^{n-1}}(a_1-2)\\ a_n=-{1\over2\^{n-1}}+2
:::

$$a_n-2={1\over2^{n-1}}(a_1-2)\\
a_n=-{1\over2^{n-1}}+2$$
::::

#### 二次函数型（双解） {#_35}

解，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=3,a\_{n+1}={4a_n-2\over a_n+1}
:::

$$a_1=3,a_{n+1}={4a_n-2\over a_n+1}$$
::::

求出不动点，

:::: {.arithmatex}
::: {.MathJax_Preview}
x={4x-2\over x+1}\\ x\^2+x=4x-2\\ x\^2-3x+2=0\\ (x-2)(x-1)=0
:::

$$x={4x-2\over x+1}\\
x^2+x=4x-2\\
x^2-3x+2=0\\
(x-2)(x-1)=0$$
::::

我们把两个不动点 []{.arithmatex}$2,1$ 分别减到递推式两边，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}-2={2a_n-4\over a_n+1}\\ a\_{n+1}-1={3a_n-3\over a_n+1}
:::

$$a_{n+1}-2={2a_n-4\over a_n+1}\\
a_{n+1}-1={3a_n-3\over a_n+1}$$
::::

化简，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}-2={2(a_n-2)\over a_n+1}\\ a\_{n+1}-1={3(a_n-1)\over a_n+1}
:::

$$a_{n+1}-2={2(a_n-2)\over a_n+1}\\
a_{n+1}-1={3(a_n-1)\over a_n+1}$$
::::

然后上下做比，

:::: {.arithmatex}
::: {.MathJax_Preview}
{a\_{n+1}-2\over a\_{n+1}-1}={2\over3}\cdot{a_n-2\over a_n-1}
:::

$${a_{n+1}-2\over a_{n+1}-1}={2\over3}\cdot{a_n-2\over a_n-1}$$
::::

注意到是等比数列，因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
{a_n-2\over a_n-1}=\left({2\over3}\right)\^{n-1}{a_1-2\over a_1-1}={1\over2}\left({2\over3}\right)\^{n-1}
:::

$${a_n-2\over a_n-1}=\left({2\over3}\right)^{n-1}{a_1-2\over a_1-1}={1\over2}\left({2\over3}\right)^{n-1}$$
::::

记后面的为 []{.arithmatex}$S_n$，则，

:::: {.arithmatex}
::: {.MathJax_Preview}
{a_n-2\over a_n-1}=S_n\\ a_n-2=a_nS_n-S_n\\ (S_n-1)a_n=S_n-2\\ a_n={S_n-2\over S_n-1}
:::

$${a_n-2\over a_n-1}=S_n\\
a_n-2=a_nS_n-S_n\\
(S_n-1)a_n=S_n-2\\
a_n={S_n-2\over S_n-1}$$
::::

带入，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n={(2/3)\^{n-1}-4\over(2/3)\^{n-1}-2}={2\^{n-1}-4\cdot3\^{n-1}\over2\^{n-1}-2\cdot3\^{n-1}}
:::

$$a_n={(2/3)^{n-1}-4\over(2/3)^{n-1}-2}={2^{n-1}-4\cdot3^{n-1}\over2^{n-1}-2\cdot3^{n-1}}$$
::::

#### 二次函数型（单解） {#_36}

解，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=5,a\_{n+1}={3a_n-4\over a_n-1}
:::

$$a_1=5,a_{n+1}={3a_n-4\over a_n-1}$$
::::

不动点，

:::: {.arithmatex}
::: {.MathJax_Preview}
x\^2-x=3x-4\\ x\^2-4x-4=0\\ x=2
:::

$$x^2-x=3x-4\\
x^2-4x-4=0\\
x=2$$
::::

只有一个解，我们两边减去，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}-2={a_n-2\over a_n-1}
:::

$$a_{n+1}-2={a_n-2\over a_n-1}$$
::::

注意到两个分子形式相同，我们两边取倒数，

:::: {.arithmatex}
::: {.MathJax_Preview}
{1\over a\_{n+1}-2}={a_n-1\over a_n-2}=1+{1\over a_n-2}
:::

$${1\over a_{n+1}-2}={a_n-1\over a_n-2}=1+{1\over a_n-2}$$
::::

为等比数列，

:::: {.arithmatex}
::: {.MathJax_Preview}
{1\over a_n-2}={1\over a_1-1}+(n-1)=n-{2\over3}
:::

$${1\over a_n-2}={1\over a_1-1}+(n-1)=n-{2\over3}$$
::::

两边再取倒数，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n-2={1\over n-2/3}={3\over3n-2}\\ a_n={3\over3n-2}+2={6n-1\over3n-2}
:::

$$a_n-2={1\over n-2/3}={3\over3n-2}\\
a_n={3\over3n-2}+2={6n-1\over3n-2}$$
::::

#### 二次函数型（无解） {#_37}

解，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=2,a_n=1-{1\over a\_{n-1}}
:::

$$a_1=2,a_n=1-{1\over a_{n-1}}$$
::::

不动点，

:::: {.arithmatex}
::: {.MathJax_Preview}
x=1-{1\over x}\\ x\^2=x-1\\ x\^2-x+1=0
:::

$$x=1-{1\over x}\\
x^2=x-1\\
x^2-x+1=0$$
::::

无解，因此该数列为周期数列，考虑，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=2\\ a_2=1/2\\ a_3=-1\\ a_4=2
:::

$$a_1=2\\
a_2=1/2\\
a_3=-1\\
a_4=2$$
::::

为 []{.arithmatex}$T=3$ 的周期数列，因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\left\\\begin{aligned} 2&\quad\operatorname{if}n\equiv1\pmod3\\ 1/2&\quad\operatorname{if}n\equiv2\pmod3\\ -1&\quad\operatorname{if}n\equiv0\pmod3\\ \end{aligned}\right.
:::

$$a_n=\left\{\begin{aligned}
2&\quad\operatorname{if}n\equiv1\pmod3\\
1/2&\quad\operatorname{if}n\equiv2\pmod3\\
-1&\quad\operatorname{if}n\equiv0\pmod3\\
\end{aligned}\right.$$
::::

#### 不动点解题技巧 {#_38}

适用于形如 []{.arithmatex}$a_{n+1}=f(a_n)$​，

求解通项公式部分，求解不动点 []{.arithmatex}$x=f(x)$ 后，

【若为一次函数】：两边减去，构造等比；

【若为二次函数双解】：两边减去两个不动点，做比，构造等比；

【若为二次函数单解】：减去不动点，去倒数，通分，构造等差；

【若为二次函数无解】：为周期数列，手模即可。

#### 例题 {#_39}

已知从 []{.arithmatex}$1$ 开始的数列，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=2,a\_{n+1}=(\sqrt2-1)(a_n+2)\\ b_1=2,b\_{n+1}={3b_n+4\over2b_n+3}
:::

$$a_1=2,a_{n+1}=(\sqrt2-1)(a_n+2)\\
b_1=2,b_{n+1}={3b_n+4\over2b_n+3}$$
::::

求证，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sqrt2\<b_n\le a\_{4n-3}
:::

$$\sqrt2<b_n\le a_{4n-3}$$
::::

考虑直接求出通项公式，

对于数列 []{.arithmatex}$\{a_n\}$，不动点，

:::: {.arithmatex}
::: {.MathJax_Preview}
x=(\sqrt2-1)(x+2)\\ x=(\sqrt2-1)x+2(\sqrt2-1)\\ (2-\sqrt2)x=2(\sqrt2-1)\\ x=(\sqrt2-1)(2+\sqrt2)\\ x=\sqrt2
:::

$$x=(\sqrt2-1)(x+2)\\
x=(\sqrt2-1)x+2(\sqrt2-1)\\
(2-\sqrt2)x=2(\sqrt2-1)\\
x=(\sqrt2-1)(2+\sqrt2)\\
x=\sqrt2$$
::::

两边减去 []{.arithmatex}$\sqrt2$，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}-\sqrt2=(\sqrt2-1)a_n+\sqrt2-2=(\sqrt2-1)(a_n-\sqrt2)
:::

$$a_{n+1}-\sqrt2=(\sqrt2-1)a_n+\sqrt2-2=(\sqrt2-1)(a_n-\sqrt2)$$
::::

因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n-\sqrt2=(\sqrt2-1)\^{n-1}(a_1-\sqrt2)=(2-\sqrt2)(\sqrt2-1)\^{n-1}\\ a_n=\sqrt2(\sqrt2-1)\^n+\sqrt2
:::

$$a_n-\sqrt2=(\sqrt2-1)^{n-1}(a_1-\sqrt2)=(2-\sqrt2)(\sqrt2-1)^{n-1}\\
a_n=\sqrt2(\sqrt2-1)^n+\sqrt2$$
::::

对于数列 []{.arithmatex}$\{b_n\}$，不动点，

:::: {.arithmatex}
::: {.MathJax_Preview}
2x\^2+3x=3x+4\\ x\^2=2\\ x\_{1,2}=\pm\sqrt2
:::

$$2x^2+3x=3x+4\\
x^2=2\\
x_{1,2}=\pm\sqrt2$$
::::

两边减去，

:::: {.arithmatex}
::: {.MathJax_Preview}
b\_{n+1}-\sqrt2={(3-2\sqrt2)(b_n-\sqrt2)\over2b_n+3}\\ b\_{n+1}+\sqrt2={(3+2\sqrt2)(b_n+\sqrt2)\over2b_n+3}
:::

$$b_{n+1}-\sqrt2={(3-2\sqrt2)(b_n-\sqrt2)\over2b_n+3}\\
b_{n+1}+\sqrt2={(3+2\sqrt2)(b_n+\sqrt2)\over2b_n+3}$$
::::

做比，

:::: {.arithmatex}
::: {.MathJax_Preview}
{b\_{n+1}+\sqrt2\over b\_{n+1}-\sqrt2}={3+2\sqrt2\over3-2\sqrt2}\cdot{b_n+\sqrt2\over b_n-\sqrt2}
:::

$${b_{n+1}+\sqrt2\over b_{n+1}-\sqrt2}={3+2\sqrt2\over3-2\sqrt2}\cdot{b_n+\sqrt2\over b_n-\sqrt2}$$
::::

注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
{3+2\sqrt2\over3-2\sqrt2}={(\sqrt2+1)\^2\over(\sqrt2-1)\^2}=\left({\sqrt2+1\over\sqrt2-1}\right)\^2
:::

$${3+2\sqrt2\over3-2\sqrt2}={(\sqrt2+1)^2\over(\sqrt2-1)^2}=\left({\sqrt2+1\over\sqrt2-1}\right)^2$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} {b_n+\sqrt2\over b_n-\sqrt2}&=\left({\sqrt2+1\over\sqrt2-1}\right)\^{2(n-1)}{b_1+\sqrt2\over b_1-\sqrt2}\\ &=\left({\sqrt2+1\over\sqrt2-1}\right)\^{2n-2}{2+\sqrt2\over 2-\sqrt2}\\ &=\left({\sqrt2+1\over\sqrt2-1}\right)\^{2n-2}{\sqrt2+1\over\sqrt2-1}\\ &=\left({\sqrt2+1\over\sqrt2-1}\right)\^{2n-1}=x \end{aligned}
:::

$$\begin{aligned}
{b_n+\sqrt2\over b_n-\sqrt2}&=\left({\sqrt2+1\over\sqrt2-1}\right)^{2(n-1)}{b_1+\sqrt2\over b_1-\sqrt2}\\
&=\left({\sqrt2+1\over\sqrt2-1}\right)^{2n-2}{2+\sqrt2\over 2-\sqrt2}\\
&=\left({\sqrt2+1\over\sqrt2-1}\right)^{2n-2}{\sqrt2+1\over\sqrt2-1}\\
&=\left({\sqrt2+1\over\sqrt2-1}\right)^{2n-1}=x
\end{aligned}$$
::::

则，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n+\sqrt2=xb_n-\sqrt2x\\ (x-1)b_n=\sqrt2(x+1)\\ b_n=\sqrt2{x+1\over x-1}=\sqrt2{(\sqrt2+1)\^{2n-1}+(\sqrt2-1)\^{2n-1}\over(\sqrt2+1)\^{2n-1}-(\sqrt2-1)\^{2n-1}}
:::

$$b_n+\sqrt2=xb_n-\sqrt2x\\
(x-1)b_n=\sqrt2(x+1)\\
b_n=\sqrt2{x+1\over x-1}=\sqrt2{(\sqrt2+1)^{2n-1}+(\sqrt2-1)^{2n-1}\over(\sqrt2+1)^{2n-1}-(\sqrt2-1)^{2n-1}}$$
::::

考虑进一步化简，此时有两个形式，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=\sqrt2{(\sqrt2+1)\^{4n-2}+1\over(\sqrt2+1)\^{4n-2}-1}=\sqrt2{1+(\sqrt2-1)\^{4n-2}\over1-(\sqrt2-1)\^{4n-2}}
:::

$$b_n=\sqrt2{(\sqrt2+1)^{4n-2}+1\over(\sqrt2+1)^{4n-2}-1}=\sqrt2{1+(\sqrt2-1)^{4n-2}\over1-(\sqrt2-1)^{4n-2}}$$
::::

考虑证明给出的性质，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sqrt2\<b_n\le a\_{4n-3}=\sqrt2(\sqrt2-1)\^{4n-3}+\sqrt2
:::

$$\sqrt2<b_n\le a_{4n-3}=\sqrt2(\sqrt2-1)^{4n-3}+\sqrt2$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
1\<{1+(\sqrt2-1)\^{4n-2}\over1-(\sqrt2-1)\^{4n-2}}\le(\sqrt2-1)\^{4n-3}+1
:::

$$1<{1+(\sqrt2-1)^{4n-2}\over1-(\sqrt2-1)^{4n-2}}\le(\sqrt2-1)^{4n-3}+1$$
::::

左侧显然，右侧，移项，

:::: {.arithmatex}
::: {.MathJax_Preview}
{2(\sqrt2-1)\^{4n-2}\over1-(\sqrt2-1)\^{4n-2}}\le(\sqrt2-1)\^{4n-3}\\ {2(\sqrt2-1)\over1-(\sqrt2-1)\^{4n-2}}\le1\\ 2(\sqrt2-1)\le1-(\sqrt2-1)\^{4n-2}\\ (\sqrt2-1)\^{4n-2}\le3-2\sqrt2=(\sqrt2-1)\^2\\ 4n-2\ge2,n\ge1
:::

$${2(\sqrt2-1)^{4n-2}\over1-(\sqrt2-1)^{4n-2}}\le(\sqrt2-1)^{4n-3}\\
{2(\sqrt2-1)\over1-(\sqrt2-1)^{4n-2}}\le1\\
2(\sqrt2-1)\le1-(\sqrt2-1)^{4n-2}\\
(\sqrt2-1)^{4n-2}\le3-2\sqrt2=(\sqrt2-1)^2\\
4n-2\ge2,n\ge1$$
::::

显然成立。

## 裂项和放缩 {#_40}

### 分式裂项 {#_41}

第一组：

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{{1\over n(n+1)}={1\over n}-{1\over n+1}}
:::

$$\boxed{{1\over n(n+1)}={1\over n}-{1\over n+1}}$$
::::

推广，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{{1\over n(n+k)}={1\over k}\left({1\over n}-{1\over n+k}\right)}
:::

$$\boxed{{1\over n(n+k)}={1\over k}\left({1\over n}-{1\over n+k}\right)}$$
::::

第二组：

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{{1\over n(n+1)(n+2)}={1\over2}\left\[{1\over n(n+1)}-{1\over(n+1)(n+2)}\right\]}
:::

$$\boxed{{1\over n(n+1)(n+2)}={1\over2}\left[{1\over n(n+1)}-{1\over(n+1)(n+2)}\right]}$$
::::

推广，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{{1\over n(n+1)\dots (n+k)}={1\over k}\left\[{1\over n\dots(n+k-1)}-{1\over(n+1)\dots(n+k)}\right\]}
:::

$$\boxed{{1\over n(n+1)\dots (n+k)}={1\over k}\left[{1\over n\dots(n+k-1)}-{1\over(n+1)\dots(n+k)}\right]}$$
::::

### 整式裂项 {#_42}

第一组，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{n(n+1)={1\over3}\[{\color{blue}n(n+1)}(n+2)-(n-1){\color{blue}n(n+1)}\]}
:::

$$\boxed{n(n+1)={1\over3}[{\color{blue}n(n+1)}(n+2)-(n-1){\color{blue}n(n+1)}]}$$
::::

推广，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{n(n+1)\dots(n+m)={1\over m+2}\[{\color{blue}n\dots}(n+m+1)-(n-1){\color{blue}\dots(n+m)}\]}
:::

$$\boxed{n(n+1)\dots(n+m)={1\over m+2}[{\color{blue}n\dots}(n+m+1)-(n-1){\color{blue}\dots(n+m)}]}$$
::::

### 根式裂项 {#_43}

第一组，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{{1\over\sqrt{n+1}-\sqrt n}=\sqrt{n+1}+\sqrt n}
:::

$$\boxed{{1\over\sqrt{n+1}-\sqrt n}=\sqrt{n+1}+\sqrt n}$$
::::

推广，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{{1\over\sqrt{n+k}-\sqrt n}={\sqrt{n+k}+\sqrt n\over k}}
:::

$$\boxed{{1\over\sqrt{n+k}-\sqrt n}={\sqrt{n+k}+\sqrt n\over k}}$$
::::

或者，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{{1\over\sqrt a\pm\sqrt b}={\sqrt a\mp\sqrt b\over a\pm b}}
:::

$$\boxed{{1\over\sqrt a\pm\sqrt b}={\sqrt a\mp\sqrt b\over a\pm b}}$$
::::

第二组，对于 []{.arithmatex}$0<\alpha<1$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{{1\over1-\alpha}\left\[{1\over(n+1)\^{\alpha-1}}-{1\over n\^{\alpha-1}}\right\]\<{1\over n\^\alpha}\<{1\over1-\alpha}\left\[{1\over n\^{\alpha-1}}-{1\over(n-1)\^{\alpha-1}}\right\]},n\ge2
:::

$$\boxed{{1\over1-\alpha}\left[{1\over(n+1)^{\alpha-1}}-{1\over n^{\alpha-1}}\right]<{1\over n^\alpha}<{1\over1-\alpha}\left[{1\over n^{\alpha-1}}-{1\over(n-1)^{\alpha-1}}\right]},n\ge2$$
::::

例如，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \alpha=1/2&\longrightarrow\boxed{2(\sqrt{n+1}-\sqrt n)\<\sqrt n\<2(\sqrt n-\sqrt{n-1})}\\ \alpha=1/3&\longrightarrow\boxed{{3\over2}\left(\sqrt\[3\]{(n+1)\^2}-\sqrt\[3\]{n\^2}\right)\<{1\over\sqrt\[3\]n}\<{3\over2}\left(\sqrt\[3\]{n\^2}-\sqrt\[3\]{(n-1)\^2}\right)} \end{aligned}
:::

$$\begin{aligned}
\alpha=1/2&\longrightarrow\boxed{2(\sqrt{n+1}-\sqrt n)<\sqrt n<2(\sqrt n-\sqrt{n-1})}\\
\alpha=1/3&\longrightarrow\boxed{{3\over2}\left(\sqrt[3]{(n+1)^2}-\sqrt[3]{n^2}\right)<{1\over\sqrt[3]n}<{3\over2}\left(\sqrt[3]{n^2}-\sqrt[3]{(n-1)^2}\right)}
\end{aligned}$$
::::

证明，

:::: {.arithmatex}
::: {.MathJax_Preview}
\int_n\^{n+1}{1\over x\^\alpha}\mathrm dx\<{1\over n\^\alpha}\<\int\_{n-1}\^n{1\over x\^\alpha}\mathrm dx
:::

$$\int_n^{n+1}{1\over x^\alpha}\mathrm dx<{1\over n^\alpha}<\int_{n-1}^n{1\over x^\alpha}\mathrm dx$$
::::

由牛顿·莱布尼茨公式化简得上式。

另一组，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sqrt{2n+4}-\sqrt{2n+2}\<{1\over\sqrt{2n+1}}\<\sqrt{2n+1}-\sqrt{2n-1}
:::

$$\sqrt{2n+4}-\sqrt{2n+2}<{1\over\sqrt{2n+1}}<\sqrt{2n+1}-\sqrt{2n-1}$$
::::

证明大体形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
{1\over\sqrt{2n+1}}\<{1\over(\sqrt{2n+1}+\sqrt{2n-1})/2}=\sqrt{2n+1}-\sqrt{2n-1}
:::

$${1\over\sqrt{2n+1}}<{1\over(\sqrt{2n+1}+\sqrt{2n-1})/2}=\sqrt{2n+1}-\sqrt{2n-1}$$
::::

### 例题 {#_44}

#### 简单例题 {#_45}

已知等差数列 []{.arithmatex}$\{a_n\}$ 满足，[]{.arithmatex}$a_3=7,a_5+a_7=26$，

- 求 []{.arithmatex}$a_n$ 及其前 []{.arithmatex}$n$ 项和 []{.arithmatex}$S_n$；
- 令 []{.arithmatex}$b_n=1/(a_n^2-1)$，求其前 []{.arithmatex}$n$ 项和 []{.arithmatex}$T_n$。

易知，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_5+a_7=2a_6=26,a_6=13\\ d=(a_6-a_3)/(6-3)=2\\ a_1=a_3-2d=3
:::

$$a_5+a_7=2a_6=26,a_6=13\\
d=(a_6-a_3)/(6-3)=2\\
a_1=a_3-2d=3$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=a_1+(n-1)d=3+2(n-1)=2n+1\\ S_n=n(a_1+a_n)/2=n\^2+2n
:::

$$a_n=a_1+(n-1)d=3+2(n-1)=2n+1\\
S_n=n(a_1+a_n)/2=n^2+2n$$
::::

那么，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n={1\over a_n\^2-1}={1\over 4n\^2+4n}={1\over4}\cdot{1\over n(n+1)}={1\over 4}\left({1\over n}-{1\over n+1}\right)
:::

$$b_n={1\over a_n^2-1}={1\over 4n^2+4n}={1\over4}\cdot{1\over n(n+1)}={1\over 4}\left({1\over n}-{1\over n+1}\right)$$
::::

那么，

:::: {.arithmatex}
::: {.MathJax_Preview}
T_n=b_1+b_2+\dots+b_n={1\over4}\left({1\over1}-{1\over2}+{1\over2}-{1\over3}+\dots+{1\over n}-{1\over n+1}\right)
:::

$$T_n=b_1+b_2+\dots+b_n={1\over4}\left({1\over1}-{1\over2}+{1\over2}-{1\over3}+\dots+{1\over n}-{1\over n+1}\right)$$
::::

注意好配对，

:::: {.arithmatex}
::: {.MathJax_Preview}
T_n={1\over4}\left(1-{1\over n+1}\right)={n\over 4n+4}
:::

$$T_n={1\over4}\left(1-{1\over n+1}\right)={n\over 4n+4}$$
::::

#### 基础例题 {#_46}

已知数列 []{.arithmatex}$\{a_n\}$ 满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=1,a_2=1/4\\ a\_{n+1}={(n-1)a_n\over n-a_n}
:::

$$a_1=1,a_2=1/4\\
a_{n+1}={(n-1)a_n\over n-a_n}$$
::::

求证，对于任意 []{.arithmatex}$n\in\mathbb N^*$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sum\_{i=1}\^na_i\^2\<{7\over6}
:::

$$\sum_{i=1}^na_i^2<{7\over6}$$
::::

注意到递推公式并不是不动点的标准形式，但是，

发现如果把分母乘过去，[]{.arithmatex}$n$ 的系数相同，会约去，因此，

设不动点 []{.arithmatex}$x$，

:::: {.arithmatex}
::: {.MathJax_Preview}
x={(n-1)x\over n-x}\\ nx-x\^2=nx-x\\ x\^2-x=x(x-1)=0\\ x_1=0,x_2=1
:::

$$x={(n-1)x\over n-x}\\
nx-x^2=nx-x\\
x^2-x=x(x-1)=0\\
x_1=0,x_2=1$$
::::

两边减去一，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}-1={n(a_n-1)\over n-a_n}
:::

$$a_{n+1}-1={n(a_n-1)\over n-a_n}$$
::::

与原式做比，

:::: {.arithmatex}
::: {.MathJax_Preview}
{a\_{n+1}\over a\_{n+1}-1}={n-1\over n}\cdot{a_n\over a_n-1}
:::

$${a_{n+1}\over a_{n+1}-1}={n-1\over n}\cdot{a_n\over a_n-1}$$
::::

注意到左边系数的分母，两项相差了一，因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
n{a\_{n+1}\over a\_{n+1}-1}=(n-1){a_n\over a_n-1}
:::

$$n{a_{n+1}\over a_{n+1}-1}=(n-1){a_n\over a_n-1}$$
::::

因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
(n-1){a_n\over a_n-1}
:::

$$(n-1){a_n\over a_n-1}$$
::::

对于 []{.arithmatex}$n\ge2$ 为常数列，因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
(n-1){a_n\over a_n-1}={a_2\over a_2-1}=-{1\over3}
:::

$$(n-1){a_n\over a_n-1}={a_2\over a_2-1}=-{1\over3}$$
::::

则，

:::: {.arithmatex}
::: {.MathJax_Preview}
1-a_n=(3n-3)a_n\\ (3n-2)a_n=1\\ a_n={1\over 3n-2}
:::

$$1-a_n=(3n-3)a_n\\
(3n-2)a_n=1\\
a_n={1\over 3n-2}$$
::::

尝试证明，

:::: {.arithmatex}
::: {.MathJax_Preview}
S_n=\sum\_{i=1}\^na_i\^2\<{7\over6}\\ 1+{1\over 4\^2}+{1\over 7\^2}+{1\over 10\^2}+\dots\<{7\over6}
:::

$$S_n=\sum_{i=1}^na_i^2<{7\over6}\\
1+{1\over 4^2}+{1\over 7^2}+{1\over 10^2}+\dots<{7\over6}$$
::::

进行放缩，

注意到我们要把每一项放缩为差为三的两项，才能用裂项消去，即，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} {1\over(3n-2)\^2}&\<{1\over(3n-2-a)(3n-2+b)}\\ &={1\over a+b}\left({1\over 3n-2-a}-{1\over 3n-2+b}\right) \end{aligned}
:::

$$\begin{aligned}
{1\over(3n-2)^2}&<{1\over(3n-2-a)(3n-2+b)}\\
&={1\over a+b}\left({1\over 3n-2-a}-{1\over 3n-2+b}\right)
\end{aligned}$$
::::

对于 []{.arithmatex}$a+b=3,a\ge b$，最自然的想法，直接取 []{.arithmatex}$a=b=1.5$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} 3S_n&\<3+{1\over 2.5}-{1\over 5.5}+{1\over 5.5}-{1\over 8.8}+\dots+{1\over 3n-3.5}-{1\over 3n-0.5}\\ &=3+{1\over 2.5}-{1\over 3n-0.5}\<3+{1\over2.5}={34\over10} \end{aligned}
:::

$$\begin{aligned}
3S_n&<3+{1\over 2.5}-{1\over 5.5}+{1\over 5.5}-{1\over 8.8}+\dots+{1\over 3n-3.5}-{1\over 3n-0.5}\\
&=3+{1\over 2.5}-{1\over 3n-0.5}<3+{1\over2.5}={34\over10}
\end{aligned}$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
S_n\<{34\over30}\<{7\over6}
:::

$$S_n<{34\over30}<{7\over6}$$
::::

类似的，我们取 []{.arithmatex}$a=2,b=1$ 等也可以，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} 3S_n&\<3+{1\over 2}-{1\over 4}+{1\over 4}-{1\over 7}+{1\over 7}-{1\over 10}+\dots+{1\over 3n-3}-{1\over 3n}\\ &={7\over2}-{1\over3n}\<{7\over2}\\ S_n&\<{7\over6} \end{aligned}
:::

$$\begin{aligned}
3S_n&<3+{1\over 2}-{1\over 4}+{1\over 4}-{1\over 7}+{1\over 7}-{1\over 10}+\dots+{1\over 3n-3}-{1\over 3n}\\
&={7\over2}-{1\over3n}<{7\over2}\\
S_n&<{7\over6}
\end{aligned}$$
::::

注意到这么做得出来的更加不准确，我们通过暴力手段可以发现，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{x\to\infty}S_n\to L
:::

$$\lim_{x\to\infty}S_n\to L$$
::::

其中 []{.arithmatex}$L$ 大约是 []{.arithmatex}$1.1217$，我们上面一个估算已经非常准确了。

#### 还是例题 {#_47}

已知数列 []{.arithmatex}$\{a_n\}$ 是公差不为零的等差数列，

且 []{.arithmatex}$a_4$ 是 []{.arithmatex}$a_2,a_8$ 等比中项，满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1+a_2+\dots+a_7=14
:::

$$a_1+a_2+\dots+a_7=14$$
::::

- 求 []{.arithmatex}$a_n$ 通项公式。

我们注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_4\^2=a_2a_8
:::

$$a_4^2=a_2a_8$$
::::

而，

:::: {.arithmatex}
::: {.MathJax_Preview}
4\^2=2\times8
:::

$$4^2=2\times8$$
::::

因此，我们大胆假设，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=na_1
:::

$$a_n=na_1$$
::::

证明：

:::: {.arithmatex}
::: {.MathJax_Preview}
a_2=a_1+d,a_4=a_1+3d,a_8=a_1+7d\\ (a_1+3d)\^2=(a_1+d)(a_1+7d)\\ 6da_1+9d\^2=7d\^2+8da_1\\ 2d\^2=2da_1,d=a_1\\ a_n=a_1+(n-1)d=na_1
:::

$$a_2=a_1+d,a_4=a_1+3d,a_8=a_1+7d\\
(a_1+3d)^2=(a_1+d)(a_1+7d)\\
6da_1+9d^2=7d^2+8da_1\\
2d^2=2da_1,d=a_1\\
a_n=a_1+(n-1)d=na_1$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
S_7=7{a_1+a_7\over2}=28a_1=14\\ a_1={1\over2}
:::

$$S_7=7{a_1+a_7\over2}=28a_1=14\\
a_1={1\over2}$$
::::

因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n={1\over2}n
:::

$$a_n={1\over2}n$$
::::

#### 还是例题 {#_48}

（也许这道题是上一道题的后续

有数列 []{.arithmatex}$\{b_n\}$ 满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_1=-1\\ b_n={n+1\over2\^{n-1}n(n-1)},n\ge2
:::

$$b_1=-1\\
b_n={n+1\over2^{n-1}n(n-1)},n\ge2$$
::::

- 求其前 []{.arithmatex}$n$ 项和 []{.arithmatex}$T_n$。

观察到 []{.arithmatex}$n(n+1)$ 的形式，裂项，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} b_n&={n+1\over2\^{n-1}}\left({1\over n-1}-{1\over n}\right)\\ &={1\over2\^{n-1}}\left({n+1\over n-1}-{n+1\over n}\right)\\ &={1\over2\^{n-1}}\left({2\over n-1}-{1\over n}\right)\\ &={1\over2\^{n-2}(n-1)}-{1\over 2\^{n-1}n} \end{aligned}
:::

$$\begin{aligned}
b_n&={n+1\over2^{n-1}}\left({1\over n-1}-{1\over n}\right)\\
&={1\over2^{n-1}}\left({n+1\over n-1}-{n+1\over n}\right)\\
&={1\over2^{n-1}}\left({2\over n-1}-{1\over n}\right)\\
&={1\over2^{n-2}(n-1)}-{1\over 2^{n-1}n}
\end{aligned}$$
::::

考虑求和，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} T_n&=b_1+b_2+b_3+\dots+b_n\\ &=-1+{1\over1}-{1\over4}+{1\over4}-{1\over12}+\dots+{1\over2\^{n-2}(n-1)}-{1\over 2\^{n-1}n}\\ &=-{1\over2\^{n-1}n} \end{aligned}
:::

$$\begin{aligned}
T_n&=b_1+b_2+b_3+\dots+b_n\\
&=-1+{1\over1}-{1\over4}+{1\over4}-{1\over12}+\dots+{1\over2^{n-2}(n-1)}-{1\over 2^{n-1}n}\\
&=-{1\over2^{n-1}n}
\end{aligned}$$
::::

注意到 []{.arithmatex}$T_1=-1$ 也成立，因此上式即为结果。

#### 又是例题 {#_49}

已知数列 []{.arithmatex}$\{a_n\}$ 是公差为 []{.arithmatex}$d\neq0$ 的等差数列，

且 []{.arithmatex}$\{a_{k_n}\}$ 是等比数列，其中 []{.arithmatex}$k_1=3,k_2=5,k_3=9$。

- 求 []{.arithmatex}$k_1+k_2+\dots+k_n$ 的值。

和上一题类似，我们注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
k_1-1=2,k_2-1=4,k_3-1=8,2\times4=5
:::

$$k_1-1=2,k_2-1=4,k_3-1=8,2\times4=5$$
::::

我们大胆猜测，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=(n-1)d
:::

$$a_n=(n-1)d$$
::::

证明，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_5\^2=a_3a_9\\ (a_1+4d)\^2=(a_1+2d)(a_1+8d)\\ 16d\^2+8a_1d=16d\^2+10a_1d\\ 4a_1d=5a_1d\\ \because d\neq0,\therefore a_1=0
:::

$$a_5^2=a_3a_9\\
(a_1+4d)^2=(a_1+2d)(a_1+8d)\\
16d^2+8a_1d=16d^2+10a_1d\\
4a_1d=5a_1d\\
\because d\neq0,\therefore a_1=0$$
::::

因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=a_1+(n-1)d=(n-1)d
:::

$$a_n=a_1+(n-1)d=(n-1)d$$
::::

观察 []{.arithmatex}$k_n$ 的值，

我们发现 []{.arithmatex}$3,5,9$ 是经典的数列，考虑大胆猜测（雾

:::: {.arithmatex}
::: {.MathJax_Preview}
k_n=2\^n+1
:::

$$k_n=2^n+1$$
::::

此时，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{k_n}=2\^nd
:::

$$a_{k_n}=2^nd$$
::::

是一个公比为 []{.arithmatex}$2$ 的等比数列，符合条件。

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
S_n=\sum\_{i=1}\^nk_i=n+\sum\_{i=1}\^n2\^i=n+2\^{n+1}-2
:::

$$S_n=\sum_{i=1}^nk_i=n+\sum_{i=1}^n2^i=n+2^{n+1}-2$$
::::

#### 又是例题 {#_50}

对于数列 []{.arithmatex}$\{b_n\}$，有，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n={n\over n+1}+\sqrt{n-1\over n+1}
:::

$$b_n={n\over n+1}+\sqrt{n-1\over n+1}$$
::::

求证，对于 []{.arithmatex}$n\in\mathbb N^*$，

:::: {.arithmatex}
::: {.MathJax_Preview}
S_n=\sum\_{i=1}\^n{1\over n(n+1)\sqrt{2b_n}}\<\sqrt{n\over n+1}
:::

$$S_n=\sum_{i=1}^n{1\over n(n+1)\sqrt{2b_n}}<\sqrt{n\over n+1}$$
::::

首先，我们注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
S_1={1\over2}\<\sqrt{1\over2}
:::

$$S_1={1\over2}<\sqrt{1\over2}$$
::::

而后面的每一步，本质是在叠加

:::: {.arithmatex}
::: {.MathJax_Preview}
{1\over n(n+1)\sqrt{2b_n}}
:::

$${1\over n(n+1)\sqrt{2b_n}}$$
::::

的贡献，因此原问题的充分必要条件为，

:::: {.arithmatex}
::: {.MathJax_Preview}
{1\over n(n+1)\sqrt{2b_n}}\<\sqrt{n\over n+1}-\sqrt{n-1\over n}
:::

$${1\over n(n+1)\sqrt{2b_n}}<\sqrt{n\over n+1}-\sqrt{n-1\over n}$$
::::

考虑恒等变形，

:::: {.arithmatex}
::: {.MathJax_Preview}
{1\over n(n+1)}\cdot{1\over\sqrt{2b_n}}\<{n-\sqrt{n\^2-1}\over\sqrt{n(n+1)}}\\ {1\over\sqrt{n(n+1)}}\cdot{1\over\sqrt{2b_n}}\<n-\sqrt{n\^2-1}\\
:::

$${1\over n(n+1)}\cdot{1\over\sqrt{2b_n}}<{n-\sqrt{n^2-1}\over\sqrt{n(n+1)}}\\
{1\over\sqrt{n(n+1)}}\cdot{1\over\sqrt{2b_n}}<n-\sqrt{n^2-1}\\$$
::::

注意到两边都是正数，因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
{1\over2n(n+1)b_n}\<(n-\sqrt{n\^2-1})\^2\\ 2n(n+1)b_n\>\left({1\over n-\sqrt{n\^2-1}}\right)\^2
:::

$${1\over2n(n+1)b_n}<(n-\sqrt{n^2-1})^2\\
2n(n+1)b_n>\left({1\over n-\sqrt{n^2-1}}\right)^2$$
::::

暂时不展开，带入，

:::: {.arithmatex}
::: {.MathJax_Preview}
2n\^2+{\color{darkred}2n\sqrt{n\^2-1}}\>(n+\sqrt{n\^2-1})\^2=2n\^2-1+{\color{darkred}2n\sqrt{n\^2-1}}\\
:::

$$2n^2+{\color{darkred}2n\sqrt{n^2-1}}>(n+\sqrt{n^2-1})^2=2n^2-1+{\color{darkred}2n\sqrt{n^2-1}}\\$$
::::

显然成立。

### 找规律题 {#_51}

已知，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\prod\_{2\le i\le n}{i\^3-1\over i\^3+1}
:::

$$a_n=\prod_{2\le i\le n}{i^3-1\over i^3+1}$$
::::

- 求 []{.arithmatex}$\lim_{n\to\infty}a_n$。

我们知道，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{n\^3-1=(n-1)(n\^2+n+1)}\\\[0.5em\] \boxed{n\^3+1=(n+1)(n\^2-n+1)}
:::

$$\boxed{n^3-1=(n-1)(n^2+n+1)}\\[0.5em]
\boxed{n^3+1=(n+1)(n^2-n+1)}$$
::::

于是，首先，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\prod\_{2\le i\le n}{i\^3-1\over i\^3+1}=\prod\_{2\le i\le n}{i-1\over i+1}\prod\_{2\le i\le n}{i\^2+i+1\over i\^2-i+1}
:::

$$a_n=\prod_{2\le i\le n}{i^3-1\over i^3+1}=\prod_{2\le i\le n}{i-1\over i+1}\prod_{2\le i\le n}{i^2+i+1\over i^2-i+1}$$
::::

左边一个乘式，

:::: {.arithmatex}
::: {.MathJax_Preview}
\prod\_{2\le i\le n}{i-1\over i+1}={1\times2\times3\times\dots\times(n-1)\over 3\times4\times\dots\times n\times(n+1)}={2\over n\^2+n}
:::

$$\prod_{2\le i\le n}{i-1\over i+1}={1\times2\times3\times\dots\times(n-1)\over 3\times4\times\dots\times n\times(n+1)}={2\over n^2+n}$$
::::

右边考，注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{(i+1)\^2-(i+1)+1=i\^2+i+1}
:::

$$\boxed{(i+1)^2-(i+1)+1=i^2+i+1}$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
\prod\_{2\le i\le n}{i\^2+i+1\over i\^2-i+1}={7\times13\times\dots\times(n\^2+n+1)\over3\times7\times13\times\dots}={n\^2+n+1\over3}
:::

$$\prod_{2\le i\le n}{i^2+i+1\over i^2-i+1}={7\times13\times\dots\times(n^2+n+1)\over3\times7\times13\times\dots}={n^2+n+1\over3}$$
::::

得到结果，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n={2\over3}\cdot{n\^2+n+1\over n\^2+n}
:::

$$a_n={2\over3}\cdot{n^2+n+1\over n^2+n}$$
::::

考虑极限，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}a_n={2\over3}\lim\_{n\to\infty}{n\^2+n+1\over n\^2+n}={2\over3}
:::

$$\lim_{n\to\infty}a_n={2\over3}\lim_{n\to\infty}{n^2+n+1\over n^2+n}={2\over3}$$
::::

总结：找不着规律，多写几项。

### 总结一下 {#_52}

我们常见的裂项技巧有：

【简单型】一眼。

【从项出发】考虑每一项如何裂项，去消掉多余的项。

【从求和出发】考虑类似数学归纳法，证明

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n\<S_n-S\_{n-1}\Rightarrow b_1+b_2+\dots+b_n\<S_n\\(S_0=0)
:::

$$b_n<S_n-S_{n-1}\Rightarrow b_1+b_2+\dots+b_n<S_n\;(S_0=0)$$
::::

### 结论题 {#_53}

求，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}\sum\_{k=1}\^n\arctan{2\over k\^2}
:::

$$\lim_{n\to\infty}\sum_{k=1}^n\arctan{2\over k^2}$$
::::

结论，令，

:::: {.arithmatex}
::: {.MathJax_Preview}
\theta_1=\arctan(k+1)\\ \theta_2=\arctan(k-1)
:::

$$\theta_1=\arctan(k+1)\\
\theta_2=\arctan(k-1)$$
::::

则，

:::: {.arithmatex}
::: {.MathJax_Preview}
\tan(\theta_1-\theta_2)={(k+1)-(k-1)\over 1+(k-1)(k+1)}={2\over k\^2}
:::

$$\tan(\theta_1-\theta_2)={(k+1)-(k-1)\over 1+(k-1)(k+1)}={2\over k^2}$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
\arctan{2\over k\^2}=\arctan(k+1)-\arctan(k-1)
:::

$$\arctan{2\over k^2}=\arctan(k+1)-\arctan(k-1)$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \sum\_{k=1}\^n\arctan{2\over k\^2}&=\sum\_{k=1}\^n\arctan(k+1)-\sum\_{k=1}\^n\arctan(k-1)\\ &=\sum\_{1\le k-1\le n}\arctan k-\sum\_{1\le k+1\le n}\arctan k\\ &=\sum\_{2\le k\le n+1}\arctan k-\sum\_{0\le k\le n-1}\arctan k\\ &=\arctan(n+1)+\arctan n-\arctan0-\arctan1 \end{aligned}
:::

$$\begin{aligned}
\sum_{k=1}^n\arctan{2\over k^2}&=\sum_{k=1}^n\arctan(k+1)-\sum_{k=1}^n\arctan(k-1)\\
&=\sum_{1\le k-1\le n}\arctan k-\sum_{1\le k+1\le n}\arctan k\\
&=\sum_{2\le k\le n+1}\arctan k-\sum_{0\le k\le n-1}\arctan k\\
&=\arctan(n+1)+\arctan n-\arctan0-\arctan1
\end{aligned}$$
::::

我们知道 []{.arithmatex}$\arctan$ 的值域是 []{.arithmatex}$(-\pi/2,\pi/2)$，因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{k\to\infty}\arctan k=\pi/2
:::

$$\lim_{k\to\infty}\arctan k=\pi/2$$
::::

因此，原式，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}\sum\_{k=1}\^n\arctan{2\over k\^2}=\pi-{\pi\over4}={3\pi\over4}
:::

$$\lim_{n\to\infty}\sum_{k=1}^n\arctan{2\over k^2}=\pi-{\pi\over4}={3\pi\over4}$$
::::

### 回归基础 {#_54}

前面省略，后面，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=a_2=a_3=1\\ a\_{n+1}={2019+a_na\_{n-1}\over a\_{n-2}},n\>3
:::

$$a_1=a_2=a_3=1\\
a_{n+1}={2019+a_na_{n-1}\over a_{n-2}},n>3$$
::::

- 求证：数列每一项都是正整数。

首先正数，（显然，数列里面没有存在减法和负数，

考虑数学归纳法，对于 []{.arithmatex}$n=1,2,3$，有 []{.arithmatex}$a_n>0$，

假设对于 []{.arithmatex}$n<k(k>3)$，[]{.arithmatex}$a_n>0$，考虑证明 []{.arithmatex}$a_k>0$。

:::: {.arithmatex}
::: {.MathJax_Preview}
a_k={2019+a\_{k-1}a\_{k-2}\over a\_{k-3}}\>0
:::

$$a_k={2019+a_{k-1}a_{k-2}\over a_{k-3}}>0$$
::::

成立，因此对于 []{.arithmatex}$n\in\mathbb N^*$，[]{.arithmatex}$a_n>0$。

然后整数，我们发现 []{.arithmatex}$2019$ 是我们不想要的，怎么办捏 QAQ

我们考虑用类似特征根消掉常数的方法，错位相减，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{k+1}a\_{k-2}=2019+a_ka\_{k-1}\\ a_ka\_{k-3}=2019+a\_{k-1}a\_{k-2}
:::

$$a_{k+1}a_{k-2}=2019+a_ka_{k-1}\\
a_ka_{k-3}=2019+a_{k-1}a_{k-2}$$
::::

上减下，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{k+1}a\_{k-2}-a_ka\_{k-3}=a_ka\_{k-1}-a\_{k-1}a\_{k-2}
:::

$$a_{k+1}a_{k-2}-a_ka_{k-3}=a_ka_{k-1}-a_{k-1}a_{k-2}$$
::::

先不要冲动提右面的公因式，因为左边没有公因式 OvO

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{k-2}(a\_{k+1}+a\_{k-1})=a_k(a\_{k-1}+a\_{k-3})
:::

$$a_{k-2}(a_{k+1}+a_{k-1})=a_k(a_{k-1}+a_{k-3})$$
::::

注意到两个括号内很现实，我们喜欢哦（

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} {a\_{k+1}+a\_{k-1}\over a_k}&={a\_{k-1}+a\_{k-3}\over a\_{k-2}}\\ b_k&=b\_{k-2}(k\>3) \end{aligned}
:::

$$\begin{aligned}
{a_{k+1}+a_{k-1}\over a_k}&={a_{k-1}+a_{k-3}\over a_{k-2}}\\
b_k&=b_{k-2}(k>3)
\end{aligned}$$
::::

因此，我们有，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=a_2=a_3=1,a_4=2020
:::

$$a_1=a_2=a_3=1,a_4=2020$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_2={2,b_3=2021}\\ \dots\\ b_n=\left\\\begin{aligned} 2&\quad,n\equiv0\pmod2\\ 2021&\quad,n\equiv1\pmod2 \end{aligned}\right.
:::

$$b_2={2,b_3=2021}\\
\dots\\
b_n=\left\{\begin{aligned}
2&\quad,n\equiv0\pmod2\\
2021&\quad,n\equiv1\pmod2
\end{aligned}\right.$$
::::

也就是，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{k+1}=b_ka_k-a\_{k-1},(k\>3)
:::

$$a_{k+1}=b_ka_k-a_{k-1},(k>3)$$
::::

故都是整数。

总结：不好看的数字，没有特殊性质，考虑变形消掉。

## 例题 {#_55}

### 例题一 {#_56}

已知数列 []{.arithmatex}$\{a_n\}_{n\in\mathbb N^*}$ 满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
\forall k\in\mathbb N\^\*,a\_{k+1}+a_k=4k+3
:::

$$\forall k\in\mathbb N^*,a_{k+1}+a_k=4k+3$$
::::

- 求 []{.arithmatex}$a_1+a_{2020}$。

方法一，注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{k+1}=-a_k+4k+3\\ a_k=-a\_{k-1}+4k-1
:::

$$a_{k+1}=-a_k+4k+3\\
a_k=-a_{k-1}+4k-1$$
::::

每个叠加的项最终只会存在变号，因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_k=(-1)\^{k-1}a_1+\sum\_{i=2}\^k(-1)\^{k-i}(4i-1)
:::

$$a_k=(-1)^{k-1}a_1+\sum_{i=2}^k(-1)^{k-i}(4i-1)$$
::::

因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1+a\_{2020}=\sum\_{i=2}\^{2020}(-1)\^i(4i-1)
:::

$$a_1+a_{2020}=\sum_{i=2}^{2020}(-1)^i(4i-1)$$
::::

考虑扰动法，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \sum\_{i=2}\^{2020}(-1)\^i(4i-1)-(4\times2021-1)&=4\times2-1+\sum\_{i=2}\^{2020}(-1)\^{i+1}\[4(i+1)-1\]\\ \sum\_{i=2}\^{2020}(-1)\^i(4i-1)-8083&=7+\sum\_{i=2}\^{2020}(-1)\^{i+1}(4i+3)\\ &=7-\sum\_{i=2}\^{2020}(-1)\^i(4i-1+4)\\ &=7-\sum\_{i=2}\^{2020}(-1)\^i(4i-1)-\sum\_{i=2}\^{2020}(-1)\^i4\\ &=7-\sum\_{i=2}\^{2020}(-1)\^i(4i-1)-4 \end{aligned}
:::

$$\begin{aligned}
\sum_{i=2}^{2020}(-1)^i(4i-1)-(4\times2021-1)&=4\times2-1+\sum_{i=2}^{2020}(-1)^{i+1}[4(i+1)-1]\\
\sum_{i=2}^{2020}(-1)^i(4i-1)-8083&=7+\sum_{i=2}^{2020}(-1)^{i+1}(4i+3)\\
&=7-\sum_{i=2}^{2020}(-1)^i(4i-1+4)\\
&=7-\sum_{i=2}^{2020}(-1)^i(4i-1)-\sum_{i=2}^{2020}(-1)^i4\\
&=7-\sum_{i=2}^{2020}(-1)^i(4i-1)-4
\end{aligned}$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} 2\sum\_{i=2}\^{2020}(-1)\^i(4i+3)&=8086\\ \sum\_{i=2}\^{2020}(-1)\^i(4i+3)&=4043 \end{aligned}
:::

$$\begin{aligned}
2\sum_{i=2}^{2020}(-1)^i(4i+3)&=8086\\
\sum_{i=2}^{2020}(-1)^i(4i+3)&=4043
\end{aligned}$$
::::

后面略，因为真的不好算。

方法二，注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
S\_{2020}={2020\over2}(a_1+a\_{2020})
:::

$$S_{2020}={2020\over2}(a_1+a_{2020})$$
::::

而，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} S\_{2020}&=(a_1+a_2)+\dots+(a\_{2019}+a\_{2020})\\ &=1010\times3+4\times(1+3+\dots+2019)\\ &=1010\times3+2020\^2 \end{aligned}
:::

$$\begin{aligned}
S_{2020}&=(a_1+a_2)+\dots+(a_{2019}+a_{2020})\\
&=1010\times3+4\times(1+3+\dots+2019)\\
&=1010\times3+2020^2
\end{aligned}$$
::::

则，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1+a\_{2020}={2S\_{2020}\over2020}=3+4040=4043
:::

$$a_1+a_{2020}={2S_{2020}\over2020}=3+4040=4043$$
::::

#### 例题二：人类智慧 {#_57}

已知数列 []{.arithmatex}$\{a_n\}_{n\in\mathbb N^*}$ 满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=1,a_2=9\\ a\_{n+2}=4a\_{n+1}-3a_n-20,(n\ge1)
:::

$$a_1=1,a_2=9\\
a_{n+2}=4a_{n+1}-3a_n-20,(n\ge1)$$
::::

- 求其前 []{.arithmatex}$n$ 项和 []{.arithmatex}$S_n$ 的最大值。

注意到，减二十是很大的操作，我们充分发挥人类智慧，

于是，我们猜测数列迭代到一定程度，就会是严格单调递减的。

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=1\\ a_2=9\\ a_3=13\\ a_4=5\\ a_5=-39\\ a_6=-191
:::

$$a_1=1\\
a_2=9\\
a_3=13\\
a_4=5\\
a_5=-39\\
a_6=-191$$
::::

这个趋势已经很明显了，考虑证明，假设单减成立，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+2}=4a\_{n+1}-3a_n-20\<a\_{n+1}\\ 3(a\_{n+1}-a_n)\<20
:::

$$a_{n+2}=4a_{n+1}-3a_n-20<a_{n+1}\\
3(a_{n+1}-a_n)<20$$
::::

注意到当 []{.arithmatex}$n\ge3$ 时，上条件成立，那么，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} 3(a\_{n+1}-a_n)\<20&\Rightarrow a\_{n+2}\<a\_{n+1}\\ &\Rightarrow a\_{n+2}-a\_{n+1}\<0\\ &\Rightarrow3(a\_{n+2}-a\_{n+1})\<20\\ &\Rightarrow a\_{n+3}\<a\_{n+2}\\ &\Rightarrow\dots \end{aligned}
:::

$$\begin{aligned}
3(a_{n+1}-a_n)<20&\Rightarrow a_{n+2}<a_{n+1}\\
&\Rightarrow a_{n+2}-a_{n+1}<0\\
&\Rightarrow3(a_{n+2}-a_{n+1})<20\\
&\Rightarrow a_{n+3}<a_{n+2}\\
&\Rightarrow\dots
\end{aligned}$$
::::

即，对于 []{.arithmatex}$n\ge3$，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}\<a_n
:::

$$a_{n+1}<a_n$$
::::

于是，观察我们的列表，可以得出，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n\<0,(n\ge5)
:::

$$a_n<0,(n\ge5)$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
S\_{n\max}=S_n\|\_{n=4}=1+9+13+5=28
:::

$$S_{n\max}=S_n|_{n=4}=1+9+13+5=28$$
::::

当然也可以求出通项公式，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=10n-2\times3\^{n-1}-8
:::

$$a_n=10n-2\times3^{n-1}-8$$
::::

当 []{.arithmatex}$n$ 很大时，幂远大于线性，因此数列越来越小。

#### 例题三：邻项相减 {#_58}

一些记号省略了，后面，

:::: {.arithmatex}
::: {.MathJax_Preview}
S_n=(-1)\^na_n+{1\over2\^n}+n-3
:::

$$S_n=(-1)^na_n+{1\over2^n}+n-3$$
::::

- 求 []{.arithmatex}$a_n$ 通项。

邻项相减（或者说前缀和的差分），

:::: {.arithmatex}
::: {.MathJax_Preview}
S_n=(-1)\^na_n+{1\over2\^n}+n-3\\ S\_{n-1}=-(-1)\^na\_{n-1}+2\cdot{1\over2\^n}+n-4
:::

$$S_n=(-1)^na_n+{1\over2^n}+n-3\\
S_{n-1}=-(-1)^na_{n-1}+2\cdot{1\over2^n}+n-4$$
::::

相减，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=S_n-S\_{n-1}=(-1)\^na_n+(-1)\^na\_{n-1}-{1\over2\^n}+1
:::

$$a_n=S_n-S_{n-1}=(-1)^na_n+(-1)^na_{n-1}-{1\over2^n}+1$$
::::

分讨奇偶性，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{2k}=a\_{2k}+a\_{2k-1}-{1\over2\^{2k}}+1\\ a\_{2k-1}=-a\_{2k-1}-a\_{2k-2}-{1\over2\^{2k-1}}+1
:::

$$a_{2k}=a_{2k}+a_{2k-1}-{1\over2^{2k}}+1\\
a_{2k-1}=-a_{2k-1}-a_{2k-2}-{1\over2^{2k-1}}+1$$
::::

整理上面的，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{2k-1}={1\over2\^{2k}}-1
:::

$$a_{2k-1}={1\over2^{2k}}-1$$
::::

对于下面的，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} a\_{2k-2}&=-2a\_{2k-1}-{1\over2\^{2k-1}}+1\\ &=-{1\over2\^{2k-1}}+2-{1\over2\^{2k-1}}+1\\ &=-{1\over2\^{2k-2}}+3\\ a\_{2k}&=-{1\over2\^{2k}}+3 \end{aligned}
:::

$$\begin{aligned}
a_{2k-2}&=-2a_{2k-1}-{1\over2^{2k-1}}+1\\
&=-{1\over2^{2k-1}}+2-{1\over2^{2k-1}}+1\\
&=-{1\over2^{2k-2}}+3\\
a_{2k}&=-{1\over2^{2k}}+3
\end{aligned}$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\left\\\begin{aligned} {1\over2\^{n+1}}-1&\quad\text{if \$n\$ 是奇数}\\ -{1\over2\^n}+3&\quad\text{if \$n\$ 是偶数}\\ \end{aligned}\right.
:::

$$a_n=\left\{\begin{aligned}
{1\over2^{n+1}}-1&\quad\text{if $n$ 是奇数}\\
-{1\over2^n}+3&\quad\text{if $n$ 是偶数}\\
\end{aligned}\right.$$
::::

#### 简单题 {#_59}

数列 []{.arithmatex}$\{a_n\}$ 满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=3, a\_{n+1}=a_n\^2-3a_n+4
:::

$$a_1=3,
a_{n+1}=a_n^2-3a_n+4$$
::::

A. []{.arithmatex}$\{a_n\}$ 严格单调递增。  
B. []{.arithmatex}$\{a_n\}$ 无界。  
C. []{.arithmatex}$a_{100}=101$.  
D. []{.arithmatex}$\displaystyle\lim_{n\to\infty}\left({1\over a_1-1}+{1\over a_2-1}+\dots+{1\over a_n-1}\right)=1$.

容易发现，右侧系数 []{.arithmatex}$134$ 类似 []{.arithmatex}$144$ 的完全平方式，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}-a_n=a_n\^2-4a_n+4=(a_n-2)\^2\ge0\\ a\_{n+1}\ge a_n,\therefore a_n\ge\dots\ge a_1=3\\ (a_n-2)\^2\ge1\Rightarrow a\_{n+1}\>a_n
:::

$$a_{n+1}-a_n=a_n^2-4a_n+4=(a_n-2)^2\ge0\\
a_{n+1}\ge a_n,\therefore a_n\ge\dots\ge a_1=3\\
(a_n-2)^2\ge1\Rightarrow a_{n+1}>a_n$$
::::

由上面的，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}-a_n=(a_n-2)\^2\ge1\\ a_n\ge a\_{n+1}\\ a_2\ge4,a_3\ge5,\dots,a_n\ge n+2
:::

$$a_{n+1}-a_n=(a_n-2)^2\ge1\\
a_n\ge a_{n+1}\\
a_2\ge4,a_3\ge5,\dots,a_n\ge n+2$$
::::

于是，数列无界且，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{100}\ge102
:::

$$a_{100}\ge102$$
::::

后面不会了，注意到迭代形如 []{.arithmatex}$a_{n+1}=f(a_n)$，我们知道不动点是一个好工具，

:::: {.arithmatex}
::: {.MathJax_Preview}
x=f(x)\\ x=x\^2-3x+4\\ x\^2-4x+4=0\\ (x-2)\^2=0\\ x=2
:::

$$x=f(x)\\
x=x^2-3x+4\\
x^2-4x+4=0\\
(x-2)^2=0\\
x=2$$
::::

递归式两边同时减二，取倒数，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}-2=a_n\^2-3a_n+2=(a_n-1)(a_n-2)\\ {1\over a\_{n+1}-2}={1\over(a_n-1)(a_n-2)}={1\over a_n-2}-{1\over a_n-1}\\ {1\over a_n-1}={1\over a_n-2}-{1\over a\_{n+1}-2}
:::

$$a_{n+1}-2=a_n^2-3a_n+2=(a_n-1)(a_n-2)\\
{1\over a_{n+1}-2}={1\over(a_n-1)(a_n-2)}={1\over a_n-2}-{1\over a_n-1}\\
{1\over a_n-1}={1\over a_n-2}-{1\over a_{n+1}-2}$$
::::

注意到形如 []{.arithmatex}$f(n)=g(n)-g(n')$ 的形式，裂项成功，

:::: {.arithmatex}
::: {.MathJax_Preview}
{1\over a_1-1}+{1\over a_2-1}+\dots+{1\over a_n-1}\\ ={1\over a_1-2}-{1\over a_2-2}+{1\over a_2-2}-{1\over a_3-2}+\dots+{1\over a_n-2}-{1\over a\_{n+1}-2}\\ ={1\over a_1-2}-{1\over a\_{n+1}-2}=1-{1\over a\_{n+1}-2}
:::

$${1\over a_1-1}+{1\over a_2-1}+\dots+{1\over a_n-1}\\
={1\over a_1-2}-{1\over a_2-2}+{1\over a_2-2}-{1\over a_3-2}+\dots+{1\over a_n-2}-{1\over a_{n+1}-2}\\
={1\over a_1-2}-{1\over a_{n+1}-2}=1-{1\over a_{n+1}-2}$$
::::

注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
0\<{1\over a\_{n+1}-2}\le{1\over n+1}
:::

$$0<{1\over a_{n+1}-2}\le{1\over n+1}$$
::::

因此这一项极限为 []{.arithmatex}$0$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lim\_{n\to\infty}\left({1\over a_1-1}+{1\over a_2-1}+\dots+{1\over a_n-1}\right)=1
:::

$$\lim_{n\to\infty}\left({1\over a_1-1}+{1\over a_2-1}+\dots+{1\over a_n-1}\right)=1$$
::::

成立，故选 ABD。

#### 签到题 {#_60}

数列，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=1, a\_{n+1}=\sqrt{a_n\^2+{1\over a_n\^{2019}}}
:::

$$a_1=1,
a_{n+1}=\sqrt{a_n^2+{1\over a_n^{2019}}}$$
::::

判断数列 []{.arithmatex}$\{a_n\}$ 是否有界。

注意到该数列每一项均为正数，且都非零，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}\^2=a_n\^2+{1\over a_n\^{2019}}\\ a\_{n+1}\^2\> a_n\^2\\ a\_{n+1}\> a_n
:::

$$a_{n+1}^2=a_n^2+{1\over a_n^{2019}}\\
a_{n+1}^2> a_n^2\\
a_{n+1}> a_n$$
::::

严格单调递增，故无界。

证明，反证法：

假设数列有界，记为 []{.arithmatex}$L$，两边取极限，

:::: {.arithmatex}
::: {.MathJax_Preview}
L\^2=L\^2+{1\over L\^{2019}}
:::

$$L^2=L^2+{1\over L^{2019}}$$
::::

显然无界，不成立。
