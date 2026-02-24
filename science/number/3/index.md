# 数论入门 {#_1}

## 因数 {#_2}

### 整除 {#_3}

若 []{.arithmatex}$b$ 能整除 []{.arithmatex}$a$，则记为 []{.arithmatex}$a\mid b$，如 []{.arithmatex}$2\mid 12$. 若 []{.arithmatex}$b$ 不能整除 []{.arithmatex}$a$，则记为 []{.arithmatex}$a\nmid b$，如 []{.arithmatex}$5\nmid 12$.

若 []{.arithmatex}$a\nmid b$，则 []{.arithmatex}$b\div a$ 存在余数 []{.arithmatex}$r$ 且 []{.arithmatex}$0<r<a$，记 []{.arithmatex}$r=a\ \mathrm{mod}\ b$. 例如，[]{.arithmatex}$3\ \mathrm{mod}\ 2=1$.

整除具有以下性质：

1.  若 []{.arithmatex}$a\mid b$ 且 []{.arithmatex}$a\mid c$，则 []{.arithmatex}$\forall x,y$，有 []{.arithmatex}$a\mid xb+yc$.
2.  若 []{.arithmatex}$a\mid b$ 且 []{.arithmatex}$b\mid c$，则 []{.arithmatex}$a\mid c$.
3.  若 []{.arithmatex}$a\mid b$ 且 []{.arithmatex}$b\mid a$，则 []{.arithmatex}$a=\pm b$.
4.  设 []{.arithmatex}$m\neq 0$，则 []{.arithmatex}$a\mid b$，当且仅当 []{.arithmatex}$ma\mid mb$.

### 最大公因数与最小公倍数 {#_4}

设 []{.arithmatex}$a,b$ 是两个不为 []{.arithmatex}$0$ 的整数，能使 []{.arithmatex}$d\mid a$ 和 []{.arithmatex}$d\mid b$ 成立的最大整数 []{.arithmatex}$d$，称为 []{.arithmatex}$a,b$ 的最大公因数，记作 []{.arithmatex}$\gcd(a,b)$.

设 []{.arithmatex}$a,b$ 是两个不为 []{.arithmatex}$0$ 的整数，能使 []{.arithmatex}$a\mid d$ 和 []{.arithmatex}$b\mid d$ 成立的最小整数 []{.arithmatex}$d$，称为 []{.arithmatex}$a,b$ 的最小公倍数，记作 []{.arithmatex}$\mathrm{lcm}(a,b)$.

- []{.arithmatex}$\forall a,b\in\N,\ \gcd(a,b)\cdot\mathrm{lcm}(a,b)=ab$

证明：设 []{.arithmatex}$\displaystyle d=\gcd(a,b),a_0=\frac{a}{d},b_0=\frac{b}{d}$. 根据最大公因数的定义，有 []{.arithmatex}$\gcd(a_0,b_0)=1$。[]{.arithmatex}$\\\ \ \ \ \ \ \ \ \ \text{}$ 再根据最小公倍数的定义，有 []{.arithmatex}$\mathrm{lcm}(a,b)=a_0\cdot b_0$. []{.arithmatex}$\\\ \ \ \ \ \ \ \ \ \text{}$ 于是 []{.arithmatex}$\displaystyle\mathrm{lcm}(a,b)=\mathrm{lcm}(a_0\cdot d,b_0\cdot d)=\mathrm{lcm}(a_0,b_0)\cdot d=a_0\cdot b_0\cdot d=\frac{a\cdot b}{d}$，原命题得证。

- 九章算术 更相减损术： []{.arithmatex}$\gcd(a,b)=\gcd(b,a-b)=\gcd(a,a-b),\gcd(2a,2b)=2\gcd(a,b)$.

证明：[]{.arithmatex}$d\mid a,d\mid b\implies d\mid(a-b)$.

- 欧几里得算法：[]{.arithmatex}$\forall a,b\in\N,b\neq 0,\gcd(a,b)=\gcd(b,a\ \mathrm{mod}\ b)$.

证明：分类讨论。

1.  若 []{.arithmatex}$a<b$，则有 []{.arithmatex}$\gcd(b,a\ \mathrm{mod}\ b)=\gcd(b,a)=\gcd(a,b)$.
2.  若 []{.arithmatex}$a\geq b$，不妨设 []{.arithmatex}$a=q\cdot b+r\ (0\leq r<b)$。显然 []{.arithmatex}$r=a\ \mathrm{mod}\ b$. 对于 []{.arithmatex}$a,b$ 的任意公因数 []{.arithmatex}$d$，[]{.arithmatex}$\\$ 因为 []{.arithmatex}$d\mid a,d\mid q\cdot b$，故 []{.arithmatex}$d\mid (a-q\cdot b)$，即 []{.arithmatex}$d\mid r$. 因此 []{.arithmatex}$d$ 也是 []{.arithmatex}$b,r$ 的公因数，反之亦成立。[]{.arithmatex}$\\$ 故 []{.arithmatex}$a,b$ 的公因数集合与 []{.arithmatex}$b,a\ \mathrm{mod}\ b$ 的公因数集合相同。于是它们的最大公因数也相等。

## 裴蜀定理 {#_5}

设 []{.arithmatex}$a,b\in\Z,ab\neq 0$，则 []{.arithmatex}$\exist x,y\in\Z$ 使 []{.arithmatex}$ax+by=\gcd(a,b)=a(x+bu)+b(y-au)$

由上易推出两个**整数 []{.arithmatex}**$a,b$ 互素的充分必要条件是 []{.arithmatex}$\exist x,y\in\Z$ 使得 []{.arithmatex}$ax+by=1$。

比如要证明 []{.arithmatex}$21n+4$ 与 []{.arithmatex}$14n+3$ 互素，知道 []{.arithmatex}$3(14n+3)-2(21n+4)=1$ 即可。

例 1：证明 []{.arithmatex}$n!+1$ 与 []{.arithmatex}$(n+1)!+1$ 互素。

有 []{.arithmatex}$(n+1)(n!+1)-[(n+1)!+1]=n$，于是 []{.arithmatex}$[d=\gcd(n!+1,(n+1)!+1)]|n$，又因为 []{.arithmatex}$d|n!$，结合 []{.arithmatex}$d|(n!+1)$ 得到 []{.arithmatex}$d=1$，原命题得证。

------------------------------------------------------------------------

例 2：记费马数 []{.arithmatex}$F_k=2^{2^k}+1,k\geq 0$，证明若 []{.arithmatex}$m\neq n$ 则 []{.arithmatex}$\gcd(F_m,F_n)=1$.

设 []{.arithmatex}$m>n$，只要利用 []{.arithmatex}$F_n|(F_m-2)$ 证明 []{.arithmatex}$\exist x\in\Z$ 使得 []{.arithmatex}$F_m+xF_n=2$【基本技巧例 2】

