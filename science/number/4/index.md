# 数论测试

## 一、请给出整除的概念及性质

对于整数 *a*, *b* (*b* ≠ 0)，如果存在整数 *c*，使得 *a* = *b\*\*c*，

则称 *b* 整除 *a*，记作 *b* ∣ *a*；否则称 *b* 不整除 *a*，记作 *b* ∤ *a*。

**性质**：

$$ \\def\\arraystretch{1.1} \\begin{array}{rlrl} 1.&a\\mid b&\\Longrightarrow&\\pm a \\mid \\pm b\\ 2.&a \\mid b,\\ b\\mid c&\\Longrightarrow&a \\mid c\\ 3.&\\forall i:b\\mid a_i&\\Longrightarrow&b\\mid\\Sigma\\ a_ik_i\\ 4.&b\\mid a&\\Longrightarrow&bc\\mid ac\\ (c\\in\\mathbb Z,c\\neq0)\\ 5.&b\\mid a\\ (a\\neq0)&\\Longrightarrow&|b|\\le|a|\\ 5.&b\\mid a,\\ |a|\<|b|&\\Longrightarrow&a=0\\ \\end{array} $$

### 二、请给出同余的概念及性质

给定正整数 *m* 称为模，*a*, *b* 为任意两个整数，满足：

$$ \\def\\arraystretch{1.1} \\begin{array}{ll} a=q_1m+r_1,&0\\le r_1\<m\\ b=q_2m+r_2,&0\\le r_2\<m\\ \\end{array} $$

则称 *a*, *b* 对 *m* 同余，记作 *a* ≡ *b* (mod  *m*)，简记为 *a* ≡ *b* (*m*)。

**性质**：

$$ \\def\\arraystretch{1.1} \\begin{array}{rlrl} 1.&a \\equiv a \\pmod m\\ 2.&a \\equiv b \\pmod m &\\Longleftrightarrow& b\\equiv a \\pmod m\\ 3.&a\\equiv b\\pmod m,\\ b\\equiv c\\pmod m&\\Longrightarrow&a\\equiv c\\pmod m\\ 4.&aK\\equiv bK\\pmod m&\\Longrightarrow&a\\equiv b\\pmod{\\frac{m}{(m,k)}}\\ 5.&a\\equiv b\\pmod m,\\ c\\equiv d\\pmod m&\\Longrightarrow&a\\pm c\\equiv b\\pm d\\pmod m\\ 6.&a\\equiv b\\pmod m,\\ c\\equiv d\\pmod m&\\Longrightarrow&ac\\equiv bd\\pmod m\\ \\end{array} $$

### 三、请给出模 *m* 的完全剩余系的概念

若 *a*1, *a*2, …, *a\*\*m* 对模 *m* 两两不同余，则这 *m* 个数构成模 *m* 的一个完全剩余系。

特殊的，任意连续的 *m* 个整数都构成模 *m* 的一个完全剩余系。

### 四、陈述裴蜀定理

对于任意整数 *a*, *b*，一定存在一组整数解 *x*, *y* 使得 *a\*\*x* + *b\*\*y* = (*a*, *b*)。

### 五、陈述费马小定理

若 *p* 是素数，则 *a\*\*p* ≡ *a* (mod  *p*)。

特别的，若 *a* ⟂ *p*，则 *a\*\*p* − 1 ≡ 1 (mod  *p*)。

### 六、给定模 *m* 的一组完全剩余系 *x*1, …, *x\*\*m*，若 *a* ⟂ *m*，请证明 *a\*\*x*1, …, *a**x**m* 也是模 *m* 的一组完全剩余系

**反证**：假设 *a\*\*x*1, …, *a**x**m* 不是模 *m* 的完全剩余系。

则一定存在 *i* ≠ *j* 使得 *a**x**i* ≡ *a**x**j* (mod  *m*)。

因为 *a* ⟂ *m*，因此有 *x\*\*i* ≡ *x\*\*j* (mod  *m*)。

与 *x*1, …, *x\*\*m* 为模 *m* 的完全剩余系不符。

假设不成立，故 *a\*\*x*1, …, *a**x**m* 是模 *m* 的完全剩余系。

### 七、设 *n* 是整数，请证明：120 ∣ *n*(*n*2 − 1)(*n*2 − 5*n* + 26)

**定理**：连续 *n* 个整数的乘积一定被 *n*! 整除。

对于这 *n* 个数都是正整数的：

$$ \\begin{array}{l} (a+1)(a+2)\\dots(a+n)=\\frac{(a+n)!}{a!}=n!\\frac{(a+n)!}{n!a!}=n!\\binom{a+n}{a} \\end{array} $$

而如果这 *n* 个数存在不是正整数的，那么一定跨过了 0，乘积为 0，整除是显然的。

**证明**：

$$ \\def\\arraystretch{1.1} \\begin{array}{ll} &n(n^2-1)(n^2-5n+26)\\ =&n(n+1)(n-1)[(n-2)(n-3)+20]\\ =&(n-3)(n-2)(n-1)n(n+1)+20(n-1)n(n+1) \\end{array} $$

因为：

$$ \\def\\arraystretch{1.1} \\begin{array}{rcl} 120&\\mid& (n-3)(n-2)(n-1)n(n+1)\\ 6&\\mid& (n-1)n(n+1)\\ 120&\\mid& 20(n-1)n(n+1) \\end{array} $$

因此 120 ∣ (*n* − 3)(*n* − 2)(*n* − 1)*n*(*n* + 1) + 20(*n* − 1)*n*(*n* + 1)。

