# 解三角形与三角形中的三角函数

## 三角形中的三角函数

条件，在三角形中，有 x+y+z=\\pi（三角形内角和），那么：

### 正切恒等式

#### 形式一

\\tan x+\\tan y+\\tan z=\\tan x\\tan y\\tan z

证明：

\\begin{aligned} \\tan z&=\\tan(\\pi-x-y)=-\\tan(x+y)\\ \\tan z&=-{\\tan x+\\tan y\\over1-\\tan x\\tan y} \\end{aligned}

下面的式子整理即可。

#### 形式二

\\tan{x\\over2}\\tan{y\\over2}+\\tan{y\\over2}\\tan{z\\over2}+\\tan{z\\over2}\\tan{x\\over2}=1

证明：

\\begin{aligned} \\tan{z\\over2}&=\\tan\\left({\\pi\\over2}-{x\\over2}-{y\\over2}\\right)={1\\over\\tan({x\\over2}+{y\\over2})}\\ \\tan{z\\over2}&={1-\\tan{x\\over2}\\tan{y\\over2}\\over\\tan{x\\over2}+\\tan{y\\over2}} \\end{aligned}

下面的式子整理即可。

### 余切恒等式

#### 形式一

\\cot x\\cot y+\\cot y\\cot z+\\cot z\\cot x=1

证明：

根据 \\displaystyle\\tan\\alpha={1\\over\\cot\\alpha} 展开正切的形式一即可。

#### 形式二

\\cot{x\\over2}+\\cot{y\\over2}+\\cot{y\\over2}=\\cot{x\\over2}\\cot{y\\over2}\\cot{y\\over2}

证明：

根据 \\displaystyle\\tan\\alpha={1\\over\\cot\\alpha} 展开正切的形式二即可。

### 一倍角弦

#### 形式一

\\sin x+\\sin y+\\sin z=4\\cos{x\\over2}\\cos{y\\over2}\\cos{z\\over2}

证明：

\\begin{aligned} \\sin x+\\sin y&=2\\sin{x+y\\over2}\\cos{x-y\\over2}\\ &=2\\cos{z\\over2}\\cos{x-y\\over2}\\ \\sin z&=2\\sin{z\\over2}\\cos{z\\over2}\\ &=2\\cos{z\\over2}\\cos{x+y\\over2} \\end{aligned}

然后加起来用和差化积公式即可。

#### 形式二

\\cos x+\\cos y+\\cos z=1+4\\sin{x\\over2}\\sin{y\\over2}\\sin{z\\over2}

证明：

\\begin{aligned} \\cos z&=1-\\sin^2{z\\over2}\\ &=1-\\sin{z\\over2}\\cos{x+y\\over2}\\ \\cos x+\\cos y&=2\\cos{x+y\\over2}\\cos{x-y\\over2}\\ &=2\\sin{z\\over2}\\cos{x-y\\over2} \\end{aligned}

然后加起来用和差化积公式即可。

### 二倍角弦

#### 形式一

\\sin2x+\\sin2y+\\sin2z=4\\sin x\\sin y\\sin z

证明：

\\begin{aligned} \\sin2z&=2\\sin z\\cos z\\ &=-2\\sin z\\cos(x+y)\\ \\sin2x+\\sin2y&=2\\sin(x+y)\\cos(x-y)\\ &=2\\sin z\\cos(x-y) \\end{aligned}

然后加起来用和差化积公式即可。

#### 形式二

\\cos2x+\\cos2y+\\cos2z=-1-\\cos x\\cos y\\cos z

证明：

\\begin{aligned} \\cos2z&=2\\cos^2z-1\\ &=-2\\cos z\\cos(x+y)-1\\ \\cos2x+\\cos2y&=2\\cos(x+y)\\cos(x-y)\\ &=-2\\cos z\\cos(x-y) \\end{aligned}

然后加起来用和差化积公式即可。

## 例题

### 例题一

已知 \\tan\\beta 有意义，且 \\sin(\\alpha+\\beta)={1\\over2}，\\sin(\\alpha-\\beta)={1\\over3}，求 \\dfrac{\\tan\\alpha}{\\tan\\beta}。

S1：和差恒等式

易得：

\\begin{cases} \\sin(\\alpha+\\beta)=\\sin\\alpha\\cos\\beta+\\cos\\alpha\\sin\\beta={1\\over2}\\ \\sin(\\alpha-\\beta)=\\sin\\alpha\\cos\\beta-\\cos\\alpha\\sin\\beta={1\\over3}\\ \\end{cases}

解得：

\\begin{cases} \\sin\\alpha\\cos\\beta={5\\over12}\\ \\cos\\alpha\\sin\\beta={1\\over12}\\ \\end{cases}

易知：

{\\tan\\alpha\\over\\tan\\beta}={\\sin\\alpha\\cos\\beta\\over\\cos\\alpha\\sin\\beta}={{5\\over12}\\over{1\\over12}}=5

S2：和差化积恒等式

易得：

\\begin{cases} \\sin(\\alpha+\\beta)+\\sin(\\alpha-\\beta)=2\\sin\\alpha\\cos\\beta={1\\over2}+{1\\over3}={5\\over6}\\ \\sin(\\alpha+\\beta)-\\sin(\\alpha-\\beta)=2\\cos\\alpha\\sin\\beta={1\\over2}-{1\\over3}={1\\over6} \\end{cases}

易知：

{\\tan\\alpha\\over\\tan\\beta}={2\\sin\\alpha\\cos\\beta\\over2\\cos\\alpha\\sin\\beta}={{5\\over6}\\over{1\\over6}}=5

### 例题二

已知 \\theta\\in\[0,2\\pi) 且 \\sin(x+\\theta) 是偶函数，求 \\theta。

根据偶函数定义：