设 []{.arithmatex}$[d=\gcd(F_m,F_n)]|2$. []{.arithmatex}$F_n$ 显然为奇数故 []{.arithmatex}$d=1$. 因此**费马数两两互素。**

------------------------------------------------------------------------

例 3：设 []{.arithmatex}$a>1,m,n>0$，证明 []{.arithmatex}$\boxed{\gcd(a^m-1,a^n-1)=a^{\gcd(m,n)}-1}$

令 []{.arithmatex}$D=\gcd(a^m-1,a^n-1)$，只要证明 []{.arithmatex}$[a^{\gcd(m,n)}-1]|D$ 及 []{.arithmatex}$D|[a^{\gcd(m,n)}-1]$ 即可。

显然 []{.arithmatex}$[a^{\gcd(m,n)}-1]|(a^m-1)$ 和 []{.arithmatex}$[a^{\gcd(m,n)}-1]|(a^n-1)$，可以证明 []{.arithmatex}$[a^{\gcd(m,n)}-1]|D$.

设 []{.arithmatex}$d=\gcd(m,n)$，可选 []{.arithmatex}$u,v>0$，使 []{.arithmatex}$mu-nv=d$. 因此 []{.arithmatex}$D|(a^m-1),D|(a^{mu}-1)$，扩展开来 []{.arithmatex}$D|(a^{mu}-a^{nv})=a^{nv}(a^d-1)$，故 []{.arithmatex}$D|(a^d-1)$. 综合上述原命题得证。

------------------------------------------------------------------------

例 4：设 []{.arithmatex}$m,n>0,mn|(m^2+n^2)$，证明 []{.arithmatex}$m=n$.

设 []{.arithmatex}$\gcd(m,n)=d,m=m_1d,n=n_1d,\gcd(m_1,n_1)=1$①. 已知化为 []{.arithmatex}$m_1n_1|(m_1^2+n_1^2)$，从而 []{.arithmatex}$m_1|n_1^2,n_1|m_1^2$. 结合①可得 []{.arithmatex}$m_1=n_1=1,m=n$.

------------------------------------------------------------------------

例 5：设 []{.arithmatex}$k$ 为正奇数，证明 []{.arithmatex}$\displaystyle\sum_{i=1}^ni$ 整除 []{.arithmatex}$\displaystyle\sum_{i=1}^ni^k$.

等价于证明 []{.arithmatex}$n|2\displaystyle\sum_{i=1}^ni^k$ 和 []{.arithmatex}$(n+1)|2\displaystyle\sum_{i=1}^ni^k$，显然

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned}2\sum\_{i=1}\^ni\^k&=\[1\^k+(n-1)\^k\]+\[2\^k+(n-2)\^k\]+\dots+\[(n-1)\^k+1\^k\]+2n\^k\\&=\[1\^k+n\^k\]+\[2\^k+(n-1)\^k\]+\dots+\[n\^k+1\^k\]\end{aligned}
:::

$$\begin{aligned}2\sum_{i=1}^ni^k&=[1^k+(n-1)^k]+[2^k+(n-2)^k]+\dots+[(n-1)^k+1^k]+2n^k\\&=[1^k+n^k]+[2^k+(n-1)^k]+\dots+[n^k+1^k]\end{aligned}$$
::::

是 []{.arithmatex}$n$ 和 []{.arithmatex}$n+1$ 的倍数。

由上可知，为了证明 []{.arithmatex}$b|a$，只需将 []{.arithmatex}$b$ 分解成若干个两两互素的整数 []{.arithmatex}$b_1,b_2,\dots,b_n$ 之积，证明 []{.arithmatex}$b_i|a$ 即可。

## 质数 {#_6}

- 定义：一个正整数无法被除了 []{.arithmatex}$1$ 和它自身之外的任何自然数整除，则成为质数，否则为合数。

- 数量：对于一个足够大的整数 []{.arithmatex}$N$，不超过 []{.arithmatex}$N$ 的质数有 []{.arithmatex}$\displaystyle\pi(x)\approx\frac{N}{\ln N}$ 个，所以第 []{.arithmatex}$n$ 个质数约为 []{.arithmatex}$n\ln n$.

- 判定：试除法，若 []{.arithmatex}$N$ 为合数，则存在一个能整除 []{.arithmatex}$N$ 的数 []{.arithmatex}$T$ 且 []{.arithmatex}$2 \leq T \leq \sqrt{N}$.

- 算数基本定理：[]{.arithmatex}$N = p_1^{c_1}p_2^{c_2}\dots p_n^{c_n}$，[]{.arithmatex}$N$ 的正约数个数 []{.arithmatex}$=\red{\boxed{\displaystyle\prod_{i=1}^{n}(c_i+1)}}$，[]{.arithmatex}$N$ 的所有正约数的和 []{.arithmatex}$=\displaystyle\prod_{i=1}^{n}(\displaystyle\sum_{j=0}^{c_i}(p_i)^j)=\red{\boxed{\prod_{i=1}^n\frac{p_i^{c_i+1}-1}{p_i-1}}}$.

一个正整数 []{.arithmatex}$N$ 的约数个数上界为 []{.arithmatex}$2\sqrt{N}$，[]{.arithmatex}$1$ \~ []{.arithmatex}$N$ 每个数的约数个数的总和大约为 []{.arithmatex}$N\log N$.

- 设 []{.arithmatex}$b|ac$，若 []{.arithmatex}$\gcd(b,c)=1$，则 []{.arithmatex}$b|a$.

- 设 []{.arithmatex}$a,b\in\N^*$ 且 []{.arithmatex}$a,b$ 之积是一个整数的 []{.arithmatex}$k(k\geq 2)$ 次幂，若 []{.arithmatex}$\gcd(a,b)=1$，则 []{.arithmatex}$a,b$ 都是整数的 []{.arithmatex}$k$ 次幂。一般地，设正整数 []{.arithmatex}$a,b,\dots,c$ 之积是一个整数的 []{.arithmatex}$k$ 次幂，且 []{.arithmatex}$a,b,\dots,c$ 两两互质，则 []{.arithmatex}$a,b,\dots,c$ 都是整数的 []{.arithmatex}$k$ 次幂。

- 对任意正整数 []{.arithmatex}$m$ 及质数 []{.arithmatex}$p$，记 []{.arithmatex}$p^c\Vert m$ 表示 []{.arithmatex}$p^c|m$ 但 []{.arithmatex}$p^{c+1}\nmid m$，即 []{.arithmatex}$p^c$ 是 []{.arithmatex}$m$ 的标准分解中出现的 []{.arithmatex}$p$ 的幂。

- 设 []{.arithmatex}$n>1,p$ 为质数，[]{.arithmatex}$p^{c_p}\Vert n!$，则 []{.arithmatex}$c_p=\displaystyle\sum_{l=1}^{+\infty}\lfloor\frac{n}{p^l}\rfloor$

