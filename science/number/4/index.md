# 数论测试 {#_1}

## 一、请给出整除的概念及性质 {#_2}

对于整数 []{.arithmatex}$a,b$ []{.arithmatex}$(b\neq0)$，如果存在整数 []{.arithmatex}$c$，使得 []{.arithmatex}$a=bc$，

则称 []{.arithmatex}$b$ 整除 []{.arithmatex}$a$，记作 []{.arithmatex}$b \mid a$；否则称 []{.arithmatex}$b$ 不整除 []{.arithmatex}$a$，记作 []{.arithmatex}$b \nmid a$。

**性质**：

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{rlrl} 1.&a\mid b&\Longrightarrow&\pm a \mid \pm b\\ 2.&a \mid b,\\ b\mid c&\Longrightarrow&a \mid c\\ 3.&\forall i:b\mid a_i&\Longrightarrow&b\mid\Sigma\\ a_ik_i\\ 4.&b\mid a&\Longrightarrow&bc\mid ac\\ (c\in\mathbb Z,c\neq0)\\ 5.&b\mid a\\ (a\neq0)&\Longrightarrow&\|b\|\le\|a\|\\ 5.&b\mid a,\\ \|a\|\<\|b\|&\Longrightarrow&a=0\\ \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{rlrl}
1.&a\mid b&\Longrightarrow&\pm a \mid \pm b\\
2.&a \mid b,\ b\mid c&\Longrightarrow&a \mid c\\
3.&\forall i:b\mid a_i&\Longrightarrow&b\mid\Sigma\ a_ik_i\\
4.&b\mid a&\Longrightarrow&bc\mid ac\ (c\in\mathbb Z,c\neq0)\\
5.&b\mid a\ (a\neq0)&\Longrightarrow&|b|\le|a|\\
5.&b\mid a,\ |a|<|b|&\Longrightarrow&a=0\\
\end{array}$$
::::

### 二、请给出同余的概念及性质 {#_3}

给定正整数 []{.arithmatex}$m$ 称为模，[]{.arithmatex}$a,b$ 为任意两个整数，满足：

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{ll} a=q_1m+r_1,&0\le r_1\<m\\ b=q_2m+r_2,&0\le r_2\<m\\ \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{ll}
a=q_1m+r_1,&0\le r_1<m\\
b=q_2m+r_2,&0\le r_2<m\\
\end{array}$$
::::

则称 []{.arithmatex}$a,b$ 对 []{.arithmatex}$m$ 同余，记作 []{.arithmatex}$a \equiv b \pmod m$，简记为 []{.arithmatex}$a \equiv b\ (m)$。

**性质**：

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{rlrl} 1.&a \equiv a \pmod m\\ 2.&a \equiv b \pmod m &\Longleftrightarrow& b\equiv a \pmod m\\ 3.&a\equiv b\pmod m,\\ b\equiv c\pmod m&\Longrightarrow&a\equiv c\pmod m\\ 4.&aK\equiv bK\pmod m&\Longrightarrow&a\equiv b\pmod{\frac{m}{(m,k)}}\\ 5.&a\equiv b\pmod m,\\ c\equiv d\pmod m&\Longrightarrow&a\pm c\equiv b\pm d\pmod m\\ 6.&a\equiv b\pmod m,\\ c\equiv d\pmod m&\Longrightarrow&ac\equiv bd\pmod m\\ \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{rlrl}
1.&a \equiv a \pmod m\\
2.&a \equiv b \pmod m &\Longleftrightarrow& b\equiv a \pmod m\\
3.&a\equiv b\pmod m,\ b\equiv c\pmod m&\Longrightarrow&a\equiv c\pmod m\\
4.&aK\equiv bK\pmod m&\Longrightarrow&a\equiv b\pmod{\frac{m}{(m,k)}}\\
5.&a\equiv b\pmod m,\ c\equiv d\pmod m&\Longrightarrow&a\pm c\equiv b\pm d\pmod m\\
6.&a\equiv b\pmod m,\ c\equiv d\pmod m&\Longrightarrow&ac\equiv bd\pmod m\\
\end{array}$$
::::

### 三、请给出模 []{.arithmatex}$m$ 的完全剩余系的概念 {#mm}

