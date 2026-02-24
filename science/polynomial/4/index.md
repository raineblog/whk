# 导数不等式 {#_1}

![alt text](../image.avif)

![alt text](../image-1.avif)

## 导数方法 {#_2}

### 不等式方法 {#_3}

求证不等式的方法有几种，最简单的是：

- 设函数，证明函数恒大于或小于零。

- 直接对函数求导，尝试证明函数最小值大于零，或最大值小于零。

- 注意到多项式只要求够多次数多导数，一定会变为零，因此如果不好解决，继续求导，对高阶导数尝试分析其是否恒正或恒负。

注意：

- 解一元一次不等式 []{.arithmatex}$ax>b$，需要按照 []{.arithmatex}$a>0,a=0,a<0$ 分类讨论。

- 解一元一次不等式 []{.arithmatex}$ax>b$，其中 []{.arithmatex}$x\in[m,n]$，先按照 []{.arithmatex}$a>0,a=0,a<0$ 分类讨论，然后按照 []{.arithmatex}$\dfrac{b}{a}$ 是否落在区间 []{.arithmatex}$[m,n]$ 内。

边界条件：

1.  二次项系数不含参数且自变量没有限制时，临界条件是 []{.arithmatex}$\Delta = 0$。

2.  二次项系数含有参数且自变量没有限制时，临界条件是二次项系数为零与 []{.arithmatex}$\Delta = 0$ 联立。

3.  二次项系数含参数且自变量有限制时，临界条件是二次项系数为零，[]{.arithmatex}$\Delta = 0$ 与区间端点处的函数值为零同时联立。

对于更复杂的情况，一般步骤如下：

- 能否直接求导解决。

- 能否通过常见变形（本文简单变形部分）后求导。

- 能否通过隐零点判断。

- 能否使用放缩技巧。

变形法：

- 除以单项式变形（[]{.arithmatex}$x^n$）。

- 整体代换、同构化变形、拆分函数、局部求值。

- 对数化：对数化是利用对数性质，将函数式中的对数与常数合并，再使用相关不等式进行放缩。例如：

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  \ln x+a=\ln(xe\^a)。
  :::

  $$\ln x+a=\ln(xe^a)。$$
  ::::

- 指数化：指数化是利用指数性质，将式子或者参数转移到指数位置上，以方便放缩。例如：

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  xe\^x=e\^{x+\ln x}\\(x\>0)，a\^x=e\^{\ln a\^x}=e\^{x\ln a}。
  :::

  $$xe^x=e^{x+\ln x}\,(x>0)，a^x=e^{\ln a^x}=e^{x\ln a}。$$
  ::::

### 简单不等式 {#_4}

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{e\^x\ge x+1,\quad x\in\R}\tag a
:::

$$\boxed{e^x\ge x+1,\quad x\in\R}\tag a$$
::::

证明：设 []{.arithmatex}$f(x)=e^x-x-1$，那么：

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x)=e\^x-1
:::

$$f'(x)=e^x-1$$
::::

因此，当 []{.arithmatex}$x>0$ 时，[]{.arithmatex}$f'(x)>0$；当 []{.arithmatex}$x<0$ 时 []{.arithmatex}$f'(x)<0$，因此：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)\ge f(0)=0
:::

$$f(x)\ge f(0)=0$$
::::

即 []{.arithmatex}$e^x\ge x+1$，带入 []{.arithmatex}$x\gets\ln x$ 有：

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{x\ge\ln x+1,\quad x\>0}\tag b
:::

$$\boxed{x\ge\ln x+1,\quad x>0}\tag b$$
::::

三角函数也有一些不等式：

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\sin x\<x,\quad x\>0}\tag c
:::

$$\boxed{\sin x<x,\quad x>0}\tag c$$
::::

证明：设 []{.arithmatex}$f(x)=x-\sin x$，那么 []{.arithmatex}$f'(x)=1-\cos x\ge0$。

所以 []{.arithmatex}$f(x)$ 在 []{.arithmatex}$(0,\infty)$ 上单调递增，[]{.arithmatex}$f(x)>f(0)=0$ 即 []{.arithmatex}$x>\sin x$。

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{x\<\tan x,\quad x\in(0,\pi/2)}\tag d
:::

$$\boxed{x<\tan x,\quad x\in(0,\pi/2)}\tag d$$
::::

证明：令 []{.arithmatex}$f(x)=\tan x-x$，则

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x)=\dfrac{1}{\cos\^2 x}-1\>0
:::

$$f'(x)=\dfrac{1}{\cos^2 x}-1>0$$
::::

所以 []{.arithmatex}$f(x)$ 在 []{.arithmatex}$(0,\pi/2)$ 上单调递增，[]{.arithmatex}$f(x)>f(0)=0$ 即 []{.arithmatex}$\tan x>x$。

我们由 []{.arithmatex}$\ln x\le x-1$ 可以推导出来一下几个基本不等式：

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln(x+1)\le x; \quad \ln\dfrac{1}{x}\ge1-x; \quad \ln x\ge1-\dfrac{1}{x}; \quad x\ln x\ge x-1
:::

$$\ln(x+1)\le x; \quad \ln\dfrac{1}{x}\ge1-x; \quad \ln x\ge1-\dfrac{1}{x}; \quad x\ln x\ge x-1$$
::::

其中最常用的不等式链为：

:::: {.arithmatex}
::: {.MathJax_Preview}
\dfrac{x}{x+1}\le\ln(x+1)\le x
:::

$$\dfrac{x}{x+1}\le\ln(x+1)\le x$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
1-\dfrac{1}{x}\le\ln x\le x-1
:::

$$1-\dfrac{1}{x}\le\ln x\le x-1$$
::::

### 一元不等式 {#_5}

我们经常见到这种形式的式子：

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x)+p(x)f(x)=q(x)
:::

$$f'(x)+p(x)f(x)=q(x)$$
::::

其中 []{.arithmatex}$p(x),q(x)$ 是关于 []{.arithmatex}$x$ 的式子，这称为一阶线性微分方程。

我们更常见到的是不等式的形式：

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x)+p(x)f(x)\>q(x)
:::

$$f'(x)+p(x)f(x)>q(x)$$
::::

我们先简单说一下简单的微分方程怎么解，我们将式子最终化为：

:::: {.arithmatex}
::: {.MathJax_Preview}
u(x)\d x=v(y)\d y
:::

$$u(x)\d x=v(y)\d y$$
::::

然后两边求积分，化简即可。

::::: {.admonition .note}
[]{.arithmatex}$p(x)=0$

我们考虑一个比较简单的形式，[]{.arithmatex}$p(x)=0$，即

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x)=q(x)
:::

$$f'(x)=q(x)$$
::::

记 []{.arithmatex}$Q'(x)=q(x)$，则：

- 若符号为 []{.arithmatex}$=$，则 []{.arithmatex}$f(x)=Q(x)+C$。

- 若符号为 []{.arithmatex}$>$，则 []{.arithmatex}$f(x)-[Q(x)+C]$ 单调递增。
:::::

::::::::::::::: {.admonition .note}
[]{.arithmatex}$q(x)=0$

我们考虑一个比较简单的形式，[]{.arithmatex}$q(x)=0$，即

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x)+p(x)f(x)=0
:::

$$f'(x)+p(x)f(x)=0$$
::::

我们有一个固定的解题方法，但是我们先推导一番，设 []{.arithmatex}$P'(x)=p(x)$。

:::: {.arithmatex}
::: {.MathJax_Preview}
\dfrac{\d y}{\d x}+p(x)y=0
:::

$$\dfrac{\d y}{\d x}+p(x)y=0$$
::::

按照微分方程的思路，

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln y=-P(x)+C
:::

$$\ln y=-P(x)+C$$
::::

即：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)=e\^{-P(x)+C}
:::

$$f(x)=e^{-P(x)+C}$$
::::

移项，构造函数 []{.arithmatex}$g(x)$：

:::: {.arithmatex}
::: {.MathJax_Preview}
g(x)=e\^{P(x)}f(x)=e\^C
:::

$$g(x)=e^{P(x)}f(x)=e^C$$
::::

具体的，对于 []{.arithmatex}$q(x)=0$ 的等式或不等式，我们两边同时乘以 []{.arithmatex}$e^{P(x)}$，即：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} e\^{P(x)}\[f\'(x)+p(x)f(x)\]&=0\\ \[e\^{P(x)}f(x)\]\'&=0 \end{aligned}
:::

$$\begin{aligned}
e^{P(x)}[f'(x)+p(x)f(x)]&=0\\
[e^{P(x)}f(x)]'&=0
\end{aligned}$$
::::

即 []{.arithmatex}$f(x)=Ce^{-P(x)}$，而对于不等式即为 []{.arithmatex}$e^{P(x)}f(x)$ 单调递增。
:::::::::::::::

例题：已知函数 []{.arithmatex}$f(x)$ 是定义在 []{.arithmatex}$\mathbb{R}$ 上的函数，且满足 []{.arithmatex}$f'(x) + f(x) > 0$，设 []{.arithmatex}$a = f(0)$，[]{.arithmatex}$b = 2f(\ln 2)$，[]{.arithmatex}$c = ef(1)$，则 []{.arithmatex}$a, b, c$ 的大小关系是？

令 []{.arithmatex}$g(x) = e^x f(x)$，则 []{.arithmatex}$g'(x) = e^x[f'(x) + f(x)] > 0$，即 []{.arithmatex}$g(x)$ 递增，因为 []{.arithmatex}$a = g(0)$，[]{.arithmatex}$b = g(\ln 2)$，[]{.arithmatex}$c = g(1)$，由 []{.arithmatex}$g(x)$ 的单调性可知 []{.arithmatex}$g(0) < g(\ln 2) < g(1)$，即 []{.arithmatex}$c > b > a$。

### 二元不等式 {#_6}

二元不等式，首选方案是将两个未知数用一个未知数表示，最常见的是两个次数相等的齐次式相除，用比值还原，将二元不等式转化为一元后，就可以求导解决了。

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\sqrt{x_1x_2}\<\dfrac{x_2-x_1}{\ln x_2-\ln x_1},\quad x_1,x_2\>0}\tag e
:::