例 1：证明无穷数列 []{.arithmatex}$10001,100010001,\dots$ 中无质数。

记 []{.arithmatex}$\displaystyle a_n=1+10^4+\dots+10^{4(n-1)}=\frac{10^{4n}-1}{10^4-1}$，接下来分 []{.arithmatex}$n$ 为奇偶讨论即可。

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{2k}=\frac{10\^{8k}-1}{10\^4-1}=\frac{10\^{8k}-1}{10\^8-1}\cdot\frac{10\^8-1}{10\^4-1}
:::

$$a_{2k}=\frac{10^{8k}-1}{10^4-1}=\frac{10^{8k}-1}{10^8-1}\cdot\frac{10^8-1}{10^4-1}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
a\_{2k+1}=\frac{10\^{4(2k+1)}-1}{10\^4-1}=\frac{10\^{2(2k+1)}-1}{10\^2-1}\cdot\frac{10\^{2(2k+1)}+1}{10\^2+1}
:::

$$a_{2k+1}=\frac{10^{4(2k+1)}-1}{10^4-1}=\frac{10^{2(2k+1)}-1}{10^2-1}\cdot\frac{10^{2(2k+1)}+1}{10^2+1}$$
::::

例 2：证明 []{.arithmatex}$\forall n\in\N^*,n>1,n^4+4^n$ 不是质数。

[]{.arithmatex}$n$ 为偶数显然。[]{.arithmatex}$n$ 为奇数时，设 []{.arithmatex}$n=2k+1$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned}n\^4+4\^n&=n\^4+4\cdot 4\^{2k}=n\^4+4\cdot (2k)\^4=n\^4+4n\^2\cdot(2\^k)\^2+4\cdot(2k)\^4-4n\^2\cdot(2\^k)\^2\\&=(n\^2+2\cdot 2\^{2k})\^2-(2n\cdot 2\^k)\^2=(n\^2+2\^{k+1}n+2\^{2k+1})(n\^2-2\^{k+1}n+2\^{2k+1})\end{aligned}
:::

$$\begin{aligned}n^4+4^n&=n^4+4\cdot 4^{2k}=n^4+4\cdot (2k)^4=n^4+4n^2\cdot(2^k)^2+4\cdot(2k)^4-4n^2\cdot(2^k)^2\\&=(n^2+2\cdot 2^{2k})^2-(2n\cdot 2^k)^2=(n^2+2^{k+1}n+2^{2k+1})(n^2-2^{k+1}n+2^{2k+1})\end{aligned}$$
::::

即把 []{.arithmatex}$4^n$ 看成 []{.arithmatex}$4y^4$，有 []{.arithmatex}$\red{\boxed{x^4+4y^4=(x^2+2y^2+2xy)(x^2+2y^2-2xy)}}$

练 1：设 []{.arithmatex}$a,b,c,d\in\N^*,ab=cd$，证明 []{.arithmatex}$a+b+c+d$ 不是质数。

例 3：证明：若 []{.arithmatex}$a,b\in\Z,2a^2+a=3b^2+b$，则 []{.arithmatex}$a-b$ 和 []{.arithmatex}$2a+2b+1$ 都为完全平方数。

已知化为 []{.arithmatex}$(a-b)(2a+2b+1)=b^2$，设 []{.arithmatex}$d=\gcd(a-b,2a+2b+1)$，若 []{.arithmatex}$d>1$，则 []{.arithmatex}$d$ 有质因子 []{.arithmatex}$p$，[]{.arithmatex}$p|b^2\implies p|b$，[]{.arithmatex}$p|(a-b)\implies p|a\implies p|1$，这不可能，因此 []{.arithmatex}$d=1$. 因为 []{.arithmatex}$b^2$ 是完全平方数，由此可得 []{.arithmatex}$|a-b|，|2a+2b+1|$ 也是完全平方。

只要证 []{.arithmatex}$a-b$ 和 []{.arithmatex}$2a+2b+1$ 不能同时 []{.arithmatex}$<0$ 即可。设 []{.arithmatex}$a-b<0$，则 []{.arithmatex}$b-a=r^2$. 显然 []{.arithmatex}$r|b,r|a$，令 []{.arithmatex}$b=b_1r,a=a_1r$，代入题目 []{.arithmatex}$a_1^2+6a_1r+3r^2+1=0$，得 []{.arithmatex}$a_1=-3r\pm\sqrt{6r^2-1}$，显然 []{.arithmatex}$6r^2-1$ 应为完全平方数，而 []{.arithmatex}$6r^2-1\equiv 2\ (\mathrm{mod}\ 3)$，矛盾，原命题得证。

## 不定方程 {#_7}

例 1：证明两个连续正整数之积不能是完全平方或完全立方。

反证法，即设 []{.arithmatex}$x(x+1)=y^2$ 有解，则 []{.arithmatex}$(2x+1)^2=4y^2+1$，分解为

:::: {.arithmatex}
::: {.MathJax_Preview}
(2x+1+2y)(2x+1-2y)=1\implies\begin{cases}2x+1+2y=1\\2x+1-2y=1\end{cases}\implies x=y=0
:::

$$(2x+1+2y)(2x+1-2y)=1\implies\begin{cases}2x+1+2y=1\\2x+1-2y=1\end{cases}\implies x=y=0$$
::::

显然不可能。类似的，对于完全立方，由于 []{.arithmatex}$x$ 和 []{.arithmatex}$x+1$ 互质，可得它们都是立方数。设 []{.arithmatex}$x=u^3,x+1=v^3,y=uv,v^3-u^3=1=(v-u)(v^2+uv+u^2)$，显然不可能。

类似的，可证明连续两个正整数之积不能是整数的 []{.arithmatex}$k(k\geq 2)$ 次幂。

练 1：设 []{.arithmatex}$k\in\N^*,k\geq 2$，证明：连续三个正整数之积不能是整数的 []{.arithmatex}$k$ 次幂。

提示：[]{.arithmatex}$x(x^2-1)=y^k\implies a^kb^k=(ab)^k,1=a^{2k}-b^k=(a^2)^k-b^k$，导出矛盾。

------------------------------------------------------------------------

例 2：证明方程 []{.arithmatex}$y^2+y=x+x^2+x^3$ 没有 []{.arithmatex}$x\neq 0$ 的整数解。

转化为 []{.arithmatex}$(y-x)(y+x+1)=x^3$，可以证明 []{.arithmatex}$\gcd(y-x,y+x+1)=1$，设 []{.arithmatex}$y-x=a^3,y+x+1=b^3,x=ab$，可得 []{.arithmatex}$b^3-a^3=(b-a)(b^2+ab+a^2)=2ab+1③$，证明该方程无解即可。[]{.arithmatex}$ab>0$ 时，[]{.arithmatex}$b-a\geq 1$，③的左边 []{.arithmatex}$\geq 3ab>$ 右边；[]{.arithmatex}$ab<0$ 时，③的左边的绝对值 []{.arithmatex}$\geq 2(a^2+b^2-|ab|)>2|ab|>$ ③的右边的绝对值。因此原命题成立。

