# 数列基础 {#_1}

## 基础概念 {#_2}

**数列**是由数字组成的有序序列，数列中的每一个数都叫做这个数列的**项**。

**项数**有限的数列成为**有限数列**，项数无穷多的成为**无穷数列**。

排在第一位的数称为这个数列的**首项**，有限数列的最后一个数成为这个数列的**末项**。

注意：无穷数列只有首项，没有末项。

对于数列，更严谨的定义，考虑最一般的复数，下文再说。

### 无穷数列 {#_3}

一个 []{.arithmatex}$(a:\mathbb N\to\mathbb C)$ 的函数被称为**无穷数列**。

可记为 []{.arithmatex}$\{a_i\}_{i\in\mathbb N}$ 或 []{.arithmatex}$(a_i)_{i\in\mathbb N}$ 或 []{.arithmatex}$\langle a_i\rangle_{i\in\mathbb N}$。

一个数列 []{.arithmatex}$a$ 的第 []{.arithmatex}$i$ 项，通常记为 []{.arithmatex}$a(i)$，简记为 []{.arithmatex}$a_i$。

### 有限数列 {#_4}

若 []{.arithmatex}$I_n=\{1,2,\dots,n\}$，则一个 []{.arithmatex}$(a:I_n\to\mathbb C)$ 的函数被称为**有限数列**。

可记为 []{.arithmatex}$\{a_i\}_{i=1}^n$ 或 []{.arithmatex}$(a_i)_{i=1}^n$ 或 []{.arithmatex}$\langle a_i\rangle_{i=1}^n$。

同时，也可以将 []{.arithmatex}$0$ 作为数列的首项，类似的。

### 数列的级数 {#_5}

数列中各个项的和称为**级数**，具体的，

一个数列 []{.arithmatex}$a_i\,(i\in\mathbb N)$ 的级数是另外一个数列 []{.arithmatex}$s_i\,(i\in\mathbb N)$，具有以下特性：

- []{.arithmatex}$s_0=a_0$，
- []{.arithmatex}$s_n=s_{n-1}+a_n\,(\forall n\in\mathbb Z^*)$

一般会将 []{.arithmatex}$\{s_i\}_{i\in\mathbb N}$ 写为，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sum \_{i=0}\^na_i
:::

$$\sum _{i=0}^na_i$$
::::

甚至更直观的 []{.arithmatex}$a_0+a_1+\dots +a_n$ 来凸显级数源于求和的直观概念。

对于从 []{.arithmatex}$1$ 开始的数列，同理，一般直接使用求和符号简记为，

:::: {.arithmatex}
::: {.MathJax_Preview}
s_i=\sum\_{i=1}\^na_i
:::

$$s_i=\sum_{i=1}^na_i$$
::::

### 数列与函数 {#_6}

我们知道函数和数列都是一种映射，只不过，函数一般是连续的，而数列一般是离散的。

容易发现，数列，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=f(n)
:::

$$a_n=f(n)$$
::::

其级数，即为 []{.arithmatex}$f$ 函数的积分，

:::: {.arithmatex}
::: {.MathJax_Preview}
s_n=g(n)
:::

$$s_n=g(n)$$
::::

其差分，即为 []{.arithmatex}$f$ 函数的微分，

:::: {.arithmatex}
::: {.MathJax_Preview}
d_n=k(n)
:::

$$d_n=k(n)$$
::::

我们在数列进阶部分讨论。

## 表示方法 {#_7}

### 列举法 {#_8}

例如：

:::: {.arithmatex}
::: {.MathJax_Preview}
a=\langle1,2,4,8,16\rangle
:::

$$a=\langle1,2,4,8,16\rangle$$
::::

对于无穷数列很不好用。

### 图像法 {#_9}

- 数列是离散的，因此数列的图像是一个散点图。

- 一般这个不好用。

下面我们介绍几个常用的表示方法：通项公式和递推公式。

### 通项公式 {#_10}

定义，表示 []{.arithmatex}$n$ 和 []{.arithmatex}$a_n$ 的关系的公式，叫做 []{.arithmatex}$a$ 的**通项公式**。

把数列看成函数的形式，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=f(n)
:::

$$a_n=f(n)$$
::::

数列对应函数的解析式，被称为数列的通项公式。

例如，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=2\^n
:::

$$a_n=2^n$$
::::

### 递推公式 {#_11}

定义，表示 []{.arithmatex}$a_n$ 和 []{.arithmatex}$a_n$ 的前一或前几项的关系的公式，叫做 []{.arithmatex}$a$ 的**递推公式**。

例如，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}=a_n+2
:::

$$a_{n+1}=a_n+2$$
::::

特殊的，如果要根据递推公式确定一个数列，还需要知道数列的任意一项。

一般会表示数列的首项，例如，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=1
:::

$$a_1=1$$
::::

如果一个数列只跟其前面的 []{.arithmatex}$k$ 项有关，其中 []{.arithmatex}$k$ 是满足这个条件的最小正整数，

那么称这个数列的阶数为 []{.arithmatex}$k$，即这个数列是一个 []{.arithmatex}$k$ 阶数列。

## 等差数列 {#_12}

在等差数列中，任何相邻两项的差相等，该差值称为**公差** []{.arithmatex}$d$。

具体的，可以表示为，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=d+qn
:::

$$a_n=d+qn$$
::::

的，都是等差数列。

上式中，公差为 []{.arithmatex}$d$，首项 []{.arithmatex}$a_1=d+q$。

- 若 []{.arithmatex}$d>0$，等差数列为一个严格单调递增数列。
- 若 []{.arithmatex}$d<0$，等差数列为一个严格单调递减数列。
- 特殊的，若 []{.arithmatex}$d=0$，等差数列退化为一个常数列。

### 递推公式 {#_13}

形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a\_{n+1}=a_n+d,(n\in\mathbb Z\^\*)}
:::

$$\boxed{a_{n+1}=a_n+d,(n\in\mathbb Z^*)}$$
::::

或者记为，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}-a_n=d
:::

$$a_{n+1}-a_n=d$$
::::

即公差的定义式。

### 通项公式 {#_14}

形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a_n=a_1+(n-1)d}
:::

$$\boxed{a_n=a_1+(n-1)d}$$
::::

即，角标减一，等于公差个数。

或者对于从 []{.arithmatex}$0$ 开始的数列，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=a_0+nd
:::

$$a_n=a_0+nd$$
::::

前面的一项即为首项，其与公差需为给定的确定的数。

### 等差性质 {#_15}

除了上述几条，

给定任意两项 []{.arithmatex}$a_n,a_m$，则公差，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{d={a_n-a_m\over n-m}}
:::

$$\boxed{d={a_n-a_m\over n-m}}$$
::::

在等差数列中，前项与后项和为该项两倍，具体的，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} a\_{n-1}+a\_{n+1}&=a_n-d+a_n+d\\ &=2a_n \end{aligned}
:::

$$\begin{aligned}
a_{n-1}+a_{n+1}&=a_n-d+a_n+d\\
&=2a_n
\end{aligned}$$
::::

从另一个角度看，等差数列中的任意一项，是其前项和后项的算术平均：

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n={a\_{n-1}+a\_{n+1}\over2}
:::

$$a_n={a_{n-1}+a_{n+1}\over2}$$
::::

对于正整数 []{.arithmatex}$m,n,p,q$，若 []{.arithmatex}$m+n=p+q$，则，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a_m+a_n=a_p+a_q}
:::

$$\boxed{a_m+a_n=a_p+a_q}$$
::::

或者简化一下，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a_m+a_n=a\_{m-k}+a\_{n+k}}
:::

$$\boxed{a_m+a_n=a_{m-k}+a_{n+k}}$$
::::

据此，有，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a\_{n-k}+a\_{n+k}=2a_n}
:::

$$\boxed{a_{n-k}+a_{n+k}=2a_n}$$
::::

对于 []{.arithmatex}$a_{n-k},a_n,a_{n+k}$ 有意义。据此，同理，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n={a\_{n-k}+a\_{n+k}\over2}
:::

$$a_n={a_{n-k}+a_{n+k}\over2}$$
::::

若 []{.arithmatex}$\langle a_n\rangle$ 为一个等差数列，则，

- []{.arithmatex}$\langle b+a_n\rangle$：为一个等差数列；
- []{.arithmatex}$\langle b\times a_n\rangle$：为一个等差数列；
- []{.arithmatex}$\langle b^{a_n}\rangle$：为一个等比数列（见下）；

### 项数公式 {#_16}

给定等差数列首项 []{.arithmatex}$a_1$ 及公差 []{.arithmatex}$d$，有项 []{.arithmatex}$a_k$，则，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} a_k=a_1+(k-1)d\\ k-1={a_k-a_1\over d}\\ \boxed{k={a_k-a_1\over d}+1} \end{aligned}
:::

$$\begin{aligned}
a_k=a_1+(k-1)d\\
k-1={a_k-a_1\over d}\\
\boxed{k={a_k-a_1\over d}+1}
\end{aligned}$$
::::

