# 简单函数 {#_1}

## 函数的概念 {#_2}

### 定义 {#_3}

函数是一个定义域 []{.arithmatex}$A$ 到值域 []{.arithmatex}$B$ 的映射关系，函数的定义域和值域是一个集合，对于定义域内的每一个数，有且仅有值域内的一个数与之对应，记为 []{.arithmatex}$f:A\to B$。

注意，定义域的是所有函数值的集合，是陪域的一个子集，严格来说函数是定义域到陪域的映射关系，只是陪域内的数，不一定是有效的函数值，只有值域内的数才是有效的函数值。

1.  函数的定义域就是能使解析式有意义的所有实数勿的集合，自然定义域是式子本身所要求的定义域。
2.  不要轻易对解析式进行化简变形，以免定义域发生变化。
3.  当一个函数由两个或两个以上代数式的和、差、积、商的形式构成时，定义域是使得各式子都有意义的公共部分、且（若有）分式有意义的集合。

复合函数：如果 []{.arithmatex}$g$ 的值域为 []{.arithmatex}$f$ 的定义域的子集，那么定义 []{.arithmatex}$y=(f\circ g)(x)=f(g(x))$。

### 解析式 {#_4}

已知函数 []{.arithmatex}$f$ 的一些关系式，求 []{.arithmatex}$f(x)$，最常用的是换元法和变形法，例如：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x+1)=x\^2
:::

$$f(x+1)=x^2$$
::::

换元法，设 []{.arithmatex}$t=x+1$，则：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(t)=(t-1)\^2=t\^2-2t+1
:::

$$f(t)=(t-1)^2=t^2-2t+1$$
::::

如果给出多个 []{.arithmatex}$f$ 的值，且自变量有对称性，那么对称联立，例如给出上式：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} 3f(x)+2f(-x)&=x+3\\ 3f(-x)+2f(x)&=-x+3 \end{cases}
:::

$$\begin{cases}
3f(x)+2f(-x)&=x+3\\
3f(-x)+2f(x)&=-x+3
\end{cases}$$
::::

类似的还有 []{.arithmatex}$x$ 与 []{.arithmatex}$1/x$ 等。

由多个子函数分段定义的函数称为分段函数，如绝对值函数：

:::: {.arithmatex}
::: {.MathJax_Preview}
\|x\|=\begin{cases} x&x\ge0\\ -x&x\<0 \end{cases}
:::

$$|x|=\begin{cases}
x&x\ge0\\
-x&x<0
\end{cases}$$
::::

分段函数的定义域是各段函数定义域的并集，值域是各段函数值域的并集。

符号函数是一种常用的分段函数：

:::: {.arithmatex}
::: {.MathJax_Preview}
\op{sgn}x=\begin{cases} 1&x\>0\\ 0&x=0\\ -1&x\<0 \end{cases}
:::

$$\op{sgn}x=\begin{cases}
1&x>0\\
0&x=0\\
-1&x<0
\end{cases}$$
::::

### 反函数 {#_5}

对于二元关系 []{.arithmatex}$(f:X\rightarrow Y)$ 和 []{.arithmatex}$(g:Y\rightarrow X)$，若 []{.arithmatex}$(\forall x\in X)\{g[f(x)]=x\}$ 且 []{.arithmatex}$(\forall y\in Y)\{f[g(y)]=y\}$，则称 []{.arithmatex}$g$ 为 []{.arithmatex}$f$ 的反函数，记为 []{.arithmatex}$f^{-1}$。

设 []{.arithmatex}$f$ 表示一个函数，其定义域为 []{.arithmatex}$X$、陪域为 []{.arithmatex}$Y$，若存在一函数 []{.arithmatex}$g$，其定义域为 []{.arithmatex}$Y$、陪域为 []{.arithmatex}$X$，且对于 []{.arithmatex}$x\in X$ 有 []{.arithmatex}$g(f(x))=x$、对于任意 []{.arithmatex}$y\in Y$ 有 []{.arithmatex}$f(g(y))=y$，则称 []{.arithmatex}$g$ 为 []{.arithmatex}$f$ 的反函数。

函数 []{.arithmatex}$f$ 的反函数记为 []{.arithmatex}$f^{-1}$，注意此处的 []{.arithmatex}$-1$（次方的写法）并不是 []{.arithmatex}$-1$ 次方，比如 []{.arithmatex}$\sin$ 的反函数 []{.arithmatex}$\arcsin$ 也记为 []{.arithmatex}$\sin^{-1}$。

单调函数总是有反函数，并且反函数的单调性与原函数一致，原函数与反函数的图像关于函数 []{.arithmatex}$y=x$ 的图像对称。

水平线测试：

- 在数学里，水平线测试为一测试方法，用来判断一函数是否为单射、满射或双射。

