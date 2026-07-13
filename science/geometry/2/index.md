# 三角函数与三角恒等变换

## 角和三角函数

### 任意角和弧度制

任意角的定义：平面内一条射线绕其端点从一个位置旋转到另一个位置形成的图形叫做角。

开始的位置称为始边，结束的位置称为终边。并规定：

- 按逆时针方向旋转形成的角叫做正角，其角度为正；
- 按顺时针方向旋转形成的角叫做负角，其角度为负；
- 终边相对于始边没有做任何旋转的角叫做零角，其角度为 0。

为什么逆时针是正角？考虑点 (1,0) 绕着 (0,0) 转一个锐角：

得到的点 A(x,y) 一定满足 x,y>0，因此定义逆时针为正角。

这样就把角的概念推向了任意角。

弧度制的定义：弧度用符号 \\text{rad} 表示，读作「弧度」。

定义正角的弧度为正、负角的弧度为负，零角的弧度为 0；

如果半径为 r 的圆的圆心角 \\alpha 所对弧长为 l ，则：

|\\alpha|=\\dfrac{l}{r}

与角 \\alpha 终边位置相同的角的集合很容易得出，为：

{\\varphi \\mid \\varphi = \\alpha - 2k\\pi, k \\in \\mathbb{Z}}

弧度与角度的转化：关键是，180^\\circ=\\pi，具体的。

以度数表示的角，把数字乘以 \\dfrac{\\pi}{180^\\circ} 便转换成弧度；

以弧度表示的角，乘以 \\dfrac{180^\\circ}{\\pi} 便转换成度数。

扇形的面积、周长、弧长公式：

- 引入了弧度制后，我们便可以轻松的计算弧长 \\ell=\\alpha r。
- 面积公式 S=\\dfrac{\\ell r}{2}=\\dfrac{\\alpha r^2}{2}=\\dfrac{\\ell^2}{2\\alpha}。
- 对于扇形，周长包括两个半径和一个弧长：C=2r+\\ell=2r+\\alpha r。

上述公式都要代入弧度制，如果是角度值，需要换算。

### 三角函数的定义

用直角三角形定义：直角三角形只有锐角三角函数的定义。指定锐角 \\theta，可做出直角三角形，使一个内角为 \\theta。

- 正弦 \\sin\\alpha 表示 \\alpha 的对边与斜边的比值。
- 余弦 \\cos\\alpha 表示 \\alpha 的邻边与斜边的比值。
- 正切 \\tan\\alpha 表示 \\alpha 的对边与邻边的比值。

用直角坐标系定义：设点 P(x,y) 是平面直角坐标系 xOy 中的一点。

- 我们记 \\theta 是从 x 旋转到 OP 的角度，r 是 OP 长度。则：

  \\begin{aligned} r=\\sqrt{x^2+y^2}\\ \\sin\\theta=\\frac{y}{r}\\ \\cos\\theta=\\frac{x}{r}\\ \\tan\\theta=\\frac{y}{x}\\ \\end{aligned}

- 这样可以定义任何角度的三角函数（除非当定义式无意义时）。

用单位圆定义：单位圆指半径为单位长度的圆。

- 通常是平面直角坐标系中以 (0,0) 为圆心、半径为 1 的圆。

- 单位圆上的点满足：x^2+y^2=1，即毕达哥拉斯定理。

- 指定一角 \\theta，点 (1,0) 旋转 \\theta 度得到的点 A(x,y)，那么：

  \\begin{aligned} x^2+y^2=1\\ \\sin\\theta=y\\ \\cos\\theta=x\\ \\tan\\theta=\\frac{y}{x}\\ \\end{aligned}

- 三角函数线：设角 \\alpha 的终边与单位圆交于点 P，过 P 做 PM\\perp x 轴，垂足为 M，过 A(1,0) 做单位圆的切线与 \\alpha 的终边或其反向延长线交于 T。

  则 T 到 x 轴的距离（带有正负号）即为 \\tan\\alpha。据此容易理解，为什么 \\tan90^\\circ 是无意义的，或者说，存在于正负无穷大了。

常见的三角函数定义：

\\begin{aligned} \\tan\\alpha=\\frac{\\sin\\alpha}{\\cos\\alpha}\\ \\cot\\alpha=\\frac{1}{\\tan\\alpha}\\ \\sec\\alpha=\\frac{1}{\\cos\\alpha}\\ \\csc\\alpha=\\frac{1}{\\sin\\alpha} \\end{aligned}

常见角度的三角函数：

