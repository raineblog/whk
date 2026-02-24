# 数论入门 {#_1}

## 因数 {#_2}

### 整除 {#_3}

若 [\$b\$]{.arithmatex} 能整除 [\$a\$]{.arithmatex}，则记为 [\$a\mid b\$]{.arithmatex}，如 [\$2\mid 12\$]{.arithmatex}. 若 [\$b\$]{.arithmatex} 不能整除 [\$a\$]{.arithmatex}，则记为 [\$a\nmid b\$]{.arithmatex}，如 [\$5\nmid 12\$]{.arithmatex}.

若 [\$a\nmid b\$]{.arithmatex}，则 [\$b\div a\$]{.arithmatex} 存在余数 [\$r\$]{.arithmatex} 且 [\$0\<r\<a\$]{.arithmatex}，记 [\$r=a\\ \mathrm{mod}\\ b\$]{.arithmatex}. 例如，[\$3\\ \mathrm{mod}\\ 2=1\$]{.arithmatex}.

整除具有以下性质：

1.  若 [\$a\mid b\$]{.arithmatex} 且 [\$a\mid c\$]{.arithmatex}，则 [\$\forall x,y\$]{.arithmatex}，有 [\$a\mid xb+yc\$]{.arithmatex}.
2.  若 [\$a\mid b\$]{.arithmatex} 且 [\$b\mid c\$]{.arithmatex}，则 [\$a\mid c\$]{.arithmatex}.
3.  若 [\$a\mid b\$]{.arithmatex} 且 [\$b\mid a\$]{.arithmatex}，则 [\$a=\pm b\$]{.arithmatex}.
4.  设 [\$m\neq 0\$]{.arithmatex}，则 [\$a\mid b\$]{.arithmatex}，当且仅当 [\$ma\mid mb\$]{.arithmatex}.

### 最大公因数与最小公倍数 {#_4}

设 [\$a,b\$]{.arithmatex} 是两个不为 [\$0\$]{.arithmatex} 的整数，能使 [\$d\mid a\$]{.arithmatex} 和 [\$d\mid b\$]{.arithmatex} 成立的最大整数 [\$d\$]{.arithmatex}，称为 [\$a,b\$]{.arithmatex} 的最大公因数，记作 [\$\gcd(a,b)\$]{.arithmatex}.

设 [\$a,b\$]{.arithmatex} 是两个不为 [\$0\$]{.arithmatex} 的整数，能使 [\$a\mid d\$]{.arithmatex} 和 [\$b\mid d\$]{.arithmatex} 成立的最小整数 [\$d\$]{.arithmatex}，称为 [\$a,b\$]{.arithmatex} 的最小公倍数，记作 [\$\mathrm{lcm}(a,b)\$]{.arithmatex}.

- [\$\forall a,b\in\N,\\ \gcd(a,b)\cdot\mathrm{lcm}(a,b)=ab\$]{.arithmatex}

证明：设 [\$\displaystyle d=\gcd(a,b),a_0=\frac{a}{d},b_0=\frac{b}{d}\$]{.arithmatex}. 根据最大公因数的定义，有 [\$\gcd(a_0,b_0)=1\$]{.arithmatex}。[\$\\\\ \\ \\ \\ \\ \\ \\ \\ \\ \text{}\$]{.arithmatex} 再根据最小公倍数的定义，有 [\$\mathrm{lcm}(a,b)=a_0\cdot b_0\$]{.arithmatex}. [\$\\\\ \\ \\ \\ \\ \\ \\ \\ \\ \text{}\$]{.arithmatex} 于是 [\$\displaystyle\mathrm{lcm}(a,b)=\mathrm{lcm}(a_0\cdot d,b_0\cdot d)=\mathrm{lcm}(a_0,b_0)\cdot d=a_0\cdot b_0\cdot d=\frac{a\cdot b}{d}\$]{.arithmatex}，原命题得证。

- 九章算术 更相减损术： [\$\gcd(a,b)=\gcd(b,a-b)=\gcd(a,a-b),\gcd(2a,2b)=2\gcd(a,b)\$]{.arithmatex}.

证明：[\$d\mid a,d\mid b\implies d\mid(a-b)\$]{.arithmatex}.

- 欧几里得算法：[\$\forall a,b\in\N,b\neq 0,\gcd(a,b)=\gcd(b,a\\ \mathrm{mod}\\ b)\$]{.arithmatex}.

证明：分类讨论。

1.  若 [\$a\<b\$]{.arithmatex}，则有 [\$\gcd(b,a\\ \mathrm{mod}\\ b)=\gcd(b,a)=\gcd(a,b)\$]{.arithmatex}.
2.  若 [\$a\geq b\$]{.arithmatex}，不妨设 [\$a=q\cdot b+r\\ (0\leq r\<b)\$]{.arithmatex}。显然 [\$r=a\\ \mathrm{mod}\\ b\$]{.arithmatex}. 对于 [\$a,b\$]{.arithmatex} 的任意公因数 [\$d\$]{.arithmatex}，[\$\\\$]{.arithmatex} 因为 [\$d\mid a,d\mid q\cdot b\$]{.arithmatex}，故 [\$d\mid (a-q\cdot b)\$]{.arithmatex}，即 [\$d\mid r\$]{.arithmatex}. 因此 [\$d\$]{.arithmatex} 也是 [\$b,r\$]{.arithmatex} 的公因数，反之亦成立。[\$\\\$]{.arithmatex} 故 [\$a,b\$]{.arithmatex} 的公因数集合与 [\$b,a\\ \mathrm{mod}\\ b\$]{.arithmatex} 的公因数集合相同。于是它们的最大公因数也相等。

## 裴蜀定理 {#_5}

设 [\$a,b\in\Z,ab\neq 0\$]{.arithmatex}，则 [\$\exist x,y\in\Z\$]{.arithmatex} 使 [\$ax+by=\gcd(a,b)=a(x+bu)+b(y-au)\$]{.arithmatex}

由上易推出两个**整数 [\$a,b\$]{.arithmatex} 互素的充分必要条件是 [\$\exist x,y\in\Z\$]{.arithmatex} 使得 [\$ax+by=1\$]{.arithmatex}。**

比如要证明 [\$21n+4\$]{.arithmatex} 与 [\$14n+3\$]{.arithmatex} 互素，知道 [\$3(14n+3)-2(21n+4)=1\$]{.arithmatex} 即可。

例 1：证明 [\$n!+1\$]{.arithmatex} 与 [\$(n+1)!+1\$]{.arithmatex} 互素。

有 [\$(n+1)(n!+1)-\[(n+1)!+1\]=n\$]{.arithmatex}，于是 [\$\[d=\gcd(n!+1,(n+1)!+1)\]\|n\$]{.arithmatex}，又因为 [\$d\|n!\$]{.arithmatex}，结合 [\$d\|(n!+1)\$]{.arithmatex} 得到 [\$d=1\$]{.arithmatex}，原命题得证。

------------------------------------------------------------------------

