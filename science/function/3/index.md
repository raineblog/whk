# 函数性质 {#_1}

## 基本性质 {#_2}

### 奇偶性 {#_3}

定义奇偶性于定义域关于 []{.arithmatex}$0$ 对称的函数上，奇函数为：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)+f(-x)=0
:::

$$f(x)+f(-x)=0$$
::::

因此，我们知道，如果定义域中有 []{.arithmatex}$0$，那么只有 []{.arithmatex}$f(0)=0$ 的函数才可能为奇函数。

偶函数为：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)=f(-x)
:::

$$f(x)=f(-x)$$
::::

特殊的，奇函数的绝对值为偶函数。

奇偶性的乘除法则：

- 奇函数 []{.arithmatex}$\pm$ 奇函数 []{.arithmatex}$=$ 奇函数。
- 偶函数 []{.arithmatex}$\pm$ 偶函数 []{.arithmatex}$=$ 偶函数。
- 奇函数 []{.arithmatex}$\pm$ 偶函数 []{.arithmatex}$=$ 非奇非偶。
- 奇函数 []{.arithmatex}$\times$ 奇函数 []{.arithmatex}$=$ 偶函数。
- 奇函数 []{.arithmatex}$\times$ 偶函数 []{.arithmatex}$=$ 奇函数。
- 偶函数 []{.arithmatex}$\times$ 偶函数 []{.arithmatex}$=$ 偶函数。

复合函数的奇偶性：

- 奇函数 []{.arithmatex}$\circ$ 奇函数 []{.arithmatex}$=$ 奇函数。
- 偶函数 []{.arithmatex}$\circ$ 奇函数 []{.arithmatex}$=$ 偶函数。
- 奇函数 []{.arithmatex}$\circ$ 偶函数 []{.arithmatex}$=$ 偶函数。
- 偶函数 []{.arithmatex}$\circ$ 偶函数 []{.arithmatex}$=$ 偶函数。

经典做题套路：

- 若 []{.arithmatex}$f(x)$ 为偶函数，首先判断是否能转化为奇函数来处理。

- 奇函数 []{.arithmatex}$f(x)$ 在定义域内有最大值 []{.arithmatex}$M$，则 []{.arithmatex}$f(x)$ 有最小值 []{.arithmatex}$N$，且 []{.arithmatex}$M+N=0$。

- 若偶函数 []{.arithmatex}$f(x)$ 在 []{.arithmatex}$[0, +\infty)$ 上单调，则 []{.arithmatex}$f(x_1) = f(x_2)$ 等价于 []{.arithmatex}$|x_1| = |x_2|$；

- 若偶函数 []{.arithmatex}$f(x)$ 在 []{.arithmatex}$[0, +\infty)$ 上单调递增，则 []{.arithmatex}$f(x_1) > f(x_2)$ 等价于 []{.arithmatex}$|x_1| > |x_2|$；

- 若偶函数 []{.arithmatex}$f(x)$ 在 []{.arithmatex}$[0, +\infty)$ 上单调递减，则 []{.arithmatex}$f(x_1) > f(x_2)$ 等价于 []{.arithmatex}$|x_1| < |x_2|$。

经典的函数模型：

- 函数 []{.arithmatex}$f(x)=\dfrac{1\pm a^x}{1\mp a^x}$，[]{.arithmatex}$g(x)=\log_a\dfrac{1\pm x}{1\mp x}$ 是单调的奇函数。

- 函数 []{.arithmatex}$f(x)=\log_a(\sqrt{x^2+1}\pm x)$ 是单调的奇函数。

- 函数 []{.arithmatex}$f(x)=a^x+a^{-x}$ 是偶函数，函数 []{.arithmatex}$g(x)=a^x-a^{-x}$ 是单调的奇函数。

奇偶性与导数：对于可导函数 []{.arithmatex}$f(x)$，如果 []{.arithmatex}$f(x)$ 是奇函数，则 []{.arithmatex}$f'(x)$ 是偶函数；如果 []{.arithmatex}$f(x)$ 是偶函数，则 []{.arithmatex}$f'(x)$ 是奇函数。

### 对称性 {#_4}

函数关于 []{.arithmatex}$x=x_0$ 对称，则：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x_0-a)=f(x_0+a),\quad\forall a\in\R\^+
:::

$$f(x_0-a)=f(x_0+a),\quad\forall a\in\R^+$$
::::

或者 []{.arithmatex}$y=f(x+x_0)$ 为偶函数。

函数关于 []{.arithmatex}$(x_0,y_0)$ 中心对称，则：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x_0-a)+f(x_0+a)=2y_0,\quad\forall a\in\R\^+
:::

$$f(x_0-a)+f(x_0+a)=2y_0,\quad\forall a\in\R^+$$
::::

或者 []{.arithmatex}$y=f(x+a)-b$ 为奇函数。

因此，我们得到，若：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x+\mu)=f(\lambda-x)
:::

$$f(x+\mu)=f(\lambda-x)$$
::::

则函数关于 []{.arithmatex}$x=\dfrac{\lambda+\mu}{2}$ 对称；若：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x+\mu)+f(\lambda-x)=k
:::

$$f(x+\mu)+f(\lambda-x)=k$$
::::

则函数关于 []{.arithmatex}$\left(\dfrac{\lambda+\mu}{2},\dfrac{k}{2}\right)$ 对称。

若给定两个函数，求一个 []{.arithmatex}$P$（点或线）使两个函数关于其对称，可以转化为求一个函数关于 []{.arithmatex}$P$ 对称的函数与另一个函数的交点问题。

| 条件 | 结论 |
|:---|:---|
| []{.arithmatex}$f(x+a)=f(x+b)$ | []{.arithmatex}$T=\vert b-a \vert$ |
| []{.arithmatex}$f(x)+f(x+a)=C$ | []{.arithmatex}$T=2\vert a \vert$ |
| []{.arithmatex}$f(x)\times f(x+a)=C$ | []{.arithmatex}$T=2\vert a \vert$ |
| []{.arithmatex}$f(x+2a)=f(x+a)-f(x)$ | []{.arithmatex}$T=6\vert a \vert$ |
| []{.arithmatex}$f(x)$ 关于 []{.arithmatex}$x=a,x=b$ 对称 | []{.arithmatex}$T=2\vert b-a \vert$ |
| []{.arithmatex}$f(x)$ 的两个对称中心 []{.arithmatex}$(a,0)$，[]{.arithmatex}$(b,0)$ | []{.arithmatex}$T=2\vert b-a \vert$ |
| []{.arithmatex}$f(x)$ 关于 []{.arithmatex}$x=a$ 对称且有一个对称中心 []{.arithmatex}$(b,0)$ | []{.arithmatex}$T=4\vert b-a \vert$ |

三次及以下的多项式函数具有一般对称性，四次及以上的多项式函数不具有一般对称性。

- 最高幂次为奇数的多项式函数只可能具有中心对称性，最高幂次为偶数的多项式函数只可能具有轴对称性。

- 如果一个多项式函数 []{.arithmatex}$f(x)=a_n x^n + a_{n-1}x^{n-1}+\dots+a_1 x+a_0$ 具有中心对称性，那么它的对称中心为

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  \left(-\frac{a\_{n-1}}{na_n},f\left(-\frac{a\_{n-1}}{na_n}\right)\right)
  :::

  $$\left(-\frac{a_{n-1}}{na_n},f\left(-\frac{a_{n-1}}{na_n}\right)\right)$$
  ::::

- 如果一个多项式函数 []{.arithmatex}$f(x)=a_n x^n + a_{n-1}x^{n-1}+\dots+a_1 x+a_0$ 具有轴对称性，那么它的对称轴

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  x=-\frac{a\_{n-1}}{na_n}
  :::

  $$x=-\frac{a_{n-1}}{na_n}$$
  ::::

- []{.arithmatex}$f(x)=ax^3+bx^2+cx+d$ 的对称中心

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  \left(-\frac{b}{3a},f\left(-\frac{b}{3a}\right)\right)
  :::

  $$\left(-\frac{b}{3a},f\left(-\frac{b}{3a}\right)\right)$$
  ::::

其他对称模型：

- []{.arithmatex}$\displaystyle f(x)=\frac{ax+b}{cx+d}$ 的对称中心 []{.arithmatex}$\displaystyle\left(-\frac{d}{c},\frac{a}{c}\right)$。注意到该函数的定义域为 []{.arithmatex}$\displaystyle\left\{x\mid x\neq - \frac{d}{c}\right\}$，值域是 []{.arithmatex}$\displaystyle\left\{x\mid x\neq\frac{a}{c}\right\}$。