$$\boxed{\sqrt{x_1x_2}<\dfrac{x_2-x_1}{\ln x_2-\ln x_1},\quad x_1,x_2>0}\tag e$$
::::

证明，不放假设 []{.arithmatex}$x_2>x_1$，则化简式子为：

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln x_2-\ln x_1\<\dfrac{x_2-x_1}{\sqrt{x_1x_2}}
:::

$$\ln x_2-\ln x_1<\dfrac{x_2-x_1}{\sqrt{x_1x_2}}$$
::::

设 []{.arithmatex}$t=\sqrt{x_2/x_1}>1$，则：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \text{LHS}&=\ln t\^2=2\ln t\\ \text{RHS}&=\dfrac{t\^2-1}{t}=t-\dfrac{1}{t} \end{aligned}
:::

$$\begin{aligned}
\text{LHS}&=\ln t^2=2\ln t\\
\text{RHS}&=\dfrac{t^2-1}{t}=t-\dfrac{1}{t}
\end{aligned}$$
::::

令 []{.arithmatex}$f(t)=t-\dfrac{1}{t}-2\ln t$，则：

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(t)=1+\dfrac{1}{t\^2}-\dfrac{2}{t}=\left(1-\dfrac{1}{t}\right)\^2\>0
:::

$$f'(t)=1+\dfrac{1}{t^2}-\dfrac{2}{t}=\left(1-\dfrac{1}{t}\right)^2>0$$
::::

而这个也是一个不等式，

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\ln x\<\sqrt{x}-\dfrac{1}{\sqrt{x}},\quad x\>1}\tag{f\$\_1\$}
:::

$$\boxed{\ln x<\sqrt{x}-\dfrac{1}{\sqrt{x}},\quad x>1}\tag{f$_1$}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\ln x\<\dfrac{1}{2}\left(x-\dfrac1x\right),\quad x\>1}\tag{f\$\_2\$}
:::

$$\boxed{\ln x<\dfrac{1}{2}\left(x-\dfrac1x\right),\quad x>1}\tag{f$_2$}$$
::::

因此 []{.arithmatex}$f(t)>f(1)=0$，这个也成为对数均值不等式：

:::: {.arithmatex}
::: {.MathJax_Preview}
\sqrt{x_1x_2}\<\boxed{\dfrac{x_2-x_1}{\ln x_2-\ln x_1}\<\dfrac{x_1+x_2}{2},\quad x_1,x_2\>0}\tag g
:::

$$\sqrt{x_1x_2}<\boxed{\dfrac{x_2-x_1}{\ln x_2-\ln x_1}<\dfrac{x_1+x_2}{2},\quad x_1,x_2>0}\tag g$$
::::

带入指数形式，替换 []{.arithmatex}$a\gets e^x,b\gets e^y$，得：

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\dfrac{e\^x-e\^y}{x-y}\<\dfrac{e\^x+e\^y}{2}}\tag h
:::

$$\boxed{\dfrac{e^x-e^y}{x-y}<\dfrac{e^x+e^y}{2}}\tag h$$
::::

另外，还可以用韦达定理中的 []{.arithmatex}$x_2+x_2=-\dfrac{b}{a}$ 或 []{.arithmatex}$x_1x_2=\dfrac{c}{a}$ 关系将双变量问题转化为单变量问题。

另外，还有推导：

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\ln\^2(x+1)\<\dfrac{x\^2}{x+1},\quad x\>0}
:::

$$\boxed{\ln^2(x+1)<\dfrac{x^2}{x+1},\quad x>0}$$
::::

二元不等式的证明中，更加常用到齐次化的策略，常见的有：

:::: {.arithmatex}
::: {.MathJax_Preview}
e\^{x_1+x_2}=e\^{x_1}e\^{x_2}
:::

$$e^{x_1+x_2}=e^{x_1}e^{x_2}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
e\^{x_1-x_2}=\dfrac{e\^{x_1}}{e\^{x_2}}
:::

$$e^{x_1-x_2}=\dfrac{e^{x_1}}{e^{x_2}}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln(x_1x_2)=\ln x_1+\ln x_2
:::

$$\ln(x_1x_2)=\ln x_1+\ln x_2$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln\dfrac{x_1}{x_2}=\ln x_1-\ln x_2
:::

$$\ln\dfrac{x_1}{x_2}=\ln x_1-\ln x_2$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\sin\^2x+\cos\^2x=0
:::

$$\sin^2x+\cos^2x=0$$
::::

### 数字不等式 {#_7}

常用方法：

- 构造函数。

- 对于有指数的，取对数。

将 []{.arithmatex}$e^3,3^e,e^\pi,\pi^e,3^\pi,\pi^3$ 按照从小到大都顺序排列。

构造函数：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)=\dfrac{\ln x}{x}
:::

$$f(x)=\dfrac{\ln x}{x}$$
::::

求导得出

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x)=\dfrac{1-\ln x}{x\^2}
:::

$$f'(x)=\dfrac{1-\ln x}{x^2}$$
::::

容易知道在 []{.arithmatex}$[e,+\infty)$ 上 []{.arithmatex}$f(x)$ 是单调递减的。

我们知道：

:::: {.arithmatex}
::: {.MathJax_Preview}
e\<3\<\pi
:::

$$e<3<\pi$$
::::

因此

:::: {.arithmatex}
::: {.MathJax_Preview}
\dfrac{\ln\pi}{\pi}\<\dfrac{\ln3}{3}\<\dfrac{\ln e}{e}
:::

$$\dfrac{\ln\pi}{\pi}<\dfrac{\ln3}{3}<\dfrac{\ln e}{e}$$
::::

可以得到三组不等式

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} \pi\^3&\<3\^\pi\\ \pi\^e&\<e\^\pi\\ 3\^e&\<e\^3 \end{cases}
:::

$$\begin{cases}
\pi^3&<3^\pi\\
\pi^e&<e^\pi\\
3^e&<e^3
\end{cases}$$
::::

现在我们可以得到下面的（用括号表示两个暂不知道大小关系）

:::: {.arithmatex}
::: {.MathJax_Preview}
3\^e\<(\pi\^e,e\^3)\<(\pi\^3,e\^\pi)\<3\^\pi
:::

$$3^e<(\pi^e,e^3)<(\pi^3,e^\pi)<3^\pi$$
::::

证法一：当 []{.arithmatex}$x>0$ 且 []{.arithmatex}$x\neq1$ 时，有不等式

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln x\>1-\frac{1}{x}
:::

$$\ln x>1-\frac{1}{x}$$
::::

从而：

:::: {.arithmatex}
::: {.MathJax_Preview}
\pi-3\ln\pi=\pi-3\ln\frac{\pi}{e}-3\<\pi-3\left(1-\frac{e}{\pi}\right)-3=\frac{\pi\^2-6\pi+3e}{\pi}\<0
:::

$$\pi-3\ln\pi=\pi-3\ln\frac{\pi}{e}-3<\pi-3\left(1-\frac{e}{\pi}\right)-3=\frac{\pi^2-6\pi+3e}{\pi}<0$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
3-e\ln\pi=3-e\ln\frac{\pi}{e}-e\<3-e\left(1-\frac{e}{\pi}\right)-e=\frac{3\pi-2e\pi+e\^2}{\pi}\<0
:::

$$3-e\ln\pi=3-e\ln\frac{\pi}{e}-e<3-e\left(1-\frac{e}{\pi}\right)-e=\frac{3\pi-2e\pi+e^2}{\pi}<0$$
::::

证法二：当 []{.arithmatex}$0<x<e$ 时，有不等式

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln x\<\frac{x}{e}
:::

$$\ln x<\frac{x}{e}$$
::::

从而：

:::: {.arithmatex}
::: {.MathJax_Preview}
\pi-3\ln\pi=\pi+3\ln\frac{e\^2}{\pi}-6\<\pi+\frac{3e}{\pi}-6=\frac{\pi\^2+3e-6\pi}{\pi}\<0
:::

$$\pi-3\ln\pi=\pi+3\ln\frac{e^2}{\pi}-6<\pi+\frac{3e}{\pi}-6=\frac{\pi^2+3e-6\pi}{\pi}<0$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
3-e\ln\pi=3+e\ln\frac{e\^2}{\pi}-2e\<3+\frac{e\^2}{\pi}-2e=\frac{3\pi-2e\pi+e\^2}{\pi}\<0
:::

$$3-e\ln\pi=3+e\ln\frac{e^2}{\pi}-2e<3+\frac{e^2}{\pi}-2e=\frac{3\pi-2e\pi+e^2}{\pi}<0$$
::::

证明：

:::: {.arithmatex}
::: {.MathJax_Preview}
\left(\frac{6}{5}\right)\^{\sqrt{3}}\>\left(\frac{5}{4}\right)\^{\sqrt{2}}
:::

$$\left(\frac{6}{5}\right)^{\sqrt{3}}>\left(\frac{5}{4}\right)^{\sqrt{2}}$$
::::

