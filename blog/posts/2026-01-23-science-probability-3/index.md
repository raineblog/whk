# 随机变量综述：概念到实践的全景指南 {#_1}

了解随机变量的定义、分布特性、统计数值以及在信息熵、频率直方图和百分位数等实际场景中的应用，帮助读者快速捕捉要点，并引导进一步阅读完整教程。

## 随机变量的概念 {#_2}

### 随机变量 {#_3}

随机变量是描述随机试验结果的函数，常用大写字母 []{.arithmatex}$X、Y、Z$ 或希腊字母 []{.arithmatex}$\xi、\eta、\zeta$ 表示。它把样本空间 []{.arithmatex}$\Omega$ 中的每个基本事件映射为实数值，从而将不确定的实验转化为可量化的数值。

### 分布函数 {#_4}

分布函数 []{.arithmatex}$F(x)$ 给出随机变量 []{.arithmatex}$X$ 小于等于某实数 []{.arithmatex}$x$ 的概率：

:::: {.arithmatex}
::: {.MathJax_Preview}
F(x) = P( X \le x )
:::

$$F(x) = P( X \le x )$$
::::

它满足右连续、单调递增并在 []{.arithmatex}$-\infty$ 与 []{.arithmatex}$+\infty$ 处分别取 []{.arithmatex}$0$ 与 []{.arithmatex}$1$。

### 示性函数 {#_5}

示性函数 []{.arithmatex}$I_A$ 用于指示事件 []{.arithmatex}$A$ 是否发生：

:::: {.arithmatex}
::: {.MathJax_Preview}
I_A(\omega) = \begin{cases} 1, & \omega \in A \\ 0, & \omega \notin A \end{cases}
:::

$$I_A(\omega) = \begin{cases}
    1, & \omega \in A \\
    0, & \omega \notin A
\end{cases}$$
::::

其期望恰好等于事件 []{.arithmatex}$A$ 的概率，即 []{.arithmatex}$E[I_A] = P(A)$。

### 离散型随机变量 {#_6}

离散型随机变量的取值集合是有限或可数无限的。例如掷骰子的点数 []{.arithmatex}$\{1,2,3,4,5,6\}$。其概率分布可用概率分布列描述：

- []{.arithmatex}$P\{ X = x_i \} = p_i$，且 []{.arithmatex}$\sum_i p_i = 1$。

### 连续型随机变量 {#_7}

连续型随机变量的取值覆盖整个区间（或更广）。单点概率通常为 []{.arithmatex}$0$，而应使用密度函数 []{.arithmatex}$f(x)$ 来刻画分布：

:::: {.arithmatex}
::: {.MathJax_Preview}
F(x) = \int\_{-\infty}\^{x} f(t) \\ dt , \qquad f(x) \ge 0 , \qquad \int\_{-\infty}\^{\infty} f(x) \\ dx = 1
:::

$$F(x) = \int_{-\infty}^{x} f(t) \, dt , \qquad f(x) \ge 0 , \qquad \int_{-\infty}^{\infty} f(x) \, dx = 1$$
::::

### 随机变量的独立性 {#_8}

若对任意实数 []{.arithmatex}$x$ 与 []{.arithmatex}$y$ 都满足

:::: {.arithmatex}
::: {.MathJax_Preview}
P( X \le x , Y \le y ) = P( X \le x ) \\ P( Y \le y )
:::

$$P( X \le x , Y \le y ) = P( X \le x ) \, P( Y \le y )$$
::::

则称 []{.arithmatex}$X$ 与 []{.arithmatex}$Y$ 相互独立。独立性意味着它们的边缘分布互不影响。

## 随机变量的数字特征 {#_9}

### 期望 {#_10}

期望是随机变量的平均值。离散情形：

:::: {.arithmatex}
::: {.MathJax_Preview}
E\[X\] = \sum_i x_i \\ p_i
:::

$$E[X] = \sum_i x_i \, p_i$$
::::

连续情形：

:::: {.arithmatex}
::: {.MathJax_Preview}
E\[X\] = \int\_{-\infty}\^{\infty} x \\ f(x) \\ dx
:::

$$E[X] = \int_{-\infty}^{\infty} x \, f(x) \, dx$$
::::

它具备线性特性 []{.arithmatex}$E[aX + bY + c] = aE[X] + bE[Y] + c$。

### 方差 {#_11}