- 任何一个函数 []{.arithmatex}$f(x)$ 都可以拆分为一个奇函数 []{.arithmatex}$F(x)$ 和一个偶函数 []{.arithmatex}$G(x)$ 的和。

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  \begin{cases} F(x)&=\dfrac{f(x)-f(-x)}{2}\\ G(x)&=\dfrac{f(x)+f(-x)}{2} \end{cases}
  :::

  $$\begin{cases}
  F(x)&=\dfrac{f(x)-f(-x)}{2}\\
  G(x)&=\dfrac{f(x)+f(-x)}{2}
  \end{cases}$$
  ::::

- []{.arithmatex}$\displaystyle f(x+a)=\frac{1+f(x)}{1-f(x)} \implies T=4a$。

### 周期性 {#_5}

对于任意 []{.arithmatex}$x\in\R$，存在非零实数 []{.arithmatex}$T$ 满足 []{.arithmatex}$f(x+T)=f(x)$，则 []{.arithmatex}$f(x)$ 为周期函数，且一个周期为 []{.arithmatex}$T$。在周期函数 所有周期中最小的一个正数，称为最小正周期。

在已知周期的前提下的求值及表达式问题都是需要把所求变量利用周期平移至所给区间，利用所给区间的表达式来求值或者求表达式。

常见的周期函数：

- 对任意的 []{.arithmatex}$x\in\R$，若 []{.arithmatex}$f(x+a)+f(x)=c$，则 []{.arithmatex}$T=2|a|$。

- 对任意的 []{.arithmatex}$x\in\R$，若 []{.arithmatex}$f(x+a)\cdot f(x)=c$，则 []{.arithmatex}$T=2|a|$。

- 对任意的 []{.arithmatex}$x\in\R$，若 []{.arithmatex}$f(x+a)=f(x-a)$，则 []{.arithmatex}$T=2|a|$。

- 对任意的 []{.arithmatex}$x\in\R$，若 []{.arithmatex}$f(x+a)=-f(x-a)$，则 []{.arithmatex}$T=4|a|$。

- 若 []{.arithmatex}$x$ 满足 []{.arithmatex}$f(x)=f(x+a)-f(x+2a)$，则 []{.arithmatex}$T=6|a|$。

对称性与周期性：

- 如果 []{.arithmatex}$f(x)$ 关于 []{.arithmatex}$x=a$ 和 []{.arithmatex}$x=b$ 对称，则 []{.arithmatex}$T=2|a-b|$。

- 如果 []{.arithmatex}$f(x)$ 关于 []{.arithmatex}$(a,0)$ 和 []{.arithmatex}$(b,0)$ 对称，则 []{.arithmatex}$T=2|a-b|$。

- 如果 []{.arithmatex}$f(x)$ 关于 []{.arithmatex}$(a,0)$ 和 []{.arithmatex}$x=b$ 对称，则 []{.arithmatex}$T=4|a-b|$。

## 函数模型 {#_6}

### 二次函数 {#_7}

对于一元二次方程 []{.arithmatex}$ax^2+bx+c(a\neq0)$，当根的判别式 []{.arithmatex}$\Delta=b^2-4ac$ 时，记 []{.arithmatex}$x_1,x_2$ 为方程的两个实根，则有韦达定理

:::: {.arithmatex}
::: {.MathJax_Preview}
x_1+x_2=-\dfrac{b}{a}
:::

$$x_1+x_2=-\dfrac{b}{a}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
x_1x_2=\dfrac{c}{a}
:::

$$x_1x_2=\dfrac{c}{a}$$
::::

一元二次方程的根往往会有各种限制，比如两根都为正、两根都为负等。这类问题需要综合考虑开口方向、对称轴、根的判别式以及韦达定理才能准确求解，例如有两个不同的正根

:::: {.arithmatex}
::: {.MathJax_Preview}
\iff\begin{cases}\Delta\>0\\x_1+x_2\>0\\x_1x_2\>0\end{cases}
:::

$$\iff\begin{cases}\Delta>0\\x_1+x_2>0\\x_1x_2>0\end{cases}$$
::::

同时，一定情况下也可以用参变分离解决，例如 []{.arithmatex}$ax^2+2x+1$ 至少有一个正根，则：

:::: {.arithmatex}
::: {.MathJax_Preview}
a=-\dfrac{2x+1}{x\^2}=-\left(\dfrac{2}{x}+\dfrac{1}{x\^2}\right)
:::

$$a=-\dfrac{2x+1}{x^2}=-\left(\dfrac{2}{x}+\dfrac{1}{x^2}\right)$$
::::

问题即为求该式在 []{.arithmatex}$x>0$ 时的值域，设 []{.arithmatex}$t=1/x>0$，则：

:::: {.arithmatex}
::: {.MathJax_Preview}
a=-(t\^2+2t)\<0
:::

$$a=-(t^2+2t)<0$$
::::

即 []{.arithmatex}$a$ 的取值范围是 []{.arithmatex}$(-\infty,0)$。

如果要求 []{.arithmatex}$f(x)=ax^2+bx+c(a\neq0)$ 有两个大于 []{.arithmatex}$r$ 的实根，容易想到，构造函数 []{.arithmatex}$g(x)=f(x+r)$，对 []{.arithmatex}$g(x)$ 应用两个实根大于 []{.arithmatex}$0$，但是这样比较复杂，我们进行一次模拟：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} \Delta\>0\\ (x_1-r)+(x_2-r)\>0\\ (x_1-r)(x_2-r)\>0 \end{cases}
:::

$$\begin{cases}
\Delta>0\\
(x_1-r)+(x_2-r)>0\\
(x_1-r)(x_2-r)>0
\end{cases}$$
::::

注意到第二个相当于：

:::: {.arithmatex}
::: {.MathJax_Preview}
x_1+x_2=-\dfrac{b}{a}\>2r
:::

$$x_1+x_2=-\dfrac{b}{a}>2r$$
::::

而第三个则为：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} x_1x_2-r(x_1+x_2)+r\^2&\>0\\ \dfrac{c}{a}+\dfrac{br}{a}+r\^2&\>0 \end{aligned}
:::

$$\begin{aligned}
x_1x_2-r(x_1+x_2)+r^2&>0\\
\dfrac{c}{a}+\dfrac{br}{a}+r^2&>0
\end{aligned}$$
::::

也就是：

:::: {.arithmatex}
::: {.MathJax_Preview}
af(r)\>0
:::

$$af(r)>0$$
::::

因此，我们把条件转化为：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} \Delta\>0\\ x_1+x_2\>2r\\ af(r)\>0 \end{cases}
:::

$$\begin{cases}
\Delta>0\\
x_1+x_2>2r\\
af(r)>0
\end{cases}$$
::::

另外，如果有两个不同的实根，在区间 []{.arithmatex}$(p,q)$ 内，那么：

:::: {.arithmatex}
::: {.MathJax_Preview}
\iff\begin{cases} \Delta\>0\\ 2p\<-\dfrac{b}{a}\<2q\\ af(p)\>0\\ af(q)\>0 \end{cases}
:::

$$\iff\begin{cases}
\Delta>0\\
2p<-\dfrac{b}{a}<2q\\
af(p)>0\\
af(q)>0
\end{cases}$$
::::

二次方程 []{.arithmatex}$f(x) = ax^2 + bx + c = 0(a \neq 0)$ 在区间 []{.arithmatex}$(p,q)$，[]{.arithmatex}$(m,n)$ 内各有一个实数根，若 []{.arithmatex}$a$ 的正负不确定，则其等价条件为

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} f(p)f(q) \< 0 \\ f(m)f(n) \< 0 \end{cases}
:::

$$\begin{cases}
f(p)f(q) < 0 \\
f(m)f(n) < 0
\end{cases}$$
::::

若已知 []{.arithmatex}$a$ 的正负，则只需具体考虑端点处函数值的正负。

### 三次函数 {#_8}

三次函数的根本思想有两个，因式分解，求导。

我们知道，即使是对于更高次的函数，求导也是一般方法，只是三次函数求导后变为二次函数更好解决。

三次函数 []{.arithmatex}$f(x)=ax^3+bx^2+cx+d(a\neq0)$ 是中心对称图像，且其对称中心为 []{.arithmatex}$\left(-\dfrac{b}{3a},f(\dots)\right)$。

### 特殊函数 {#_9}

复合函数：