或对于 []{.arithmatex}$a_0$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} a_k=a_0+kd\\ k={a_k-a_0\over d}\\ \end{aligned}
:::

$$\begin{aligned}
a_k=a_0+kd\\
k={a_k-a_0\over d}\\
\end{aligned}$$
::::

另外的，函数思想，有，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} a_n=f(n)\\ n=g(a_n) \end{aligned}
:::

$$\begin{aligned}
a_n=f(n)\\
n=g(a_n)
\end{aligned}$$
::::

即 []{.arithmatex}$f,g$ 互为反函数，这个可以用于求多种数列。

### 求和公式 {#_17}

一般考虑，

:::: {.arithmatex}
::: {.MathJax_Preview}
S_i=\sum\_{i=1}\^na_i
:::

$$S_i=\sum_{i=1}^na_i$$
::::

有常用公式，

:::: {.arithmatex}
::: {.MathJax_Preview}
S_n-S\_{n-1}=a_n
:::

$$S_n-S_{n-1}=a_n$$
::::

考虑求解出，求和公式的封闭形式，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} S_n&=a_1+(a_1+d)+(a_1+2d)+\dots+\[a_1+(n-1)d\]\\ &=na_1+d\[1+2+3+\dots(n-1)\]\\ &=na_1+dT\_{n-1} \end{aligned}
:::

$$\begin{aligned}
S_n&=a_1+(a_1+d)+(a_1+2d)+\dots+[a_1+(n-1)d]\\
&=na_1+d[1+2+3+\dots(n-1)]\\
&=na_1+dT_{n-1}
\end{aligned}$$
::::

而对于，

:::: {.arithmatex}
::: {.MathJax_Preview}
T_n=1+2+3+\dots+n
:::

$$T_n=1+2+3+\dots+n$$
::::

我们首尾配对，

:::: {.arithmatex}
::: {.MathJax_Preview}
T_n=n+(n-1)+\dots+1
:::

$$T_n=n+(n-1)+\dots+1$$
::::

两者相加，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} 2T_n=n(n+1)\\ T_n=n(n+1)/2 \end{aligned}
:::

$$\begin{aligned}
2T_n=n(n+1)\\
T_n=n(n+1)/2
\end{aligned}$$
::::

另，一般题中出现 []{.arithmatex}$x_1 + x_2 = k$（[]{.arithmatex}$k$ 为常数），且 []{.arithmatex}$f(x_1) + f(x_2) = \ell$（[]{.arithmatex}$\ell$ 为常数）时，可以采用倒序相加的方法进行求和。

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} S_n&=na_1+dT\_{n-1}\\ &=\boxed{na_1+{n(n-1)\over2}d}\\ &={n\over2}\[2a_1+(n-1)d\]\\ &=\boxed{{n(a_1+a_n)\over2}} \end{aligned}
:::

$$\begin{aligned}
S_n&=na_1+dT_{n-1}\\
&=\boxed{na_1+{n(n-1)\over2}d}\\
&={n\over2}[2a_1+(n-1)d]\\
&=\boxed{{n(a_1+a_n)\over2}}
\end{aligned}$$
::::

或者，对于原始公式直接首尾配对，用上面的结论，也可以得出。

总结一下，一般写为，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{S_n={\[2a_1+(n-1)\]d\over2}\cdot n={n(a_1+a_n)\over2}}
:::

$$\boxed{S_n={[2a_1+(n-1)]d\over2}\cdot n={n(a_1+a_n)\over2}}$$
::::

常用二次函数的思想：

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{S_n={d\over2}n\^2+\left(a_1-{d\over2}\right)n}
:::

$$\boxed{S_n={d\over2}n^2+\left(a_1-{d\over2}\right)n}$$
::::

据此，可以等差数列和的极点存在于，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{n={d/2-a_1\over d}={1\over2}-{a_1\over d}}
:::

$$\boxed{n={d/2-a_1\over d}={1\over2}-{a_1\over d}}$$
::::

我们发现，该函数图像过原点，因此我们定义，

:::: {.arithmatex}
::: {.MathJax_Preview}
S_0=0
:::

$$S_0=0$$
::::

同时，对于上面的式子，如果我们假设存在 []{.arithmatex}$a_0$，那么求和，

得出很重要的一个结论，任何一个二次函数，都可以表示为一个等差数列的级数。

也就是说：数列 []{.arithmatex}$\{a_n\}$ 是等差数列，等价于 []{.arithmatex}$S_n=An^2+Bn$，等价于 []{.arithmatex}$\left\{\dfrac{S_n}{n}\right\}$ 为等差数列。

等差数列和在中文教科书中常表达为：

一个等差数列的和，等于其首项与末项的和，乘以项数除以二。

对于等差数列的前 []{.arithmatex}$n$ 项和，也可以将其构造为等差数列。等差数列 []{.arithmatex}$\{a_n\}$，设公差为 []{.arithmatex}$d$，若前 []{.arithmatex}$n$ 项和为 []{.arithmatex}$S_n$，则 []{.arithmatex}$\{S_m,S_{2m}-S_m,S_{3m}-S_{2m}\}$ 仍构成等差数列，公差为 []{.arithmatex}$m^2d$。

如果数列 []{.arithmatex}$\{a_n\}$ 为等差数列，[]{.arithmatex}$\{a_n\}$ 的前 []{.arithmatex}$n$ 项和 []{.arithmatex}$S_n$ 有如下结论：

- 若 []{.arithmatex}$a_1 < 0, d > 0$，且此时 []{.arithmatex}$n$ 满足 []{.arithmatex}$\begin{cases} a_n \le 0 \\ a_{n+1} \ge 0 \end{cases}$，则 []{.arithmatex}$S_n$ 有最小值；

- 若 []{.arithmatex}$a_1 > 0, d < 0$，且此时 []{.arithmatex}$n$ 满足 []{.arithmatex}$\begin{cases} a_n \ge 0 \\ a_{n+1} \le 0 \end{cases}$，则 []{.arithmatex}$S_n$ 有最大值。

### 等差中项 {#_18}

对于 []{.arithmatex}$a,b$，有 []{.arithmatex}$c$ 满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
c-a=b-c
:::

$$c-a=b-c$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
c={a+b\over2}
:::

$$c={a+b\over2}$$
::::

即算术平均数。

或者，若 []{.arithmatex}$\{a,b,c\}$ 为一个等差数列，那么

:::: {.arithmatex}
::: {.MathJax_Preview}
b-a=c-b
:::

$$b-a=c-b$$
::::

一般写为，

:::: {.arithmatex}
::: {.MathJax_Preview}
a+c=2b
:::

$$a+c=2b$$
::::

可以用这个来判断一个三项数列是否为等差数列。

例题，对于等差数列 []{.arithmatex}$\{a,b,c\}$，证明，

:::: {.arithmatex}
::: {.MathJax_Preview}
\left\\{1\over\sqrt b+\sqrt c},{1\over\sqrt c+\sqrt a},{1\over\sqrt a+\sqrt b}\right\\
:::

$$\left\{{1\over\sqrt b+\sqrt c},{1\over\sqrt c+\sqrt a},{1\over\sqrt a+\sqrt b}\right\}$$
::::

也是一个等差数列。

暴力展开，

:::: {.arithmatex}
::: {.MathJax_Preview}
{2\over\sqrt c+\sqrt a}={1\over\sqrt b+\sqrt c}+{1\over\sqrt a+\sqrt b}\\ {2\over\sqrt c+\sqrt a}={2\sqrt b+\sqrt a+\sqrt c\over b+\sqrt b(\sqrt a+\sqrt c)+\sqrt{ac}}\\ 2b+2\sqrt{ac}+2\sqrt b(\sqrt a+\sqrt c)=2\sqrt b(\sqrt a+\sqrt c)+a+c+\sqrt ac\\ a+c=2b
:::

$${2\over\sqrt c+\sqrt a}={1\over\sqrt b+\sqrt c}+{1\over\sqrt a+\sqrt b}\\
{2\over\sqrt c+\sqrt a}={2\sqrt b+\sqrt a+\sqrt c\over b+\sqrt b(\sqrt a+\sqrt c)+\sqrt{ac}}\\
2b+2\sqrt{ac}+2\sqrt b(\sqrt a+\sqrt c)=2\sqrt b(\sqrt a+\sqrt c)+a+c+\sqrt ac\\
a+c=2b$$
::::

对于等差数列 []{.arithmatex}$\{a,b,c\}$ 成立。Q.E.D.

或者，观察到原式中，分母都是根号的形式，考虑分母有理化，

:::: {.arithmatex}
::: {.MathJax_Preview}
{2\over\sqrt c+\sqrt a}={1\over\sqrt b+\sqrt c}+{1\over\sqrt a+\sqrt b}\\ {2(\sqrt c-\sqrt a)\over2d}={\sqrt c-\sqrt b\over d}+{\sqrt b-\sqrt a\over d}
:::

$${2\over\sqrt c+\sqrt a}={1\over\sqrt b+\sqrt c}+{1\over\sqrt a+\sqrt b}\\
{2(\sqrt c-\sqrt a)\over2d}={\sqrt c-\sqrt b\over d}+{\sqrt b-\sqrt a\over d}$$
::::