我们两边取对数，构造函数

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)=\frac{\sqrt{x}\ln x}{x-1},x\>1
:::

$$f(x)=\frac{\sqrt{x}\ln x}{x-1},x>1$$
::::

去导数，计算可能有一点复杂：

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x)=\frac{x+1}{2\sqrt{x}(x-1)\^2}\cdot\left\[\frac{2(x-1)}{x+1}-\ln x\right\]\<0
:::

$$f'(x)=\frac{x+1}{2\sqrt{x}(x-1)^2}\cdot\left[\frac{2(x-1)}{x+1}-\ln x\right]<0$$
::::

故 []{.arithmatex}$f(x)$ 单调递减，因此有

:::: {.arithmatex}
::: {.MathJax_Preview}
f\left(\frac{6}{5}\right)\>f\left(\frac{5}{4}\right)
:::

$$f\left(\frac{6}{5}\right)>f\left(\frac{5}{4}\right)$$
::::

得证。

## 恒成立问题 {#_8}

### 函数模型 {#_9}

简单的恒成立问题：

- []{.arithmatex}$f(x)\ge0$ 在定义域内恒成立 []{.arithmatex}$\iff f(x)_{\min}\ge0$。

- []{.arithmatex}$f(x)\le0$ 在定义域内恒成立 []{.arithmatex}$\iff f(x)_{\max}\le0$。

对于任何单调函数，最值必在端点处取到：

- 单调函数 []{.arithmatex}$f(x)\ge0$ 在 []{.arithmatex}$[x_1,x_2]$ 上恒成立等价于 []{.arithmatex}$\begin{cases}f(x_1)&\ge0\\ f(x_2)&\ge0\end{cases}$。

- 单调函数 []{.arithmatex}$f(x)\le0$ 在 []{.arithmatex}$[x_1,x_2]$ 上恒成立等价于 []{.arithmatex}$\begin{cases}f(x_1)&\le0\\ f(x_2)&\le0\end{cases}$。

对任何一个函数 []{.arithmatex}$f(x)$，若它在区间上是先减后增，则其最大值必在端点处取得，同理可得若函数在区间上先增后减，其最小值必在区间端点处取得：

- 若 []{.arithmatex}$a > 0$，则 []{.arithmatex}$f(x) = ax^2 + bx + c \le 0$ 在 []{.arithmatex}$[x_1, x_2]$ 上恒成立等价于 []{.arithmatex}$\begin{cases}f(x_1)&\le0\\ f(x_2)&\le0\end{cases}$。

- 若 []{.arithmatex}$a < 0$，则 []{.arithmatex}$f(x) = ax^2 + bx + c \ge 0$ 在 []{.arithmatex}$[x_1, x_2]$ 上恒成立等价于 []{.arithmatex}$\begin{cases}f(x_1)&\ge0\\ f(x_2)&\ge0\end{cases}$。

二次函数恒正、恒负的等价条件：

1.  对一切实数 []{.arithmatex}$x$，[]{.arithmatex}$ax^2 + bx + c \ge 0$ 恒成立的条件是：

    :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \begin{cases} a &\> 0 \\ \Delta &\le 0 \end{cases}
    :::

    $$\begin{cases}
    a &> 0 \\
    \Delta &\le 0
    \end{cases}$$
    ::::

2.  对一切实数 []{.arithmatex}$x$，[]{.arithmatex}$ax^2 + bx + c \le 0$ 恒成立的条件是：

    :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \begin{cases} a &\< 0 \\ \Delta &\le 0 \end{cases}
    :::

    $$\begin{cases}
    a &< 0 \\
    \Delta &\le 0
    \end{cases}$$
    ::::

绝对值函数：

- 函数 []{.arithmatex}$f(x)=|ax+b|$ 在 []{.arithmatex}$[x_1,x_2]$ 上的最大值必在端点处取到。

- 对于内部不是一次函数的，可以设处二次函数为 []{.arithmatex}$u$，利用换元法解决，例如：

  已知 []{.arithmatex}$t$ 为常数，函数 []{.arithmatex}$y=|x^2-2x-t|$ 在区间 []{.arithmatex}$[0,3]$ 上的最大值为 []{.arithmatex}$2$，则 []{.arithmatex}$t=$？

  令 []{.arithmatex}$u=x^2-2x\in[-1,3]$，则问题转化为求 []{.arithmatex}$t$ 大取值范围使得 []{.arithmatex}$|u-t|$ 在 []{.arithmatex}$[-1,3]$ 上的最大值为 []{.arithmatex}$2$。

  若最大值在 []{.arithmatex}$u=-1$ 取到，解得 []{.arithmatex}$t=1$；若最大值在 []{.arithmatex}$u=3$ 取到，解得 []{.arithmatex}$t=1$。故 []{.arithmatex}$t=1$。

### 共零点法 {#_10}

对于含参恒成立问题

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)g(x)\ge0
:::

$$f(x)g(x)\ge0$$
::::

容易知道，我们只需要让两个函数处处异号（或为零）即可。

首先验证当 []{.arithmatex}$x$ 趋近于正负无穷是否满足，然后就可以令 []{.arithmatex}$f,g$ 零点重合即可。

### 参变分离法 {#_11}

参变分离，即为将参数和变量分开，使不等式一边只有参数，另一边只含有变量，可以进行参变分离的一定是显式的。

**例题**：已知 []{.arithmatex}$y = xe^x + x^2 + 2x + a$ 恰有两个不同的零点，则 []{.arithmatex}$a$ 的取值范围为。

**答案**：由题意方程 []{.arithmatex}$xe^x + x^2 + 2x + a = 0$ 有两个不同的实根，分离参数 []{.arithmatex}$-a = xe^x + x^2 + 2x$。令 []{.arithmatex}$f(x) = xe^x + x^2 + 2x$，则函数 []{.arithmatex}$f(x)$ 的定义域为 []{.arithmatex}$\mathbb{R}$，求导

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x) = (x+1)(e\^x + 2)
:::

$$f'(x) = (x+1)(e^x + 2)$$
::::

当 []{.arithmatex}$x < -1$ 时，[]{.arithmatex}$f'(x) < 0$，[]{.arithmatex}$f(x)$ 单调递减；当 []{.arithmatex}$x > -1$ 时，[]{.arithmatex}$f'(x) > 0$，[]{.arithmatex}$f(x)$ 单调递增，所以函数 []{.arithmatex}$f(x)$ 在 []{.arithmatex}$x = -1$ 处取得极小值：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(-1) = -\dfrac{1}{e} - 1
:::

$$f(-1) = -\dfrac{1}{e} - 1$$
::::

从而作出函数 []{.arithmatex}$f(x)$ 的图像，则 []{.arithmatex}$-a > -\dfrac{1}{e} - 1$ 时，函数 []{.arithmatex}$y = f(x)$ 的图像与直线 []{.arithmatex}$y = -a$ 有两个交点，所以

:::: {.arithmatex}
::: {.MathJax_Preview}
a \< \dfrac{1}{e} + 1
:::

$$a < \dfrac{1}{e} + 1$$
::::

**例题**：已知函数 []{.arithmatex}$f(x) = x(\ln x - ax)$ 有两个极值点，则实数 []{.arithmatex}$a$ 的取值范围为。

**答案**：函数 []{.arithmatex}$f(x)$ 的定义域为 []{.arithmatex}$x > 0$，由题意 []{.arithmatex}$f'(x) = \ln x - 2ax + 1$ 有两个零点，分离参数

:::: {.arithmatex}
::: {.MathJax_Preview}
2a = \dfrac{\ln x + 1}{x}=g(x)
:::

$$2a = \dfrac{\ln x + 1}{x}=g(x)$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
g\'(x) = \dfrac{1 - \ln x - 1}{x\^2} = \dfrac{-\ln x}{x\^2}
:::

$$g'(x) = \dfrac{1 - \ln x - 1}{x^2} = \dfrac{-\ln x}{x^2}$$
::::

当 []{.arithmatex}$0 < x < 1$ 时，[]{.arithmatex}$g'(x) > 0$，[]{.arithmatex}$g(x)$ 单调递增；当 []{.arithmatex}$x > 1$ 时，[]{.arithmatex}$g'(x) < 0$，[]{.arithmatex}$g(x)$ 单调递减，所以函数 []{.arithmatex}$g(x)$ 在 []{.arithmatex}$x = 1$ 处取得极大值 []{.arithmatex}$g(1) = 1$。

当 []{.arithmatex}$x \to +\infty$ 时，[]{.arithmatex}$g(x) \to 0$；当 []{.arithmatex}$x \to 0$ 时，[]{.arithmatex}$g(x) \to -\infty$。当 []{.arithmatex}$0 < 2a < 1$，即 []{.arithmatex}$0 < a < \dfrac{1}{2}$ 时，直线 []{.arithmatex}$y = 2a$ 与 []{.arithmatex}$y = g(x)$ 的图像有两个交点。

我们这一节的内容是恒成立问题，参变分离解决恒成立问题通常更加简单，直接把参数挪到一边，然后对另一边应用函数模型即可。

解决这类问题的方法分为三种，带着参数讨论、参变分离和半分参，下面讲解一下半分参。半分参的技巧性比较强，下面只介绍几种最经典的。

::::: {.admonition .note}
例题

若 []{.arithmatex}$f(x) = e^x - ax + 2a > 0$ 恒成立，求 []{.arithmatex}$a$ 的取值范围。

我们进行化简：

:::: {.arithmatex}
::: {.MathJax_Preview}
e\^x \> a(x-2)
:::

$$e^x > a(x-2)$$
::::