\\begin{aligned} \\sin(x+\\theta)=\\sin(-x+\\theta)\\ \\sin\\theta\\cos x+\\cos\\theta\\sin x=\\sin\\theta\\cos x-\\cos\\theta\\sin x\\ \\cos\\theta\\sin x=0 \\end{aligned}

因为 x\\in\\mathbb R，所以 \\cos\\theta=0，即： \\displaystyle\\theta={\\pi\\over2}/{3\\pi\\over2}。

知识点：偶函数、和差恒等式。

### 例题三

求函数 \\displaystyle g(x)=\\sin^2\\left(x+{\\pi\\over12}\\right)+\\sin^2\\left(x+{\\pi\\over4}\\right) 的值域。

化简：

\\begin{aligned} &\\sin^2\\left(x+{\\pi\\over12}\\right)+\\sin^2\\left(x+{\\pi\\over4}\\right)\\ =;&{1\\over2}\\left[1-\\cos\\left(2x+{\\pi\\over6}\\right)+1-\\cos\\left(2x+{\\pi\\over2}\\right)\\right]\\ =;&1-{1\\over2}\\left[\\cos\\left(2x+{\\pi\\over6}\\right)+\\cos\\left(2x+{\\pi\\over2}\\right)\\right]\\ =;&1-{1\\over2}\\left({\\sqrt3\\over2}\\cos2x-{1\\over2}\\sin2x-\\sin2x\\right)\\ =;&1+{1\\over4}\\left(3\\sin2x-\\sqrt3\\cos2x\\right)\\ =;&1+{\\sqrt3\\over2}\\sin\\left(2x-{\\pi\\over6}\\right)\\end{aligned}

然后就忒简单了，答案是，函数 g 的值域为 \\displaystyle\\left[1-{\\sqrt3\\over2},1+{\\sqrt3\\over2}\\right]。

知识点：函数、和差恒等式、降次公式、辅助角公式。

另外：最后辅助角公式的应用中，\\arctan b/a 可以不用算出来，因为 x 属于实数域，\\sin 函数里面一定是任何一个实数都取得到，直接取 r=\\sqrt{a^2+b^2}=2\\sqrt3 即可得出答案。

### 例题四

求值：

\\cos20\\degree\\cos40\\degree\\cos80\\degree

答案：

\\begin{aligned} S&=\\dfrac{1}{\\sin20\\degree}\\sin20\\degree\\cos20\\degree\\cdot\\cos40\\degree\\cos80\\degree\\ &=\\dfrac{1}{2\\sin20\\degree}\\sin40\\degree\\cos40\\degree\\cdot\\cos80\\degree\\ &=\\dfrac{1}{4\\sin20\\degree}\\sin80\\degree\\cos80\\degree\\ &=\\dfrac{1}{8\\sin20\\degree}\\sin160\\degree=\\dfrac{1}{8} \\end{aligned}

本质是角的变换。

### 例题五

求值：

\\sin10\\degree+\\dfrac{\\sqrt3}4\\tan10\\degree

答案：

\\begin{aligned} S&=\\dfrac{4\\sin10\\degree\\cos10\\degree+\\sqrt3\\sin10\\degree}{4\\cos10\\degree}\\ &=\\dfrac{2\\sin(30\\degree-10\\degree)+\\sqrt3\\sin10\\degree}{4\\cos10\\degree}\\ &=\\dfrac{\\cos10\\degree}{4\\cos10\\degree}=\\dfrac14 \\end{aligned}

本质也是角的变换。

## 基本方法

### 基本原理

回忆初中平几，根据全等三角形的判断：

如果知道 ASA、AAS、SAS、SSS、HL 就可以唯一的确定一个三角形。

总结一下就是两个角全都可以，三个边可以，一个角两个边就需要是夹角。

即知道 aCb、cBa、bAc，才可以唯一确定一个两边一角的三角形。

至于 SSA，只有一个角是直角才可以唯一确定，不过这个就是 HL 了。

三角形确定，意味着我们可以求出所有边的长度以及所有角度的大小。

正弦定理、余弦定理就为我们提供了方法：可以利用角度和边长互相表示。

像这样，确定三角形边、角的过程，就是解三角形。

如何选择正弦定理、余弦定理？

遇到正弦选正弦定理，遇到齐次式考虑正弦定理。

遇到余弦选余弦定理，遇到边的二次齐次式考虑余弦定理。

原则：边角统一。

### 三角函数

在三角形中，

A+B+C=\\pi

因此就有：

\\begin{aligned} \\sin A&=\\sin(B+C)\\ \\sin B&=\\sin(A+C)\\ \\sin C&=\\sin{A+B} \\end{aligned}

\\begin{aligned} \\cos A&=-\\cos(B+C)\\ \\cos B&=-\\cos(A+C)\\ \\cos C&=-\\cos(A+B) \\end{aligned}

\\begin{aligned} \\sin\\dfrac{A}{2}&=\\cos\\left(\\dfrac{B+C}{2}\\right)\\ \\sin\\dfrac{B}{2}&=\\cos\\left(\\dfrac{A+C}{2}\\right)\\ \\sin\\dfrac{C}{2}&=\\cos\\left(\\dfrac{A+B}{2}\\right) \\end{aligned}

\\begin{aligned} \\cos\\dfrac{A}{2}&=\\sin\\left(\\dfrac{B+C}{2}\\right)\\ \\cos\\dfrac{B}{2}&=\\sin\\left(\\dfrac{A+C}{2}\\right)\\ \\cos\\dfrac{C}{2}&=\\sin\\left(\\dfrac{A+B}{2}\\right) \\end{aligned}

在三角形中，a=b\\cos C+c\\cos B。

若 \\sin^2A+\\sin^2B=\\sin^2C，则该三角形是以 \\angle C 为直角的 \\mathrm{Rt\\triangle}。

