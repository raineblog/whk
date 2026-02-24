# 数列基础全攻略：从概念到高级技巧 {#_1}

本篇博文梳理了数列的核心概念与常用方法，涵盖无限与有限数列、等差、等比、裂项放缩以及变量换元等专题。通过直观示例和简练公式，帮助高中生、竞赛爱好者以及自学者在短时间内建立完整的数列框架，进一步提升解题效率。

## 基础概念 {#_2}

数列是一组按顺序排列的数值，每一个位置称为 **项**。根据项数的不同，可分为 **无限数列** 与 **有限数列**。

### 无穷数列 {#_3}

若 [\$a:\mathbb N\to\mathbb C\$]{.arithmatex} 为函数，则记为

::: {.arithmatex}
\$\$ \\a_n\\\_{n\in\mathbb N}\quad\text{或}\quad(a_n)\_{n\in\mathbb N} \$\$
:::

其中 [\$a_n\$]{.arithmatex} 为第 [\$n\$]{.arithmatex} 项。

### 有限数列 {#_4}

设 [\$I_n=\\1,2,\dots ,n\\\$]{.arithmatex}，则函数 [\$a:I_n\to\mathbb C\$]{.arithmatex} 称为 **有限数列**，记作 [\$\\a_i\\\_{i=1}\^{n}\$]{.arithmatex}。

### 数列的级数 {#_5}

数列的逐项累加得到的序列称为 **级数**，记为

::: {.arithmatex}
\$\$ S_n=\sum\_{i=1}\^{n}a_i \$\$
:::

[\$S_n\$]{.arithmatex} 的递推关系为 [\$S_n=S\_{n-1}+a_n\$]{.arithmatex}（[\$S_0=0\$]{.arithmatex}）。

### 数列与函数 {#_6}

数列本质是离散函数，常用 [\$a_n=f(n)\$]{.arithmatex} 表示其通项。由此可以把求和、差分等运算类比为积分、微分的离散版。

## 表示方法 {#_7}

### 列举法 {#_8}

直接写出前几项，如 [\$\langle 1,2,4,8,\dots\rangle\$]{.arithmatex}。适用于短序列，无法完整描述无限数列。

### 图像法 {#_9}

把每一项对应的点绘于平面，仅能呈现离散散点，实际教学中不常使用。

### 通项公式 {#_10}

用代数式揭示 [\$n\$]{.arithmatex} 与 [\$a_n\$]{.arithmatex} 的关系。例如等比数列 [\$a_n=a_1q\^{\\n-1}\$]{.arithmatex}。

### 递推公式 {#_11}

用前一项或前几项描述后继项，如

::: {.arithmatex}
\$\$ a\_{n+1}=a_n+d \quad\text{（等差）} \$\$
:::

或

::: {.arithmatex}
\$\$ a\_{n+1}=qa_n \quad\text{（等比）} \$\$
:::

## 等差数列 {#_12}

相邻两项的差恒为常数 [\$d\$]{.arithmatex}，称为 **公差**。

### 递推公式 {#_13}

::: {.arithmatex}
\$\$ a\_{n+1}=a_n+d\qquad (n\ge 1) \$\$
:::

### 通项公式 {#_14}

::: {.arithmatex}
\$\$ a_n=a_1+(n-1)d \$\$
:::

### 等差性质 {#_15}

- 前后项差：[\$d=\dfrac{a_n-a_m}{\\n-m\\}\$]{.arithmatex}
- 中项等式：[\$a_n=\dfrac{a\_{n-1}+a\_{n+1}}{2}\$]{.arithmatex}
- 任意两项之和相等：若 [\$m+n=p+q\$]{.arithmatex}，则 [\$a_m+a_n=a_p+a_q\$]{.arithmatex}。

### 项数公式 {#_16}

已知首项 [\$a_1\$]{.arithmatex} 与第 [\$k\$]{.arithmatex} 项 [\$a_k\$]{.arithmatex}，可求项数

::: {.arithmatex}
\$\$ k=\frac{a_k-a_1}{d}+1 \$\$
:::

### 求和公式 {#_17}

等差前 [\$n\$]{.arithmatex} 项和为

::: {.arithmatex}
\$\$ S_n=\frac{n\bigl(a_1+a_n\bigr)}{2} =na_1+\frac{n(n-1)}{2}d \$\$
:::

把 [\$S_n\$]{.arithmatex} 看作二次函数 [\$S_n=\frac{d}{2}n\^{2}+\bigl(a_1-\frac{d}{2}\bigr)n\$]{.arithmatex}，可直接求极值位置。

### 等差中项 {#_18}

给定两端 [\$a,b\$]{.arithmatex}，中项 [\$c\$]{.arithmatex} 为算术平均数：

::: {.arithmatex}
\$\$ c=\frac{a+b}{2} \$\$
:::

### 累加法 {#_19}

若递推式 [\$a_n=a\_{n-1}+f(n)\$]{.arithmatex}，则