若 []{.arithmatex}$a_1,a_2,\dots,a_m$ 对模 []{.arithmatex}$m$ 两两不同余，则这 []{.arithmatex}$m$ 个数构成模 []{.arithmatex}$m$ 的一个完全剩余系。

特殊的，任意连续的 []{.arithmatex}$m$ 个整数都构成模 []{.arithmatex}$m$ 的一个完全剩余系。

### 四、陈述裴蜀定理 {#_4}

对于任意整数 []{.arithmatex}$a,b$，一定存在一组整数解 []{.arithmatex}$x,y$ 使得 []{.arithmatex}$ax+by=(a,b)$。

### 五、陈述费马小定理 {#_5}

若 []{.arithmatex}$p$ 是素数，则 []{.arithmatex}$a^p\equiv a\pmod p$。

特别的，若 []{.arithmatex}$a\perp p$，则 []{.arithmatex}$a^{p-1}\equiv1\pmod p$。

### 六、给定模 []{.arithmatex}$m$ 的一组完全剩余系 []{.arithmatex}$x_1,\dots,x_m$，若 []{.arithmatex}$a \perp m$，请证明 []{.arithmatex}$ax_1,\dots,ax_m$ 也是模 []{.arithmatex}$m$ 的一组完全剩余系 {#mm-x_1dotsx_mx_1dotsx_m-a-perp-ma-perp-m-ax_1dotsax_max_1dotsax_m-mm}

**反证**：假设 []{.arithmatex}$ax_1,\dots,ax_m$ 不是模 []{.arithmatex}$m$ 的完全剩余系。

则一定存在 []{.arithmatex}$i\neq j$ 使得 []{.arithmatex}$ax_i\equiv ax_j\pmod m$。

因为 []{.arithmatex}$a \perp m$，因此有 []{.arithmatex}$x_i\equiv x_j\pmod m$。

与 []{.arithmatex}$x_1,\dots,x_m$ 为模 []{.arithmatex}$m$ 的完全剩余系不符。

假设不成立，故 []{.arithmatex}$ax_1,\dots,ax_m$ 是模 []{.arithmatex}$m$ 的完全剩余系。

### 七、设 []{.arithmatex}$n$ 是整数，请证明：[]{.arithmatex}$120 \mid n(n^2-1)(n^2-5n+26)$ {#nn-120-mid-nn2-1n2-5n26120-mid-nn2-1n2-5n26}

**定理**：连续 []{.arithmatex}$n$ 个整数的乘积一定被 []{.arithmatex}$n!$ 整除。

对于这 []{.arithmatex}$n$ 个数都是正整数的：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{array}{l} (a+1)(a+2)\dots(a+n)=\frac{(a+n)!}{a!}=n!\frac{(a+n)!}{n!a!}=n!\binom{a+n}{a} \end{array}
:::

$$\begin{array}{l}
(a+1)(a+2)\dots(a+n)=\frac{(a+n)!}{a!}=n!\frac{(a+n)!}{n!a!}=n!\binom{a+n}{a}
\end{array}$$
::::

而如果这 []{.arithmatex}$n$ 个数存在不是正整数的，那么一定跨过了 []{.arithmatex}$0$，乘积为 []{.arithmatex}$0$，整除是显然的。

**证明**：

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{ll} &n(n\^2-1)(n\^2-5n+26)\\ =&n(n+1)(n-1)\[(n-2)(n-3)+20\]\\ =&(n-3)(n-2)(n-1)n(n+1)+20(n-1)n(n+1) \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{ll}
&n(n^2-1)(n^2-5n+26)\\
=&n(n+1)(n-1)[(n-2)(n-3)+20]\\
=&(n-3)(n-2)(n-1)n(n+1)+20(n-1)n(n+1)
\end{array}$$
::::

因为：

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{rcl} 120&\mid& (n-3)(n-2)(n-1)n(n+1)\\ 6&\mid& (n-1)n(n+1)\\ 120&\mid& 20(n-1)n(n+1) \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{rcl}
120&\mid& (n-3)(n-2)(n-1)n(n+1)\\
6&\mid& (n-1)n(n+1)\\
120&\mid& 20(n-1)n(n+1)
\end{array}$$
::::

因此 []{.arithmatex}$120\mid(n-3)(n-2)(n-1)n(n+1)+20(n-1)n(n+1)$。

即 []{.arithmatex}$120 \mid n(n^2-1)(n^2-5n+26)$。

