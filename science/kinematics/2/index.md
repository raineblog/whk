# 直线运动 {#_1}

## 相关定义 {#_2}

### 位移 {#_3}

如果质点做直线运动，我们可以取运动直线为坐标轴，设正方向为 []{.arithmatex}$x$ 方向。

质点位置：

:::: {.arithmatex}
::: {.MathJax_Preview}
x=x(t)
:::

$$x=x(t)$$
::::

质点的位移：

:::: {.arithmatex}
::: {.MathJax_Preview}
\Delta x=x(t+\Delta t)-x(t)
:::

$$\Delta x=x(t+\Delta t)-x(t)$$
::::

### 速度 {#_4}

质点的平均速度定义为：

:::: {.arithmatex}
::: {.MathJax_Preview}
\bar v=\dfrac{\Delta v}{\Delta t}
:::

$$\bar v=\dfrac{\Delta v}{\Delta t}$$
::::

平均速度是反映质点运动快慢与运动方向的物理量，而且是较为粗糙的反映 []{.arithmatex}$\Delta t$ 时间段内运动的平均快慢和方向。如果要精确的描述质点在各时刻运动的快慢和方向，需取 []{.arithmatex}$\Delta t\to0$ 的极限：

:::: {.arithmatex}
::: {.MathJax_Preview}
v=\lim\_{\Delta t\to0}\dfrac{\Delta v}{\Delta t}
:::

$$v=\lim_{\Delta t\to0}\dfrac{\Delta v}{\Delta t}$$
::::

做直线运动的质点的位置随时间变化的关系，可以在 []{.arithmatex}$x-t$ 坐标中用一条曲线（称为位置图线）来表示。速度等于过曲线上一点切线的斜率，它是位置对时间的瞬时变化率。

于是，平均速度：

:::: {.arithmatex}
::: {.MathJax_Preview}
\bar v=\dfrac{x(t+\Delta t)-x(t)}{\Delta t}=\tan\alpha
:::

$$\bar v=\dfrac{x(t+\Delta t)-x(t)}{\Delta t}=\tan\alpha$$
::::

其中 []{.arithmatex}$\tan\alpha$ 表示割线斜率，当 []{.arithmatex}$\Delta t\to0$，割线变成了切线。

### 加速度 {#_5}

同样，可以定义平均加速度：

:::: {.arithmatex}
::: {.MathJax_Preview}
\bar a=\dfrac{\Delta v}{\Delta t}
:::

$$\bar a=\dfrac{\Delta v}{\Delta t}$$
::::

以及，瞬时加速度：

:::: {.arithmatex}
::: {.MathJax_Preview}
a=\lim\_{\Delta t\to0}\dfrac{\Delta v}{\Delta t}
:::

$$a=\lim_{\Delta t\to0}\dfrac{\Delta v}{\Delta t}$$
::::

其中，[]{.arithmatex}$\bar a$ 是反映质点运动速度在 []{.arithmatex}$\Delta t$ 时间内变化快慢和方向物理量。

当 []{.arithmatex}$\Delta t\to0$ 时，成为能精确描述的瞬时加速度。

做直线运动的质点的速度随时间的变化关系，可以在 []{.arithmatex}$v-t$ 坐标中用一条曲线（称为速度图线）来表示。同样，平均加速度 []{.arithmatex}$\bar a$ 和加速度 []{.arithmatex}$a$ 分别是过曲线上两点割线的斜率和曲线上一点切线的斜率。

应用 []{.arithmatex}$v-t$ 图像（即速度图线）可以求出质点在任意时间内的位移，具体做法可以用近似求解。令 []{.arithmatex}$t_1\to t_2$ 时间内分成 []{.arithmatex}$n$ 个相等的小段，每段大小为 []{.arithmatex}$\Delta t$，只需 []{.arithmatex}$\Delta t$ 足够小，就可以近似认为 []{.arithmatex}$\Delta t$ 内速度大小几乎不变，然后写出总面积：

:::: {.arithmatex}
::: {.MathJax_Preview}
S=\sum\_{i=1}\^nv(t_i)\Delta t
:::

$$S=\sum_{i=1}^nv(t_i)\Delta t$$
::::

