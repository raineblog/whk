# 数学归纳法 {#_1}

数学归纳法是证明某个命题对于所有满足 []{.arithmatex}$n\ge n_0$ 的整数 []{.arithmatex}$n$ 都成立的一般方法。首先我们在 []{.arithmatex}$n$ 取 最小值 []{.arithmatex}$n_0$ 时证明该命题，这一步骤成为**基础**。然后对 []{.arithmatex}$n>n_0$，假设该命题对 []{.arithmatex}$n_0\sim n-1$ 之间的所有值已经被证明，再证明该命题对 []{.arithmatex}$n$ 成立，这一步骤成为**归纳**。

这样一种证明方法仅用有限步就得到无限多个结果。

## 皮亚诺公理 {#_2}

一个最简单的例子，皮亚诺公理的自然数定义：

1.  []{.arithmatex}$0$ 是自然数；
2.  每一个确定的自然数 []{.arithmatex}$a$，都有一个确定的后继 []{.arithmatex}$a'$，[]{.arithmatex}$a'$ 也是自然数；
3.  对于每个自然数 []{.arithmatex}$b,c$，[]{.arithmatex}$b=c$ 当且仅当 []{.arithmatex}$b'=c'$；
4.  []{.arithmatex}$0$ 不是任何自然数的后继；
5.  任意关于自然数的命题，如果证明：
    - 它对 []{.arithmatex}$0$ 成立，且假定它对自然数 []{.arithmatex}$a'$ 为真时，
    - 可以证明它对 []{.arithmatex}$a'$ 也成立。
    - 那么该命题对所有自然数都成立。

公理 []{.arithmatex}$5$ 保证了数学归纳法的正确性，从而被称为归纳法原理。

PS：在集合论和计算机科学领域中，认为 []{.arithmatex}$0$ 属于自然数。

但在数论领域中，认为 []{.arithmatex}$0$ 不属于自然数，因而按数论描述，自然数会同义于正整数。

因此，如果定义 []{.arithmatex}$0$ 不属于自然数，把上面的 []{.arithmatex}$0$ 改成 []{.arithmatex}$1$ 即可。

### 戴德金-皮亚诺结构 {#-}

戴德金-皮亚诺结构可以描述为满足所有以下条件的三元组 []{.arithmatex}$(S,f,e)$：

1.  []{.arithmatex}$(e\in S)$
2.  []{.arithmatex}$(\forall a\in S)(f(a)\in S)$
3.  []{.arithmatex}$(\forall b\in S)(\forall c\in S)((f(b)=f(c))\Rightarrow(b=c))$
4.  []{.arithmatex}$(\forall a\in S)(f(a)\neq e)$
5.  []{.arithmatex}$(\forall A\subseteq S)(((e\in A)\wedge(\forall a\in A)(f(a)\in A))\Rightarrow(A=S))$

一个形象化的例子就是最上面的，即三元组 []{.arithmatex}$(\mathbb N,(f:\mathbb N\to\mathbb N_+;\;x\mapsto(x+1)),0)$。

## 正向数学归纳法 {#_3}

此处不区分第一数学归纳法，第二数学归纳法。

### 例子 {#_4}

证明，

:::: {.arithmatex}
::: {.MathJax_Preview}
S_n=1+2+\dots+n={n(n+1)\over2}
:::

$$S_n=1+2+\dots+n={n(n+1)\over2}$$
::::

由于，

:::: {.arithmatex}
::: {.MathJax_Preview}
1={1\times2\over2}
:::

$$1={1\times2\over2}$$
::::

假设我们已经证明，

:::: {.arithmatex}
::: {.MathJax_Preview}
S\_{n-1}={n(n-1)\over2}
:::

$$S_{n-1}={n(n-1)\over2}$$
::::

那么，

:::: {.arithmatex}
::: {.MathJax_Preview}
S_n=S\_{n-1}+n={n(n-1)\over2}+n={n(n+1)\over2}
:::

$$S_n=S_{n-1}+n={n(n-1)\over2}+n={n(n+1)\over2}$$
::::

则，其对于任意自然数成立。

### 应用 {#_5}

解递归式，

:::: {.arithmatex}
::: {.MathJax_Preview}
Q_0=\alpha,Q_1=\beta\\ Q_n={1+Q\_{n-1}\over Q\_{n-2}},n\>1
:::

$$Q_0=\alpha,Q_1=\beta\\
Q_n={1+Q_{n-1}\over Q_{n-2}},n>1$$
::::

容易发现，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{array}{c\|c} \begin{aligned} Q_0&=\alpha\\ Q_1&=\beta\\ Q_2&={1+\beta\over\alpha}\\ Q_3&={1+\alpha+\beta\over\alpha\beta}\\ Q_4&={1+\alpha\over\beta} \end{aligned}& \begin{aligned} Q_5&=\alpha\\ Q_6&=\beta\\ \dots\\\\\\\\\\ \end{aligned} \end{array}
:::

