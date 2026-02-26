# 圆周运动

## 圆周运动相关定义

### 物理量

1. 线速度：单位时间通过的弧长，$v(\mathrm\{m/s})$；
2. 角速度：单位时间通过的角度，$\omega(\mathrm\{rad/s})$；
3. 周期：完成一次的时间，$T(\mathrm\{s})$；
4. 频率：单位时间完成的次数：$f(\mathrm\{s^\{-1},Hz})$；
5. 转速：单位时间完成的圈数：$n(\mathrm\{r/s})$。

### 匀速圆周运动

$$
T=\dfrac\{2\pi r}\{v}=\dfrac\{2\pi}\{\omega}
$$

推导出来：

$$
v=\omega r
$$

即速度（$v$）在（$=$）绕（$r$）弯（$\omega$）。

$$
f=n=\dfrac\{1}\{T}
$$

### 向心力和向心加速度

向心力：

$$
F\_c=\dfrac\{mv^2}\{r}=m\omega^2r=mv\omega
$$

向心加速度：

$$
a\_c=\dfrac\{v^2}\{r}=\omega^2r=v\omega
$$

## 圆周运动解题思路

### 列表法

对于匀速圆周运动多个圈的题目，列表：

$$
\begin\{array}\{|c|l|l|l}\hline \&P\_c\&Q\_c&\dots\\\hline \bm r\\\hline \bm \omega\\\hline \bm v\\\hline \bm a\\\hline \end\{array}
$$

上面对应的就是几个圆周，从上到下填表。

填表的时候常用公式 $a=v\omega$。

如果是求比例，那么设 $\omega$ 相同的点为单位 $1$。

### 关联速度

现象：传送带上，各处线速度相同；同一物体，各处角速度相同。

现象：沿绳沿杆速度大小相同，力相同，垂直于接触面方向速度相同。

解决方法：

1. 判断合运动方向；
2. 分解合运动到沿绳沿杆方向；
3. 根据速度分量列等式。

### 牛二思路

切线方向，列平衡式子，注意这个式子一定要列，下面可能会用到；

向心方向，列 $F\_合=F\_向 $（匀速），其中合外力通过受力分析找，$r$ 要找。

常有模型：圆锥摆。

## 圆锥摆模型

### 基础圆锥摆模型

指向圆心和竖直方向建系，列出两个方向上的牛二方程：

$$
\begin\{aligned} F\_合=T\sin\theta\ T\cos\theta=mg \end\{aligned}
$$

其中 $\theta$ 为绳子和竖直方向的夹角。

列出合外力等于向心力：

$$
F\_合=m\omega^2r
$$

计算得到：

$$
\omega=\sqrt\{\dfrac\{g}\{L\cos\theta}}
$$

### 同角不同面模型

![同角不同面|right|w30%](data:image/avif;base64,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)
物体和法线的夹角相同，但是不同水平面，如右图所示。

假设接触面光滑：

$$
\begin\{aligned} F\_合=F\_N\cos\theta\ F\_N\sin\theta=mg \end\{aligned}
$$

结论是向心加速度相同：

$$
a=\dfrac\{F\_合}\{m}=g\cot\theta
$$

同角不同面，最常见的是漏斗里面小球转圈圈。

- 根据 $F\_向=ma$，因此质量越大，向心力越大。

- 根据 $\displaystyle F\_N=\dfrac\{mg}\{\sin\theta}$，因此质量越大，对斜面压力越大。

- 根据 $a=\omega^2r$，因此半径越大，角速度越小。

- 根据 $\displaystyle a=\dfrac\{v^2}\{r}$，因此半径越大，线速度越大。

### 同面不同角模型

![同面不同角|right|w35%](/static/image/image-1.79446c9952.avif)
物体在同一平面，与法线的夹角不同，如右图。

根据圆锥摆的公式，角速度 $\omega$ 对各物体相同：

$$
\omega=\sqrt\{\dfrac\{g}\{L\cos\theta}}=\sqrt\{\dfrac\{g}\{H}}
$$

- 根据 $a=\omega^2r$，因此半径越大，加速度越大。

- 根据 $v=r\omega$，因此半径越大，线速度越大。

反向推论：角速度相同，则物体也会在同一平面上。

### 圆锥摆求夹角

在一根长度为 $l$ 的绳子下端悬挂一个质量为 $M$ 的小球，以匀角速度 $\omega$ 旋转。

求：绳子与铅锤方向所成的角 $\theta$。

易得：

$$
\begin\{aligned} T\cos\theta&=Mg\ T\sin\theta&=M\omega^2r=M\omega^2l\sin\theta \end\{aligned}
$$

