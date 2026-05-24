# 均值不等式

## 简单不等式

### 一般不等式

糖水不等式：

a>b>0,m>0\\implies\\dfrac{b+m}{a+m}>\\dfrac{b}{a}

这个的实际意义是，溶质糖的质量分数，加糖会更大。这就要求质量分数必须小于 1。如果大于 1，及 b>a>0，上述不等式反向。

不等式加法：

a>b,c>d\\implies a+c>b+d

不等式减法：

a>b,c\<d\\implies a-c>b-d

不等式联立：

\\begin{cases} a_1\<x+y\<a_2\\ b_1\<x-y\<b_2 \\end{cases}\\implies\\begin{cases} a_1+b_1\<2x\<a_2+b_2\\ a_1-b_1\<2y\<a_2-b_2 \\end{cases}

等式的性质​：

- a=a（自反性）
- ‌a=b\\Rightarrow b=a（对称性）
- a=b,b=c\\Rightarrow a=c（传递性）
- a=b\\Rightarrow a\\pm c=b\\pm c,ac=bc,\\frac{a}{c}=\\frac{b}{c}（c\\neq 0）（替代性）
- 替代性：如果两个对象相等，那么在任何出现它们的位置，都可以用一个替代另一个，等式仍然成立。

不等式的性质​：

- a>b\\Rightarrow b\<a（对称性）
- a>b,b>c\\Rightarrow a>c（传递性）
- a>b\\Rightarrow a\\pm c>b\\pm c
- a>b,c>0\\Rightarrow ac>bc,c\<0\\Rightarrow ac\<bc
- a>b,c>d\\Rightarrow a+c>b+d（加法单调性）
- a>b>0,c>d>0\\Rightarrow ac>bd（乘法单调性）
- a>b>0,n>0\\Rightarrow a^n>b^n,n\<0\\Rightarrow a^n\<b^n

常用技巧​：

- 减法可以转化为加法：a-b=a+(-b)，而除法可以转化为乘法：\\frac{a}{b}=a\\times \\frac{1}{b}。
- 比较两个正数 a,b>0 的常用方法：通过做差比较 a-b 与 0 的关系；通过做商比较 \\frac{a}{b} 与 1 的关系。

根据三角形两边之和大于（如果是退化的三角形可取等）第三边，两边之差小于第三边：

||a|-|b||\\le|a\\pm b|\\le|a|+|b|

这就是三角不等式。注意，用数量积小于等于长度积，是柯西不等式。

重要不等式：

a^2+b^2\\ge2ab

当且仅当 a=b 成立。

例题：证明 a^2+b^2+c^2\\ge ab+bc+ca。

对 ab,bc,ca 列出重要不等式，各式相加即可得到。

高次不等式穿根法：

- 因式分解，做数轴标根。
- 偶数次不穿过数轴，结果抠点。
- 分式不等式分解因式后当做乘法（两边同乘分母的平方），扣去无意义的点。

### 绝对值不等式

如果对于任意 x 都有 |f(x)|\<g(x)，则

-g(x)\<f(x)\<g(x)

对千绝对值不等式，更多的是分类讨论去掉绝对值，结论本身并不重要。

- 函数 f(x)=|x-m|+|x-n|(m\<n) 的图像是以点 A(m, n-m)，B(n, n-m) 为折点的倒梯形；f(x) 在 (-\\infty, m\] 上单调递减，在 \[n, +\\infty) 上单调递增，在 [m,n] 上无单调性，此时 f(x) 恒等于其最小值 n-m；f(x) 在 \\mathbb{R} 上无最大值，其对称轴为 x=\\dfrac{m+n}{2}。
- 当 m > n 时，f(x) = |x-m| - |x-n| 的图像是以点 A(n, m-n)，B(m, n-m) 为折点的“Z 字形”；在 (-\\infty, n\] 上函数恒取得最大值 m-n，在 \[m, +\\infty) 上函数恒取得最小值 n-m；函数在 [n, m] 上递减，其对称中心为 \\left(\\dfrac{m+n}{2}, 0\\right)。
- 当 n > m 时，f(x) = |x-m| - |x-n| 的图像是以点 A(m, m-n)，B(n, n-m) 为折点的“反 Z 字形”；在 (-\\infty, m\] 上函数恒取得最小值 m-n，在 \[n, +\\infty) 上函数恒取得最大值 n-m；函数在 [m, n] 上递增，其对称中心为 \\left(\\dfrac{m+n}{2}, 0\\right)。