| 角度       | 弧度     | 正弦（\\sin） | 余弦（\\cos） | 正切（\\tan） |
| ---------- | -------- | ------------- | ------------- | ------------- |
| 0^\\circ   | 0        | 0             | 1             | 0             |
| 30^\\circ  | \\pi/6   | 1/2           | \\sqrt3/2     | \\sqrt3/3     |
| 45^\\circ  | \\pi/4   | \\sqrt2/2     | \\sqrt2/2     | 1             |
| 60^\\circ  | \\pi/3   | \\sqrt3/2     | 1/2           | \\sqrt3       |
| 90^\\circ  | \\pi/2   | 1             | 0             | 无意义        |
| 120^\\circ | 2\\pi/3  | \\sqrt3/2     | -1/2          | -\\sqrt3      |
| 135^\\circ | 3\\pi/4  | \\sqrt2/2     | -\\sqrt2/2    | -1            |
| 150^\\circ | 5\\pi/6  | 1/2           | -\\sqrt3/2    | -\\sqrt3/3    |
| 180^\\circ | \\pi     | 0             | -1            | 0             |
| 210^\\circ | 7\\pi/6  | -1/2          | -\\sqrt3/2    | \\sqrt3/3     |
| 225^\\circ | 5\\pi/4  | -\\sqrt2/2    | -\\sqrt2/2    | 1             |
| 240^\\circ | 4\\pi/3  | -\\sqrt3/2    | -1/2          | \\sqrt3       |
| 270^\\circ | 3\\pi/2  | -1            | 0             | 无意义        |
| 300^\\circ | 5\\pi/3  | -\\sqrt3/2    | 1/2           | -\\sqrt3      |
| 315^\\circ | 7/4      | -\\sqrt2/2    | \\sqrt2/2     | -1            |
| 330^\\circ | 11\\pi/6 | -1/2          | \\sqrt3/2     | -\\sqrt3/3    |
| 360^\\circ | 2\\pi    | 0             | 1             | 0             |

尼云定理指出，在 0\\sim90^\\circ 范围内，如果正弦函数 \\sin 的自变量和因变量都要求是有理数，那么答案只有：

\\begin{aligned} \\sin0^\\circ&=0\\ \\sin30^\\circ&=1/2\\ \\sin90^\\circ&=1 \\end{aligned}

### 正弦函数的性质

分析函数的套路：

- 定义域、值域、图像。
- 周期性、单调性。
- 对称轴、对称中心。
- 最大值、最小值、零点。

图像：

三角函数

周期性：

\\begin{aligned} \\sin\\alpha=\\sin(\\alpha+2\\pi)\\ \\cos\\alpha=\\cos(\\alpha+2\\pi) \\end{aligned}

可知 \\sin、\\cos 是最小正周期为 2\\pi 的周期函数。

奇偶性：正弦函数是奇函数，余弦函数是偶函数。

对称性：

1. 正弦函数：
   - 中心对称：(k\\pi,0),k\\in\\mathbb Z；
   - 轴对称：x=k\\pi-\\pi/2,k\\in\\mathbb Z；
1. 余弦函数：
   - 中心对称：(k\\pi-\\pi/2),k\\in\\mathbb Z；
   - 轴对称：x=k\\pi,k\\in\\mathbb Z。

- 对称中心：零点；对称轴：极值点。

解含参对称性问题的套路：不妨代入 \\sin x=0 表示中心对称，代入 \\cos x=\\pm 1 为轴对称，通过这种转化，或者直接写 x=\\dots 用 k\\pi,k\\in\\mathbb Z 的通式。

单调性：

1. 正弦函数：
   - 单调递增：[2k\\pi-\\pi/2,2k\\pi+\\pi/2],k\\in\\mathbb Z；
   - 单调递减：[2k\\pi+\\pi/2,2k\\pi+3\\pi/2],k\\in\\mathbb Z；
1. 余弦函数：
   - 单调递增：[2k\\pi-\\pi,2k\\pi],k\\in\\mathbb Z；
   - 单调递减：[2k\\pi,2k\\pi+\\pi],k\\in\\mathbb Z；

解单调性的套路：设 t=\\omega x+\\varphi，然后不妨解关于 t 的方程。这一部分通常的解法，就是找出所有 t 的关系，有的可以直接写出 t=\\dots 用 k\\pi,2k\\pi 表示，有的可以写 \\dots\\le t\\le\\dots 讨论参数范围，但是总之来说，思考难度不大，计算难度不小，细心即可。

正弦曲线及其性质：正弦曲线，形如 y=A\\sin(\\omega x+\\varphi)。注意到 \\sin、\\cos 其实都属于正弦曲线。

函数 y=A\\sin x 的性质:

- 我们发现这个操作其实就是对 y 轴的伸缩：
- 若 A>1，图像伸长；若 A\<1，图像压缩；伸缩倍率为 A。
- 也就是图像上任何一个点的纵坐标变成了原来的 A 倍。
- 其中 A 决定了函数上的点的纵坐标的变化幅度，我们称为振幅。

函数 y=\\sin(x+\\varphi) 的性质:

- 我们发现这个操作其实就是对 y=\\sin x 图像的平移：
- 若 \\varphi>0，图像向左平移；若 \\varphi\<0 图像向右平移；平移单位为 |\\varphi|。
- 也就是点 P(x,\\sin x) 平移到了 P'(x-\\varphi,\\sin x)。
- 其中 \\varphi 决定了初始时刻的位置，我们称为初相。

函数 y=\\sin(\\omega x) 的性质:

- 我们发现这个操作其实就是对 x 轴的伸缩：

- 若 \\omega>1，图像压缩；若 \\omega\<1，图像伸长；伸缩倍率为 1/\\omega。

- 也就是点 P(x,\\sin x) 平移到了 P'\\left(\\dfrac{x}{\\omega},\\sin x\\right)。

- 其中 \\omega 决定了函数值的变化快慢，我们称为角速度。