练 2：求方程 []{.arithmatex}$(x^2-y^2)^2=1+16y$ 的所有整数解。

提示：[]{.arithmatex}$y\geq 0，|x|\geq$ 或 []{.arithmatex}$\leq y+1$，均可得出 []{.arithmatex}$(x^2-y^2)^2\geq(2y-1)^2$，得 []{.arithmatex}$(2y-1)^2\leq 1+16y$，答案 []{.arithmatex}$(x,y)=(\pm 1,0),(\pm 4,3)(\pm4,5)$.

------------------------------------------------------------------------

例 3：设 []{.arithmatex}$x,y,z\in\N^*,2x^x=y^y+z^z$，证明 []{.arithmatex}$x=y=z$.

:::: {.arithmatex}
::: {.MathJax_Preview}
(x+1)\^{x+1}\>x\^{x+1}+(x+1)x\^x\>2x\^x\implies y,z\leq x
:::

$$(x+1)^{x+1}>x^{x+1}+(x+1)x^x>2x^x\implies y,z\leq x$$
::::

反之，设 []{.arithmatex}$y\geq x+1$，则 []{.arithmatex}$y^y+z^z>(x+1)^{x+1}>2x^x$，矛盾。而 []{.arithmatex}$y^y+z^z\leq x^x+x^x=2x^x$，所以 []{.arithmatex}$x=y=z$.

## 欧拉函数 {#_8}

[]{.arithmatex}$1$ \~ []{.arithmatex}$N$ 中与 []{.arithmatex}$N$ 互质的数的个数被称为欧拉函数，记为 []{.arithmatex}$\varphi(N)$. 用数学符号表示即为 []{.arithmatex}$\varphi(N)=\displaystyle\sum_{i=1}^{N}[\gcd(i,N)=1]$.

若 []{.arithmatex}$N = p_1^{c_1}p_2^{c_2}\dots p_n^{c_n}$，则 []{.arithmatex}$\displaystyle\varphi(N)=N\times\frac{p_1-1}{p_1}\times\frac{p_2-1}{p_2}\times\dots\times\frac{p_n-1}{p_n}=N\cdot\displaystyle\prod_{质数p|N}\left(1-\frac{1}{p}\right)$

证明：设 []{.arithmatex}$p,q$ 为 []{.arithmatex}$N$ 的不同质因子，[]{.arithmatex}$1$ \~ []{.arithmatex}$N$ 中 []{.arithmatex}$p$ 的倍数有 []{.arithmatex}$\displaystyle \frac{N}{p}$ 个，[]{.arithmatex}$q$ 的倍数有 []{.arithmatex}$\displaystyle \frac{N}{q}$ 个。若把 []{.arithmatex}$\displaystyle \frac{N}{p}+\frac{N}{q}$ 个数去掉，则 []{.arithmatex}$\displaystyle\frac{N}{pq}$ 被计算了 []{.arithmatex}$2$ 次（容斥原理）。因此， []{.arithmatex}$1$ \~ []{.arithmatex}$N$ 中不与 []{.arithmatex}$N$ 含有相同质因子的 []{.arithmatex}$p$ 或 []{.arithmatex}$q$ 数量为 []{.arithmatex}$\displaystyle N-\frac{N}{p}-\frac{N}{q}+\frac{N}{pq}=N\left(1-\frac{1}{p}\right)\left(1-\frac{1}{q}\right)$，对 []{.arithmatex}$N$ 的全部质因子继续容斥即可得到公式。

| []{.arithmatex}$n$ | []{.arithmatex}$1$ | []{.arithmatex}$2$ | []{.arithmatex}$3$ | []{.arithmatex}$4$ | []{.arithmatex}$5$ | []{.arithmatex}$6$ | []{.arithmatex}$7$ | []{.arithmatex}$8$ | []{.arithmatex}$9$ | []{.arithmatex}$10$ | []{.arithmatex}$11$ | []{.arithmatex}$12$ | []{.arithmatex}$13$ | []{.arithmatex}$14$ | []{.arithmatex}$15$ |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| []{.arithmatex}$\varphi(n)$ | []{.arithmatex}$1$ | []{.arithmatex}$1$ | []{.arithmatex}$2$ | []{.arithmatex}$2$ | []{.arithmatex}$4$ | []{.arithmatex}$2$ | []{.arithmatex}$6$ | []{.arithmatex}$4$ | []{.arithmatex}$6$ | []{.arithmatex}$4$ | []{.arithmatex}$10$ | []{.arithmatex}$4$ | []{.arithmatex}$12$ | []{.arithmatex}$6$ | []{.arithmatex}$8$ |

欧拉函数的性质：

1.  []{.arithmatex}$\forall n>1$，[]{.arithmatex}$1$ \~ []{.arithmatex}$n$ 中与 []{.arithmatex}$n$ 互质的数的和为 []{.arithmatex}$\displaystyle\frac{n\times\varphi(n)}{2}$.
2.  若 []{.arithmatex}$a,b$ 互质，则 []{.arithmatex}$\varphi(ab)=\varphi(a)\varphi(b)$.
3.  设 []{.arithmatex}$p$ 为质数，[]{.arithmatex}$\varphi(p)=p-1$.
4.  设 []{.arithmatex}$p$ 为质数，[]{.arithmatex}$k\in\N^*,\varphi(p^k)=p^{k-1}\times(p-1)=p^k-p^{k-1}$.
5.  设 []{.arithmatex}$p$ 为质数，若 []{.arithmatex}$p\mid n$ 且 []{.arithmatex}$p^2\mid n$，则 []{.arithmatex}$\displaystyle\varphi(n)=\varphi\left(\frac{n}{p}\right)\times p$.
6.  设 []{.arithmatex}$p$ 为质数，若 []{.arithmatex}$p\mid n$ 但 []{.arithmatex}$p^2\nmid n$，则 []{.arithmatex}$\displaystyle\varphi(n)=\varphi\left(\frac{n}{p}\right)\times (p-1)$.
7.  若 []{.arithmatex}$n$ 为奇数，则 []{.arithmatex}$\varphi(2n)=\varphi(n)$.
8.  []{.arithmatex}$\forall n\geq 3,\ n\in\N^*,\ 2\mid\varphi(n)$.
9.  欧拉反演：[]{.arithmatex}$\displaystyle\sum_{d\mid n}\varphi(d)=n$.

证明：