- 若函数 []{.arithmatex}$f(x)$ 单调递增，则 []{.arithmatex}$f(f(x))=x$ 的解与 []{.arithmatex}$f(x)=x$ 的解相同。

- 方程 []{.arithmatex}$f(f(x))=x$ 有解等价于 []{.arithmatex}$f(x)=x$ 有解；方程 []{.arithmatex}$f(f(x))=x$ 无解等价于 []{.arithmatex}$f(x)=x$ 无解。

- 记 []{.arithmatex}$f(x)=x$ 的解集为 []{.arithmatex}$A$，记 []{.arithmatex}$f(f(x))=x$ 的解集为 []{.arithmatex}$B$，若 []{.arithmatex}$f(x)$ 单调递增，则 []{.arithmatex}$A=B$，否则 []{.arithmatex}$A\subseteq B$。

- 方程 []{.arithmatex}$f(g(x))=x$ 有解等价于 []{.arithmatex}$g(f(x))=x$ 有解。

高斯函数：

- 下取整函数 []{.arithmatex}$f(x) = [x]$，其中 []{.arithmatex}$[x]$ 表示不超过 []{.arithmatex}$x$ 的最大整数，例如 []{.arithmatex}$[1.2] = 1$，[]{.arithmatex}$[-1.2] = -2$，[]{.arithmatex}$[2] = 2$。

- 上取整函数 []{.arithmatex}$f(x) = \{x\}$，其中 []{.arithmatex}$\{x\}$ 表示不小于 []{.arithmatex}$x$ 的最小整数，例如 []{.arithmatex}$\{1.1\} = 2$，[]{.arithmatex}$\{-1.1\} = -1$，[]{.arithmatex}$\{2\} = 2$。

- 非负小数部分函数 []{.arithmatex}$f(x) = x - [x]$。非负小数部分函数是一个周期为 []{.arithmatex}$1$，值域为 []{.arithmatex}$[0, 1)$ 的周期函数。

![alt text](../image-3.avif){width="80%"}

基本性质：

- 下取整函数满足 []{.arithmatex}$x - 1 < [x] \le x$，[]{.arithmatex}$[x] \le x < [x] + 1$。

- 上取整函数满足 []{.arithmatex}$x \le \{x\} < x+1$，[]{.arithmatex}$\{x\} - 1 < x \le \{x\}$。

形如 []{.arithmatex}$[f(x)] = g(x)$ 方程的一般解法：

1.  令 []{.arithmatex}$[f(x)] = k$（[]{.arithmatex}$k \in \mathbb{Z}$），得不等式 []{.arithmatex}$k \le f(x) < k+1$。
2.  从 []{.arithmatex}$g(x) = k$ 中反解出 []{.arithmatex}$x$，记为 []{.arithmatex}$x = h(k)$，即 []{.arithmatex}$k \le f[h(k)] < k+1$。
3.  解（2）中的关于整数 []{.arithmatex}$k$ 的不等式，将所得 []{.arithmatex}$k$ 值代入 []{.arithmatex}$x = h(k)$ 得方程的解。

常见函数：

![alt text](../geogebra-export.svg)

![alt text](../geogebra-export%20%282%29.svg)

### 函数构造 {#_10}

解决此类问题的关键在于识别代数式中的"导数指纹"。

- 见到 []{.arithmatex}$xf'(x) + f(x)$，构造 []{.arithmatex}$h(x) = xf(x)$。

- 见到 []{.arithmatex}$xf'(x) - f(x)$，构造 []{.arithmatex}$h(x) = \frac{f(x)}{x}$。

- 见到 []{.arithmatex}$f'(x) \ln x - \frac{f(x)}{x}$，构造 []{.arithmatex}$h(x) = \frac{f(x)}{\ln x}$。

- 见到 []{.arithmatex}$f'(x) + f(x)$，构造 []{.arithmatex}$h(x) = e^x f(x)$。

高中数学中的"构造辅助函数"往往被视为一种"技巧"或"灵感"，学生通常通过背诵口诀（如"加用乘，减用除"）来应对。但在大学数学（常微分方程和算子理论）的视角下，这并非偶然的灵感，而是一套严密的**系统性方法**，即**一阶线性微分方程的求解理论**。

在高中阶段，我们处理的核心是不等式 []{.arithmatex}$f'(x) + P(x)f(x) > 0$。解决它的关键在于**将左边凑成一个整体的导数**。

- 乘法法则的逆向：

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  \[u(x)v(x)\]\' = u\'(x)v(x) + u(x)v\'(x)
  :::

  $$[u(x)v(x)]' = u'(x)v(x) + u(x)v'(x)$$
  ::::

  如果我们遇到形如 []{.arithmatex}$xf'(x) + f(x) > 0$ 的式子，你会敏锐地发现这就是 []{.arithmatex}$(xf(x))' > 0$。

- 除法法则的逆向：

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  \left\[\frac{u(x)}{v(x)}\right\]\' = \frac{u\'(x)v(x) - u(x)v\'(x)}{v\^2(x)}
  :::

  $$\left[\frac{u(x)}{v(x)}\right]' = \frac{u'(x)v(x) - u(x)v'(x)}{v^2(x)}$$
  ::::

  对于不等式 []{.arithmatex}$f'(x) - f(x) > 0$，我们将其变形为

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  \dfrac{f\'(x) \cdot e\^x - f(x) \cdot (e\^x)\'}{e\^{2x}} \> 0
  :::

  $$\dfrac{f'(x) \cdot e^x - f(x) \cdot (e^x)'}{e^{2x}} > 0$$
  ::::

  即 []{.arithmatex}$[f(x)/e^x]' > 0$。

高中视角的局限在于：当系数变得复杂时（比如 []{.arithmatex}$f'(x) + xf(x) > 0$），单纯靠观察"积的导数"或"商的导数"很难直接凑出辅助函数。这就需要引入更通用的工具------积分因子。

积分因子法：任何一阶线性形式 []{.arithmatex}$f'(x) + P(x)f(x)$，都可以通过乘以一个非零函数 []{.arithmatex}$\mu(x)$（称为积分因子），使其变为一个整体的导数 []{.arithmatex}$[\mu(x)f(x)]'$。

假设我们要处理不等式：

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x) + P(x)f(x) \> 0
:::

$$f'(x) + P(x)f(x) > 0$$
::::

我们希望找到一个函数 []{.arithmatex}$\mu(x)$（假定 []{.arithmatex}$\mu(x) > 0$），使得不等式两边同乘 []{.arithmatex}$\mu(x)$ 后，左边变成一个乘积的导数：

:::: {.arithmatex}
::: {.MathJax_Preview}
\mu(x)f\'(x) + \mu(x)P(x)f(x) \equiv \[\mu(x)f(x)\]\'
:::

$$\mu(x)f'(x) + \mu(x)P(x)f(x) \equiv [\mu(x)f(x)]'$$
::::

展开右边：

:::: {.arithmatex}
::: {.MathJax_Preview}
\[\mu(x)f(x)\]\' = \mu(x)f\'(x) + \mu\'(x)f(x)
:::

$$[\mu(x)f(x)]' = \mu(x)f'(x) + \mu'(x)f(x)$$
::::

对比左右两边的系数，因此，我们需要满足微分方程：

:::: {.arithmatex}
::: {.MathJax_Preview}
\mu\'(x) = P(x)\mu(x)
:::

$$\mu'(x) = P(x)\mu(x)$$
::::

利用分离变量法求解 []{.arithmatex}$\mu(x)$：

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{d\mu}{\mu} = P(x)dx \implies \ln\|\mu\| = \int P(x)dx \implies \mu(x) = e\^{\int P(x)dx}
:::

$$\frac{d\mu}{\mu} = P(x)dx \implies \ln|\mu| = \int P(x)dx \implies \mu(x) = e^{\int P(x)dx}$$
::::

**万能公式**：对于 []{.arithmatex}$f'(x) + P(x)f(x)$ 型结构，辅助函数构造的一般规律是构造

:::: {.arithmatex}
::: {.MathJax_Preview}
g(x) = e\^{\int P(x)dx} \cdot f(x)
:::

$$g(x) = e^{\int P(x)dx} \cdot f(x)$$
::::

微分算子：将求导看作一种线性变换，定义微分算子 []{.arithmatex}$D = \frac{d}{dx}$，恒等算子 []{.arithmatex}$I$（即 []{.arithmatex}$If = f$）。原不等式 []{.arithmatex}$f'(x) + P(x)f(x) > 0$ 可以写成算子作用的形式：

:::: {.arithmatex}
::: {.MathJax_Preview}
(D + P(x))f(x) \> 0
:::

