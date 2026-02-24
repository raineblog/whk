# 微积分 {#_1}

![alt text](../image-6.avif)

## 积分 {#_2}

### 几何意义 {#_3}

如果在 []{.arithmatex}$[a,b](a\neq b)$ 上函数 []{.arithmatex}$f(x)$ 连续且恒有 []{.arithmatex}$f(x)\geq 0$，那么定积分 []{.arithmatex}$\displaystyle\int_{a}^{b}f(x)dx$ 表示由曲线 []{.arithmatex}$y=f(x)$ 以及直线 []{.arithmatex}$x=a,x=b,y=0$ 围成的曲边梯形的面积。

若 []{.arithmatex}$f(x)\leq 0$，那么定积分 []{.arithmatex}$\displaystyle\int_{a}^{b}f(x)dx$ 表示由曲线 []{.arithmatex}$y=f(x)$ 以及直线 []{.arithmatex}$x=a,x=b,y=0$ 围成的曲边梯形的面积的**负值**。

如果我们把 []{.arithmatex}$x$ 轴上方的面积赋予正号，下方的面积赋予负号，那么在一般情形下，定积分 []{.arithmatex}$\displaystyle\int_{a}^{b}f(x)dx$ 表示由曲线 []{.arithmatex}$y=f(x)$ 以及直线 []{.arithmatex}$x=a,x=b,y=0$ 围成的各部分图形面积的代数和。

### 微积分基本定理 / []{.arithmatex}$\mathrm{Newton-Leibniz}$ 牛顿 - 莱布尼兹公式 {#mathrmnewton-leibnizmathrmnewton-leibniz-}

以下设 []{.arithmatex}$C$ 是一个常数。

如果 []{.arithmatex}$f(x)$ 是 []{.arithmatex}$[a,b]$ 上的连续函数且 []{.arithmatex}$F'(x)=f(x)$，那么

:::: {.arithmatex}
::: {.MathJax_Preview}
\boxed{\int\_{a}\^{b}f(x)\\ dx=F(x)\|\_{a}\^{b}=F(b)-F(a) }
:::

$$\boxed{\int_{a}^{b}f(x)\ dx=F(x)|_{a}^{b}=F(b)-F(a) }$$
::::

我们称 []{.arithmatex}$F(x)$ 是 []{.arithmatex}$f(x)$ 的原函数。因为 []{.arithmatex}$[F(x)+C]'=f(x)$，所以 []{.arithmatex}$F(x)+C$ 也是 []{.arithmatex}$f(x)$ 的原函数。

常用定积分公式：

:::: {.arithmatex}
::: {.MathJax_Preview}
\int\_{a}\^{b}C\\ dx=Cx\|\_{a}\^{b}=Cb-Ca=C(b-a)
:::

$$\int_{a}^{b}C\ dx=Cx|_{a}^{b}=Cb-Ca=C(b-a)$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\int\_{a}\^{b}x\^n\\ dx=\frac{1}{n+1}x\^{n+1}\|\_{a}\^{b}=\frac{1}{n+1}b\^{n+1}-\frac{1}{n+1}a\^{n+1}=\frac{b\^{n+1}-a\^{n+1} }{n+1}
:::

$$\int_{a}^{b}x^n\ dx=\frac{1}{n+1}x^{n+1}|_{a}^{b}=\frac{1}{n+1}b^{n+1}-\frac{1}{n+1}a^{n+1}=\frac{b^{n+1}-a^{n+1} }{n+1}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\int_a\^b\sin x\\ dx=(-\cos x)\|\_a\^b=-\cos b+\cos a
:::

$$\int_a^b\sin x\ dx=(-\cos x)|_a^b=-\cos b+\cos a$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\int_a\^b\cos x\\ dx=\sin x\|\_a\^b=\sin b-\sin a
:::

$$\int_a^b\cos x\ dx=\sin x|_a^b=\sin b-\sin a$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\int_a\^b\frac{1}{x}\\ dx=\ln x\|\_a\^b=\ln b-\ln a=\ln\frac{b}{a}
:::

$$\int_a^b\frac{1}{x}\ dx=\ln x|_a^b=\ln b-\ln a=\ln\frac{b}{a}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\int_a\^b e\^x\\ dx=e\^x\|\_a\^b=e\^b-e\^a
:::

$$\int_a^b e^x\ dx=e^x|_a^b=e^b-e^a$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\int_a\^b n\^x\\ dx=\frac{n\^x}{\ln n}\|\_a\^b=\frac{n\^b}{\ln b}-\frac{n\^a}{\ln a}
:::

$$\int_a^b n^x\ dx=\frac{n^x}{\ln n}|_a^b=\frac{n^b}{\ln b}-\frac{n^a}{\ln a}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\int_L\^R \frac{cx+d}{ax+b}\\ dx=\frac{cx}{a}+(\frac{d}{a}-\frac{bc}{a\^2})\times\ln\|ax+b\|\\ \|\_L\^R
:::

$$\int_L^R \frac{cx+d}{ax+b}\ dx=\frac{cx}{a}+(\frac{d}{a}-\frac{bc}{a^2})\times\ln|ax+b|\ |_L^R$$
::::

#### 定积分的基本性质 {#_4}

1.  :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \int_a\^b Cf(x)\\ dx=C\int_a\^b f(x)\\ dx
    :::

    $$\int_a^b Cf(x)\ dx=C\int_a^b f(x)\ dx$$
    ::::