例 2：记费马数 [\$F_k=2\^{2\^k}+1,k\geq 0\$]{.arithmatex}，证明若 [\$m\neq n\$]{.arithmatex} 则 [\$\gcd(F_m,F_n)=1\$]{.arithmatex}.

设 [\$m\>n\$]{.arithmatex}，只要利用 [\$F_n\|(F_m-2)\$]{.arithmatex} 证明 [\$\exist x\in\Z\$]{.arithmatex} 使得 [\$F_m+xF_n=2\$]{.arithmatex}【基本技巧例 2】

设 [\$\[d=\gcd(F_m,F_n)\]\|2\$]{.arithmatex}. [\$F_n\$]{.arithmatex} 显然为奇数故 [\$d=1\$]{.arithmatex}. 因此**费马数两两互素。**

------------------------------------------------------------------------

例 3：设 [\$a\>1,m,n\>0\$]{.arithmatex}，证明 [\$\boxed{\gcd(a\^m-1,a\^n-1)=a\^{\gcd(m,n)}-1}\$]{.arithmatex}

令 [\$D=\gcd(a\^m-1,a\^n-1)\$]{.arithmatex}，只要证明 [\$\[a\^{\gcd(m,n)}-1\]\|D\$]{.arithmatex} 及 [\$D\|\[a\^{\gcd(m,n)}-1\]\$]{.arithmatex} 即可。

显然 [\$\[a\^{\gcd(m,n)}-1\]\|(a\^m-1)\$]{.arithmatex} 和 [\$\[a\^{\gcd(m,n)}-1\]\|(a\^n-1)\$]{.arithmatex}，可以证明 [\$\[a\^{\gcd(m,n)}-1\]\|D\$]{.arithmatex}.

设 [\$d=\gcd(m,n)\$]{.arithmatex}，可选 [\$u,v\>0\$]{.arithmatex}，使 [\$mu-nv=d\$]{.arithmatex}. 因此 [\$D\|(a\^m-1),D\|(a\^{mu}-1)\$]{.arithmatex}，扩展开来 [\$D\|(a\^{mu}-a\^{nv})=a\^{nv}(a\^d-1)\$]{.arithmatex}，故 [\$D\|(a\^d-1)\$]{.arithmatex}. 综合上述原命题得证。

------------------------------------------------------------------------

例 4：设 [\$m,n\>0,mn\|(m\^2+n\^2)\$]{.arithmatex}，证明 [\$m=n\$]{.arithmatex}.

设 [\$\gcd(m,n)=d,m=m_1d,n=n_1d,\gcd(m_1,n_1)=1\$]{.arithmatex}①. 已知化为 [\$m_1n_1\|(m_1\^2+n_1\^2)\$]{.arithmatex}，从而 [\$m_1\|n_1\^2,n_1\|m_1\^2\$]{.arithmatex}. 结合①可得 [\$m_1=n_1=1,m=n\$]{.arithmatex}.

------------------------------------------------------------------------

例 5：设 [\$k\$]{.arithmatex} 为正奇数，证明 [\$\displaystyle\sum\_{i=1}\^ni\$]{.arithmatex} 整除 [\$\displaystyle\sum\_{i=1}\^ni\^k\$]{.arithmatex}.

等价于证明 [\$n\|2\displaystyle\sum\_{i=1}\^ni\^k\$]{.arithmatex} 和 [\$(n+1)\|2\displaystyle\sum\_{i=1}\^ni\^k\$]{.arithmatex}，显然

::: {.arithmatex}
\$\$\begin{aligned}2\sum\_{i=1}\^ni\^k&=\[1\^k+(n-1)\^k\]+\[2\^k+(n-2)\^k\]+\dots+\[(n-1)\^k+1\^k\]+2n\^k\\&=\[1\^k+n\^k\]+\[2\^k+(n-1)\^k\]+\dots+\[n\^k+1\^k\]\end{aligned}\$\$
:::

是 [\$n\$]{.arithmatex} 和 [\$n+1\$]{.arithmatex} 的倍数。

由上可知，为了证明 [\$b\|a\$]{.arithmatex}，只需将 [\$b\$]{.arithmatex} 分解成若干个两两互素的整数 [\$b_1,b_2,\dots,b_n\$]{.arithmatex} 之积，证明 [\$b_i\|a\$]{.arithmatex} 即可。

## 质数 {#_6}

- 定义：一个正整数无法被除了 [\$1\$]{.arithmatex} 和它自身之外的任何自然数整除，则成为质数，否则为合数。

- 数量：对于一个足够大的整数 [\$N\$]{.arithmatex}，不超过 [\$N\$]{.arithmatex} 的质数有 [\$\displaystyle\pi(x)\approx\frac{N}{\ln N}\$]{.arithmatex} 个，所以第 [\$n\$]{.arithmatex} 个质数约为 [\$n\ln n\$]{.arithmatex}.

- 判定：试除法，若 [\$N\$]{.arithmatex} 为合数，则存在一个能整除 [\$N\$]{.arithmatex} 的数 [\$T\$]{.arithmatex} 且 [\$2 \leq T \leq \sqrt{N}\$]{.arithmatex}.

- 算数基本定理：[\$N = p_1\^{c_1}p_2\^{c_2}\dots p_n\^{c_n}\$]{.arithmatex}，[\$N\$]{.arithmatex} 的正约数个数 [\$=\red{\boxed{\displaystyle\prod\_{i=1}\^{n}(c_i+1)}}\$]{.arithmatex}，[\$N\$]{.arithmatex} 的所有正约数的和 [\$=\displaystyle\prod\_{i=1}\^{n}(\displaystyle\sum\_{j=0}\^{c_i}(p_i)\^j)=\red{\boxed{\prod\_{i=1}\^n\frac{p_i\^{c_i+1}-1}{p_i-1}}}\$]{.arithmatex}.

一个正整数 [\$N\$]{.arithmatex} 的约数个数上界为 [\$2\sqrt{N}\$]{.arithmatex}，[\$1\$]{.arithmatex} \~ [\$N\$]{.arithmatex} 每个数的约数个数的总和大约为 [\$N\log N\$]{.arithmatex}.

- 设 [\$b\|ac\$]{.arithmatex}，若 [\$\gcd(b,c)=1\$]{.arithmatex}，则 [\$b\|a\$]{.arithmatex}.

- 设 [\$a,b\in\N\^\*\$]{.arithmatex} 且 [\$a,b\$]{.arithmatex} 之积是一个整数的 [\$k(k\geq 2)\$]{.arithmatex} 次幂，若 [\$\gcd(a,b)=1\$]{.arithmatex}，则 [\$a,b\$]{.arithmatex} 都是整数的 [\$k\$]{.arithmatex} 次幂。一般地，设正整数 [\$a,b,\dots,c\$]{.arithmatex} 之积是一个整数的 [\$k\$]{.arithmatex} 次幂，且 [\$a,b,\dots,c\$]{.arithmatex} 两两互质，则 [\$a,b,\dots,c\$]{.arithmatex} 都是整数的 [\$k\$]{.arithmatex} 次幂。