$$(D + P(x))f(x) > 0$$
::::

我们有一个非常漂亮的**算子恒等式**（移位公式）：

:::: {.arithmatex}
::: {.MathJax_Preview}
D + P(x) = e\^{-\int P dx} \cdot D \cdot e\^{\int P dx}
:::

$$D + P(x) = e^{-\int P dx} \cdot D \cdot e^{\int P dx}$$
::::

**证明**：设 []{.arithmatex}$M(x) = e^{\int P(x)dx}$。

对任意函数 []{.arithmatex}$y$，考虑右边 []{.arithmatex}$M^{-1} D (M y)$ 的作用结果：

:::: {.arithmatex}
::: {.MathJax_Preview}
e\^{-\int P} \frac{d}{dx} \left( e\^{\int P} y \right) = e\^{-\int P} \left( P e\^{\int P} y + e\^{\int P} y\' \right) = P y + y\' = (D + P)y
:::

$$e^{-\int P} \frac{d}{dx} \left( e^{\int P} y \right) = e^{-\int P} \left( P e^{\int P} y + e^{\int P} y' \right) = P y + y' = (D + P)y$$
::::

**应用意义**：不等式 []{.arithmatex}$(D + P)f > 0$ 等价于

:::: {.arithmatex}
::: {.MathJax_Preview}
e\^{-\int P} D \left( e\^{\int P} f \right) \> 0
:::

$$e^{-\int P} D \left( e^{\int P} f \right) > 0$$
::::

因为指数函数 []{.arithmatex}$e^{-\int P}$ 恒正，可以直接约去（如果是方程则不能随便约，不等式只看符号）：

:::: {.arithmatex}
::: {.MathJax_Preview}
D \left( e\^{\int P} f \right) \> 0
:::

$$D \left( e^{\int P} f \right) > 0$$
::::

即 []{.arithmatex}$\left[ e^{\int P(x)dx} \cdot f(x) \right]'$ 单调递增。

**这一视角极其强大，因为它把"构造辅助函数"变成了"算子分解"。**

下面我们运用"积分因子/算子法"解决从高中到竞赛难度的几类问题。

#### 类型一：常系数模型（基础） {#_11}

**题目**：已知 []{.arithmatex}$f(x)$ 定义在 []{.arithmatex}$\mathbb{R}$ 上，且 []{.arithmatex}$f'(x) + 2f(x) > 0$，求 []{.arithmatex}$f(x) > e^{-2x}$ 的解集（已知 []{.arithmatex}$f(0)=1$）。

**解析**：

1.  识别 []{.arithmatex}$P(x) = 2$。
2.  积分因子 []{.arithmatex}$\mu(x) = e^{\int 2 dx} = e^{2x}$。
3.  构造 []{.arithmatex}$g(x) = e^{2x}f(x)$。
4.  由 []{.arithmatex}$f'(x) + 2f(x) > 0$ 两边乘 []{.arithmatex}$e^{2x}$ 得 []{.arithmatex}$[e^{2x}f(x)]' > 0$。
5.  []{.arithmatex}$g(x)$ 单调递增。[]{.arithmatex}$g(x) > g(0) \implies e^{2x}f(x) > 1 \implies f(x) > e^{-2x}$。
6.  解集为 []{.arithmatex}$(0, +\infty)$。

#### 类型二：一次函数系数模型（进阶） {#_12}

**题目**：已知 []{.arithmatex}$x > 0$ 时，[]{.arithmatex}$xf'(x) + 2f(x) > 0$，且 []{.arithmatex}$f(1)=1$，解 []{.arithmatex}$f(x) < \frac{1}{x^2}$。

**解析**：

1.  标准化：[]{.arithmatex}$f'(x) + \frac{2}{x}f(x) > 0$。
2.  识别 []{.arithmatex}$P(x) = \frac{2}{x}$。
3.  积分因子 []{.arithmatex}$\mu(x) = e^{\int \frac{2}{x} dx} = e^{2\ln x} = x^2$。
4.  构造 []{.arithmatex}$g(x) = x^2 f(x)$。
5.  验证：[]{.arithmatex}$g'(x) = 2xf(x) + x^2 f'(x) = x(2f(x) + xf'(x))$。在 []{.arithmatex}$x>0$ 时，符号与原条件一致。
6.  []{.arithmatex}$g(x)$ 增，[]{.arithmatex}$g(x) < g(1) = 1 \implies x^2 f(x) < 1 \implies f(x) < \frac{1}{x^2}$。
7.  解集为 []{.arithmatex}$(0, 1)$。

#### 类型三：变系数模型（高阶/竞赛） {#_13}

**题目**：定义在 []{.arithmatex}$\mathbb{R}$ 上的函数满足 []{.arithmatex}$f'(x) + xf(x) > 0$，且 []{.arithmatex}$f(0)=1$，试比较 []{.arithmatex}$f(1)$ 与 []{.arithmatex}$e^{-0.5}$ 的大小。

**解析**：

1.  识别 []{.arithmatex}$P(x) = x$。
2.  积分因子 []{.arithmatex}$\mu(x) = e^{\int x dx} = e^{\frac{1}{2}x^2}$。
3.  构造 []{.arithmatex}$g(x) = e^{\frac{x^2}{2}} f(x)$。
4.  求导：[]{.arithmatex}$g'(x) = e^{\frac{x^2}{2}}(xf(x) + f'(x)) > 0$。
5.  []{.arithmatex}$g(x)$ 单调递增。
6.  []{.arithmatex}$g(1) > g(0) \implies e^{1/2}f(1) > e^0 \cdot f(0) = 1$。
7.  []{.arithmatex}$f(1) > e^{-1/2}$。

#### 类型四：非齐次项的处理（广义积分因子） {#_14}

**题目**：[]{.arithmatex}$f'(x) - f(x) > e^{2x}$，且 []{.arithmatex}$f(0)=0$。

**解析**：

1.  积分因子：针对 []{.arithmatex}$f'(x) - f(x)$，因子是 []{.arithmatex}$e^{-x}$。

2.  两边同乘 []{.arithmatex}$e^{-x}$：

    :::: {.arithmatex}
    ::: {.MathJax_Preview}
    e\^{-x}f\'(x) - e\^{-x}f(x) \> e\^{2x} \cdot e\^{-x}
    :::

    $$e^{-x}f'(x) - e^{-x}f(x) > e^{2x} \cdot e^{-x}$$
    ::::

    :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \[e\^{-x}f(x)\]\' \> e\^x
    :::

    $$[e^{-x}f(x)]' > e^x$$
    ::::

3.  令 []{.arithmatex}$g(x) = e^{-x}f(x)$。此时 []{.arithmatex}$g'(x) > e^x$。

4.  这不再是简单的单调性，而是**导数有下界**。

5.  在 []{.arithmatex}$[0, x]$ 上对 []{.arithmatex}$g'(t)$ 积分：

    :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \int_0\^x g\'(t) dt \> \int_0\^x e\^t dt
    :::

    $$\int_0^x g'(t) dt > \int_0^x e^t dt$$
    ::::

    :::: {.arithmatex}
    ::: {.MathJax_Preview}
    g(x) - g(0) \> e\^x - 1
    :::

    $$g(x) - g(0) > e^x - 1$$
    ::::

6.  代入 []{.arithmatex}$g(0) = f(0) = 0$：

    :::: {.arithmatex}
    ::: {.MathJax_Preview}
    e\^{-x}f(x) \> e\^x - 1
    :::

    $$e^{-x}f(x) > e^x - 1$$
    ::::

    :::: {.arithmatex}
    ::: {.MathJax_Preview}
    f(x) \> e\^{2x} - e\^x
    :::

    $$f(x) > e^{2x} - e^x$$
    ::::

## 单调性 {#_15}

### 定义法求解 {#_16}

高中认为单调性即为严格单调性，定义法证明流程如下：

- 设 []{.arithmatex}$x_1<x_2\in D$ 其中 []{.arithmatex}$D$ 为定义域。

- 证明 []{.arithmatex}$f(x_1)-f(x_2)$ 的正负性，通常将式子化为关于 []{.arithmatex}$(x_1-x_2)$ 的式子。

- 声称 []{.arithmatex}$f(x_1)$ 大于或小于 []{.arithmatex}$f(x_2)$，得到单调性。

在高考情景下，定义法一般不常用，因为函数通常涉及到 []{.arithmatex}$e$ 和对数运算等稍显困难的函数。

### 导数法求解 {#_17}

容易知道，在区间 []{.arithmatex}$[a,b]$ 上：

- 如果 []{.arithmatex}$f'(x)>0$，那么函数单调递增。

- 如果 []{.arithmatex}$f'(x)<0$，那么函数单调递减。

- 如果 []{.arithmatex}$f'(x)=0$，那么函数为常函数。

注意，在高中阶段（默认下面的函数均可导）：

- 若函数 []{.arithmatex}$f(x)$ 在区间 []{.arithmatex}$D$ 上有 []{.arithmatex}$f'(x)>0$，则 []{.arithmatex}$f(x)$ 在 []{.arithmatex}$D$ 上单调递增。

- 若函数 []{.arithmatex}$f(x)$ 在区间 []{.arithmatex}$D$ 上单调递增，不能说明 []{.arithmatex}$f'(x)>0$，例如 []{.arithmatex}$f(x)=x^3$ 在 []{.arithmatex}$0$ 处导数为零。

- 若函数 []{.arithmatex}$f(x)$ 在区间 []{.arithmatex}$D$ 上单调递增，则 []{.arithmatex}$f'(x)\ge0$ 且所有使得 []{.arithmatex}$f'(x)=0$ 的点不能组成一个连续的区间，例如 []{.arithmatex}$f(x)=C$。

- 若函数 []{.arithmatex}$f(x)$ 在区间 []{.arithmatex}$D$ 上单调递增，且 []{.arithmatex}$f'(x)\ge0$，不能说明使得 []{.arithmatex}$f'(x)=0$ 的点是有限的，例如 []{.arithmatex}$f(x)=x-\sin x$。

- 在高中阶段，排除掉常函数，大部分函数都可以用 []{.arithmatex}$f'(x)\ge0$ 或 []{.arithmatex}$f'(x)\le0$ 判断单调性，例如 []{.arithmatex}$f(x) = \begin{cases} e^{-1/x} & \text{if } x > 0 \\ 0 & \text{if } x \le 0 \end{cases}$。

复合函数的单调性：满足同增异减，即单调性相同则为单增函数，单调性不同则为单减函数。

严格来说，一个连续函数在某一区间上的单调性，与其导函数符号之间的关系，是微积分中最核心但也最容易被"想当然"的地方。

为了表述极其严谨，我们先约定术语：

- **单调不减（Non-decreasing）**：对于 []{.arithmatex}$x_1 < x_2$，有 []{.arithmatex}$f(x_1) \le f(x_2)$。（允许局部平直）
- **严格单调递增（Strictly increasing）**：对于 []{.arithmatex}$x_1 < x_2$，有 []{.arithmatex}$f(x_1) < f(x_2)$。（不允许局部平直）

以下是它们之间的**严格对应关系**，以及极易犯错的 **5 个盲点**。

假设函数 []{.arithmatex}$f(x)$ 在区间 []{.arithmatex}$I$ 上**连续**，且在 []{.arithmatex}$I$ 的**内部（开区间）可导**：

1.  **判定"单调不减"的充要条件**：[]{.arithmatex}$f(x)$ 在 []{.arithmatex}$I$ 上单调不减 []{.arithmatex}$\iff$ 在 []{.arithmatex}$I$ 的内部，始终有 []{.arithmatex}$f'(x) \ge 0$。

2.  **判定"严格单调递增"的充分条件**：如果在 []{.arithmatex}$I$ 的内部，始终有 []{.arithmatex}$f'(x) > 0$，那么 []{.arithmatex}$f(x)$ 在 []{.arithmatex}$I$ 上严格单调递增。

3.  **判定"严格单调递增"的充要条件（终极法则）**：[]{.arithmatex}$f(x)$ 在 []{.arithmatex}$I$ 上严格单调递增 []{.arithmatex}$\iff$ 在 []{.arithmatex}$I$ 的内部，**[]{.arithmatex}**$f'(x) \ge 0$，且 []{.arithmatex}$f'(x)$ 在任何子区间上都不恒为 0。

盲点 1：认为"严格单调递增 []{.arithmatex}$\implies f'(x) > 0$" （大错特错！）

- **误区**：很多人认为，如果函数严格递增，那么它的导数一定大于 0。
- **正解**：严格递增的函数，其导数**可以等于 0**，只要等于 0 的点是孤立的即可。
- **经典反例**：[]{.arithmatex}$f(x) = x^3$。它在 []{.arithmatex}$(-\infty, +\infty)$ 上是严格单调递增的，但是在 []{.arithmatex}$x=0$ 处，它的导数 []{.arithmatex}$f'(0) = 0$。

盲点 2：遇到 []{.arithmatex}$f'(x) = 0$ 就觉得单调性被破坏了

- **误区**：解出 []{.arithmatex}$f'(x) \ge 0$，发现有无数个点使得 []{.arithmatex}$f'(x)=0$，就认为函数不是"严格"递增，只是"单调不减"。
- **正解**：只要 []{.arithmatex}$f'(x)=0$ 的点**没有连成一个区间**（即这些点是离散的、孤立的），函数依然是**严格单调递增**的。
- **经典反例**：[]{.arithmatex}$f(x) = x + \sin x$，其导数 []{.arithmatex}$f'(x) = 1 + \cos x \ge 0$。当 []{.arithmatex}$x = \pi, 3\pi, 5\pi\dots$ 时，[]{.arithmatex}$f'(x) = 0$。这里有无穷多个导数为 0 的点，但因为它们没有连成一片（不构成任何区间），所以 []{.arithmatex}$f(x) = x + \sin x$ 在 []{.arithmatex}$\mathbb{R}$ 上依然是**严格单调递增**的。

盲点 3：开区间与闭区间（端点问题）

- **误区**：求导只能在开区间求，所以单调区间只能写开区间 []{.arithmatex}$(a, b)$。
- **正解**：单调性是一个**整体性质**，只要函数在端点处**连续**，单调区间就**必须包含端点**。
- **经典例子**：[]{.arithmatex}$f(x) = \sqrt{x}$ 定义域是 []{.arithmatex}$[0, +\infty)$。导数 []{.arithmatex}$f'(x) = \frac{1}{2\sqrt{x}}$。显然，在开区间 []{.arithmatex}$(0, +\infty)$ 上 []{.arithmatex}$f'(x) > 0$。但是，因为 []{.arithmatex}$f(x)$ 在 []{.arithmatex}$x=0$ 处连续，所以它的单调递增区间是 **闭区间 []{.arithmatex}**$[0, +\infty)$，而不是 []{.arithmatex}$(0, +\infty)$。

盲点 4：不可导点会打断单调性

- **误区**：如果区间内有一个点不可导，就不能用导数判断单调性，或者必须把区间从不可导点处断开。
- **正解**：只要函数在整个区间上**连续**，个别不可导点**完全不影响**单调性的延伸。
- **经典例子**：[]{.arithmatex}$f(x) = \sqrt[3]{x}$ （即 []{.arithmatex}$x^{1/3}$）它在 []{.arithmatex}$x=0$ 处不可导（切线垂直于 x 轴，[]{.arithmatex}$f'(0)$ 为无穷大）。但在 []{.arithmatex}$(-\infty, 0)$ 和 []{.arithmatex}$(0, +\infty)$ 上，[]{.arithmatex}$f'(x) > 0$。因为 []{.arithmatex}$f(x)$ 在 []{.arithmatex}$x=0$ 处连续，所以它在整个 []{.arithmatex}$(-\infty, +\infty)$ 上严格单调递增，不需要在 0 处断开。

盲点 5：符号混乱（国内教材的特殊性）

- **误区**：对"单调递增"这个词的理解产生歧义。

- **说明**：在高等数学（如严格的数学分析）中，"单调递增"通常指 []{.arithmatex}$f(x_1) \le f(x_2)$（允许平直，英文叫 non-decreasing 或 monotonically increasing）。但在**中国的中学教材和部分考研数学**中，题目里常说的"单调递增"往往默认就是**"严格单调递增"**（不允许平直）。

  - **做题策略**：如果在国内高中或考研中遇到"已知 []{.arithmatex}$f(x)$ 在区间 []{.arithmatex}$I$ 上单调递增，求参数 []{.arithmatex}$a$ 的取值范围"，**正确的做法是令 []{.arithmatex}**$f'(x) \ge 0$ 恒成立，然后再去检验等号是否会在一个区间内成立（通常不会）。很多学生直接令 []{.arithmatex}$f'(x) > 0$，往往会**漏掉参数的边界值**。

总结口诀：

1.  **已知单调求参数**：闭眼写 []{.arithmatex}$f'(x) \ge 0$（千万别忘了等号），再排查恒为 0 的区间。
2.  **已知函数求单调**：求出 []{.arithmatex}$f'(x) > 0$ 的区间，若端点连续，果断带上端点（写成闭区间）。孤立的导数为 0 的点，直接跨过去，不影响严格单调。

### 题型总结式 {#_18}

#### 经典商形式 {#_19}

#### 经典积形式 {#_20}

#### 指对混合式 {#_21}

#### 双曲函数式 {#_22}

#### 复合函数式 {#_23}

### 凹凸性问题 {#_24}

容易知道，凹凸性可以由二阶导数反应，由于高中课本没有涉及，而且凹凸性的定义也有不同说法，我们只需要知道，二阶导数可以反应凹凸性即可。

另外，如果函数 []{.arithmatex}$f$ 在点 []{.arithmatex}$x_0$ 凹凸性改变，那么 []{.arithmatex}$x_0$ 是 []{.arithmatex}$f$ 的一个拐点。注意，如同驻点不一定是极值点，[]{.arithmatex}$f''(x_0)=0$ 不代表 []{.arithmatex}$x_0$ 一定是拐点。

根据凹凸性可以进行割线放缩，对于函数 []{.arithmatex}$f$ 在区间 []{.arithmatex}$[a,b]$ 上的割线 []{.arithmatex}$g$，如果 []{.arithmatex}$f$ 具有凹凸性，有 []{.arithmatex}$g(x)\ge f(x)$ 或 []{.arithmatex}$g(x)\le f(x)$ 恒成立。

利用凹凸形也可以用于解决一些有意思的问题，例如用凹凸形辅助必要性探路、极值点偏移等，以例题：已知函数 []{.arithmatex}$f(x)=axe^x-(a+1)(2x-1)$ 在 []{.arithmatex}$(0,\infty)$ 上 []{.arithmatex}$f(x)\ge0$ 恒成立，求实数 []{.arithmatex}$a$ 的取值范围。

对其求两次导数：

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x)=ae\^x(x+1)-2(a+1)
:::

$$f'(x)=ae^x(x+1)-2(a+1)$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'\'(x)=ae\^x(x+2)\>0
:::

$$f''(x)=ae^x(x+2)>0$$
::::

因此函数是凸的，同时我们注意到，取 []{.arithmatex}$x=\dfrac{1}{2}$ 或 []{.arithmatex}$x\to+\infty$，[]{.arithmatex}$a>0$ 是必然的，那么若要"刚好恒非负"的临界情形，必出现某点 []{.arithmatex}$x_0$ 使图像与 []{.arithmatex}$x$ 轴相切，列出式子：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x_0)=ax_0e\^{x_0}-(a+1)(2x_0-1)=0
:::