1.  因为 []{.arithmatex}$\gcd(n,x)=\gcd(n,n-x)$，所以与 []{.arithmatex}$n$ 不互质的数 []{.arithmatex}$x,n-x$ 成对出现，平均值为 []{.arithmatex}$\displaystyle\frac{n}{2}$. []{.arithmatex}$\\$ 因此与 []{.arithmatex}$n$ 互质的数的平均值也是 []{.arithmatex}$\displaystyle\frac{n}{2}$，进而得到性质 1。
2.  根据欧拉函数的计算式可直接获得性质 2。
3.  根据欧拉函数的定义可直接获得性质 3。
4.  从 []{.arithmatex}$1$ \~ []{.arithmatex}$p^{k}$ 中的所有数，除了 []{.arithmatex}$p^{k-1}$ 个 []{.arithmatex}$p$ 的倍数外都与 []{.arithmatex}$p^k$ 互素。
5.  若 []{.arithmatex}$p\mid n$ 且 []{.arithmatex}$p^2\mid n$，则 []{.arithmatex}$\displaystyle n,\frac{n}{p}$ 包含相同的质因子，只是 []{.arithmatex}$p$ 的指数不同。[]{.arithmatex}$\\$ 按照欧拉函数的计算公式，[]{.arithmatex}$\displaystyle \frac{\varphi(n)}{\varphi(\frac{n}{p})}=\frac{n}{\frac{n}{p}}=p$，得到性质 5。
6.  若 []{.arithmatex}$p\mid n$ 且 []{.arithmatex}$p^2\mid n$，则 []{.arithmatex}$\displaystyle n,\frac{n}{p}$ 互质。因为 []{.arithmatex}$\displaystyle\varphi(n)=\varphi\left(\frac{n}{p}\right)\varphi(p)$，而 []{.arithmatex}$\varphi(p)=p-1$，得到性质 6。
7.  []{.arithmatex}$\forall m<2n,m\in\N^*$，若 []{.arithmatex}$2\mid m$，则 []{.arithmatex}$\gcd(m,2n)\neq 1$，也就是对欧拉函数的值没有贡献；[]{.arithmatex}$\\$ 若 []{.arithmatex}$2\nmid m$，则 []{.arithmatex}$\gcd(m,2n)=1$，欧拉函数的值也就与 []{.arithmatex}$2n$ 中的偶质因子无关。
8.  []{.arithmatex}$n\geq 3$ 时，与 []{.arithmatex}$n$ 互质的数不可能为 []{.arithmatex}$\displaystyle\frac{n}{2}\implies\forall x<n,\gcd(x,n)=\gcd(n-x,n)$，也就是存在一一对应关系。
9.  设 []{.arithmatex}$f(n)=\displaystyle\sum_{d\mid n}\varphi(d)$，利用 []{.arithmatex}$\varphi$ 是积性函数，得到：[]{.arithmatex}$\\$ 若 []{.arithmatex}$n,m$ 互质，则 []{.arithmatex}$f(nm)=\displaystyle\sum_{d\mid nm}\varphi(d)=\displaystyle\sum_{d\mid n}\varphi(d)\cdot\displaystyle\sum_{d\mid m}\varphi(d)=f(n)f(m)$，即 []{.arithmatex}$f(n)$ 是积性函数。[]{.arithmatex}$\\$ 对于单个质因子有：[]{.arithmatex}$\begin{aligned}f(p^m)&=\displaystyle\sum_{d\mid p^m}\varphi(d)=\displaystyle\sum_{i=0}^{m}\varphi(p^i)=\varphi(1)+\varphi(p)+\varphi(p^2)+\varphi(p^3)+\dots+\varphi(p^m)\\&= 1+(p-1)+(p-1)p+(p-1)p^2+\dots+(p-1)p^{m-1}\\&=1+(p-1)+(p^2-p)+(p^3-p^2)+\dots+(p^m-p^{m-1})=p^m\end{aligned} \\$ 所以 []{.arithmatex}$f(n)=\displaystyle\prod_{i=1}^{m}f(p_i^{c_i})=\displaystyle\prod_{i=1}^{m}p_i^{c_i}=n$

### 积性函数与完全积性函数 {#_9}

若函数 []{.arithmatex}$f(x)$ 满足 []{.arithmatex}$f(1)=1$ 且 []{.arithmatex}$\forall x,y\in\N^{*},\gcd(x,y)=1$ 都有 []{.arithmatex}$f(xy)=f(x)f(y)$，则 []{.arithmatex}$f(x)$ 是积性函数。

若函数 []{.arithmatex}$f(x)$ 满足 []{.arithmatex}$f(1)=1$ 且 []{.arithmatex}$\forall x,y\in\N^{*}$ 都有 []{.arithmatex}$f(xy)=f(x)f(y)$，则 []{.arithmatex}$f(x)$ 是完全积性函数。

性质：

1.  若 []{.arithmatex}$f(x)$ 和 []{.arithmatex}$g(x)$ 均为积性函数，则以下函数也为积性函数： \$[]{.arithmatex}$\begin{aligned}h(x)&=f(x^p) \\ h(x)&=f^p(x) \\ h(x)&=f(x)g(x) \\ h(x)&=\displaystyle\sum_{d\mid x}f(d)g\left(\frac{x}{d}\right)\end{aligned}$\$
2.  设 []{.arithmatex}$x=\displaystyle\prod p_i^{c_i}$，

若 []{.arithmatex}$f(x)$ 为积性函数，则 []{.arithmatex}$f(x)=\displaystyle\prod f(p_i^{c_i})$。

若 []{.arithmatex}$f(x)$ 为完全积性函数，则 []{.arithmatex}$f(x)=\displaystyle\prod f^{c_i}(p_i)$。

例子：

积性函数：[]{.arithmatex}$\varphi(n),\sigma _k(n)=\displaystyle\sum_{d\mid n}d^k,\sigma _0(n)$ 通常简记为 []{.arithmatex}$d(n)$ 或 []{.arithmatex}$\tau(n)$，[]{.arithmatex}$\sigma _1(n)$ 通常简记为 []{.arithmatex}$\sigma(n)$。

完全积性函数：[]{.arithmatex}$\varepsilon(n)=[n=1],\text{id}_k(n)=n^k,\text{id}_1(n)$ 通常简记为 []{.arithmatex}$\text{id}(n),f(n)=1$.

## 同余 {#_10}

- 平方数 []{.arithmatex}$\mathrm{mod}\ 4\equiv 0$ 或 []{.arithmatex}$1,\mathrm{mod}\ 8\equiv0$ 或 []{.arithmatex}$1$ 或 []{.arithmatex}$4,\mathrm{mod}\ 3\equiv 0$ 或 []{.arithmatex}$1,\mathrm{mod}\ 5\equiv0$ 或 []{.arithmatex}$\pm 1$.
- 立方数 []{.arithmatex}$\mathrm{mod}\ 9\equiv 0$ 或 []{.arithmatex}$\pm 1$.
- 四次幂 []{.arithmatex}$\mathrm{mod}\ 16\equiv 0$ 或 []{.arithmatex}$1$.

例如可证明 []{.arithmatex}$a,b,c,d\in\N^*,a^{4b+d}-a^{4c+d}$ 能被 []{.arithmatex}$240=2^4\times 3\times 5$ 整除。

