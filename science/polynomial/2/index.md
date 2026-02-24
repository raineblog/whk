# 多项式科技 {#_1}

## 生成函数 {#_2}

序列 []{.arithmatex}$a$ （有穷无穷均可）的普通生成函数定义为形式幂级数：[]{.arithmatex}$\displaystyle F(x)=\sum_na_nx^n$。例如：

1.  []{.arithmatex}$a=\lang1,2,3\rang$ 的普通生成函数是 []{.arithmatex}$1+2x+3x^2$
2.  []{.arithmatex}$a=\lang1,1,1,\dots\rang$ 的普通生成函数是 []{.arithmatex}$\displaystyle\sum_{n\geq 0}x^n$
3.  []{.arithmatex}$a=\lang1,2,4,8,16,\dots\rang$ 的生成函数是 []{.arithmatex}$\displaystyle\sum_{n\geq 0}2^nx^n$
4.  []{.arithmatex}$a=\lang1,3,5,7,9\rang$ 的生成函数是 []{.arithmatex}$\displaystyle\sum_{n\geq 0}(2n+1)x^n$

换句话说，如果序列 []{.arithmatex}$a$ 有通项公式，那么它的普通生成函数的系数就是通项公式。

### 基本运算 {#_3}

两个序列 []{.arithmatex}$a,b$ 的生成函数 []{.arithmatex}$F(x),G(x)$，则 []{.arithmatex}$F(x)\pm G(x)$ 是序列 []{.arithmatex}$\lang a_n\pm b_n\rang$ 的生成函数。

:::: {.arithmatex}
::: {.MathJax_Preview}
F(x)\pm G(x)=\sum\_{n}(a_n\pm b_n)x\^n
:::

$$F(x)\pm G(x)=\sum_{n}(a_n\pm b_n)x^n$$
::::

乘法运算即卷积，推出 []{.arithmatex}$F(x)G(x)$ 是序列 []{.arithmatex}$\left\lang\displaystyle\sum_{i=0}^na_ib_{n-i}\right\rang$ 的生成函数。

:::: {.arithmatex}
::: {.MathJax_Preview}
F(x)G(x)=\sum_nx\^n\sum\_{i=0}\^na_ib\_{n-i}
:::

$$F(x)G(x)=\sum_nx^n\sum_{i=0}^na_ib_{n-i}$$
::::

#### 形式幂级数形式 []{.arithmatex}$\to$ 封闭形式 {#toto}

例如 []{.arithmatex}$a=\lang1,1,1,\dots\rang$ 的普通生成函数是 []{.arithmatex}$\displaystyle F(x)=\sum_{n\geq 0}x^n$，可以发现 []{.arithmatex}$F(x)x+1=F(x)$，于是解方程得到 []{.arithmatex}$\displaystyle F(x)=\frac{1}{1-x}$，这就是 []{.arithmatex}$\displaystyle\sum_{n\geq 0}x^n$ 的封闭形式。

又例如等比数列 []{.arithmatex}$\lang1,p,p^2,\dots\rang$ 的生成函数 []{.arithmatex}$F(x)=\displaystyle\sum_{n\geq 0}p^nx^n$，有 []{.arithmatex}$F(x)px+1=F(x)$ 得 []{.arithmatex}$F(x)=\displaystyle\frac{1}{1-px}$.

[]{.arithmatex}$a=\lang 1,0,1,0,1,\dots\rang$ 的 []{.arithmatex}$F(x)=\displaystyle\sum_{n\geq 0}x^{2n}=\frac{1}{1-x^2}$

[]{.arithmatex}$a=\lang 1,2,3,4,\dots\rang$ 的 []{.arithmatex}$F(x)=\displaystyle\sum_{n\geq 0}(n+1)x^n=\sum_{n\geq 0}(x^n)'=\left(\frac{1}{1-x}\right)'=\frac{1}{(1-x)^2}$

[]{.arithmatex}$a_n=\begin{pmatrix}m\\n\end{pmatrix}$ 的 []{.arithmatex}$F(x)=\displaystyle\sum_{n\geq 0}\begin{pmatrix}m\\n\end{pmatrix}x^n=(1+x)^m$

[]{.arithmatex}$Fib$ 数列定义为 []{.arithmatex}$a_0=0,a_1=1,a_n=a_{n-1}+a_{n-2}$，于是有

:::: {.arithmatex}
::: {.MathJax_Preview}
F(x)=xF(x)+x\^2F(x)-a_0x+a_1x+a_0\implies F(x)=\frac{x}{1-x-x\^2}
:::

$$F(x)=xF(x)+x^2F(x)-a_0x+a_1x+a_0\implies F(x)=\frac{x}{1-x-x^2}$$
::::

#### 应用 {#_4}

1.  在许多不同种类的食物中选出 []{.arithmatex}$n$ 个，计算方案数。每种食物的限制如下：

| 汉堡：偶数个 | 可乐：不超高一个 | 鸡腿：不超过两个 | 蜜桃多：奇数个 |
|:--:|:--:|:--:|:--:|
| 鸡块：[]{.arithmatex}$4$ 的倍数个 | 包子：不超过三个 | 土豆片炒肉：不超过一个 | 面包：[]{.arithmatex}$3$ 的倍数个 |

构造生成函数：