- 由于 \\sin x 的最小正周期为 2\\pi，因此 \\sin(\\omega x) 的最小正周期为：

  T=\\frac{2\\pi}{\\omega}

函数 y=\\sin(\\omega x+\\varphi) 的性质：

- 一切变换是对于 x,y 的且满足左加右减，上加下减。
- \\omega,\\varphi 可以统称为相位（初相和角速度）。

我们把上面两个操作合在一起，但是，顺序？我们来分析一下。

考虑 y=\\sin x 平移 \\varphi 和 x 轴伸缩 \\omega 这两个操作以不同的顺序会得到什么：

- 先平移 \\varphi，后 x 轴伸缩 \\omega：
  1. y=\\sin x
  1. y=\\sin(x+\\varphi)
  1. y=\\sin(\\omega x+\\varphi)
- 先 x 轴伸缩 \\omega，后平移 \\varphi：
  1. y=\\sin x
  1. y=\\sin(\\omega x)
  1. y=\\sin(\\omega(x+\\varphi))
  1. y=\\sin(\\omega x+\\omega\\varphi)
- 易错点：
  - 平移是对于 x 的，而伸缩（在 x 轴上）是对应整个函数的。
  - 把函数 y=\\sin(\\omega x+\\varphi)（可以看为 f(x)=\\sin(\\omega x+\\varphi)）：
  - 平移 \\varphi' 是 y=\\sin(\\omega(x+\\varphi')+\\varphi)，而不是 y=\\sin(\\omega x+\\varphi'+\\varphi)
  - 伸缩 \\omega' 是 y=\\sin(\\omega'\\omega x+\\varphi)，而不是 y=\\sin(\\omega'(\\omega x+\\varphi))
  - 即，平移是对于 x 的操作，伸缩是对于传入函数的值的操作。

注意到 y=\\sin(\\omega x+\\varphi) 相当于 y=\\sin(\\omega x) 平移 \\dfrac{\\varphi}{\\omega} 得到的，

这个函数过点 P\\left(-\\dfrac{\\varphi}{\\omega},0\\right)，而不是 y=\\sin(\\omega x+\\omega\\varphi) 过 P'(-\\varphi,0)。

据此，我们得出，从 y=\\sin x 变换到 y=\\sin(\\omega x+\\varphi)，需要：

- 先平移 \\varphi，再对 x 轴伸缩 \\omega。

因此可以得出，P(x,\\sin x) 平移到了 P'\\left(\\dfrac{x-\\varphi}{\\omega},\\sin x\\right)。

正弦函数到 y=A\\sin(\\omega x+\\varphi) 的变换：

- 其实就相当于对函数 y=\\sin(\\omega x+\\varphi) 的 y 轴伸缩 A 倍。
- 注意到 A 只是对 y 轴的伸缩，因此可以在任意时间变换。
- 注意到 \\omega 是对 x 轴的伸缩，因此需要在 \\varphi 的变换之后（前文已述）。

当然上面说的是分别进行三个变换各一次的顺序，据此我们进行组合：

1. 平移 \\varphi；
1. x 轴伸缩 \\omega；
1. y 轴伸缩 A。

可以从 y=\\sin x 得到 y=A\\sin(\\omega x+\\varphi) 的组合有：

(1,2,3),(1,3,2),(3,1,2)

三种方式。

注意倒推法的应用。

函数 y=A\\sin(\\omega x+\\varphi) 的性质：基础性质上文写的很详细了，再梳理一遍。

我们知道，正弦函数和余弦函数只差了一个平移，

因此下文只讨论了正弦函数对应的正弦曲线，余弦函数的自己脑补。

首先我们整理一下各个字母的含义：

- A 表示振幅：
  - 若 A>1，图像在 y 轴上伸长；
  - 若 A\<1，图像在 y 轴上压缩；
  - 伸缩倍率为 A。
- \\omega 表示角速度：
  - 若 \\omega>1，图像在 x 轴上压缩；
  - 若 \\omega\<1，图像在 x 轴上伸长；
  - 伸缩倍率为 1/\\omega。
- \\varphi 表示初相，但是并不单独决定函数的位置。

这个函数相当于函数 y=\\sin x 进行一定的操作（下面再说）。

其中，点 P(x,\\sin x) 平移到了 P\\left(\\dfrac{x-\\varphi}{\\omega},A\\sin x\\right)。

定义域和值域：我们在这里统一说明正弦曲线的定义域和值域。

- 定义域，\\mathbb R；值域，[-A,A]。
- 因此，\\sin、\\cos 函数的值域就是 [-1,1]。

最小正周期：由于其进行的变换对最小正周期没有影响，因此，

T=\\frac{2\\pi}{\\omega}

绘制简图：**五点作图法**。

- 正弦曲线在一个周期内，一定是上去下来上去（或是歪了的）。
- 因此我们可以对于周期内的五个点（分为四个区间）画图：
- 比如，最小正周期为 \\pi 的，我们可以做出 [0,\\pi/4,\\pi/2,3\\pi/4,\\pi] 五个点的图像。
- 然后用光滑的曲线连接，再根据周期性画出其他部位的图像即可。
- 也可以先看出来在所求范围内，函数的极大、极小点在哪里。
- 也就是正弦函数的最值点，求出传入函数的值中 x 对应多少。
- 然后先把这些点画出来，再找三个或更多上述性质的点求解、画图。

如果思考含参比较困难，不妨直接写 F(x)=0,F(x)=\\dfrac{\\pi}{2},\\dots，然后解出一组最好看的解，去讨论即可。

**单调区间**可以用下面的方式：

- 我们知道正弦函数的单增区间是 [2k\\pi-\\pi/2,2k\\pi+\\pi/2]。

- 意思是当传入正弦函数的值在这个区间内，函数值单增。

- 因此可以把传入函数的值当做一个整体，对于 y=A\\sin(\\omega x+\\varphi)：

  2k\\pi-\\pi/2\\le\\omega x+\\varphi\\le2k\\pi+\\pi/2

  就是单调区间，化简即可。

- 单减区间是 [2k\\pi+\\pi/2,2k\\pi+\\pi]，计算同理。

- 不过单减区间还有一个求法，就是单增区间的两个端点都加上 T/2。

- 原理就是单增区间往右到下一个单增区间是单减的且长度是半周期。

对于整个图像的最值，就是函数的值域 [-A,A]。

对于一个区间的最值，可以有两个方法：

1. 画出函数简图，找到区间在图像上的位置，找到极大极小点求解。
1. 画出单位圆的示意图，在单位圆上找到函数的极大极小点，求解。

对称轴、对称中心：

- 对称轴：最值点。

  正弦函数的最值点都可以表示为 k\\pi+\\pi/2,k\\in\\mathbb Z，余弦函数不加 \\pi/2。

- 对称中心：零点。

  余弦函数的零点都可以表示为 k\\pi+\\pi/2,k\\in\\mathbb Z，正弦函数不加 \\pi/2。

求正弦曲线解析式：也就是求三个值 A、\\omega、\\varphi。

- 其中 A 只与函数的最值有关，因此我们可以求出来它，则 A 就是函数的最值。

- 其次 \\omega 表示的是角速度，根据公式 T=2\\pi/\\omega 可以写出 \\omega=2\\pi/T。

- 而 T 就是两个相邻极值点的距离的两倍、极值和零点的距离的四倍。

- 考虑 \\varphi，易发现最好求的方法就是函数与 y 轴的交点 y|\_{x=0}，那么就有

  A\\sin\\varphi=y|\_{x=0}

- 求解即可。其次我们可以用函数的最值点、零点等，列：

  A\\sin(\\omega x_0+\\varphi)=y|\_{x=x_0}

- 解方程时要注意 \\varphi 的取值一般是 0\\le\\varphi\<T，A、\\omega 的取值一般是正数。

### 正切函数的性质

分析函数的套路：

- 定义域：{x\\mid x\\neq k\\pi+\\pi/2,k\\in\\mathbb Z}；
- 值域：(-\\infty,+\\infty)
- 周期性：T=\\pi；
- 单调性：在 (k\\pi-\\pi/2,k\\pi+\\pi/2) 单调递增。
- 对称性：奇函数，关于 (k\\pi,0),k\\in\\mathbb Z 对称。

齐次和弦化切、切化弦：

- 我们定义正弦和余弦都是一次的，那么正切就是零次的。
- 根据 \\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha} 且 \\sin^2\\alpha+\\cos^2\\alpha，那么，对于任意齐偶数次式，都可以化为和 \\tan\\alpha 为唯一变量的式子。
- 后文会再次提到，正切半角公式也是相当好用的一个归一方法。

