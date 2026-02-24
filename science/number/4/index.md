# 数论测试 {#_1}

## 一、请给出整除的概念及性质 {#_2}

对于整数 [\$a,b\$]{.arithmatex} [\$(b\neq0)\$]{.arithmatex}，如果存在整数 [\$c\$]{.arithmatex}，使得 [\$a=bc\$]{.arithmatex}，

则称 [\$b\$]{.arithmatex} 整除 [\$a\$]{.arithmatex}，记作 [\$b \mid a\$]{.arithmatex}；否则称 [\$b\$]{.arithmatex} 不整除 [\$a\$]{.arithmatex}，记作 [\$b \nmid a\$]{.arithmatex}。

**性质**：

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{rlrl} 1.&a\mid b&\Longrightarrow&\pm a \mid \pm b\\ 2.&a \mid b,\\ b\mid c&\Longrightarrow&a \mid c\\ 3.&\forall i:b\mid a_i&\Longrightarrow&b\mid\Sigma\\ a_ik_i\\ 4.&b\mid a&\Longrightarrow&bc\mid ac\\ (c\in\mathbb Z,c\neq0)\\ 5.&b\mid a\\ (a\neq0)&\Longrightarrow&\|b\|\le\|a\|\\ 5.&b\mid a,\\ \|a\|\<\|b\|&\Longrightarrow&a=0\\ \end{array} \$\$
:::

### 二、请给出同余的概念及性质 {#_3}

给定正整数 [\$m\$]{.arithmatex} 称为模，[\$a,b\$]{.arithmatex} 为任意两个整数，满足：

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{ll} a=q_1m+r_1,&0\le r_1\<m\\ b=q_2m+r_2,&0\le r_2\<m\\ \end{array} \$\$
:::

则称 [\$a,b\$]{.arithmatex} 对 [\$m\$]{.arithmatex} 同余，记作 [\$a \equiv b \pmod m\$]{.arithmatex}，简记为 [\$a \equiv b\\ (m)\$]{.arithmatex}。

**性质**：

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{rlrl} 1.&a \equiv a \pmod m\\ 2.&a \equiv b \pmod m &\Longleftrightarrow& b\equiv a \pmod m\\ 3.&a\equiv b\pmod m,\\ b\equiv c\pmod m&\Longrightarrow&a\equiv c\pmod m\\ 4.&aK\equiv bK\pmod m&\Longrightarrow&a\equiv b\pmod{\frac{m}{(m,k)}}\\ 5.&a\equiv b\pmod m,\\ c\equiv d\pmod m&\Longrightarrow&a\pm c\equiv b\pm d\pmod m\\ 6.&a\equiv b\pmod m,\\ c\equiv d\pmod m&\Longrightarrow&ac\equiv bd\pmod m\\ \end{array} \$\$
:::

### 三、请给出模 [\$m\$]{.arithmatex} 的完全剩余系的概念 {#m}

若 [\$a_1,a_2,\dots,a_m\$]{.arithmatex} 对模 [\$m\$]{.arithmatex} 两两不同余，则这 [\$m\$]{.arithmatex} 个数构成模 [\$m\$]{.arithmatex} 的一个完全剩余系。

特殊的，任意连续的 [\$m\$]{.arithmatex} 个整数都构成模 [\$m\$]{.arithmatex} 的一个完全剩余系。

### 四、陈述裴蜀定理 {#_4}

对于任意整数 [\$a,b\$]{.arithmatex}，一定存在一组整数解 [\$x,y\$]{.arithmatex} 使得 [\$ax+by=(a,b)\$]{.arithmatex}。

### 五、陈述费马小定理 {#_5}

若 [\$p\$]{.arithmatex} 是素数，则 [\$a\^p\equiv a\pmod p\$]{.arithmatex}。

特别的，若 [\$a\perp p\$]{.arithmatex}，则 [\$a\^{p-1}\equiv1\pmod p\$]{.arithmatex}。

### 六、给定模 [\$m\$]{.arithmatex} 的一组完全剩余系 [\$x_1,\dots,x_m\$]{.arithmatex}，若 [\$a \perp m\$]{.arithmatex}，请证明 [\$ax_1,\dots,ax_m\$]{.arithmatex} 也是模 [\$m\$]{.arithmatex} 的一组完全剩余系 {#m-x_1dotsx_m-a-perp-m-ax_1dotsax_m-m}

**反证**：假设 [\$ax_1,\dots,ax_m\$]{.arithmatex} 不是模 [\$m\$]{.arithmatex} 的完全剩余系。