- 设一带有图像的函数为 []{.arithmatex}$f:X\rightarrow Y$，接着使用 []{.arithmatex}$X\times Y$ 上的水平线：

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  y_0\in Y,\\ \\\langle x,y_0\rangle\in f\mid x\in X\\
  :::

  $$y_0\in Y,\ \{\langle x,y_0\rangle\in f\mid x\in X\}$$
  ::::

  若函数为单射，则其图像绝不会和任何一条水平线相交超过一次。

  若函数为满射，则每一水平线和图像至少相交一次。

  若函数为双射，则每一水平线和图像相交于一点且只有一点。

求反函数：记 []{.arithmatex}$g$ 表示函数 []{.arithmatex}$f$ 的反函数，那么从图像的角度考虑，若 []{.arithmatex}$\langle x,y\rangle\in f$，那么 []{.arithmatex}$\langle y,x\rangle\in g$，因此，我们对于 []{.arithmatex}$y=f(x)=\dots x$，只需要将 []{.arithmatex}$x,y$ 互换，得到的就是反函数的解析式。当然也不能写 []{.arithmatex}$x=\dots y$ 的形式，要化为 []{.arithmatex}$y=\dots x$ 的形式。

例题：求 []{.arithmatex}$f(x)=2x+1$ 的反函数。答案：有 []{.arithmatex}$y=f(x)=2x+1$；交换 []{.arithmatex}$x,y$，即 []{.arithmatex}$x=g(y)=2y+1$；整理，得 []{.arithmatex}$y=g(y)=\dfrac{1}{2}x-\dfrac{1}{2}$。

### 朗博 W 函数 {#w}

我们将朗博 []{.arithmatex}$W$ 函数定义为 []{.arithmatex}$f(x)=xe^x$ 的反函数。

也就是说，有关方程 []{.arithmatex}$\displaystyle xe^x=a$ 可以给出通解

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} W_0(a)&a\ge-\frac{1}{e}\\ W\_{-1}(a)&a\in\left(-\dfrac{1}{e},0\right) \end{cases}
:::

$$\begin{cases}
W_0(a)&a\ge-\frac{1}{e}\\
W_{-1}(a)&a\in\left(-\dfrac{1}{e},0\right)
\end{cases}$$
::::

但是 []{.arithmatex}$W(x)$ 没有初等意义的解析式，只有积分式。

- 将定义域限制在 []{.arithmatex}$\displaystyle\left[-\frac{1}{e},+\infty\right)$ 上，取其在 []{.arithmatex}$[-1,+\infty)$ 上的函数值，那么就定义了一个单调递增的函数 []{.arithmatex}$W
  _0(x)$；

- 将定义域限制在 []{.arithmatex}$\displaystyle\left(-\frac{1}{e},0\right)$ 上，取其在 []{.arithmatex}$(-\infty,-1)$ 上的函数值，那么就定义了一个单调递减的函数 []{.arithmatex}$W_{-1}(x)$.

![](../Mplwp_lambert_W_branches.svg)

性质：当 []{.arithmatex}$a\geq 0$ 时，[]{.arithmatex}${W(x)\cdot e^{W(x)}=x}$，此外可以推出

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} x\ln x=a&\implies x=e\^{W(a)}\\ x+\ln x=a&\implies x=W(e\^a)\\ \frac{\ln x}{x}=-a&\implies x=e\^{-W(a)} \end{aligned}
:::

$$\begin{aligned}
x\ln x=a&\implies x=e^{W(a)}\\
x+\ln x=a&\implies x=W(e^a)\\
\frac{\ln x}{x}=-a&\implies x=e^{-W(a)}
\end{aligned}$$
::::

以及朗博不等式，可以同构证明：[]{.arithmatex}${xe^x\geq x+\ln x+1}$

## 初等函数 {#_6}

- 正比例函数：[]{.arithmatex}$f(x+y)=f(x)+f(y)$。

- 幂型函数：[]{.arithmatex}$f(xy)=f(x)f(y)$。

- 对数型函数：[]{.arithmatex}$f(xy)=f(x)+f(y)$。

- 指数形函数：[]{.arithmatex}$f(x+y)=f(x)f(y)$。

### 幂函数 {#_7}

形如 []{.arithmatex}$y=x^\alpha$（通常认为 []{.arithmatex}$\alpha\neq0$），有性质：

- 函数恒过 []{.arithmatex}$(1,1)$ 点。

- 如果 []{.arithmatex}$\alpha>0$，那么函数恒过 []{.arithmatex}$(0,0)$.

- 如果 []{.arithmatex}$\alpha\in\Z^+$，那么函数有奇偶性，与 []{.arithmatex}$\alpha$ 的奇偶性相同。

- 在 []{.arithmatex}$(0,\infty)$ 上函数奇偶性与 []{.arithmatex}$\alpha$ 关于 []{.arithmatex}$1$ 的大小有关。