- 对任意正整数 [\$m\$]{.arithmatex} 及质数 [\$p\$]{.arithmatex}，记 [\$p\^c\Vert m\$]{.arithmatex} 表示 [\$p\^c\|m\$]{.arithmatex} 但 [\$p\^{c+1}\nmid m\$]{.arithmatex}，即 [\$p\^c\$]{.arithmatex} 是 [\$m\$]{.arithmatex} 的标准分解中出现的 [\$p\$]{.arithmatex} 的幂。

- 设 [\$n\>1,p\$]{.arithmatex} 为质数，[\$p\^{c_p}\Vert n!\$]{.arithmatex}，则 [\$c_p=\displaystyle\sum\_{l=1}\^{+\infty}\lfloor\frac{n}{p\^l}\rfloor\$]{.arithmatex}

例 1：证明无穷数列 [\$10001,100010001,\dots\$]{.arithmatex} 中无质数。

记 [\$\displaystyle a_n=1+10\^4+\dots+10\^{4(n-1)}=\frac{10\^{4n}-1}{10\^4-1}\$]{.arithmatex}，接下来分 [\$n\$]{.arithmatex} 为奇偶讨论即可。

::: {.arithmatex}
\$\$a\_{2k}=\frac{10\^{8k}-1}{10\^4-1}=\frac{10\^{8k}-1}{10\^8-1}\cdot\frac{10\^8-1}{10\^4-1}\$\$
:::

::: {.arithmatex}
\$\$a\_{2k+1}=\frac{10\^{4(2k+1)}-1}{10\^4-1}=\frac{10\^{2(2k+1)}-1}{10\^2-1}\cdot\frac{10\^{2(2k+1)}+1}{10\^2+1}\$\$
:::

例 2：证明 [\$\forall n\in\N\^\*,n\>1,n\^4+4\^n\$]{.arithmatex} 不是质数。

[\$n\$]{.arithmatex} 为偶数显然。[\$n\$]{.arithmatex} 为奇数时，设 [\$n=2k+1\$]{.arithmatex}，

::: {.arithmatex}
\$\$\begin{aligned}n\^4+4\^n&=n\^4+4\cdot 4\^{2k}=n\^4+4\cdot (2k)\^4=n\^4+4n\^2\cdot(2\^k)\^2+4\cdot(2k)\^4-4n\^2\cdot(2\^k)\^2\\&=(n\^2+2\cdot 2\^{2k})\^2-(2n\cdot 2\^k)\^2=(n\^2+2\^{k+1}n+2\^{2k+1})(n\^2-2\^{k+1}n+2\^{2k+1})\end{aligned}\$\$
:::

即把 [\$4\^n\$]{.arithmatex} 看成 [\$4y\^4\$]{.arithmatex}，有 [\$\red{\boxed{x\^4+4y\^4=(x\^2+2y\^2+2xy)(x\^2+2y\^2-2xy)}}\$]{.arithmatex}

练 1：设 [\$a,b,c,d\in\N\^\*,ab=cd\$]{.arithmatex}，证明 [\$a+b+c+d\$]{.arithmatex} 不是质数。

例 3：证明：若 [\$a,b\in\Z,2a\^2+a=3b\^2+b\$]{.arithmatex}，则 [\$a-b\$]{.arithmatex} 和 [\$2a+2b+1\$]{.arithmatex} 都为完全平方数。

已知化为 [\$(a-b)(2a+2b+1)=b\^2\$]{.arithmatex}，设 [\$d=\gcd(a-b,2a+2b+1)\$]{.arithmatex}，若 [\$d\>1\$]{.arithmatex}，则 [\$d\$]{.arithmatex} 有质因子 [\$p\$]{.arithmatex}，[\$p\|b\^2\implies p\|b\$]{.arithmatex}，[\$p\|(a-b)\implies p\|a\implies p\|1\$]{.arithmatex}，这不可能，因此 [\$d=1\$]{.arithmatex}. 因为 [\$b\^2\$]{.arithmatex} 是完全平方数，由此可得 [\$\|a-b\|，\|2a+2b+1\|\$]{.arithmatex} 也是完全平方。

只要证 [\$a-b\$]{.arithmatex} 和 [\$2a+2b+1\$]{.arithmatex} 不能同时 [\$\<0\$]{.arithmatex} 即可。设 [\$a-b\<0\$]{.arithmatex}，则 [\$b-a=r\^2\$]{.arithmatex}. 显然 [\$r\|b,r\|a\$]{.arithmatex}，令 [\$b=b_1r,a=a_1r\$]{.arithmatex}，代入题目 [\$a_1\^2+6a_1r+3r\^2+1=0\$]{.arithmatex}，得 [\$a_1=-3r\pm\sqrt{6r\^2-1}\$]{.arithmatex}，显然 [\$6r\^2-1\$]{.arithmatex} 应为完全平方数，而 [\$6r\^2-1\equiv 2\\ (\mathrm{mod}\\ 3)\$]{.arithmatex}，矛盾，原命题得证。

## 不定方程 {#_7}

例 1：证明两个连续正整数之积不能是完全平方或完全立方。

反证法，即设 [\$x(x+1)=y\^2\$]{.arithmatex} 有解，则 [\$(2x+1)\^2=4y\^2+1\$]{.arithmatex}，分解为

::: {.arithmatex}
\$\$(2x+1+2y)(2x+1-2y)=1\implies\begin{cases}2x+1+2y=1\\2x+1-2y=1\end{cases}\implies x=y=0\$\$
:::

显然不可能。类似的，对于完全立方，由于 [\$x\$]{.arithmatex} 和 [\$x+1\$]{.arithmatex} 互质，可得它们都是立方数。设 [\$x=u\^3,x+1=v\^3,y=uv,v\^3-u\^3=1=(v-u)(v\^2+uv+u\^2)\$]{.arithmatex}，显然不可能。

类似的，可证明连续两个正整数之积不能是整数的 [\$k(k\geq 2)\$]{.arithmatex} 次幂。

练 1：设 [\$k\in\N\^\*,k\geq 2\$]{.arithmatex}，证明：连续三个正整数之积不能是整数的 [\$k\$]{.arithmatex} 次幂。

提示：[\$x(x\^2-1)=y\^k\implies a\^kb\^k=(ab)\^k,1=a\^{2k}-b\^k=(a\^2)\^k-b\^k\$]{.arithmatex}，导出矛盾。

------------------------------------------------------------------------

例 2：证明方程 [\$y\^2+y=x+x\^2+x\^3\$]{.arithmatex} 没有 [\$x\neq 0\$]{.arithmatex} 的整数解。