我们发现此时如果进行参变分离，就要讨论 []{.arithmatex}$x-2$ 的符号，我们知道我们应当避免讨论自变量的符号，而应当讨论参数的符号（因为这也能帮我们确定参数的取值范围）。

![alt text](../desmos-graph%20%283%29.svg){width="50%"}

因此我们令 []{.arithmatex}$g(x)=e^x$，[]{.arithmatex}$h(x)=a(x-2)$。

- 当 []{.arithmatex}$a<0$ 时，[]{.arithmatex}$g(x)>h(x)$ 不恒成立。

- 当 []{.arithmatex}$a=0$ 时 []{.arithmatex}$e^x>0$ 恒成立。

- 当 []{.arithmatex}$a>0$ 时：设 []{.arithmatex}$g(x)$ 与 []{.arithmatex}$h(x)$ 相切于点 []{.arithmatex}$(x_0,e^{x_0})$，此时直线 []{.arithmatex}$h(x)$ 的斜率 []{.arithmatex}$a_0$ 就应当等于曲线在该点的切线斜率

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  a_0=e\^{x_0}
  :::

  $$a_0=e^{x_0}$$
  ::::

  根据斜率，写出：

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  \dfrac{e\^{x_0}}{x_0-2}=e\^{x_0}
  :::

  $$\dfrac{e^{x_0}}{x_0-2}=e^{x_0}$$
  ::::

  解得 []{.arithmatex}$x_0=3$，则 []{.arithmatex}$a_0=e^{x_0}=e^3$。

综上，[]{.arithmatex}$a\in [0, e^3)$。
:::::

在半分参中，通常是一条直线和一条曲线，除非两条曲线是非常经典且简单的形式，这也可以用于预判是否可以使用半分参。

### 简单变形法 {#_12}

复杂的恒成立问题，优先考虑求导数的零点，如果很难求解，则通过下面两个方法：

- 与指数相关的恒成立问题，如果很难求导数的零点，则优先考虑将函数变形为 []{.arithmatex}$e^xf(x)$ 或 []{.arithmatex}$e^{-x}f(x)$ 的形式。

- 与对数相关的恒成立问题，如果很难求导数的零点，则优先考虑将函数变形为 []{.arithmatex}$f(x) + \ln g(x)$ 的形式。其思想精髓是将对数与其他函数分离，达到求导后可以摆脱对数的干扰。除了 []{.arithmatex}$f(x) + \ln g(x)$ 这种形式外，还有一种形式，求导后可以"甩掉"对数。

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  f(x)(\ln f(x) + C)
  :::

  $$f(x)(\ln f(x) + C)$$
  ::::

  求导后的结果是：

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  f\'(x)(\ln f(x) + C + 1)，
  :::

  $$f'(x)(\ln f(x) + C + 1)，$$
  ::::

  其中 []{.arithmatex}$C$ 为常数。显然其导数的零点与对数函数也无关。

  因此，与对数函数相关的函数题中，首先考虑将函数变形为 []{.arithmatex}$f(x) + \ln g(x)$ 或 []{.arithmatex}$f(x)(\ln f(x) + C)$ 的形式。

- 不要一看到指数函数就想变形，因为某些与指数函数相关的问题就不需要变形也能求其极值点。

- 如果问题是让你求函数 []{.arithmatex}$f(x)$ 的最值、极值或者单调性之类的，则无论如何也**不能变形**，因为这会导致**变形后的问题与原问题不等价**。

例如如果要求

:::: {.arithmatex}
::: {.MathJax_Preview}
e\^x+ax\^2-x\ge\dfrac{1}{2}x\^3+1
:::

$$e^x+ax^2-x\ge\dfrac{1}{2}x^3+1$$
::::

在 []{.arithmatex}$x\ge0$ 恒成立，不妨移项得到

:::: {.arithmatex}
::: {.MathJax_Preview}
e\^x\ge\dfrac{1}{2}x\^3-ax\^2+x+1
:::

$$e^x\ge\dfrac{1}{2}x^3-ax^2+x+1$$
::::

再把 []{.arithmatex}$e^x$ 除过去，得到

:::: {.arithmatex}
::: {.MathJax_Preview}
\left\\\dfrac{\dfrac{1}{2}x\^3-ax\^2+x+1}{e\^x}\right\\\_{\max}\le1
:::

$$\left\{\dfrac{\dfrac{1}{2}x^3-ax^2+x+1}{e^x}\right\}_{\max}\le1$$
::::

恒成立，再用端点效应必要性探路即可解决。

### 必要性探路 {#_13}

一种解题方法，可应用于一类带参数的恒成立问题。求参数范围时，从满足题意的自变量范围内选择一个数，代入求得一个参数范围，此时这个范围是题意的必要条件。之后再设法证明该必要条件也是题意的充分条件，或者讨论别的点。若充分性也成立，则该范围是题意的充要条件，即为所求的范围。这种方法需从逻辑条件上进行理解，因为先得到的是必要条件，故称为必要探路法。

最常见的必要性探路为端点效应：我们把通过端点来缩小参数取值范围的方法称为端点效应，其思想是通过端点来缩小参数的取值范围。注意，端点效应只是缩小参数的取值范围，也就是说该范围只是恒成立的---个必要条件，而非充分条件。

利用端点效应解题的基本步骤如下：

1.  首先由端点效应初步获得参数的取值范围，这个范围是必要的。
2.  然后利用这个范围来判断函数是否单调。
3.  如果函数单调，则由端点得到的范围就是最终答案；如果函数不单调，则再利用端点确定的范围进一步确定函数的最值。

具体的：

1.  若 []{.arithmatex}$f(x) \ge 0$ 在 []{.arithmatex}$[a, b]$ 上恒成立，则由端点效应可知 []{.arithmatex}$\begin{cases}f(a) \ge 0\\ f(b) \ge 0\end{cases}$。

2.  若 []{.arithmatex}$f(x) > 0$ 在 []{.arithmatex}$[a, b]$ 上恒成立，则由端点效应可知 []{.arithmatex}$\begin{cases}f(a) > 0\\ f(b) > 0\end{cases}$。

3.  若 []{.arithmatex}$f(x) \ge 0$ 在 []{.arithmatex}$(a, b)$ 上恒成立，则由端点效应可知 []{.arithmatex}$\begin{cases}f(a) \ge 0\\ f(b) \ge 0\end{cases}$。

4.  若 []{.arithmatex}$f(x) > 0$ 在 []{.arithmatex}$(a, b)$ 上恒成立，则由端点效应可知 []{.arithmatex}$\begin{cases}f(a) \ge 0\\ f(b) \ge 0\end{cases}$。

若函数 []{.arithmatex}$f(x)g(x) \ge 0$ 在 []{.arithmatex}$(a, b)$ 上恒成立，则：

- 若 []{.arithmatex}$f(x)$ 在 []{.arithmatex}$(a, b)$ 恒正（恒负），则 []{.arithmatex}$g(x)$ 在 []{.arithmatex}$(a, b)$ 也恒正（恒负）；

- 若 []{.arithmatex}$\alpha$ 是 []{.arithmatex}$f(x)$ 的变号零点，则 []{.arithmatex}$\alpha$ 也是 []{.arithmatex}$g(x)$ 的变号零点。

已知 []{.arithmatex}$f(x) \ge 0$ 在 []{.arithmatex}$[a, b]$（或 []{.arithmatex}$(a, b)$）上恒成立：

- 若 []{.arithmatex}$f(a) = 0$，则 []{.arithmatex}$f'(a) \ge 0$；

- 若 []{.arithmatex}$f(b) = 0$，则 []{.arithmatex}$f'(b) \le 0$。

如果导数为零，我们求二阶导：

- []{.arithmatex}$f(x) \ge 0$ 在 []{.arithmatex}$[a, b]$ 上恒成立，若 []{.arithmatex}$f(a) = 0$，[]{.arithmatex}$f'(a) = 0$，则 []{.arithmatex}$f''(a) \ge 0$；若 []{.arithmatex}$f(b) = 0$，[]{.arithmatex}$f'(b) = 0$，则 []{.arithmatex}$f''(b) \le 0$。

- []{.arithmatex}$f(x) \ge 0$ 在 []{.arithmatex}$[a, b]$ 上恒成立，若 []{.arithmatex}$f(a) = 0$ 且 []{.arithmatex}$f'(x) = g(x)h(x)$，其中 []{.arithmatex}$g(x) \ge 0$，则 []{.arithmatex}$h(a) \ge 0$。

对于一小部分题目，可以直接观察使用端点效应等必要性探路，然后直接尝试证明充分性，可能直接证明。

### 隐零点问题 {#_14}

考虑不等式组

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} f\'(x_0) &= 0 &&①\\ f(x_0) &\ge 0 &&②\end{cases}
:::

$$\begin{cases} f'(x_0) &= 0 &&①\\ f(x_0) &\ge 0 &&②\end{cases}$$
::::

其中 []{.arithmatex}$f'(x_0)$ 和 []{.arithmatex}$f(x_0)$ 均含有参数 []{.arithmatex}$a$。

有两种方式处理上面不等式组：

1.  **若①中的参数 []{.arithmatex}**$a$ 和 []{.arithmatex}$x_0$ 容易分离：

    - 首先在①中用零点 []{.arithmatex}$x_0$ 表示参数 []{.arithmatex}$a$。
    - 然后代入②来确定零点 []{.arithmatex}$x_0$ 的取值范围。
    - 最后利用获得的零点 []{.arithmatex}$x_0$ 的范围和①确定参数 []{.arithmatex}$a$ 的取值范围。
    - 既适合已知恒成立求参数范围的问题，也适用于不等式的证明。