a|x-m|+b|x-n|(m\<n) 的图像是以 A(m, f(m))，B(n, f(n)) 为折点的折线。

- 当 a+b>0 时，两端向上无限延伸，故有最小值，最小值为 \\min{f(m), f(n)}；
- 当 a+b\<0 时，两端向下无限延伸，故有最大值，最大值为 \\max{f(m), f(n)}；
- 当 a+b=0 时，两端无限延伸且平行于 x 轴，故既有最大值又有最小值，最大值为 \\max{f(m), f(n)}，最小值为 \\min{f(m), f(n)}。

更复杂的，f(x) = |x-a_1| + |x-a_2| + \\cdots + |x-a_n|（a_i \\in \\mathbb{R}, i, n \\in \\mathbb{N}^\*, 设 a_1 < a_2 < \\cdots < a_n）。

- 若 n=2k-1(k \\in \\mathbb{N}^\*)，则 f(x) 的图像是以 (a_k, f(a_k)) 为顶点的“V 字形”图像。

  - 当且仅当 x=a_k 时，[f(x)]_{\\min} = |(a_1 + a_2 + \\cdots + a_{k-1}) - (a\_{k+1} + a\_{k+2} + \\cdots + a\_{2k-1})|；
  - 函数 f(x) 在 (-\\infty, a_k\] 上单调递减，在 \[a_k, +\\infty) 上单调递增，若 {a_i} 为等差数列，则图像关于 x=a_k 对称。

- 若 n=2k(k \\in \\mathbb{N}^\*)，则 f(x) 的图像是以点 A(a_k, f(a_k)), B(a\_{k+1}, f(a\_{k+1})) 为折点的倒梯形。

  - 当且仅当 x \\in [a_k, a\_{k+1}] 时，[f(x)]_{\\min} = |(a_1+a_2+\\cdots+a_k) - (a_{k+1}+a\_{k+2}+\\cdots+a\_{2k})|；
  - 函数 f(x) 在 (-\\infty, a_k\] 上单调递减，在 \[a\_{k+1}, +\\infty) 上单调递增，在 [a_k, a\_{k+1}] 上无单调性。若 {a_i} 为等差数列，则函数图像关于 x=\\dfrac{a_k+a\_{k+1}}{2} 对称。

### 均值不等式

二元形式，若 a,b>0，则：

\\dfrac{2}{\\dfrac{1}{a}+\\dfrac{1}{b}}\\le\\sqrt[2]{ab}\\le\\dfrac{a+b}{2}\\le\\sqrt[2]{\\dfrac{a^2+b^2}{2}}

理解方式：<https://www.bilibili.com/video/BV1Nf4y1G7xV/>。

多元形式，若 a,b>0，则：

H_n\\le G_n\\le A_n\\le Q_n\\

也就是

\\frac{n}{\\sum\_{i=1}^n{1\\over x_i}}\\le\\sqrt[n]{\\textstyle\\prod\_{i=1}^nx_i}\\le\\frac{\\sum\_{i=1}^nx_i}{n}\\le\\sqrt[2]{\\frac{\\sum\_{i=1}^nx_i^2}{n}}

当且仅当 x_1=x_2=\\dots=x_n 时，等号成立。

即，对于正实数：调和平均数 ≤ 几何平均数 ≤ 算术平均数 ≤ 平方平均数。

简记为：「调几算方」。

我们称两两为 X-Y 均值不等式，例如算数-几何均值不等式：