显然成立。

### 累加法 {#_19}

最简单的，形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=a\_{n-1}+f(n)
:::

$$a_n=a_{n-1}+f(n)$$
::::

都可以使用累加法，具体的，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} a_n&=a\_{n-1}+f(n)\\ a\_{n-1}&=a\_{n-2}+f(n-1)\\ &\dots\\ a_3&=a_2+f(3)\\ a_2&=a_1+f(2) \end{aligned}
:::

$$\begin{aligned}
a_n&=a_{n-1}+f(n)\\
a_{n-1}&=a_{n-2}+f(n-1)\\
&\dots\\
a_3&=a_2+f(3)\\
a_2&=a_1+f(2)
\end{aligned}$$
::::

上述所有式子相加，得

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=a_1+f(2)+f(2)+\dots+f(n)
:::

$$a_n=a_1+f(2)+f(2)+\dots+f(n)$$
::::

### 多阶等差 {#_20}

容易发现，我们对于公差求前缀和，可以得到一个普通等差数列。

那么，我们对于普通等差数列再求和，就可以得到二阶等差数列。

具体的，定义常数为零阶等差数列，普通等差数列为一阶等差数列。

容易发现，若 []{.arithmatex}$\{a_i\}$ 为一阶等差数列，[]{.arithmatex}$\{b_i\}$ 同样，那么 []{.arithmatex}$\{a_ib_i\}$ 为一个二阶等差数列。

根据定义，对于一个二阶等差数列，其相邻两项的差为一个一阶等差数列，相邻两项差的相邻两项差为一个常数。

## 等比数列 {#_21}

在等比数列中，任何相邻两项的比例相等，该比值称为公比 []{.arithmatex}$q$。

具体的，可以表示为，

:::: {.arithmatex}
::: {.MathJax_Preview}
a=pq\^n
:::

$$a=pq^n$$
::::

的，都是等比数列。

上式中，公比为 []{.arithmatex}$q$，首项 []{.arithmatex}$a_1=pq$。

### 递推公式 {#_22}

形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a\_{n+1}=qa_n,\\(n\in\mathbb Z\^\*,q\neq0)}
:::

$$\boxed{a_{n+1}=qa_n,\,(n\in\mathbb Z^*,q\neq0)}$$
::::

或者记为，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{q={a\_{n+1}\over a_n}}
:::

$$\boxed{q={a_{n+1}\over a_n}}$$
::::

即公比的定义式。

易知此式中，[]{.arithmatex}$a_n\neq0$，为了方便，我们一般规定 []{.arithmatex}$q\neq0$。

### 通项公式 {#_23}

形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a_n=a_1q\^{n-1}}
:::

$$\boxed{a_n=a_1q^{n-1}}$$
::::

换句话说，任意一个等比数列 []{.arithmatex}$\{a_n\}$ 都可以写为，

:::: {.arithmatex}
::: {.MathJax_Preview}
\\a,aq,aq\^2,\dots aq\^{n-1}\\
:::

$$\{a,aq,aq^2,\dots aq^{n-1}\}$$
::::

即，角标减一，等于公比幂次。

### 等比性质 {#_24}

除了上述几条，

在等比数列中，前项与后项积为该项平方，具体的，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} a\_{n-1}\times a\_{n+1}&=aq\^{n-2}aq\^{n}\\ &=a\^2q\^{2n-2}\\ &=(aq\^{n-1})\^2\\ &=a_n\^2 \end{aligned}
:::

$$\begin{aligned}
a_{n-1}\times a_{n+1}&=aq^{n-2}aq^{n}\\
&=a^2q^{2n-2}\\
&=(aq^{n-1})^2\\
&=a_n^2
\end{aligned}$$
::::

对于正整数 []{.arithmatex}$m,n,p,q$，若 []{.arithmatex}$m+n=p+q$，则，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a_m\cdot a_n=a_p\cdot a_q}
:::

$$\boxed{a_m\cdot a_n=a_p\cdot a_q}$$
::::

或者简化一下，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a_m\cdot a_n=a\_{m-k}\cdot a\_{n+k}}
:::

$$\boxed{a_m\cdot a_n=a_{m-k}\cdot a_{n+k}}$$
::::

据此，有，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a\_{n-k}\cdot a\_{n+k}=a_n\^2}
:::

$$\boxed{a_{n-k}\cdot a_{n+k}=a_n^2}$$
::::

还有一些和上面等比数列类似的操作的结论，

但是因为正负号的问题，不具体写出，可以根据上述平方的公式推导。

若 []{.arithmatex}$\langle a_n\rangle$ 为一个等比数列，则，

- []{.arithmatex}$\langle b+a_n\rangle$：为一个等比数列；
- []{.arithmatex}$\langle b\times a_n\rangle$：为一个等比数列；
- []{.arithmatex}$\langle \log_ba_n\rangle$：为一个等差数列（见上）；

### 求和公式 {#_25}

等差数列中给出的公式依然成立，

:::: {.arithmatex}
::: {.MathJax_Preview}
S_n-S\_{n-1}=a_n
:::

$$S_n-S_{n-1}=a_n$$
::::

实际上，这个对于任意数列都成立。

考虑求解出，等比数列求和公式的封闭形式，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} S_n&=a_1+a_1q+a_1q\^2+\dots+a_1q\^{n-1}\\ &=a_1(1+q+q\^2+\dots+q\^{n-1}) \end{aligned}
:::

$$\begin{aligned}
S_n&=a_1+a_1q+a_1q^2+\dots+a_1q^{n-1}\\
&=a_1(1+q+q^2+\dots+q^{n-1})
\end{aligned}$$
::::

注意到后面的是经典的分解因式，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{S_n=a_1\cdot{q\^n-1\over q-1},\\(q\neq 1)}
:::

$$\boxed{S_n=a_1\cdot{q^n-1\over q-1},\,(q\neq 1)}$$
::::

或者，错位相减，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} qS_n-S_n=a_1q\^n-a_1\\ S_n=a_1\cdot{q\^n-1\over q-1},\\(q\neq 1) \end{aligned}
:::

$$\begin{aligned}
qS_n-S_n=a_1q^n-a_1\\
S_n=a_1\cdot{q^n-1\over q-1},\,(q\neq 1)
\end{aligned}$$
::::

同时，若 []{.arithmatex}$q=1$，数列退化为常数列，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{S_n=na_1,\\(q=1)}
:::

$$\boxed{S_n=na_1,\,(q=1)}$$
::::

### 等比中项 {#_26}

对于 []{.arithmatex}$a,b$，有 []{.arithmatex}$c$ 满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
{b\over c}={c\over a}
:::

$${b\over c}={c\over a}$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
c=\pm\sqrt{ab}
:::

$$c=\pm\sqrt{ab}$$
::::

取其中的正数，即几何平均数。

### 累乘法 {#_27}

和累加法类似的，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=a\_{n-1}f(n)
:::

$$a_n=a_{n-1}f(n)$$
::::

累乘法，即

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} a_n&=a\_{n-1}f(n)\\ a\_{n-1}&=a\_{n-2}f(n-1)\\ &\dots\\ a_3&=a_2f(3)\\ a_2&=a_1f(2) \end{aligned}
:::

$$\begin{aligned}
a_n&=a_{n-1}f(n)\\
a_{n-1}&=a_{n-2}f(n-1)\\
&\dots\\
a_3&=a_2f(3)\\
a_2&=a_1f(2)
\end{aligned}$$
::::

上述所有式子相乘，得

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=a_1f(2)f(3)\dots f(n)
:::

$$a_n=a_1f(2)f(3)\dots f(n)$$
::::

## 裂项放缩 {#_28}

### 经典裂项 {#_29}

有性质，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{{1\over n(n+1)}={1\over n}-{1\over n+1}}
:::

$$\boxed{{1\over n(n+1)}={1\over n}-{1\over n+1}}$$
::::

可以求解，形如

:::: {.arithmatex}
::: {.MathJax_Preview}
S={1\over1\times2}+{1\over2\times3}+\dots+{1\over n(n+1)}
:::

$$S={1\over1\times2}+{1\over2\times3}+\dots+{1\over n(n+1)}$$
::::

的问题。

同时，易证，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{{1\over n(n+k)}={1\over k}\left({1\over k}-{1\over n+k}\right)}
:::

$$\boxed{{1\over n(n+k)}={1\over k}\left({1\over k}-{1\over n+k}\right)}$$
::::

注意，此时裂项一定要找准剩下的。

我们可以分别写出括号内的正数、负数。

以 []{.arithmatex}$k=2$ 为例，

:::: {.arithmatex}
::: {.MathJax_Preview}
S={1\over1\times3}+{1\over2\times4}+\dots+{1\over n(n+2)}
:::

$$S={1\over1\times3}+{1\over2\times4}+\dots+{1\over n(n+2)}$$
::::

化简，

:::: {.arithmatex}
::: {.MathJax_Preview}
2S={1\over1}-{1\over3}+{1\over2}-{1\over4}+\dots+{1\over n}-{1\over n+2}
:::