::: {.arithmatex}
\$\$ a_n=a_1+\sum\_{k=2}\^{n}f(k) \$\$
:::

### 多阶等差 {#_20}

对公差再求前缀和可得到二阶等差数列；若两阶数列相乘仍保持二阶结构。

## 等比数列 {#_21}

相邻两项的比值恒为常数 [\$q\$]{.arithmatex}，称为 **公比**。

### 递推公式 {#_22}

::: {.arithmatex}
\$\$ a\_{n+1}=qa_n\qquad (q\neq0) \$\$
:::

### 通项公式 {#_23}

::: {.arithmatex}
\$\$ a_n=a_1q\^{\\n-1} \$\$
:::

### 等比性质 {#_24}

- 前后项积：[\$a\_{n-1}a\_{n+1}=a_n\^{2}\$]{.arithmatex}
- 任意两项乘积相等：若 [\$m+n=p+q\$]{.arithmatex}，则 [\$a_m a_n=a_p a_q\$]{.arithmatex}。

### 求和公式 {#_25}

若 [\$q\neq1\$]{.arithmatex}，前 [\$n\$]{.arithmatex} 项和为

::: {.arithmatex}
\$\$ S_n=a_1\frac{q\^{\\n}-1}{q-1} \$\$
:::

若 [\$q=1\$]{.arithmatex}，则 [\$S_n=na_1\$]{.arithmatex}。

### 等比中项 {#_26}

两端 [\$a,b\$]{.arithmatex} 的几何平均数为中项：

::: {.arithmatex}
\$\$ c=\sqrt{ab} \$\$
:::

### 累乘法 {#_27}

若递推式 [\$a_n=a\_{n-1}f(n)\$]{.arithmatex}，则

::: {.arithmatex}
\$\$ a_n=a_1\prod\_{k=2}\^{n}f(k) \$\$
:::

## 裂项放缩 {#_28}

通过把复杂分式拆成差的形式，可以让求和过程出现大量相消项。

### 经典裂项 {#_29}

::: {.arithmatex}
\$\$ \frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1} \$\$
:::

### 整式裂项 {#_30}

利用立方或高次多项式的差分进行拆分，如

::: {.arithmatex}
\$\$ n(n+1)=\frac{1}{3}\Bigl\[n(n+1)(n+2)-(n-1)n(n+1)\Bigr\] \$\$
:::

从而得到

::: {.arithmatex}
\$\$ \sum\_{k=1}\^{n}k(k+1)=\frac{n(n+1)(n+2)}{3} \$\$
:::

### 更多裂项 {#_31}

包括根式、阶乘以及高次幂的裂项，例如

::: {.arithmatex}
\$\$ \frac{1}{\sqrt{a}+\sqrt{b}} =\frac{\sqrt{a}-\sqrt{b}}{a-b} \$\$
:::

以及

::: {.arithmatex}
\$\$ \frac{2\^{k}}{2k\^{4}+1} =\frac{1}{2k\^{2}-2k+1}-\frac{1}{2k\^{2}+2k+1} \$\$
:::

### 共轭根式 {#_32}

利用 [\$(\sqrt a-\sqrt b)(\sqrt a+\sqrt b)=a-b\$]{.arithmatex}，可快速化简含根号的分式。

### 阶乘问题 {#_33}

典型恒等式

::: {.arithmatex}
\$\$ n\cdot n!=(n+1)!-n! \$\$
:::

帮助把阶乘序列转化为差分形式。

### 放缩基础与进阶 {#_34}

对于收敛性或渐进估计，常用不等式

::: {.arithmatex}
\$\$ \frac{1}{n}-\frac{1}{n+1}\<\frac{1}{n\^{2}}\<\frac{1}{n-1}-\frac{1}{n} \$\$
:::

进一步可以使用根号不等式

::: {.arithmatex}
\$\$ \frac{1}{\sqrt{n}}\<2\bigl(\sqrt{n+1}-\sqrt{n}\bigr) \$\$
:::

提升估计精度。

## 通用方法 {#_35}

### 速算技巧 {#_36}

- 把 [\$S_0\$]{.arithmatex} 设为 [\$0\$]{.arithmatex}，有时可直接求出常数项。
- 当级数满足 [\$S_n=a\cdot2\^{\\n-1}+a-2\$]{.arithmatex} 时，令 [\$n=0\$]{.arithmatex} 求 [\$a\$]{.arithmatex}。

### 等差等比混合 {#_37}

若数列形如 [\$a_n=(An+B)q\^{\\n-1}\$]{.arithmatex}，可化为

::: {.arithmatex}
\$\$ S_n=(Dn+E)q\^{\\n}-E \$\$
:::

其中 [\$D=\dfrac{A}{q-1}\$]{.arithmatex}、[\$E=\dfrac{B-D}{q-1}\$]{.arithmatex}。

### 数学归纳 {#_38}

通过基例与归纳假设，验证递推式的通项公式。

### 直接变形 {#_39}