有幂的性质：

:::: {.arithmatex}
::: {.MathJax_Preview}
a\^{\frac{m}{n}}=\sqrt\[n\]{a\^m}=\sqrt\[n\]{a}\^m
:::

$$a^{\frac{m}{n}}=\sqrt[n]{a^m}=\sqrt[n]{a}^m$$
::::

其中 []{.arithmatex}$n,m$ 均为正数且不同奇偶。

:::: {.arithmatex}
::: {.MathJax_Preview}
a\^{-x}=\dfrac{1}{a\^x}
:::

$$a^{-x}=\dfrac{1}{a^x}$$
::::

这一条经常用于简化除法的求导，转化为乘法可以更方便。

:::: {.arithmatex}
::: {.MathJax_Preview}
\sqrt{a\pm\sqrt{b}}=\sqrt{a+\sqrt{a\^2-b}\over2}\pm\sqrt{a-\sqrt{a\^2-b}\over2}
:::

$$\sqrt{a\pm\sqrt{b}}=\sqrt{a+\sqrt{a^2-b}\over2}\pm\sqrt{a-\sqrt{a^2-b}\over2}$$
::::

对于自然数 []{.arithmatex}$a,b$，只有 []{.arithmatex}$a^2-b$ 是完全平方数的时候，才能开出来。

证明：我们设 []{.arithmatex}$\sqrt{a+\sqrt{b}}$ 化简完的结果是 []{.arithmatex}$\sqrt x+\sqrt y$：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \sqrt{a+\sqrt{b}}&=\sqrt x+\sqrt y\\ a+\sqrt{b}&=x+y+2\sqrt{xy} \end{aligned}
:::

$$\begin{aligned}
\sqrt{a+\sqrt{b}}&=\sqrt x+\sqrt y\\
a+\sqrt{b}&=x+y+2\sqrt{xy}
\end{aligned}$$
::::

因为 []{.arithmatex}$a$ 外面没有根号，与 []{.arithmatex}$x+y$ 相对应：

:::: {.arithmatex}
::: {.MathJax_Preview}
\left\\\begin{aligned} a&=x+y\\ \sqrt{b}&=2\sqrt{xy} \end{aligned}\right.
:::

$$\left\{\begin{aligned}
a&=x+y\\
\sqrt{b}&=2\sqrt{xy}
\end{aligned}\right.$$
::::

然后我们把下面的式子平方，可以写出方程组：

:::: {.arithmatex}
::: {.MathJax_Preview}
\left\\\begin{aligned} x+y&=a\\ xy&={b\over4} \end{aligned}\right.
:::

$$\left\{\begin{aligned}
x+y&=a\\
xy&={b\over4}
\end{aligned}\right.$$
::::

然后用公式：

:::: {.arithmatex}
::: {.MathJax_Preview}
\left\\\begin{aligned} x+y&=a\\ x-y&=\sqrt{(x+y)\^2-4xy}\\ &=\sqrt{a\^2-b} \end{aligned}\right.
:::

$$\left\{\begin{aligned}
x+y&=a\\
x-y&=\sqrt{(x+y)^2-4xy}\\
&=\sqrt{a^2-b}
\end{aligned}\right.$$
::::

或者设 []{.arithmatex}$t$ 满足：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} (t-x)(t-y)&=0\\ t\^2-(x+y)t+xy&=0 \end{aligned}
:::

$$\begin{aligned}
(t-x)(t-y)&=0\\
t^2-(x+y)t+xy&=0
\end{aligned}$$
::::

解这个方程，得到的 []{.arithmatex}$t$ 的两个根分别就是 []{.arithmatex}$x$ 和 []{.arithmatex}$y$。

具体的：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} t\^2-at+{b\over4}=0\\ t={a\pm\sqrt{a\^2-b}\over2} \end{aligned}
:::

$$\begin{aligned}
t^2-at+{b\over4}=0\\
t={a\pm\sqrt{a^2-b}\over2}
\end{aligned}$$
::::

解得：

:::: {.arithmatex}
::: {.MathJax_Preview}
\left\\\begin{aligned} x&={a+\sqrt{a\^2-b}\over2}\\ y&={a-\sqrt{a\^2-b}\over2} \end{aligned}\right.
:::

$$\left\{\begin{aligned}
x&={a+\sqrt{a^2-b}\over2}\\
y&={a-\sqrt{a^2-b}\over2}
\end{aligned}\right.$$
::::

因此：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} &\sqrt{a+\sqrt{b}}=\sqrt x+\sqrt y\\ =\\&\sqrt{a+\sqrt{a\^2-b}\over2}+\sqrt{a-\sqrt{a\^2-b}\over2} \end{aligned}
:::

$$\begin{aligned}
&\sqrt{a+\sqrt{b}}=\sqrt x+\sqrt y\\
=\;&\sqrt{a+\sqrt{a^2-b}\over2}+\sqrt{a-\sqrt{a^2-b}\over2}
\end{aligned}$$
::::

减法同理。

### 指数函数 {#_8}

形如 []{.arithmatex}$y=f(x)=a^x$（[]{.arithmatex}$a>0$ 且 []{.arithmatex}$a\neq1$），有性质：

- 恒过 []{.arithmatex}$(0,1)$ 点。

- 满足 []{.arithmatex}$f(x)\cdot f(-x)=1$。

指数函数非积非偶，换元常常先统一底数，例如：

:::: {.arithmatex}
::: {.MathJax_Preview}
4\^x+2\^{x+1}+3=(2\^x)\^2+2\cdot2\^x+3
:::

$$4^x+2^{x+1}+3=(2^x)^2+2\cdot2^x+3$$
::::

指数函数中，有一种函数特别重要：

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)=e\^x
:::