解三角形里面常用的奇怪三角函数：

\\sin15^\\circ=\\cos75^\\circ={\\sqrt6-\\sqrt2\\over4}\\[0.5em] \\sin75^\\circ=\\cos15^\\circ={\\sqrt6+\\sqrt2\\over4}

特殊的，如果 \\sin 2A=\\sin 2B，则有 2A=2B 或 2A+2B=\\pi，即 A=B 或 A+B=90^\\circ，即等腰或直角三角形。

### 平面几何法

利用平面几何定理，直接解决。

通常平面几何关注的是角与边的关系。

角，联系三角函数，倒角解决。

边，通常联系正余弦定理，以及一些特殊的定理。

建系法：将数据用坐标表示，详见解析几何。

如果直角三角形三边成等差数列，则变长一定为 3,4,5。

### 向量基底法

用向量基底分解，利用点乘的性质解决。

通常情况下，向量法是一个好用而简洁的方法。

算两次原理：用同一组基底，用不同方式表示一个向量，则系数一定相等。

### 三角形应用

基线：在测量过程中，根据测量的需要而确定的线段叫做基线。

仰角：在同一铅垂平面内，视线在水平线上方时与水平线的夹角。

俯角：在同一铅垂平面内，视线在水平线下方时与水平线的夹角。

方向角：从正北或正南方向到目标方向所形成的小于九十度的角。

方位角：从某点的指北方向线起依顺时针方向到目标方向线之间的水平夹角。

### [TODO] 黄金分割比与黄金三角形

## 三角法定理

### 正弦定理

回顾初中几何，三角形面积，

S={1\\over2}ab\\sin C={1\\over2}bc\\sin A={1\\over2}ac\\sin B

下面的证明过程只考虑锐角三角形，对于钝角三角形，结论不变。

做过 \\angle A 的垂线，则该垂线长度 h：

h=b\\sin C=c\\sin B

对每个角应用，最后可得，

{a\\over\\sin A}={b\\over\\sin B}={c\\over\\sin C}=k

做出该三角形的外接圆，过圆心做 BC 的高，则，

a=2R\\sin A,{a\\over\\sin A}=2R

即值 k 为三角形外接圆直径 2R。

常常这么写：

a=2R\\sin A,b=2R\\sin B,c=2R\\sin C\\ \\sin A={a\\over2R},\\sin B={b\\over2R},\\sin C={c\\over2R}

正弦定理推论：大边对大角，小边对小角。

### 余弦定理

在 \\triangle ABC 中，

\\begin{array}{c} \\overrightarrow{AB}=\\overrightarrow{CB}-\\overrightarrow{CA}\\[0.5em] |\\overrightarrow{AB}|^2=|\\overrightarrow{CB}|^2+|\\overrightarrow{CA}|^2-2|\\overrightarrow{CB}|\\cdot|\\overrightarrow{CA}|\\cdot\\cos\\theta\\[0.5em] c^2=a^2+b^2-2ab\\cos\\theta \\end{array}

其中 \\theta 为 c 的对角，即 \\angle C；第二步就是两边平方。

常写作：

\\cos A={b^2+c^2-a^2\\over2bc},\\cos B={a^2+c^2-b^2\\over2ac},\\cos C={a^2+b^2-c^2\\over2ab}

推论：

\\begin{aligned} a^2+b^2-c^2>0 &\\Longrightarrow \\cos C>0 \\Longrightarrow C\\in(0,\\pi/2)\\ a^2+b^2-c^2=0 &\\Longrightarrow \\cos C=0 \\Longrightarrow C=\\pi/2\\ a^2+b^2-c^2\<0 &\\Longrightarrow \\cos C\<0 \\Longrightarrow C\\in(\\pi/2,\\pi) \\end{aligned}

### 余切定理

\\begin{aligned} \\zeta&=\\sqrt{{1\\over p}(p-a)(p-b)(p-c)}\\ p&={a+b+c\\over2} \\end{aligned}

其中 \\zeta 为 \\triangle ABC 内切圆半径，p 为三角形的半周长。

推论，一各三角形内切圆半径为，

R_内={2S\\over a+b+c}

其中 S 表示三角形面积，a,b,c 分别表示三边长。

### 正切定理

正切定理指出，三角形中，两条边的和与差的比值，等于这两条边的对角的和与差的一半的正切的比值：

{a-b\\over a+b}={\\tan{\\angle A-\\angle B\\over2}\\over\\tan{\\angle A+\\angle B\\over2}}

## 三角形四心

| 编号   | 心的名称 | 定义                   |
| ------ | -------- | ---------------------- |
| X_1(I) | 内心     | 三条**角平分线**的交点 |
| X_2(G) | 重心     | 三条**中线**的交点     |
| X_3(O) | 外心     | 三条**中垂线**的交点   |
| X_4(H) | 垂心     | 三条**高线**的交点     |

### 奔驰定理

在锐角 \\triangle ABC 中，

S\_{\\triangle BOC}\\cdot\\overrightarrow{OA}+S\_{\\triangle AOC}\\cdot\\overrightarrow{OB}+S\_{\\triangle AOB}\\cdot\\overrightarrow{OC}=\\vec0

推论：

- 设 I 为内心，则 a\\cdot\\overrightarrow{IA}+b\\cdot\\overrightarrow{IB}+c\\cdot\\overrightarrow{IC}=\\vec0.
- 设 H 为垂心，则 \\tan A\\cdot\\overrightarrow{HA}+\\tan B\\cdot\\overrightarrow{HB}+\\tan C\\cdot\\overrightarrow{HC}=\\vec0.
- 设 O 为外心，则 \\sin2A\\cdot\\overrightarrow{OA}+\\sin2B\\cdot\\overrightarrow{OB}+\\sin2C\\cdot\\overrightarrow{OC}=\\vec0.