$$2S={1\over1}-{1\over3}+{1\over2}-{1\over4}+\dots+{1\over n}-{1\over n+2}$$
::::

列出正负，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} +&:{1\over1},{1\over2},{1\over3},\dots,{1\over n-1},{1\over n}\\ -&:{1\over3},{1\over4},{1\over5},\dots,{1\over n+1},{1\over n+2} \end{aligned}
:::

$$\begin{aligned}
+&:{1\over1},{1\over2},{1\over3},\dots,{1\over n-1},{1\over n}\\
-&:{1\over3},{1\over4},{1\over5},\dots,{1\over n+1},{1\over n+2}
\end{aligned}$$
::::

容易发现，

:::: {.arithmatex}
::: {.MathJax_Preview}
2S=1+{1\over2}-{1\over n+1}-{1\over n-2}
:::

$$2S=1+{1\over2}-{1\over n+1}-{1\over n-2}$$
::::

或者用求和符号简单的表示，下文再说。

### 整式裂项 {#_30}

有公式，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{n(n+1)={1\over3}\Big\[n(n+1)(n+2)-(n-1)n(n+1)\Big\]}
:::

$$\boxed{n(n+1)={1\over3}\Big[n(n+1)(n+2)-(n-1)n(n+1)\Big]}$$
::::

于是，例题，

:::: {.arithmatex}
::: {.MathJax_Preview}
S=1\times2+2\times3+3\times4+\dots+n(n+1)
:::

$$S=1\times2+2\times3+3\times4+\dots+n(n+1)$$
::::

化简，

:::: {.arithmatex}
::: {.MathJax_Preview}
3S=1\times2\times3-0\times1\times2+\dots+n(n+1)(n+2)-(n-1)n(n+1)
:::

$$3S=1\times2\times3-0\times1\times2+\dots+n(n+1)(n+2)-(n-1)n(n+1)$$
::::

得，

:::: {.arithmatex}
::: {.MathJax_Preview}
S={n(n+1)(n+2)\over3}
:::

$$S={n(n+1)(n+2)\over3}$$
::::

利用上述等式，注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
n\^2=n(n+1)-n
:::

$$n^2=n(n+1)-n$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{1\^2+2\^2+\dots+n\^2=S-{n(n+1)\over2}={n(n+1)(2n+1)\over6}}
:::

$$\boxed{1^2+2^2+\dots+n^2=S-{n(n+1)\over2}={n(n+1)(2n+1)\over6}}$$
::::

或者用求和符号简单的表示，下文再说。

### 更多裂项 {#_31}

以下是一些基本的小学奥数难度的裂项。

:::: {.arithmatex}
::: {.MathJax_Preview}
a\^2-a+1=\frac{a\^4+a\^2+1}{a\^4+a+1}
:::

$$a^2-a+1=\frac{a^4+a^2+1}{a^4+a+1}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1}
:::

$$\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{n(n+1)(n+2)}=\frac{1}{2}\left\[\frac{1}{n(n+1)}-\frac{1}{(n+1)(n+2)}\right\]
:::

$$\frac{1}{n(n+1)(n+2)}=\frac{1}{2}\left[\frac{1}{n(n+1)}-\frac{1}{(n+1)(n+2)}\right]$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{(2n-1)(2n+1)}=\frac{1}{2}\left(\frac{1}{2n-1}-\frac{1}{2n+1}\right)
:::

$$\frac{1}{(2n-1)(2n+1)}=\frac{1}{2}\left(\frac{1}{2n-1}-\frac{1}{2n+1}\right)$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{\sqrt{a}+\sqrt{b} }=\frac{1}{a-b}\left(\sqrt{a}-\sqrt{b}\right)
:::

$$\frac{1}{\sqrt{a}+\sqrt{b} }=\frac{1}{a-b}\left(\sqrt{a}-\sqrt{b}\right)$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{a_na\_{n+k} }=\frac{1}{dk}\left(\frac{1}{a_n}-\frac{1}{a\_{n+k} }\right)
:::

$$\frac{1}{a_na_{n+k} }=\frac{1}{dk}\left(\frac{1}{a_n}-\frac{1}{a_{n+k} }\right)$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{2\^n}{(2\^n+1)(2\^{n+1}+1)}=\frac{1}{2\^n+1}-\frac{1}{2\^{n+1}+1}
:::

$$\frac{2^n}{(2^n+1)(2^{n+1}+1)}=\frac{1}{2^n+1}-\frac{1}{2^{n+1}+1}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{q\^n}{(q\^{n+1}+1)(q\^n+1)}=\frac{1}{q-1}\left(\frac{1}{q\^n+1}-\frac{1}{q\^{n+1}+1}\right)
:::

$$\frac{q^n}{(q^{n+1}+1)(q^n+1)}=\frac{1}{q-1}\left(\frac{1}{q^n+1}-\frac{1}{q^{n+1}+1}\right)$$
::::

一个特点：前面保留几项，后面就保留几项。例如

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \sum\_{k=1}\^n \frac{1}{k(k+2)}&=\frac{1}{2}(1-\frac{1}{3}+\frac{1}{2}-\frac{1}{4}+\dots+\frac{n}{1}-\frac{1}{n+2})\\&=\frac{1}{2}(1+\frac{1}{2}-\frac{1}{n+1}-\frac{1}{n+2}) \end{aligned}
:::

$$\begin{aligned}
\sum_{k=1}^n \frac{1}{k(k+2)}&=\frac{1}{2}(1-\frac{1}{3}+\frac{1}{2}-\frac{1}{4}+\dots+\frac{n}{1}-\frac{1}{n+2})\\&=\frac{1}{2}(1+\frac{1}{2}-\frac{1}{n+1}-\frac{1}{n+2})
\end{aligned}$$
::::

现在我们要学习一些高难度的裂项。坐稳了，前方高能！

:::: {.arithmatex}
::: {.MathJax_Preview}
\sqrt{1+\frac{1}{k\^2}+\frac{1}{(k+1)\^2} }=1+\frac{1}{k}-\frac{1}{k+1}
:::

$$\sqrt{1+\frac{1}{k^2}+\frac{1}{(k+1)^2} }=1+\frac{1}{k}-\frac{1}{k+1}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{k}{(2k+1)\^2(2k-1)\^2}=\frac{1}{8}\left(\frac{1}{(2k-1)\^2}-\frac{1}{(2k+1)\^2}\right)
:::

$$\frac{k}{(2k+1)^2(2k-1)^2}=\frac{1}{8}\left(\frac{1}{(2k-1)^2}-\frac{1}{(2k+1)^2}\right)$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{k\sqrt{k+1}+(k+1)\sqrt{k} }=\frac{1}{\sqrt{k} }-\frac{1}{\sqrt{k+1} }
:::

$$\frac{1}{k\sqrt{k+1}+(k+1)\sqrt{k} }=\frac{1}{\sqrt{k} }-\frac{1}{\sqrt{k+1} }$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\sum\_{k=1}\^n k!(k\^2+k+1)=\sum\_{k=1}\^n \[(k+1)!(k+1)-k!k\]=(n+1)!(n+1)-1
:::

$$\sum_{k=1}^n k!(k^2+k+1)=\sum_{k=1}^n [(k+1)!(k+1)-k!k]=(n+1)!(n+1)-1$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\sum\_{k=1}\^n \frac{k\^2+k-1}{(k+2)!}=\sum\_{k=1}\^n \left(\frac{k}{(k+1)!}-\frac{k+1}{(k+2)!}\right)=\frac{1}{2}-\frac{n+1}{(n+2)!}
:::

$$\sum_{k=1}^n \frac{k^2+k-1}{(k+2)!}=\sum_{k=1}^n \left(\frac{k}{(k+1)!}-\frac{k+1}{(k+2)!}\right)=\frac{1}{2}-\frac{n+1}{(n+2)!}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{3k\^2-1}{(k\^3-k)\^2}=\frac{k-\frac{1}{2} }{k\^2(k-1)\^2}-\frac{k+\frac{1}{2} }{k\^2(k+1)\^2}
:::

$$\frac{3k^2-1}{(k^3-k)^2}=\frac{k-\frac{1}{2} }{k^2(k-1)^2}-\frac{k+\frac{1}{2} }{k^2(k+1)^2}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{4k}{4k\^4+1}=\frac{1}{2k\^2-2k+1}-\frac{1}{2k\^2+2k+1}
:::

$$\frac{4k}{4k^4+1}=\frac{1}{2k^2-2k+1}-\frac{1}{2k^2+2k+1}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{\sqrt{k+\sqrt{k\^2-1}}}=\frac{\sqrt{k+1}-\sqrt{k-1}}{\sqrt{2}}
:::

$$\frac{1}{\sqrt{k+\sqrt{k^2-1}}}=\frac{\sqrt{k+1}-\sqrt{k-1}}{\sqrt{2}}$$
::::

### 共轭根式 {#_32}

形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sqrt a+\sqrt b,\sqrt a-\sqrt b
:::

$$\sqrt a+\sqrt b,\sqrt a-\sqrt b$$
::::