$$f(x_0)=ax_0e^{x_0}-(a+1)(2x_0-1)=0$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
ae\^{x_0}(x_0+1)-2(a+1)=0
:::

$$ae^{x_0}(x_0+1)-2(a+1)=0$$
::::

整理得：

:::: {.arithmatex}
::: {.MathJax_Preview}
a=\dfrac{2}{e\^{x_0}(x_0+1)-2}
:::

$$a=\dfrac{2}{e^{x_0}(x_0+1)-2}$$
::::

带入上式，也就是

:::: {.arithmatex}
::: {.MathJax_Preview}
a+1=\dfrac{ax_0e\^{x_0}}{2x_0-1}=\dfrac{e\^{x_0}(x_0+1)}{e\^{x_0}(x_0+1)-2}
:::

$$a+1=\dfrac{ax_0e^{x_0}}{2x_0-1}=\dfrac{e^{x_0}(x_0+1)}{e^{x_0}(x_0+1)-2}$$
::::

所以：

:::: {.arithmatex}
::: {.MathJax_Preview}
a=\dfrac{e\^{x_0}(x_0+1)}{e\^{x_0}(x_0+1)-2}\cdot\dfrac{2x_0-1}{x_0e\^{x_0}}
:::

$$a=\dfrac{e^{x_0}(x_0+1)}{e^{x_0}(x_0+1)-2}\cdot\dfrac{2x_0-1}{x_0e^{x_0}}$$
::::