### 欧拉线定理

- 欧拉定理：O,I 分别为外接圆、内切圆圆心，则有 OI^2=R^2-2Rr.

- 欧拉线定理：三角形的外心 O，垂心 H，重心 G 依次位于同一直线上，且重心到外心的距离是重心到垂心的距离的一半，即

  \\overrightarrow{OG}=\\frac{1}{3}\\overrightarrow{OH}=\\frac{1}{3}(\\overrightarrow{OA}+\\overrightarrow{OB}+\\overrightarrow{OC})

### 极化恒等式

一般形式：

- 已知平面上非零向量 \\boldsymbol{a} 与 \\boldsymbol{b}，则 \\boldsymbol{a} \\cdot \\boldsymbol{b} = \\dfrac{1}{4}(|\\boldsymbol{a} + \\boldsymbol{b}|^2 - |\\boldsymbol{a} - \\boldsymbol{b}|^2)。
- 在 \\triangle ABC 中，若 M 是 BC 的中点，则 \\overrightarrow{AB} \\cdot \\overrightarrow{AC} = |\\overrightarrow{AM}|^2 - \\dfrac{1}{4}|\\overrightarrow{BC}|^2。

在 \\triangle ABC 中，对于共起点的数量积 \\overrightarrow{AB} \\cdot \\overrightarrow{AC} 的求解问题，我们首先想到的是找出 BC 的中点 M，则

\\overrightarrow{AM} = \\dfrac{1}{2}(\\overrightarrow{AB} + \\overrightarrow{AC})

所以

\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = \\left[\\dfrac{1}{2}(\\overrightarrow{AB} + \\overrightarrow{AC})\\right]^2 - \\dfrac{1}{4}|\\overrightarrow{BC}|^2

化简整理便可得到如下结论：在 \\triangle ABC 中，

2\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = |\\overrightarrow{AB}|^2 + |\\overrightarrow{AC}|^2 - |\\overrightarrow{BC}|^2

任何事物都是由特殊再到一般，我们研究平面几何问题更多的是在研究三角形，因为三角形是我们接触最多也是最熟悉的，然后由三角形再延伸到四边形问题。那么对于向量余弦式是否也可以延伸到四边形呢？我们知道四边形通过对角线是可以分割成三角形的，下面一起来探讨这个问题。在平面四边形 ABCD 中，它可以由 \\triangle ABC 与 \\triangle ACD 组成，则在 \\triangle ABC 中，由向量余弦式可得

\\overrightarrow{AB} \\cdot \\overrightarrow{AC} = \\dfrac{|\\overrightarrow{AB}|^2 + |\\overrightarrow{AC}|^2 - |\\overrightarrow{BC}|^2}{2}

那么在 \\triangle ACD 中，则向量余弦式可得

\\overrightarrow{AD} \\cdot \\overrightarrow{AC} = \\dfrac{|\\overrightarrow{AD}|^2 + |\\overrightarrow{AC}|^2 - |\\overrightarrow{DC}|^2}{2}

两式相减可得

\\overrightarrow{AD} \\cdot \\overrightarrow{AC} - \\overrightarrow{AB} \\cdot \\overrightarrow{AC} = \\dfrac{|\\overrightarrow{AD}|^2 + |\\overrightarrow{AC}|^2 - |\\overrightarrow{DC}|^2}{2} - \\dfrac{|\\overrightarrow{AB}|^2 + |\\overrightarrow{AC}|^2 - |\\overrightarrow{BC}|^2}{2}

整理后可得

\\overrightarrow{AC} \\cdot \\overrightarrow{BD} = \\dfrac{|\\overrightarrow{AD}|^2 + |\\overrightarrow{BC}|^2 - |\\overrightarrow{AB}|^2 - |\\overrightarrow{CD}|^2}{2}

这就得到了平面四边形的向量余弦式的形式。

在四边形 ABCD 中，

\\overrightarrow{AC} \\cdot \\overrightarrow{BD} = \\dfrac{|\\overrightarrow{AD}|^2 + |\\overrightarrow{BC}|^2 - |\\overrightarrow{AB}|^2 - |\\overrightarrow{CD}|^2}{2}

这个结论也称之为对角线定理，它不仅仅可以在平面四边形中得到应用，还可以推广到空间四边形的情形。

### 分点的向量方程

特殊的，中点的向量方程：

\\vecc{AD}=\\dfrac12\\vecc{AB}+\\dfrac12\\vecc{AC}

交叉定理

即对边比例相乘向量相加。

### 重心及其性质

重心：三角形三边中线交点，在平面直角坐标系中，重心的坐标是顶点坐标的算术平均，也就是说对于平面内任意一点 P：

\\vecc{PG}=\\dfrac13\\left(\\vecc{PA}+\\vecc{PB}+\\vecc{PC}\\right)

重心和三角形任意两个顶点组成的三个三角形面积相等，而重心到三条边的距离与三条边的长成反比。

根据奔驰定理，有三角形重心到其各个顶点向量之和为零。

\\vecc{GA}+\\vecc{GB}+\\vecc{GC}=\\vec 0

特性：一个三角形的重心同时也是其中点三角形的重心，中位线证明。

根据是中线的性质，做 AG 并延长交 BC 于点 H，则：

\\dfrac{AG}{GH}=\\dfrac21

特殊的，重心到三边距离之积最大、到三角形三个顶点距离的平方和最小。

### 内心及其性质

内心为三角形内切圆圆心，因此为三个角的角平分线交点：

\\vecc{AI}=\\lambda\\left(\\dfrac{\\vecc{AB}}{|\\vecc{AB}}+\\dfrac{\\vecc{AC}}{|\\vecc{AC}|}\\right)

有奔驰定理的形式：

\\sin A\\cdot\\vecc{IA}+\\sin B\\cdot\\vecc{IB}+\\sin C\\cdot\\vecc{IC}=\\vec 0

