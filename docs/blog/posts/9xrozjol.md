---
description: 本文以3Blue1Brown为来源，用光线反射解释滑块弹性碰撞问题。通过坐标变换证明速度不变和反射角相等，得到碰撞次数为⌊π/arctan√(m2/m1)⌋，直观展现圆周率。
authors:
  - RainPPR
---

# 滑块、光线和圆周率

本文以3Blue1Brown为来源，用光线反射解释滑块弹性碰撞问题。通过坐标变换证明速度不变和反射角相等，得到碰撞次数为⌊π/arctan√(m2/m1)⌋，直观展现圆周率。

<!-- more -->

注：下文使用弧度制，如果你不会，请见 [三角函数](./022dp2g2)。

来源：3B1B（3Blue1Brown）。

## 光线反射次数

光线平行于夹角一边入射，夹角为 $\theta$。

那么反射次数 $n=\lfloor\pi/\theta\rfloor$，推导过程：

把反射类比为在穿过镜子，进入镜面世界。

于是我们的光线完全反射就需要穿过 $\pi$ 的角度。

即 $\lfloor\pi/\theta\rfloor$。然后你理解一下（万能解释：易证。

## 滑块碰撞次数

场景为，一个质量为 $m_1$ 的滑块，向左撞击质量为 $m_2$ 的滑块。

最左侧有一墙壁；忽略动能损失（弹性碰撞），注意 $m_1>m_2$。

我们记平面直角坐标系 $xOy$，$x=\sqrt{m_1}d_1,y=\sqrt{m_2}d_2$。

其中 $d_1$ 表示 $1$ 物体左侧距墙面，$d_2$ 表示 $2$ 物体右侧距墙面。

根据动能守恒及动量守恒，易推得反射角等于入射角，即相当于光线的碰撞。

先看结论，后面证明。

镜面相当于 $y=\sqrt{m_2/m_1}x$，及 $y=m_2$。

即镜面夹角为 $\theta=\arctan(\sqrt{m_2/m_1})$。

则易知碰撞次数为 $\lfloor\pi/\arctan(\sqrt{m_2/m_1})\rfloor$。

神奇吧（

## 证明一：点的速度不变

对应光速不变。

对于 $x$ 方向：

$$
{\mathrm dx\over\mathrm dt}=\sqrt{m_1}{\mathrm dd_1\over\mathrm dt}=\sqrt{m_1}v_1
$$

对于 $y$ 方向：

$$
{\mathrm dy\over\mathrm dt}=\sqrt{m_2}{\mathrm dd_2\over\mathrm dt}=\sqrt{m_2}v_2
$$

速度的大小：

$$
\begin{aligned}
v&=\sqrt{(\mathrm dx/\mathrm dt)^2+(\mathrm dy/\mathrm dt)^2}\\
&=\sqrt{m_1v_1^2+m_2v_2^2}=\sqrt{2E_k}
\end{aligned}
$$

因为动能守恒，即：

$$
v=\mathrm{const.}
$$

Q.E.D.

## 证明二：反射角等于入射角

对应光的反射定律。

其中镜面相当于 $d_1=d_2$，即 $y=\sqrt{m_2/m_1}x$，斜率 $k=\sqrt{m_2/m_1}$。

根据动量守恒，我们知道：

$$
m_1v_1+m_2v_2=\mathrm{const.}
$$

我们把它看成列向量点乘的形式：

$$
\begin{bmatrix}
m_1\\m_2
\end{bmatrix}\cdot\begin{bmatrix}
v_1\\v_2
\end{bmatrix}=\mathrm{const.}
$$

类比的，我们把 $mv$ 写成 $\sqrt{m}\cdot\sqrt{m}v$ 的形式：

$$
\sqrt{m_1}\cdot\sqrt{m_1}v_1+\sqrt{m_2}\cdot\sqrt{m_2}v_2=\mathrm{const.}
$$

即：

$$
\begin{bmatrix}
\sqrt{m_1}\\\sqrt{m_2}
\end{bmatrix}\cdot\begin{bmatrix}
\sqrt{m_1}v_1\\\sqrt{m_2}v_2
\end{bmatrix}=\mathrm{const.}
$$

注意到后面的形式就是 $\mathrm dx/\mathrm dt$ 等的形式：

$$
\begin{bmatrix}
\sqrt{m_1}\\\sqrt{m_2}
\end{bmatrix}\cdot\begin{bmatrix}
\mathrm dx/\mathrm dt\\\mathrm dy/\mathrm dt
\end{bmatrix}=\mathrm{const.}
$$

我们记为：

$$
\bm w\cdot\bm v=||\bm w||\cdot||\bm v||\cdot\cos\theta=\mathrm{const.}
$$

注意到 $||\bm w||,||\bm v||$ 都是不变的，因此 $\cos\theta$ 也不变。

即与镜面的夹角不变，即反射角等于入射角。

Q.E.D.
