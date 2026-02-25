# 数学归纳法 {#_1}

数学归纳法是证明某个命题对于所有满足 $n\ge n_0$ 的整数 $n$ 都成立的一般方法。首先我们在 $n$ 取 最小值 $n_0$ 时证明该命题，这一步骤成为**基础**。然后对 $n>n_0$，假设该命题对 $n_0\sim n-1$ 之间的所有值已经被证明，再证明该命题对 $n$ 成立，这一步骤成为**归纳**。

这样一种证明方法仅用有限步就得到无限多个结果。

## 皮亚诺公理 {#_2}

一个最简单的例子，皮亚诺公理的自然数定义：

1.  $0$ 是自然数；
2.  每一个确定的自然数 $a$，都有一个确定的后继 $a'$，$a'$ 也是自然数；
3.  对于每个自然数 $b,c$，$b=c$ 当且仅当 $b'=c'$；
4.  $0$ 不是任何自然数的后继；
5.  任意关于自然数的命题，如果证明：
    - 它对 $0$ 成立，且假定它对自然数 $a'$ 为真时，
    - 可以证明它对 $a'$ 也成立。
    - 那么该命题对所有自然数都成立。

公理 $5$ 保证了数学归纳法的正确性，从而被称为归纳法原理。

PS：在集合论和计算机科学领域中，认为 $0$ 属于自然数。

但在数论领域中，认为 $0$ 不属于自然数，因而按数论描述，自然数会同义于正整数。

因此，如果定义 $0$ 不属于自然数，把上面的 $0$ 改成 $1$ 即可。

### 戴德金-皮亚诺结构 {#-}

戴德金-皮亚诺结构可以描述为满足所有以下条件的三元组 $(S,f,e)$：

1.  $(e\in S)$
2.  $(\forall a\in S)(f(a)\in S)$
3.  $(\forall b\in S)(\forall c\in S)((f(b)=f(c))\Rightarrow(b=c))$
4.  $(\forall a\in S)(f(a)\neq e)$
5.  $(\forall A\subseteq S)(((e\in A)\wedge(\forall a\in A)(f(a)\in A))\Rightarrow(A=S))$

一个形象化的例子就是最上面的，即三元组 $(\mathbb N,(f:\mathbb N\to\mathbb N_+;\;x\mapsto(x+1)),0)$。

## 正向数学归纳法 {#_3}

此处不区分第一数学归纳法，第二数学归纳法。

### 例子 {#_4}

证明，

$$
S_n=1+2+\dots+n={n(n+1)\over2}
$$

由于，

$$
1={1\times2\over2}
$$

假设我们已经证明，

$$
S_{n-1}={n(n-1)\over2}
$$

那么，

$$
S_n=S_{n-1}+n={n(n-1)\over2}+n={n(n+1)\over2}
$$

则，其对于任意自然数成立。

### 应用 {#_5}

解递归式，

$$
Q_0=\alpha,Q_1=\beta\ Q_n={1+Q_{n-1}\over Q_{n-2}},n>1
$$

容易发现，

$$
\begin{array}{c|c} \begin{aligned} Q_0&=\alpha\ Q_1&=\beta\ Q_2&={1+\beta\over\alpha}\ Q_3&={1+\alpha+\beta\over\alpha\beta}\ Q_4&={1+\alpha\over\beta} \end{aligned}& \begin{aligned} Q_5&=\alpha\ Q_6&=\beta\ \dots\\\ \end{aligned} \end{array}
$$

是一个周期函数，结论：