2.  **若①不容易分离参数 []{.arithmatex}**$a$ 和 []{.arithmatex}$x_0$，或分离后结构复杂：

    - 首先猜测方程组 []{.arithmatex}$\begin{cases} f'(x_0) = 0 \\ f(x_0) = 0 \end{cases}$ 的解 []{.arithmatex}$x_0$。
    - 然后由 []{.arithmatex}$f(x_0) \ge 0$ 和端点效应解出 []{.arithmatex}$a$ 的取值范围（该范围为最终的答案）。
    - 最后证明在该范围下 []{.arithmatex}$f(x) \ge 0$ 恒成立。
    - 注意这个只适合已知恒成立求参数范围的问题，不适于不等式的证明。

通常来说，我们设 []{.arithmatex}$x_0$ 为函数的零点，列出 []{.arithmatex}$f(x_0)=0$ 和要求的条件，组成方程组解方程即可。

如果函数的导数非常复杂，则考虑变换主元法：

1.  首先由端点效应初步获得参数的取值范围，验证这个范围是否为最终范围；若不是，则判断函数的极值并获取参数的取值范围；

2.  根据主元函数的形式，判断主元函数的单调性，然后求主元函数的最值（此最值应当是一个函数），最后判断该最值函数是否满足题中的不等式。

## 不等式方法 {#_15}

### 一般放缩法 {#_16}

首先放缩的依据见简单不等式中的三个不等式，以及四个推导不等式。

若问题没有任何第（I）问的提示且函数为指数、对数和其他幂函数的混合型，则把指数与对数分开，再平衡幂函数和指数与对数函数，使得不等式两边一边是指数，另外一边是对数，然后分别计算它们的最值。这种方法一般只适合不等式的证明！

函数不等式中含有 []{.arithmatex}$xe^x$ 与 []{.arithmatex}$\frac{e^x}{x}$ 这类固定搭配，则考虑放缩如下：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} xe\^x &= e\^{x+\ln x} &&\ge x + \ln x + 1\\ \frac{e\^x}{x} &= e\^{x-\ln x} &&\ge x - \ln x + 1 \end{aligned}
:::

$$\begin{aligned}
xe^x &= e^{x+\ln x} &&\ge x + \ln x + 1\\
\frac{e^x}{x} &= e^{x-\ln x} &&\ge x - \ln x + 1
\end{aligned}$$
::::

### 整体代换法 {#_17}

一部分导数题形式为第一问要求证明一个不等式，而在第二问就可以用这个不等式，通过整体代换的形式进行解决。

例题：证明 []{.arithmatex}$\dfrac{e^x}{x^2}-x\ge1-2\ln x$。

问题显然为：

:::: {.arithmatex}
::: {.MathJax_Preview}
\dfrac{e\^x}{x\^2}\ge\ln\dfrac{e\^x}{x\^2}+1
:::

$$\dfrac{e^x}{x^2}\ge\ln\dfrac{e^x}{x^2}+1$$
::::

根据 []{.arithmatex}$x\ge\ln x-1$，不等式显然。

### 同构化构造 {#_18}

简单的同构化，例如 []{.arithmatex}$\sqrt{11}-\sqrt{10}$ 与 []{.arithmatex}$\sqrt{12}-\sqrt{11}$ 比大小，构造同构化函数 []{.arithmatex}$f(x)=\sqrt{x}-\sqrt{x-1}$，求导解决。

::::::: {.admonition .note}
例题

当 []{.arithmatex}$m > n > 0$ 时，证明：[]{.arithmatex}$me^n + n < ne^m + m$。

要证 []{.arithmatex}$me^n + n < ne^m + m$，即证

:::: {.arithmatex}
::: {.MathJax_Preview}
\dfrac{me\^n}{mn} + \dfrac{n}{mn} \< \dfrac{ne\^m}{mn} + \dfrac{m}{mn}
:::

$$\dfrac{me^n}{mn} + \dfrac{n}{mn} < \dfrac{ne^m}{mn} + \dfrac{m}{mn}$$
::::

即

:::: {.arithmatex}
::: {.MathJax_Preview}
\dfrac{e\^n}{n} - \dfrac{1}{n} \< \dfrac{e\^m}{m} - \dfrac{1}{m}
:::

$$\dfrac{e^n}{n} - \dfrac{1}{n} < \dfrac{e^m}{m} - \dfrac{1}{m}$$
::::

此不等式两边的结构形式一致，构造 []{.arithmatex}$f(x) = \dfrac{e^x}{x} - \dfrac{1}{x}$，只需证明 []{.arithmatex}$f(x)$ 在 []{.arithmatex}$(0, +\infty)$ 上单调递增即可。
:::::::

最常见的一种形式是：

:::: {.arithmatex}
::: {.MathJax_Preview}
yf(x)=xf(y)
:::

$$yf(x)=xf(y)$$
::::

整理得到：

:::: {.arithmatex}
::: {.MathJax_Preview}
\dfrac{f(x)}{x}\>\dfrac{f(y)}{y}
:::

$$\dfrac{f(x)}{x}>\dfrac{f(y)}{y}$$
::::

其中 []{.arithmatex}$y$ 为关于 []{.arithmatex}$x$ 的函数。

以 []{.arithmatex}$f(x) = xe^x - x - \ln x$ 的最小值为例，对其变形

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)=e\^{x+\ln x}-(x+\ln x)=e\^t-t
:::

$$f(x)=e^{x+\ln x}-(x+\ln x)=e^t-t$$
::::

又或者，

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)=xe\^x-\ln(xe\^x)
:::

$$f(x)=xe^x-\ln(xe^x)$$
::::

分别设 []{.arithmatex}$t=x+\ln x$ 和 []{.arithmatex}$t=xe^x$，即可。

### 积分构造法 {#_19}

我们知道一个经典的不等式

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln x\le x-1
:::

$$\ln x\le x-1$$
::::

当且仅当 []{.arithmatex}$x=1$ 时取等，我们对两边同时求积分，如图左。为了使两边依旧在 []{.arithmatex}$x=1$ 时取等，我们将 []{.arithmatex}$\ln x$ 的积分 []{.arithmatex}$(\ln x-1)x$ 修正为其加 []{.arithmatex}$\dfrac{1}{2}$，如图右

::: {.grid}
![alt text](../desmos-graph%20%282%29.svg)

![alt text](../desmos-graph.svg)
:::

利用求导也可以证明下面的不等式：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} 0\<x\le1&\ln x\ge\dfrac{1}{2}\left(x-\dfrac{1}{x}\right)\\ x\>1&\ln x\<\dfrac{1}{2}\left(x-\dfrac{1}{x}\right) \end{cases}
:::

$$\begin{cases}
0<x\le1&\ln x\ge\dfrac{1}{2}\left(x-\dfrac{1}{x}\right)\\
x>1&\ln x<\dfrac{1}{2}\left(x-\dfrac{1}{x}\right)
\end{cases}$$
::::

类似的，继续求积分，我们还可以得到下面的不等式：

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln x\le\dfrac{(x+5)(x-1)}{4x+2}
:::

$$\ln x\le\dfrac{(x+5)(x-1)}{4x+2}$$
::::

类似的，我们对经典的不等式

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln x\ge1-\dfrac{1}{x}
:::

$$\ln x\ge1-\dfrac{1}{x}$$
::::

进行类似的积分构造。可以得到

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} 0\<x\le1&\ln x\le\dfrac{2(x-1)}{x+1}\\ x\>1&\ln x\ge\dfrac{2(x-1)}{x+1} \end{cases}
:::

$$\begin{cases}
0<x\le1&\ln x\le\dfrac{2(x-1)}{x+1}\\
x>1&\ln x\ge\dfrac{2(x-1)}{x+1}
\end{cases}$$
::::

### 替换构造法 {#_20}

我们对

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} 0\<x\le1&\ln x\ge\dfrac{1}{2}\left(x-\dfrac{1}{x}\right)\\ x\>1&\ln x\<\dfrac{1}{2}\left(x-\dfrac{1}{x}\right) \end{cases}
:::

$$\begin{cases}
0<x\le1&\ln x\ge\dfrac{1}{2}\left(x-\dfrac{1}{x}\right)\\
x>1&\ln x<\dfrac{1}{2}\left(x-\dfrac{1}{x}\right)
\end{cases}$$
::::

令 []{.arithmatex}$x\gets e^x$，则有

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} x\le0& e\^x-e\^{-x}\le2x\\ x\>0& e\^x-e\^{-x}\>2x \end{cases}
:::

$$\begin{cases}
x\le0& e^x-e^{-x}\le2x\\
x>0& e^x-e^{-x}>2x
\end{cases}$$
::::

类似的，我们对

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} 0\<x\le1&\ln x\le\dfrac{2(x-1)}{x+1}\\ x\>1&\ln x\ge\dfrac{2(x-1)}{x+1} \end{cases}
:::

$$\begin{cases}
0<x\le1&\ln x\le\dfrac{2(x-1)}{x+1}\\
x>1&\ln x\ge\dfrac{2(x-1)}{x+1}
\end{cases}$$
::::

令 []{.arithmatex}$x\gets e^x$，则有

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} x\le0&(2-x)e\^x\ge2+x\\ x\>0&(2-x)e\^x\<2+x \end{cases}
:::

$$\begin{cases}
x\le0&(2-x)e^x\ge2+x\\
x>0&(2-x)e^x<2+x
\end{cases}$$
::::

### 局部求值法 {#_21}

