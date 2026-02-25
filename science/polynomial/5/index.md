# 不等式进阶 \{#\_1}

## （二）柯西-施瓦茨不等式 \{#-}

### 简化形式 \{#\_2}

对于实数 $a\_1,a\_2,b\_1,b\_2$：

$$
(a\_1^2+a\_2^2)(b\_1^2+b\_2^2)\ge(a\_1b\_1+a\_2b\_2)^2
$$

证明：

$$
\begin\{aligned} \&a\_1^2b\_2^2+a\_2^2b\_1^2\ge 2a\_1b\_1a\_2b\_2\ \Leftrightarrow;\&a\_1^2b\_1^2+a\_2^2b\_2^2+a\_1^2b\_2^2+a\_2^2b\_1^2\ge a\_1^2b\_1^2+a\_2^2b\_2^2+2a\_1b\_1a\_2b\_2\ \Leftrightarrow;&(a\_1^2+a\_2^2)(b\_1^2+b\_2^2)\ge(a\_1b\_1+a\_2b\_2)^2 \end\{aligned}
$$

取等条件：

$$
\{a\_1\over b\_1}=\{a\_2\over b\_2}
$$

### 一般形式 \{#\_3}

对于实数序列 $a,b$：

$$
\sum\_\{i=1}^na\_i^2\sum\_\{i=1}^nb\_i^2\ge\left(\sum\_\{i=1}^na\_ib\_i\right)^2
$$

证明：

$$
\begin\{aligned} &\sum\_\{i=1}^na\_i^2\sum\_\{i=1}^nb\_i^2-\left(\sum\_\{i=1}^na\_ib\_i\right)^2\ =;&\sum\_\{1\le i\<j\le n}(a\_ib\_j-a\_jb\_i)^2 \end\{aligned}
$$

上式即拉格朗日恒等式，可知其 $\ge0$ 且取等条件为：

$$
\{a\_1\over b\_1}=\{a\_2\over b\_2}=\dots=\{a\_n\over b\_n}
$$

### 物理证明 \{#\_4}

转自：[https://www.zhihu.com/question/359244589/answer/3440897794](https://www.zhihu.com/question/359244589/answer/3440897794)。

光滑桌子（$\mu=0$）上面放着若干个质量不一的薄板，其中间的摩擦因数不为零（$\mu\neq0$）。

设其质量分别为 $m\_1,m\_2,\dots,m\_n$，给他们一个互异的初速度 $v\_1,v\_2,\dots,v\_n$。

根据能量守恒定律，经过有限的时间后，它们必定会趋于同一个速度，设为 $v\_f$。

那么，根据动量守恒定律和功能关系：

$$
\begin\{aligned} m\_1v\_1+m\_2v\_2+\dots+m\_nv\_n&=m\_1v\_f+m\_2v\_f+\dots+m\_nv\_f\ \{1\over2}m\_1v\_1^2+\{1\over2}m\_2v\_2^2+\dots+\{1\over2}m\_nv\_n^2&\ge \{1\over2}m\_1v\_f^2+\{1\over2}m\_2v\_f^2+\dots+\{1\over2}m\_nv\_f^2 \end\{aligned}
$$

化简、移项，得到：

$$
\begin\{aligned} v\_f=\{\sum m\_iv\_i\over\sum m\_i}\ \sum(m\_iv\_i^2)\ge(\sum m\_i)v\_f^2 \end\{aligned}
$$

上式带入下式，得：

$$
\sum(m\_iv\_i^2)\ge\{(\sum m\_iv\_i)^2\over\sum m\_i}
$$

再移项，得：

$$
\sum(m\_iv\_i^2)\sum m\_i\ge(\sum m\_iv\_i)^2
$$

我们取 $m\to a^2$，$v\to b/a$，即：

$$
\sum\{a\_i^2}\sum\{b\_i^2}\ge(\sum\{a\_ib\_i})^2
$$

取等条件为 $v\_i=v\_g$，即初始就共速，则：

$$
\{b\_1\over a\_1}=\{b\_2\over a\_2}=\dots=\{b\_n\over a\_n}
$$

即柯西不等式（当然这个结论比柯西不等式弱一些）。

***

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
(5x+2y)^2\le 87\Rightarrow 5x+2y\le\sqrt\{87}
$$

所以 $5x+2y$ 的最大值为 $\sqrt\{87}$。

权方和不等式​：

$$
\frac\{a^2}\{x}+\frac\{b^2}\{y}\ge\frac\{(a+b)^2}\{x+y}
$$

示例：已知实数 $x,y>0$ 满足 $\frac\{1}\{x}+\frac\{4}\{y}=1$，求 $x+y$ 的最小值。根据权方和不等式：

$$
1=\frac\{1^2}\{x}+\frac\{2^2}\{y}=\frac\{a^2}\{x}+\frac\{b^2}\{y}\ge\frac\{(a+b)^2}\{x+y}=\frac\{(1+2)^2}\{x+y}=\frac\{9}\{x+y}
$$

即：

$$
1\ge\frac\{9}\{x+y}\Rightarrow x+y\ge 9
$$

所以 $x+y$ 的最小值为 $9$。

## （三）排序不等式 \{#\_5}

### 基本形式 \{#\_6}

对于非严格单调递增（或递减）的实数序列 $x,y$，另 $\sigma(i)$ 表示 $1\sim n$ 的任意一个排列，有，

$$
x\_1y\_1+\dots+x\_ny\_n\ge x\_\{\sigma(1)}y\_1+\dots+x\_\{\sigma(n)}y\_n\ge x\_ny\_1+\dots+x\_1y\_n
$$

顺序和不小于乱序和，乱序和不小于逆序和；取等为 $x,y$ 分别两两相等。

排序不等式不限正负，证明可以归纳法。

## 其他不等式 \{#\_7}

### 伯努利不等式 \{#\_8}

若 $x\_1,x\_2\dots,x\_n\ge-1$ 且 $x\_2,x\_2,\dots,x\_n$ 同号，则

$$
(1+x\_1)(1+x\_2)\dots(1+x\_n)\ge1+x\_1+x\_2+\dots+x\_n
$$

### 权方和不等式 \{#\_9}

设 $a\_1,a\_2,\cdots,a\_n>0，b\_1,b\_2,\cdots,b\_n>0，r\in\mathbb\{R}$，则

- 当 $r\ge0$，或 $r\le-1$ 时，有

  $$
  \frac\{a\_1^\{r+1}}\{b\_1^\{r}}+\frac\{a\_2^\{r+1}}\{b\_2^\{r}}+\cdots+\frac\{a\_n^\{r+1}}\{b\_n^\{r}}\ge\frac\{(a\_1+a\_2+\cdots+a\_n)^\{r+1}}\{(b\_1+b\_2+\cdots+b\_n)^\{r}}。
  $$

- 当 $-1\<r\<0$ 时，有

  $$
  \frac\{a\_1^\{r+1}}\{b\_1^\{r}}+\frac\{a\_2^\{r+1}}\{b\_2^\{r}}+\cdots+\frac\{a\_n^\{r+1}}\{b\_n^\{r}}\le\frac\{(a\_1+a\_2+\cdots+a\_n)^\{r+1}}\{(b\_1+b\_2+\cdots+b\_n)^\{r}}。
  $$

### 杨格不等式 \{#\_10}

若 $a,b>0，p>1，\dfrac\{1}\{p}+\dfrac\{1}\{q}=1$，则有

$$
ab\le\dfrac\{1}\{p}a^\{p}+\dfrac\{1}\{q}b^\{q}。
$$