转化为 [\$(y-x)(y+x+1)=x\^3\$]{.arithmatex}，可以证明 [\$\gcd(y-x,y+x+1)=1\$]{.arithmatex}，设 [\$y-x=a\^3,y+x+1=b\^3,x=ab\$]{.arithmatex}，可得 [\$b\^3-a\^3=(b-a)(b\^2+ab+a\^2)=2ab+1③\$]{.arithmatex}，证明该方程无解即可。[\$ab\>0\$]{.arithmatex} 时，[\$b-a\geq 1\$]{.arithmatex}，③的左边 [\$\geq 3ab\>\$]{.arithmatex} 右边；[\$ab\<0\$]{.arithmatex} 时，③的左边的绝对值 [\$\geq 2(a\^2+b\^2-\|ab\|)\>2\|ab\|\>\$]{.arithmatex} ③的右边的绝对值。因此原命题成立。

练 2：求方程 [\$(x\^2-y\^2)\^2=1+16y\$]{.arithmatex} 的所有整数解。

提示：[\$y\geq 0，\|x\|\geq\$]{.arithmatex} 或 [\$\leq y+1\$]{.arithmatex}，均可得出 [\$(x\^2-y\^2)\^2\geq(2y-1)\^2\$]{.arithmatex}，得 [\$(2y-1)\^2\leq 1+16y\$]{.arithmatex}，答案 [\$(x,y)=(\pm 1,0),(\pm 4,3)(\pm4,5)\$]{.arithmatex}.

------------------------------------------------------------------------

例 3：设 [\$x,y,z\in\N\^\*,2x\^x=y\^y+z\^z\$]{.arithmatex}，证明 [\$x=y=z\$]{.arithmatex}.

::: {.arithmatex}
\$\$(x+1)\^{x+1}\>x\^{x+1}+(x+1)x\^x\>2x\^x\implies y,z\leq x\$\$
:::

反之，设 [\$y\geq x+1\$]{.arithmatex}，则 [\$y\^y+z\^z\>(x+1)\^{x+1}\>2x\^x\$]{.arithmatex}，矛盾。而 [\$y\^y+z\^z\leq x\^x+x\^x=2x\^x\$]{.arithmatex}，所以 [\$x=y=z\$]{.arithmatex}.

## 欧拉函数 {#_8}

[\$1\$]{.arithmatex} \~ [\$N\$]{.arithmatex} 中与 [\$N\$]{.arithmatex} 互质的数的个数被称为欧拉函数，记为 [\$\varphi(N)\$]{.arithmatex}. 用数学符号表示即为 [\$\varphi(N)=\displaystyle\sum\_{i=1}\^{N}\[\gcd(i,N)=1\]\$]{.arithmatex}.

若 [\$N = p_1\^{c_1}p_2\^{c_2}\dots p_n\^{c_n}\$]{.arithmatex}，则 [\$\displaystyle\varphi(N)=N\times\frac{p_1-1}{p_1}\times\frac{p_2-1}{p_2}\times\dots\times\frac{p_n-1}{p_n}=N\cdot\displaystyle\prod\_{质数p\|N}\left(1-\frac{1}{p}\right)\$]{.arithmatex}

证明：设 [\$p,q\$]{.arithmatex} 为 [\$N\$]{.arithmatex} 的不同质因子，[\$1\$]{.arithmatex} \~ [\$N\$]{.arithmatex} 中 [\$p\$]{.arithmatex} 的倍数有 [\$\displaystyle \frac{N}{p}\$]{.arithmatex} 个，[\$q\$]{.arithmatex} 的倍数有 [\$\displaystyle \frac{N}{q}\$]{.arithmatex} 个。若把 [\$\displaystyle \frac{N}{p}+\frac{N}{q}\$]{.arithmatex} 个数去掉，则 [\$\displaystyle\frac{N}{pq}\$]{.arithmatex} 被计算了 [\$2\$]{.arithmatex} 次（容斥原理）。因此， [\$1\$]{.arithmatex} \~ [\$N\$]{.arithmatex} 中不与 [\$N\$]{.arithmatex} 含有相同质因子的 [\$p\$]{.arithmatex} 或 [\$q\$]{.arithmatex} 数量为 [\$\displaystyle N-\frac{N}{p}-\frac{N}{q}+\frac{N}{pq}=N\left(1-\frac{1}{p}\right)\left(1-\frac{1}{q}\right)\$]{.arithmatex}，对 [\$N\$]{.arithmatex} 的全部质因子继续容斥即可得到公式。

| [\$n\$]{.arithmatex} | [\$1\$]{.arithmatex} | [\$2\$]{.arithmatex} | [\$3\$]{.arithmatex} | [\$4\$]{.arithmatex} | [\$5\$]{.arithmatex} | [\$6\$]{.arithmatex} | [\$7\$]{.arithmatex} | [\$8\$]{.arithmatex} | [\$9\$]{.arithmatex} | [\$10\$]{.arithmatex} | [\$11\$]{.arithmatex} | [\$12\$]{.arithmatex} | [\$13\$]{.arithmatex} | [\$14\$]{.arithmatex} | [\$15\$]{.arithmatex} |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| [\$\varphi(n)\$]{.arithmatex} | [\$1\$]{.arithmatex} | [\$1\$]{.arithmatex} | [\$2\$]{.arithmatex} | [\$2\$]{.arithmatex} | [\$4\$]{.arithmatex} | [\$2\$]{.arithmatex} | [\$6\$]{.arithmatex} | [\$4\$]{.arithmatex} | [\$6\$]{.arithmatex} | [\$4\$]{.arithmatex} | [\$10\$]{.arithmatex} | [\$4\$]{.arithmatex} | [\$12\$]{.arithmatex} | [\$6\$]{.arithmatex} | [\$8\$]{.arithmatex} |

欧拉函数的性质：

1.  [\$\forall n\>1\$]{.arithmatex}，[\$1\$]{.arithmatex} \~ [\$n\$]{.arithmatex} 中与 [\$n\$]{.arithmatex} 互质的数的和为 [\$\displaystyle\frac{n\times\varphi(n)}{2}\$]{.arithmatex}.
2.  若 [\$a,b\$]{.arithmatex} 互质，则 [\$\varphi(ab)=\varphi(a)\varphi(b)\$]{.arithmatex}.
3.  设 [\$p\$]{.arithmatex} 为质数，[\$\varphi(p)=p-1\$]{.arithmatex}.
4.  设 [\$p\$]{.arithmatex} 为质数，[\$k\in\N\^\*,\varphi(p\^k)=p\^{k-1}\times(p-1)=p\^k-p\^{k-1}\$]{.arithmatex}.
5.  设 [\$p\$]{.arithmatex} 为质数，若 [\$p\mid n\$]{.arithmatex} 且 [\$p\^2\mid n\$]{.arithmatex}，则 [\$\displaystyle\varphi(n)=\varphi\left(\frac{n}{p}\right)\times p\$]{.arithmatex}.
6.  设 [\$p\$]{.arithmatex} 为质数，若 [\$p\mid n\$]{.arithmatex} 但 [\$p\^2\nmid n\$]{.arithmatex}，则 [\$\displaystyle\varphi(n)=\varphi\left(\frac{n}{p}\right)\times (p-1)\$]{.arithmatex}.
7.  若 [\$n\$]{.arithmatex} 为奇数，则 [\$\varphi(2n)=\varphi(n)\$]{.arithmatex}.
8.  [\$\forall n\geq 3,\\ n\in\N\^\*,\\ 2\mid\varphi(n)\$]{.arithmatex}.
9.  欧拉反演：[\$\displaystyle\sum\_{d\mid n}\varphi(d)=n\$]{.arithmatex}.