\\sqrt[n]{x_2x_2\\dots x_n}\\le\\dfrac1n(x_1+x_2+\\dots+x_n)

可以进行推广，得到加权平均不等式：

x_1^{\\lambda_1}x_2^{\\lambda_2}\\dots x_n^{\\lambda_n}\\le\\lambda_1x_1+\\lambda_2x_2+\\dots+\\lambda_nx_n

其中 x_1,x_2,\\dots,x_n>0，\\lambda_1,\\lambda_2,\\dots,\\lambda_n>0 且 \\lambda_1+\\lambda_2+\\dots+\\lambda_n=1。

我们考虑证明一下 A_n\\ge G_n，即：

\\dfrac{a_1+a_2+\\dots a_n}{n}\\ge\\sqrt[n]{a_1a_2\\dots a_n}

考虑构造

\\exp\\paren{\\dfrac{nA_n}{G_n}-n}=\\exp\\paren{\\dfrac{a_1+a_2+\\dots+a_n}{G_n}-n}

注意到右边的指数可以拆解成 n 个

=\\exp\\paren{\\dfrac{a_1}{G_n}-1}\\exp\\paren{\\dfrac{a_2}{G_n}-1}\\dots\\exp\\paren{\\dfrac{a_n}{G_n}-1}

应用 \\exp x=e^x\\ge x+1 经典放缩，我们可以得到：

\\ge\\dfrac{a_1}{G_n}\\cdot\\dfrac{a_2}{G_n}\\dots\\dfrac{a_n}{G_n}=1

于是 A_n\\ge G_n 就证明了。

这个命题，还可以用反向数学归纳法证明，核心思想例如

a+b+c+d\\ge2\\sqrt{ab}+2\\sqrt{cd}\\ge2\\sqrt{2\\sqrt{ab}\\cdot2\\sqrt{cd}}=4\\sqrt[4]{abcd}

于是我们可以直接推导 2^k 的不等式，然后考虑反向归纳，比较复杂，且与前面相比较为复杂，不再展开。

关于 ab（a,b\\in\\R）：

ab\\le\\dfrac14(a+b)^2\\le\\dfrac12(a^2+b^2)

关于 a^2+b^2（a,b\\in\\R）：

a^2+b^2\\ge\\dfrac12(a+b)^2\\ge2ab

关于 a+b（a,b,\\in\\R\_+）：

2\\sqrt{ab}\\le a+b\\le\\sqrt{2(a^2+b^2)}

关于 \\sqrt a+\\sqrt b（a,b,\\in\\R\_+）：

\\sqrt{a}+\\sqrt b\\le\\sqrt{2(a+b)}

关于 \\sqrt{ab}（a,b,\\in\\R\_+）：

\\dfrac{2ab}{a+b}\\le\\sqrt{ab}\\le\\dfrac14(\\sqrt a+\\sqrt b)^2\\le\\dfrac12(a+b)\\le\\sqrt{\\dfrac12(a^2+b^2)}

关于 \\dfrac{1}{a}+\\dfrac{1}{b}（a,b,\\in\\R\_+）：

\\dfrac{1}{a}+\\dfrac{1}{b}\\ge\\dfrac2{\\sqrt{ab}}\\ge\\dfrac4{a+b}

关于 \\dfrac1{\\sqrt{a}}+\\dfrac1{\\sqrt{b}}（a,b,\\in\\R\_+）：

\\dfrac{1}{\\sqrt a}+\\dfrac{1}{\\sqrt b}\\ge\\dfrac4{\\sqrt a+\\sqrt b}\\ge\\dfrac8{a+b}

积定和最小，和定积最小。

以上所有，都建议熟练掌握，考试时建议先写出来 a+b\\ge2\\sqrt{ab}，把 2 除过去，然后根据调几算方的口诀，写出不等式链，然后分别代入平方和根号，即可得到上面大部分不等式了。

若缩放所得上下界有未知数，则缩放失效。