### 八、设 []{.arithmatex}$n$ 是正整数，且 []{.arithmatex}$2n+1$ 与 []{.arithmatex}$3n+1$ 都是完全平方数。请证明：[]{.arithmatex}$40 \mid n$ {#nn-2n12n1-3n13n1-40-mid-n40-mid-n}

**性质1**：奇数的完全平方数模 []{.arithmatex}$8$ 同余于 []{.arithmatex}$1$。

:::: {.arithmatex}
::: {.MathJax_Preview}
(2k+1)\^2\equiv4k(k+1)+1\equiv1\pmod8
:::

$$(2k+1)^2\equiv4k(k+1)+1\equiv1\pmod8$$
::::

**性质2**：任何一个数的平方模 []{.arithmatex}$5$ 同余于 []{.arithmatex}$0,\pm1$。

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{lcll} t&\equiv&0,\pm1,\pm2&\pmod5\\ t\^2&\equiv&0,\pm1&\pmod5 \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{lcll}
t&\equiv&0,\pm1,\pm2&\pmod5\\
t^2&\equiv&0,\pm1&\pmod5
\end{array}$$
::::

**证明**：

因为 []{.arithmatex}$2n+1$ 是奇数且是完全平方数，则

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{rcll} 2n+1&\equiv&1&\pmod8\\ n&\equiv&0&\pmod4 \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{rcll}
2n+1&\equiv&1&\pmod8\\
n&\equiv&0&\pmod4
\end{array}$$
::::

所以，[]{.arithmatex}$n$ 是偶数，[]{.arithmatex}$3n+1$ 是奇数且是完全平方数，则

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{rcll} 3n+1&\equiv&1&\pmod8\\ n&\equiv&0&\pmod8 \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{rcll}
3n+1&\equiv&1&\pmod8\\
n&\equiv&0&\pmod8
\end{array}$$
::::

且

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{rcll} 2n+1&\equiv&0,\pm1&\pmod5\\ 3n+1&\equiv&0,\pm1&\pmod5 \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{rcll}
2n+1&\equiv&0,\pm1&\pmod5\\
3n+1&\equiv&0,\pm1&\pmod5
\end{array}$$
::::

则有

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{rcll} (2n+1)+(3n+1)&\equiv&2&\pmod5\\ 2n+1&\equiv&1&\pmod5\\ 3n+1&\equiv&1&\pmod5\\ n&\equiv&0&\pmod5 \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{rcll}
(2n+1)+(3n+1)&\equiv&2&\pmod5\\
2n+1&\equiv&1&\pmod5\\
3n+1&\equiv&1&\pmod5\\
n&\equiv&0&\pmod5
\end{array}$$
::::

因此 []{.arithmatex}$n\equiv0\pmod{40}$，即 []{.arithmatex}$40 \mid n$。

### 九、求 []{.arithmatex}$10^{10} \bmod 7$ {#1010-bmod-71010-bmod-7}

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{ll} &10\^{10} \bmod 7\\ =&(10 \bmod 7)\^{10\bmod 6}\bmod 7\\ =&3\^4\bmod7\\ =&81\bmod7\\ =&4 \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{ll}
&10^{10} \bmod 7\\
=&(10 \bmod 7)^{10\bmod 6}\bmod 7\\
=&3^4\bmod7\\
=&81\bmod7\\
=&4
\end{array}$$
::::

即 []{.arithmatex}$10^{10}\bmod7=4$。

### 十、求满足以下条件的正整数解：[]{.arithmatex}$(a,b)+[a,b]+a+b=ab$ {#abababababababab}

设 []{.arithmatex}$d=(a,b)$，则记 []{.arithmatex}$a=a_0d$，[]{.arithmatex}$b=b_0d$（[]{.arithmatex}$a_0\perp b_0$）。

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{rcl} (a,b)+\[a,b\]+a+b&=&ab\\ d+a_0b_0d+a_0d+b_0d&=&a_0b_0d\^2\\ a_0b_0+a_0+b_0+1&=&a_0b_0d \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{rcl}
(a,b)+[a,b]+a+b&=&ab\\
d+a_0b_0d+a_0d+b_0d&=&a_0b_0d^2\\
a_0b_0+a_0+b_0+1&=&a_0b_0d
\end{array}$$
::::