证明：

1.  因为 [\$\gcd(n,x)=\gcd(n,n-x)\$]{.arithmatex}，所以与 [\$n\$]{.arithmatex} 不互质的数 [\$x,n-x\$]{.arithmatex} 成对出现，平均值为 [\$\displaystyle\frac{n}{2}\$]{.arithmatex}. [\$\\\$]{.arithmatex} 因此与 [\$n\$]{.arithmatex} 互质的数的平均值也是 [\$\displaystyle\frac{n}{2}\$]{.arithmatex}，进而得到性质 1。
2.  根据欧拉函数的计算式可直接获得性质 2。
3.  根据欧拉函数的定义可直接获得性质 3。
4.  从 [\$1\$]{.arithmatex} \~ [\$p\^{k}\$]{.arithmatex} 中的所有数，除了 [\$p\^{k-1}\$]{.arithmatex} 个 [\$p\$]{.arithmatex} 的倍数外都与 [\$p\^k\$]{.arithmatex} 互素。
5.  若 [\$p\mid n\$]{.arithmatex} 且 [\$p\^2\mid n\$]{.arithmatex}，则 [\$\displaystyle n,\frac{n}{p}\$]{.arithmatex} 包含相同的质因子，只是 [\$p\$]{.arithmatex} 的指数不同。[\$\\\$]{.arithmatex} 按照欧拉函数的计算公式，[\$\displaystyle \frac{\varphi(n)}{\varphi(\frac{n}{p})}=\frac{n}{\frac{n}{p}}=p\$]{.arithmatex}，得到性质 5。
6.  若 [\$p\mid n\$]{.arithmatex} 且 [\$p\^2\mid n\$]{.arithmatex}，则 [\$\displaystyle n,\frac{n}{p}\$]{.arithmatex} 互质。因为 [\$\displaystyle\varphi(n)=\varphi\left(\frac{n}{p}\right)\varphi(p)\$]{.arithmatex}，而 [\$\varphi(p)=p-1\$]{.arithmatex}，得到性质 6。
7.  [\$\forall m\<2n,m\in\N\^\*\$]{.arithmatex}，若 [\$2\mid m\$]{.arithmatex}，则 [\$\gcd(m,2n)\neq 1\$]{.arithmatex}，也就是对欧拉函数的值没有贡献；[\$\\\$]{.arithmatex} 若 [\$2\nmid m\$]{.arithmatex}，则 [\$\gcd(m,2n)=1\$]{.arithmatex}，欧拉函数的值也就与 [\$2n\$]{.arithmatex} 中的偶质因子无关。
8.  [\$n\geq 3\$]{.arithmatex} 时，与 [\$n\$]{.arithmatex} 互质的数不可能为 [\$\displaystyle\frac{n}{2}\implies\forall x\<n,\gcd(x,n)=\gcd(n-x,n)\$]{.arithmatex}，也就是存在一一对应关系。
9.  设 [\$f(n)=\displaystyle\sum\_{d\mid n}\varphi(d)\$]{.arithmatex}，利用 [\$\varphi\$]{.arithmatex} 是积性函数，得到：[\$\\\$]{.arithmatex} 若 [\$n,m\$]{.arithmatex} 互质，则 [\$f(nm)=\displaystyle\sum\_{d\mid nm}\varphi(d)=\displaystyle\sum\_{d\mid n}\varphi(d)\cdot\displaystyle\sum\_{d\mid m}\varphi(d)=f(n)f(m)\$]{.arithmatex}，即 [\$f(n)\$]{.arithmatex} 是积性函数。[\$\\\$]{.arithmatex} 对于单个质因子有：[\$\begin{aligned}f(p\^m)&=\displaystyle\sum\_{d\mid p\^m}\varphi(d)=\displaystyle\sum\_{i=0}\^{m}\varphi(p\^i)=\varphi(1)+\varphi(p)+\varphi(p\^2)+\varphi(p\^3)+\dots+\varphi(p\^m)\\&= 1+(p-1)+(p-1)p+(p-1)p\^2+\dots+(p-1)p\^{m-1}\\&=1+(p-1)+(p\^2-p)+(p\^3-p\^2)+\dots+(p\^m-p\^{m-1})=p\^m\end{aligned} \\\$]{.arithmatex} 所以 [\$f(n)=\displaystyle\prod\_{i=1}\^{m}f(p_i\^{c_i})=\displaystyle\prod\_{i=1}\^{m}p_i\^{c_i}=n\$]{.arithmatex}

### 积性函数与完全积性函数 {#_9}

若函数 [\$f(x)\$]{.arithmatex} 满足 [\$f(1)=1\$]{.arithmatex} 且 [\$\forall x,y\in\N\^{\*},\gcd(x,y)=1\$]{.arithmatex} 都有 [\$f(xy)=f(x)f(y)\$]{.arithmatex}，则 [\$f(x)\$]{.arithmatex} 是积性函数。

若函数 [\$f(x)\$]{.arithmatex} 满足 [\$f(1)=1\$]{.arithmatex} 且 [\$\forall x,y\in\N\^{\*}\$]{.arithmatex} 都有 [\$f(xy)=f(x)f(y)\$]{.arithmatex}，则 [\$f(x)\$]{.arithmatex} 是完全积性函数。

性质：

1.  若 [\$f(x)\$]{.arithmatex} 和 [\$g(x)\$]{.arithmatex} 均为积性函数，则以下函数也为积性函数： \$[\$\begin{aligned}h(x)&=f(x\^p) \\ h(x)&=f\^p(x) \\ h(x)&=f(x)g(x) \\ h(x)&=\displaystyle\sum\_{d\mid x}f(d)g\left(\frac{x}{d}\right)\end{aligned}\$]{.arithmatex}\$
2.  设 [\$x=\displaystyle\prod p_i\^{c_i}\$]{.arithmatex}，

若 [\$f(x)\$]{.arithmatex} 为积性函数，则 [\$f(x)=\displaystyle\prod f(p_i\^{c_i})\$]{.arithmatex}。

若 [\$f(x)\$]{.arithmatex} 为完全积性函数，则 [\$f(x)=\displaystyle\prod f\^{c_i}(p_i)\$]{.arithmatex}。

例子：

积性函数：[\$\varphi(n),\sigma \_k(n)=\displaystyle\sum\_{d\mid n}d\^k,\sigma \_0(n)\$]{.arithmatex} 通常简记为 [\$d(n)\$]{.arithmatex} 或 [\$\tau(n)\$]{.arithmatex}，[\$\sigma \_1(n)\$]{.arithmatex} 通常简记为 [\$\sigma(n)\$]{.arithmatex}。