的，称为共轭根式。

容易证明，

:::: {.arithmatex}
::: {.MathJax_Preview}
(\sqrt a-\sqrt b)\cdot(\sqrt a+\sqrt b)=a-b\\(a,b\ge0)
:::

$$(\sqrt a-\sqrt b)\cdot(\sqrt a+\sqrt b)=a-b\;(a,b\ge0)$$
::::

于是，有裂项，

:::: {.arithmatex}
::: {.MathJax_Preview}
{1\over\sqrt a+\sqrt b}={\sqrt a-\sqrt b\over a-b}
:::

$${1\over\sqrt a+\sqrt b}={\sqrt a-\sqrt b\over a-b}$$
::::

以及，

:::: {.arithmatex}
::: {.MathJax_Preview}
{1\over\sqrt a-\sqrt b}={\sqrt a+\sqrt b\over a-b}
:::

$${1\over\sqrt a-\sqrt b}={\sqrt a+\sqrt b\over a-b}$$
::::

### 阶乘问题 {#_33}

定义，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{n!=1\times2\times3\times\dots\times(n-1)\times n}
:::

$$\boxed{n!=1\times2\times3\times\dots\times(n-1)\times n}$$
::::

称为阶乘，有，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{n\cdot n!=(n+1)!-n!}
:::

$$\boxed{n\cdot n!=(n+1)!-n!}$$
::::

还有组合数的，但是这里还没涉及到。

### 放缩基础 {#_34}

数列求和是一种精确的方法，当我们无法精确的计算的时候，就可以放缩来估计。

例如，估计

:::: {.arithmatex}
::: {.MathJax_Preview}
S={1\over1\^2}+{1\over2\^2}+\dots+{1\over n\^2}
:::

$$S={1\over1^2}+{1\over2^2}+\dots+{1\over n^2}$$
::::

的级别。

容易发现，

:::: {.arithmatex}
::: {.MathJax_Preview}
{1\over n}-{1\over n-1}={1\over n(n+1)}\<{1\over n\^2}\<{1\over n(n-1)}={1\over n-1}-{1\over n}
:::

$${1\over n}-{1\over n-1}={1\over n(n+1)}<{1\over n^2}<{1\over n(n-1)}={1\over n-1}-{1\over n}$$
::::

于是，我们可以以此估计。

我们把 []{.arithmatex}$1/1^2$ 保持不动，估计

:::: {.arithmatex}
::: {.MathJax_Preview}
1.5\<S\<2
:::

$$1.5<S<2$$
::::

而为了提高精度，我们减少放缩的项数。

或者说，把 []{.arithmatex}$1/2^2,1/3^2$ 等直接计算，而不是放缩。

这就是放缩提高精度的方法：保留更多的项。

### 放缩进阶 {#_35}

:::: {.arithmatex}
::: {.MathJax_Preview}
{\sqrt k\over k\^2}={1\over k\^{3/2}}\<2\left({1\over\sqrt{k-1}}-{1\over\sqrt k}\right)
:::

$${\sqrt k\over k^2}={1\over k^{3/2}}<2\left({1\over\sqrt{k-1}}-{1\over\sqrt k}\right)$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
{2(\sqrt{n+1}-\sqrt{n})}=\frac{2}{\sqrt{n}+\sqrt{n+1}}\<\frac{2}{\sqrt{n}+\sqrt{n}}=\frac{1}{\sqrt{n}}
:::

$${2(\sqrt{n+1}-\sqrt{n})}=\frac{2}{\sqrt{n}+\sqrt{n+1}}<\frac{2}{\sqrt{n}+\sqrt{n}}=\frac{1}{\sqrt{n}}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
{\frac{1}{\sqrt{n}}=\frac{2}{\sqrt{n}+\sqrt{n}}}\<\frac{2}{\sqrt{n}+\sqrt{n-1}}={2(\sqrt{n}-\sqrt{n-1})}
:::

$${\frac{1}{\sqrt{n}}=\frac{2}{\sqrt{n}+\sqrt{n}}}<\frac{2}{\sqrt{n}+\sqrt{n-1}}={2(\sqrt{n}-\sqrt{n-1})}$$
::::

## 通用方法 {#_36}

### 速算方法 {#_37}

方法一：令 []{.arithmatex}$S_0=0$。

例题：等比数列 []{.arithmatex}$\set{a_n}$ 的 []{.arithmatex}$S_n=a\cdot 2^{n-1}+a-2$，求 []{.arithmatex}$a$。

直接代入 []{.arithmatex}$S_0=\frac{3}{2}a-2=0$ 得 []{.arithmatex}$\displaystyle a=\frac{4}{3}$。

方法二：令数列为常数数列。

例：等差数列 []{.arithmatex}$S_9=72$，求 []{.arithmatex}$a_2+a_4+a_9$ 的值。

令 []{.arithmatex}$a_i=8$，则答案为 []{.arithmatex}$24$。

### 等差等比 {#_38}

等差乘等比。

若 []{.arithmatex}$a_n=(An+B)q^{\red{n-1}}$，令 []{.arithmatex}$\red{\boxed{D=\frac{A}{q-1},E=\frac{B-D}{q-1}}}$，则 []{.arithmatex}$\red{\boxed{S_n=(Dn+E)q^n-E}}$.

例题：[]{.arithmatex}$\displaystyle a_n=\frac{n}{3^n}$，求 []{.arithmatex}$S_n$.

### 数学归纳 {#_39}

尝试证明，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=2\^n-1
:::

$$a_n=2^n-1$$
::::

容易发现，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=2\^1-1=1
:::

$$a_1=2^1-1=1$$
::::

假设对于 []{.arithmatex}$n=k,k\in\mathbb N^*$ 成立，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_k=2\^k-1
:::

$$a_k=2^k-1$$
::::

尝试证明对于 []{.arithmatex}$n=k+1$ 也成立，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{k+1}=2a_k+1=2\^{k+1}-2+1=2\^{k+1}-1
:::

$$a_{k+1}=2a_k+1=2^{k+1}-2+1=2^{k+1}-1$$
::::

于是，该通项公式对于任意 []{.arithmatex}$n\in\mathbb N^*$ 成立。

### 直接变形 {#_40}

容易发现，递推公式两边同时加一，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n+1=2a\_{n-1}+2
:::

$$a_n+1=2a_{n-1}+2$$
::::

另，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=a_n+1
:::

$$b_n=a_n+1$$
::::

上式即为，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=2b\_{n-1},b_1=2
:::

$$b_n=2b_{n-1},b_1=2$$
::::

那么这是一个等比数列，易得，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=2\^n
:::

$$b_n=2^n$$
::::

那么，根据关系，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=b_n-1=2\^n-1
:::

$$a_n=b_n-1=2^n-1$$
::::

Q.E.D.

**考虑推广这一类问题**，形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=pa\_{n-1}+q
:::

$$a_n=pa_{n-1}+q$$
::::

我们两边同时加一个数，设为 []{.arithmatex}$x$，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n+x=pa\_{n-1}+q+x
:::

$$a_n+x=pa_{n-1}+q+x$$
::::

记新数列，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=a_n+x,a_n=b_n-x
:::

$$b_n=a_n+x,a_n=b_n-x$$
::::

原数列，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=p(b\_{n-1}-x)+q+x=pb\_{n-1}+q-(p-1)x
:::

$$b_n=p(b_{n-1}-x)+q+x=pb_{n-1}+q-(p-1)x$$
::::

另右侧常数项为零，于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{x={q\over p-1}}
:::

$$\boxed{x={q\over p-1}}$$
::::

即，对于原数列，加上这个数，即可转化为普通的等比数列。

- 数列 []{.arithmatex}$\{a_n\}$ 的前 []{.arithmatex}$n$ 项和为 []{.arithmatex}$S_n$，若有如下项：[]{.arithmatex}$f(n)S_n$，[]{.arithmatex}$f(a_n)S_n$(即 []{.arithmatex}$S_n$ 的系数跟 []{.arithmatex}$n$ 有关)，则我们将递推式中的 []{.arithmatex}$a_n$ 改写为 []{.arithmatex}$S_n - S_{n-1}$。

- 若数列 []{.arithmatex}$\{a_n\}$ 的递推式形如 []{.arithmatex}$a_{n+1} = a_n + f(n)$，则可采用累加法求通项公式。

- 若数列 []{.arithmatex}$\{a_n\}$ 的递推式形如 []{.arithmatex}$a_{n+1} = a_n \cdot f(n)$，则可采用累乘法求通项公式。

- 形如 []{.arithmatex}$a_{n+1} = pa_n + q(p \ne 1, q \ne 0)$ 的递推式，两边同时加上 []{.arithmatex}$x$ 可构造成等比数列 []{.arithmatex}$\{a_n + x\}(n \in \mathbb{N}^*)$，通过比较可求得 []{.arithmatex}$x = \dfrac{q}{p-1}$。

- 形如 []{.arithmatex}$a_{n+1} = pa_n + kn + q(p \ne 1, k \ne 0, n \in \mathbb{N}^*)$ 的递推式，在两边同时加上 []{.arithmatex}$xn+y$ 构造等比数列 []{.arithmatex}$\{a_n + xn + y\}(n \in \mathbb{N}^*)$，方法见例 2.9 解析。