## 三角恒等变化

### 诱导公式

函数关于 2\\pi 的周期性：是 \\sin、\\cos 的周期。

\\begin{aligned} \\sin(\\alpha+2\\pi)&=\\sin\\alpha\\ \\cos(\\alpha+2\\pi)&=\\cos\\alpha\\ \\tan(\\alpha+2\\pi)&=\\tan\\alpha \\end{aligned}

函数关于 \\pi 的周期性：是 \\tan、\\cot 的周期。

\\begin{aligned} \\sin(\\alpha+\\pi)&=-\\sin\\alpha\\ \\cos(\\alpha+\\pi)&=-\\cos\\alpha\\ \\tan(\\alpha+\\pi)&=\\tan\\alpha \\end{aligned}

函数的奇偶性：奇函数 \\sin、\\tan、\\cot，偶函数 \\cos。

\\begin{aligned} \\sin(-\\alpha )&=-\\sin \\alpha\\ \\cos(-\\alpha )&=\\cos \\alpha\\ \\tan(-\\alpha )&=-\\tan \\alpha\\ \\end{aligned}

函数关于 y 轴的对称性：用单位圆象限角理解。

\\begin{aligned} \\sin(\\pi-\\alpha)&=\\sin\\alpha\\ \\cos(\\pi-\\alpha)&=-\\cos\\alpha\\ \\tan(\\pi-\\alpha)&=-\\tan\\alpha \\end{aligned}

余函数恒等式：用单位圆象限角理解。

\\begin{aligned} \\sin(\\pi/2-\\alpha)&=\\cos\\alpha\\ \\cos(\\pi/2-\\alpha)&=\\sin\\alpha\\ \\tan(\\pi/2-\\alpha)&=\\cot\\alpha \\end{aligned}

在直角三角形中的转换：用单位圆象限角理解。