例 1：设 []{.arithmatex}$a,b,c\in\Z,a+b+c=0,d=a^{1999}+b^{1999}+c^{1999}$，证明 []{.arithmatex}$d$ 可被 []{.arithmatex}$6$ 整除。

:::: {.arithmatex}
::: {.MathJax_Preview}
u\^{1999}\equiv u(\mathrm{mod}\\ 2)\implies d\equiv a+b+c\equiv 0(\mathrm{mod}\\ 2)\implies2\|d
:::

$$u^{1999}\equiv u(\mathrm{mod}\ 2)\implies d\equiv a+b+c\equiv 0(\mathrm{mod}\ 2)\implies2|d$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
u\^3\equiv u(\mathrm{mod}\\ 3)\implies u\^{1999}\equiv u\cdot u\^{1998}\equiv u\cdot u\^{666}\equiv u\cdot u\^{222}\equiv u\^{75}\equiv u\^{25}\equiv u\^9\equiv u(\mathrm{mod}\\ 3)
:::

$$u^3\equiv u(\mathrm{mod}\ 3)\implies u^{1999}\equiv u\cdot u^{1998}\equiv u\cdot u^{666}\equiv u\cdot u^{222}\equiv u^{75}\equiv u^{25}\equiv u^9\equiv u(\mathrm{mod}\ 3)$$
::::

注意 []{.arithmatex}$u^3\equiv u(\mathrm{mod}\ 3)$ 是费马小定理的特殊情形。

练 1：设 []{.arithmatex}$x,y,z\in\Z,(x-y)(y-z)(z-x)=x+y+z$，证明 []{.arithmatex}$27|(x+y+z)$.

只要证明 []{.arithmatex}$x,y,z$ 两两模 []{.arithmatex}$3$ 同余即可。

练 2：证明 []{.arithmatex}$11,111,1111,\dots$ 不是完全平方数。只要知道 []{.arithmatex}$11\ \mathrm{mod}\ 4\neq 0$ 即可。

------------------------------------------------------------------------

例 2：数列 []{.arithmatex}$\set{x_n}$ 为 []{.arithmatex}$1,3,5,11,\dots$，满足 []{.arithmatex}$x_{n+1}=x_n+2x_{n-1}$.

数列 []{.arithmatex}$\set{y_n}$ 为 []{.arithmatex}$7,17,55,161,\dots$，满足 []{.arithmatex}$y_{n+1}=2y_n+3y_{n-1}$. 证明：两个数列无相同项。

考虑以 []{.arithmatex}$8$ 为模，因为 []{.arithmatex}$x_2\equiv 3,x_3\equiv 5$. 若 []{.arithmatex}$x_{n-1}\equiv 3,x_n\equiv 5$，则 []{.arithmatex}$x_{n+1}\equiv 3,x_{n+2}\equiv 5$.

显然 []{.arithmatex}$\set{x_n}$ 是模 []{.arithmatex}$8$ 后的周期数列，同理 []{.arithmatex}$\set{y_n}$ 也是（ []{.arithmatex}$7,1,7,1,\dots$ ），于是命题得证。

### 费马小定理与欧拉定理 {#_11}

若整数 []{.arithmatex}$a$ 和整数 []{.arithmatex}$b$ 除以正整数 []{.arithmatex}$m$ 的余数相等，则称 []{.arithmatex}$a,b$ 模 []{.arithmatex}$m$ 同余，记为 []{.arithmatex}$a\equiv b\ (\mathrm{mod}\  m)$.

并且注意到 []{.arithmatex}$\displaystyle k\ \mathrm{mod}\ i=k-\left\lfloor\frac{k}{i}\right\rfloor\cdot i$，且同余满足同加性、同乘性、同幂性，但不满足同除性。

对于 []{.arithmatex}$\forall a \in [0, m - 1]$，集合 []{.arithmatex}$\set{a+km\ (k\in\Z)}$ 的所有数模 []{.arithmatex}$m$ 同余，余数都是 []{.arithmatex}$a$. 该集合称为一个模 []{.arithmatex}$m$ 的同余类，简记为 []{.arithmatex}$\overline{a}$.

模 []{.arithmatex}$m$ 的同余类一共有 []{.arithmatex}$m$ 个，分别为 []{.arithmatex}$\overline{0},\overline{1},\overline{2},\dots,\overline{m-1}$. 它们构成 []{.arithmatex}$m$ 的完全剩余系。

[]{.arithmatex}$1$ \~ []{.arithmatex}$m$ 中与 []{.arithmatex}$m$ 互质的数代表的同余类共有 []{.arithmatex}$\varphi(m)$ 个，它们构成 []{.arithmatex}$m$ 的简化剩余系。[]{.arithmatex}$\\$ 例如，模 []{.arithmatex}$10$ 的简化剩余系为 []{.arithmatex}$\set{\overline{1},\overline{3},\overline{7},\overline{9}}$。

若从某个非空数集中任选两个元素（同一元素可重复选出），选出的这两个元素通过某种（或几种）运算后的得数仍是该数集中的元素，那么，就说该集合对于这种（或几种）运算是封闭的。[]{.arithmatex}$\\$ 例如若一个集合中的元素，如果能够做到做加法运算的结果还在这个集合中，就说这个集合对加法运算封闭。[]{.arithmatex}$\\$ 例如 []{.arithmatex}$\N$ 对加法、乘法运算是封闭的；[]{.arithmatex}$\Z$ 对加、减、乘法运算是封闭的；[]{.arithmatex}$\mathbb{Q}, \mathbb{C}$ 对四则运算是封闭的。

简化剩余系关于模 []{.arithmatex}$m$ 乘法封闭。这是因为若 []{.arithmatex}$a,b\ (1\leq a,b\leq m)$ 与 []{.arithmatex}$m$ 互质，则 []{.arithmatex}$ab$ 也与 []{.arithmatex}$m$ 互质。[]{.arithmatex}$\\$ 由余数的定义得 []{.arithmatex}$ab\ \mathrm{mod}\ m$ 也与 []{.arithmatex}$m$ 互质，即 []{.arithmatex}$ab\ \mathrm{mod}\ m$ 也属于 []{.arithmatex}$m$ 的简化剩余系。

- 费马小定理：若 []{.arithmatex}$p$ 是质数，则对于任意整数 []{.arithmatex}$a$，有 []{.arithmatex}$a^p\equiv a\ (\mathrm{mod}\ p)$.
- 欧拉定理：若正整数 []{.arithmatex}$a,n$ 互质，则 []{.arithmatex}$a^{\varphi(n)}\equiv 1\ (\mathrm{mod}\ n)$.