- 对于 []{.arithmatex}$a_{n+1} = p a_n^r (p > 0, p \ne 1, r \ne 1)$ 型，两边同时取以 []{.arithmatex}$p$ 为底的对数，于是可得 []{.arithmatex}$\log_p a_{n+1} = r \log_p a_n + 1$，构造等比数列 []{.arithmatex}$\{\log_p a_n + x\}$，其中 []{.arithmatex}$x = \dfrac{1}{r-1}$。

对于形如 []{.arithmatex}$a_{n+1} = pa_n + q^n(p \ne 0, 1 \text{ 且 } q \ne 0, 1)$ 的数列求通项公式，有以下两种方法：

- 两边同除以 []{.arithmatex}$p^{n+1}$，再累加求通项；

- 两边同加上 []{.arithmatex}$xq^{n+1}$，再构造成等比数列 []{.arithmatex}$\{a_n + xq^n\}$。

- 若 []{.arithmatex}$p=q$，则只能采用（1），而用（2）无法求解。

对于 []{.arithmatex}$a_{n+1} = \dfrac{a a_n}{b a_n + c}$，[]{.arithmatex}$abc \ne 0$，取倒数得 []{.arithmatex}$\dfrac{1}{a_{n+1}} = \dfrac{b a_n + c}{a a_n} = \dfrac{c}{a} \cdot \dfrac{1}{a_n} + \dfrac{b}{a}$。

- 当 []{.arithmatex}$a=c$ 时，[]{.arithmatex}$\dfrac{1}{a_{n+1}} = \dfrac{1}{a_n} + \dfrac{c}{a}$，则 []{.arithmatex}$\{\dfrac{1}{a_n}\}$ 为等差数列；

- 当 []{.arithmatex}$a \ne c$ 时，[]{.arithmatex}$\dfrac{1}{a_{n+1}} = \dfrac{c}{a} \cdot \dfrac{1}{a_n} + \dfrac{b}{a}$，则 []{.arithmatex}$\{\dfrac{1}{a_n} + x\}$ 为等比数列，[]{.arithmatex}$x = \dfrac{b}{c-a}$。

### 变形累加 {#_41}

容易得出，下面的式子不断乘二，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} a_n=2a\_{n-1}+1\\ 2a\_{n-1}=4a\_{n-1}+2\\ 4a\_{n=2}=8a\_{n-2}+4\\ \dots\\ 2\^{n-3}a_3=2\^{n-2}a_2+2\^{n-3}\\ 2\^{n-2}a_2=2\^{n-1}a_1+2\^{n-2} \end{aligned}
:::

$$\begin{aligned}
a_n=2a_{n-1}+1\\
2a_{n-1}=4a_{n-1}+2\\
4a_{n=2}=8a_{n-2}+4\\
\dots\\
2^{n-3}a_3=2^{n-2}a_2+2^{n-3}\\
2^{n-2}a_2=2^{n-1}a_1+2^{n-2}
\end{aligned}$$
::::

上述式子相加，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=2\^{n-1}a_1+2\^{n-2}+2\^{n-3}+\dots+4+2+1
:::

$$a_n=2^{n-1}a_1+2^{n-2}+2^{n-3}+\dots+4+2+1$$
::::

因为 []{.arithmatex}$a_1=1$，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=2\^n-1
:::

$$a_n=2^n-1$$
::::

Q.E.D.

**考虑推广这一类问题**，形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=pa\_{n-1}+q
:::

$$a_n=pa_{n-1}+q$$
::::

我们还可以等式两边同除 []{.arithmatex}$p^n$，得

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{{a_n\over p\^n}={a\_{n-1}\over p\^{n-1}}+{q\over p\^n}}
:::

$$\boxed{{a_n\over p^n}={a_{n-1}\over p^{n-1}}+{q\over p^n}}$$
::::

设新的数列，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n={a_n\over p\^n}
:::

$$b_n={a_n\over p^n}$$
::::

原数列形如，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=b\_{n-1}+{q\over p\^n}
:::

$$b_n=b_{n-1}+{q\over p^n}$$
::::

对 []{.arithmatex}$b$ 数列进行累加法，可以得出，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n={a_1\over p}+{q\over p\^2}+{q\over p\^3}+\dots+{q\over p\^n}
:::

$$b_n={a_1\over p}+{q\over p^2}+{q\over p^3}+\dots+{q\over p^n}$$
::::

右边为等比数列，即，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n={a_1\over p}+{q\over p\^n}\cdot{p\^n-1\over p-1}-{q\over p}
:::

$$b_n={a_1\over p}+{q\over p^n}\cdot{p^n-1\over p-1}-{q\over p}$$
::::

两边同时乘 []{.arithmatex}$p^n$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{a_n=(a_1-q)p\^{n-1}+{q\over p-1}(p\^n-1)}
:::

$$\boxed{a_n=(a_1-q)p^{n-1}+{q\over p-1}(p^n-1)}$$
::::

即通用公式。

同时，若 []{.arithmatex}$q=f(n)$，依然可以用这个方法来做。

### 数列判定 {#_42}

判断和证明数列是等差、等比数列的常见方法有如下几种：

- 定义法（用于证明）：对于 []{.arithmatex}$n \ge 2$ 的任意正整数，验证 []{.arithmatex}$a_n - a_{n-1}$ 或 []{.arithmatex}$\dfrac{a_n}{a_{n-1}}$ 为同一常数。

- 通项公式法（用于判断）：

  若 []{.arithmatex}$a_n = a_1 + (n-1)d = a_k + (n-k)d$，则 []{.arithmatex}$\{a_n\}$ 为等差数列；

  若 []{.arithmatex}$a_n = a_1q^{n-1} = a_kq^{n-k}$，则 []{.arithmatex}$\{a_n\}$ 为等比数列。

- 中项公式法（用于证明）：

  若 []{.arithmatex}$2a_n = a_{n-1} + a_{n+1}(n \ge 2, n \in \mathbb{N}^*)$，则 []{.arithmatex}$\{a_n\}$ 为等差数列；

  若 []{.arithmatex}$a_n^2 = a_{n-1}a_{n+1}(n \ge 2, n \in \mathbb{N}^*)$，则 []{.arithmatex}$\{a_n\}$ 为等比数列。

### 奇偶数列 {#_43}

奇偶项数列能求通项公式的要求是各下标的奇偶性一致。

绝对值数列：

- 对于首项小于 0 而公差大于 0 的等差数列 []{.arithmatex}$\{a_n\}$ 加绝对值后得到的数列 []{.arithmatex}$\{|a_n|\}$ 求和，设 []{.arithmatex}$\{a_n\}$ 的前 []{.arithmatex}$n$ 项和为 []{.arithmatex}$S_n$，[]{.arithmatex}$\{|a_n|\}$ 的前 []{.arithmatex}$n$ 项和为 []{.arithmatex}$T_n$，数列 []{.arithmatex}$\{a_n\}$ 的第 []{.arithmatex}$k$ 项小于 0 而从第 []{.arithmatex}$k+1$ 项开始大于或等于 0，于是有

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  T_n = \begin{cases} -S_n & n \le k \\ S_n - 2S_k & n \> k \end{cases}
  :::

  $$T_n = \begin{cases} -S_n & n \le k \\ S_n - 2S_k & n > k \end{cases}$$
  ::::

- 对于首项大于 0 而公差小于 0 的等差数列 []{.arithmatex}$\{a_n\}$ 加绝对值后得到的数列 []{.arithmatex}$\{|a_n|\}$ 求和，设 []{.arithmatex}$\{a_n\}$ 的前 []{.arithmatex}$n$ 项和为 []{.arithmatex}$S_n$，[]{.arithmatex}$\{|a_n|\}$ 的前 []{.arithmatex}$n$ 项和为 []{.arithmatex}$T_n$，数列 []{.arithmatex}$\{a_n\}$ 的第 []{.arithmatex}$k$ 项大于 0 而从第 []{.arithmatex}$k+1$ 项开始小于或等于 0，于是有

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  T_n = \begin{cases} S_n & n \le k \\ 2S_k - S_n & n \> k \end{cases}
  :::

  $$T_n = \begin{cases} S_n & n \le k \\ 2S_k - S_n & n > k \end{cases}$$
  ::::

### 单调性 {#_44}

对于 []{.arithmatex}$\forall n\in\mathbb  Z^*$，

- 若 []{.arithmatex}$a_{n+1}\ge a_n$，那么称 []{.arithmatex}$a$ 为**单调递增**数列。

- 若 []{.arithmatex}$a_{n+1}>a_n$，那么称 []{.arithmatex}$a$ 为**严格单调递增**数列。

- 若 []{.arithmatex}$a_{n+1}\le a_n$，那么称 []{.arithmatex}$a$ 为**单调递减**数列。

- 若 []{.arithmatex}$a_{n+1}<a_n$，那么称 []{.arithmatex}$a$ 为**严格单调递减**数列。