\\begin{aligned} \\sin \\left(\\pi/2+\\alpha\\right)&=\\cos\\alpha\\ \\cos \\left(\\pi/2+\\alpha\\right)&=-\\sin\\alpha\\ \\tan \\left(\\pi/2+\\alpha\\right)&=-\\cot\\alpha\\ \\end{aligned}

单位圆象限角：上述所有式子有一个联系。

\\begin{aligned} \\sin(k\\pi/2\\pm\\alpha)&,k\\in\\mathbb{Z}\\ \\cos(k\\pi/2\\pm\\alpha)&,k\\in\\mathbb{Z}\\ \\tan(k\\pi/2\\pm\\alpha)&,k\\in\\mathbb{Z} \\end{aligned}

转换法则：

- 当 k 为偶数时，三角函数则不变换。
- 当 k 为奇数时，\\sin 变为 \\cos，\\cos 变为 \\sin，\\tan 变为 \\cot，\\cot 变为 \\tan。
- 对于正负号，则要看最后角所在的象限进行判断。

可使用口诀：奇变偶不变，符号看象限（ASTC, All Students Take Calculus）记忆。

- 第一象限的 A 即是 All（全部皆正）。
- 第二象限的 S 即是 Sine（正弦以及余割为正）。
- 第三象限的 T 即是 Tangent（正切以及余切为正）。
- 第四象限的 C 即是 Cosine（余弦以及正割为正）。

常见化简方法：周期性（\\sin、\\cos 是 2\\pi，\\tan、\\cot 是 \\pi），奇偶性（\\sin、\\tan、\\cot 是奇函数，\\cos 是偶函数），出现 \\pi/2 系列的要变符号，画出单位圆求解。

### 毕达哥拉斯三角恒等式

基础形式：

\\begin{aligned} \\sin^2\\alpha+\\cos^2\\alpha=1 \\end{aligned}

也称为三角函数的勾股定理。

根据上面的，易得：

\\begin{aligned} \\sin^2\\alpha&=1-\\cos^2\\alpha\\ \\cos^2\\alpha&=1-\\sin^2\\alpha \\end{aligned}

开方，得：

\\begin{aligned} \\sin\\alpha&=\\pm\\sqrt{1-\\cos^2\\alpha}\\ \\cos\\alpha&=\\pm\\sqrt{1-\\sin^2\\alpha} \\end{aligned}

一定要注意正负号，正负号由该角所在象限决定。

### 和差恒等式

也称为「和差定理」、「和差公式」或「和角公式」。

\\begin{aligned} \\sin(\\alpha\\pm\\beta)&=\\sin\\alpha\\cos\\beta\\pm\\cos\\alpha\\sin\\beta\\ \\cos(\\alpha\\pm\\beta)&=\\cos\\alpha\\cos\\beta\\mp\\sin\\alpha\\sin\\beta\\ \\tan(\\alpha\\pm\\beta)&=\\frac{\\tan\\alpha\\pm\\tan\\beta}{1\\mp\\tan\\alpha\\tan\\beta} \\end{aligned}

注意正负号的对应。

由 \\tan 的和角公式，不妨代入某角为 45^\\circ，即可得出：

\\tan(45^\\circ+\\alpha)=\\dfrac{1+\\tan\\alpha}{1-\\tan\\alpha}

\\tan(45^\\circ-\\alpha)=\\dfrac{1-\\tan\\alpha}{1+\\tan\\alpha}

同时，正切的和角公式有经典变形：

\\tan\\alpha\\pm\\tan\\beta=\\tan(\\alpha\\pm\\beta)(1\\mp\\tan\\alpha\\tan\\beta)

\\tan\\alpha\\tan\\beta=1-\\dfrac{\\tan\\alpha+\\tan\\beta}{\\tan(\\alpha+\\beta)}

\\tan\\alpha\\tan\\beta=\\dfrac{\\tan\\alpha-\\tan\\beta}{\\tan(\\alpha-\\beta)}-1

因此：

\\tan\\alpha\\tan\\beta=\\dfrac{\\tan\\alpha-\\tan\\beta}{\\tan(\\alpha-\\beta)}-\\dfrac{\\tan\\alpha+\\tan\\beta}{\\tan(\\alpha+\\beta)}

### 倍角公式

二倍角公式：

\\begin{aligned} \\sin2\\alpha&=2\\sin\\alpha\\cos\\alpha\\ \\cos2\\alpha&=\\cos^2\\alpha-\\sin^2\\alpha\\ &=1-2\\sin^2\\alpha\\ &=2\\cos^2\\alpha-1\\ \\tan2\\alpha&=\\frac{2\\tan\\alpha}{1-\\tan^2\\alpha} \\end{aligned}

可以根据里面的结论推出降次公式。

这里有一个很好的推论，同时使用二倍角公式和辅助角公式：

(\\sin\\alpha+\\cos\\alpha)^2=\\sin^2\\alpha+\\cos^2\\alpha+2\\sin\\alpha\\cos\\alpha=1+2\\sin2\\alpha

同时：

\\sin\\alpha+\\cos\\alpha=\\sqrt{2}\\sin(\\alpha+45^\\circ)

以及用 \\sin\\alpha-\\cos\\alpha 做类似推导，就可以得出：

