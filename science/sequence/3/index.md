# 数列进阶 {#_1}

## 回顾及补充 {#_2}

### 经典常量 {#_3}

::: {.arithmatex}
\$\$ \pi\approx3.14159 \$\$
:::

::: {.arithmatex}
\$\$ e\approx2.71828 \$\$
:::

::: {.arithmatex}
\$\$ \gamma\approx0.57721 \$\$
:::

::: {.arithmatex}
\$\$ \varphi={1+\sqrt5\over2}\approx1.61803 \$\$
:::

::: {.arithmatex}
\$\$ \hat\varphi={1-\sqrt5\over2}\approx-.61803 \$\$
:::

### 基础公式 {#_4}

一些公式，

::: {.arithmatex}
\$\$ \sum\_{i=1}\^ni={n(n+1)\over2} \$\$
:::

::: {.arithmatex}
\$\$ \sum\_{i=1}\^ni\^2={n(n+1)(2n+1)\over6}={n(n+1/2)(n+1)\over3} \$\$
:::

::: {.arithmatex}
\$\$ \sum\_{i=1}\^ni\^3=\left\[{n(n+1)\over2}\right\]\^2={n\^2(n+1)\^2\over4} \$\$
:::

可以通过扰动法（见下）或者待定系数并归纳得出。

::: {.arithmatex}
\$\$ \sum\_{i=0}\^nc\^i={c\^{n+1}-1\over c-1},c\neq1 \$\$
:::

::: {.arithmatex}
\$\$ \sum\_{i\ge0}c\^i={1\over 1-c},\|c\|\<1 \$\$
:::

::: {.arithmatex}
\$\$ \sum\_{i\ge1}c\^i={c\over 1-c},\|c\|\<1 \$\$
:::

上面的是等比数列，下面的用极限得出。

::: {.arithmatex}
\$\$ \sum\_{i=0}\^nic\^i={nc\^{n+2}-(n-1)c\^{n+1}+c\over(c-1)\^2},c\neq1 \$\$
:::

::: {.arithmatex}
\$\$ \sum\_{i\ge0}ic\^i={c\over(1-c)\^2},\|c\|\<1 \$\$
:::

上面的可以扰动法得出，下面的极限得出。

### 调和级数 {#_5}

::: {.arithmatex}
\$\$ H_n=\sum\_{i=1}\^n{1\over i} \$\$
:::

有，

::: {.arithmatex}
\$\$ \ln n\<H_n\<\ln n+1 \$\$
:::

::: {.arithmatex}
\$\$ H_n=\ln n+\gamma+\mathcal O\left({1\over n}\right) \$\$
:::

同时，

::: {.arithmatex}
\$\$ \sum\_{i=1}\^nH_i=(n+1)H_n-n \$\$
:::

::: {.arithmatex}
\$\$ \sum\_{i=1}\^niH_i={n(n+1)\over2}H_n-{n(n-1)\over4} \$\$
:::

::: {.arithmatex}
\$\$ \sum\_{i=1}\^n{i\choose m}H_i={n+1\choose m+1}\left(H\_{n+1}-{1\over m+1}\right) \$\$
:::

证明下面再说。

### 欧拉公式 {#_6}

::: {.arithmatex}
\$\$ \def\ff#1{{1\over#1\^2}} {\pi\^2\over6}=\ff1+\ff2+\ff3+\ff4+\ff5+\dots \$\$
:::

::: {.arithmatex}
\$\$ \def\ff#1{{1\over#1\^2}} {\pi\^2\over8}=\ff1+\ff3+\ff5+\ff7+\ff9+\dots \$\$
:::

### 组合数学 {#_7}

见我的排列组合笔记。

::: {.arithmatex}
\$\$ \def\qq{\quad} \begin{array}{c} 1\\ 1\qq1\\ 1\qq2\qq1\\ 1\qq3\qq3\qq1\\ 1\qq4\qq6\qq4\qq1\\ 1\qq5\qq10\qq10\qq5\qq1\\ 1\qq6\qq15\qq20\qq15\qq6\qq1\\ 1\qq7\qq21\qq35\qq35\qq21\qq7\qq1\\ 1\qq8\qq28\qq56\qq70\qq56\qq28\qq8\qq1\\ 1\qq9\qq36\qq84\qq126\qq126\qq84\qq36\qq9\qq1\\ 1\qq10\qq45\qq120\qq210\qq252\qq210\qq120\qq45\qq10\qq1\\ \end{array} \$\$
:::

### 线代基础 {#_8}

::: {.arithmatex}
\$\$ \left\lvert\begin{matrix}a&b\\c&d\end{matrix}\right\rvert=ad+bc \$\$
:::

::: {.arithmatex}
\$\$ \det A=\sum\_{\pi\in S_n}\operatorname{sgn}(\pi)\prod\_{i=1}\^na\_{i,\pi(i)} \$\$
:::