证明函数最值大于或小于一个数，可以将函数拆为几个易于求值的部分，对每一个部分分别运算，在整体上，这个最值不一定取得到，但是也可以证出结果（要证明的不等式不一定很严格）。

例题：证明

:::: {.arithmatex}
::: {.MathJax_Preview}
\dfrac{e\^x}{x}-\dfrac{8}{x\^2}\ln\dfrac{2}{x}+x\>e+2
:::

$$\dfrac{e^x}{x}-\dfrac{8}{x^2}\ln\dfrac{2}{x}+x>e+2$$
::::

设

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)=\dfrac{e\^x}{x}
:::

$$f(x)=\dfrac{e^x}{x}$$
::::

则

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x)=e\^x\dfrac{x-1}{x\^2}
:::

$$f'(x)=e^x\dfrac{x-1}{x^2}$$
::::

因此

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)\ge f(1)=e
:::

$$f(x)\ge f(1)=e$$
::::

设

:::: {.arithmatex}
::: {.MathJax_Preview}
g(x)=x-\dfrac{8}{x\^2}\ln\dfrac{2}{x}
:::

$$g(x)=x-\dfrac{8}{x^2}\ln\dfrac{2}{x}$$
::::

则

:::: {.arithmatex}
::: {.MathJax_Preview}
g\'(x)=1-\dfrac{16\ln\dfrac{x}{2}-8}{x\^3}
:::

$$g'(x)=1-\dfrac{16\ln\dfrac{x}{2}-8}{x^3}$$
::::

易知 []{.arithmatex}$g'(x)$ 单调递增且 []{.arithmatex}$g'(2)=0$，因此：

:::: {.arithmatex}
::: {.MathJax_Preview}
g(x)\ge g(2)=2
:::

$$g(x)\ge g(2)=2$$
::::

所以

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)+g(x)\>e+2
:::

$$f(x)+g(x)>e+2$$
::::

不取等号因为局部不等式不同时取等。

### 隐零点方法 {#_22}

在前文隐零点我们说过，如果可以简单的分离、带入，那么容易解决，但是有的时候不能这么解决，此时问题就麻烦一点，我们以例题：已知 []{.arithmatex}$f(x)=e^x-\ln(x+2)$，求证 []{.arithmatex}$f(x)>\dfrac{1}{6}$ 恒成立。

容易想到，我们对 []{.arithmatex}$f(x)$ 求导

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x)=e\^x-\dfrac{1}{x+2}
:::

$$f'(x)=e^x-\dfrac{1}{x+2}$$
::::

容易知道函数先单调递减，再单调递增，[]{.arithmatex}$f'(x_0)=0$ 容易得到

:::: {.arithmatex}
::: {.MathJax_Preview}
e\^{x_0}=\dfrac{1}{x_0+2}
:::

$$e^{x_0}=\dfrac{1}{x_0+2}$$
::::

那么就有

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x_0)=e\^{x_0}-\ln(x_0+2)=\dfrac{1}{x_0+2}+x_0
:::

$$f(x_0)=e^{x_0}-\ln(x_0+2)=\dfrac{1}{x_0+2}+x_0$$
::::

根据零点存在性定理，我们可以知道 []{.arithmatex}$f'(x)$ 的零点应该在 []{.arithmatex}$(-1,0)$。

不妨令

:::: {.arithmatex}
::: {.MathJax_Preview}
g(x)=\dfrac{1}{x+2}+x
:::

$$g(x)=\dfrac{1}{x+2}+x$$
::::

取等当且仅当 []{.arithmatex}$x=-1$，而 []{.arithmatex}$g(x)$ 在 []{.arithmatex}$(-1,0)$ 单调递增，不妨令

:::: {.arithmatex}
::: {.MathJax_Preview}
g(x_1)=\dfrac{1}{6}
:::

$$g(x_1)=\dfrac{1}{6}$$
::::

解得

:::: {.arithmatex}
::: {.MathJax_Preview}
x_1=\dfrac{1}{2}
:::

$$x_1=\dfrac{1}{2}$$
::::

此时有 []{.arithmatex}$f'(x_1)<0$，因此 []{.arithmatex}$x_0>x_1$

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x_0)\>f(x_1)=\dfrac{1}{6}
:::

$$f(x_0)>f(x_1)=\dfrac{1}{6}$$
::::

### 加强不等式 {#_23}

加强不等式是一种构造方法，我们使待证不等式加强，使加强后的不等式能够更易于变形或求值，最常见的是增添项，或者改变恒正负者系数，以约去不等式的部分项。

利用凹凸性割线放缩，是加强不等式的一种。

### 拉格朗日乘数法 {#_24}

对于一个函数 []{.arithmatex}$f(x,y)$ 在附加条件 []{.arithmatex}$\varphi(x,y)=0$ 下的极值，可以构造三元函数

:::: {.arithmatex}
::: {.MathJax_Preview}
L(x,y,\lambda)=f(x,y)+\lambda\varphi(x,y)
:::

$$L(x,y,\lambda)=f(x,y)+\lambda\varphi(x,y)$$
::::

求解下面这个方程组，代回原方程就是他的极值点

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} \dfrac{\partial L}{\partial x}&=0\\ \dfrac{\partial L}{\partial y}&=0\\ \varphi(x,y)&=0 \end{cases}
:::

$$\begin{cases}
\dfrac{\partial L}{\partial x}&=0\\
\dfrac{\partial L}{\partial y}&=0\\
\varphi(x,y)&=0
\end{cases}$$
::::

例题：已知 []{.arithmatex}$a,b,c$ 均为正实数，[]{.arithmatex}$a^2+b^2+4c^2=1$，则 []{.arithmatex}$ab+2ac+3\sqrt{2}bc$ 的最大值为？

:::: {.arithmatex}
::: {.MathJax_Preview}
\varphi(a,b,c)=a\^2+b\^2+4c\^2-1
:::

$$\varphi(a,b,c)=a^2+b^2+4c^2-1$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
f(a,b,c)=ab+2ac+3\sqrt{2}bc
:::

$$f(a,b,c)=ab+2ac+3\sqrt{2}bc$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
L(a,b,c,\lambda)=ab+2ac+3\sqrt{2}bc+\lambda(a\^2+b\^2+4c\^2-1)
:::

$$L(a,b,c,\lambda)=ab+2ac+3\sqrt{2}bc+\lambda(a^2+b^2+4c^2-1)$$
::::

求偏导，得

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{\partial L}{\partial a}=b+2c+2a\lambda=0
:::

$$\frac{\partial L}{\partial a}=b+2c+2a\lambda=0$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{\partial L}{\partial b}=a+3\sqrt{2}c+2b\lambda=0
:::

$$\frac{\partial L}{\partial b}=a+3\sqrt{2}c+2b\lambda=0$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{\partial L}{\partial c}=2a+3\sqrt{2}b+8c\lambda=0
:::

$$\frac{\partial L}{\partial c}=2a+3\sqrt{2}b+8c\lambda=0$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\varphi(a,b,c)=a\^2+b\^2+4c\^2-1=0
:::

$$\varphi(a,b,c)=a^2+b^2+4c^2-1=0$$
::::

联立解得

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} a&=\dfrac{\sqrt{2}}{\sqrt{10}}\\ b&=\dfrac{2}{\sqrt{10}}\\ c&=\dfrac{1}{\sqrt{10}}\\ \lambda&=-\sqrt{2} \end{cases}
:::

$$\begin{cases}
a&=\dfrac{\sqrt{2}}{\sqrt{10}}\\
b&=\dfrac{2}{\sqrt{10}}\\
c&=\dfrac{1}{\sqrt{10}}\\
\lambda&=-\sqrt{2}
\end{cases}$$
::::

代回得到

:::: {.arithmatex}
::: {.MathJax_Preview}
f\_{\max}=\sqrt{2}
:::

$$f_{\max}=\sqrt{2}$$
::::

## 极值点偏移 {#_25}

### 偏移概述 {#_26}

我们在证明形如 []{.arithmatex}$x_1+x_2>m$ 或 []{.arithmatex}$x_1x_2>m$ 的式子成立时，可以尝试将待证的不等式在形式上进行转化，转而证明转化后的不等式 []{.arithmatex}$x_1>m-x_2$ 或 []{.arithmatex}$x_1>\dfrac{m}{x_2}$ 成立，之后利用函数的单调性，转化为函数值之间的关系，即 []{.arithmatex}$f(x_1)$ 与 []{.arithmatex}$f(m-x_2)$ 或 []{.arithmatex}$f\left(\dfrac{m}{x_2}\right)$ 进行比较。

![alt text](../image-6.avif)

使用构造类对称法解此题时，首先要注意变量的取值范围，我们需要保证构造后不等号两边的变量取值在同一区间内，然后才能使用单调性进行证明。

对于极值点偏移问题，有的还可以直接用变双变量为单变量的方法，这其实就是二元不等式的思想。同时，也可以通过零点的相关性质，将不等式中的常数或者参数转化为与两个零点相关的式子。

有的时候，换元会导致式子变得次数非常复杂，此时应当直接设出函数；有的时候，不等式中参数过于复杂，此时应当用参数转换法；下面提供两种写步骤的方案。

在解决极值点偏移或者类极值点偏移的题目中，经常用到以下两个单变量的不等式链：