则一定存在 [\$i\neq j\$]{.arithmatex} 使得 [\$ax_i\equiv ax_j\pmod m\$]{.arithmatex}。

因为 [\$a \perp m\$]{.arithmatex}，因此有 [\$x_i\equiv x_j\pmod m\$]{.arithmatex}。

与 [\$x_1,\dots,x_m\$]{.arithmatex} 为模 [\$m\$]{.arithmatex} 的完全剩余系不符。

假设不成立，故 [\$ax_1,\dots,ax_m\$]{.arithmatex} 是模 [\$m\$]{.arithmatex} 的完全剩余系。

### 七、设 [\$n\$]{.arithmatex} 是整数，请证明：[\$120 \mid n(n\^2-1)(n\^2-5n+26)\$]{.arithmatex} {#n-120-mid-nn2-1n2-5n26}

**定理**：连续 [\$n\$]{.arithmatex} 个整数的乘积一定被 [\$n!\$]{.arithmatex} 整除。

对于这 [\$n\$]{.arithmatex} 个数都是正整数的：

::: {.arithmatex}
\$\$ \begin{array}{l} (a+1)(a+2)\dots(a+n)=\frac{(a+n)!}{a!}=n!\frac{(a+n)!}{n!a!}=n!\binom{a+n}{a} \end{array} \$\$
:::

而如果这 [\$n\$]{.arithmatex} 个数存在不是正整数的，那么一定跨过了 [\$0\$]{.arithmatex}，乘积为 [\$0\$]{.arithmatex}，整除是显然的。

**证明**：

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{ll} &n(n\^2-1)(n\^2-5n+26)\\ =&n(n+1)(n-1)\[(n-2)(n-3)+20\]\\ =&(n-3)(n-2)(n-1)n(n+1)+20(n-1)n(n+1) \end{array} \$\$
:::

因为：

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{rcl} 120&\mid& (n-3)(n-2)(n-1)n(n+1)\\ 6&\mid& (n-1)n(n+1)\\ 120&\mid& 20(n-1)n(n+1) \end{array} \$\$
:::

因此 [\$120\mid(n-3)(n-2)(n-1)n(n+1)+20(n-1)n(n+1)\$]{.arithmatex}。

即 [\$120 \mid n(n\^2-1)(n\^2-5n+26)\$]{.arithmatex}。

### 八、设 [\$n\$]{.arithmatex} 是正整数，且 [\$2n+1\$]{.arithmatex} 与 [\$3n+1\$]{.arithmatex} 都是完全平方数。请证明：[\$40 \mid n\$]{.arithmatex} {#n-2n1-3n1-40-mid-n}

**性质1**：奇数的完全平方数模 [\$8\$]{.arithmatex} 同余于 [\$1\$]{.arithmatex}。

::: {.arithmatex}
\$\$(2k+1)\^2\equiv4k(k+1)+1\equiv1\pmod8\$\$
:::

**性质2**：任何一个数的平方模 [\$5\$]{.arithmatex} 同余于 [\$0,\pm1\$]{.arithmatex}。

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{lcll} t&\equiv&0,\pm1,\pm2&\pmod5\\ t\^2&\equiv&0,\pm1&\pmod5 \end{array} \$\$
:::

**证明**：

因为 [\$2n+1\$]{.arithmatex} 是奇数且是完全平方数，则

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{rcll} 2n+1&\equiv&1&\pmod8\\ n&\equiv&0&\pmod4 \end{array} \$\$
:::

所以，[\$n\$]{.arithmatex} 是偶数，[\$3n+1\$]{.arithmatex} 是奇数且是完全平方数，则

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{rcll} 3n+1&\equiv&1&\pmod8\\ n&\equiv&0&\pmod8 \end{array} \$\$
:::

且

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{rcll} 2n+1&\equiv&0,\pm1&\pmod5\\ 3n+1&\equiv&0,\pm1&\pmod5 \end{array} \$\$
:::

则有

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{rcll} (2n+1)+(3n+1)&\equiv&2&\pmod5\\ 2n+1&\equiv&1&\pmod5\\ 3n+1&\equiv&1&\pmod5\\ n&\equiv&0&\pmod5 \end{array} \$\$
:::

因此 [\$n\equiv0\pmod{40}\$]{.arithmatex}，即 [\$40 \mid n\$]{.arithmatex}。