三角形的内心到边的距离（即内切圆的半径）与三边长及面积之间有关系：

r_内=\\dfrac{2S}{a+b+c}=\\dfrac{2S}{C}

可以连接内心与三顶点，等面积法求解。

### 外心及其性质

外心为三角形外接圆圆心，因此为三边中垂线交点，不一定在三角形内部，到三角形三点距离相等。

\\vecc{OA}^2=\\vecc{OB}^2=\\vecc{OC}^2

有奔驰定理的形式：

\\sin2A\\cdot\\vecc{OA}+\\sin2B\\cdot\\vecc{OB}+\\sin2C\\cdot\\vecc{OC}=\\vec 0

而，

R_外={abc\\over4S}

- 当三角形为锐角三角形时，外心在三角形内部。
- 当三角形为钝角三角形时，外心在三角形外部。
- 当三角形为直角三角形时，外心在斜边的中点上。

锐角三角形外心到三边距离之和等于 R+r。

证明：等价于证

R(\\cos A+\\cos B+\\cos C)=R+r

我们知道

\\begin{aligned} S\_{\\Delta ABC}&=\\frac{1}{2}(a+b+c)r\\ &=S\_{\\Delta OAB}+S\_{\\Delta OAC}+S\_{\\Delta OBC}\\ &=\\frac{1}{2}R(a\\cos A+b\\cos B+c\\cos C) \\end{aligned}

联立上两式（相乘），直接展开易知等式成立。

### 垂心及其性质

垂心是三角形三边垂线的交点，因此有点积为零。

\\vecc{HA}\\cdot{BC}=\\vecc{HB}\\cdot\\vecc{AC}=\\vecc{HC}\\cdot\\vecc{AB}=0

两两整理，得到：

\\vecc{HA}\\cdot\\vecc{HB}=\\vecc{HB}\\cdot\\vecc{HC}=\\vecc{HC}\\cdot\\vecc{HA}

有奔驰定理的形式：

\\tan A\\cdot\\vecc{HA}+\\tan B\\cdot\\vecc{HB}+\\tan C\\cdot\\vecc{HC}=\\vec 0

而垂心到三角形一顶点距离等于此三角形外心到此顶点对边距离的 2 倍。

三角形外心 O、重心 G、垂心 H 三点共线且 OG:GH=1:2 此直线称为三角形的欧拉线。

## 三角形三线

### 中线长定理

在 \\triangle ABC 中，BC 的中点为 M，对于中线 AM，有：

AM^2={1\\over2}b^2+{1\\over2}c^2-{1\\over4}a^2

或，

AM^2+BM^2={1\\over2}(AC^2+AB^2)

或，

AM={1\\over2}\\sqrt{2b^2+2c^2-a^2}

证明，基底分解：

\\overrightarrow{AM}={1\\over2}\\overrightarrow{AB}+{1\\over2}\\overrightarrow{AC}\\[0.5em] \\overrightarrow{BM}={1\\over2}\\overrightarrow{AC}-{1\\over2}\\overrightarrow{AB}

则，

|\\overrightarrow{AM}|^2+|\\overrightarrow{BM}|^2={1\\over2}|\\overrightarrow{AB}|^2+{1\\over2}|\\overrightarrow{AC}|^2

或者中点两个底角分别列余弦定理，相加化简。

### 分角定理

在 \\triangle ABC 中，BC 上有一点 M，则：

{BM\\over CM}={AB\\sin\\angle BAM\\over AC\\sin\\angle CAM}

证明，左右两边等面积法：

{BM\\over CM}={S\_{\\triangle ABM}\\over S\_{\\triangle ACM}}={AB\\cdot AM\\sin\\angle BAM\\over AC\\cdot AM\\sin\\angle CAM}={AB\\sin\\angle BAM\\over AC\\sin\\angle CAM}

或正弦定理：

{BM\\over\\sin\\angle BAM}={AB\\over\\sin\\angle AMB}\\[0.5em] {CM\\over\\sin\\angle CAM}={AC\\over\\sin\\angle AMC}

上下做比。

### 角平分线定理

在 \\triangle ABC 中，\\angle A 的平分线 AM，有：

{BM\\over CM}={AB\\over AC}

是分角定理的直接推论。

### 角平分线长定理

\\begin{aligned} AD&=\\sqrt{AB\\cdot AC-BD\\cdot CD}\\ &=\\sqrt{bc\\left(1-{a^2\\over(b+c)^2}\\right)}\\ &={2bc\\over b+c}\\cos{A\\over2} \\end{aligned}

## 边长公式

### 射影定理

射影定理表示为：

a=b\\cos C+c\\cos B

在初中我们学习过影高乘积等于树高平方的射影定理。

在 \\triangle ABC 中 BC 上的高为 AD，则：

AB^2=BD\\cdot BC

AD^2=BD\\cdot CD

AC^2=BC\\cdot CD

### 斯图尔特定理

又译斯台沃特定理，在 \\triangle ABC 边 BC 上任意一点 D，

AB^2\\cdot CD+AC^2\\cdot BD-AD^2\\cdot BC=BD\\cdot CD\\cdot BC

可以由两次余弦定理推导得出。

### 平行四边形恒等式

AB^2+BC^2+CD^2+AD^2=AC^2+BD^2

对于一般的四边形，等式不成立，但是有不等式：

AB^2+BC^2+CD^2+AD^2\\ge AC^2+BD^2

或者设 x 表示两条对角线中点所连线段的长度：

AB^2+BC^2+CD^2+AD^2=AC^2+BD^2+4x^2

注意到平行四边形对角线互相平分，即 x=0，可得上面的第一个恒等式。

### 边元塞瓦定理

赛瓦定理

其逆定理用于表示三角形内三点共线，角元塞瓦定理较为复杂。