2.  :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \int_a\^b\[f(x)\pm g(x)\]\\ dx=\int_a\^b f(x)\\ dx\pm\int_a\^b g(x)\\ dx
    :::

    $$\int_a^b[f(x)\pm g(x)]\ dx=\int_a^b f(x)\ dx\pm\int_a^b g(x)\ dx$$
    ::::

3.  :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \int_a\^b f(x)\\ dx=\int_a\^c f(x)\\ dx+\int_c\^b f(x)\\ dx
    :::

    $$\int_a^b f(x)\ dx=\int_a^c f(x)\ dx+\int_c^b f(x)\ dx$$
    ::::

4.  在区间 []{.arithmatex}$[a,b]$ 上满足 []{.arithmatex}$f(x)\geq 0$，则 \$[]{.arithmatex}$\int_a^b f(x)\ dx\geq 0$\$

5.  在区间 []{.arithmatex}$[a,b]$ 上满足 []{.arithmatex}$f(x)\leq g(x)$，则 \$[]{.arithmatex}$\int_a^b f(x)\ dx\leq\int_a^b g(x)\ dx$\$

6.  :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \left\|\int_a\^bf(x)\\ dx\right \|\leq\int_a\^b\|f(x)\|\\ dx
    :::

    $$\left|\int_a^bf(x)\ dx\right |\leq\int_a^b|f(x)|\ dx$$
    ::::

7.  若 []{.arithmatex}$f(x)$ 是偶函数，且在 []{.arithmatex}$[-a,a]$ 上连续，则 \$[]{.arithmatex}$\int_{-a}^af(x)\ dx=2\int_0^af(x)\ dx$\$

8.  若 []{.arithmatex}$f(x)$ 是奇函数，且在 []{.arithmatex}$[-a,a]$ 上连续，则 \$[]{.arithmatex}$\int_{-a}^af(x)\ dx=0$\$

#### 不定积分 {#_5}

我们现在需要一种简单的表示反导数的方式。根据微积分基本定理，我们可以用 []{.arithmatex}$\displaystyle\int f(x)\ dx$ 表示"函数 []{.arithmatex}$f$ 的反导数的集合"，注意任何可积函数都有无数个反导数，唯一不同的是常数部分。例如，

:::: {.arithmatex}
::: {.MathJax_Preview}
\int x\^2\\ dx=\frac{x\^3}{3}+C
:::

$$\int x^2\ dx=\frac{x^3}{3}+C$$
::::

对于任意常数 []{.arithmatex}$C$ 都成立。也就是说，若 []{.arithmatex}$F'(x)=f(x)$，则

:::: {.arithmatex}
::: {.MathJax_Preview}
\int f(x)\\ dx=F(x)+C
:::

$$\int f(x)\ dx=F(x)+C$$
::::

不定积分的性质同定积分的性质。

#### 换元法 {#_6}

- 第一换元积分法：令 []{.arithmatex}$y=g(x)$ 有：