完全积性函数：[\$\varepsilon(n)=\[n=1\],\text{id}\_k(n)=n\^k,\text{id}\_1(n)\$]{.arithmatex} 通常简记为 [\$\text{id}(n),f(n)=1\$]{.arithmatex}.

## 同余 {#_10}

- 平方数 [\$\mathrm{mod}\\ 4\equiv 0\$]{.arithmatex} 或 [\$1,\mathrm{mod}\\ 8\equiv0\$]{.arithmatex} 或 [\$1\$]{.arithmatex} 或 [\$4,\mathrm{mod}\\ 3\equiv 0\$]{.arithmatex} 或 [\$1,\mathrm{mod}\\ 5\equiv0\$]{.arithmatex} 或 [\$\pm 1\$]{.arithmatex}.
- 立方数 [\$\mathrm{mod}\\ 9\equiv 0\$]{.arithmatex} 或 [\$\pm 1\$]{.arithmatex}.
- 四次幂 [\$\mathrm{mod}\\ 16\equiv 0\$]{.arithmatex} 或 [\$1\$]{.arithmatex}.

例如可证明 [\$a,b,c,d\in\N\^\*,a\^{4b+d}-a\^{4c+d}\$]{.arithmatex} 能被 [\$240=2\^4\times 3\times 5\$]{.arithmatex} 整除。

例 1：设 [\$a,b,c\in\Z,a+b+c=0,d=a\^{1999}+b\^{1999}+c\^{1999}\$]{.arithmatex}，证明 [\$d\$]{.arithmatex} 可被 [\$6\$]{.arithmatex} 整除。

::: {.arithmatex}
\$\$u\^{1999}\equiv u(\mathrm{mod}\\ 2)\implies d\equiv a+b+c\equiv 0(\mathrm{mod}\\ 2)\implies2\|d\$\$
:::

::: {.arithmatex}
\$\$u\^3\equiv u(\mathrm{mod}\\ 3)\implies u\^{1999}\equiv u\cdot u\^{1998}\equiv u\cdot u\^{666}\equiv u\cdot u\^{222}\equiv u\^{75}\equiv u\^{25}\equiv u\^9\equiv u(\mathrm{mod}\\ 3)\$\$
:::

注意 [\$u\^3\equiv u(\mathrm{mod}\\ 3)\$]{.arithmatex} 是费马小定理的特殊情形。

练 1：设 [\$x,y,z\in\Z,(x-y)(y-z)(z-x)=x+y+z\$]{.arithmatex}，证明 [\$27\|(x+y+z)\$]{.arithmatex}.

只要证明 [\$x,y,z\$]{.arithmatex} 两两模 [\$3\$]{.arithmatex} 同余即可。

练 2：证明 [\$11,111,1111,\dots\$]{.arithmatex} 不是完全平方数。只要知道 [\$11\\ \mathrm{mod}\\ 4\neq 0\$]{.arithmatex} 即可。

------------------------------------------------------------------------

例 2：数列 [\$\set{x_n}\$]{.arithmatex} 为 [\$1,3,5,11,\dots\$]{.arithmatex}，满足 [\$x\_{n+1}=x_n+2x\_{n-1}\$]{.arithmatex}.

数列 [\$\set{y_n}\$]{.arithmatex} 为 [\$7,17,55,161,\dots\$]{.arithmatex}，满足 [\$y\_{n+1}=2y_n+3y\_{n-1}\$]{.arithmatex}. 证明：两个数列无相同项。

考虑以 [\$8\$]{.arithmatex} 为模，因为 [\$x_2\equiv 3,x_3\equiv 5\$]{.arithmatex}. 若 [\$x\_{n-1}\equiv 3,x_n\equiv 5\$]{.arithmatex}，则 [\$x\_{n+1}\equiv 3,x\_{n+2}\equiv 5\$]{.arithmatex}.

显然 [\$\set{x_n}\$]{.arithmatex} 是模 [\$8\$]{.arithmatex} 后的周期数列，同理 [\$\set{y_n}\$]{.arithmatex} 也是（ [\$7,1,7,1,\dots\$]{.arithmatex} ），于是命题得证。

### 费马小定理与欧拉定理 {#_11}

若整数 [\$a\$]{.arithmatex} 和整数 [\$b\$]{.arithmatex} 除以正整数 [\$m\$]{.arithmatex} 的余数相等，则称 [\$a,b\$]{.arithmatex} 模 [\$m\$]{.arithmatex} 同余，记为 [\$a\equiv b\\ (\mathrm{mod}\\ m)\$]{.arithmatex}.

并且注意到 [\$\displaystyle k\\ \mathrm{mod}\\ i=k-\left\lfloor\frac{k}{i}\right\rfloor\cdot i\$]{.arithmatex}，且同余满足同加性、同乘性、同幂性，但不满足同除性。

对于 [\$\forall a \in \[0, m - 1\]\$]{.arithmatex}，集合 [\$\set{a+km\\ (k\in\Z)}\$]{.arithmatex} 的所有数模 [\$m\$]{.arithmatex} 同余，余数都是 [\$a\$]{.arithmatex}. 该集合称为一个模 [\$m\$]{.arithmatex} 的同余类，简记为 [\$\overline{a}\$]{.arithmatex}.

模 [\$m\$]{.arithmatex} 的同余类一共有 [\$m\$]{.arithmatex} 个，分别为 [\$\overline{0},\overline{1},\overline{2},\dots,\overline{m-1}\$]{.arithmatex}. 它们构成 [\$m\$]{.arithmatex} 的完全剩余系。

[\$1\$]{.arithmatex} \~ [\$m\$]{.arithmatex} 中与 [\$m\$]{.arithmatex} 互质的数代表的同余类共有 [\$\varphi(m)\$]{.arithmatex} 个，它们构成 [\$m\$]{.arithmatex} 的简化剩余系。[\$\\\$]{.arithmatex} 例如，模 [\$10\$]{.arithmatex} 的简化剩余系为 [\$\set{\overline{1},\overline{3},\overline{7},\overline{9}}\$]{.arithmatex}。

若从某个非空数集中任选两个元素（同一元素可重复选出），选出的这两个元素通过某种（或几种）运算后的得数仍是该数集中的元素，那么，就说该集合对于这种（或几种）运算是封闭的。[\$\\\$]{.arithmatex} 例如若一个集合中的元素，如果能够做到做加法运算的结果还在这个集合中，就说这个集合对加法运算封闭。[\$\\\$]{.arithmatex} 例如 [\$\N\$]{.arithmatex} 对加法、乘法运算是封闭的；[\$\Z\$]{.arithmatex} 对加、减、乘法运算是封闭的；[\$\mathbb{Q}, \mathbb{C}\$]{.arithmatex} 对四则运算是封闭的。