把递推式两边加（或减）常数，使其转化为等比形式。例如 [\$a_n=pa\_{n-1}+q\$]{.arithmatex}，取 [\$x=\dfrac{q}{p-1}\$]{.arithmatex}，则 [\$b_n=a_n+x\$]{.arithmatex} 为等比数列。

### 变形累加 {#_40}

对 [\$a_n=pa\_{n-1}+q\$]{.arithmatex} 两边除以 [\$p\^{\\n}\$]{.arithmatex}，再累加得到

::: {.arithmatex}
\$\$ a_n=(a_1-q)p\^{\\n-1}+ \frac{q}{p-1}\bigl(p\^{\\n}-1\bigr) \$\$
:::

### 数列判定 {#_41}

- **定义法**：检验 [\$a_n-a\_{n-1}\$]{.arithmatex}（等差）或 [\$\dfrac{a_n}{a\_{n-1}}\$]{.arithmatex}（等比）是否为常数。
- **中项法**：等差满足 [\$2a_n=a\_{n-1}+a\_{n+1}\$]{.arithmatex}，等比满足 [\$a_n\^{2}=a\_{n-1}a\_{n+1}\$]{.arithmatex}。

### 奇偶数列 {#_42}

对交错符号或绝对值数列，可分别讨论正负段的和，从而得到整体求和公式。

### 单调性 {#_43}

若 [\$a\_{n+1}\ge a_n\$]{.arithmatex}（或 [\$\>\$]{.arithmatex}）则称为单调递增；若 [\$a\_{n+1}\le a_n\$]{.arithmatex}（或 [\$\<\$]{.arithmatex}）则为单调递减。迭代式 [\$a\_{n+1}=f(a_n)\$]{.arithmatex} 的单调性可通过 [\$f\'(x)\$]{.arithmatex} 的符号判断。

## 换元初步 {#_44}

### 三角换元 {#_45}

常用恒等式：

::: {.arithmatex}
\$\$ \cos2\theta=2\cos\^{2}\theta-1,\qquad \tan2\theta=\frac{2\tan\theta}{1-\tan\^{2}\theta} \$\$
:::

帮助把二次递推转化为角度倍增。

### 例题（三角换元） {#_46}

递推 [\$a\_{n+1}=a_n\^{2}-2\$]{.arithmatex}，取 [\$a_n=2\cos\theta_n\$]{.arithmatex}，得到 [\$\theta\_{n+1}=2\theta_n\$]{.arithmatex}，于是

::: {.arithmatex}
\$\$ a_n=2\cos\\\Bigl(2\^{\\n-1}\arccos\frac14\Bigr) \$\$
:::

### 双曲换元 {#_47}

递推 [\$a\_{n+1}=2a_n\^{2}-1\$]{.arithmatex}，令 [\$a_n=\dfrac{k\^{x}+k\^{-x}}{2}\$]{.arithmatex}，得到

::: {.arithmatex}
\$\$ a_n=\frac{(3+2\sqrt2)\^{\\2\^{\\n-1}}+(3-2\sqrt2)\^{\\2\^{\\n-1}}}{2} \$\$
:::

## 基础例题精选 {#_48}

下面列出四道常见递推题的快速求解过程，帮助读者熟悉技巧。

### 例题一 {#_49}

递推 [\$a_n=2a\_{n-1}+3\\(n\ge2),\\ a_1=1\$]{.arithmatex}。  
加上常数 [\$3\$]{.arithmatex} 后得到等比数列 [\$b_n=a_n+3=2\^{\\n+1}\$]{.arithmatex}，故

::: {.arithmatex}
\$\$ a_n=2\^{\\n+1}-3 \$\$
:::

### 例题二 {#_50}

递推 [\$a_n=a\_{n-1}+n\\(n\ge2),\\ a_1=1\$]{.arithmatex}。  
累加得到

::: {.arithmatex}
\$\$ a_n=1+2+\dots +n=\frac{n(n+1)}{2} \$\$
:::

### 例题三 {#_51}

递推 [\$a_n=2a\_{n-1}+n\\(n\ge2),\\ a_1=1\$]{.arithmatex}。  
除以 [\$2\^{\\n}\$]{.arithmatex}，累加后化简得

::: {.arithmatex}
\$\$ a_n=2\^{\\n+1}-2-n \$\$
:::

### 例题四 {#_52}

递推 [\$a_n=2a\_{n-1}+n\^{2}\\(n\ge2),\\ a_1=1\$]{.arithmatex}。  
同样除以 [\$2\^{\\n}\$]{.arithmatex}，经过差分与累加，最终得到

::: {.arithmatex}
\$\$ a_n=3\cdot2\^{\\n+1}-n\^{2}-4n-6 \$\$
:::

------------------------------------------------------------------------

想要深入了解每个章节的完整推导、更多练习以及完整的原始手稿，请访问原文链接：

[数列基础原文（完整版）](https://raineblog.dpdns.org/whk/science/sequence/1/)

祝你在数列的世界里玩得开心，收获满满！