其中 []{.arithmatex}$v(t_i)$ 为第 []{.arithmatex}$i$ 条内的速度值。当 []{.arithmatex}$\Delta t\to0$，即 []{.arithmatex}$n\to\infty$ 时，此值 []{.arithmatex}$S$ 即为位移的精确值。

## 解题方法 {#_6}

### 运动学方程 {#_7}

加速度 []{.arithmatex}$a$ 保持不变的匀速直线运动称为匀变速直线运动。

|              描述              | 公式                                     |
|:------------------------------:|------------------------------------------|
|  少 []{.arithmatex}$x$ 的公式  | []{.arithmatex}$v_t=v_0+at$              |
|  少 []{.arithmatex}$a$ 的公式  | []{.arithmatex}$x=\dfrac{v_0+v_t}{2}t$   |
| 少 []{.arithmatex}$v_t$ 的公式 | []{.arithmatex}$x=v_0t+\dfrac{1}{2}at^2$ |
| 少 []{.arithmatex}$v_0$ 的公式 | []{.arithmatex}$x=v_tt-\dfrac{1}{2}at^2$ |
|  少 []{.arithmatex}$t$ 的公式  | []{.arithmatex}$2ax={v_t}^2-{v_0}^2$     |

上述方程包括五个参量：[]{.arithmatex}$v_0$、[]{.arithmatex}$v_t$、[]{.arithmatex}$a$、[]{.arithmatex}$t$、[]{.arithmatex}$x$。

若把这五个参量当成是「独立参量」，那么以上各方程独立的只有两个方程，因此欲由上述方程求解未知参量，必须先给出三个参量。

### 平均速度 {#_8}

| 描述 | 公式 |
|:--:|----|
| 平均速度等于中时速度 | []{.arithmatex}$\bar v=v_{t/2}=\dfrac{v_0+v_t}{2}$ |
| 中位移速度等于平方平均数 | []{.arithmatex}$v_{x/2}=\sqrt{\dfrac{v_t^2+v_0^2}{2}}$ |
| 中位移速度推广 | []{.arithmatex}$v_{mx/n}=\sqrt{\dfrac{(n-m)v_0^2+mv_t^2}{n}}$ |

题型：知道两段时间和位移，求出平均速度作为中时速度，可得加速度。

### 公式的选择 {#_9}

把已知量打对钩，要求的打问号，例如：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} v_0&\checkmark\\ v_t&\checkmark\\ a&\\?\\\\ t&\checkmark\\ x& \end{cases}
:::

$$\begin{cases}
v_0&\checkmark\\
v_t&\checkmark\\
a&\,?\,\\
t&\checkmark\\
x&
\end{cases}$$
::::

于是考虑用少 []{.arithmatex}$x$ 的公式，即 []{.arithmatex}$v_t=v_0+at$。

### 无初速度比例 {#_10}

等分时间：

| 物理量 | 比例 | 解释 |
|:--:|:--:|----|
| 末速度 | []{.arithmatex}$1:2:3:4:\dots$ | 由 []{.arithmatex}$v=at$ 可知 |
| 位移 | []{.arithmatex}$1:4:9:16:\dots$ | 由 []{.arithmatex}$x=0.5at^2$ 可知 |
| 位移差分 | []{.arithmatex}$1:3:5:7:\dots$ | 由位移差分可得 |

等分位移：

| 物理量 | 比例 | 解释 |
|:--:|:--:|----|
| 末速度 | []{.arithmatex}$1:\sqrt2:\sqrt3:\sqrt4:\dots$ | 由 []{.arithmatex}$x=0.5at^2$ 可知 |
| 时间 | []{.arithmatex}$1:\sqrt2:\sqrt3:\sqrt4:\dots$ | 由 []{.arithmatex}$v=at$ 可知 |
| 时间差分 | []{.arithmatex}$1:\sqrt2-1:\sqrt3-\sqrt2:\sqrt4-\sqrt3:\dots$ | 由位移差分可得 |

## 实际问题 {#_11}

### 逐差法 {#_12}

有公式：

:::: {.arithmatex}
::: {.MathJax_Preview}
\Delta x=aT\^2
:::

$$\Delta x=aT^2$$
::::

表示的是，两段相邻 []{.arithmatex}$T$ 时间内，位移的差值 []{.arithmatex}$x_2-x_1$ 的数值。

根据这个，可以计算打点计时器算加速度。

多段逐差法计算：