简化剩余系关于模 [\$m\$]{.arithmatex} 乘法封闭。这是因为若 [\$a,b\\ (1\leq a,b\leq m)\$]{.arithmatex} 与 [\$m\$]{.arithmatex} 互质，则 [\$ab\$]{.arithmatex} 也与 [\$m\$]{.arithmatex} 互质。[\$\\\$]{.arithmatex} 由余数的定义得 [\$ab\\ \mathrm{mod}\\ m\$]{.arithmatex} 也与 [\$m\$]{.arithmatex} 互质，即 [\$ab\\ \mathrm{mod}\\ m\$]{.arithmatex} 也属于 [\$m\$]{.arithmatex} 的简化剩余系。

- 费马小定理：若 [\$p\$]{.arithmatex} 是质数，则对于任意整数 [\$a\$]{.arithmatex}，有 [\$a\^p\equiv a\\ (\mathrm{mod}\\ p)\$]{.arithmatex}.
- 欧拉定理：若正整数 [\$a,n\$]{.arithmatex} 互质，则 [\$a\^{\varphi(n)}\equiv 1\\ (\mathrm{mod}\\ n)\$]{.arithmatex}.

证明：设 [\$n\$]{.arithmatex} 的简化剩余系为 [\$\set{\overline{a_1},\overline{a_2},\dots,\overline{a\_{\varphi(n)}}}\$]{.arithmatex}. [\$\forall a_i,a_j\$]{.arithmatex}，若 [\$a\cdot a_i\equiv a\cdot a_j\\ (\mathrm{mod}\\ n)\$]{.arithmatex}，则 [\$a\cdot(a_i-a_j)\equiv 0.\$]{.arithmatex} 因为 [\$a,n\$]{.arithmatex} 互质，所以 [\$a_i\equiv a_j\$]{.arithmatex}. 故当 [\$a_i\neq a_j\$]{.arithmatex} 时，[\$aa_i,aa_j\$]{.arithmatex} 也代表不同的同余类。

又因为简化剩余系关于模 [\$m\$]{.arithmatex} 乘法封闭，故 [\$\overline{aa_1}\$]{.arithmatex} 也在简化剩余系集合中。因此，集合 [\$\set{\overline{a_1},\overline{a_2},\dots,\overline{a\_{\varphi(n)}}}\$]{.arithmatex} 与集合 [\$\set{\overline{aa_1},\overline{aa_2},\dots,\overline{aa\_{\varphi(n)}}}\$]{.arithmatex} 都能表示 [\$n\$]{.arithmatex} 的简化剩余系。综上所述：

::: {.arithmatex}
\$\$a\^{\varphi(n)}a_1a_2\dots a\_{\varphi(n)}\equiv(aa_1)(aa_2)\dots(aa\_{\varphi(n)})\equiv a_1a_2\dots a\_{\varphi(n)}\\ (\mathrm{mod}\\ n)\$\$
:::

因此 [\$a\^{\varphi(n)}\equiv 1\\ (\mathrm{mod}\\ n)\$]{.arithmatex}。当 [\$p\$]{.arithmatex} 为质数时，满足 [\$\varphi(p)=p-1\$]{.arithmatex}，两边同乘 [\$a\$]{.arithmatex} 即可得到费马小定理。

另外，当 [\$a\$]{.arithmatex} 是 [\$p\$]{.arithmatex} 的倍数，费马小定理显然成立。

------------------------------------------------------------------------

- 欧拉定理的推论：若正整数 [\$a,n\$]{.arithmatex} 互质，则对于任意正整数 [\$b\$]{.arithmatex}，有 [\$a\^b\equiv a\^{b\\ \mathrm{mod}\\ \varphi(n)}\\ (\mathrm{mod}\\ n)\$]{.arithmatex}

证明：设 [\$b=q\cdot \varphi(n)+r\$]{.arithmatex}，其中 [\$0\leq r\<\varphi(n)\$]{.arithmatex}，即 [\$r=b\\ \mathrm{mod}\\ \varphi(n)\$]{.arithmatex}. 于是有：

::: {.arithmatex}
\$\$a\^b\equiv a\^{q\cdot\varphi(n)+r}\equiv (a\^{\varphi(n)})\^q\cdot a\^r\equiv 1\^q\cdot a\^r\equiv a\^r\equiv a\^{b\\ \mathrm{mod}\\ \varphi(n)}\\ (\mathrm{mod}\\ n)\$\$
:::

证毕。面对 [\$a+b,a-b,a\cdot b\$]{.arithmatex} 这样的算式，可以在计算前先把 [\$a,b\$]{.arithmatex} 对 [\$p\$]{.arithmatex} 取模。面对 [\$a\^b\$]{.arithmatex} 这样的乘方算式，可以先把底数对 [\$p\$]{.arithmatex} 取模、指数对 [\$\varphi(p)\$]{.arithmatex} 取模，再计算乘方。

即 [\$a\^b\equiv (a\\ \mathrm{mod}\\ p)\^{b\\ \mathrm{mod}\\ \varphi(p)}\\ (\mathrm{mod}\\ p)\$]{.arithmatex}

------------------------------------------------------------------------

- 扩展欧拉定理

\$[\$a\^b\equiv\begin{cases}a\^{b\\ \mathrm{mod}\\ \varphi(m)}&\text{if }\gcd(a,m)=1\\ a\^b&\text{if }\gcd(a,m)\neq 1,b\<\varphi(m)\\ a\^{b\\ \mathrm{mod}\\ \varphi(m)+\varphi(m)}&\text{if }\gcd(a,m)\neq 1,b\geq\varphi(m)\end{cases}\\ (\mathrm{mod}\\ m)\$]{.arithmatex}\$

证明十分显然，略。

------------------------------------------------------------------------

- 若正整数 [\$a,n\$]{.arithmatex} 互质，则满足 [\$a\^x\equiv 1\\ (\mathrm{mod}\\ n)\$]{.arithmatex} 的最小正整数 [\$x_0\$]{.arithmatex} 是 [\$\varphi(n)\$]{.arithmatex} 的约数。

反证法，假设满足 [\$a\^x\equiv 1\\ (\mathrm{mod}\\ n)\$]{.arithmatex} 的最小正整数 [\$x_0\$]{.arithmatex} 不能整除 [\$\varphi(n)\$]{.arithmatex}.

设 [\$\varphi(n)=qx_0+r\\ (0\<r\<x_0)\$]{.arithmatex}，因为 [\$a\^{x_0}\equiv 1\\ (\mathrm{mod}\\ n)\$]{.arithmatex}，所以 [\$a\^{qx_0}\equiv 1\\ (\mathrm{mod}\\ n)\$]{.arithmatex}. 根据欧拉定理 [\$a\^{\varphi(n)}\equiv 1\\ (\mathrm{mod}\\ n)\$]{.arithmatex}，所以 [\$a\^r\equiv 1\\ (\mathrm{mod}\\ n)\$]{.arithmatex}. 这与 [\$x_0\$]{.arithmatex} 最小矛盾。故假设不成立，原命题成立。

### 中国剩余定理 {#_12}