$$\begin{array}{c|c}
\begin{aligned}
Q_0&=\alpha\\
Q_1&=\beta\\
Q_2&={1+\beta\over\alpha}\\
Q_3&={1+\alpha+\beta\over\alpha\beta}\\
Q_4&={1+\alpha\over\beta}
\end{aligned}&
\begin{aligned}
Q_5&=\alpha\\
Q_6&=\beta\\
\dots\\\\\\\\\\
\end{aligned}
\end{array}$$
::::

是一个周期函数，结论：

:::: {.arithmatex}
::: {.MathJax_Preview}
Q_n=\left\\\begin{aligned} &\alpha&\kern{1em}\operatorname{if}n\equiv0\pmod5\\ &\beta&\kern{1em}\operatorname{if}n\equiv1\pmod5\\ &{1+\beta\over\alpha}&\kern{1em}\operatorname{if}n\equiv2\pmod5\\ &{1+\alpha+\beta\over\alpha\beta}&\kern{1em}\operatorname{if}n\equiv3\pmod5\\ &{1+\alpha\over\beta}&\kern{1em}\operatorname{if}n\equiv4\pmod5\\ \end{aligned}\right.
:::

$$Q_n=\left\{\begin{aligned}
&\alpha&\kern{1em}\operatorname{if}n\equiv0\pmod5\\
&\beta&\kern{1em}\operatorname{if}n\equiv1\pmod5\\
&{1+\beta\over\alpha}&\kern{1em}\operatorname{if}n\equiv2\pmod5\\
&{1+\alpha+\beta\over\alpha\beta}&\kern{1em}\operatorname{if}n\equiv3\pmod5\\
&{1+\alpha\over\beta}&\kern{1em}\operatorname{if}n\equiv4\pmod5\\
\end{aligned}\right.$$
::::

证明：

对于 []{.arithmatex}$n\in[0,5)$，易证。

假设对于 []{.arithmatex}$n=5k+q,k\le t,k\in\mathbb Z,q\in[0,5)$ 成立。

证明对于 []{.arithmatex}$n=5(k+1)+q$ 也成立，以 []{.arithmatex}$n=5(k+1)$ 为例，

:::: {.arithmatex}
::: {.MathJax_Preview}
Q\_{5(k+1)}={1+Q\_{5(k+1)-1}\over Q\_{5(k+1)-2}}={1+Q\_{5k+4}\over Q\_{5k+3}}=\alpha
:::

$$Q_{5(k+1)}={1+Q_{5(k+1)-1}\over Q_{5(k+1)-2}}={1+Q_{5k+4}\over Q_{5k+3}}=\alpha$$
::::

对于 []{.arithmatex}$q=2,3,4$，同理，略。

## 反向数学归纳法 {#_6}

反向数学归纳法，是从 []{.arithmatex}$n$ 到 []{.arithmatex}$n-1$ 来证明命题，而不是相反。

例如，证明：

:::: {.arithmatex}
::: {.MathJax_Preview}
\prod\_{i=1}\^nx_i\le\left({\sum\_{i=1}\^nx_i\over n}\right)\^n
:::

$$\prod_{i=1}^nx_i\le\left({\sum_{i=1}^nx_i\over n}\right)^n$$
::::

对于 []{.arithmatex}$x_1,x_2\dots x_n\ge0$。

证明：

记命题，

:::: {.arithmatex}
::: {.MathJax_Preview}
P(n):x_1\dots x_n\le\left({x_1+\dots+x_n\over n}\right)\^n
:::

$$P(n):x_1\dots x_n\le\left({x_1+\dots+x_n\over n}\right)^n$$
::::

则，

:::: {.arithmatex}
::: {.MathJax_Preview}
P(1):x_1\le x_1
:::

$$P(1):x_1\le x_1$$
::::

显然成立。

:::: {.arithmatex}
::: {.MathJax_Preview}
P(2):x_1x_2\le\left({x_1+x_2\over2}\right)\^2
:::

$$P(2):x_1x_2\le\left({x_1+x_2\over2}\right)^2$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
4x_1x_2\le x_1\^2+2x_1x_2+x_2\^2\\ x_1\^2-2x_1x_2+x_2\^2\ge0
:::

$$4x_1x_2\le x_1^2+2x_1x_2+x_2^2\\
x_1^2-2x_1x_2+x_2^2\ge0$$
::::

显然成立。

即，[]{.arithmatex}$P(1),P(2)$ 成立。

### 性质一 {#_7}

若 []{.arithmatex}$P(n)$ 成立，则 []{.arithmatex}$P(n-1)$ 也成立。

记，

:::: {.arithmatex}
::: {.MathJax_Preview}
x_n={x_1+\dots+x\_{n-1}\over n-1}
:::

$$x_n={x_1+\dots+x_{n-1}\over n-1}$$
::::

则 []{.arithmatex}$P(n)$ 为，

:::: {.arithmatex}
::: {.MathJax_Preview}
x_1\dots x\_{n-1}\cdot{x_1+\dots+x\_{n-1}\over n-1}\le\left({x_1+\dots+x\_{n-1}\over n-1}\right)\^n
:::

$$x_1\dots x_{n-1}\cdot{x_1+\dots+x_{n-1}\over n-1}\le\left({x_1+\dots+x_{n-1}\over n-1}\right)^n$$
::::

即 []{.arithmatex}$P(n-1)$，

:::: {.arithmatex}
::: {.MathJax_Preview}
x_1\dots x\_{n-1}\le\left({x_1+\dots+x\_{n-1}\over n-1}\right)\^{n-1}
:::

$$x_1\dots x_{n-1}\le\left({x_1+\dots+x_{n-1}\over n-1}\right)^{n-1}$$
::::

Q.E.D.

### 性质二 {#_8}

若 []{.arithmatex}$P(n)$ 成立，则 []{.arithmatex}$P(2n)$ 成立。

我们记第一个 []{.arithmatex}$P(n)$ 为，

:::: {.arithmatex}
::: {.MathJax_Preview}
x_1\dots x_n\le\left({x_1+\dots+x_n\over n}\right)\^n
:::

$$x_1\dots x_n\le\left({x_1+\dots+x_n\over n}\right)^n$$
::::

同样的，记第二个 []{.arithmatex}$P(n)$ 为，

:::: {.arithmatex}
::: {.MathJax_Preview}
x\_{n+1}\dots x\_{2n}\le\left({x\_{n+1}+\dots+x\_{2n}\over n}\right)\^n
:::

$$x_{n+1}\dots x_{2n}\le\left({x_{n+1}+\dots+x_{2n}\over n}\right)^n$$
::::

我们知道 []{.arithmatex}$P(2)$ 是成立的，记

:::: {.arithmatex}
::: {.MathJax_Preview}
y_1=x_1\dots x_n\\ y_2=x\_{n+1}\dots x\_{2n}
:::

$$y_1=x_1\dots x_n\\
y_2=x_{n+1}\dots x_{2n}$$
::::

对 []{.arithmatex}$y_1,y_2$ 应用 []{.arithmatex}$P(2)$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} y_1y_2&\le\left({y_1+y_2\over2}\right)\^2\\ x_1\dots x\_{2n}&\le\left(x_1\dots x_n+x\_{n+1}\dots x\_{2n}\over2\right)\^2\\ &={(x_1\dots x_n)\^2+(x\_{n+1}+x\_{2n})\^2+2x_1\dots x\_{2n}\over4}\\ &={(x_1\dots x_n)\^2+(x\_{n+1}+x\_{2n})\^2\over2}\\ &\le{(x_1+\dots+x_n)\^{2n}+(x\_{n+1}+\dots+x\_{2n})\^{2n}\over(2n)\^{2n}}\\ &\le\left({x_1+\dots+x\_{2n}\over2n}\right)\^{2n} \end{aligned}
:::

