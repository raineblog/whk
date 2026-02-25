# 不等式进阶 {#_1}

## （二）柯西-施瓦茨不等式 {#-}

### 简化形式 {#_2}

对于实数 $a_1,a_2,b_1,b_2$：

$$
(a_1^2+a_2^2)(b_1^2+b_2^2)\ge(a_1b_1+a_2b_2)^2
$$

证明：

$$
\begin{aligned} &a_1^2b_2^2+a_2^2b_1^2\ge 2a_1b_1a_2b_2\\ \Leftrightarrow\;&a_1^2b_1^2+a_2^2b_2^2+a_1^2b_2^2+a_2^2b_1^2\ge a_1^2b_1^2+a_2^2b_2^2+2a_1b_1a_2b_2\\ \Leftrightarrow\;&(a_1^2+a_2^2)(b_1^2+b_2^2)\ge(a_1b_1+a_2b_2)^2 \end{aligned}
$$

取等条件：

$$
{a_1\over b_1}={a_2\over b_2}
$$

### 一般形式 {#_3}

对于实数序列 $a,b$：

$$
\sum_{i=1}^na_i^2\sum_{i=1}^nb_i^2\ge\left(\sum_{i=1}^na_ib_i\right)^2
$$

证明：

$$
\begin{aligned} &\sum_{i=1}^na_i^2\sum_{i=1}^nb_i^2-\left(\sum_{i=1}^na_ib_i\right)^2\\ =\;&\sum_{1\le i<j\le n}(a_ib_j-a_jb_i)^2 \end{aligned}
$$

上式即拉格朗日恒等式，可知其 $\ge0$ 且取等条件为：

$$
{a_1\over b_1}={a_2\over b_2}=\dots={a_n\over b_n}
$$

### 物理证明 {#_4}

转自：<https://www.zhihu.com/question/359244589/answer/3440897794>。

光滑桌子（$\mu=0$）上面放着若干个质量不一的薄板，其中间的摩擦因数不为零（$\mu\neq0$）。

设其质量分别为 $m_1,m_2,\dots,m_n$，给他们一个互异的初速度 $v_1,v_2,\dots,v_n$。

根据能量守恒定律，经过有限的时间后，它们必定会趋于同一个速度，设为 $v_f$。

那么，根据动量守恒定律和功能关系：

$$
\begin{aligned} m_1v_1+m_2v_2+\dots+m_nv_n&=m_1v_f+m_2v_f+\dots+m_nv_f\\ {1\over2}m_1v_1^2+{1\over2}m_2v_2^2+\dots+{1\over2}m_nv_n^2&\ge {1\over2}m_1v_f^2+{1\over2}m_2v_f^2+\dots+{1\over2}m_nv_f^2 \end{aligned}
$$

化简、移项，得到：

$$
\begin{aligned} v_f={\sum m_iv_i\over\sum m_i}\\ \sum(m_iv_i^2)\ge(\sum m_i)v_f^2 \end{aligned}
$$

上式带入下式，得：

$$
\sum(m_iv_i^2)\ge{(\sum m_iv_i)^2\over\sum m_i}
$$

再移项，得：

$$
\sum(m_iv_i^2)\sum m_i\ge(\sum m_iv_i)^2
$$

我们取 $m\to a^2$，$v\to b/a$，即：

$$
\sum{a_i^2}\sum{b_i^2}\ge(\sum{a_ib_i})^2
$$

取等条件为 $v_i=v_g$，即初始就共速，则：

$$
{b_1\over a_1}={b_2\over a_2}=\dots={b_n\over a_n}
$$

即柯西不等式（当然这个结论比柯西不等式弱一些）。

------------------------------------------------------------------------

柯西-施瓦茨不等式​：对于正实数 $a,b,x,y$，有

$$
(a^2+b^2)(c^2+d^2)\ge(ac+bd)^2
$$

当且仅当 $ad=bc$ 时，等号成立。

示例：已知实数 $x,y$ 满足 $x^2+y^2=3$，求 $5x+2y$ 的最大值。根据柯西不等式：

$$
(5x+2y)^2=(ac+bd)^2\le (a^2+b^2)(c^2+d^2)=(5^2+2^2)(x^2+y^2)=87
$$

即：

$$
(5x+2y)^2\le 87\Rightarrow 5x+2y\le\sqrt{87}
$$

所以 $5x+2y$ 的最大值为 $\sqrt{87}$。

权方和不等式​：

$$
\frac{a^2}{x}+\frac{b^2}{y}\ge\frac{(a+b)^2}{x+y}
$$

示例：已知实数 $x,y>0$ 满足 $\frac{1}{x}+\frac{4}{y}=1$，求 $x+y$ 的最小值。根据权方和不等式：

$$
1=\frac{1^2}{x}+\frac{2^2}{y}=\frac{a^2}{x}+\frac{b^2}{y}\ge\frac{(a+b)^2}{x+y}=\frac{(1+2)^2}{x+y}=\frac{9}{x+y}
$$

即：

$$
1\ge\frac{9}{x+y}\Rightarrow x+y\ge 9
$$

所以 $x+y$ 的最小值为 $9$。

## （三）排序不等式 {#_5}

### 基本形式 {#_6}

对于非严格单调递增（或递减）的实数序列 $x,y$，另 $\sigma(i)$ 表示 $1\sim n$ 的任意一个排列，有，

$$
x_1y_1+\dots+x_ny_n\ge x_{\sigma(1)}y_1+\dots+x_{\sigma(n)}y_n\ge x_ny_1+\dots+x_1y_n
$$

顺序和不小于乱序和，乱序和不小于逆序和；取等为 $x,y$ 分别两两相等。

排序不等式不限正负，证明可以归纳法。

## 其他不等式 {#_7}

### 伯努利不等式 {#_8}

若 $x_1,x_2\dots,x_n\ge-1$ 且 $x_2,x_2,\dots,x_n$ 同号，则

$$
(1+x_1)(1+x_2)\dots(1+x_n)\ge1+x_1+x_2+\dots+x_n
$$

### 权方和不等式 {#_9}

设 $a_1,a_2,\cdots,a_n>0，b_1,b_2,\cdots,b_n>0，r\in\mathbb{R}$，则

- 当 $r\ge0$，或 $r\le-1$ 时，有

  $$
  \frac{a_1^{r+1}}{b_1^{r}}+\frac{a_2^{r+1}}{b_2^{r}}+\cdots+\frac{a_n^{r+1}}{b_n^{r}}\ge\frac{(a_1+a_2+\cdots+a_n)^{r+1}}{(b_1+b_2+\cdots+b_n)^{r}}。
  $$

- 当 $-1<r<0$ 时，有

  $$
  \frac{a_1^{r+1}}{b_1^{r}}+\frac{a_2^{r+1}}{b_2^{r}}+\cdots+\frac{a_n^{r+1}}{b_n^{r}}\le\frac{(a_1+a_2+\cdots+a_n)^{r+1}}{(b_1+b_2+\cdots+b_n)^{r}}。
  $$

### 杨格不等式 {#_10}

若 $a,b>0，p>1，\dfrac{1}{p}+\dfrac{1}{q}=1$，则有

$$
ab\le\dfrac{1}{p}a^{p}+\dfrac{1}{q}b^{q}。
$$