方差衡量离散程度：

:::: {.arithmatex}
::: {.MathJax_Preview}
\operatorname{Var}(X) = E\\\left\[(X - E\[X\])\^{2}\right\] = E\[X\^{2}\] - (E\[X\])\^{2}
:::

$$\operatorname{Var}(X) = E\!\left[(X - E[X])^{2}\right] = E[X^{2}] - (E[X])^{2}$$
::::

若对变量作线性变换 []{.arithmatex}$aX + b$，则 []{.arithmatex}$\operatorname{Var}(aX + b) = a^{2}\operatorname{Var}(X)$。

### 协方差 {#_12}

协方差描述两个变量的线性相关程度：

:::: {.arithmatex}
::: {.MathJax_Preview}
\operatorname{Cov}(X, Y) = E\\\big\[(X - E\[X\]) (Y - E\[Y\])\big\]
:::

$$\operatorname{Cov}(X, Y) = E\!\big[(X - E[X]) (Y - E[Y])\big]$$
::::

它满足 []{.arithmatex}$\operatorname{Cov}(X, X) = \operatorname{Var}(X)$，以及 []{.arithmatex}$\operatorname{Cov}(aX + bY, Z) = a\,\operatorname{Cov}(X, Z) + b\,\operatorname{Cov}(Y, Z)$。

### 相关系数 {#_13}

相关系数 []{.arithmatex}$\rho_{X,Y}$ 将协方差标准化：

:::: {.arithmatex}
::: {.MathJax_Preview}
\rho\_{X,Y} = \frac{\operatorname{Cov}(X, Y)}{\sigma_X \\ \sigma_Y}
:::

$$\rho_{X,Y} = \frac{\operatorname{Cov}(X, Y)}{\sigma_X \, \sigma_Y}$$
::::

其中 []{.arithmatex}$\sigma_X = \sqrt{\operatorname{Var}(X)}$。其取值范围为 []{.arithmatex}$-1 \le \rho_{X,Y} \le 1$；若 []{.arithmatex}$| \rho_{X,Y} | = 1$，则 []{.arithmatex}$X$ 与 []{.arithmatex}$Y$ 线性相关。

### Markov 不等式 {#markov}

对非负随机变量 []{.arithmatex}$X$，任意正数 []{.arithmatex}$a$ 满足

:::: {.arithmatex}
::: {.MathJax_Preview}
P( X \ge a ) \le \frac{E\[X\]}{a}
:::

$$P( X \ge a ) \le \frac{E[X]}{a}$$
::::

该不等式仅依赖期望即可给出上界。

## 随机变量的应用 {#_14}

### 信息熵 {#_15}

信息熵衡量随机变量的不确定性：

:::: {.arithmatex}
::: {.MathJax_Preview}
H(X) = -\sum\_{x} P(X = x) \\ \log\_{2} P(X = x)
:::

$$H(X) = -\sum_{x} P(X = x) \, \log_{2} P(X = x)$$
::::

若 []{.arithmatex}$X$ 均匀分布于 []{.arithmatex}$\{1,2,\dots ,n\}$，则 []{.arithmatex}$H(X) = \log_{2} n$，说明存储 []{.arithmatex}$n$ 个等概率符号至少需要 []{.arithmatex}$\log_{2} n$ 比特。

### 频率分布直方图 {#_16}

直方图以矩形面积表示频率，横轴为取值区间，纵轴为相对频率（频数除以总数）。等距分组常用于展示连续型数据的分布形态。

### 百分位数和四分位数 {#_17}

将有序数据 []{.arithmatex}$x_{1}\le x_{2}\le \dots \le x_{n}$ 按累计比例划分，可得到第 []{.arithmatex}$k$ 百分位数 []{.arithmatex}$P_{k}$。常见四分位数包括：

- []{.arithmatex}$Q_{1}=P_{25}$（上四分位数）
- []{.arithmatex}$Q_{2}=P_{50}$（中位数）
- []{.arithmatex}$Q_{3}=P_{75}$（下四分位数）

四分位距 []{.arithmatex}$Q_{3} - Q_{1}$ 描述数据的离散程度。

------------------------------------------------------------------------

想进一步掌握随机变量的理论细节与实际例题，请访问原文 **随机变量专题**（<https://raineblog.dpdns.org/whk/science/probability/3/>），深入阅读完整章节内容。