(\\sin\\alpha+\\cos\\alpha)^2=1+2\\sin2\\alpha=2\\sin^2(\\alpha+45^\\circ)

(\\sin\\alpha-\\cos\\alpha)^2=1-2\\sin2\\alpha=2\\sin^2(\\alpha-45^circ)

以及

\\sqrt{1+\\pm \\sin2\\alpha}=|\\sin\\alpha\\pm\\cos\\alpha|

用余弦的倍角公式，也可以得到：

\\sqrt{1-\\cos2\\alpha}=\\sqrt{2}|\\sin\\alpha|

\\sqrt{1+\\cos2\\alpha}=\\sqrt{2}|\\cos\\alpha|

同时还有一个公式：

\\sin\\alpha=\\dfrac{\\sin2\\alpha}{2\\cos\\alpha}

\\cos\\alpha=\\dfrac{\\sin2\\alpha}{2\\sin\\alpha}

三倍角公式：

\\begin{aligned} \\sin3\\alpha&=3\\sin\\alpha-4\\sin^3\\alpha&&=4\\sin\\left(\\dfrac\\pi3-\\alpha\\right)\\sin\\alpha\\sin\\left(\\dfrac\\pi3+\\alpha\\right)\\ \\cos3\\alpha&=4\\cos^3\\alpha-3\\cos\\alpha&&=4\\cos\\left(\\dfrac\\pi3-\\alpha\\right)\\cos\\alpha\\cos\\left(\\dfrac\\pi3+\\alpha\\right)\\ \\end{aligned}

下面的式子即为：

\\cos3\\alpha=4\\cos(\\alpha-60^\\circ)\\cos\\alpha\\cos(\\alpha+60^\\circ)

正切同理，也可以用这个式子进行三次降幂。

\\cos 3\\theta=\\begin{vmatrix}\\cos\\theta & 1 & 0 \\ 1 & 2\\cos\\theta & 1 \\ 0 & 1 & 2\\cos\\theta\\end{vmatrix}

\\sin 3\\theta=\\begin{vmatrix}\\sin\\theta & 0 & 0 \\ 0 & 2\\sin\\theta & 1 \\ 0 & 1 & 2\\cos\\theta\\end{vmatrix}

\\cos n\\theta=\\begin{vmatrix} \\cos\\theta & 1 & 0 & \\cdots & 0 & 0 \\ 1 & 2\\cos\\theta & 1 & \\cdots & 0 & 0 \\ 0 & 1 & 2\\cos\\theta & \\cdots & 0 & 0 \\ \\vdots & \\vdots & \\vdots & \\ddots & \\vdots & \\vdots \\ 0 & 0 & 0 & \\cdots & 2\\cos\\theta & 1 \\ 0 & 0 & 0 & \\cdots & 1 & 2\\cos\\theta \\end{vmatrix}

\\sin n\\theta=\\begin{vmatrix} \\sin\\theta & 0 & 0 & \\cdots & 0 & 0 \\ 0 & 2\\cos\\theta & 1 & \\cdots & 0 & 0 \\ 0 & 1 & 2\\cos\\theta & \\cdots & 0 & 0 \\ \\vdots & \\vdots & \\vdots & \\ddots & \\vdots & \\vdots \\ 0 & 0 & 0 & \\cdots & 2\\cos\\theta & 1 \\ 0 & 0 & 0 & \\cdots & 1 & 2\\cos\\theta \\end{vmatrix}

这就是高倍角公式的行列式表示。

### 半角公式

半角公式：

\\begin{aligned} \\sin\\frac{\\alpha}{2}&=\\pm\\sqrt{\\frac{1-\\cos\\alpha}{2}}\\ \\cos\\frac{\\alpha}{2}&=\\pm\\sqrt{\\frac{1+\\cos\\alpha}{2}}\\ \\tan{\\frac{\\alpha}{2}}&=\\pm{\\sqrt{1-\\cos\\theta\\over1+\\cos\\theta}}\\ \\tan{\\frac{\\alpha}{2}}&=\\frac{\\sin\\alpha}{1+\\cos\\alpha}=\\frac{1-\\cos\\alpha}{\\sin\\alpha} \\end{aligned}

正负号由半角所在象限决定。

最后一行的公式相当常用，推导方式，可以直接从右面用正切半径公式展开。如果要从左面推右面，可以用配凑的方法：

\\tan\\dfrac{\\alpha}{2}=\\dfrac{\\sin\\frac{\\alpha}{2}}{\\cos\\frac{\\alpha}{2}}=\\dfrac{2\\sin\\frac{\\alpha}{2}\\cos\\frac{\\alpha}{2}}{2\\cos^2\\dfrac{\\alpha}{2}}

然后分别用倍角公式展开即可。

### 正切半角公式

也称为万能公式。

\\begin{aligned} \\sin\\alpha&={2\\tan{\\alpha\\over2}\\over1+\\tan^2{\\alpha\\over2}}\\ \\cos\\alpha&={1-\\tan^2{\\alpha\\over2}\\over1+\\tan^2{\\alpha\\over2}}\\ \\tan\\alpha&={2\\tan{\\alpha\\over2}\\over1-\\tan^2{\\alpha\\over2}} \\end{aligned}