证明：设 []{.arithmatex}$n$ 的简化剩余系为 []{.arithmatex}$\set{\overline{a_1},\overline{a_2},\dots,\overline{a_{\varphi(n)}}}$. []{.arithmatex}$\forall a_i,a_j$，若 []{.arithmatex}$a\cdot a_i\equiv a\cdot a_j\ (\mathrm{mod}\ n)$，则 []{.arithmatex}$a\cdot(a_i-a_j)\equiv 0.$ 因为 []{.arithmatex}$a,n$ 互质，所以 []{.arithmatex}$a_i\equiv a_j$. 故当 []{.arithmatex}$a_i\neq a_j$ 时，[]{.arithmatex}$aa_i,aa_j$ 也代表不同的同余类。

又因为简化剩余系关于模 []{.arithmatex}$m$ 乘法封闭，故 []{.arithmatex}$\overline{aa_1}$ 也在简化剩余系集合中。因此，集合 []{.arithmatex}$\set{\overline{a_1},\overline{a_2},\dots,\overline{a_{\varphi(n)}}}$ 与集合 []{.arithmatex}$\set{\overline{aa_1},\overline{aa_2},\dots,\overline{aa_{\varphi(n)}}}$ 都能表示 []{.arithmatex}$n$ 的简化剩余系。综上所述：

:::: {.arithmatex}
::: {.MathJax_Preview}
a\^{\varphi(n)}a_1a_2\dots a\_{\varphi(n)}\equiv(aa_1)(aa_2)\dots(aa\_{\varphi(n)})\equiv a_1a_2\dots a\_{\varphi(n)}\\ (\mathrm{mod}\\ n)
:::

$$a^{\varphi(n)}a_1a_2\dots a_{\varphi(n)}\equiv(aa_1)(aa_2)\dots(aa_{\varphi(n)})\equiv a_1a_2\dots a_{\varphi(n)}\ (\mathrm{mod}\ n)$$
::::

因此 []{.arithmatex}$a^{\varphi(n)}\equiv 1\ (\mathrm{mod}\ n)$。当 []{.arithmatex}$p$ 为质数时，满足 []{.arithmatex}$\varphi(p)=p-1$，两边同乘 []{.arithmatex}$a$ 即可得到费马小定理。

另外，当 []{.arithmatex}$a$ 是 []{.arithmatex}$p$ 的倍数，费马小定理显然成立。

------------------------------------------------------------------------

- 欧拉定理的推论：若正整数 []{.arithmatex}$a,n$ 互质，则对于任意正整数 []{.arithmatex}$b$，有 []{.arithmatex}$a^b\equiv a^{b\ \mathrm{mod}\ \varphi(n)}\ (\mathrm{mod}\ n)$

证明：设 []{.arithmatex}$b=q\cdot \varphi(n)+r$，其中 []{.arithmatex}$0\leq r<\varphi(n)$，即 []{.arithmatex}$r=b\ \mathrm{mod}\ \varphi(n)$. 于是有：

:::: {.arithmatex}
::: {.MathJax_Preview}
a\^b\equiv a\^{q\cdot\varphi(n)+r}\equiv (a\^{\varphi(n)})\^q\cdot a\^r\equiv 1\^q\cdot a\^r\equiv a\^r\equiv a\^{b\\ \mathrm{mod}\\ \varphi(n)}\\ (\mathrm{mod}\\ n)
:::

$$a^b\equiv a^{q\cdot\varphi(n)+r}\equiv (a^{\varphi(n)})^q\cdot a^r\equiv 1^q\cdot a^r\equiv a^r\equiv a^{b\ \mathrm{mod}\ \varphi(n)}\ (\mathrm{mod}\ n)$$
::::

证毕。面对 []{.arithmatex}$a+b,a-b,a\cdot b$ 这样的算式，可以在计算前先把 []{.arithmatex}$a,b$ 对 []{.arithmatex}$p$ 取模。面对 []{.arithmatex}$a^b$ 这样的乘方算式，可以先把底数对 []{.arithmatex}$p$ 取模、指数对 []{.arithmatex}$\varphi(p)$ 取模，再计算乘方。

即 []{.arithmatex}$a^b\equiv (a\ \mathrm{mod}\ p)^{b\ \mathrm{mod}\ \varphi(p)}\ (\mathrm{mod}\ p)$

------------------------------------------------------------------------

- 扩展欧拉定理

\$[]{.arithmatex}$a^b\equiv\begin{cases}a^{b\ \mathrm{mod}\ \varphi(m)}&\text{if }\gcd(a,m)=1\\ a^b&\text{if }\gcd(a,m)\neq 1,b<\varphi(m)\\ a^{b\ \mathrm{mod}\ \varphi(m)+\varphi(m)}&\text{if }\gcd(a,m)\neq 1,b\geq\varphi(m)\end{cases}\ (\mathrm{mod}\ m)$\$

证明十分显然，略。

------------------------------------------------------------------------

- 若正整数 []{.arithmatex}$a,n$ 互质，则满足 []{.arithmatex}$a^x\equiv 1\ (\mathrm{mod}\ n)$ 的最小正整数 []{.arithmatex}$x_0$ 是 []{.arithmatex}$\varphi(n)$ 的约数。

反证法，假设满足 []{.arithmatex}$a^x\equiv 1\ (\mathrm{mod}\ n)$ 的最小正整数 []{.arithmatex}$x_0$ 不能整除 []{.arithmatex}$\varphi(n)$.

设 []{.arithmatex}$\varphi(n)=qx_0+r\ (0<r<x_0)$，因为 []{.arithmatex}$a^{x_0}\equiv 1\ (\mathrm{mod}\ n)$，所以 []{.arithmatex}$a^{qx_0}\equiv 1\ (\mathrm{mod}\ n)$. 根据欧拉定理 []{.arithmatex}$a^{\varphi(n)}\equiv 1\ (\mathrm{mod}\ n)$，所以 []{.arithmatex}$a^r\equiv 1\ (\mathrm{mod}\  n)$. 这与 []{.arithmatex}$x_0$ 最小矛盾。故假设不成立，原命题成立。

### 中国剩余定理 {#_12}

设 []{.arithmatex}$m_1,m_2,\dots,m_n$ 是两两互质的整数，[]{.arithmatex}$m=\displaystyle\prod_{i=1}^n m_i,M_i=\frac{m}{m_i},t_i$ 是线性同余方程 []{.arithmatex}$M_it_i\equiv 1\ (\mathrm{mod}\ m_i)$ 的一个解。对于任意的 []{.arithmatex}$n$ 个整数，方程组

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases}x\equiv a_1\\ (\mathrm{mod}\\ m_1) \\ x\equiv a_2\\ (\mathrm{mod}\\ m_2)\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \vdots\\ x\equiv a_n\\ (\mathrm{mod}\\ m_n)\end{cases}
:::

$$\begin{cases}x\equiv a_1\ (\mathrm{mod}\ m_1) \\ x\equiv a_2\ (\mathrm{mod}\ m_2)\\ \ \ \ \ \ \ \ \ \ \ \ \ \vdots\\ x\equiv a_n\ (\mathrm{mod}\ m_n)\end{cases}$$
::::