### 九、求 [\$10\^{10} \bmod 7\$]{.arithmatex} {#1010-bmod-7}

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{ll} &10\^{10} \bmod 7\\ =&(10 \bmod 7)\^{10\bmod 6}\bmod 7\\ =&3\^4\bmod7\\ =&81\bmod7\\ =&4 \end{array} \$\$
:::

即 [\$10\^{10}\bmod7=4\$]{.arithmatex}。

### 十、求满足以下条件的正整数解：[\$(a,b)+\[a,b\]+a+b=ab\$]{.arithmatex} {#abababab}

设 [\$d=(a,b)\$]{.arithmatex}，则记 [\$a=a_0d\$]{.arithmatex}，[\$b=b_0d\$]{.arithmatex}（[\$a_0\perp b_0\$]{.arithmatex}）。

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{rcl} (a,b)+\[a,b\]+a+b&=&ab\\ d+a_0b_0d+a_0d+b_0d&=&a_0b_0d\^2\\ a_0b_0+a_0+b_0+1&=&a_0b_0d \end{array} \$\$
:::

因为 [\$a_0b_0\ge a_0b_0,a_0,b_0\ge1\$]{.arithmatex}，所以 [\$0\<d\le4\$]{.arithmatex}。

当 [\$d=1\$]{.arithmatex} 时，[\$a_0+b_0+1=0\$]{.arithmatex}，无解。

当 [\$d=2\$]{.arithmatex} 时，

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{rcl} a_0b_0+a_0+b_0+1&=&2a_0b_0\\ a_0b_0-a_0-b_0&=&1\\ a_0(b_0-1)-(b_0-1)&=&2\\ (a_0-1)(b_0-1)&=&2\\ \end{array} \$\$
:::

- [\$a_0-1=1\$]{.arithmatex}，[\$b_0-1=2\$]{.arithmatex}；[\$a_0=2\$]{.arithmatex}，[\$b_2=3\$]{.arithmatex}；[\$a=4\$]{.arithmatex}，[\$b=6\$]{.arithmatex}。
- [\$a_0-1=2\$]{.arithmatex}，[\$b_0-1=1\$]{.arithmatex}；[\$a_0=3\$]{.arithmatex}，[\$b_2=2\$]{.arithmatex}；[\$a=6\$]{.arithmatex}，[\$b=4\$]{.arithmatex}。

当 [\$d=3\$]{.arithmatex} 时，

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{rcl} a_0b_0+a_0+b_0+1&=&3a_0b_0\\ 2a_0b_0-a_0-b_0&=&1\\ 4a_0b_0-2a_0-2b_0&=&2\\ 2a_0(2b_0-1)-(2b_0-1)&=&3\\ (2a_0-1)(2b_0-1)&=&3\\ \end{array} \$\$
:::

- [\$2a_0-1=1\$]{.arithmatex}，[\$2b_0-1=3\$]{.arithmatex}；[\$a_0=1\$]{.arithmatex}，[\$b_2=2\$]{.arithmatex}；[\$a=3\$]{.arithmatex}，[\$b=6\$]{.arithmatex}。
- [\$2a_0-1=3\$]{.arithmatex}，[\$2b_0-1=1\$]{.arithmatex}；[\$a_0=2\$]{.arithmatex}，[\$b_2=1\$]{.arithmatex}；[\$a=6\$]{.arithmatex}，[\$b=3\$]{.arithmatex}。

当 [\$d=4\$]{.arithmatex} 时，

::: {.arithmatex}
\$\$ \def\arraystretch{1.1} \begin{array}{rcl} a_0b_0+a_0+b_0+1&=&4a_0b_0\\ 3a_0b_0-a_0-b_0&=&1\\ 9a_0b_0-3a_0-3b_0&=&3\\ 3a_0(3b_0-1)-(3b_0-1)&=&4\\ (3a_0-1)(3b_0-1)&=&4\\ \end{array} \$\$
:::

- [\$3a_0-1=2\$]{.arithmatex}，[\$3b_0-1=2\$]{.arithmatex}；[\$a_0=b_0=1\$]{.arithmatex}；[\$a=b=4\$]{.arithmatex}。
- [\$2a_0-1=1\$]{.arithmatex}，[\$2b_0-1=4\$]{.arithmatex}；不存在整数解。
- [\$2a_0-1=4\$]{.arithmatex}，[\$2b_0-1=1\$]{.arithmatex}；不存在整数解。

因此，可行解有：

::: {.arithmatex}
\$\$ (a,b)=(4,6),(6,4),(3,6),(6,3),(4,4) \$\$
:::