$$
Q_n=\left{\begin{aligned} &\alpha&\kern{1em}\operatorname{if}n\equiv0\pmod5\ &\beta&\kern{1em}\operatorname{if}n\equiv1\pmod5\ &{1+\beta\over\alpha}&\kern{1em}\operatorname{if}n\equiv2\pmod5\ &{1+\alpha+\beta\over\alpha\beta}&\kern{1em}\operatorname{if}n\equiv3\pmod5\ &{1+\alpha\over\beta}&\kern{1em}\operatorname{if}n\equiv4\pmod5\ \end{aligned}\right.
$$

证明：

对于 $n\in[0,5)$，易证。

假设对于 $n=5k+q,k\le t,k\in\mathbb Z,q\in[0,5)$ 成立。

证明对于 $n=5(k+1)+q$ 也成立，以 $n=5(k+1)$ 为例，

$$
Q_{5(k+1)}={1+Q_{5(k+1)-1}\over Q_{5(k+1)-2}}={1+Q_{5k+4}\over Q_{5k+3}}=\alpha
$$

对于 $q=2,3,4$，同理，略。

## 反向数学归纳法 {#_6}

反向数学归纳法，是从 $n$ 到 $n-1$ 来证明命题，而不是相反。

例如，证明：

$$
\prod_{i=1}^nx_i\le\left({\sum_{i=1}^nx_i\over n}\right)^n
$$

对于 $x_1,x_2\dots x_n\ge0$。

证明：

记命题，

$$
P(n):x_1\dots x_n\le\left({x_1+\dots+x_n\over n}\right)^n
$$

则，

$$
P(1):x_1\le x_1
$$

显然成立。

$$
P(2):x_1x_2\le\left({x_1+x_2\over2}\right)^2
$$

即，

$$
4x_1x_2\le x_1^2+2x_1x_2+x_2^2\ x_1^2-2x_1x_2+x_2^2\ge0
$$

显然成立。

即，$P(1),P(2)$ 成立。

### 性质一 {#_7}

若 $P(n)$ 成立，则 $P(n-1)$ 也成立。

记，

$$
x_n={x_1+\dots+x_{n-1}\over n-1}
$$

则 $P(n)$ 为，

$$
x_1\dots x_{n-1}\cdot{x_1+\dots+x_{n-1}\over n-1}\le\left({x_1+\dots+x_{n-1}\over n-1}\right)^n
$$

即 $P(n-1)$，

$$
x_1\dots x_{n-1}\le\left({x_1+\dots+x_{n-1}\over n-1}\right)^{n-1}
$$

Q.E.D.

### 性质二 {#_8}

若 $P(n)$ 成立，则 $P(2n)$ 成立。

我们记第一个 $P(n)$ 为，

$$
x_1\dots x_n\le\left({x_1+\dots+x_n\over n}\right)^n
$$

同样的，记第二个 $P(n)$ 为，

$$
x_{n+1}\dots x_{2n}\le\left({x_{n+1}+\dots+x_{2n}\over n}\right)^n
$$

我们知道 $P(2)$ 是成立的，记

$$
y_1=x_1\dots x_n\ y_2=x_{n+1}\dots x_{2n}
$$

对 $y_1,y_2$ 应用 $P(2)$，

$$
\begin{aligned} y_1y_2&\le\left({y_1+y_2\over2}\right)^2\ x_1\dots x_{2n}&\le\left(x_1\dots x_n+x_{n+1}\dots x_{2n}\over2\right)^2\ &={(x_1\dots x_n)^2+(x_{n+1}+x_{2n})^2+2x_1\dots x_{2n}\over4}\ &={(x_1\dots x_n)^2+(x_{n+1}+x_{2n})^2\over2}\ &\le{(x_1+\dots+x_n)^{2n}+(x_{n+1}+\dots+x_{2n})^{2n}\over(2n)^{2n}}\ &\le\left({x_1+\dots+x_{2n}\over2n}\right)^{2n} \end{aligned}
$$

即，$P(2n)$。

Q.E.D.

### 整理 {#_9}

根据，

$$
P(1),P(2)\ P(n)\Rightarrow P(2n)\ P(n)\Rightarrow P(n-1)
$$

我们可以知道，对于 $\forall n\in\mathbb N^*$，$P(n)$ 成立。

END.