即 120 ∣ *n*(*n*2 − 1)(*n*2 − 5*n* + 26)。

### 八、设 *n* 是正整数，且 2*n* + 1 与 3*n* + 1 都是完全平方数。请证明：40 ∣ *n*

**性质1**：奇数的完全平方数模 8 同余于 1。

(2*k* + 1)2 ≡ 4*k*(*k* + 1) + 1 ≡ 1 (mod  8)

**性质2**：任何一个数的平方模 5 同余于 0, ±1。

$$ \\def\\arraystretch{1.1} \\begin{array}{lcll} t&\\equiv&0,\\pm1,\\pm2&\\pmod5\\ t^2&\\equiv&0,\\pm1&\\pmod5 \\end{array} $$

**证明**：

因为 2*n* + 1 是奇数且是完全平方数，则

$$ \\def\\arraystretch{1.1} \\begin{array}{rcll} 2n+1&\\equiv&1&\\pmod8\\ n&\\equiv&0&\\pmod4 \\end{array} $$

所以，*n* 是偶数，3*n* + 1 是奇数且是完全平方数，则

$$ \\def\\arraystretch{1.1} \\begin{array}{rcll} 3n+1&\\equiv&1&\\pmod8\\ n&\\equiv&0&\\pmod8 \\end{array} $$

且

$$ \\def\\arraystretch{1.1} \\begin{array}{rcll} 2n+1&\\equiv&0,\\pm1&\\pmod5\\ 3n+1&\\equiv&0,\\pm1&\\pmod5 \\end{array} $$

则有

$$ \\def\\arraystretch{1.1} \\begin{array}{rcll} (2n+1)+(3n+1)&\\equiv&2&\\pmod5\\ 2n+1&\\equiv&1&\\pmod5\\ 3n+1&\\equiv&1&\\pmod5\\ n&\\equiv&0&\\pmod5 \\end{array} $$

因此 *n* ≡ 0 (mod  40)，即 40 ∣ *n*。

### 九、求 1010 mod  7

$$ \\def\\arraystretch{1.1} \\begin{array}{ll} &10^{10} \\bmod 7\\ =&(10 \\bmod 7)^{10\\bmod 6}\\bmod 7\\ =&3^4\\bmod7\\ =&81\\bmod7\\ =&4 \\end{array} $$

即 1010 mod  7 = 4。

### 十、求满足以下条件的正整数解：(*a*, *b*) + \[*a*, *b*\] + *a* + *b* = *a\*\*b*

设 *d* = (*a*, *b*)，则记 *a* = *a*0*d*，*b* = *b*0*d*（*a*0 ⟂ *b*0）。

$$ \\def\\arraystretch{1.1} \\begin{array}{rcl} (a,b)+[a,b]+a+b&=&ab\\ d+a_0b_0d+a_0d+b_0d&=&a_0b_0d^2\\ a_0b_0+a_0+b_0+1&=&a_0b_0d \\end{array} $$

因为 *a*0*b*0 ≥ *a*0*b*0, *a*0, *b*0 ≥ 1，所以 0 \< *d* ≤ 4。

当 *d* = 1 时，*a*0 + *b*0 + 1 = 0，无解。

当 *d* = 2 时，

$$ \\def\\arraystretch{1.1} \\begin{array}{rcl} a_0b_0+a_0+b_0+1&=&2a_0b_0\\ a_0b_0-a_0-b_0&=&1\\ a_0(b_0-1)-(b_0-1)&=&2\\ (a_0-1)(b_0-1)&=&2\\ \\end{array} $$

- *a*0 − 1 = 1，*b*0 − 1 = 2；*a*0 = 2，*b*2 = 3；*a* = 4，*b* = 6。
- *a*0 − 1 = 2，*b*0 − 1 = 1；*a*0 = 3，*b*2 = 2；*a* = 6，*b* = 4。

当 *d* = 3 时，

$$ \\def\\arraystretch{1.1} \\begin{array}{rcl} a_0b_0+a_0+b_0+1&=&3a_0b_0\\ 2a_0b_0-a_0-b_0&=&1\\ 4a_0b_0-2a_0-2b_0&=&2\\ 2a_0(2b_0-1)-(2b_0-1)&=&3\\ (2a_0-1)(2b_0-1)&=&3\\ \\end{array} $$

- 2*a*0 − 1 = 1，2*b*0 − 1 = 3；*a*0 = 1，*b*2 = 2；*a* = 3，*b* = 6。
- 2*a*0 − 1 = 3，2*b*0 − 1 = 1；*a*0 = 2，*b*2 = 1；*a* = 6，*b* = 3。

当 *d* = 4 时，

$$ \\def\\arraystretch{1.1} \\begin{array}{rcl} a_0b_0+a_0+b_0+1&=&4a_0b_0\\ 3a_0b_0-a_0-b_0&=&1\\ 9a_0b_0-3a_0-3b_0&=&3\\ 3a_0(3b_0-1)-(3b_0-1)&=&4\\ (3a_0-1)(3b_0-1)&=&4\\ \\end{array} $$

- 3*a*0 − 1 = 2，3*b*0 − 1 = 2；*a*0 = *b*0 = 1；*a* = *b* = 4。
- 2*a*0 − 1 = 1，2*b*0 − 1 = 4；不存在整数解。
- 2*a*0 − 1 = 4，2*b*0 − 1 = 1；不存在整数解。

因此，可行解有：

(*a*, *b*) = (4, 6), (6, 4), (3, 6), (6, 3), (4, 4)

[RainPPR](mailto:PPR2125773894@163.com),  [Bot](mailto:bot@noreply.github.com)