因为 []{.arithmatex}$a_0b_0\ge a_0b_0,a_0,b_0\ge1$，所以 []{.arithmatex}$0<d\le4$。

当 []{.arithmatex}$d=1$ 时，[]{.arithmatex}$a_0+b_0+1=0$，无解。

当 []{.arithmatex}$d=2$ 时，

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{rcl} a_0b_0+a_0+b_0+1&=&2a_0b_0\\ a_0b_0-a_0-b_0&=&1\\ a_0(b_0-1)-(b_0-1)&=&2\\ (a_0-1)(b_0-1)&=&2\\ \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{rcl}
a_0b_0+a_0+b_0+1&=&2a_0b_0\\
a_0b_0-a_0-b_0&=&1\\
a_0(b_0-1)-(b_0-1)&=&2\\
(a_0-1)(b_0-1)&=&2\\
\end{array}$$
::::

- []{.arithmatex}$a_0-1=1$，[]{.arithmatex}$b_0-1=2$；[]{.arithmatex}$a_0=2$，[]{.arithmatex}$b_2=3$；[]{.arithmatex}$a=4$，[]{.arithmatex}$b=6$。
- []{.arithmatex}$a_0-1=2$，[]{.arithmatex}$b_0-1=1$；[]{.arithmatex}$a_0=3$，[]{.arithmatex}$b_2=2$；[]{.arithmatex}$a=6$，[]{.arithmatex}$b=4$。

当 []{.arithmatex}$d=3$ 时，

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{rcl} a_0b_0+a_0+b_0+1&=&3a_0b_0\\ 2a_0b_0-a_0-b_0&=&1\\ 4a_0b_0-2a_0-2b_0&=&2\\ 2a_0(2b_0-1)-(2b_0-1)&=&3\\ (2a_0-1)(2b_0-1)&=&3\\ \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{rcl}
a_0b_0+a_0+b_0+1&=&3a_0b_0\\
2a_0b_0-a_0-b_0&=&1\\
4a_0b_0-2a_0-2b_0&=&2\\
2a_0(2b_0-1)-(2b_0-1)&=&3\\
(2a_0-1)(2b_0-1)&=&3\\
\end{array}$$
::::

- []{.arithmatex}$2a_0-1=1$，[]{.arithmatex}$2b_0-1=3$；[]{.arithmatex}$a_0=1$，[]{.arithmatex}$b_2=2$；[]{.arithmatex}$a=3$，[]{.arithmatex}$b=6$。
- []{.arithmatex}$2a_0-1=3$，[]{.arithmatex}$2b_0-1=1$；[]{.arithmatex}$a_0=2$，[]{.arithmatex}$b_2=1$；[]{.arithmatex}$a=6$，[]{.arithmatex}$b=3$。

当 []{.arithmatex}$d=4$ 时，

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\arraystretch{1.1} \begin{array}{rcl} a_0b_0+a_0+b_0+1&=&4a_0b_0\\ 3a_0b_0-a_0-b_0&=&1\\ 9a_0b_0-3a_0-3b_0&=&3\\ 3a_0(3b_0-1)-(3b_0-1)&=&4\\ (3a_0-1)(3b_0-1)&=&4\\ \end{array}
:::

$$\def\arraystretch{1.1}
\begin{array}{rcl}
a_0b_0+a_0+b_0+1&=&4a_0b_0\\
3a_0b_0-a_0-b_0&=&1\\
9a_0b_0-3a_0-3b_0&=&3\\
3a_0(3b_0-1)-(3b_0-1)&=&4\\
(3a_0-1)(3b_0-1)&=&4\\
\end{array}$$
::::

- []{.arithmatex}$3a_0-1=2$，[]{.arithmatex}$3b_0-1=2$；[]{.arithmatex}$a_0=b_0=1$；[]{.arithmatex}$a=b=4$。
- []{.arithmatex}$2a_0-1=1$，[]{.arithmatex}$2b_0-1=4$；不存在整数解。
- []{.arithmatex}$2a_0-1=4$，[]{.arithmatex}$2b_0-1=1$；不存在整数解。

因此，可行解有：

:::: {.arithmatex}
::: {.MathJax_Preview}
(a,b)=(4,6),(6,4),(3,6),(6,3),(4,4)
:::

$$(a,b)=(4,6),(6,4),(3,6),(6,3),(4,4)$$
::::