所以：

:::: {.arithmatex}
::: {.MathJax_Preview}
2=\dfrac{(x_0+1)(2x_0-1)}{x_0}
:::

$$2=\dfrac{(x_0+1)(2x_0-1)}{x_0}$$
::::

因此 []{.arithmatex}$x_0=1$，反代得 []{.arithmatex}$a=\dfrac{1}{e-1}$，不妨验证充分性后直接下结论。

## 基本问题 {#_25}

### 极值问题 {#_26}

由费马引理，我们知道，若 []{.arithmatex}$x_0$ 为 []{.arithmatex}$f(x)$ 的极值点，那么一定有 []{.arithmatex}$f'(x)=0$。

但是，[]{.arithmatex}$f'(x)=0$ 仅仅是前命题的必要不充分条件，充分性不完全正确，例如对于 []{.arithmatex}$f(x)=x^3$，有 []{.arithmatex}$f'(0)=0$ 但是 []{.arithmatex}$x=0$ 仅仅是一个拐点。

其充分性有几种不同的说法：

- 第一充分条件：严谨的数学语言略，我们感性的理解，如果函数的导数在 []{.arithmatex}$x_0$ 处为零，且其左右一个大于零、一个小于零，那么 []{.arithmatex}$x_0$ 为 []{.arithmatex}$f(x)$ 的极值点。

- 第二充分条件：通过二阶导数，我们可以知道 []{.arithmatex}$f'(x)=0$ 且 []{.arithmatex}$f''(x)\neq0$，那么 []{.arithmatex}$x_0$ 为 []{.arithmatex}$f(x)$ 的极值点。

- 凹凸性条件：设函数 []{.arithmatex}$f$ 满足 []{.arithmatex}$f'(x_0)=0$ 且在 []{.arithmatex}$x_0$ 二阶可导，

  - 若 []{.arithmatex}$f''(x_0)>0$，则 []{.arithmatex}$x_0$ 为 []{.arithmatex}$f$ 的一个极小值点；
  - 若 []{.arithmatex}$f''(x_0)<0$，则 []{.arithmatex}$x_0$ 为 []{.arithmatex}$f$ 的一个极大值点。

但是注意，加上第一充分条件后，就是充分必要的；但是加上第二充分条件或者凹凸性条件，就不是必要的了，例如 []{.arithmatex}$f(x)=x^4$ 在 []{.arithmatex}$0$ 处二阶导为零，但是是一个极值点，具体的：

- 如果 []{.arithmatex}$f'(x_0)=0$ 且 []{.arithmatex}$f''(x_0)\neq0$，那么 []{.arithmatex}$x_0$ 一定是极值点。

- 如果 []{.arithmatex}$f'(x_0)=0$ 且其导函数左边为正、右边为负，则 []{.arithmatex}$x_0$ 一定是极大值点。

- 如果 []{.arithmatex}$f'(x_0)=0$ 且其导函数左边为负、右边为正，则 []{.arithmatex}$x_0$ 一定是极小值点。

- 如果 []{.arithmatex}$x_0$ 为 []{.arithmatex}$f(x)$ 极值点，那么一定满足 []{.arithmatex}$f'(x_0)=0$ 且为导函数变号点。

- 容易发现，因式分解后如果有一项的次数为偶数，那么在这里就是不变号的。

最值点：

- 最值点指的是区间或全局最大、最小的点的横坐标。

- 最值点一定是极值点，但是极值点不一定能是最值点。

- 求区间 []{.arithmatex}$[a,b]$ 上的最值点方法是，按照 []{.arithmatex}$f'(x_0)=0$ 找出所有可能的极值点（这不是充分的，但是必要就已经足够了），然后取最大或最小值。

还有另外的表述，可以拆绝对值推导：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \max\\a,b\\&=\dfrac{a+b}{2}+\dfrac{\|a-b\|}{2}\\ \min\\a,b\\&=\dfrac{a+b}{2}-\dfrac{\|a-b\|}{2} \end{aligned}
:::

$$\begin{aligned}
\max\{a,b\}&=\dfrac{a+b}{2}+\dfrac{|a-b|}{2}\\
\min\{a,b\}&=\dfrac{a+b}{2}-\dfrac{|a-b|}{2}
\end{aligned}$$
::::

### 交点问题 {#_27}

我们给出一个分段函数或周期函数的解析式，求一条直线与这个曲线的交点个数。

容易想到，我们做出图来，然后根据图像解决，注意，一定要小心有的时候直线可能会与曲线凸出来的部分相交或相切，而不一定是在拐点上，如图。