高中阶段一般认为单调即严格单调。

- 对于迭代数列 []{.arithmatex}$a_{n+1} = f(a_n)$，其中 []{.arithmatex}$f'(x) > 0$。若 []{.arithmatex}$a_1 < a_2$，则数列 []{.arithmatex}$\{a_n\}$ 单调递增；若 []{.arithmatex}$a_1 > a_2$，则数列 []{.arithmatex}$\{a_n\}$ 单调递减；若 []{.arithmatex}$a_1 = a_2$，则数列 []{.arithmatex}$\{a_n\}$ 是常数列。

- 对于迭代数列 []{.arithmatex}$a_{n+1} = f(a_n)$，若 []{.arithmatex}$f(x)$ 是二次函数，则数列单调递增的充分必要条件为 []{.arithmatex}$a_1 < a_2 < a_3$，且对于任意 []{.arithmatex}$n \ge 2, n \in \mathbb{N}^*$，在 []{.arithmatex}$[a_2, a_n]$ 上，[]{.arithmatex}$f'(x) \ge 0$。

- 迭代数列 []{.arithmatex}$a_{n+1} = f(a_n)$，其中 []{.arithmatex}$f'(x) < 0$，则 []{.arithmatex}$\{a_{2n}\}$ 与 []{.arithmatex}$\{a_{2n-1}\}$ 的单调性相反。

## 换元初步 {#_45}

### 三角换元 {#_46}

我们复习一下再换元里面常用的恒等变换，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\cos2\theta=2\cos\^2\theta-1}\tag1
:::

$$\boxed{\cos2\theta=2\cos^2\theta-1}\tag1$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\tan2\theta={2\tan\theta\over1-\tan\^2\theta}}\tag2
:::

$$\boxed{\tan2\theta={2\tan\theta\over1-\tan^2\theta}}\tag2$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\sin3\theta=3\sin\theta-4\sin\^2\theta}\tag3
:::

$$\boxed{\sin3\theta=3\sin\theta-4\sin^2\theta}\tag3$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\cos3\theta=4\cos\^2\theta-3\cos\theta}\tag4
:::

$$\boxed{\cos3\theta=4\cos^2\theta-3\cos\theta}\tag4$$
::::

注意到，除了正切函数，其他的函数值域都是 []{.arithmatex}$[-1,1]$（不指定定义域）。

因此，我们先需要证明函数值在一个区间内，然后利用上面的去换元。

### 一道例题 {#_47}

已知数列 []{.arithmatex}$\{a_n\}$ 满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1={1\over2},a\_{n+1}=a_n\^2-2
:::

$$a_1={1\over2},a_{n+1}=a_n^2-2$$
::::

- 求通项公式。

观察到右面类似余弦二倍角公式，考虑猜测 []{.arithmatex}$a_n\in[-2,2]$。

证明：考虑数学归纳，

:::: {.arithmatex}
::: {.MathJax_Preview}
-2\le a_1={1\over2}\le2
:::

$$-2\le a_1={1\over2}\le2$$
::::

尝试，[]{.arithmatex}$a_n\in[-2,2]\Rightarrow a_{n+1}\in[-2,2]$。

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n-1}=a_n\^2-2
:::

$$a_{n-1}=a_n^2-2$$
::::

由于，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n\in\[-2,2\]\Rightarrow a_n\^2\in\[0,4\]\Rightarrow a_n\^2-2\in\[-2,2\]
:::

$$a_n\in[-2,2]\Rightarrow a_n^2\in[0,4]\Rightarrow a_n^2-2\in[-2,2]$$
::::

因此，注意到递推式右面的 []{.arithmatex}$2$，我们设，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=2\cos\theta_n
:::

$$a_n=2\cos\theta_n$$
::::

容易发现，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}=a_n\^2-2\\ 2\cos\theta\_{n+1}=4\cos\^2\theta_n-2\\ \cos\theta\_{n+1}=2\cos\^2\theta_n-1\\ \cos\theta\_{n+1}=\cos2\theta_n
:::

$$a_{n+1}=a_n^2-2\\
2\cos\theta_{n+1}=4\cos^2\theta_n-2\\
\cos\theta_{n+1}=2\cos^2\theta_n-1\\
\cos\theta_{n+1}=\cos2\theta_n$$
::::

不妨令，

:::: {.arithmatex}
::: {.MathJax_Preview}
\theta\_{n+1}=2\theta_n
:::

$$\theta_{n+1}=2\theta_n$$
::::

于是，通项公式，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=2\cos(2\^{n-1}\theta)
:::

$$a_n=2\cos(2^{n-1}\theta)$$
::::

考虑 []{.arithmatex}$\theta$ 是多少，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=2\cos\theta={1\over2}\\ \cos\theta={1\over4}\\ \theta=\arccos1/4
:::

$$a_1=2\cos\theta={1\over2}\\
\cos\theta={1\over4}\\
\theta=\arccos1/4$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=2\cos\left(2\^{n-1}\arccos{1\over4}\right)
:::

$$a_n=2\cos\left(2^{n-1}\arccos{1\over4}\right)$$
::::

### 双曲换元 {#_48}

若，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=3, a\_{n+1}=2a_n\^2-1
:::

$$a_1=3,
a_{n+1}=2a_n^2-1$$
::::

- 求 []{.arithmatex}$a_n$ 通项。

我们考虑另外一个满足此式的式子，另，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n={k\^x+k\^{-x}\over2}=f(x)
:::

$$a_n={k^x+k^{-x}\over2}=f(x)$$
::::

其中 []{.arithmatex}$k$ 是任意变量，则，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{n+1}=2a_n\^2-1={k\^{2x}+k\^{-2x}\over2}=f(2x)
:::

$$a_{n+1}=2a_n^2-1={k^{2x}+k^{-2x}\over2}=f(2x)$$
::::

令，初项，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_1=f(t)={k\^t+k\^{-t}\over2}=3
:::

$$a_1=f(t)={k^t+k^{-t}\over2}=3$$
::::

令，

:::: {.arithmatex}
::: {.MathJax_Preview}
k\^t=3+2\sqrt2,k\^{-t}=3-2\sqrt2
:::

$$k^t=3+2\sqrt2,k^{-t}=3-2\sqrt2$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_2=f(2t)={k\^{2t}+k\^{-2t}\over2}\\ a_3=f(4t)={k\^{4t}+k\^{-4t}\over2}\\ \dots\\ a_n=f(2\^{n-1}t)={k\^{2\^{n-1}t}+k\^{-2\^{n-1}t}\over2}={(k\^t)\^{2\^{n-1}}+(k\^{-t})\^{2\^{n-1}}\over2}
:::

$$a_2=f(2t)={k^{2t}+k^{-2t}\over2}\\
a_3=f(4t)={k^{4t}+k^{-4t}\over2}\\
\dots\\
a_n=f(2^{n-1}t)={k^{2^{n-1}t}+k^{-2^{n-1}t}\over2}={(k^t)^{2^{n-1}}+(k^{-t})^{2^{n-1}}\over2}$$
::::

带入，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n={(3+2\sqrt2)\^{2\^{n-1}}+(3-2\sqrt2)\^{2\^{n-1}}\over2}
:::

$$a_n={(3+2\sqrt2)^{2^{n-1}}+(3-2\sqrt2)^{2^{n-1}}\over2}$$
::::

这个东西就是（类似）双曲换元。

## 基础例题 {#_49}

求下列数列的通项公式。

### 例题一 {#_50}

求：[]{.arithmatex}$a_n=2a_{n-1}+3\,(n\ge2),a_1=1$。

因为 []{.arithmatex}$q/(p-1)=3$，等式两边同时加三，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n+3=2a\_{n-1}+6=2\^{n+1}\\ a_n=2\^{n+1}-3
:::

$$a_n+3=2a_{n-1}+6=2^{n+1}\\
a_n=2^{n+1}-3$$
::::

注意到当 []{.arithmatex}$n=1,a_1=1$ 满足该式，因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=2\^{n+1}-3
:::

$$a_n=2^{n+1}-3$$
::::

### 例题二 {#_51}

求：[]{.arithmatex}$a_n=a_{n-1}+n\,(n\ge2),a_1=1$。

注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=a\_{n-1}+n\\ a\_{n-1}=a{n-2}+n-1\\ \dots\\ a_2=a_1+2=1+2
:::

$$a_n=a_{n-1}+n\\
a_{n-1}=a{n-2}+n-1\\
\dots\\
a_2=a_1+2=1+2$$
::::

上式相加，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=1+2+3+\dots+n-1+n={n(n+1)\over2}
:::

$$a_n=1+2+3+\dots+n-1+n={n(n+1)\over2}$$
::::

注意到当 []{.arithmatex}$n=1,a_1=1$ 满足该式，因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n={n(n+1)\over2}
:::

$$a_n={n(n+1)\over2}$$
::::

### 例题三 {#_52}

求：[]{.arithmatex}$a_n=2a_{n-1}+n\,(n\ge2),a_1=1$。

等式两边同时除以 []{.arithmatex}$2^n$，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
{a_n\over2\^n}={a\_{n-1}\over2\^{n-1}}+{n\over2\^n}
:::