:::: {.arithmatex}
::: {.MathJax_Preview}
\red{\boxed{\int_a\^bf(g(x))g\'(x)\\ dx=\int\_{g(a)}\^{g(b)}f(y)\\ dy}}
:::

$$\red{\boxed{\int_a^bf(g(x))g'(x)\ dx=\int_{g(a)}^{g(b)}f(y)\ dy}}$$
::::

1.  :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \int 2\sin 2x\\ dx\xlongequal{u=2x}\int\sin u\\ du=-\cos u+C=-\cos 2x+C\\ \\ \\ \\ (du=2dx)
    :::

    $$\int 2\sin 2x\ dx\xlongequal{u=2x}\int\sin u\ du=-\cos u+C=-\cos 2x+C\ \ \ \ (du=2dx)$$
    ::::

2.  :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \int (2x+1)\^5\\ dx\xlongequal{u=2x+1}\int u\^5\\ du=\frac{1}{12}u\^6+C=\frac{1}{12}(2x+1)\^6+C\\ \\ \\ \\ (du=2dx)
    :::

    $$\int (2x+1)^5\ dx\xlongequal{u=2x+1}\int u^5\ du=\frac{1}{12}u^6+C=\frac{1}{12}(2x+1)^6+C\ \ \ \ (du=2dx)$$
    ::::

3.  :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \begin{aligned}\int\frac{2x}{(x\^2+1)\^3}\\ dx&=\int(x\^2+1)\^{-3}\cdot 2x\\ dx\xlongequal{u=x\^2+1}\int u\^{-3}\\ du\\&=-\frac{1}{2}u\^{-2}+C=-\frac{1}{2(x\^2+1)}+C\\ \\ \\ \\ (du=2xdx)\end{aligned}
    :::

    $$\begin{aligned}\int\frac{2x}{(x^2+1)^3}\ dx&=\int(x^2+1)^{-3}\cdot 2x\ dx\xlongequal{u=x^2+1}\int u^{-3}\ du\\&=-\frac{1}{2}u^{-2}+C=-\frac{1}{2(x^2+1)}+C\ \ \ \ (du=2xdx)\end{aligned}$$
    ::::

4.  :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \begin{aligned}\int x\sqrt{1-x\^2}\\ dx&=-\frac{1}{2}\int\sqrt{1-x\^2}(-2x\\ dx)\xlongequal{u=1-x\^2}-\frac{1}{2}\int u\^{\frac{1}{2}}\\ du\\&=-\frac{1}{3}u\^{\frac{3}{2}}+C=-\frac{1}{3}(1-x\^2)\^{\frac{3}{2}}+C\\ \\ \\ \\ (du=-2dx)\end{aligned}
    :::

    $$\begin{aligned}\int x\sqrt{1-x^2}\ dx&=-\frac{1}{2}\int\sqrt{1-x^2}(-2x\ dx)\xlongequal{u=1-x^2}-\frac{1}{2}\int u^{\frac{1}{2}}\ du\\&=-\frac{1}{3}u^{\frac{3}{2}}+C=-\frac{1}{3}(1-x^2)^{\frac{3}{2}}+C\ \ \ \ (du=-2dx)\end{aligned}$$
    ::::

5.  :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \int\frac{1}{x\^2+a\^2}\\ dx=\frac{1}{a\^2}\int\frac{1}{\frac{x\^2}{a\^2}+1}\\ dx=\frac{1}{a}\int\frac{1}{1+(\frac{x}{a})\^2}\\ d(\frac{x}{a})=\frac{1}{a}\arctan\frac{x}{a}+C
    :::

    $$\int\frac{1}{x^2+a^2}\ dx=\frac{1}{a^2}\int\frac{1}{\frac{x^2}{a^2}+1}\ dx=\frac{1}{a}\int\frac{1}{1+(\frac{x}{a})^2}\ d(\frac{x}{a})=\frac{1}{a}\arctan\frac{x}{a}+C$$
    ::::

6.  :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \int_0\^1e\^{2x}\\ dx=\int_0\^2\frac{1}{2}e\^y\\ dy=\frac{1}{2}(e\^2-e\^0)=\frac{1}{2}(e\^2-1)
    :::

    $$\int_0^1e^{2x}\ dx=\int_0^2\frac{1}{2}e^y\ dy=\frac{1}{2}(e^2-e^0)=\frac{1}{2}(e^2-1)$$
    ::::

7.  第二换元积分法：令 []{.arithmatex}$x=g(t),dx=g'(t)dt$ 有：

:::: {.arithmatex}
::: {.MathJax_Preview}
\red{\boxed{\int f(x)\\ dx=\int f\[g(t)\]g\'(t)\\ dt}}
:::

$$\red{\boxed{\int f(x)\ dx=\int f[g(t)]g'(t)\ dt}}$$
::::

1.  :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \begin{aligned}\int\frac{1}{1+\sqrt x}\\ dx&\xlongequal{x=t\^2}\int\frac{1}{1+t}\cdot 2t\\ dt=2\int(1-\frac{1}{1+t})\\ dt=2t-2\ln\|1+t\|+C\\&=2\sqrt{x}-2\ln\|1+\sqrt{x}\|+C\end{aligned}
    :::

    $$\begin{aligned}\int\frac{1}{1+\sqrt x}\ dx&\xlongequal{x=t^2}\int\frac{1}{1+t}\cdot 2t\ dt=2\int(1-\frac{1}{1+t})\ dt=2t-2\ln|1+t|+C\\&=2\sqrt{x}-2\ln|1+\sqrt{x}|+C\end{aligned}$$
    ::::

2.  :::: {.arithmatex}
    ::: {.MathJax_Preview}
    \begin{aligned}\int\sqrt{a\^2-x\^2}\\ dx&\xlongequal{x=a\sin t}\int a\cos t\cdot a\cos t\\ dt=a\^2\int \cos\^2 t\\ dt\\&=a\^2\int\frac{1+\cos 2t}{2}dt=a\^2(\frac{1}{2}t+\frac{1}{4}\sin 2t)+C\\&=a\^2(\frac{1}{2}\arcsin\frac{x}{a}+\frac{1}{4}\frac{2}{a\^2}x\sqrt{a\^2-x\^2})+C\\&=\frac{a\^2}{2}\arcsin\frac{x}{a}+\frac{x}{2}\sqrt{a\^2-x\^2}+C\end{aligned}
    :::

    $$\begin{aligned}\int\sqrt{a^2-x^2}\ dx&\xlongequal{x=a\sin t}\int a\cos t\cdot a\cos t\ dt=a^2\int \cos^2 t\ dt\\&=a^2\int\frac{1+\cos 2t}{2}dt=a^2(\frac{1}{2}t+\frac{1}{4}\sin 2t)+C\\&=a^2(\frac{1}{2}\arcsin\frac{x}{a}+\frac{1}{4}\frac{2}{a^2}x\sqrt{a^2-x^2})+C\\&=\frac{a^2}{2}\arcsin\frac{x}{a}+\frac{x}{2}\sqrt{a^2-x^2}+C\end{aligned}$$
    ::::

#### 分部积分法 {#_7}

:::: {.arithmatex}
::: {.MathJax_Preview}
(uv)\'=u\'v+uv\'\implies uv\'=(uv)\'-vu\'\implies \int uv\'\\ dx=uv-\int vu\'\\ dx
:::

$$(uv)'=u'v+uv'\implies uv'=(uv)'-vu'\implies \int uv'\ dx=uv-\int vu'\ dx$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\red{\boxed{\int u\\ dv=uv-\int v\\ du}}
:::

$$\red{\boxed{\int u\ dv=uv-\int v\ du}}$$
::::

1.  计算 []{.arithmatex}$\displaystyle\int x\cos x\ dx$，设 []{.arithmatex}$u=x,dv=\cos x\ dx$，则 []{.arithmatex}$du=dx,v=\sin x$ \$[]{.arithmatex}$\int x\cos x\ dx=x\sin x-\int \sin x\ dx=x\sin x+\cos x+C$\$

2.  计算 []{.arithmatex}$\displaystyle\int\arctan x\ dx$，设 []{.arithmatex}$u=\arctan x,dv=dx$，则 []{.arithmatex}$\displaystyle du=\frac{1}{1+x^2}\ dx,v=x$ \$[]{.arithmatex}$\begin{aligned}\int \arctan x&=x\arctan x-\int\frac{1}{1+x^2}\ dx=x\arctan x-\frac{1}{2}\int\frac{1}{1+x^2}d(1+x^2)\\&=x\arctan x-\frac{1}{2}\ln(1+x^2)+C\end{aligned}$\$

3.  计算 []{.arithmatex}$\displaystyle\int x\ln x\ dx$，设 []{.arithmatex}$u=\ln x,dv=x\ dx$，则 []{.arithmatex}$\displaystyle du=\frac{1}{x}\ dx,v=\frac{1}{2}x^2$ \$[]{.arithmatex}$\int x\ln x\ dx=\frac{1}{2}x^2\ln x-\int\frac{1}{x}\cdot\frac{1}{2}x^2\ dx=\frac{1}{2}x^2\ln x-\frac{1}{4}x^2+C$\$

#### Gamma 函数（第二类欧拉积分） {#gamma}

欧拉发现当 []{.arithmatex}$n$ 为整数时，[]{.arithmatex}$\displaystyle\int_0^{+\infty}t^ne^{-t}\ dt=n!$，于是我们把 []{.arithmatex}$n$ 替换成实数，就可变为

:::: {.arithmatex}
::: {.MathJax_Preview}
\Gamma(s)=\int_0\^{+\infty}t\^{s-1}e\^{-t}\\ dt
:::

$$\Gamma(s)=\int_0^{+\infty}t^{s-1}e^{-t}\ dt$$
::::

1.  []{.arithmatex}$s$ 为非正整数的复数 []{.arithmatex}$s$ 时，[]{.arithmatex}$\Gamma(s+1)=s\Gamma(s)$
2.  []{.arithmatex}$n$ 为整数时，[]{.arithmatex}$\Gamma(n+1)=n!$
3.  余元公式（欧拉反射原理）：[]{.arithmatex}$s\in(0,1)$ 时，[]{.arithmatex}$\displaystyle\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin\pi s}$，得 []{.arithmatex}$\displaystyle\Gamma\left(\frac{1}{2}\right)=\sqrt\pi$

#### 应用 {#_8}

1.  计算 []{.arithmatex}$y=e^x$ 在 []{.arithmatex}$x=0$ 与 []{.arithmatex}$x=1$ 之间与 []{.arithmatex}$x$ 轴围成的曲边梯形的面积。

只需计算 []{.arithmatex}$\displaystyle\int_0^1e^x\ dx=e^1-e^0=e-1$

1.  计算 []{.arithmatex}$x=y^2$ 与 []{.arithmatex}$x=1$ 之间围成的图形的面积。

只需计算 []{.arithmatex}$\displaystyle\int_0^1(\sqrt{x}-(-\sqrt{x}))\ dx=\int_0^1(2\sqrt{x})\ dx=\frac{4}{3}\sqrt{x^3}|_0^1=\frac{4}{3}-0=\frac{4}{3}$

1.  【2025 GD 一模 T19】如果函数 []{.arithmatex}$F(x)$ 的导数为 []{.arithmatex}$F'(x)=f(x)$，可记为 []{.arithmatex}$\displaystyle\int f(x)\ dx=F(x)$，若 []{.arithmatex}$f(x)\geq 0$，则 []{.arithmatex}$\displaystyle\int_a^bf(x)\ dx=F(b)-F(a)$ 表示曲线 []{.arithmatex}$y=f(x)$，直线 []{.arithmatex}$x=a,x=b$ 以及 []{.arithmatex}$x$ 轴围成的"曲边梯形"的面积。如：[]{.arithmatex}$\displaystyle\int 2x\ dx=x^2+C$，其中 []{.arithmatex}$C$ 为常数；[]{.arithmatex}$\displaystyle\int_0^2 2x\ dx=(2^2+C)-(0+C)=4$，则表示 []{.arithmatex}$x=0,x=1,y=2x+C$ 以及 []{.arithmatex}$x$ 轴围成的面积为 []{.arithmatex}$4$. []{.arithmatex}$(1)$ 若 []{.arithmatex}$f(x)=\displaystyle\int(e^x+1)\ dx,f(0)=2$，求 []{.arithmatex}$f(x)$ 的表达式。 []{.arithmatex}$(2)$ 求曲线 []{.arithmatex}$y=x^2$ 与直线 []{.arithmatex}$y=-x+6$ 所围成图形的面积。 []{.arithmatex}$(3)$ 若 []{.arithmatex}$f(x)=e^x-1-2mx,x\in[0,+\infty)$，其中 []{.arithmatex}$m\in\R,\forall a,b\in[0,+\infty)$，若 []{.arithmatex}$a>b$，都满足 []{.arithmatex}$\displaystyle\int_0^a f(x)\ dx>\int_0^b f(x)\ dx$，求 []{.arithmatex}$m$ 取值范围。

解：[]{.arithmatex}$(1)\ f(x)=e^x+x+1$.

[]{.arithmatex}$(2)$ 先解方程 []{.arithmatex}$x^2=-x+6$ 得到 []{.arithmatex}$x=-3$ 或 []{.arithmatex}$2$.

答案即为 []{.arithmatex}$\displaystyle\int_{-3}^2 (-x+6-x^2)\ dx=(-\frac{1}{2}x^2+6x-\frac{1}{3}x^3)|_{-3}^2=\frac{22}{3}-(-\frac{27}{2})=\frac{125}{6}$.

[]{.arithmatex}$(3)$ 由题意可知，[]{.arithmatex}$\forall a,b\in[0,+\infty),a>b$ 满足 []{.arithmatex}$F(a)-F(0)>F(b)-F(0)$，即 []{.arithmatex}$F(a)\uparrow$，进而 []{.arithmatex}$f(x)\geq 0$ 在 []{.arithmatex}$[0,+\infty)$ 恒成立。

接下来就是常规导数了。分离参数 []{.arithmatex}$m\leq\frac{e^x-1}{2x}=g(x),g'(x)=\frac{(x-1)e^x+1}{2x^2}$，令 []{.arithmatex}$h(x)=(x-1)e^x,h'(x)=xe^x\geq 0$，即 []{.arithmatex}$h(x)\uparrow,g'(x)\uparrow,g(x)\uparrow$，由洛必达法则，[]{.arithmatex}$\displaystyle m\leq\lim_{x\to 0}\frac{e^x-1}{2x}=\lim_{x\to 0}\frac{e^x}{2}=\frac{1}{2}$.

## 微积分在数列中的应用 {#_9}

秒杀神秘放缩的终极方法。但是需要一些高等知识，比如说解简单的常微分方程。但是一般的方程一眼看出来就可以了，这里给出通法：

对于一阶齐次线性微分方程：

:::: {.arithmatex}
::: {.MathJax_Preview}
y\'+P(x)y=0
:::

$$y'+P(x)y=0$$
::::

解为

:::: {.arithmatex}
::: {.MathJax_Preview}
y=Ce\^{-\int P(x)dx}
:::

$$y=Ce^{-\int P(x)dx}$$
::::

对于一阶非齐次线性微分方程：

:::: {.arithmatex}
::: {.MathJax_Preview}
y\'+P(x)y=Q(x)
:::

$$y'+P(x)y=Q(x)$$
::::

先解 []{.arithmatex}$y'+P(x)y=0$ 得到 []{.arithmatex}$y=Ce^{-\int P(x)dx}$，再令 []{.arithmatex}$C=u(x)$ 得

:::: {.arithmatex}
::: {.MathJax_Preview}
y=u(x)e\^{-\int P(x) dx}
:::

$$y=u(x)e^{-\int P(x) dx}$$
::::

代入原方程得

:::: {.arithmatex}
::: {.MathJax_Preview}
u\'(x)=\frac{Q(x)}{e\^{-\int P(x)dx}}
:::

$$u'(x)=\frac{Q(x)}{e^{-\int P(x)dx}}$$
::::

对 []{.arithmatex}$u'(x)$ 积分带入得到通解：

:::: {.arithmatex}
::: {.MathJax_Preview}
y=Ce\^{-\int P(x)dx}+e\^{-\int P(x)dx}\int Q(x)e\^{\int P(x)dx}dx
:::

$$y=Ce^{-\int P(x)dx}+e^{-\int P(x)dx}\int Q(x)e^{\int P(x)dx}dx$$
::::

以上的 []{.arithmatex}$C$ 都为常数，由初始条件决定。

------------------------------------------------------------------------

[]{.arithmatex}$\displaystyle a_1=1,a_{n+1}=a_n+\frac{1}{a_n}$，求 []{.arithmatex}$a_{2024}$ 的整数部分？

设 []{.arithmatex}$a_n$ 近似为一个连续函数 []{.arithmatex}$f(x)$，考虑 []{.arithmatex}$a_{n+1}-a_n$ 和 []{.arithmatex}$\frac{1}{a_n}$ 的关系。对于 []{.arithmatex}$n\to +\infty$，有

:::: {.arithmatex}
::: {.MathJax_Preview}
f\'(x)=\frac{1}{f(x)}\implies\frac{\mathrm{d}f(x)}{\mathrm{d}x}=\frac{1}{f(x)} \implies f(x)\mathrm{d}f(x)=\mathrm{d}x\\\implies\int f(x)\mathrm{d}f(x)=\int\mathrm{d}x\implies \frac{f\^2(x)}{2}=x+C
:::

$$f'(x)=\frac{1}{f(x)}\implies\frac{\mathrm{d}f(x)}{\mathrm{d}x}=\frac{1}{f(x)} \implies f(x)\mathrm{d}f(x)=\mathrm{d}x\\\implies\int f(x)\mathrm{d}f(x)=\int\mathrm{d}x\implies \frac{f^2(x)}{2}=x+C$$
::::

由 []{.arithmatex}$f(1)=1$ 得到 []{.arithmatex}$\displaystyle C=-\frac{1}{2}$，微分方程解得 []{.arithmatex}$f(x)=\sqrt{2x-1}$，得到 []{.arithmatex}$f(2024)=\sqrt{4047}\approx 63$

------------------------------------------------------------------------

已知 []{.arithmatex}$\displaystyle a_1=1,a_{n+1}=a_n-\frac{1}{3}a_n^2$，则 []{.arithmatex}$100a_{100}$ 的范围是哪个：[]{.arithmatex}$\displaystyle\left(2,\frac{5}{2}\right),\left(\frac{5}{2},3\right), \left(3,\frac{7}{2}\right)$ ？

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{a\_{n+1}}=\frac{3}{a_n(3-a_n)}=\frac{1}{a_n}+\frac{1}{3-a_n}\>\frac{1}{a_n}+\frac{1}{3}
:::

$$\frac{1}{a_{n+1}}=\frac{3}{a_n(3-a_n)}=\frac{1}{a_n}+\frac{1}{3-a_n}>\frac{1}{a_n}+\frac{1}{3}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{a_n}\>a_1+\frac{n-1}{3}=\frac{n+2}{3}\implies a_n\<\frac{3}{n+2}\implies 100a\_{100}\<3
:::

$$\frac{1}{a_n}>a_1+\frac{n-1}{3}=\frac{n+2}{3}\implies a_n<\frac{3}{n+2}\implies 100a_{100}<3$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{a\_{n+1}}\<\frac{1}{a_n}+\frac{1}{3-\frac{3}{n+2}}=\frac{1}{a_n}+\frac{n+2}{3(n+1)}=\frac{1}{a_n}+\frac{1}{3}+\frac{1}{3(n+1)}
:::

$$\frac{1}{a_{n+1}}<\frac{1}{a_n}+\frac{1}{3-\frac{3}{n+2}}=\frac{1}{a_n}+\frac{n+2}{3(n+1)}=\frac{1}{a_n}+\frac{1}{3}+\frac{1}{3(n+1)}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{a\_{100}}\<\frac{1}{a_1}+\frac{99}{3}+\frac{1}{3}\left(\frac{1}{2}+\frac{1}{3}+\dots+\frac{1}{100}\right)=34+\frac{1}{3}\left(\frac{1}{2}+\frac{1}{3}+\dots+\frac{1}{100}\right)
:::

$$\frac{1}{a_{100}}<\frac{1}{a_1}+\frac{99}{3}+\frac{1}{3}\left(\frac{1}{2}+\frac{1}{3}+\dots+\frac{1}{100}\right)=34+\frac{1}{3}\left(\frac{1}{2}+\frac{1}{3}+\dots+\frac{1}{100}\right)$$
::::

**注意到**

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{2}+\frac{1}{3}+\dots+\frac{1}{100}\<\frac{1}{2}\times 4+\frac{1}{6}\times 96=18
:::

$$\frac{1}{2}+\frac{1}{3}+\dots+\frac{1}{100}<\frac{1}{2}\times 4+\frac{1}{6}\times 96=18$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{a\_{100}}\<\frac{1}{40}\implies 100a\_{100}\>\frac{5}{2}
:::

$$\frac{1}{a_{100}}<\frac{1}{40}\implies 100a_{100}>\frac{5}{2}$$
::::

这道题是我们班的补充题，当时无人证出 []{.arithmatex}$\displaystyle >\frac{5}{2}$，我们老师上课思考了不到 []{.arithmatex}$15$ 分钟讲了这种方法（他从不备课），注意力简直惊为天人。

积分法：[]{.arithmatex}$\displaystyle f(x)=a_n,f'(x)=\frac{df(x)}{dx}=-\frac{1}{3}f^2(x)\implies \int f^{-2}(x)df(x)=\int-\frac{1}{3}dx\\-f^{-1}(x)=-\frac{1}{3}x+C,f(x)=\frac{3}{x+C}\implies\frac{3}{x+2}$，显然 []{.arithmatex}$\displaystyle 100a_{100}\in\left(\frac{5}{2},3\right)$. 可以代入 []{.arithmatex}$a_2,a_3$ 获得更高的精度。

------------------------------------------------------------------------

已知 []{.arithmatex}$\displaystyle a_1=1,a_{n+1}=\frac{a_n}{1+\sqrt[3]{a_n}}$，求 []{.arithmatex}$S_{100}$ 的整数部分。

答案：准确值是 []{.arithmatex}$2.38$.

:::: {.arithmatex}
::: {.MathJax_Preview}
\frac{1}{a\_{n+1}}=\frac{1}{a_n}+\frac{1}{a_n\^{\frac{2}{3}}}\xlongequal{b_n=\frac{1}{a_n}}b\_{n+1}=b_n+b_n\^{\frac{2}{3}}\xlongequal{f(x)=b_n}f\'(x)=f\^{\frac{2}{3}}(x)
:::

$$\frac{1}{a_{n+1}}=\frac{1}{a_n}+\frac{1}{a_n^{\frac{2}{3}}}\xlongequal{b_n=\frac{1}{a_n}}b_{n+1}=b_n+b_n^{\frac{2}{3}}\xlongequal{f(x)=b_n}f'(x)=f^{\frac{2}{3}}(x)$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\int f\^{-\frac{2}{3}}(x) df(x)=\int dx\implies 3f\^{\frac{1}{3}}(x)=x+C\implies f(x)=\left(\frac{x+2}{3}\right)\^3=\left(\frac{x-2+3\sqrt\[3\]{2}}{3}\right)\^3
:::

$$\int f^{-\frac{2}{3}}(x) df(x)=\int dx\implies 3f^{\frac{1}{3}}(x)=x+C\implies f(x)=\left(\frac{x+2}{3}\right)^3=\left(\frac{x-2+3\sqrt[3]{2}}{3}\right)^3$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
a_n=\frac{27}{(x+2)\^3},\zeta(3)=\sum\_{n=1}\^{\infty}\frac{1}{n\^3}\approx 1.202,S\_{\infty}=27\cdot 0.077=2.079
:::

$$a_n=\frac{27}{(x+2)^3},\zeta(3)=\sum_{n=1}^{\infty}\frac{1}{n^3}\approx 1.202,S_{\infty}=27\cdot 0.077=2.079$$
::::

另外，欧拉常数 []{.arithmatex}$\displaystyle\gamma=\lim_{n\to\infty}\left[\left(\sum_{k=1}^n\frac{1}{k}\right)-\ln n\right]=\int_1^{\infty}\left(\frac{1}{\lfloor x\rfloor}-\frac{1}{x}\right)\approx 0.57721 56649 01532 86060$，于是可以估计 []{.arithmatex}$\displaystyle\sum_{k=1}^n\frac{1}{k}\approx\ln n+\gamma$.

------------------------------------------------------------------------

也可以用一个结论（Basel 问题，[知乎专栏](https://zhuanlan.zhihu.com/p/144278965) ）：[]{.arithmatex}$\red{\boxed{\sum_{n=1}^{+\infty}\frac{1}{n^2}=\frac{\pi^2}{6}\approx 1.645}}$

相关证明：设黎曼 Zeta 函数 []{.arithmatex}$\zeta(s)=\displaystyle\sum_{n=1}^{+\infty}\frac{1}{n^s}\ (s>1)$，显然 []{.arithmatex}$\displaystyle\lim_{s\to 1^+}\zeta(s)=+\infty,\lim_{s\to+\infty}\zeta(s)=1$.

由泰勒展开得 []{.arithmatex}$\displaystyle\sin x=x-\frac{x^3}{6}+\frac{x^5}{120}+\dots=\sum_{k=0}^{+\infty}\frac{(-1)^k}{(2k+1)!}x^{2k+1}$

因此 []{.arithmatex}$\displaystyle\frac{\sin x}{x}=1-\frac{x^2}{3!}+\frac{x^4}{5!}+\dots=\sum_{n=0}^{+\infty}\frac{(-1)^nx^{2n}}{(2n+1)!}①$（ []{.arithmatex}$\displaystyle\frac{\sin x}{x}$ 的无穷级数展开）

熟知 []{.arithmatex}$\displaystyle\frac{\sin x}{x}$ 的无穷乘积展开 []{.arithmatex}$\displaystyle\frac{\sin x}{x}=\prod_{n=1}^{+\infty}\left(1-\frac{x^2}{n^2\pi^2}\right)=\left(1-\frac{x^2}{\pi^2}\right)\left(1-\frac{x^2}{4\pi^2}\right)\cdots②$

Basel 问题即 []{.arithmatex}$\displaystyle\zeta(2)=\sum_{n=1}^{+\infty}\frac{1}{n^2}$，比较 []{.arithmatex}$①②$ 式中二次项系数得 []{.arithmatex}$\displaystyle -\frac{1}{3!}=-\frac{1}{\pi^2}-\frac{1}{2^2\pi^2}-\dots$

由此可得 []{.arithmatex}$\displaystyle\zeta(2)=\frac{\pi^2}{6}$，进一步地我们有 []{.arithmatex}$\displaystyle\zeta(4)=\frac{\pi^4}{90},\zeta(6)=\frac{\pi^6}{945}$.

:::: {.arithmatex}
::: {.MathJax_Preview}
\zeta(2n)=\left\[\sum\_{k=1}\^{n-1}\frac{(-1)\^{k+1}\pi\^{2k}\zeta(2n-2k)}{(2k+1)!}\right\]+\frac{(-1)\^{n+1}n\pi\^{2n}}{(2n+1)!}\\ \\ \\ \\ \\ \\ n\in\N\^\*
:::

$$\zeta(2n)=\left[\sum_{k=1}^{n-1}\frac{(-1)^{k+1}\pi^{2k}\zeta(2n-2k)}{(2k+1)!}\right]+\frac{(-1)^{n+1}n\pi^{2n}}{(2n+1)!}\ \ \ \ \ \ n\in\N^*$$
::::

上述思路可总结出一个结论：若 []{.arithmatex}$\displaystyle\sum_{k=0}^{+\infty}a_kx^k=\prod_{k=1}^{+\infty}(1+b_kx)$，设 []{.arithmatex}$S_n=\displaystyle\sum_{k=1}^{+\infty}b_k^n$，则 \$[]{.arithmatex}$S_1=a_1,\ \ \ S_n=\displaystyle\sum_{k=1}^{n-1}(-1)^{k+1}a_kS_{n-k}+(-1)^{n+1}na_n$\$

### 积分放缩在数列中的应用 {#_10}

我们熟知的积分放缩一般是这样的（证明：几何意义）

:::: {.arithmatex}
::: {.MathJax_Preview}
\int_1\^{n+1}f(x)\\ dx \<\sum\_{k=1}\^nf(k)\<\int_0\^nf(x)\\ dx\\ \\ \\ \\ \\ \\ \\ \\ f(x)\downarrow
:::

$$\int_1^{n+1}f(x)\ dx <\sum_{k=1}^nf(k)<\int_0^nf(x)\ dx\ \ \ \ \ \ \ \ f(x)\downarrow$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\int_0 \^{n}f(x)\\ dx\<\sum\_{k=1}\^nf(k)\<\int_1\^{n+1}f(x)\\ dx\\ \\ \\ \\ \\ \\ \\ \\ f(x)\uparrow
:::

$$\int_0    ^{n}f(x)\ dx<\sum_{k=1}^nf(k)<\int_1^{n+1}f(x)\ dx\ \ \ \ \ \ \ \ f(x)\uparrow$$
::::

例如：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned}\sum\_{k=1}\^n\frac{1}{\sqrt{k} }&\>\int_1\^{n+1}\frac{1}{\sqrt{x} }\\ dx=2\sqrt{x}\|\_1\^{n+1}=2\left(\sqrt{n+1}-1\right)\\&\<\int_0\^n\frac{1}{\sqrt{x} }\\ dx=2\sqrt{x}\|\_0\^n=2\sqrt{n}\end{aligned}
:::

$$\begin{aligned}\sum_{k=1}^n\frac{1}{\sqrt{k} }&>\int_1^{n+1}\frac{1}{\sqrt{x} }\ dx=2\sqrt{x}|_1^{n+1}=2\left(\sqrt{n+1}-1\right)\\&<\int_0^n\frac{1}{\sqrt{x} }\ dx=2\sqrt{x}|_0^n=2\sqrt{n}\end{aligned}$$
::::

练习 1：证明 []{.arithmatex}$\displaystyle\sum_{k=2}^n\frac{1}{k\sqrt{k}}<\sqrt{2}\ \ \ \ \text{}$ 和 []{.arithmatex}$\ \ \ \ \displaystyle\frac{2}{3}n^\frac{3}{2}\leq\sum_{k=1}^n\sqrt{k}\leq\frac{2}{3}[(n+1)^\frac{3}{2}-n]$

练习 2：证明 []{.arithmatex}$\displaystyle\sum_{k=2}^{n+1}\frac{1}{k}<\ln(n+1)<\sum_{k=1}^n\frac{1}{k}\ \ \ \ \text{}$ 和 []{.arithmatex}$\ \ \ \ \displaystyle\frac{4}{7}<\sum_{k=n+1}^{2n}\frac{1}{k}<\ln 2<\frac{25}{36}<\frac{\sqrt{2}}{2}$

练习 3：证明 []{.arithmatex}$\displaystyle\begin{cases}\displaystyle\sum_{k=1}^n\frac{1}{k^p}<\frac{p}{p-1}&p>1\\\displaystyle\sum_{k=1}^n\frac{1}{k^p}\geq\displaystyle\sum_{k=1}^n\frac{1}{k}>\ln n&p\leq 1\end{cases}$

我们还可以根据 []{.arithmatex}$f(x)$ 的凹凸性进一步放缩。

当 []{.arithmatex}$f(x)\downarrow$ 且下凸时，

:::: {.arithmatex}
::: {.MathJax_Preview}
\int_1\^{n+1}f(x)\\ dx+\frac{f(1)-f(n+1)}{2}\<\sum\_{k=1}\^nf(k)\<\int_0\^nf(x)\\ dx
:::

$$\int_1^{n+1}f(x)\ dx+\frac{f(1)-f(n+1)}{2}<\sum_{k=1}^nf(k)<\int_0^nf(x)\ dx$$
::::

当 []{.arithmatex}$f(x)\downarrow$ 且上凸时，

:::: {.arithmatex}
::: {.MathJax_Preview}
\int_1\^{n+1}f(x)\\ dx\<\sum\_{k=1}\^nf(k)\<\int_0\^nf(x)\\ dx-\frac{f(0)-f(n)}{2}
:::

$$\int_1^{n+1}f(x)\ dx<\sum_{k=1}^nf(k)<\int_0^nf(x)\ dx-\frac{f(0)-f(n)}{2}$$
::::

当 []{.arithmatex}$f(x)\uparrow$ 且下凸时，

:::: {.arithmatex}
::: {.MathJax_Preview}
\int_0\^nf(x)\\ dx+\frac{f(n)-f(0)}{2}\<\sum\_{k=1}\^nf(k)\<\int_1\^{n+1}f(x)\\ dx
:::

$$\int_0^nf(x)\ dx+\frac{f(n)-f(0)}{2}<\sum_{k=1}^nf(k)<\int_1^{n+1}f(x)\ dx$$
::::

当 []{.arithmatex}$f(x)\uparrow$ 且上凸时，

:::: {.arithmatex}
::: {.MathJax_Preview}
\int_0\^nf(x)\\ dx\<\sum\_{k=1}\^nf(k)\<\int_1\^{n+1}f(x)\\ dx-\frac{f(n+1)-f(1)}{2}
:::

$$\int_0^nf(x)\ dx<\sum_{k=1}^nf(k)<\int_1^{n+1}f(x)\ dx-\frac{f(n+1)-f(1)}{2}$$
::::
