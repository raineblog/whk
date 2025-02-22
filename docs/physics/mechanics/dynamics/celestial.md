# 天体运动

## 天体运动概述

### 天体运动相关概念

- $r$：质心间距，$r=R_1+d+R_2$；
- $R$：星球半径；
- $h$：轨道高度；

1. 当讨论质点与星球时：$r=R+h$；
2. 贴地飞行、近地卫星、忽略高度：$r=R$；
3. 轨道高度远大于星球半径、忽略星球半径：$r=h$。

### 万有引力定律

公式：$F=G\dfrac{Mm}{r^2}$。

其中 $r$ 为质心间距，一般表示为 $r=R_1+d+R_2$。

常用割补法求解 $F_r=F_1-F_2$。

同时，可得引力加速度 $a_g=G\dfrac{M}{r^2}$。

## 开普勒三大定律

### 开普勒第一定律

又称：椭圆定律、轨道定律。

行星绕太阳的轨迹是椭圆轨道，太阳在椭圆的一个焦点上。

### 开普勒第二定律

又称：等面积定律。

在相等时间内，行星与太阳的连线扫过的面积相等。

结论：近日点速度较大，远日点速度较小。

### 开普勒第三定律

又称：周期定律。

行星轨迹的半长轴 $a$ 的三次方与公转周期 $T$ 的平方的比值是一个定值 $k$。

用公式表示为：$\dfrac{{a_1}^3}{{T_1}^2}=\dfrac{{a_2}^3}{{T_2}^2}=k$。

其中 $k$ 是常数，只与中心天体的质量有关。

## 三大宇宙速度

### 第一宇宙速度

第一宇宙速度（环绕速度）是指在地球上发射的物体绕地球飞行作圆周运动所需的最小初始速度。

物体从地面发射，即 $r=R$，那么 $v=\sqrt{\dfrac{GM}{R}}=\sqrt{\dfrac{R^2g}{R}}=\sqrt{gR}\approx 7.9\mathrm{km/s}$。

### 第二宇宙速度

第二宇宙速度（脱离速度、逃逸速度）是指在地球上发射的物体摆脱地球引力束缚，飞离地球所需的最小初始速度。

物体从地面发射，即 $r=R$，那么从动能和重力势能的角度：

$$
\begin{aligned}
\dfrac{1}{2}mv^2&=G\dfrac{Mm}{R}\\
v^2&=\dfrac{2GM}{R}\\
v&=\sqrt{\dfrac{2R^2g}{R}}\\
v&=\sqrt{2gR}\approx 11.2\mathrm{km/s}
\end{aligned}
$$

### 第三宇宙速度

第三宇宙速度（英语：third cosmic velocity），是指在地球上发射的物体摆脱太阳引力束缚，飞出太阳系所需的最小初始速度。

在地球轨道上，要脱离太阳引力所需的初始速度为 $42.1\mathrm{km/s}$；地球绕太阳公转时令地面所有物体已具有 $29.8\mathrm{km/s}$ 的初始速度。

故此若沿地球公转方向发射，还需要提供 $12.3\mathrm{km/s}$ 的动能，因此在脱离地球引力以外额外再加上适当的动能即可：

$$
\begin{aligned}
\dfrac{1}{2}m{v_3}^2&=\dfrac{1}{2}m{v_2}^2+\dfrac{1}{2}m\Delta v^2\\
{v_3}^2&={v_2}^2+\Delta v^2\\
v_3&=\sqrt{{v_2}^2+\Delta v^2}\\
v_3&\approx\sqrt{11.2^2+12.3^2}\approx 16.7\mathrm{km/s}
\end{aligned}
$$

记忆方法：

- 第一 $[7.9]$。

- 第二 $[1+1]$（$1+1=2\Rightarrow11.2$）。

- 第三 $[1+6]$（$1+6=7\Rightarrow16.7$）。

## 天体运动模型概述

### 匀速圆周天体运动

天体运动公式：

$$
\begin{aligned}
v&=\sqrt{\dfrac{GM}{r}}\\
\omega&=\sqrt{\dfrac{GM}{r^3}}\\
T&=2\pi\sqrt{\dfrac{r^3}{GM}}\\
a&=\dfrac{MG}{r^2}\\
\omega&=\dfrac{2\pi}{T}
\end{aligned}
$$

黄夫人公式：$T^2MG=4\pi^2r^3$。

物理量的变化：当 $r$ 增大时，$v$ 减小、$\omega$ 减小、$a$ 减小，$T$ 增大（前提：圆周运动）。

代数运算：常取 $G\approx 20/3\times10^{-11}$（忽略单位），$\pi^2\approx 10$。

古老的公式：$\rho=\dfrac{m}{V}$，$V=\dfrac{4}{3}\pi r^3$。

### 简单双星

