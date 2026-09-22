# 高中常见不等式概念及理解

## 不等式入门

### 不等式的引入

不等式加法：

a>b,c>d\\implies a+c>b+d

不等式减法：

a>b,c\<d\\implies a-c>b-d

不等式联立：

\\begin{cases} a_1\<x+y\<a_2\\ b_1\<x-y\<b_2 \\end{cases}\\implies\\begin{cases} a_1+b_1\<2x\<a_2+b_2\\ a_1-b_1\<2y\<a_2-b_2 \\end{cases}

等式的性质：

- a=a（自反性）
- a=b\\Rightarrow b=a（对称性）
- a=b,b=c\\Rightarrow a=c（传递性）
- a=b\\Rightarrow a\\pm c=b\\pm c,ac=bc,\\frac{a}{c}=\\frac{b}{c}（c\\neq 0）（替代性）
- 替代性：如果两个对象相等，那么在任何出现它们的位置，都可以用一个替代另一个，等式仍然成立。

不等式的性质：

- a>b\\Rightarrow b\<a（对称性）
- a>b,b>c\\Rightarrow a>c（传递性）
- a>b\\Rightarrow a\\pm c>b\\pm c
- a>b,c>0\\Rightarrow ac>bc,c\<0\\Rightarrow ac\<bc
- a>b,c>d\\Rightarrow a+c>b+d（加法单调性）
- a>b>0,c>d>0\\Rightarrow ac>bd（乘法单调性）
- a>b>0,n>0\\Rightarrow a^n>b^n,n\<0\\Rightarrow a^n\<b^n

常用技巧：

- 减法可以转化为加法：a-b=a+(-b)，而除法可以转化为乘法：\\frac{a}{b}=a\\times \\frac{1}{b}。
- 比较两个正数 a,b>0 的常用方法：通过做差比较 a-b 与 0 的关系；通过做商比较 \\frac{a}{b} 与 1 的关系。

**糖水不等式**：

a>b>0,m>0\\implies\\dfrac{b+m}{a+m}>\\dfrac{b}{a}

**伯努利不等式**：若 x_1,x_2\\dots,x_n\\ge-1 且 x_2,x_2,\\dots,x_n 同号，则

(1+x_1)(1+x_2)\\dots(1+x_n)\\ge1+x_1+x_2+\\dots+x_n

这个的实际意义是，溶质糖的质量分数，加糖会更大。这就要求质量分数必须小于 1。如果大于 1，及 b>a>0，上述不等式反向。

**三角不等式**：根据三角形两边之和大于（如果是退化的三角形可取等）第三边，两边之差小于第三边

||a|-|b||\\le|a\\pm b|\\le|a|+|b|

用数量积小于等于长度积，是**柯西不等式**。

**重要不等式**：

a^2+b^2\\ge2ab

当且仅当 a=b 成立。

例题：证明 a^2+b^2+c^2\\ge ab+bc+ca。

对 ab,bc,ca 列出重要不等式，各式相加即可得到。

**高次不等式**穿根法：

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

一些证明的碎碎念

我们考虑证明一下 A_n\\ge G_n，即：

\\dfrac{a_1+a_2+\\dots a_n}{n}\\ge\\sqrt[n]{a_1a_2\\dots a_n}

考虑构造

\\exp\\left(\\dfrac{nA_n}{G_n}-n\\right)=\\exp\\left(\\dfrac{a_1+a_2+\\dots+a_n}{G_n}-\\right)

注意到右边的指数可以拆解成 n 个

=\\exp\\left(\\dfrac{a_1}{G_n}-1\\right)\\exp\\left(\\dfrac{a_2}{G_n}-1\\right)\\dots\\exp\\left(\\dfrac{a_n}{G_n}-1\\right)

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

## 不等式进阶

我们将讲解以向量为背景的不等式，这一部分的不等式需要建立一种思维，在二维（以及三位空间中），我们有欧式几何，从中可以推导出很多形式，将其代数化，这是有理有据的，比如向量经典三角不等式

|\\bm u+\\bm v|\\le|\\bm u|+|\\bm v|

在二维空间中，我们完全可以用欧式几何来证明，三维空间同理，但是在高维空间中，我们需要用闵可夫斯基不等式来证明，因此这就是为什么闵可夫斯基不等式不能用上式来证明。