$$f(x)=e^x$$
::::

其中，[]{.arithmatex}$e$ 是一个无理数，近似值为 []{.arithmatex}$2.71828\dots$。

### 对数函数 {#_9}

若 []{.arithmatex}$a^x=n$（[]{.arithmatex}$a>0$ 且 []{.arithmatex}$a\neq1$），则记 []{.arithmatex}$x=\log_an$，其中 []{.arithmatex}$a$ 为底数，[]{.arithmatex}$n$ 为真数。

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} a\^{\log_ax}&=x\\ \log_aa\^x&=x \end{aligned}
:::

$$\begin{aligned}
a^{\log_ax}&=x\\
\log_aa^x&=x
\end{aligned}$$
::::

因此：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \log_a1&=0\\ \log_aa&=1\\ \end{aligned}
:::

$$\begin{aligned}
\log_a1&=0\\
\log_aa&=1\\
\end{aligned}$$
::::

对数也有一些特殊记号，例如：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \log_ex&=\ln x\\ \log_2x&=\operatorname{lb}x\\ \log\_{10}x&=\lg x \end{aligned}
:::

$$\begin{aligned}
\log_ex&=\ln x\\
\log_2x&=\operatorname{lb}x\\
\log_{10}x&=\lg x
\end{aligned}$$
::::

对数的运算法则与指数相对，如下：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \log_axy&=\log_ax+\log_ay&&\qquad&a\^xa\^y&=a\^{x+y}\\ \log_a\frac{x}{y}&=\log_ax-\log_ay&&\qquad&\frac{a\^x}{a\^y}&=a\^{x-y}\\ \log_ax\^y&=y\log_ax&&\qquad&(a\^x)\^y&=a\^{xy}\\ \log_a\sqrt\[y\]x&=\frac{\log_ax}y&&\qquad&\sqrt\[y\]x&=x\^\frac{1}{y} \end{aligned}
:::

$$\begin{aligned}
\log_axy&=\log_ax+\log_ay&&\qquad&a^xa^y&=a^{x+y}\\
\log_a\frac{x}{y}&=\log_ax-\log_ay&&\qquad&\frac{a^x}{a^y}&=a^{x-y}\\
\log_ax^y&=y\log_ax&&\qquad&(a^x)^y&=a^{xy}\\
\log_a\sqrt[y]x&=\frac{\log_ax}y&&\qquad&\sqrt[y]x&=x^\frac{1}{y}
\end{aligned}$$
::::

另外，还有换底公式，非常常用

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \log_ax&=\frac{\log_bx}{\log_ba}\\ \log_ax&=\frac{1}{\log_xa}\\ \log\_{a\^n}b&=\frac{\log_ab}{n} \end{aligned}
:::

$$\begin{aligned}
\log_ax&=\frac{\log_bx}{\log_ba}\\
\log_ax&=\frac{1}{\log_xa}\\
\log_{a^n}b&=\frac{\log_ab}{n}
\end{aligned}$$
::::

另外，还有：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} x\^{\log_ay}&=y\^{\log_ax}\\ \log_ab\log_bx&=\log_ax\\ \log_a\dfrac{1}{x}&=-\log_ax \end{aligned}
:::

$$\begin{aligned}
x^{\log_ay}&=y^{\log_ax}\\
\log_ab\log_bx&=\log_ax\\
\log_a\dfrac{1}{x}&=-\log_ax
\end{aligned}$$
::::

也就是说：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \log_am\log_bn&=\log_bm\log_an\\ \dfrac nm\log_ab&=\log\_{a\^m}b\^n=\log_ab\^{\frac nm} \end{aligned}
:::

$$\begin{aligned}
\log_am\log_bn&=\log_bm\log_an\\
\dfrac nm\log_ab&=\log_{a^m}b^n=\log_ab^{\frac nm}
\end{aligned}$$
::::