$${a_n\over2^n}={a_{n-1}\over2^{n-1}}+{n\over2^n}$$
::::

记 []{.arithmatex}$b_n=a_n/2^n$，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=b\_{n-1}+n/2\^n\\ b\_{n-1}=b\_{n-2}+(n-1)/2\^{n-1}\\ \dots\\ b_2=b_1+1/2\\ b_1=1/2
:::

$$b_n=b_{n-1}+n/2^n\\
b_{n-1}=b_{n-2}+(n-1)/2^{n-1}\\
\dots\\
b_2=b_1+1/2\\
b_1=1/2$$
::::

上式相加，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n={n\over2\^n}+{n-1\over2\^{n-1}}+\dots+{1\over2}+{1\over2}
:::

$$b_n={n\over2^n}+{n-1\over2^{n-1}}+\dots+{1\over2}+{1\over2}$$
::::

注意到分母为二的幂次的形式，等式乘二，

:::: {.arithmatex}
::: {.MathJax_Preview}
2b_n={n\over2\^{n-1}}+{n-1\over2\^{n-2}}+\dots+1+1
:::

$$2b_n={n\over2^{n-1}}+{n-1\over2^{n-2}}+\dots+1+1$$
::::

下式减上式，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} b_n&=-{n\over2\^n}+{1\over2\^{n-1}}+{1\over2\^{n-2}}+\dots+{1\over2\^1}+1\\ &={1\over2\^{n-1}}\left(1+2+\dots+2\^{n-1}\right)-{n\over2\^n}\\ &={2\^n-1\over2\^{n-1}}-{n\over2\^n}=2-{2+n\over2\^n} \end{aligned}
:::

$$\begin{aligned}
b_n&=-{n\over2^n}+{1\over2^{n-1}}+{1\over2^{n-2}}+\dots+{1\over2^1}+1\\
&={1\over2^{n-1}}\left(1+2+\dots+2^{n-1}\right)-{n\over2^n}\\
&={2^n-1\over2^{n-1}}-{n\over2^n}=2-{2+n\over2^n}
\end{aligned}$$
::::

带入原式，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=2\^nb_n=2\^{n+1}-2-n
:::

$$a_n=2^nb_n=2^{n+1}-2-n$$
::::

注意到当 []{.arithmatex}$n=1,a_1=1$ 满足该式，因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=2\^{n+1}-2-n
:::

$$a_n=2^{n+1}-2-n$$
::::

### 例题四 {#_53}

求：[]{.arithmatex}$a_n=2a_{n-1}+n^2\,(n\ge2),a_1=1$。

等式两边同时除以 []{.arithmatex}$2^n$，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
{a_n\over2\^n}={a\_{n-1}\over2\^{n-1}}+{n\^2\over2\^n}
:::

$${a_n\over2^n}={a_{n-1}\over2^{n-1}}+{n^2\over2^n}$$
::::

记，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=a_n/2\^n,a_n=2\^nb_n
:::

$$b_n=a_n/2^n,a_n=2^nb_n$$
::::

则，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=b\_{n-1}+{n\^2\over2\^n},b_1={a_1\over2\^1}={1\over2}={1\^2\over2\^1}
:::

$$b_n=b_{n-1}+{n^2\over2^n},b_1={a_1\over2^1}={1\over2}={1^2\over2^1}$$
::::

得，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n={1\^2\over2\^1}+{2\^2\over2\^2}+{3\^2\over2\^3}+{4\^2\over2\^4}+\dots+{(n-1)\^2\over2\^{n-1}}+{n\^2\over2\^n}
:::

$$b_n={1^2\over2^1}+{2^2\over2^2}+{3^2\over2^3}+{4^2\over2^4}+\dots+{(n-1)^2\over2^{n-1}}+{n^2\over2^n}$$
::::

两边同时乘二，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
2b_n=1+{2\^2\over2\^1}+{3\^2\over2\^2}+{4\^2\over2\^3}+\dots+{(n-1)\^2\over2\^{n-2}}+{n\^2\over2\^{n-1}}
:::

$$2b_n=1+{2^2\over2^1}+{3^2\over2^2}+{4^2\over2^3}+\dots+{(n-1)^2\over2^{n-2}}+{n^2\over2^{n-1}}$$
::::

下式减上式，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=1-{n\^2\over2\^n}+{2\^2-1\^2\over2\^1}+{3\^2-2\^2\over2\^2}+{4\^2-3\^2\over2\^3}+\dots+{(n-1)\^2-(n-2)\^2\over2\^{n-2}}+{n\^2-(n-1)\^2\over2\^{n-1}}
:::

$$b_n=1-{n^2\over2^n}+{2^2-1^2\over2^1}+{3^2-2^2\over2^2}+{4^2-3^2\over2^3}+\dots+{(n-1)^2-(n-2)^2\over2^{n-2}}+{n^2-(n-1)^2\over2^{n-1}}$$
::::

注意到，

:::: {.arithmatex}
::: {.MathJax_Preview}
n\^2-(n-1)\^2=n\^2-n\^2-1+2n=2n-1
:::

$$n^2-(n-1)^2=n^2-n^2-1+2n=2n-1$$
::::

于是，记，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} c_n&={2\^2-1\^2\over2\^1}+{3\^2-2\^2\over2\^2}+{4\^2-3\^2\over2\^3}+\dots+{(n-1)\^2-(n-2)\^2\over2\^{n-2}}+{n\^2-(n-1)\^2\over2\^{n-1}}\\ &={2\times2-1\over2\^1}+{2\times3-1\over2\^2}+{2\times4-1\over2\^3}+\dots+{2(n-1)-1\over2\^{n-2}}+{2n-1\over2\^{n-1}} \end{aligned}
:::

$$\begin{aligned}
c_n&={2^2-1^2\over2^1}+{3^2-2^2\over2^2}+{4^2-3^2\over2^3}+\dots+{(n-1)^2-(n-2)^2\over2^{n-2}}+{n^2-(n-1)^2\over2^{n-1}}\\
&={2\times2-1\over2^1}+{2\times3-1\over2^2}+{2\times4-1\over2^3}+\dots+{2(n-1)-1\over2^{n-2}}+{2n-1\over2^{n-1}}
\end{aligned}$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=1-{n\^2\over2\^n}+c_n
:::

$$b_n=1-{n^2\over2^n}+c_n$$
::::

下式两边同时乘二，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
2c_n=3+{2\times3-1\over2\^1}+{2\times4-1\over2\^2}+\dots+{2(n-1)-1\over2\^{n-3}}+{2n-1\over2\^{n-2}}\\
:::

$$2c_n=3+{2\times3-1\over2^1}+{2\times4-1\over2^2}+\dots+{2(n-1)-1\over2^{n-3}}+{2n-1\over2^{n-2}}\\$$
::::

与原式相减，得，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} c_n&=3-{2n-1\over2\^{n-1}}+{2\over2\^1}+{2\over2\^2}+\dots+{2\over2\^{n-3}}+{2\over2\^{n-2}}\\ &=3-{2n-1\over2\^{n-1}}+{1\over2\^0}+{1\over2\^1}+\dots+{1\over2\^{n-4}}+{1\over2\^{n-3}}\\ &=3-{2n-1\over2\^{n-1}}+{1\over2\^{n-3}}(1+2+2\^2+\dots+2\^{n-3})\\ &=3-{2n-1\over2\^{n-1}}+{2\^{n-2}-1\over2\^{n-3}}\\ &=5-{2n-1\over2\^{n-1}}-{1\over2\^{n-3}} \end{aligned}
:::

$$\begin{aligned}
c_n&=3-{2n-1\over2^{n-1}}+{2\over2^1}+{2\over2^2}+\dots+{2\over2^{n-3}}+{2\over2^{n-2}}\\
&=3-{2n-1\over2^{n-1}}+{1\over2^0}+{1\over2^1}+\dots+{1\over2^{n-4}}+{1\over2^{n-3}}\\
&=3-{2n-1\over2^{n-1}}+{1\over2^{n-3}}(1+2+2^2+\dots+2^{n-3})\\
&=3-{2n-1\over2^{n-1}}+{2^{n-2}-1\over2^{n-3}}\\
&=5-{2n-1\over2^{n-1}}-{1\over2^{n-3}}
\end{aligned}$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
b_n=1-{n\^2\over2\^n}+c_n=6-{n\^2\over2\^n}-{2n-1\over2\^{n-1}}-{1\over2\^{n-3}}
:::

$$b_n=1-{n^2\over2^n}+c_n=6-{n^2\over2^n}-{2n-1\over2^{n-1}}-{1\over2^{n-3}}$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=2\^nb_n=3\times2\^{n+1}-n\^2-4n-6
:::

$$a_n=2^nb_n=3\times2^{n+1}-n^2-4n-6$$
::::

注意到当 []{.arithmatex}$n=1,a_1=1$ 满足该式，因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=3\times2\^{n+1}-n\^2-4n-6
:::

$$a_n=3\times2^{n+1}-n^2-4n-6$$
::::