- 在 []{.arithmatex}$x\in(1,+\infty)$，

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  \small\frac{x-1}{x}\<\frac{2(x-1)}{x+1}\<\frac{3(x\^2-1)}{x\^2+4x+1}\<\ln x\<\sqrt{x}-\frac{1}{\sqrt{x}}\<\frac{1}{2}\left(x-\frac{1}{x}\right)\<x-1
  :::

  $$\small\frac{x-1}{x}<\frac{2(x-1)}{x+1}<\frac{3(x^2-1)}{x^2+4x+1}<\ln x<\sqrt{x}-\frac{1}{\sqrt{x}}<\frac{1}{2}\left(x-\frac{1}{x}\right)<x-1$$
  ::::

- 在 []{.arithmatex}$x\in(0,1)$，

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  \small\frac{x-1}{x}\<\frac{1}{2}\left(x-\frac{1}{x}\right)\<\sqrt{x}-\frac{1}{\sqrt{x}}\<\ln x\<\frac{3(x\^2-1)}{x\^2+4x+1}\<\frac{2(x-1)}{x+1}\<x-1
  :::

  $$\small\frac{x-1}{x}<\frac{1}{2}\left(x-\frac{1}{x}\right)<\sqrt{x}-\frac{1}{\sqrt{x}}<\ln x<\frac{3(x^2-1)}{x^2+4x+1}<\frac{2(x-1)}{x+1}<x-1$$
  ::::

对于一部分参数意义不明的题，可以采取分离参数的方法，把参数化没。

例题：函数 []{.arithmatex}$f(x)=x^2-2x+1+a e^x$。函数有两个极值点 []{.arithmatex}$x_1$、[]{.arithmatex}$x_2$，求证 []{.arithmatex}$x_1+x_2>4$。

求出导函数 []{.arithmatex}$f'(x)=2x-2+a e^x$，分离参数即 []{.arithmatex}$a=\dfrac{2-2x}{e^x}$ 有 []{.arithmatex}$2$ 解 []{.arithmatex}$x_1$、[]{.arithmatex}$x_2$。

也就是说 []{.arithmatex}$y=a$ 与 []{.arithmatex}$g=\dfrac{2-2x}{e^x}$ 有 []{.arithmatex}$2$ 交点 []{.arithmatex}$x_1$、[]{.arithmatex}$x_2$。

令 []{.arithmatex}$g(x)=\dfrac{2-2x}{e^x}$，则有 []{.arithmatex}$g(x_1)=g(x_2)=a$，这就是一个经典的极值点偏移问题。

其中等于 []{.arithmatex}$a$ 是因为我们将 []{.arithmatex}$a$ 减到 []{.arithmatex}$g(x)$ 里面是等价的，因此也可以分出来常数忽略。

### 对称和模型 {#_27}

模型形如证明 []{.arithmatex}$h(x_1,x_2)>C$，其中 []{.arithmatex}$x_1,x_2$ 可交换。

- 基础模型 []{.arithmatex}$h(x_1,x_2)=x_1+x_2$。有 []{.arithmatex}$f'(x)$ 在 []{.arithmatex}$(-\infty,C/2)$ 恒正（函数单调递增），在 []{.arithmatex}$(C/2,+\infty)$ 恒负（函数单调递减），且 []{.arithmatex}$f'(C/2)=0$（极大值点）。

  设 []{.arithmatex}$x_1,x_2$ 为 []{.arithmatex}$f$ 的两个零点且 []{.arithmatex}$x_1<x_2$，满足 []{.arithmatex}$f(x_1)=f(x_2)=0$。

  要证明 []{.arithmatex}$x_1+x_2>C$，不妨令

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  F(\Delta)=f\left(\dfrac{C}{2}+\Delta\right)-f\left(\dfrac{C}{2}-\Delta\right)
  :::

  $$F(\Delta)=f\left(\dfrac{C}{2}+\Delta\right)-f\left(\dfrac{C}{2}-\Delta\right)$$
  ::::

  其中 []{.arithmatex}$\Delta\ge0$，对 []{.arithmatex}$F$ 求导得

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  F\'(\Delta)=f\'\left(\dfrac{C}{2}+\Delta\right)+f\'\left(\dfrac{C}{2}-\Delta\right)
  :::

  $$F'(\Delta)=f'\left(\dfrac{C}{2}+\Delta\right)+f'\left(\dfrac{C}{2}-\Delta\right)$$
  ::::

  尝试证明其恒大于 []{.arithmatex}$0$，即 []{.arithmatex}$F$ 单调递增。

  得出 []{.arithmatex}$F(\Delta)\ge F(0)=0$，因此对于 []{.arithmatex}$\Delta>0$ 有

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  f\left(\dfrac{C}{2}+\Delta\right)\>f\left(\dfrac{C}{2}-\Delta\right)
  :::

  $$f\left(\dfrac{C}{2}+\Delta\right)>f\left(\dfrac{C}{2}-\Delta\right)$$
  ::::

  令 []{.arithmatex}$x_1=\dfrac{C}{2}-\Delta$，那么

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  f(x_2)=f(x_1)=f\left(\dfrac{C}{2}-\Delta\right)\<f\left(\dfrac{C}{2}+\Delta\right)
  :::

  $$f(x_2)=f(x_1)=f\left(\dfrac{C}{2}-\Delta\right)<f\left(\dfrac{C}{2}+\Delta\right)$$
  ::::

  因为 []{.arithmatex}$x_2>\dfrac{C}{2}$，因此 []{.arithmatex}$x_2>\dfrac{C}{2}+\Delta$，那么

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  x_1+x_2\>C
  :::

  $$x_1+x_2>C$$
  ::::

- 基础模型 []{.arithmatex}$h(x_1,x_2)=x_1x_2$。有 []{.arithmatex}$f'(x)$ 在 []{.arithmatex}$(-\infty,C)$ 恒负（函数单调递减），在 []{.arithmatex}$(C,+\infty)$ 恒正（函数单调递增），且 []{.arithmatex}$f'(C)=0$（极小值点）。

  设 []{.arithmatex}$x_1,x_2$ 为 []{.arithmatex}$f$ 的两个零点且 []{.arithmatex}$x_1<x_2$，满足 []{.arithmatex}$f(x_1)=f(x_2)=0$。

  要证明 []{.arithmatex}$x_1x_2<C^2$，不妨令

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  F(t)=f(tC)-f\left(\dfrac{1}{t}C\right)
  :::

  $$F(t)=f(tC)-f\left(\dfrac{1}{t}C\right)$$
  ::::

  其中 []{.arithmatex}$t\ge1$，对 []{.arithmatex}$F$ 求导得

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  F\'(t)=Cf\'(tC)+C\dfrac{1}{t\^2}f\'\left(\dfrac{1}{t}C\right)=C\left(1-\dfrac{1}{t\^2}\right)f\'\left(\dfrac{1}{t}C\right)
  :::

  $$F'(t)=Cf'(tC)+C\dfrac{1}{t^2}f'\left(\dfrac{1}{t}C\right)=C\left(1-\dfrac{1}{t^2}\right)f'\left(\dfrac{1}{t}C\right)$$
  ::::

  尝试证明其恒大于 []{.arithmatex}$0$，即 []{.arithmatex}$F$ 单调递增。

  得出 []{.arithmatex}$F(\Delta)\ge F(1)=0$，因此对于 []{.arithmatex}$t>1$ 有

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  f(tC)\>f\left(\dfrac{1}{t}C\right)
  :::

  $$f(tC)>f\left(\dfrac{1}{t}C\right)$$
  ::::

  令 []{.arithmatex}$x_1=\dfrac{1}{t}C$，那么

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  f(x_2)=f(x_1)=f\left(\dfrac{1}{t}C\right)\<f(tC)
  :::

  $$f(x_2)=f(x_1)=f\left(\dfrac{1}{t}C\right)<f(tC)$$
  ::::

  因为 []{.arithmatex}$x_2>C$，因此 []{.arithmatex}$x_2<tC$，那么

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  x_1x_2\<C\^2
  :::

  $$x_1x_2<C^2$$
  ::::

注意，直接进行极值点偏移，需要保证函数的极值点就是 []{.arithmatex}$C/2$ 或 []{.arithmatex}$\sqrt{C}$，如果不满足，就需要进行一定的变换。

### 构造变量法 {#_28}

经典例题：已知函数 []{.arithmatex}$f(x)=e^x-ax(a\neq0)$ 有两个零点 []{.arithmatex}$x_1,x_2$ 且 []{.arithmatex}$x_1<x_2$，证明 []{.arithmatex}$x_1+x_2>2$。

我们知道

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} e\^{x_1}&=ax_1\\ e\^{x_2}&=ax_2 \end{cases}
:::

$$\begin{cases}
e^{x_1}&=ax_1\\
e^{x_2}&=ax_2
\end{cases}$$
::::

那么：

:::: {.arithmatex}
::: {.MathJax_Preview}
x_2-x_1=\ln\dfrac{x_2}{x_1}
:::

$$x_2-x_1=\ln\dfrac{x_2}{x_1}$$
::::

令 []{.arithmatex}$t=\dfrac{x_2}{x_1}>1$，则：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} x_1&=\dfrac{\ln t}{t-1}\\ x_2&=\dfrac{t\ln t}{t-1} \end{cases}
:::

$$\begin{cases}
x_1&=\dfrac{\ln t}{t-1}\\
x_2&=\dfrac{t\ln t}{t-1}
\end{cases}$$
::::

要证 []{.arithmatex}$x_1+x_2>2$ 即证：

:::: {.arithmatex}
::: {.MathJax_Preview}
\dfrac{t+1}{t-1}\ln t\>2
:::

$$\dfrac{t+1}{t-1}\ln t>2$$
::::

即：

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln t\>\dfrac{2(t-1)}{t+1}
:::

$$\ln t>\dfrac{2(t-1)}{t+1}$$
::::