$$\begin{aligned}
y_1y_2&\le\left({y_1+y_2\over2}\right)^2\\
x_1\dots x_{2n}&\le\left(x_1\dots x_n+x_{n+1}\dots x_{2n}\over2\right)^2\\
&={(x_1\dots x_n)^2+(x_{n+1}+x_{2n})^2+2x_1\dots x_{2n}\over4}\\
&={(x_1\dots x_n)^2+(x_{n+1}+x_{2n})^2\over2}\\
&\le{(x_1+\dots+x_n)^{2n}+(x_{n+1}+\dots+x_{2n})^{2n}\over(2n)^{2n}}\\
&\le\left({x_1+\dots+x_{2n}\over2n}\right)^{2n}
\end{aligned}$$
::::

即，[]{.arithmatex}$P(2n)$。

Q.E.D.

### 整理 {#_9}

根据，

:::: {.arithmatex}
::: {.MathJax_Preview}
P(1),P(2)\\ P(n)\Rightarrow P(2n)\\ P(n)\Rightarrow P(n-1)
:::

$$P(1),P(2)\\
P(n)\Rightarrow P(2n)\\
P(n)\Rightarrow P(n-1)$$
::::

我们可以知道，对于 []{.arithmatex}$\forall n\in\mathbb N^*$，[]{.arithmatex}$P(n)$ 成立。

END.