- 求 []{.arithmatex}$v$ 瞬时速度：

  从这个点前后找最长的相等等分时间，用总位移除以总时间。

- 求 []{.arithmatex}$a$ 加速度：

  在位移中选择最长的连续的偶数段，记为 []{.arithmatex}$n+n=2n$ 段，则：

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  a=\dfrac{x_后-x_前}{(nT)\^2}
  :::

  $$a=\dfrac{x_后-x_前}{(nT)^2}$$
  ::::

  例如：

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  a=\dfrac{(x_3+x_4)-(x_1+x_2)}{(2T)\^2}
  :::

  $$a=\dfrac{(x_3+x_4)-(x_1+x_2)}{(2T)^2}$$
  ::::

  注意原始点和计数点的关系。

### 函数法 {#_13}

列出位移**或位置**关于时间的函数，联立。

相遇，令 []{.arithmatex}$\Delta x(t)=0$，极值利用二次函数或分式函数求解。

### 图像法 {#_14}

一般画出 []{.arithmatex}$v-t$ 图像，图像面积的意义为位移大小。

图像法的缺点：没有绝对位置信息，无法表示变加速度，变加速度需要分段。

- 常规图像：

  ![alt text](../image-4.avif)

  ![alt text](../image-5.avif)

- 特殊图像 []{.arithmatex}$\dfrac{x}{t}-t$ 图像：由 []{.arithmatex}$x=v_0t+\dfrac{1}{2}at^2$ 可得 []{.arithmatex}$\dfrac{x}{t}=v_0+\dfrac12at$，图线斜率为 []{.arithmatex}$\dfrac12a$，图像纵截距为初速度，如图 a。

  特殊图像 []{.arithmatex}$v^2-x$ 图像：由 []{.arithmatex}$v^2-v_0^2=2ax$ 可得 []{.arithmatex}$v^2=v_0^2+2ax$，图线斜率为 []{.arithmatex}$2a$，图像纵截距为初速度的二次方，如图 b。

  ![alt text](../image-6.avif){width="70%"}

- 特殊图像 []{.arithmatex}$a-x$ 图像：由 []{.arithmatex}$v^2-v_0^2=2ax$ 可得 []{.arithmatex}$ax=\dfrac{v^2-v_0^2}{2}$，图线与 []{.arithmatex}$x$ 轴所围成面积表示速度平方的变化量的一半，如图 c。

  ![alt text](../image-8.avif){width="30%"}

注意声明正方向。

注意：判定不需要证明，直接给出结论。

特殊图像问题：一次函数关注解析式、[]{.arithmatex}$k,b$ 含义，二次函数关注特殊点。

## 直线运动例题 {#_15}

### 例题一 {#_16}

一物体从静止开始从 []{.arithmatex}$A$ 点做匀加速直线运动，加速度大小为 []{.arithmatex}$5\mathrm{m/s^2}$。一段时间后做匀减速直线运动，加速度大小为 []{.arithmatex}$2.5\mathrm{m/s^2}$，已知 []{.arithmatex}$AB$ 距离为 []{.arithmatex}$60\mathrm{m}$，求物体加速多久，可以恰好停在 []{.arithmatex}$B$ 点。

设加速时间为 []{.arithmatex}$t\mathrm{s}$，则可以列出方程：

:::: {.arithmatex}
::: {.MathJax_Preview}
5t\times\left(\dfrac{5t}{2.5}+t\right)\times\dfrac{1}{2}=60
:::

$$5t\times\left(\dfrac{5t}{2.5}+t\right)\times\dfrac{1}{2}=60$$
::::

解得 []{.arithmatex}$t=2\sqrt2\mathrm{s}$。

### 例题二 {#_17}

一火箭从某个无大气层的行星的一个极地竖直向上发射。由火箭上传递过来的无线电信息知，从火箭发射时的一段时间 []{.arithmatex}$\tau$ 内，火箭上所有物体对支持物的压力或对其悬挂装置的拉力是火箭发射前的 []{.arithmatex}$1.8$ 倍。在落回行星表面前的所有时间内，火箭里的物体处于完全失重状态。试问，从火箭发射到落回行星表面经过多少时间？设行星引力大小随距行星高度的变化可以忽略不计。

设星球重力加速度 []{.arithmatex}$g$，则火箭上升的 []{.arithmatex}$\tau$ 时间内，加速度 []{.arithmatex}$a$ 恒为：