不妨令 []{.arithmatex}$g(t)=\ln t-\dfrac{2(t-1)}{t+1}$，则：

:::: {.arithmatex}
::: {.MathJax_Preview}
g\'(t)=\dfrac{1}{t}-\dfrac{2(t+1)-2(t-1)}{(t+1)\^2}=\dfrac{1}{t}-\dfrac{4}{(t+1)\^2}=\dfrac{(t-1)\^2}{t(t+1)\^2}
:::

$$g'(t)=\dfrac{1}{t}-\dfrac{2(t+1)-2(t-1)}{(t+1)^2}=\dfrac{1}{t}-\dfrac{4}{(t+1)^2}=\dfrac{(t-1)^2}{t(t+1)^2}$$
::::

我们注意到 []{.arithmatex}$g'(1)=0$ 且在 []{.arithmatex}$(1,+\infty)$ 上恒正，因此

:::: {.arithmatex}
::: {.MathJax_Preview}
g(x)\>g(1)=0
:::

$$g(x)>g(1)=0$$
::::

即不等式成立。

还有一种方法，由

:::: {.arithmatex}
::: {.MathJax_Preview}
x_2-x_1=\dfrac{x_2}{x_1}
:::

$$x_2-x_1=\dfrac{x_2}{x_1}$$
::::

得

:::: {.arithmatex}
::: {.MathJax_Preview}
\dfrac{x_2-x_1}{\ln\dfrac{x_2}{x_1}}=1
:::

$$\dfrac{x_2-x_1}{\ln\dfrac{x_2}{x_1}}=1$$
::::

要证 []{.arithmatex}$x_1+x_2>2$ 即证：

:::: {.arithmatex}
::: {.MathJax_Preview}
x_1+x_2\>\dfrac{2(x_2-x_1)}{\ln\dfrac{x_2}{x_1}}
:::

$$x_1+x_2>\dfrac{2(x_2-x_1)}{\ln\dfrac{x_2}{x_1}}$$
::::

令 []{.arithmatex}$t=\dfrac{x_2}{x_1}>1$，即证：

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln t\>\dfrac{2(t-1)}{t+1}
:::

$$\ln t>\dfrac{2(t-1)}{t+1}$$
::::

前面已经证明，显然成立。

对于形如证明 []{.arithmatex}$x_1x_2<C$ 的，我们将在下面构造函数法中写。

### 构造函数法 {#_29}

例题：已知函数 []{.arithmatex}$f(x)=\dfrac{1}{2}x+m+\dfrac{3}{2x}-\ln x(m\in\R)$，若 []{.arithmatex}$x_1,x_2$ 是函数 []{.arithmatex}$g(x)=xf(x)$ 的两个极值点，且 []{.arithmatex}$x_1<x_2$，证明 []{.arithmatex}$x_1x_2<1$。

我们令 []{.arithmatex}$g(x)=xf(x)=mx-x\ln x+\dfrac{1}{2}x^2+\dfrac{3}{2}$，对其求导

:::: {.arithmatex}
::: {.MathJax_Preview}
g\'(x)=x-\ln x+m-1
:::

$$g'(x)=x-\ln x+m-1$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
g\'\'(x)=\dfrac{x-1}{x}
:::

$$g''(x)=\dfrac{x-1}{x}$$
::::

当 []{.arithmatex}$0<x<1$ 时，[]{.arithmatex}$g''(x)<0$，[]{.arithmatex}$g'(x)$ 单调递减；当 []{.arithmatex}$x>1$ 时，[]{.arithmatex}$g''(x)>0$，[]{.arithmatex}$g'(x)$ 单调递增。因此 []{.arithmatex}$1$ 为 []{.arithmatex}$g'(x)$ 的极值点，因此 []{.arithmatex}$0<x_1<1<x_2$。

要证 []{.arithmatex}$x_1x_2<1$ 即证

:::: {.arithmatex}
::: {.MathJax_Preview}
x_2\<\dfrac{1}{x_1}
:::

$$x_2<\dfrac{1}{x_1}$$
::::

因为 []{.arithmatex}$0<x_1<1$ 所以 []{.arithmatex}$\dfrac{1}{x_1}>1$，因此尝试证明

:::: {.arithmatex}
::: {.MathJax_Preview}
g\'(x_2)\<g\'\left(\dfrac{1}{x_1}\right)
:::

$$g'(x_2)<g'\left(\dfrac{1}{x_1}\right)$$
::::

又因为 []{.arithmatex}$g'(x_1)=g'(x_2)=0$，因此证明

:::: {.arithmatex}
::: {.MathJax_Preview}
g\'(x_1)\<g\'\left(\dfrac{1}{x_1}\right)
:::

$$g'(x_1)<g'\left(\dfrac{1}{x_1}\right)$$
::::

令函数

:::: {.arithmatex}
::: {.MathJax_Preview}
h(x)=g\'(x)-g\'\left(\dfrac{1}{x}\right)=x-\dfrac{1}{x}-2\ln x(0\<x\<1)
:::

$$h(x)=g'(x)-g'\left(\dfrac{1}{x}\right)=x-\dfrac{1}{x}-2\ln x(0<x<1)$$
::::

求导得

:::: {.arithmatex}
::: {.MathJax_Preview}
h\'(x)=\dfrac{(x-1)\^2}{x\^2}\>0
:::

$$h'(x)=\dfrac{(x-1)^2}{x^2}>0$$
::::

因此 []{.arithmatex}$h(x)$ 单调递增，从而 []{.arithmatex}$h(x)<h(1)=0$，得证。

这道题也可以用构造变量法，同样令 []{.arithmatex}$t=\dfrac{x_2}{x_1}>1$，证明

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln t\<\sqrt{t}-\dfrac{1}{\sqrt{t}}
:::

$$\ln t<\sqrt{t}-\dfrac{1}{\sqrt{t}}$$
::::

即可。

### 变形双变量 {#_30}

当双变量不再对称，构造函数与构造变量都可以适用。

- 对于构造函数，只需要确保极值点与常数项对应，然后找到极值点两边证明即可。

- 对于构造变量，只需要按照原来的方法，带入不等式，只是解不等式可能有一些复杂。

联立两个零点，经常可以得到类似于

:::: {.arithmatex}
::: {.MathJax_Preview}
\ln\dfrac{x_1}{x_2}=x_1-x_2
:::

$$\ln\dfrac{x_1}{x_2}=x_1-x_2$$
::::

的式子，设 []{.arithmatex}$t=\dfrac{x_1}{x_2}\in(0,1)$，一是可以将其化为

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} x_1&=\dfrac{t\ln t}{t-1}\\ x_2&=\dfrac{\ln t}{t-1} \end{cases}
:::

$$\begin{cases}
x_1&=\dfrac{t\ln t}{t-1}\\
x_2&=\dfrac{\ln t}{t-1}
\end{cases}$$
::::

然后带入，直接证明一元不等式，二是可以将

:::: {.arithmatex}
::: {.MathJax_Preview}
1=\dfrac{x_1-x_2}{\ln\dfrac{x_1}{x_2}}
:::

$$1=\dfrac{x_1-x_2}{\ln\dfrac{x_1}{x_2}}$$
::::

或其倒数，利用 []{.arithmatex}$1$ 的代还，解决问题。

### 拐点偏移 {#_31}

我们知道拐点是二阶导数的变号点。若函数在拐点两侧的变化速度相同，那么函数图像关于拐点中心对称；若变化速度不同，则图像会出现"偏移"。我们把这种现象称为"拐点偏移"。

我们知道常见的极值点偏移是给出 []{.arithmatex}$f(x_1)=f(x_2)=0$，而拐点偏移比较常见的是给出 []{.arithmatex}$f(x_1)+f(x_2)=C$ 这种，我们以例题。

例题：已知函数 []{.arithmatex}$f(x)=2\ln x+x^2-1$，若 []{.arithmatex}$x_1,x_2$ 是两个不相等的正数，且 []{.arithmatex}$f(x_1)+f(x_2)=0$，证明 []{.arithmatex}$x_1+x_2>2$。

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x)=\dfrac{2}{x}+2x\ge4
:::

$$f'(x)=\dfrac{2}{x}+2x\ge4$$
::::

因此 []{.arithmatex}$f(x)$ 单调递增，且 []{.arithmatex}$f(1)=0$，注意到 []{.arithmatex}$2$ 就是两倍的零点，我们不妨设

:::: {.arithmatex}
::: {.MathJax_Preview}
0\<x_1\<1\<x_2\<2
:::

$$0<x_1<1<x_2<2$$
::::

因为 []{.arithmatex}$x_2>2$ 的时候，显然 []{.arithmatex}$x_1+x_2>2$。考虑这个部分，即证

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x_2)\>f(2-x_1)
:::

$$f(x_2)>f(2-x_1)$$
::::

又因为 []{.arithmatex}$f(x_2)=-f(x_1)$，因此证

:::: {.arithmatex}
::: {.MathJax_Preview}
-f(x_1)\>f(2-x_1)
:::

$$-f(x_1)>f(2-x_1)$$
::::

不妨设

:::: {.arithmatex}
::: {.MathJax_Preview}
g(x)=f(x)+f(2-x)=2\ln(2x-x\^2)-2(2x-x\^2)+2
:::

$$g(x)=f(x)+f(2-x)=2\ln(2x-x^2)-2(2x-x^2)+2$$
::::

其中 []{.arithmatex}$x\in(0,1)$，不妨令 []{.arithmatex}$t=2x-x^2\in(0,1)$，由 []{.arithmatex}$\ln t<x-1$，不等式显然成立。
