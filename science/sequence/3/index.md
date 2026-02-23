# 数列进阶

## 回顾及补充

### 经典常量

[ \\pi\\approx3.14159 ]

[ e\\approx2.71828 ]

[ \\gamma\\approx0.57721 ]

[ \\varphi={1+\\sqrt5\\over2}\\approx1.61803 ]

[ \\hat\\varphi={1-\\sqrt5\\over2}\\approx-.61803 ]

### 基础公式

一些公式，

[ \\sum\_{i=1}^ni={n(n+1)\\over2} ]

[ \\sum\_{i=1}^ni^2={n(n+1)(2n+1)\\over6}={n(n+1/2)(n+1)\\over3} ]

\[ \\sum\_{i=1}^ni^3=\\left[{n(n+1)\\over2}\\right]^2={n^2(n+1)^2\\over4} \]

可以通过扰动法（见下）或者待定系数并归纳得出。

[ \\sum\_{i=0}^nc^i={c^{n+1}-1\\over c-1},c\\neq1 ]

[ \\sum\_{i\\ge0}c^i={1\\over 1-c},|c|\<1 ]

[ \\sum\_{i\\ge1}c^i={c\\over 1-c},|c|\<1 ]

上面的是等比数列，下面的用极限得出。

[ \\sum\_{i=0}^nic^i={nc^{n+2}-(n-1)c^{n+1}+c\\over(c-1)^2},c\\neq1 ]

[ \\sum\_{i\\ge0}ic^i={c\\over(1-c)^2},|c|\<1 ]

上面的可以扰动法得出，下面的极限得出。

### 调和级数

[ H_n=\\sum\_{i=1}^n{1\\over i} ]

有，

[ \\ln n\<H_n\<\\ln n+1 ]

[ H_n=\\ln n+\\gamma+\\mathcal O\\left({1\\over n}\\right) ]

同时，

[ \\sum\_{i=1}^nH_i=(n+1)H_n-n ]

[ \\sum\_{i=1}^niH_i={n(n+1)\\over2}H_n-{n(n-1)\\over4} ]

[ \\sum\_{i=1}^n{i\\choose m}H_i={n+1\\choose m+1}\\left(H\_{n+1}-{1\\over m+1}\\right) ]

证明下面再说。

### 欧拉公式

[ \\def\\ff#1{{1\\over#1^2}} {\\pi^2\\over6}=\\ff1+\\ff2+\\ff3+\\ff4+\\ff5+\\dots ]

[ \\def\\ff#1{{1\\over#1^2}} {\\pi^2\\over8}=\\ff1+\\ff3+\\ff5+\\ff7+\\ff9+\\dots ]

### 组合数学

见我的排列组合笔记。

[ \\def\\qq{\\quad} \\begin{array}{c} 1\\ 1\\qq1\\ 1\\qq2\\qq1\\ 1\\qq3\\qq3\\qq1\\ 1\\qq4\\qq6\\qq4\\qq1\\ 1\\qq5\\qq10\\qq10\\qq5\\qq1\\ 1\\qq6\\qq15\\qq20\\qq15\\qq6\\qq1\\ 1\\qq7\\qq21\\qq35\\qq35\\qq21\\qq7\\qq1\\ 1\\qq8\\qq28\\qq56\\qq70\\qq56\\qq28\\qq8\\qq1\\ 1\\qq9\\qq36\\qq84\\qq126\\qq126\\qq84\\qq36\\qq9\\qq1\\ 1\\qq10\\qq45\\qq120\\qq210\\qq252\\qq210\\qq120\\qq45\\qq10\\qq1\\ \\end{array} ]

### 线代基础

[ \\left\\lvert\\begin{matrix}a&b\\c&d\\end{matrix}\\right\\rvert=ad+bc ]

[ \\det A=\\sum\_{\\pi\\in S_n}\\operatorname{sgn}(\\pi)\\prod\_{i=1}^na\_{i,\\pi(i)} ]

[RainPPR](https://github.com/RainPPR)