设 [\$m_1,m_2,\dots,m_n\$]{.arithmatex} 是两两互质的整数，[\$m=\displaystyle\prod\_{i=1}\^n m_i,M_i=\frac{m}{m_i},t_i\$]{.arithmatex} 是线性同余方程 [\$M_it_i\equiv 1\\ (\mathrm{mod}\\ m_i)\$]{.arithmatex} 的一个解。对于任意的 [\$n\$]{.arithmatex} 个整数，方程组

::: {.arithmatex}
\$\$\begin{cases}x\equiv a_1\\ (\mathrm{mod}\\ m_1) \\ x\equiv a_2\\ (\mathrm{mod}\\ m_2)\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \vdots\\ x\equiv a_n\\ (\mathrm{mod}\\ m_n)\end{cases}\$\$
:::

有整数解，解为 [\$x=\displaystyle\sum\_{i=1}\^{n}a_iM_it_i\$]{.arithmatex}，通解可以表示为 [\$x+km(k\in\Z)\$]{.arithmatex}，最小非负整数解为 [\$x\\ \mathrm{mod}\\ m\$]{.arithmatex}.

证明：因为 [\$\displaystyle M_i=\frac{m}{m_i}\$]{.arithmatex} 是除了 [\$m_i\$]{.arithmatex} 之外所有模数的倍数，所以 [\$\forall k\neq i,a_iM_it_i\equiv 0\\ (\mathrm{mod}\\ m_i)\$]{.arithmatex}，[\$\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \text{}\$]{.arithmatex} 所以代入 [\$x=\displaystyle\sum\_{i=1}\^{n}a_iM_it_i\$]{.arithmatex}，原方程组成立。

### 威尔逊定理 {#_13}

- [\$p\$]{.arithmatex} 为素数 [\$\xLeftrightarrow{}(p-1)!\equiv -1\\ (\mathrm{mod}\\ p)\$]{.arithmatex}

证明：

1.  充分性

对于 [\$p\$]{.arithmatex} 不是素数的情况，有 [\$\begin{cases} p=1 & (1-1)!\equiv 0\\ (\mathrm{mod}\\ 1) \\ p=4 & (4-1)!\equiv 2\\ (\mathrm{mod}\\ 4) \\ p\>4 & 分类讨论得出\\ (p-1)!\equiv 0\\ (\mathrm{mod}\\ p) \end{cases}\$]{.arithmatex}

\(a\) 当 [\$p\$]{.arithmatex} 为完全平方数。

    则 $p=k^2$ 且 $k>2$，用相减法比较 $2k$ 与 $p$ 的大小得 $2k<p$，于是有

    $$\begin{aligned}(p-1)!&=1\times 2\times\dots\times k\times\dots\times 2k\times\dots\times (p-1)\\ &=2nk^2\\&=2np\end{aligned}$$

    所以 $(p-1)!\equiv 0\ (\mathrm{mod}\ p)$ 且 $p$ 为完全平方数。

    (b) 当 $p$ 不为完全平方数。

    则 $p$ 可以表示为两个不相等的数 $a$ 和 $b$ 的乘积，设 $a<b$，则有 $p=ab,1<a<b<p$

    $$\begin{aligned}(p-1)!&=1\times 2\times\dots\times a\times\dots\times b\times\dots\times (p-1)\\&=a\times b\times n\\ &=np\end{aligned}$$

    所以 $(p-1)!\equiv 0\ (\mathrm{mod}\ p)$ 且 $p$ 不为完全平方数。

1.  必要性

当 [\$p\$]{.arithmatex} 为素数时，考虑二次剩余式 [\$x\^2\equiv 1\\ (\mathrm{mod}\\ p)\$]{.arithmatex}，化简得 [\$(x-1)(x+1)\equiv 0\\ (\mathrm{mod}\\ p)\$]{.arithmatex}

于是 [\$x\equiv 1\\ (\mathrm{mod}\\ p)\$]{.arithmatex} 或 [\$x\equiv p-1\\ (\mathrm{mod}\\ p)\$]{.arithmatex}。现在先抛开 [\$1\$]{.arithmatex} 和 [\$p-1\$]{.arithmatex} 不管，

[\$\forall a\in \[2,p-2\]\$]{.arithmatex}，必然存在一个和它不相等的逆元 [\$a\^{-1}\in\[2,p-2\]\$]{.arithmatex}，满足 [\$aa\^{-1}\equiv 1\\ (\mathrm{mod}\\ p)\$]{.arithmatex}

所以必然有 [\$\displaystyle\frac{p-3}{2}\$]{.arithmatex} 对数相乘的乘积为 [\$1\$]{.arithmatex}，即 [\$(p-2)!\equiv 1\\ (\mathrm{mod}\\ p)\$]{.arithmatex}

等式两边同时乘 [\$p-1\$]{.arithmatex} 就得到威尔逊定理。

例题：[\$n\in\N\^\*\$]{.arithmatex} 且 [\$n\leq 10\^6\$]{.arithmatex}，求 [\$S_n\$]{.arithmatex}.

::: {.arithmatex}
\$\$S_n=\displaystyle\sum\_{k=1}\^{n}\left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor\$\$
:::

令 [\$d=3k+7\$]{.arithmatex}，原式化简为

::: {.arithmatex}
\$\$S_n=\displaystyle\sum\_{k=1}\^{n}\left\lfloor\frac{(d-1)!+1}{d}-\left\lfloor\frac{(d-1)!}{d}\right\rfloor\right\rfloor\$\$
:::

由威尔逊定理，当 [\$d\$]{.arithmatex} 为素数时，[\$\displaystyle\frac{(d-1)!+1}{d}\$]{.arithmatex} 必然是整数，而 [\$\displaystyle\left\lfloor\frac{(d-1)!}{d}\right\rfloor\$]{.arithmatex} 必然比 [\$\displaystyle\frac{(d-1)!+1}{d}\$]{.arithmatex} 小 [\$1\$]{.arithmatex}，于是有：

::: {.arithmatex}
\$\$\begin{cases}p\\ 为素数 & \displaystyle\left\lfloor\frac{(d-1)!+1}{d}-\left\lfloor\frac{(d-1)!}{d}\right\rfloor\right\rfloor=1 \\ p\\ 为合数 & \displaystyle\left\lfloor\frac{(d-1)!+1}{d}-\left\lfloor\frac{(d-1)!}{d}\right\rfloor\right\rfloor=0\end{cases}\$\$
:::

所以只需统计 [\$\[1,3\times 10\^6+7\]\$]{.arithmatex} 中的素数即可得出答案。

## 拉格朗日定理 {#_14}

若 [\$p\$]{.arithmatex} 是质数，则对于模 [\$p\$]{.arithmatex} 意义下的 [\$n\$]{.arithmatex} 次整系数多项式 [\$f(x)=a_nx\^n+a\_{n-1}x\^{n-1}+\dots+a_0(p\nmid a_n)\$]{.arithmatex} 同余方程 [\$f(x)\equiv 0(\mathrm{mod}\\ p)\$]{.arithmatex} 至多有 [\$n\$]{.arithmatex} 个不同的解。