### 梅涅劳斯定理

一直线与 \\triangle ABC 的三边 AB,BC,AC 或他们的延长线分别交于 X,Y,Z 三点，则：

\\dfrac{AX}{XB}\\cdot\\dfrac{BY}{YC}\\cdot\\dfrac{CZ}{ZA}=0

梅涅劳斯定理

梅涅劳斯定理的逆定理表示为，满足上述式子，则 X,Y,Z 三点共线。

## 面积公式

### 海伦公式

任意三角形面积可以表示为：

\\begin{aligned} S&=\\sqrt{p(p-a)(p-b)(p-c)}\\ p&={a+b+c\\over2} \\end{aligned}

即：

S=\\dfrac14\\sqrt{(a+b+c)(a+b-c)(a-b+c)(-a+b+c)}

其中 p 为三角形的半周长。

### 布雷特施奈德公式

任意四边形面积可以表示为：

\\begin{aligned} S&=\\sqrt{(p-a)(p-b)(p-c)(p-d)-abcd\\cos^2{\\alpha+\\beta\\over2}}\\ p&={a+b+c+d\\over2} \\end{aligned}

其中 p 为四边形的半周长，\\alpha,\\beta 为其中二个对角。

布雷特施奈德公式可视为婆罗摩笈多公式之推广。

### 婆罗摩笈多公式

注意到圆内接四边形对角互补，其半角余弦值为零，\\cos90^\\circ=0 则圆内接四边形面积可以简化为：

\\begin{aligned} S&=\\sqrt{(p-a)(p-b)(p-c)(p-d)}\\ p&={a+b+c+d\\over2} \\end{aligned}

其中 p 为四边形的半周长。

## 解三角形例题

### 例题一

2\\cos^2{B\\over2}+\\sqrt3\\sin B=3

- 求 B.

\\cos B=2\\cos^2{B\\over2}-1\\ \\cos B+\\sqrt3\\sin B=2\\ {\\sqrt3\\over2}\\sin B+{1\\over2}\\cos B=1\\ \\sin B\\cos30^\\circ+\\cos B\\sin30^\\circ=1\\ \\sin(B+30^\\circ)=1=\\sin90^\\circ\\ B=60^\\circ

### 例题二

(\\sin B-\\sin C)^2=\\sin^2 A-\\sin B\\sin C

- 求 A.
- 若 \\sqrt2a + b= 2c，求 C.

观察到是角的二次齐次式，且都是正弦，考虑正弦定理，

(\\sin B-\\sin C)^2=\\sin^2 A-\\sin B\\sin C\\\\ (b-c)^2=a^2-bc\\\\ b^2+c^2-2bc=a^2-bc\\\\ a^2=b^2+c^2-bc

于是，

\\cos A={b^2+c^2-a^2\\over2bc}={1\\over2}\\\\ A=60^\\circ

观察到 \\sqrt2a + b= 2c 为边的一次齐次，考虑用正弦定理。

\\sqrt2a+b=2c\\\\ \\sqrt2\\sin A+\\sin B=2\\sin C

根据上一问，\\sin A=\\sin60^\\circ=\\sqrt3/2，

\\sqrt6/2+\\sin B=2\\sin C\\\\ \\sqrt6/2+\\sin(120-C)=2\\sin C\\\\ \\sqrt6/2+\\sqrt3/2\\cos C+\\sin C/2=2\\sin C

继续整理，

{\\sqrt6\\over2}+{\\sqrt3\\over2}\\cos C+{1\\over2}\\sin C=2\\sin C\\\\ {3\\over2}\\sin C-{\\sqrt3\\over2}\\cos C={\\sqrt6\\over2}\\\\ {\\sqrt3\\over2}\\sin C-{1\\over2}\\cos C={\\sqrt2\\over2}\\\\ \\sin C\\cos30^\\circ-\\cos C\\sin30^\\circ={\\sqrt2\\over2}\\\\ \\sin(C-30^\\circ)={\\sqrt2\\over2}=\\sin45^\\circ

因为 C \\in (0^\\circ,120 ^\\circ)，C-30^\\circ\\in(-30^\\circ,90^\\circ)，因此，

C-30^\\circ=45^\\circ,\\ C=75^\\circ

### 例题三

在锐角 \\triangle ABC 中，

2b\\sin A-\\sqrt3a=0

- 求 B.
- 求 \\cos A+\\cos B+\\cos C 的取值范围。

不考虑 \\sin A 是边的二次齐次式，于是应用正弦定理，

2\\sin B\\sin A-\\sqrt2\\sin A=0\\\\ 2\\sin B=\\sqrt3\\ \\sin B=\\sqrt3/2

因为 \\angle B 是锐角，

B=60^\\circ

设，

\\def\\degree{^\\circ} \\begin{aligned} S&=\\cos A+\\cos B+\\cos C\\ &=\\cos A+\\cos C+1/2\\ &=\\cos(120\\degree-C)+\\cos C+1/2\\ &=-{1\\over2}\\cos C+{\\sqrt3\\over2}\\sin C+\\cos C+{1\\over2}\\ &={\\sqrt3\\over2}\\sin C+{1\\over2}\\cos C+{1\\over2}\\ &=\\sin C\\cos30\\degree+\\cos C\\sin30\\degree +1/2\\ &=\\sin(C+30\\degree)+1/2 \\end{aligned}

因为 0^\\circ\<A,B,C\<90^\\circ，

\\def\\degree{^\\circ} \\begin{cases} 0\\degree\<&C&\<90\\degree\\ 0\\degree\<&B&\<90\\degree \\end{cases} \\Longleftrightarrow \\begin{cases} 0\\degree\<&C&\<90\\degree\\ 0\\degree\<&120-C&\<90\\degree \\end{cases}