有整数解，解为 []{.arithmatex}$x=\displaystyle\sum_{i=1}^{n}a_iM_it_i$，通解可以表示为 []{.arithmatex}$x+km(k\in\Z)$，最小非负整数解为 []{.arithmatex}$x\ \mathrm{mod}\ m$.

证明：因为 []{.arithmatex}$\displaystyle M_i=\frac{m}{m_i}$ 是除了 []{.arithmatex}$m_i$ 之外所有模数的倍数，所以 []{.arithmatex}$\forall k\neq i,a_iM_it_i\equiv 0\ (\mathrm{mod}\ m_i)$，[]{.arithmatex}$\\ \ \  \ \ \ \ \  \ \ \ \text{}$ 所以代入 []{.arithmatex}$x=\displaystyle\sum_{i=1}^{n}a_iM_it_i$，原方程组成立。

### 威尔逊定理 {#_13}

- []{.arithmatex}$p$ 为素数 []{.arithmatex}$\xLeftrightarrow{}(p-1)!\equiv -1\ (\mathrm{mod}\ p)$

证明：

1.  充分性

对于 []{.arithmatex}$p$ 不是素数的情况，有 []{.arithmatex}$\begin{cases}
   p=1 & (1-1)!\equiv 0\ (\mathrm{mod}\ 1) \\
   p=4 & (4-1)!\equiv 2\ (\mathrm{mod}\ 4) \\
   p>4 & 分类讨论得出\ (p-1)!\equiv 0\ (\mathrm{mod}\ p)
   \end{cases}$

\(a\) 当 []{.arithmatex}$p$ 为完全平方数。

    则 $p=k^2$ 且 $k>2$，用相减法比较 $2k$ 与 $p$ 的大小得 $2k<p$，于是有

    $$\begin{aligned}(p-1)!&=1\times 2\times\dots\times k\times\dots\times 2k\times\dots\times (p-1)\\ &=2nk^2\\&=2np\end{aligned}$$

    所以 $(p-1)!\equiv 0\ (\mathrm{mod}\ p)$ 且 $p$ 为完全平方数。

    (b) 当 $p$ 不为完全平方数。

    则 $p$ 可以表示为两个不相等的数 $a$ 和 $b$ 的乘积，设 $a<b$，则有 $p=ab,1<a<b<p$

    $$\begin{aligned}(p-1)!&=1\times 2\times\dots\times a\times\dots\times b\times\dots\times (p-1)\\&=a\times b\times n\\ &=np\end{aligned}$$

    所以 $(p-1)!\equiv 0\ (\mathrm{mod}\ p)$ 且 $p$ 不为完全平方数。

1.  必要性

当 []{.arithmatex}$p$ 为素数时，考虑二次剩余式 []{.arithmatex}$x^2\equiv 1\ (\mathrm{mod}\ p)$，化简得 []{.arithmatex}$(x-1)(x+1)\equiv 0\ (\mathrm{mod}\ p)$

于是 []{.arithmatex}$x\equiv 1\ (\mathrm{mod}\ p)$ 或 []{.arithmatex}$x\equiv p-1\ (\mathrm{mod}\ p)$。现在先抛开 []{.arithmatex}$1$ 和 []{.arithmatex}$p-1$ 不管，

[]{.arithmatex}$\forall a\in [2,p-2]$，必然存在一个和它不相等的逆元 []{.arithmatex}$a^{-1}\in[2,p-2]$，满足 []{.arithmatex}$aa^{-1}\equiv 1\ (\mathrm{mod}\ p)$

所以必然有 []{.arithmatex}$\displaystyle\frac{p-3}{2}$ 对数相乘的乘积为 []{.arithmatex}$1$，即 []{.arithmatex}$(p-2)!\equiv 1\ (\mathrm{mod}\ p)$

等式两边同时乘 []{.arithmatex}$p-1$ 就得到威尔逊定理。

例题：[]{.arithmatex}$n\in\N^*$ 且 []{.arithmatex}$n\leq 10^6$，求 []{.arithmatex}$S_n$.

:::: {.arithmatex}
::: {.MathJax_Preview}
S_n=\displaystyle\sum\_{k=1}\^{n}\left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor
:::

$$S_n=\displaystyle\sum_{k=1}^{n}\left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor$$
::::

令 []{.arithmatex}$d=3k+7$，原式化简为

:::: {.arithmatex}
::: {.MathJax_Preview}
S_n=\displaystyle\sum\_{k=1}\^{n}\left\lfloor\frac{(d-1)!+1}{d}-\left\lfloor\frac{(d-1)!}{d}\right\rfloor\right\rfloor
:::

$$S_n=\displaystyle\sum_{k=1}^{n}\left\lfloor\frac{(d-1)!+1}{d}-\left\lfloor\frac{(d-1)!}{d}\right\rfloor\right\rfloor$$
::::

由威尔逊定理，当 []{.arithmatex}$d$ 为素数时，[]{.arithmatex}$\displaystyle\frac{(d-1)!+1}{d}$ 必然是整数，而 []{.arithmatex}$\displaystyle\left\lfloor\frac{(d-1)!}{d}\right\rfloor$ 必然比 []{.arithmatex}$\displaystyle\frac{(d-1)!+1}{d}$ 小 []{.arithmatex}$1$，于是有：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases}p\\ 为素数 & \displaystyle\left\lfloor\frac{(d-1)!+1}{d}-\left\lfloor\frac{(d-1)!}{d}\right\rfloor\right\rfloor=1 \\ p\\ 为合数 & \displaystyle\left\lfloor\frac{(d-1)!+1}{d}-\left\lfloor\frac{(d-1)!}{d}\right\rfloor\right\rfloor=0\end{cases}
:::

$$\begin{cases}p\ 为素数 & \displaystyle\left\lfloor\frac{(d-1)!+1}{d}-\left\lfloor\frac{(d-1)!}{d}\right\rfloor\right\rfloor=1 \\ p\ 为合数 & \displaystyle\left\lfloor\frac{(d-1)!+1}{d}-\left\lfloor\frac{(d-1)!}{d}\right\rfloor\right\rfloor=0\end{cases}$$
::::

所以只需统计 []{.arithmatex}$[1,3\times 10^6+7]$ 中的素数即可得出答案。

## 拉格朗日定理 {#_14}

若 []{.arithmatex}$p$ 是质数，则对于模 []{.arithmatex}$p$ 意义下的 []{.arithmatex}$n$ 次整系数多项式 []{.arithmatex}$f(x)=a_nx^n+a_{n-1}x^{n-1}+\dots+a_0(p\nmid a_n)$ 同余方程 []{.arithmatex}$f(x)\equiv 0(\mathrm{mod}\ p)$ 至多有 []{.arithmatex}$n$ 个不同的解。