又如柯西不等式本身说的是

|\\bm u\\cdot\\bm v|\\le|\\bm u|\\cdot|\\bm v|

其本身定义了高维空间下的向量夹角余弦值，而在二、三维空间中，我们可以用欧式几何来定义夹角余弦值，同样在高维空间中，我们不能用上式来证明柯西不等式。

我们可以做一个没有道理的推导，在二、三维空间中的以上结论，可以辅助我们理解和记忆，但是不能直接用来证明高维下的不等式，但是用向量来记忆和理解，确实非常有效的，因为其反应了我们对世界的基本数学认知。

### 柯西-施瓦茨不等式

柯西不等式表明，对于实数 a_1,a_2,b_1,b_2：

(a_1^2+a_2^2)(b_1^2+b_2^2)\\ge(a_1b_1+a_2b_2)^2

在柯西不等式中，因为有平方，所以开方要小心绝对值、正负号等问题，比如上式右侧 a_1b_1,a_2b_2，系数均可以写作 \\pm 1，但左侧必须是加而不能是减。

**【经典例题】**：填出所有使不等式成立的答案。

1. (a_1^{\_\_}+a_2^{\_\_}(b_1^2+b_2^2)\\ge(a_1^3b_1+a_2^3b_2)

   答案：6；6。

1. (a_1^2+a_2^2)(b_1^2+b_2^2)\\ge(\_\_ a_1b_1+a_2b_2)^2

   答案：\\pm 1（1 或 -1）。

1. (x^2+y^2)(9+\_\_)\\ge(3x-2y)^2

   答案：4。

任何不等式的使用必须验证取等条件，上不等式取等条件为

a_1b_2=a_2b_1

**【经典例题】**：写出不等式的取等条件，并判断在相应条件下，是否可以取等。

1. 5(a^2 + b^2) \\ge (2a + b)^2
1. 已知 a + b = 1，5(a^2 + b^2) \\ge (2a + b)^2
1. 5(a^2 + b^2) \\ge (2a - b)^2
1. 已知 a + b = 1，5(a^2 + b^2) \\ge (2a - b)^2
1. 14(a^2 + b^2 + c^2) \\ge (a + 2b + 3c)^2
1. 已知 a + b + c = 1，14(a^2 + b^2 + c^2) \\ge (a + 2b + 3c)^2
1. 已知 a + b + c = 1，a = 2c，14(a^2 + b^2 + c^2) \\ge (a + 2b + 3c)^2

证明方法一：直接展开

要证明这个简单的不等式，最方便的做法就是直接展开：

a_1^2b_1^2+a_2^2b_2^2+a_1^2b_2^2+a_2^2b_1^2\\ge a_1^2b_1^2+a_2^2b_2^2+2a_1b_1a_2b_2

约去相同的项，得到

a_1^2b_2^2+a_2^2b_1^2\\ge 2a_1b_1a_2b_2

可以配方，也可以根据均值不等式，

a_1^2b_2^2+a_2^2b_1^2\\ge2\\sqrt{a_1^2a_2^2b_1^2b_2^2}\\ge2a_1a_2b_1b_2

取等条件：

{a_1\\over b_1}={a_2\\over b_2}

证明方法二：换元法

还可以换元，不妨设

A=\\sqrt{a_1^2+a_2^2},B=\\sqrt{b_1^2+b_2^2}

则不等式可以表示为

\\dfrac{(a_1b_1+a_2b_2)}{AB}\\le1

不妨拆开，也就是

\\dfrac{a_1b_1}{AB}+\\dfrac{a_2b_2}{AB}\\le\\dfrac{1}{2}\\left(\\dfrac{a_1^2}{A^2}+\\dfrac{b_1^2}{B^2}+\\dfrac{a_2^2}{A^2}+\\dfrac{b_2^2}{B^2}\\right)=1

对于一般的实数序列 a,b：

\\sum\_{i=1}^na_i^2\\sum\_{i=1}^nb_i^2\\ge\\left(\\sum\_{i=1}^na_ib_i\\right)^2

证明可以展开，用拉格朗日恒等式，但是较为复杂，取等条件为：

{a_1\\over b_1}={a_2\\over b_2}=\\dots={a_n\\over b_n}

若某个 b 为零，这个式子失效，但是仍然可以用任两 a,b 相乘相等来验证。

证明方法三：判别式法

可以用判别式证明，不妨令

A=\\sum\_{i=1}^na_i^2,B=\\sum\_{i=1}^na_ib_i,C=\\sum\_{i=1}^nb_i^2,

要证即 AC\\ge B^2，不妨构造方程，注意到可以将 \\sum 合并，配方为

f(x)=Ax^2+2Bx+C=\\sum\_{i=1}^n(a_ix+b_i)^2\\ge0

因为二次函数恒非负，且二次项系数 A 非负，则一定有判别式非正：

\\dfrac{\\Delta}{4}=B^2-AC\\le 0\\implies AC\\ge B^2

取等可以是存在 x 使得 a_ix+b_i 均为零。

柯西不等式有两个常见的变形，这两个变形无须记忆，重点应该记忆柯西不等式的标准形式

1. 平方和形式：设 a_1, a_2, \\dots, a_n 为任意实数，则

   \\left(\\sum\_{i=1}^n a_i\\right)^2 \\leqslant n \\sum\_{i=1}^n a_i^2,

   等号当且仅当 a_1 = a_2 = \\dots = a_n 时成立。

   在柯西不等式中取 b_i = 1（i = 1, 2, \\dots, n），即得 \\left(\\sum\_{i=1}^n a_i\\right)^2 \\leqslant \\left(\\sum\_{i=1}^n a_i^2\\right) \\cdot n。等号条件为 a_i 与常数 1 成比例，即 a_i 全部相等。

1. 倒数和形式：设 a_1, a_2, \\dots, a_n 为正实数，则

   \\left(\\sum\_{i=1}^n a_i\\right) \\left(\\sum\_{i=1}^n \\frac{1}{a_i}\\right) \\geqslant n^2,

   等号当且仅当 a_1 = a_2 = \\dots = a_n 时成立。

   在柯西不等式中取 b_i = 1/\\sqrt{a_i}，则 a_i b_i = \\sqrt{a_i} \\cdot 1/\\sqrt{a_i} = 1，故 \\left(\\sum\_{i=1}^n 1\\right)^2 = n^2 \\leqslant \\left(\\sum\_{i=1}^n a_i\\right) \\left(\\sum\_{i=1}^n \\frac{1}{a_i}\\right)。等号条件为 \\sqrt{a_i} 与 1/\\sqrt{a_i} 成比例，即 a_i 全部相等。

更常见的推论是分数和形式，我们在下面单独讲解。

证明方法四：物理法

光滑桌子（\\mu=0）上面放着若干个质量不一的薄板，其中间的摩擦因数不为零（\\mu\\neq0）。

设其质量分别为 m_1,m_2,\\dots,m_n，给他们一个互异的初速度 v_1,v_2,\\dots,v_n。

根据能量守恒定律，经过有限的时间后，它们必定会趋于同一个速度，设为 v_f。

那么，根据动量守恒定律和功能关系：

\\begin{aligned} m_1v_1+m_2v_2+\\dots+m_nv_n&=m_1v_f+m_2v_f+\\dots+m_nv_f\\ {1\\over2}m_1v_1^2+{1\\over2}m_2v_2^2+\\dots+{1\\over2}m_nv_n^2&\\ge {1\\over2}m_1v_f^2+{1\\over2}m_2v_f^2+\\dots+{1\\over2}m_nv_f^2 \\end{aligned}

化简、移项，得到：

\\begin{aligned} v_f={\\sum m_iv_i\\over\\sum m_i}\\ \\sum(m_iv_i^2)\\ge(\\sum m_i)v_f^2 \\end{aligned}

上式带入下式，得：

\\sum(m_iv_i^2)\\ge{(\\sum m_iv_i)^2\\over\\sum m_i}

再移项，得：

\\sum(m_iv_i^2)\\sum m_i\\ge(\\sum m_iv_i)^2

我们取 m\\to a^2，v\\to b/a，即：

\\sum{a_i^2}\\sum{b_i^2}\\ge(\\sum{a_ib_i})^2

取等条件为 v_i=v_g，即初始就共速，则：

{b_1\\over a_1}={b_2\\over a_2}=\\dots={b_n\\over a_n}

即柯西不等式（当然这个结论比柯西不等式弱一些）。

在 n 维空间中，夹角余弦值的定义就是内积

\\cos\\theta=\\dfrac{\\bm a\\cdot \\bm b}{|\\bm a|\\cdot|\\bm b|}

而要证明夹角余弦值的绝对值 \\le 1，即证明

|\\bm a\\cdot\\bm b|\\le|\\bm a|\\cdot|\\bm b|

不妨设两向量为

\\bm a=(a_1,a_2,\\dots,a_n),\\bm b=(b_1,b_2,\\dots,b_n)

展开即为柯西不等式，因此夹角余弦值可以用来记忆和理解柯西不等式，但是不能用来证明柯西不等式，因为 |\\cos\\theta|\\le1 本身就是柯西不等式的一种形式。需要注意的是，在二维、三维中，从几何余弦定理可以推出柯西不等式，因为几何角度独立；但 n 维的“夹角”通常没有独立几何定义，是内积诱导的。即使可以嵌入二维平面，也需先建立内积与长度，可能仍依赖柯西不等式。

从向量的角度证明柯西不等式与判别式法类似，对任意实数 t，有

|\\bm a+t\\bm b|=|\\bm a|^2+2t(\\bm a\\cdot\\bm b)+t^2|\\bm b|^2\\ge 0

因此判别式 \\Delta\\le 0，即柯西不等式的向量形式。

### 柯西不等式的分式形式

柯西不等式的分式形式，也称为分数和形式、Engel 形式（虽然中文不常用，但是也可以叫作安多形式）、Titu 引理（或谐音为 T2 引理），更一般化的时候称为权方和不等式，因为权方和不等式的形式很复杂，且用起来也不方便，因此一般只用 Engel 形式。

最简单的二元形式可以写作

\\dfrac{a_1^2}{b_1}+\\dfrac{a_2^2}{b_2}\\ge\\dfrac{(a_1+a_2)^2}{b_1+b_2}

更一般的形式可以写作

\\dfrac{a_1^2}{b_1}+\\dfrac{a_2^2}{b_2}+\\dots+\\dfrac{a_n^2}{b_n}\\ge\\dfrac{(a_1+a_2+\\dots+a_n)^2}{b_1+b_2+\\dots+b_n}

等号成立当且仅当

\\dfrac{a_1}{b_1}=\\dfrac{a_2}{b_2}=\\dots=\\dfrac{a_n}{b_n}

证明由柯西不等式形式

(a_1^2+a_2^2+\\dots+a_n^2)(b_1^2+b_2^2+\\dots+b_n^2)\\ge(a_1b_1+a_2b_2+\\dots+a_nb_n)

令 a_i=\\dfrac{x_i}{\\sqrt{y_i}},b_i=\\sqrt{y_i}，那么

\\left(\\dfrac{x_1^2}{y_1}+\\dfrac{x_2^2}{y_2}+\\dots+\\dfrac{x_n^2}{y_n}\\right)(y_1+y_2+\\dots+y_n)\\ge(x_1+x_2+\\dots+x_n)

除过去即为 Engel 形式。

权方和不等式

设 a_1,a_2,\\dots,a_n>0，b_1,b_2,\\dots,b_n>0，r\\in\\mathbb{R}，则

- 当 r\\ge0，或 r\\le-1 时，有

  \\frac{a_1^{r+1}}{b_1^{r}}+\\frac{a_2^{r+1}}{b_2^{r}}+\\dots+\\frac{a_n^{r+1}}{b_n^{r}}\\ge\\frac{(a_1+a_2+\\dots+a_n)^{r+1}}{(b_1+b_2+\\dots+b_n)^{r}}。

- 当 -1\<r\<0 时，有

  \\frac{a_1^{r+1}}{b_1^{r}}+\\frac{a_2^{r+1}}{b_2^{r}}+\\dots+\\frac{a_n^{r+1}}{b_n^{r}}\\le\\frac{(a_1+a_2+\\dots+a_n)^{r+1}}{(b_1+b_2+\\dots+b_n)^{r}}。

示例：已知实数 x,y>0 满足 \\frac{1}{x}+\\frac{4}{y}=1，求 x+y 的最小值。根据权方和不等式：

1=\\frac{1^2}{x}+\\frac{2^2}{y}=\\frac{a^2}{x}+\\frac{b^2}{y}\\ge\\frac{(a+b)^2}{x+y}=\\frac{(1+2)^2}{x+y}=\\frac{9}{x+y}

即：

1\\ge\\frac{9}{x+y}\\Rightarrow x+y\\ge 9

所以 x+y 的最小值为 9。

### 闵可夫斯基不等式

闵科夫斯基不等式（或闵可夫斯基不等式，作者的输入法抽风，本文可能混用，感谢您的理解）表明，对于任意实数 a_1,a_1,b_1,b_2 有

\\sqrt{a_1^2+a_2^2}+\\sqrt{b_1^2+b_2^2}\\ge\\sqrt{(a_1+b_1)^2+(a_2+b_2)^2}

如果我们令 \\bm u=(a_1,a_2),\\bm v=(b_1,b_2)，这个式子说的就是

|\\bm u|+|\\bm v|\\ge|\\bm u+\\bm v|

由代数特征，不难发现实际上也有

\\sqrt{a_1^2+a_2^2}+\\sqrt{b_1^2+b_2^2}\\ge\\sqrt{(a_1\\pm b_1)^2+(a_2\\pm b_2)^2}

\\sqrt{a_1^2+a_2^2}+\\sqrt{b_1^2+b_2^2}\\ge\\sqrt{(a_1\\pm b_2)^2+(a_2\\pm b_1)^2}

等等，用各种方法都可以证明，上式取等条件为

\\dfrac{a_1}{b_1}=\\dfrac{a_2}{b_2}

或者

a_1b_2=a_2b_1

拓展到 n 维就是

\\sqrt{a_1^2+a_2^2+\\dots+a_n^2}+\\sqrt{b_1^2+b_2^2+\\dots+b_n^2}\\ge\\sqrt{(a_1+b_1)^2+(a_2+b_2)^2+\\dots+(a_n+b_n)^2}

更一般的，设 p\\ge 1，x_k,y_k\\in\\mathbb R，有

\\sqrt[p]{\\sum\_{k=1}^n|x_k+y_k|^p}+\\sqrt[p]{\\sum\_{k=1}^n|x_k|^p}\\ge\\sqrt[p]{\\sum\_{k=1}^n|y_k|^p}

这两个取等条件为

\\dfrac{a_1}{b_1}=\\dfrac{a_2}{b_2}=\\dots=\\dfrac{a_n}{b_n}

注意如果有零，那么必然一个数列是全零，因此这样问题可以化简为只有一个数列没有零，把他当作 b 即可避免 0 作为除数的问题。

当 p=1 的平凡形式即为

\\sum\_{k=1}^n|x_k+y_k|\\le\\sum\_{k=1}^n|x_k|+|y_k|

或

|x+y|\\le|x|+|y|

的三角不等式形式。

因为有较强的几何意义，因此闵可夫斯基不等式在难度不大的题目中，应用比下面几个广泛得多，例如，**已知 x+y=2，求 \\sqrt{x^2+1}+\\sqrt{y^2+4} 的最小值。**

从闵可夫斯基不等式的角度，构造

\\sqrt{x^2+1}+\\sqrt{y^2+4}\\ge\\sqrt{(x+y)^2+(1+2)^2}=\\sqrt{13}

### 杨氏不等式

杨氏不等式，即杨格不等式，表明，当 p,q>1 且 \\dfrac{1}{p}+\\dfrac{1}{q}=1 时，

ab\\le\\dfrac{a^p}{p}+\\dfrac{b^q}{q}

等号成立当且仅当 a^p=b^q 也就是 a^{p-1}=b。

当 p=q=2 时，不等式化为均值不等式

ab\\le\\dfrac{p^2+q^2}{2}

杨氏不等式可以用来证明赫尔德不等式，但是形式复杂，这里不再描述。

### 赫尔德不等式

赫尔德不等式，或赫耳德不等式，表明当 p,q>1 且 \\dfrac{1}{p}+\\dfrac{1}{q}=1 时，在实数下

\\sum\_{k=1}^n|a_kb_k|\\le\\sqrt[p]{\\sum\_{k=1}^n|a_k|^p}\\sqrt[q]{\\sum\_{k=1}^n|b_k|^q}

等号成立条件为 {a_n},{b_n} 至少有一个数列为零数列，或者

|a_1|:|a_2|:\\dots:|a_n|=|b_1|:|b_2|:\\dots:|b_n|

赫尔德不等式可以用来证明三角不等式、闵可夫斯基不等式，当 p=q=2 时为柯西不等式。

### 马勒不等式

马勒不等式表明，对于正项数列 {x_n},{y_n}（即每一项都是正数）

\\sqrt[n]{\\prod\_{k=1}^nx_k}+\\sqrt[n]{\\prod\_{k=1}^ny_k}\\le\\sqrt[n]{\\prod\_{k=1}^n(x_k+y_k)}

马勒不等式陈述说由两个无穷正项序列的对应项的和构成序列的几何均值大于或等于这两个无穷序列几何均值的和，当 n=2 时的形式我们较为熟悉

\\sqrt{x_1+x_2}+\\sqrt{y_1+y_2}\\le\\sqrt{(x_1+y_1)(x_2+y_2)}

我们考虑证明一般的，构造均值不等式

\\sqrt[n]{\\prod\_{k=1}^n\\dfrac{x_k}{x_k+y_k}}\\le\\dfrac{1}{n}\\sum\_{k=1}^n\\dfrac{x_k}{x_k+y_k}

\\sqrt[n]{\\prod\_{k=1}^n\\dfrac{y_k}{x_k+y_k}}\\le\\dfrac{1}{n}\\sum\_{k=1}^n\\dfrac{y_k}{x_k+y_k}\\ge

两遍相加即可得到

\\sqrt[n]{\\prod\_{k=1}^n\\dfrac{x_k}{x_k+y_k}}+\\sqrt[n]{\\prod\_{k=1}^n\\dfrac{y_k}{x_k+y_k}}\\le1

把分母乘过去即可。

## 其他不等式

### 排序不等式

对于非严格单调递增（或递减）的实数序列 x,y，另 \\sigma(i) 表示 1\\sim n 的任意一个排列，有，

x_1y_1+\\dots+x_ny_n\\ge x\_{\\sigma(1)}y_1+\\dots+x\_{\\sigma(n)}y_n\\ge x_ny_1+\\dots+x_1y_n

顺序和不小于乱序和，乱序和不小于逆序和；取等为 x,y 分别两两相等。

排序不等式不限正负，证明可以归纳法。

对于两个非负实数 a, b，均值不等式 a+b \\ge 2\\sqrt{ab} 完全可以由排序不等式直接推出。

设 x_1 = \\sqrt{a},; x_2 = \\sqrt{b}，不妨假设 x_1 \\le x_2（即 \\sqrt{a} \\le \\sqrt{b}$）。现在我们有两个完全相同的序列：

A = (x_1, x_2),\\quad B = (x_1, x_2)

根据**排序不等式**，对两个同序序列，顺序和最大，逆序和最小：

- **顺序和**（同序相乘再相加）：x_1x_1 + x_2x_2 = a + b。
- **逆序和**（一正一反相乘再相加）：x_1x_2 + x_2x_1 = 2\\sqrt{ab}。

因为顺序和 \\ge 逆序和，所以 a + b \\ge 2\\sqrt{ab} 这正是二元均值不等式。

这个推导相当于把均值不等式看作是“自己与自己”的排序不等式：将 (\\sqrt{a}, \\sqrt{b}) 这个序列与自身做同序匹配得到 a+b，做逆序匹配得到 2\\sqrt{ab}。由于同序和最大，便自然得到了算术平均不小于几何平均。

因此，二元均值不等式确实可以视为排序不等式在序列 \\sqrt{a}, \\sqrt{b} 上的一个特例。多元均值不等式同样可以看作排序不等式的一个推论，只是此时需要反复应用排序不等式，不像二元时一步到位。我们就不展开讲解了。

2025-08-112026-09-22

[RainPPR](mailto:PPR2125773894@163.com),  [Bot](mailto:bot@noreply.github.com)