![alt text](../image-7.avif){width="60%"}

虽然交点个数往往可以转化为零点问题，但是这类问题往往在代数上很难算，只能数形结合，简化问题后再带入计算。

有的时候，我们遇到的问题是曲线与曲线的交点，此时有一种简单方法是，等式两边同时乘除 []{.arithmatex}$x$，也许可以将问题转化为直线与曲线的交点。

根据极限思想：[]{.arithmatex}$f(x)$，[]{.arithmatex}$g(x)$ 是连续函数，若 []{.arithmatex}$f(x_0) > g(x_0)$，则在以 []{.arithmatex}$x_0$ 为中心的一个很小的区间内，都有 []{.arithmatex}$f(x) > g(x)$。它告诉我们，只需判断在一点处的大小，就能知道在一小段区间内的大小。

1.  若 []{.arithmatex}$f(x_0) = g(x_0)$ 且 []{.arithmatex}$f'(x_0) > g'(x_0)$，则在 []{.arithmatex}$x_0$ 左边的一个小区间内有 []{.arithmatex}$f(x) < g(x)$，在 []{.arithmatex}$x_0$ 右边的一个小区间内有 []{.arithmatex}$f(x) > g(x)$。

2.  若 []{.arithmatex}$f(x_0) = g(x_0)$ 且 []{.arithmatex}$f'(x_0) < g'(x_0)$，则在 []{.arithmatex}$x_0$ 左边的一个小区间内有 []{.arithmatex}$f(x) > g(x)$，在 []{.arithmatex}$x_0$ 右边的一个小区间内有 []{.arithmatex}$f(x) < g(x)$。

### 图像绘制 {#_28}

其中，曲线的渐近线是当 []{.arithmatex}$x$ 坐标或 []{.arithmatex}$y$ 坐标或两者同时趋于无穷大时，与该曲线距离趋于 []{.arithmatex}$0$ 的直线。

- 直线 []{.arithmatex}$x = x_{0}$ 是曲线 []{.arithmatex}$y = f(x)$ 的垂直渐近线，当且仅当

  []{.arithmatex}$\lim\limits_{x \to x_{0}^{-}} f(x) = \infty$ 或 []{.arithmatex}$\lim\limits_{x \to x_{0}^{+}} f(x) = \infty$

- 直线 []{.arithmatex}$y = b$ 是曲线 []{.arithmatex}$y = f(x)$ 的水平渐近线，当且仅当

  []{.arithmatex}$\lim\limits_{x \to +\infty} f(x) = b$ 或 []{.arithmatex}$\lim\limits_{x \to -\infty} f(x) = b$

- 直线 []{.arithmatex}$y = ax + b (a \ne 0)$ 是曲线 []{.arithmatex}$y = f(x)$ 的斜渐近线，当且仅当

  []{.arithmatex}$\lim\limits_{x \to +\infty} [f(x) - (ax + b)] = 0$ 或 []{.arithmatex}$\lim\limits_{x \to -\infty} [f(x) - (ax + b)] = 0$

一般来说，函数图像的绘制有以下步骤：

1.  确定函数的定义域；
2.  确定函数的对称性与周期性；
3.  确定函数的渐近线；
4.  计算导数，确定函数的单调区间和极值点；
5.  计算二阶导数，确定函数的凹凸区间和拐点。

通过导数，我们可以判断函数的单调性与凹凸性，从而就能粗略地绘制出函数的图像。

### 任意存在 {#_29}

存在型：

- 若存在 []{.arithmatex}$x\in D$，使得 []{.arithmatex}$f(x)>m$，则 []{.arithmatex}$f(x)_{\max}>m$。

- 若存在 []{.arithmatex}$x\in D$，使得 []{.arithmatex}$f(x)<m$，则 []{.arithmatex}$f(x)_{\min}<m$。

简单组合型：

- 对任意的 []{.arithmatex}$x_1 \in A$，存在 []{.arithmatex}$x_2 \in B$，使得 []{.arithmatex}$f(x_1) = g(x_2)$，则 []{.arithmatex}$f(x)$ 的值域是 []{.arithmatex}$g(x)$ 值域的子集，即 []{.arithmatex}$f(A) \subseteq g(B)$。
- 存在 []{.arithmatex}$x_1 \in A$，存在 []{.arithmatex}$x_2 \in B$ 使得 []{.arithmatex}$f(x_1) = g(x_2)$，则 []{.arithmatex}$f(x)$ 的值域与 []{.arithmatex}$g(x)$ 值域有非空交集，即 []{.arithmatex}$f(A) \cap g(B) \ne \varnothing$。

任意与存在：

- 任意的 []{.arithmatex}$x_1 \in A$，任意的 []{.arithmatex}$x_2 \in B$ 使得 []{.arithmatex}$f(x_1) \le g(x_2)$，则 []{.arithmatex}$f(x)_{\max} \le g(x)_{\min}$；

- 任意的 []{.arithmatex}$x_1 \in A$，任意的 []{.arithmatex}$x_2 \in B$ 使得 []{.arithmatex}$f(x_1) \ge g(x_2)$，则 []{.arithmatex}$f(x)_{\min} \ge g(x)_{\max}$。

- 对任意的 []{.arithmatex}$x_1 \in A$，存在 []{.arithmatex}$x_2 \in B$ 使得 []{.arithmatex}$f(x_1) \le g(x_2)$，则 []{.arithmatex}$f(x)_{\max} \le g(x)_{\max}$；

- 对任意的 []{.arithmatex}$x_1 \in A$，存在 []{.arithmatex}$x_2 \in B$ 使得 []{.arithmatex}$f(x_1) \ge g(x_2)$，则 []{.arithmatex}$f(x)_{\min} \ge g(x)_{\min}$。

- 存在 []{.arithmatex}$x_1 \in A$，存在 []{.arithmatex}$x_2 \in B$ 使得 []{.arithmatex}$f(x_1) \le g(x_2)$，则 []{.arithmatex}$f(x)_{\min} \le g(x)_{\max}$；

- 存在 []{.arithmatex}$x_1 \in A$，存在 []{.arithmatex}$x_2 \in B$ 使得 []{.arithmatex}$f(x_1) \ge g(x_2)$，则 []{.arithmatex}$f(x)_{\max} \ge g(x)_{\min}$。

绝对值问题：

- 对任意的 []{.arithmatex}$x_1 \in A$，任意的 []{.arithmatex}$x_2 \in B$ 有 []{.arithmatex}$|f(x_1) - g(x_2)| \le a$，等价于 []{.arithmatex}$g(x)_{\max} - f(x)_{\min} \le a$ 且 []{.arithmatex}$f(x)_{\max} - g(x)_{\min} \le a$。

- 对任意的 []{.arithmatex}$x_1 \in A$，任意的 []{.arithmatex}$x_2 \in B$ 有 []{.arithmatex}$|f(x_1) - g(x_2)| \ge a$，等价于 []{.arithmatex}$g(x)_{\min} - f(x)_{\max} \ge a$ 或 []{.arithmatex}$f(x)_{\min} - g(x)_{\max} \ge a$。

- 若存在 []{.arithmatex}$x_1 \in A$，存在 []{.arithmatex}$x_2 \in B$ 使得 []{.arithmatex}$|f(x_1) - g(x_2)| \le a$，等价于 []{.arithmatex}$g(x)_{\min} - f(x)_{\max} \le a$ 且 []{.arithmatex}$f(x)_{\min} - g(x)_{\max} \le a$。

- 若存在 []{.arithmatex}$x_1 \in A$，存在 []{.arithmatex}$x_2 \in B$ 使得 []{.arithmatex}$|f(x_1) - g(x_2)| \ge a$，等价于 []{.arithmatex}$g(x)_{\max} - f(x)_{\min} \ge a$ 或 []{.arithmatex}$f(x)_{\max} - g(x)_{\min} \ge a$。

- 若存在 []{.arithmatex}$x_1, x_2 \in A$，有 []{.arithmatex}$|f(x_1) - f(x_2)| \ge a$，等价于 []{.arithmatex}$f(x)_{\max} - f(x)_{\min} \ge a$。

- 对任意 []{.arithmatex}$x_1 \in A$，存在 []{.arithmatex}$x_2 \in B$ 使得 []{.arithmatex}$|f(x_1) - g(x_2)| \le a$，等价于 []{.arithmatex}$g(x)_{\min} - a \le f(x)_{\min}$ 且 []{.arithmatex}$f(x)_{\max} \le a + g(x)_{\max}$。