### 与均值有关的定积分函数

高中老师可能讲过，均值不等式的本质是

f(x)=\\sqrt[x]{\\dfrac{a^x+b^x}{2}}

在 \\R 上单调递增（其中 0 可去间断）。

我们这里参考 [与均值有关的定积分函数 - lailai](https://lailai.one/zh-Hans/blog/math/average-integral) 一些与均值有关的定积分函数。

设：

f(t)=\\frac{\\int_a^b x^{t+1}\\mathrm{d}x}{\\int_a^b x^t\\mathrm{d}x}

当 t\\ne -1\\land t\\ne -2 时，可化简为：

f(t)=\\frac{(t+1)(b^{t+2}-a^{t+2})}{(t+2)(b^{t+1}-a^{t+1})}

显然，函数 f(t) 单调不减。

该函数可以并推广均值不等式。

0\<a\\le b

a\\le H(a,b)\\le G(a,b)\\le L(a,b)\\le N(a,b)\\le A(a,b)\\le T(a,b)\\le b

调和平均数：

H(a,b)=f(-3)=\\frac{-2(b^{-1}-a^{-1})}{-1(b^{-2}-a^{-2})}=\\frac{2ab}{a+b}=\\frac{1}{\\frac{1}{a}+\\frac{1}{b}}

几何平均数：

G(a,b)=f(-1.5)=\\frac{-0.5(b^{0.5}-a^{0.5})}{0.5(b^{-0.5}-a^{-0.5})}=\\sqrt{ab}

对数平均数：

L(a,b)=f(-1)=\\frac{\\int_a^b x^0\\mathrm{d}x}{\\int_a^b x^{-1}\\mathrm{d}x}=\\frac{b-a}{\\ln b-\\ln a}

海伦平均数：

N(a,b)=f(-0.5)=\\frac{0.5(b^{1.5}-a^{1.5})}{1.5(b^{0.5}-a^{0.5})}=\\frac{a+\\sqrt{ab}+b}{3}

算术平均数：

A(a,b)=f(0)=\\frac{1(b^2-a^2)}{2(b^1-a^1)}=\\frac{a+b}{2}

质心平均数：

T(a,b)=f(1)=\\frac{2(b^3-a^3)}{3(b^2-a^2)}=\\frac{2(a^2+ab+b^2)}{3(a+b)}

## 做题方法

### 对勾函数

对于定义在 \\R-{0} 的函数

f(x)=ax+\\dfrac{b}{x}

设 x_0 满足

ax_0=\\dfrac{b}{x_0}

即

x_0^2=\\dfrac{b}{a}

不妨取正的一个解（同时 f(x)=f(y) 当且仅当 xy=\\dfrac{b}{a}）。

容易知道，f(x) 在 (0,x_0\] 单调递减，在 \[x_0,+\\infty) 单调递增。

在负半轴类似，同时因为在正半轴

f(x)=ax+\\dfrac{b}{x}\\ge2\\sqrt{ab}

也就是说 f(x) 的值域是 (-\\infty,-2\\sqrt{ab})\\cup(2\\sqrt{ab},+\\infty)。

### 基本规则

基本不等式的求最值一定要满足“一正、二定、三相等”，即先判定正负性，然后判断放缩后是否为定值，最后验证取等条件。

如果不是定值，通常会导致最值不在缩放的点上，我们可以复杂，对于缩放问题，就不需要是定值了。

例题：若实数 a,b 满足 \\dfrac{1}{a}+\\dfrac{2}{b}=\\sqrt{ab}，则 ab 的最小值为

我们知道

\\sqrt{ab}=\\dfrac{1}{a}+\\dfrac{2}{b}\\ge2\\sqrt{\\dfrac{2}{ab}}

因此

ab\\ge2\\sqrt2

当且仅当 b=2a 时取等。

利用基本不等式求函数 f(x) 的最大值通常有三种途径：

1. 直接利用均值不等式放缩成 f(x) \\le k，其中 k 为常数，最后检查等号能否成立；
1. 直接利用均值不等式放缩成 f(x) \\le g(x)，然后通过解不等式获得 f(x) 的范围，最后检查等号能否成立。
1. 多次利用均值不等式放缩成 f(x) \\le g(x) \\le k，其中 k 为常数，最后检查所有等号成立的条件是否一致。

自由变量公式：

- 自由变量的个数等千变堂的个数减去方程的个数。
- 使用基本不等式的次数等于自由变霆的个数。

凑系数、换元法是最基础的方法，除此之外，我们还有妙用：

- 若已知 ax+by 为定值，求它们的倒数和 \\dfrac{c}{x} + \\dfrac{d}{y} 的最小值，既可以用消元的方法，也可以利用“1”的代换，但是我们推荐使用“1”的代换；
- 若已知 \\dfrac{c}{x} + \\dfrac{d}{y} 为定值，求和 ax+by 的最小值，既可以用消元的方法，也可以利用“1”的代换，但是我们推荐使用“1”的代换；
- 若已知 axy+bx+cy+d=0，求和 ex+fy 的最小值，如果分解因式很显然，使用“1”的代换；否则，使用消元法。

具体的，例如已知 ax+by=C，则

\\begin{aligned} \\dfrac{c}{x}+\\dfrac{d}{y}&=\\dfrac{1}{C}(ax+by)\\paren{\\dfrac{c}{x}+\\dfrac{d}{y}}\\ &=\\dfrac{1}{C}\\left(ac+bd+ad\\dfrac{x}{y}+bc\\dfrac{y}{x}\\right)\\ &\\ge\\dfrac{1}{C}\\left(ac+bd+2\\sqrt{ad\\cdot bc}\\right)\\ &=\\dfrac{1}{C}\\left(\\sqrt{ac}+\\sqrt{bd}\\right)^2\\ \\end{aligned}

当 x,y>0 时，等号当且仅当 ad\\dfrac{x}{y}=bc\\dfrac{y}{x} 即 \\dfrac{x}{y}=\\sqrt{\\dfrac{bc}{ad}}。

最常见的方法是分母不变，其他拼凑

x+\\dfrac{3}{x-2}=x-2+\\dfrac{3}{x-2}+2\\ge\\dots

x+\\dfrac{3}{2x-3}=x-\\dfrac{3}{2}+\\dfrac{2}{2x-3}+\\dfrac{3}{2}\\ge\\dots

如果分子的次数比分母高，通常把上面的先分下来，称为分离常数。

对于积的不等式，通常用调整常数

x(1-3x)=3x(1-3x)\\cdot\\dfrac13

形如 ab=a+b 的，通常转化为

1=\\dfrac{1}{a}+\\dfrac{1}{b}

### 加权待定

我们知道了 f(x)=\\ln x 与 g(x)=\\dfrac{2(x-1)}{x+1} 和 h(x)=\\dfrac{1}{2}\\left(x-\\dfrac{1}{x}\\right) 的关系，那么不妨讨论 f(x) 与

\\varphi(x)=\\lambda g(x)+(1-\\lambda)h(x)

的关系，对 y=\\ln x-\\varphi(x) 求导即可，此处略。

我们知道高中常见的均值不等式链：

\\dfrac{2ab}{a+b}\<\\sqrt{ab}\<\\dfrac{a-b}{\\ln a-\\ln b}\<\\dfrac{a+b}{2}\<\\sqrt{\\dfrac{a^2+b^2}{2}}\<\\dfrac{a^2+b^2}{a+b}

此处不写等号因为对数平均数部分没有办法取等。

另外还有

\\dfrac{2}{3}\\cdot\\dfrac{a^2+b^2}{a+b}+\\dfrac{1}{3}\\cdot\\dfrac{2ab}{a+b}

\\dfrac{2}{3}\\cdot\\dfrac{a+b}{2}+\\dfrac{1}{3}\\cdot\\sqrt{ab}

\\dfrac{1}{3}\\cdot\\dfrac{a+b}{2}+\\dfrac{2}{3}\\cdot\\sqrt{ab}

等形式，都可以用加权待定来理解。

- 在 x\\in(1,+\\infty)，

  \\small\\frac{x-1}{x}\<\\frac{2(x-1)}{x+1}\<\\frac{3(x^2-1)}{x^2+4x+1}\<\\ln x\<\\sqrt{x}-\\frac{1}{\\sqrt{x}}\<\\frac{1}{2}\\left(x-\\frac{1}{x}\\right)\<x-1

- 在 x\\in(0,1)，

  \\small\\frac{x-1}{x}\<\\frac{1}{2}\\left(x-\\frac{1}{x}\\right)\<\\sqrt{x}-\\frac{1}{\\sqrt{x}}\<\\ln x\<\\frac{3(x^2-1)}{x^2+4x+1}\<\\frac{2(x-1)}{x+1}\<x-1

### 简单例题

例题

若 x_i > 0，且 \\sum\_{i=1}^{n} x_i = 1，则

\\left(x_1 + \\dfrac{1}{x_1}\\right)\\left(x_2 + \\dfrac{1}{x_2}\\right)\\cdots\\left(x_n + \\dfrac{1}{x_n}\\right) \\ge \\left(n + \\dfrac{1}{n}\\right)^n

当且仅当 x_i = \\dfrac{1}{n} 时等号成立；

如果 \\sum\_{i=1}^{n} x_i \\ne 1，则上述结论不成立，为了简化，我们只给出两个变量的情形：

已知 a > 0，b > 0，且 a+b=k，则 \\left(a+\\dfrac{1}{a}\\right)\\left(b+\\dfrac{1}{b}\\right) 的最小值为

\\begin{cases} \\left(\\dfrac{k}{2} + \\dfrac{2}{k}\\right)^2, & 0 < k \\le 2\\sqrt{2+\\sqrt{5}} \\ 2\\sqrt{1+k^2}-2, & k > 2\\sqrt{2+\\sqrt{5}} \\end{cases}

例题

已知 a,b>0 且 ab=a+b+3，则 ab,a+b 的最小值分别为？

方法一：由 ab=a+b+3，得到 a=\\dfrac{b+3}{b-1}，带入消元即可。

方法二：ab=a+b+3\\ge2\\sqrt{ab}+3，解得 \\sqrt{ab}\\ge3 即 ab\\ge9。

方法三：由 ab-a-b+1=4 得 4=(a-1)(b-1)\\le\\dfrac14(a+b-2)^2，则 a+b\\ge6。

例题

已知 x,y>0 且 x+3y=5xy，则 3x+4y 的最小值为？

方法一：我们知道 y=\\dfrac{x}{5x-3}，带入消元即可。

方法二：由 5xy-x-3y+\\dfrac{3}{5}=\\dfrac{3}{5}，得到 (5x-3)(5y-1)=3，因此

\\dfrac{144}{25}=\\paren{3x-\\dfrac{9}{5}}\\paren{4x-\\dfrac{4}{5}}\\le\\paren{3x+4y-\\dfrac{13}{5}}^2

方法三：我们知道 \\dfrac{1}{y}+\\dfrac3x=5，因此

\\begin{aligned} 3x+4y&=\\dfrac15(3x+4y)\\paren{\\dfrac3x+\\dfrac1y}\\ &=\\dfrac15\\paren{13+12\\dfrac yx+3\\dfrac xy}\\ge5 \\end{aligned}

例题

已知 a,b>0 且 2a+b=1，则 \\dfrac1a+\\dfrac ab 的最小值为？

\\dfrac1a+\\dfrac ab=\\dfrac{2a+b}a+\\dfrac{a}{b}=2+\\dfrac ab+\\dfrac ba\\ge4

例题

已知 0\<x\<1，则 \\dfrac9x+\\dfrac{16}{1-x} 的最小值为？

\\begin{aligned} \\dfrac9x+\\dfrac{16}{1-x}&=\\paren{\\dfrac9x+\\dfrac{16}{1-x}}[(x)+(1-x)]\\ &=25+9\\dfrac{1-x}x+16\\dfrac x{1-x}\\ge49 \\end{aligned}

例题

已知 a,b>0 且 (a+3b)(2a+b)=6，则 8a+9b 的最小值为？

注意到形式较为复杂，不妨设 \\lambda,\\mu 化简

\\lambda(a+3b)\\cdot\\mu(2a+b)=6\\lambda\\mu

且使得

\\begin{cases} \\lambda+2\\mu&=8\\ 3\\lambda+\\mu&=9 \\end{cases}

解得 \\lambda=2,\\mu=3，因此

36=(2a+6b)(6a+3b)\\le\\dfrac14(8a+9b)^2

### 拼凑构造

拼凑构造，虽然有些题是对脑电波，或者暴力待定系数，但是在中档题里面是有一定规律的，例如将代数式中一项或几项拆开，齐次化构造，分离常数，并项（通分），或者配凑系数，甚至是配凑某些项。

例题一

已知 a,b>0，求 \\dfrac{a^2+4}{2a}+\\dfrac{2b^2+b+2}{2b+1} 的最小值。

第一反应应该是将前面的除下去，然后将后面的 2b+1 视为一个整体，分离常数，这是显然的，设原式为 S，则 S=\\dfrac{a}{2}+\\dfrac{2}{a}+\\dfrac{2b+1}{2}+\\dfrac{2}{2b+1}-\\dfrac{1}{2}\\ge\\dfrac{7}{2}。

验证取等条件是必不可少的，容易发现 a=2b+1=2 是显然可以取到的。

例题二

已知 a,b>0 且 ab=1，求 \\dfrac{1}{2a}+\\dfrac{1}{2b}+\\dfrac{8}{a+b} 的最小值。

容易发现，第三项 a+b 在分母上，不好化简，考虑可以将前面的也化为和 a+b 有关的式子，容易发现直接通分，代入 ab=1 即可。

具体步骤很简单，我们关注这道题告诉我们 ab=1 这种限制条件给我们带来了什么。第一就是在计算中用已知量去简化式子、化简运算，比如 ab^+a^2b=ab(a+b)=ab。第二就是最后取等条件的验证过程中，作为一种限制。

不妨用自由度的角度分析，我们发现，两个变量（这里是 a,b 比如），两次放缩，两个取等要求，是可以接受的。但是当多了一个初始限制的时候，往往用一次放缩（除非取等条件比较松）。

还有一类经典的配凑系数，比如把 ab 写成 \\dfrac{1}{4}\\cdot a\\cdot 4b，然后将 a,4b 用基本不等式，这个的意义在于，乘法可以把单个系数提出来，但是加法不能，放缩时，可以用这种技巧把系数放进加法中。与此相对应的，还可以配凑加减，这都是很常见的，比如 a+b=(a+1)+b-1，可以把加减偏移量放进乘法中，很好用。

还有比如我们初中物理就接触过的，把分子的 x 除下去，在分母上用不等式放缩。

我们上面提到的就是所谓拼凑的技巧，还是相当常用的。我们在此与 1 的代换做一个联系。我们在前面，包括做题过程中，发现一些次数上的特征，比如 x 和 \\dfrac{1}{x} 一起出现，往往会把后者乘到前者，然后构造齐次化，进行一次放缩。

例如若正数 x,y 满足 x+y=4，求 \\dfrac{x^2}{x+1}+\\dfrac{y^2}{y+2} 的最值。就可以写作 (x+1)+(y+2)=7，乘过去，然后放缩即可。

再次强调，取等条件的重要性。直接使用不等式必须判断取等，如果取不了等，可以考虑用对钩函数的性质（大题可以直接求导）。

[RainPPR](mailto:PPR2125773894@163.com),  [Bot](mailto:bot@noreply.github.com)