其中下面的一个也等价于正切函数的二倍角公式。

\\tan\\alpha-\\dfrac{1}{\\tan\\alpha}=\\dfrac{\\sin^2\\alpha-\\cos^2\\alpha}{\\sin\\alpha\\cos\\alpha}=-\\dfrac{2}{\\tan2\\alpha}

### 升降幂公式

降幂公式：

\\begin{aligned} \\sin^2\\alpha&=\\frac{1-\\cos2\\alpha}{2}\\ \\cos^2\\alpha&=\\frac{1+\\cos2\\alpha}{2}\\ \\tan^2\\alpha&=\\frac{1-\\cos2\\alpha}{1+\\cos2\\alpha} \\end{aligned}

补充一个属于幂简约公式的：

\\sin^2\\alpha\\cos^2\\alpha={1-\\cos4\\alpha\\over8}

可以根据里面的结论推出半角公式。

升幂公式：

1+\\cos2\\alpha=2\\cos^2\\alpha

1-\\cos2\\alpha=2\\sin^2\\alpha

### 第一类切比雪夫多项式

第一类 Chebyshev（切比雪夫）多项式由以下递推关系确定：

\\begin{aligned} T_0(x)&=1\\ T_1(x)&=x\\ T\_{n+1}(x)&=2xT_n(x)-T\_{n-1}(x) \\end{aligned}

有三角恒等式：

cos(n\\theta)=T_n(\\cos\\theta)

其中：

\\begin{aligned} T\_{0}(x) & = 1\\ T\_{1}(x) & = x\\ T\_{2}(x) & = 2x^{2}-1\\ T\_{3}(x) & = 4x^{3}-3x\\ T\_{4}(x) & = 8x^{4}-8x^{2}+1\\ T\_{5}(x) & = 16x^{5}-20x^{3}+5x\\ T\_{6}(x) & = 32x^{6}-48x^{4}+18x^{2}-1\\ T\_{7}(x) & = 64x^{7}-112x^{5}+56x^{3}-7x\\ T\_{8}(x) & = 128x^{8}-256x^{6}+160x^{4}-32x^{2}+1\\ T\_{9}(x) & = 256x^{9}-576x^{7}+432x^{5}-120x^{3}+9x \\end{aligned}

### 和差化积与积化和差

和差化积恒等式：

\\begin{aligned} \\sin\\alpha+\\sin\\beta&=2\\sin{\\alpha+\\beta\\over2}\\cos{\\alpha-\\beta\\over2}\\ \\sin\\alpha-\\sin\\beta&=2\\cos{\\alpha+\\beta\\over2}\\sin {\\alpha-\\beta\\over2}\\ \\cos\\alpha+\\cos\\beta&=2\\cos{\\alpha+\\beta\\over2}\\cos {\\alpha-\\beta\\over2}\\ \\cos\\alpha-\\cos\\beta&=-2\\sin{\\alpha+\\beta\\over2}\\sin {\\alpha-\\beta\\over2} \\end{aligned}

积化和差恒等式：

\\begin{aligned} \\sin\\alpha\\cos\\beta&={\\sin(\\alpha+\\beta)+\\sin(\\alpha-\\beta)\\over2}\\ \\cos\\alpha\\sin\\beta&={\\sin(\\alpha+\\beta)-\\sin(\\alpha-\\beta)\\over2}\\ \\cos\\alpha\\cos\\beta&={\\cos(\\alpha+\\beta)+\\cos(\\alpha-\\beta)\\over2}\\ \\sin\\alpha\\sin\\beta&=-{\\cos(\\alpha+\\beta)-\\cos(\\alpha-\\beta)\\over2} \\end{aligned}

轮换 \\alpha,\\beta，令其为相反数，根据 \\sin,\\cos 奇偶性判断。

### 平方差公式

\\begin{aligned} \\sin(x+y)\\sin(x-y)&&&=\\sin^2x-\\sin^2y&&=\\cos^2y-\\cos^2x\\ \\cos(x+y)\\cos(x-y)&&&=\\cos^2x-\\sin^2y&&=\\cos^2y-\\sin^2x \\end{aligned}

注意到右边的式子还可以用平方差公式展开。

### 辅助角公式

对于式子：

a\\sin x+b\\cos x

如果 a=r\\cos\\varphi，b=r\\sin\\varphi，

可知

a^2+b^2=r^2(\\sin^2\\varphi+\\cos^2\\varphi)=r^2

即 r=\\sqrt{a^2+b^2}，则有 \\cos\\varphi=a/r，\\sin\\varphi=b/r。

化简式子：

\\begin{aligned} a\\sin x+b\\cos x&=r\\cos\\varphi\\sin x+r\\sin\\varphi\\cos x\\ &=r\\sin(x+\\varphi)=\\sqrt{a^2+b^2}\\sin(x+\\varphi) \\end{aligned}

其中，\\varphi 满足：

\\begin{cases} \\cos\\varphi&=a/r\\ \\sin\\varphi&=b/r \\end{cases}

若 a>0，可以写成 \\varphi=\\arctan b/a 的形式。

也就是 a\\sin x+b\\cos x=\\sqrt{a^2+b^2}\\sin(x+\\arctan b/a)。

## 三角函数思想

### 变角思想