- 对任意 []{.arithmatex}$x_1 \in A$，存在 []{.arithmatex}$x_2 \in B$ 使得 []{.arithmatex}$|f(x_1) - g(x_2)| \ge a$，等价于 []{.arithmatex}$g(x)_{\max} - f(x)_{\max} \ge a$ 或 []{.arithmatex}$f(x)_{\min} - g(x)_{\min} \ge a$。

### 零点个数 {#_30}

零点存在性定理：在 []{.arithmatex}$[a,b]$ 连续的函数若 []{.arithmatex}$f(a)f(b)<0$，则在 []{.arithmatex}$(a,b)$ 中至少存在一个零点。

- 若 []{.arithmatex}$f(x)$ 在区间 []{.arithmatex}$(a,b)$ 上有零点且单调，则零点唯一。

- 若 []{.arithmatex}$f(x)$ 在区间 []{.arithmatex}$(a,b)$ 上有唯一零点 []{.arithmatex}$x_0$ 且 []{.arithmatex}$f(a)f(b)>0$，则 []{.arithmatex}$f'(x_0)=0$。

判断函数的零点个数，首先确定所有的单调区间，然后在每一个单调区间上验证零点是否存在，而导数正好可以求出所有的极值点，容易想到，我们对函数求导。由于每个单调区间上至多有一个零点，所以零点的个数不超过单调区间的个数。

判断函数 []{.arithmatex}$f(x)$ 在区间 []{.arithmatex}$(a, b)$ 上零点个数的基本步骤：

1.  首先查看函数 []{.arithmatex}$f(x)$ 是否在 []{.arithmatex}$(a, b)$ 的某个子区间上恒为正或恒为负，若存在，则将其排除；然后研究 []{.arithmatex}$f(x)$ 在剩余区间上的单调性（通过导函数的正负去判断）。
2.  若步骤（1）无法确定函数 []{.arithmatex}$f(x)$ 的单调区间，则对导函数 []{.arithmatex}$f'(x)$ 重复步骤（1）的流程。
3.  在每一个单调区间上验证零点是否存在。

具体的，我们的一般解决思路如下：

......[]{.arithmatex}$f'''(x)$ 的符号 → []{.arithmatex}$f''(x)$ 的单调性（特殊点）

→ []{.arithmatex}$f''(x)$ 的符号 → []{.arithmatex}$f'(x)$ 的单调性（特殊点）

→ []{.arithmatex}$f'(x)$ 的符号 → []{.arithmatex}$f(x)$ 的单调性（特殊点）

→ []{.arithmatex}$f(x)$ 的符号、零点。

具体的，我们对函数不断求导，直到能轻松判断出来所有区间的恒正、恒负。

然后，我们先对端点进行判断，判断端点是不是零点，假设要求的区间是 []{.arithmatex}$(a,b)$ 然后列出：

:::: {.arithmatex}
::: {.MathJax_Preview}
\dots,\begin{cases} f\'\'\'(a)&=0\\ f\'\'\'(b)&=0\\ \end{cases},\begin{cases} f\'\'(a)&=0\\ f\'\'(b)&=0\\ \end{cases},\begin{cases} f\'(a)&=0\\ f\'(b)&=0\\ \end{cases}
:::

$$\dots,\begin{cases}
f'''(a)&=0\\
f'''(b)&=0\\
\end{cases},\begin{cases}
f''(a)&=0\\
f''(b)&=0\\
\end{cases},\begin{cases}
f'(a)&=0\\
f'(b)&=0\\
\end{cases}$$
::::

解出对应的 []{.arithmatex}$x$ 后，按照这些 []{.arithmatex}$x$ 将区间 []{.arithmatex}$(a,b)$ 分类讨论，就可以比较容易的判断出每一个区间的函数、导函数及其导函数的单调性、符号了。

例题：已知 []{.arithmatex}$f(x)=e^x-ex-a(x^2-x)$ 在 []{.arithmatex}$(0,1)$ 上有零点，求 []{.arithmatex}$a$ 的取值范围。

首先，我们发现 []{.arithmatex}$f(0)=1,f(1)=0$。

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} f\'(x)&=e\^x-e-a(2x-1)\\ f\'\'(x)&=e\^x-2a \end{aligned}
:::

$$\begin{aligned}
f'(x)&=e^x-e-a(2x-1)\\
f''(x)&=e^x-2a
\end{aligned}$$
::::

- 令 []{.arithmatex}$f'(0)=0$，解得 []{.arithmatex}$a=e-1$。

- 令 []{.arithmatex}$f'(1)=0$，解得 []{.arithmatex}$a=0$。

- 令 []{.arithmatex}$f''(0)=0$，解得 []{.arithmatex}$a=\dfrac{1}{2}$。

- 令 []{.arithmatex}$f''(1)=0$，解得 []{.arithmatex}$a=\dfrac{e}{2}$。

按照这几个点将函数分为 []{.arithmatex}$5$ 段分类讨论，每一段都可以知道二阶导数的正负和一阶导数的单调性，再根据端点的一阶导数正负、函数的端点值，即可判断函数 []{.arithmatex}$f(x)$ 是否有零点，一定可以判断出零点个数，注意开闭区间即可。

### 内点效应 {#_31}

找一个点满足 []{.arithmatex}$f(x)-g(x)>0$，我们将其转化为 []{.arithmatex}$f(x)>g(x)$，然后在里面插入一个 []{.arithmatex}$\alpha\in(g(x),f(x))$ 使得 []{.arithmatex}$f(x)>\alpha>g(x)$，然后解方程组

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases}f(x)&\>\alpha\\ g(x)&\<\alpha\end{cases}
:::

$$\begin{cases}f(x)&>\alpha\\ g(x)&<\alpha\end{cases}$$
::::

其中 []{.arithmatex}$\alpha$ 可以任意选，但一般挑选一个合适的数，我们就可以在解集内任意找一个使得 []{.arithmatex}$f(x)-g(x)>0$ 的 []{.arithmatex}$x$ 了。

内点效应的威力在于它将一个不可解的不等式分成若干个可解的不等式，只需要把我们的分析倒过来写就可以了。

同时，内点效应的意义还在于，我们通常写的，当 []{.arithmatex}$x$ 趋近于多少，[]{.arithmatex}$f(x)$ 大于或小于多少，这种不能在高中的步骤中出现，因此我们可以根据内点效应，直接找到一个满足的点，再根据单调性，得出这种类似的结论。

### 近似零点 {#_32}

而导数还可以用于找零点的近似值，称为牛顿迭代法：初始时我们从给定的 []{.arithmatex}$f(x)$ 和一个近似解 []{.arithmatex}$x_0$ 开始（初值的问题与 Newton 分形有关，可参考 3Blue1Brown 的 [牛顿分形](https://www.bilibili.com/video/BV1HQ4y1q78v/)。

假设我们目前的近似解是 []{.arithmatex}$x_i$，我们画出与 []{.arithmatex}$f(x)$ 切于点 []{.arithmatex}$(x_i,f(x_i))$ 的直线 []{.arithmatex}$l$，将 []{.arithmatex}$l$ 与 []{.arithmatex}$x$ 轴的交点横坐标记为 []{.arithmatex}$x_{i+1}$，那么这就是一个更优的近似解。重复这个迭代的过程。

![alt text](../image-5.avif){width="60%"}

根据导数的几何意义，可以得到如下关系：

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x_i) = \frac{f(x_i)}{x\_{i} - x\_{i+1}}
:::

$$f'(x_i) = \frac{f(x_i)}{x_{i} - x_{i+1}}$$
::::

整理后得到如下递推式：

:::: {.arithmatex}
::: {.MathJax_Preview}
x\_{i+1} = x_i - \frac{f(x_i)}{f\'(x_i)}
:::

$$x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}$$
::::

直观地说，如果 []{.arithmatex}$f(x)$ 比较平滑，那么随着迭代次数的增加，[]{.arithmatex}$x_i$ 会越来越逼近方程的解。

牛顿迭代法的收敛率是平方级别的，这意味着每次迭代后近似解的精确数位会翻倍。关于牛顿迭代法的收敛性证明可参考 [citizendium - Newton method Convergence analysis](http://en.citizendium.org/wiki/Newton%27s_method#Convergence_analysis)。当然牛顿迭代法也同样存在着缺陷，详情参考 [Xiaolin Wu - Roots of Equations 第 []{.arithmatex}](https://www.ece.mcmaster.ca/~xwu/part2.pdf)$18 \\sim 20$ 页分析。