即，30^\\circ\<C\<90^\\circ，60^\\circ\<C+30^\\circ\<120^\\circ。

画出单位圆，易得 \\sin(C+30\\degree)\\in(\\sqrt3/2,1\]，即，

\\cos A+\\cos B+\\cos C\\in\\left({\\sqrt3+1\\over2},{3\\over2}\\right\]

### 例题四

在 \\triangle ABC 中，a+b=11，

\\cos A={1\\over8},\\cos B={9\\over16}

- 求 a,b。

考虑余弦转正弦，因为是三角形的角，因此正弦值非负，

\\sin A=\\sqrt{1-\\cos^2 A}=\\sqrt{63\\over64}={3\\sqrt7\\over8}\\ \\sin B=\\sqrt{1-\\cos^2 B}=\\sqrt{175\\over256}={5\\sqrt7\\over16}

{a\\over b}={\\sin A\\over\\sin B}={6\\over5}

因此 a=6,b=5。

### 例题五

{\\sin A\\over\\sin B-\\sin C}={b+c\\over b-a}

- 求 \\cos C。

考虑 \\cos C 可以怎么表示，可以通过 \\sin C 用毕达哥拉斯定理，也可以余弦定理。

考虑到这个原形式是一次齐次，因此考虑角化变。

{a\\over b-c}={b+c\\over b-a}\\ b^2-c^2=ab-a^2\\ c^2=a^2+b^2-ab

因此，

\\cos C={a^2+b^2-c^2\\over2bc}={1\\over2}

### 例题六

若，

\\begin{cases} \\sin A=3\\sin B\\ c=\\sqrt5\\ \\cos C=5/6 \\end{cases}

- 求 a。

尝试考虑这三个东西各自什么用。

最容易发现第二个式子最简单，可以最后带入用。

因为 \\cos 关于余弦定理，关于边数多，因此考虑后用。

第一个式子结构很好，是一次齐次，因此带入第一个正弦定理。

a=3b

又因为，

\\cos C={a^2+b^2-c^2\\over2ab}

带入即可，解得 a=3。

### 例题七

若，

\\begin{cases} b\\sin2A=a\\sin B\\ c=2b \\end{cases}

- 求 a/b。

考虑到第二个式子的形式很简单，因此用于消元。

第一个形式中，出现了二倍角，是不好处理的，因此考虑正弦定理。

\\sin B\\sin2A=\\sin A\\sin B\\ \\sin A=\\sin2A\\ \\sin A=2\\sin A\\cos A\\ \\cos A=1/2

考虑到 a/b 是一个一次其次的比例式，因此余弦定理，

\\cos A={b^2+c^2-a^2\\over2bc}

带入，解得 a^2=3b^2，即 a/b=\\sqrt3。

### 例题八

在 \\triangle ABC 中，

S=a^2-(b-c)^2

求 \\sin A。

这个式子没有很好的性质，考虑展开，

S=a^2-b^2-c^2+2bc

注意到这个形式，而且还是二次齐次式，根据余弦定理，

a^2=b^2+c^2-2bc\\cos A

有，

S=2bc(1-\\cos A)={1\\over2}bc\\sin A\\ \\sin A=4-4\\cos A

联立得方程，

(4-4\\cos A)^2+\\cos^2A=1\\ 16(1-\\cos A)^2=(1-\\cos A)(1+\\cos A)\\ 16-16\\cos A=1+\\cos A\\ \\cos A={15\\over17}, \\sin A={8\\over17}

### 例题九

在 \\triangle ABC 中，

\\sin A=2\\sin B\\cos C\\ a^2=b^2+c^2-bc

- 求，\\triangle ABC 形状。

两个式子都很典型，第二个好说，先处理，

联立二式及余弦定理，

a^2=b^2+c^2-bc\\ a^2=b^2+c^2-2bc\\cos A

得，

\\cos A={1\\over2},A=60^\\circ

第一个式子，可以不带入 A，尝试通过三角函数的变换，

\\begin{aligned} \\sin A&=\\sin(\\pi-B-C)=\\sin(B+C)\\ &=\\sin B\\cos C+\\cos B\\sin C \\end{aligned}

联立下式及一式，

\\sin B\\cos C+\\cos B\\sin C=2\\sin B\\cos C\\ \\sin B\\cos C=\\cos B\\sin C\\ \\tan B=\\tan C

因为 B,C\\in(0,\\pi)，正切函数在此范围内唯一，则

B=C=A=60^\\circ

即 \\triangle ABC 是正三角形。

### 例题十

在 \\triangle ABC 中，

\\cos(2B+C)+\\cos C>0

- 判断三角形是锐角、直角、钝角三角形。

容易发现，\\cos 里面的角有很好的性质，考虑和差化积，

\\begin{aligned} &\\cos(2B+C)+\\cos C\\ =;&2\\cos(B+C)\\cos B\\ =;&-2\\cos A\\cos B>0 \\end{aligned}

因此，

\\cos A\\cos B\<0

即 A,B 中有一个钝角，即 \\triangle ABC 为钝角三角形。

### 例题十一

在 \\triangle ABC 中，三边长分别为 a,a+2,a+4，最小角余弦值为 13/14。

- 求该三角形的面积

因为大边对大角，因此最小角是 a 对的，

\\cos A={(a+2)^2+(a+4)^2-a^2\\over2(a+2)(a+4)}={13\\over14}

解得，a=3，于是用海伦公式，

p={3+5+7\\over2}={15\\over2}

S=\\sqrt{{15\\over2}\\cdot{9\\over2}\\cdot{5\\over2}\\cdot{1\\over2}}={15\\sqrt3\\over4}

### 例题十二

在 \\triangle ABC 中，\\angle A=120^\\circ，BC=6。

- 求：其面积最大值。

考虑面积可以怎么表示。

Solution 1:

S={1\\over2}bc\\sin A={\\sqrt3\\over4}bc

根据余弦定理，

36=a^2=b^2+c^2-2bc\\cos A=b^2+c^2+bc\\ge3bc

即，

bc\\le12,S\\le3\\sqrt3

Solution 2:

考虑到顶角不变，则可以固定底边，使顶点移动。

易知其轨迹为一个圆弧，则面积最大即底边高线最大。

高线最大即该三角形为等腰三角形，做出高线，

S={1\\over2}ah=3\\sqrt3

### 例题十三

在 \\triangle ABC 中，若

a-b=c(\\cos B-\\cos A)

- 判断其形状。

考虑到余弦定理展开后是三次式，有点复杂，因此正弦定理。

\\sin A-\\sin B=\\sin C\\cos B-\\sin C\\cos A

考虑凑项，右边的两项很像正弦的和角公式，于是，

\\begin{aligned} &\\sin(B+C)-\\sin(A+C)\\ =;&\\sin B\\cos C+\\sin C\\cos B-\\sin A\\cos C-\\sin C\\cos A\\ =;&\\sin C\\cos B-\\sin C\\cos A \\end{aligned}

化简，

(\\sin B-\\sin A)\\cos C=0

即 \\sin A=\\sin B 或 \\cos C=0，

即 \\triangle ABC 为等腰三角形或直角三角形。

### 例题十四

若 \\triangle ABC 中，\\angle C 为钝角，且其面积，

S={\\sqrt3\\over4}(a^2+c^2-b^2)

- 求 \\angle B。

考虑到 a^2+c^2-b^2 是经典掉牙的形式，

\\cos B={a^2+c^2-b^2\\over2ac}

于是，

S={\\sqrt3\\over4}\\cdot2ac\\cos B={\\sqrt3\\over2}ac\\cos B

考虑很经典的面积公式，

S={1\\over2}ac\\sin B={\\sqrt3\\over2}ac\\cos B\\ \\sin B=\\sqrt3\\cos B\\ \\tan B=\\sqrt3,B=60^\\circ

### 例题十五

在 \\triangle ABC 中，

\\sin^2A-\\sin^2B-\\sin^2C=\\sin B\\sin C

- 求 A.
- 若 BC=3，求其周长最大值。

因为是正弦的二次齐次式，考虑正弦定理，

a^2=b^2+c^2+bc

于是 \\angle A=120^\\circ。

考虑周长最大，即 b+c 最大，

a^2=9=b^2+c^2+bc\\ge3bc\\ bc\\le3

考虑周长如何建立联系

b+c=\\sqrt{b^2+c^2+2bc}=\\sqrt{9+bc}\\le2\\sqrt3

即周长，

a+b+c\\le2\\sqrt3+3

### 例题十六

在 \\triangle ABC 中，

\\sin A+2\\sin B\\cos C=0\\ c=\\sqrt3b

- 求 \\tan A。

考虑到第二个很适合消元 c，于是第一个式子可以看成一次齐次，

a+2b\\cos C=0\\ \\cos C=-{a\\over2b}={a^2+b^2-c^2\\over2bc}={a^2-2b^2\\over2bc}

因此，

a^2=b^2\\ a=b

因为 c=\\sqrt3b，这是一个 30^\\circ,30^\\circ,120^\\circ 的等腰三角形，

\\tan A=\\tan30^\\circ={\\sqrt3\\over3}

### 例题十七

在 \\triangle ABC 中，

a^2+b^2=2022c^2

求，

{2\\tan A\\tan B\\over\\tan C(\\tan A+\\tan B)}

考虑到没有什么好玩的结构，因此展开正切。

\\begin{aligned} S&={2\\tan A\\tan B\\over\\tan C(\\tan A+\\tan B)}\\ &={2\\sin A\\sin B\\over\\sin C/\\cos C\\cdot(\\sin A\\cos B+\\cos A+\\sin B)}\\ &={2\\sin A\\sin B\\cos C\\over\\sin^2C} \\end{aligned}

考虑到上下正弦构成二次齐次，正弦定理，

\\begin{aligned} S&={2\\sin A\\sin B\\cos C\\over\\sin^2C}\\ &={2ab\\cos C\\over c^2} \\end{aligned}

注意到 2ab 和 \\cos C 的余弦定理的分母类似，

\\cos C={a^2+b^2-c^2\\over2ab}

\\begin{aligned} S&={a^2+b^2-c^2\\over c^2}={a^2+b^2\\over c^2}-1\\ &=2022-1=2021 \\end{aligned}

### 例题十八

在锐角三角形 ABC 中，a^2-b^2=bc。

求证：A=2B。

经典题，因为角不好表示，上式又是边的二次齐次式，考虑，

\\cos A={b^2+c^2-a^2\\over2bc}={c^2-bc\\over2bc}={c-b\\over2b}\\

\\begin{aligned} \\cos 2B&=2\\cos^2B-1=2\\left({a^2+c^2-b^2\\over2ac}\\right)^2-1\\ &=2\\left({c+b\\over2a}\\right)^2-1={2c^2+2b^2+4bc-4a^2\\over4a^2}\\ &={2c^2-2b^2\\over4b^2+4bc}={2(c+b)(c-b)\\over4b(b+c)}={c-b\\over2b} \\end{aligned}

于是，

(\\cos A=\\cos2B)\\Longrightarrow(A=2B)

2025-07-212026-07-05

[RainPPR](mailto:PPR2125773894@163.com),  [Bot](mailto:bot@noreply.github.com),  [RaineMtF](mailto:192512683+RaineMtF@users.noreply.github.com),  [Copilot](mailto:198982749+Copilot@users.noreply.github.com),  [google-labs-jules[bot]](mailto:161369871+google-labs-jules%5Bbot%5D@users.noreply.github.com)