在三角函数式的化简中，“次降角升”和“次升角降”是基本的规律，根号中含有三角函数式时，一般需要升次。其化简往往要遵循以下三个原则：

1. 一看“角”，这是最重要的一环，通过看角之间的差别与联系，把角进行合理的拆分，从而正确使用公式；
1. 二看“函数名称”，看函数名称之间的差异，从而确定使用的公式，常见的有“切化弦”等；
1. 三看“结构特征”，分析结构特征，可以帮助我们找到变形的方向，如“遇到分式要通分”等。

我们知道单独考查三角函数式的化简是极少见的，绝大多数的化简其背后就是求值，常见的求值问题有：给值求值、给角求值、给值求角。

变角

三角函数：角为先，公式特征为要。

公式特征注意：用 \\cos2\\alpha 联系 \\sin\\alpha,\\cos\\alpha。

4\\sin\\alpha\\cos\\alpha=(\\sin\\alpha+\\cos\\alpha)^2-(\\sin\\alpha-\\cos\\alpha)^2

右图为这三者的转换关系。

\\left{ \\begin{aligned} x&=\\sin\\alpha-\\sin\\beta\\ y&=\\cos\\alpha-\\cos\\beta \\end{aligned} \\right.

根据上面的可以推出 \\alpha,\\beta 和差角的正余弦。

- 两式平方后作和、平方后作差。
- 两式相乘。

也可以换元，设 t 为 \\sin,\\cos 等，将原式化为关于 t 的二次函数或分式。

注意求区间上的值域，也可以结合不等式相关内容。

### 一角一函数

一角一函数，可以简单的理解为 y=A\\sin(\\omega x+\\varphi) 的形式。

即一个角在一个三角函数里，可以更好的求解。

### 齐次思想

齐次思想，也可以归为次数的重要性。

三角函数中，弦为一次，切为零次，割为负一次。

例如对于求值类问题，升幂降角、降幂升角，是很关键的。

当一个式子中的函数次数仅为奇数后者偶数的时候，可以补充 \\sin^2+\\cos^2=1 齐次。

也可以结合弦化切，除以一个 \\sin^2+cos^2 的若干次方。

当然也存在次数的奇偶性转化，例如：

\\sin-\\cos=\\pm\\sqrt{(\\sin^2-\\cos^2)}=\\pm\\sqrt{1-2\\sin\\cos}

这种不常用，注意正负号。

### 整体角思想

整体角，即将 y=A\\sin(\\omega x+\\varphi) 中的 \\omega x+\\varphi 设为单独的变量如 t 后进行解决的思想。

化为一角一函数后，用整体角结合三角函数性质进行快速解决。

根据整体角的范围，画出函数图像或者列出关于 k,k\\in\\mathbb Z 的方程。

注意区间的开闭问题。

### 弦化切思想

切化弦通常是很容易想到的，我们直接令：

\\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha}

但是弦化切也有很大的用处，具体体现在：

- 将一个复杂的式子化为仅关于一个变量的式子。
- 对于某些求值类问题，可以使用正切半角公式（万能公式）。

### 参变分离思想

也就是主元思想的体现，将参数作为主元化简。

然后根据等式右侧的函数性质得到参数的特征。

也可以使用等式相当于左右两侧函数交点问题。

### 不同参数的常见求法

对于：

y=A\\sin(\\omega x+\\varphi)+B

- A：振幅。
- B：极值。
- \\omega：周期。
- \\varphi：通常带入求解。

### 根据周期长度解题

对于有多少零点的问题，可以在还原之前根据区间长度和周期长度得到一个大体的范围。

给定单调区间，首先可以写出，单调区间长度小于等于半周期，即：

r_0-l_0\\le\\frac{T}{2}=\\frac{\\pi}{\\omega}

然后就可以在这个大体的范围内求解，如果不好求解也会方便枚举。

然后如果可以求出 \\omega 的一些其他条件（比如奇偶性），直接求出来。

### 已知起点终点

思想：复合函数、还原。

对于 f(x)=A\\sin(\\omega x+\\varphi)，我们令 t=\\omega x+\\varphi。

注意 \\omega 的正负性，得出 t 的取值范围，进行进一步求解。

比如，给定零点横坐标、对称轴，转化为：

\\omega x_0+\\varphi=\\lambda k\\pi(+\\pi/2)

未知 \\varphi：根据已知点或特殊信息（对称轴、对称中心）带入，列出方程组求出 \\varphi。

### 未知起点终点

可以将问题再分为：正正、正负。

- 对于正负的，通常区间内存在一个已知点（\\omega=0），画图解题。
- 对于正正的，通常先用周期长度限制，然后列关于 k 的式子。

特殊的，如果 \\omega 的正负不确定，应当讨论 \\operatorname{sgn}(\\omega)。

### \\varphi 未知求 \\omega

这一类问题通常比较难：

- 各种条件，先转化为区间长度，初步限制 \\omega 的范围。
- 根据特殊信息，限制 \\omega 的奇偶性等性质。
- 在独立的 \\omega 取值中，一次判断是否满足条件。

比较难算。

2025-05-182026-07-12

[RainPPR](mailto:PPR2125773894@163.com),  [Bot](mailto:bot@noreply.github.com)