:::: {.arithmatex}
::: {.MathJax_Preview}
a=(1.8-1)g=0.8g
:::

$$a=(1.8-1)g=0.8g$$
::::

在 []{.arithmatex}$\tau$ 时间内，火箭达到的高度：

:::: {.arithmatex}
::: {.MathJax_Preview}
h=\dfrac{1}{2}a\tau\^2
:::

$$h=\dfrac{1}{2}a\tau^2$$
::::

在 []{.arithmatex}$t$ 秒末火箭的速度（方向向上）：

:::: {.arithmatex}
::: {.MathJax_Preview}
v=a\tau
:::

$$v=a\tau$$
::::

火箭落回星球表面，完全失重表明火箭自由落体：

:::: {.arithmatex}
::: {.MathJax_Preview}
-h=vt-\dfrac{1}{2}gt\^2
:::

$$-h=vt-\dfrac{1}{2}gt^2$$
::::

带入可得：

:::: {.arithmatex}
::: {.MathJax_Preview}
-0.4g\tau\^2=0.8g\tau t-\dfrac{1}{2}gt\^2
:::

$$-0.4g\tau^2=0.8g\tau t-\dfrac{1}{2}gt^2$$
::::

解得 []{.arithmatex}$t_1=-0.4\tau{\scriptsize\texttt{（舍）}},t_2=2\tau$。

即火箭从发射到落回星球表面共用时 []{.arithmatex}$3\tau$ 时间。

### 例题三 {#_18}

两个完全相同的球 []{.arithmatex}$A$ 和 []{.arithmatex}$B$，质量均为 []{.arithmatex}$m$，[]{.arithmatex}$A$ 在 []{.arithmatex}$B$ 后的距离为 []{.arithmatex}$a$。如 []{.arithmatex}$A$ 受沿 []{.arithmatex}$AB$ 方向的冲量 []{.arithmatex}$I$ 的作用，同时 []{.arithmatex}$B$ 受沿 []{.arithmatex}$AB$ 方向的常力 []{.arithmatex}$F$ 的作用开始运动。试推导 []{.arithmatex}$A$ 不超越 []{.arithmatex}$B$ 的条件。

球 []{.arithmatex}$A$ 受到冲量 []{.arithmatex}$I$ 的作用，做速度为 []{.arithmatex}$v_A$ 的匀速运动：

:::: {.arithmatex}
::: {.MathJax_Preview}
I=mv_A
:::

$$I=mv_A$$
::::

球 []{.arithmatex}$B$ 受到常力 []{.arithmatex}$F$ 的作用，做加速度为 []{.arithmatex}$a_B$ 的匀加速运动：

:::: {.arithmatex}
::: {.MathJax_Preview}
F=ma_B
:::

$$F=ma_B$$
::::

则运动方程：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} x_A&=v_At&&={I\over m}t\\ x_B&=a+\dfrac{1}{2}at\^2&&=a+\dfrac{1}{2}{F\over m}t\^2 \end{aligned}
:::

$$\begin{aligned}
x_A&=v_At&&={I\over m}t\\
x_B&=a+\dfrac{1}{2}at^2&&=a+\dfrac{1}{2}{F\over m}t^2
\end{aligned}$$
::::

球 []{.arithmatex}$A$ 不超越 []{.arithmatex}$B$，即 []{.arithmatex}$x_B$ 恒大于 []{.arithmatex}$x_A$：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} x_B\>x_A\\ a+\dfrac{1}{2}{F\over m}t\^2\>{I\over m}t\\ 2am+Ft\^2\>2It \end{aligned}
:::

$$\begin{aligned}
x_B>x_A\\
a+\dfrac{1}{2}{F\over m}t^2>{I\over m}t\\
2am+Ft^2>2It
\end{aligned}$$
::::

得到：

:::: {.arithmatex}
::: {.MathJax_Preview}
Ft\^2-2It+2am\>0
:::

$$Ft^2-2It+2am>0$$
::::

因为 []{.arithmatex}$F>0$，此式恒成立的条件为 []{.arithmatex}$\Delta<0$，即：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} 4I\^2-8maF\<0\\ I\^2\<2maF \end{aligned}
:::

$$\begin{aligned}
4I^2-8maF<0\\
I^2<2maF
\end{aligned}$$
::::