| []{.arithmatex}$\displaystyle\sum_{n\geq 0}x^{2n}=\frac{1}{1-x^2}$ | []{.arithmatex}$1+x$ | []{.arithmatex}$\displaystyle 1+x+x^2=\frac{1-x^3}{1-x}$ | []{.arithmatex}$\displaystyle\frac{x}{1-x^2}$ |
|:--:|:--:|:--:|:--:|
| []{.arithmatex}$\displaystyle\sum_{n\geq 0}x^{4n}=\frac{1}{1-x^4}$ | []{.arithmatex}$\displaystyle 1+x+x^2+x^3=\frac{1-x^4}{1-x}$ | []{.arithmatex}$1+x$ | []{.arithmatex}$\displaystyle\frac{1}{1-x^3}$ |

全部乘起来得到答案的生成函数：

:::: {.arithmatex}
::: {.MathJax_Preview}
F(x)=\frac{(1+x)(1-x\^3)x(1-x\^4)(1+x)}{(1-x\^2)(1-x)(1-x\^2)(1-x\^4)(1-x)(1-x\^3)}=\frac{x}{(1-x)\^4}=\sum\_{n\geq 1}\begin{pmatrix}n+2\\n-1\end{pmatrix}x\^n
:::

$$F(x)=\frac{(1+x)(1-x^3)x(1-x^4)(1+x)}{(1-x^2)(1-x)(1-x^2)(1-x^4)(1-x)(1-x^3)}=\frac{x}{(1-x)^4}=\sum_{n\geq 1}\begin{pmatrix}n+2\\n-1\end{pmatrix}x^n$$
::::

于是答案 []{.arithmatex}$=\begin{pmatrix}n+2\\n-1\end{pmatrix}=\begin{pmatrix}n+2\\3\end{pmatrix}$

1.  []{.arithmatex}$a_{n+1}+a_n=2^n,a_0=0$，求通项。

[]{.arithmatex}$f(x)=\displaystyle\sum_{n=0}^{+\infty}a_nx^n$，原式变为 []{.arithmatex}$x^{-1}(a_{n+1}x^{n+1})+a_nx^n=(2x)^n$，再求和有

:::: {.arithmatex}
::: {.MathJax_Preview}
\displaystyle\sum\_{n=0}\^{+\infty}x\^{-1}(a\_{n+1}x\^{n+1})+\sum\_{n=0}\^{+\infty}(a_nx\^n)=\sum\_{n=0}\^{+\infty}(2x)\^n=\frac{1}{1-2x}\implies (\frac{1}{x}+1)f(x)=\frac{1}{1-2x}
:::

$$\displaystyle\sum_{n=0}^{+\infty}x^{-1}(a_{n+1}x^{n+1})+\sum_{n=0}^{+\infty}(a_nx^n)=\sum_{n=0}^{+\infty}(2x)^n=\frac{1}{1-2x}\implies (\frac{1}{x}+1)f(x)=\frac{1}{1-2x}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
f(x)=\frac{x}{(1-2x)(1+x)}=\frac{1}{3}(\frac{1}{1-2x}-\frac{1}{1+x})=\frac{1}{3}\sum\_{n=0}\^{+\infty}\[2\^n-(-1)\^n\]x\^n
:::

$$f(x)=\frac{x}{(1-2x)(1+x)}=\frac{1}{3}(\frac{1}{1-2x}-\frac{1}{1+x})=\frac{1}{3}\sum_{n=0}^{+\infty}[2^n-(-1)^n]x^n$$
::::

于是 []{.arithmatex}$\displaystyle a_n=\frac{1}{3}[2^n-(-1)^n]$.

1.  卡特兰数：一个 []{.arithmatex}$n\times n$ 的方阵从 []{.arithmatex}$(0,0)$ 走到 []{.arithmatex}$(n,n)$，不经过对角线的方案数，记作 []{.arithmatex}$C_n$。

有如下关系：[]{.arithmatex}$C_n=\displaystyle\sum_{k=0}^nC_{n-k}C_k$，构造 []{.arithmatex}$f(x)=\displaystyle\sum_{n=0}^{+\infty}C_nx^n$，有

:::: {.arithmatex}
::: {.MathJax_Preview}
f\^2(x)=C_0\^2+(C_0C_1+C_1C_0)x+\dots\implies xf\^2(x)+C_0=f(x)\implies f(x)=\frac{1-\sqrt{1-4x} }{2x}
:::

$$f^2(x)=C_0^2+(C_0C_1+C_1C_0)x+\dots\implies xf^2(x)+C_0=f(x)\implies f(x)=\frac{1-\sqrt{1-4x} }{2x}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\implies f(x)=\frac{1-\left\\1+\displaystyle\sum\_{k=1}\^{+\infty}\left\[-2\begin{pmatrix}2k-2\\ k-1\end{pmatrix}\right\]x\^k\right\\}{2x}=\sum\_{k=0}\^{+\infty}\frac{\begin{pmatrix}2k\\k\end{pmatrix}x\^k}{k+1}\implies\red{\boxed{C_n=\frac{\begin{pmatrix}2n\\n\end{pmatrix}}{n+1}}}
:::

$$\implies f(x)=\frac{1-\left\{1+\displaystyle\sum_{k=1}^{+\infty}\left[-2\begin{pmatrix}2k-2\\ k-1\end{pmatrix}\right]x^k\right\}}{2x}=\sum_{k=0}^{+\infty}\frac{\begin{pmatrix}2k\\k\end{pmatrix}x^k}{k+1}\implies\red{\boxed{C_n=\frac{\begin{pmatrix}2n\\n\end{pmatrix}}{n+1}}}$$
::::