两个星球同时绕一质心 $O$ 做匀速圆周运动。

基本原理为 $F_g=F_c$，列式：

$$
\begin{aligned}
G\dfrac{m_Am_B}{L^2}&=m_A\omega^2r_{OA}\\
G\dfrac{m_Am_B}{L^2}&=m_B\omega^2r_{OB}\\
\end{aligned}
$$

两式做比：$m_Ar_{OA}=m_Br_{OB}$。

两式做和：$G(m_A+m_B)=\omega^2L^2(r_{OA}+r_{OB})=\omega^2L^3=GM$，其中 $M=m_A+m_B$。

结论：

1. 此双星系统中，两星所受万有引力大小相等。
2. 此双星系统中，$\omega$ 只与两星总质量 $M$ 和间距 $L$ 有关（若一星质量加 $\Delta m$，一星质量减 $\Delta m$，$\omega$ 不变）。
3. 此双星系统中，一星质量越大，公转半径越小。
4. 此双星系统中，根据两星 $\omega$ 相同，则 $v=r\omega$，公转半径越大，速度越大。
5. 综上两条，一星质量越大，公转半径越小，速度越小。

### 三星及多星

对于 $N$ 体问题，这里只考虑星体依次连线，形状为正 $N$ 边形的情况。

此时，存在两个可用的条件，$\omega$ 相同，以及 $F_r$ 及 $r$ 的关系，列式即可。

其实是作者太菜，不会。

### 相遇与追及问题

总体思路：用相对角速度算时间。

公式：$t=\dfrac{\mathrm{rad}}{\Delta\omega}$，即相对角度除以相对角速度。

## 表面模型

### 忽略自转的星球表面

定义表面的物体：不绕着星球转，不一定在地面；同步卫星不属于表面物体。

### 地面位置

$MG=R^2g$，整理得 $g=\dfrac{MG}{R^2}$；

### 表面以上位置

$MG=(R+h)^2g$，整理得 $g=\dfrac{MG}{(R+h)^2}$；

### 星球内部

考虑万有引力，只有星球的一部分对物体产生万有引力。

对物体产生万有引力的部分的星球质量：$M'=\dfrac{4}{3}\pi(R-h)^3\rho$。

由 $G\dfrac{M'm}{(R-h)^2}=mg$，得 $g=\dfrac{G}{(R-h)^2}M'$。

整理得， $g=\dfrac{G}{(R-h)^2}\times\dfrac{4}{3}\pi(R-h)^3\rho=\dfrac{4}{3}G\pi(R-h)\rho$。

## 自转模型

### 万有引力和向心力

有公式：$\vec F_g=\vec G+\vec F_c$（矢量相加）。

实际上 $F_c$ 很小（其中的 $r$ 是到地轴的距离，不是星球半径）。

### 极点位置

到地轴的距离为 $0$，即向心力 $F_c=0$。

展开：

$$
\begin{aligned}
F_g&=G+F_c\\
MG&=R^2g_0\\
M&=\dfrac{R^2g_0}{G}
\end{aligned}
$$

### 赤道位置

此时 $G$ 和 $F_c$ 方向相同，则 $F_g=G+F_c$。

展开：

$$
\begin{aligned}
F_g&=G+F_c\\
G\dfrac{Mm}{R^2}&=mg+m\omega^2R\\
\dfrac{MG}{R^2}&=g+\dfrac{4\pi^2}{T^2}R\\
MG&=R^2g+\dfrac{4\pi^2}{T^2}R^3
\end{aligned}
$$

联立上述二式，可解得 $g_0$：

$$
\begin{aligned}
\dfrac{R^2g_0}{R^2}&=g+\omega^2R\\
g_0&=g+\dfrac{4\pi^2}{T^2}R
\end{aligned}
$$

同时，也可解得 $R$：

$$
\begin{aligned}
R^2g_0&=R^2g+\dfrac{4\pi^2}{T^2}R^3\\
g_0&=g+\dfrac{4\pi^2}{T^2}R\\
R&=\dfrac{(g_0-g)T^2}{4\pi^2}
\end{aligned}
$$

联立上述四式，可解得 $M$，不过这玩意没啥用。

### 星球密度

解：

$$
\begin{aligned}
\rho&=\dfrac{M}{V}=\dfrac{\frac{R^2g_0}{G}}{\frac{4}{3}\pi R^3}=\dfrac{3R^2g_0}{4\pi GR^3}\\
&=\dfrac{3g_0}{4\pi GR}=\dfrac{3g_0}{4\pi G\frac{(g_0-g)T^2}{4\pi^2}}=\dfrac{3g_0\pi}{G(g_0-g)T^2}\\
&=\dfrac{g_0}{g_0-g}\cdot\dfrac{3\pi}{GT^2}
\end{aligned}
$$