注意到一个可行解是 $\sin\theta=0$，即 $\theta=0$（因为 $\theta=\pi$ 是不稳定状态）。

否则，

$$
T=M\omega^2l
$$

即，

$$
Mg=T\cos\theta=M\omega^2l\cos\theta
$$

$$
\cos\theta=\dfrac\{g}\{\omega^2l},;\theta=\arccos\left(\dfrac\{g}\{\omega^2l}\right)
$$

结论：

$$
\theta=\left\{\begin\{aligned} &0&,\omega\le\sqrt\{\dfrac\{g}\{l}}\ &\arccos\left(\dfrac\{g}\{\omega^2l}\right)&,\omega>\sqrt\{\dfrac\{g}\{l}}\ \end\{aligned}\right.
$$

### 圆锥摆临界问题

先求出临界状态下的角速度。

根据临界角速度和实际角速度，做出受力分析。

## 圆盘模型

### 单物体圆盘模型

一个水平转动的圆盘上有一个物体。

此时，摩擦力提供向心力，物体与圆盘之间的摩擦因数为 $\mu$。

当最大静摩擦力（大小视为滑动摩擦力）等于向心力时恰好不滑动。

$$
\mu mg=m\omega^2r
$$

得出：

$$
\omega=\sqrt\{\dfrac\{\mu g}\{r}}
$$

### 多物体圆盘模型

一个水平转动的圆盘上两个物体，考虑谁会先开始滑动。

物体 $m\_1,m\_2,\mu\_1,\mu\_2$，可以计算出每个物体的临界角速度。

$$
\begin\{aligned} \mu\_1m\_1g&=m\_1\omega\_1^2r\_1\ \mu\_2m\_2g&=m\_2\omega\_2^2r\_2\ \end\{aligned}
$$

得出：

$$
\begin\{aligned} \omega\_1&=\sqrt\{\mu\_1g\over r\_1}\ \omega\_2&=\sqrt\{\mu\_2g\over r\_2} \end\{aligned}
$$

即 $\displaystyle\{\mu\over r}$ 小的先发生滑动，大的后发生滑动。

如果摩擦系数相同，则离圆心越远，越先开始滑动。

### 同侧连接体圆盘模型

两物体质量分别为 $m\_1,m\_2$，用轻绳连接。

两物体与圆盘摩擦系数为 $\mu\_1,\mu\_2$，且距圆心分别为 $r\_1,r\_2(r\_1\<r\_2)$ 同侧。

问题一：转速多大绳子出现拉力。

根据单物体圆盘模型，两物体独立的临界角速度分别为：

$$
\omega\_1=\sqrt\{\mu\_1g\over r\_1}
$$

$$
\omega\_2=\sqrt\{\dfrac\{\mu\_2g}\{r\_2}}
$$

如果 $\omega\_1\<\omega\_2$，则绳子会松弛，我们不考虑这个情况。

因此，当转速大于等于 $\omega\_2$ 的时候，绳子会出现拉力。

问题二：转速多大物体一起运动。

对物体整体法分析：

$$
\mu\_1m\_1g+\mu\_2m\_2g=m\_1\omega^2r\_1+m\_2\omega^2r\_2
$$

得出：

$$
\omega=\sqrt\{\dfrac\{(\mu\_1m\_1+\mu\_2m\_2)g}\{m\_1r\_1+m\_2r\_2}}
$$

假设物体质量相等，即 $m\_1=m\_2$，则有：

$$
\omega=\sqrt\{(\mu\_1+\mu\_2)g\over r\_1+r\_2}
$$

假设物体摩擦因数相等，即 $\mu\_1=\mu\_2$，则有：

$$
\omega=\sqrt\{\dfrac\{\mu g(m\_1+m\_2)}\{m\_1r\_1+m\_2r\_2}}
$$

假设 $m\_1=m\_2$ 且 $\mu\_1=\mu\_2$，则有：

$$
\omega=\sqrt\{\dfrac\{2\mu g}\{r\_1+r\_2}}
$$

注意到不可能有 $r\_1=r\_2$，因为是两个物体。

### 异侧连接体圆盘模型

可以进行质心的分析，简单来说两物体需要提供的向心力增量：

$$
\begin\{aligned} \Delta F\_1&=m\_1\Delta(\omega^2)r\_1\ \Delta F\_2&=m\_2\Delta(\omega^2)r\_2 \end\{aligned}
$$

随着 $\omega$ 的增大，一定有一个先产生相对滑动趋势，假设是 $1$ 物体。

$$
\omega\_1=\sqrt\{\dfrac\{\mu\_1g}\{r\_1}}
$$

表示达到这个角速度时 $1$ 物体恰好没有产生相对滑动趋势。

此时，我们知道角速度增大一个小的增量 $\Delta\omega$，绳子就会提供 $\Delta F\_1$ 的拉力。

- 此时注意到，如果 $\Delta F\_1>\Delta F\_2$，也就是 $m\_1r\_1>m\_2r\_2$，此时绳子拉力的增大快于了 $2$ 物体向心力的需求增量。那么，$2$ 物体的摩擦力就会减小，然后反向，最终向 $1$ 物体一侧滑开。我们设 $\omega\_2$ 表示恰好 $2$ 物体没有摩擦力，$\omega\_3$ 表示恰好不滑动。

  $$
  \begin\{aligned} \omega\_1&=\sqrt\{\mu g\over r\_1}\ \omega\_2&=\sqrt\{\mu g\over r\_1-r\_2}\ \omega\_3&=\sqrt\{2\mu g\over r\_1-r\_2} \end\{aligned}
  $$

- 此时注意到，如果 $\Delta F\_1=\Delta F\_2$，也就是 $m\_1r\_1=m\_2r\_2$，绳子拉力的增量等于了 $2$ 物体向心力的需求增量。那么，此时绳子拉力不断增大，$1$ 物体保持最大静摩擦状态，$2$ 物体保持原先的摩擦力大小，然而绳子拉力大小不断增大，有拉力 $T$ 和角速度的关系：

  $$
  T=m\_2(\omega^2-\omega\_1)^2r\_2
  $$

- 此时注意到，如果 $\Delta F\_1\<\Delta F\_2$，也就是 $m\_1r\_1\<m\_2r\_2$，此时绳子拉力的增量不足 $2$ 物体向心力的需求增量，因此 $2$ 物体摩擦力继续增大，因为绳子拉力保持了 $1$ 的静止，因此最终发生 $2$ 的最大静摩擦及滑动，向 $2$ 物体一侧滑开。

注意到这个可以通过质点的形式解决，我们将会在质点系中再次讨论。

## 非匀速绳杆模型

### 基础形态

区别：绳子无法提供对物体向上的力。

列式：

$$
\begin\{aligned} G+T&=F\_c\ mg+T&=m\frac\{v^2}\{r} \end\{aligned}
$$

![alt text|w100%](/static/image/C1C8B823E95E88FD9F01E5EA5E9E2311.97a0c1c78e.avif)
### 绳模型

考虑最高点最小速度、恰好经过顶点、绳子无拉力：

物理量的表示，即：$v$ 最小，$F\_c$ 最小，$T$ 为 $0$。

故：

$$
\begin\{aligned} mg&=m\frac\{v^2}\{r}\ v&=\sqrt\{gr} \end\{aligned}
$$

性质：

- 在圆上一定满足提供了向心力 $F\_r=\dfrac\{mv^2}\{r}$。

- 脱离的临界态：在圆上、无拉力弹力、向心方向恰好提供了 $F\_r$。

- 脱离的瞬间重力与所在半径连线夹角 $\cos\theta=\dfrac\{v^2}\{gr}$。

### 杆模型

杆子可以提供最大为 $-mg$ 的力（表示为顶着物体）。

即，有最高点最小速度 $v=0$，杆子不受力 $v=\sqrt\{gr}$。

最高点时，杆子的力可以向上、向下，因此记临界速度 $v\_0=\sqrt\{gr}$：

若 $v>v\_0$ 则杆子对物体的力向下，若 $v\<v\_0$ 杆子对物体的力向上。

然后写牛二式子 $mg\pm T=m\dfrac\{v^2}\{r}$。

拉力的作用力范围为 $(-\infty,mg]$，以支持力为正。

### 圆环模型

小球在圆环里面转圈，双环相当于杆，单环相当于绳。

注意到双环中，只可能两侧中的一侧受力，写牛二即可求 $T$。

### 动能定理

重力做功等于动能变化量，最高点速度可以求出来。

那么就可以求出来最低点的速度以及绳子的拉力。

### 绳子碰钉模型

一个绳子拴着小球，摆下来遇到钉子然后绕着更小的半径运动。

瞬间小球速度不变，忽略能量损耗，小球线速度 $v$ 始终不变。

- 根据 $\displaystyle F=\dfrac\{mv^2}\{r}$，绳子拉力增大；

- 根据 $\displaystyle\omega=\dfrac\{v}\{r}$，角速度增大；

- 根据 $a=v\omega$，加速度增大。

- 根据 $\displaystyle T=\dfrac\{2\pi}\{\omega}$，周期减小。
