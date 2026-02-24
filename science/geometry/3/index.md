# 圆锥曲线 {#_1}

## 椭圆 {#_2}

### 第一定义 {#_3}

到两个定点 [\$F_1\$]{.arithmatex}、[\$F_2\$]{.arithmatex} 的距离之和为定值（大于 [\$\|F_1F_2\|\$]{.arithmatex}）的点所形成的轨迹称为椭圆。这两个定点叫做椭圆的焦点，两焦点间的距离叫做椭圆的焦距，焦距的一半称为半焦距。

我们不妨设 [\$F_1=(-c,0),F_2=(c,0)\$]{.arithmatex} 为焦点的椭圆经过 [\$M\$]{.arithmatex} 点，且 [\$M\$]{.arithmatex} 到 [\$F_1,F_2\$]{.arithmatex} 的局里之和为 [\$2a\$]{.arithmatex}，其中 [\$a\>c\$]{.arithmatex}，那么写出方程：

::: {.arithmatex}
\$\$ \sqrt{(x-c)\^2+y\^2}+\sqrt{(x+c)\^2+y\^2}=2a \$\$
:::

我们把一个根号移到另一侧，然后两边平方，整理后再平方，可以得到：

::: {.arithmatex}
\$\$ \dfrac{x\^2}{a\^2}+\dfrac{y\^2}{a\^2-c\^2}=1 \$\$
:::

不妨令 [\$b=\sqrt{a\^2-c\^2}\$]{.arithmatex}，那么**椭圆的标准方程**：

::: {.arithmatex}
\$\$ \dfrac{x\^2}{a\^2}+\dfrac{y\^2}{b\^2}=1(a\>b\>0) \$\$
:::

这个椭圆的焦点在 [\$x\$]{.arithmatex} 轴上，容易知道焦点在 [\$y\$]{.arithmatex} 轴上的椭圆

::: {.arithmatex}
\$\$ \dfrac{x\^2}{b\^2}+\dfrac{y\^2}{a\^2}=1(a\>b\>0) \$\$
:::

注意 [\$c\^2=a\^2-b\^2\$]{.arithmatex} 这个式子很重要。

### 第二定义 {#_4}

到一定点 [\$F_1\$]{.arithmatex} 的距离与到一定直线的距离之比为定值（小于 [\$1\$]{.arithmatex}）的点所形成的轨迹称为椭圆。该定直线称为准线。

我们不妨设 [\$F_1=(c,0),F_2=(-c,0)\$]{.arithmatex}，同样还有一个 [\$a\$]{.arithmatex} 那么：

::: {.arithmatex}
\$\$ \sqrt{(x-c)\^2+y\^2}+\sqrt{(x+c)\^2+y\^2}=2a \$\$
:::

不妨写出这个式子的共轭根式，

::: {.arithmatex}
\$\$ \sqrt{(x-c)\^2+y\^2}-\sqrt{(x+c)\^2+y\^2}=\dfrac{2cx}{a} \$\$
:::

容易知道他们的乘积就是 [\$4cx\$]{.arithmatex}，因此写出其共轭根式为上式，联立两式，不难得到

::: {.arithmatex}
\$\$ \sqrt{(x-c)\^2+y\^2}=\dfrac{c}{a}\vert{x-\dfrac{a\^2}{c}} \$\$
:::

容易知道准线方程为

::: {.arithmatex}
\$\$ x=\dfrac{a\^2}{c} \$\$
:::

因为我们是取的右焦点，因此这个准线也称为右准线；同理取左焦点

::: {.arithmatex}
\$\$ x=-\dfrac{a\^2}{c} \$\$
:::

称为左准线，而比值就是 [\$\dfrac{c}{a}\$]{.arithmatex}，这称为离心率：

::: {.arithmatex}
\$\$ e=\dfrac{c}{a}=\sqrt{1-\dfrac{b\^2}{a\^2}}\in(0,1) \$\$
:::

特别的，圆的离心率为零；离心率越大，椭圆越扁平。

### 第三定义 {#_5}

第三定义是关于斜率的一种定义，其由两种形式，因为常见做法通常是点差法，因此有的时候也直接称为点差法。设椭圆

::: {.arithmatex}
\$\$ C:\dfrac{x\^2}{a\^2}+\dfrac{y\^2}{b\^2}=1 \$\$
:::

1.  在 [\$C\$]{.arithmatex} 上有一点 [\$P\$]{.arithmatex}（除左右顶点 [\$A,B\$]{.arithmatex} 外） ，则

    ::: {.arithmatex}
    \$\$ k\_{PA}\cdot k\_{PB}=-\dfrac{b\^2}{a\^2}=e\^2-1 \$\$
    :::

2.  在 [\$C\$]{.arithmatex} 上有两点 [\$P,Q\$]{.arithmatex}，[\$M\$]{.arithmatex} 为 [\$PQ\$]{.arithmatex} 重点，则

    ::: {.arithmatex}
    \$\$ k\_{OM}\cdot k\_{PQ}=-\dfrac{b\^2}{a\^2}=e\^2-1 \$\$
    :::

证明可以用点差法，即设处两点坐标，做差得到直线斜率。这类关于中点、斜率的问题通常可以用点差法，同时因为是椭圆的一条弦与它的中点，我们也称其为中点弦问题。

点差法

不妨设

::: {.arithmatex}
\$\$ P(x_1,y_1),Q(x_2,y_2) \$\$
:::

因此

::: {.arithmatex}
\$\$ \begin{cases} \dfrac{x_1\^2}{a\^2}+\dfrac{y_1\^2}{b\^2}&=1\\ \dfrac{x_2\^2}{a\^2}+\dfrac{y_2\^2}{b\^2}&=1 \end{cases} \$\$
:::

做差，得到

::: {.arithmatex}
\$\$ (x_1-x_2)\cdot\dfrac{x_1+x_2}{a\^2}+(y_1-y_2)\cdot\dfrac{y_1+y_2}{b\^2}=0 \$\$
:::

根据中点

::: {.arithmatex}
\$\$ \begin{cases} x_1+x_2&=2x_M\\ y_1+y_2&=2y_M \end{cases} \$\$
:::

因此

::: {.arithmatex}
\$\$ (x_1-x_2)\cdot\dfrac{x_M}{a\^2}+(y_1-y_2)\cdot\dfrac{y_M}{b\^2} \$\$
:::

又因为斜率

::: {.arithmatex}
\$\$ k=\dfrac{y_1-y_2}{x_1-x_2} \$\$
:::

因此就有

::: {.arithmatex}
\$\$ \dfrac{x_M}{a\^2}+k\cdot\dfrac{y_M}{b\^2}=0 \$\$
:::

整理可得出两个结论。

在点差法的使用过程中一定要注意检验，首先是涉及到斜率不存在的问题，其次是我们设出直线与圆锥曲线交于两点，前提是要有两个焦点，即要验证求出来的斜率能否使得 [\$\Delta\>0\$]{.arithmatex} 的问题。

同时，我们也可以根据仿射变换轻松得到，这将其视为一种变换。

### 几何性质 {#_6}

椭圆有两条对称轴（两个坐标轴）和一个对称中心（原点）。

::: {.arithmatex}
\$\$ \dfrac{x\^2}{a\^2}+\dfrac{y\^2}{b\^2}=1(a\>b\>0) \$\$
:::

我们注意到，

::: {.arithmatex}
\$\$ x\^2=a\^2\paren{1-\dfrac{y\^2}{b\^2}} \$\$
:::

因此

::: {.arithmatex}
\$\$ -a\le x\le a \$\$
:::

同理

::: {.arithmatex}
\$\$ -b\le y\le b \$\$
:::

也就是说，椭圆整个图形都在一个中心在原点、长为 [\$b\$]{.arithmatex} 高为 [\$a\$]{.arithmatex} 的矩形中心，矩形与椭圆焦点分为上下左右四个。

- 椭圆的面积：[\$S=\pi ab\$]{.arithmatex}（[\$a,b\$]{.arithmatex} 分别为长半轴、短半轴的长）。

  证明：根据仿射变换显然。或利用微积分，此处略。

- 椭圆的周长是一个没有答案的问题，历史上许多伟大的数学家，如拉马努金，都提出了非常精确的近似公式来估算椭圆周长，但它们都只是近似，无法得到精确的有理数结果。现代我们知道可以用第二类完全椭圆积分来表示，但这对高中数学便没有任何意义了。

椭圆的特征三角形：左右焦点、原点、上下顶点，所构成的三角形称为特征三角形，因为其在一个三角形内完美的展现了 [\$a,b,c\$]{.arithmatex} 三个非常重要的参数，也被用于求解椭圆的离心率，或者放缩。

我们发现椭圆的离心率即为椭圆的特征三角形的短边顶点的角的正弦值，这常常用来计算离心率。因为特征三角形某种意义上也是一个焦点三角形（把另一半补上），因此一些用途我们在焦点三角形部分再说。

此外，我们知道椭圆的焦点三角形是及其重要的一个模型，因为其过于复杂，我们后面会开一个单独的模块讲解。

### 正切半角 {#_7}

我们直到椭圆的偏心角参数形式可以写作：

::: {.arithmatex}
\$\$ (a\cos\theta,b\sin\theta),\theta\in\R \$\$
:::

我们在三角函数部分提到过一个很*万能*的公式，正切半角公式（也叫做万能公式），不妨记 [\$\varphi\$]{.arithmatex} 为 [\$\theta\$]{.arithmatex} 的半角，那么：

::: {.arithmatex}
\$\$ \sin\theta=\sin\paren{2\times\dfrac{\theta}{2}}=\dfrac{2\sin\varphi\cos\varphi}{\sin\^2\varphi+\cos\^2\varphi} \$\$
:::

::: {.arithmatex}
\$\$ \cos\theta=\cos\paren{2\times\dfrac{\theta}{2}}=\dfrac{\cos\^2\varphi-\sin\^2\varphi}{\sin\^2\varphi+\cos\^2\varphi} \$\$
:::

根据正切函数的定义，那么就有正切半角公式系列：

::: {.arithmatex}
\$\$ \sin\theta=\dfrac{2\tan\varphi}{1+\tan\^2\varphi}\quad\cos\theta=\dfrac{1-\tan\^2\varphi}{1+\tan\^2\varphi} \$\$
:::

那么，将其带入椭圆的偏心交参数，便可以得出椭圆的一个经典的有理参数方程：

::: {.arithmatex}
\$\$ x(t)=a\dfrac{1-t\^2}{1+t\^2} \$\$
:::

::: {.arithmatex}
\$\$ y(t)=b\dfrac{2t}{1+t\^2} \$\$
:::

此时，坐标就变成了关于 [\$t\$]{.arithmatex} 的有理函数，可以大幅缩小计算量（尤其是用计算机模拟计算多项式、分式方程会比一般形式快很多、方便很多）。

我们观察这个方程的形式，也可以通过计算机作图来辅助，我们发现：

- 当 [\$t\in\R\$]{.arithmatex} 从小到大连续变化时，点 [\$(x(t),y(t))\$]{.arithmatex} 从左端点开始，沿着顺时针方向绕一圈，然后回到左端点。

- 当 [\$t\to\pm\infty\$]{.arithmatex} 时，点为椭圆的左端点，也就是说这个曲线严格来讲，是取不到左端点的！

因此，可以把 [\$\mathbb R\cup\\\infty\\\$]{.arithmatex}（射影直线）与椭圆建立几乎一一对应。因此，自然也可以由椭圆上一点反求到参数，利用：

::: {.arithmatex}
\$\$ t=\tan\dfrac{\theta}{2}=\dfrac{\sin\theta}{1+\cos\theta} \$\$
:::

从而：

::: {.arithmatex}
\$\$ t=\dfrac{ay}{b(a+x)}\quad(x\neq-a) \$\$
:::

这在"从点反算参数""拟合/求交/迭代"里非常好用。

如果我们按照 [\$x(t)+a,y(t)\$]{.arithmatex} 列出来，也就是说，我们会发现：

::: {.arithmatex}
\$\$ \dfrac{y(t)}{x(t)+a}=\dfrac{b}{a}t \$\$
:::

也就是说，参数 [\$t\$]{.arithmatex} 本质上就是从左端点向外发射的直线的斜率（差一个比例）。这解释了为何它能把椭圆参数化成有理函数：任何非退化二次曲线都可用"过定点作一束直线取第二交点"的方式有理参数化。

一类立刻好用的结论：与直线求交只需解二次方程。这是计算几何里最常用的点，避免三角、避免开方，稳定且快，设直线

::: {.arithmatex}
\$\$ y=kx+d \$\$
:::

把有理参数带入，最终化简整理得一个关于 [\$t\$]{.arithmatex} 的二次方程：

::: {.arithmatex}
\$\$ (ka-d)t\^2+2bt-(ka+d)=0 \$\$
:::

解出 [\$t\$]{.arithmatex} 就得到焦点，而与竖线求焦点则更简单：

::: {.arithmatex}
\$\$ y\^2=\dfrac{a-x_0}{a+x_0}\quad(\|x_0\|\<a) \$\$
:::

切线公式变得特别"干净"：一条线性方程（且系数有理），带入即可化简得到

::: {.arithmatex}
\$\$ (1-t\^2)bx+2tay=(1+t\^2)ab \$\$
:::

外点 [\$P(X,Y)\$]{.arithmatex} 作椭圆切线（求切点）只需解二次方程：

::: {.arithmatex}
\$\$ (X+a)t\^2-\dfrac{2aY}{b}t+(a-X)=0 \$\$
:::

切线斜率 / 法线斜率直接有理表达，根据：

::: {.arithmatex}
\$\$ \dfrac{\d x}{\d t}=-\dfrac{4at}{(1+t\^2)\^2} \$\$
:::

::: {.arithmatex}
\$\$ \dfrac{\d y}{\d t}=\dfrac{2b(1-t\^2)}{(1+t\^2)\^2} \$\$
:::

所以切线斜率为：

::: {.arithmatex}
\$\$ \dfrac{\d y}{\d x}=\dfrac{\d t}{\d t}\cdot\dfrac{\d t}{\dt x}=\dfrac{b(t\^2-1)}{2at} \$\$
:::

结论 1：弦的斜率公式，椭圆上两点 [\$P_1(\theta_1), P_2(\theta_2)\$]{.arithmatex} 连线斜率

::: {.arithmatex}
\$\$ k = -\frac{b}{a} \cot\frac{\theta_1+\theta_2}{2} = -\frac{b}{a} \cdot \frac{1-t_1t_2}{t_1+t_2} \$\$
:::

结论 2：弦的方程

::: {.arithmatex}
\$\$ \frac{x}{a}\cos\frac{\theta_1+\theta_2}{2} + \frac{y}{b}\sin\frac{\theta_1+\theta_2}{2} = \cos\frac{\theta_1-\theta_2}{2} \$\$
:::

结论 3：弦中点坐标，设 [\$S = t_1 + t_2\$]{.arithmatex}，[\$P = t_1 t_2\$]{.arithmatex}，则中点 [\$M(\bar{x}, \bar{y})\$]{.arithmatex}

::: {.arithmatex}
\$\$ \bar{x} = \frac{a(1-P\^2) - aS\^2 + 2aP}{(1+t_1\^2)(1+t_2\^2)} = \frac{a(1-t_1\^2 t_2\^2)}{(1+t_1\^2)(1+t_2\^2)} \$\$
:::

::: {.arithmatex}
\$\$ \bar{y} = \frac{b(t_1+t_2)(1+t_1t_2)}{(1+t_1\^2)(1+t_2\^2)} \$\$
:::

结论 4：焦点三角形面积，点 [\$P(\theta)\$]{.arithmatex} 与两焦点构成的三角形面积为

::: {.arithmatex}
\$\$ S = bc\|\sin\theta\| = \frac{2bc\|t\|}{1+t\^2} \$\$
:::

一个"数论 / 构造"层面的好处：生成有理点，若 [\$a,b\$]{.arithmatex} 为有理数，则对于任意有理 [\$t\$]{.arithmatex} 有 [\$x(t),y(t)\$]{.arithmatex} 都是有理数，从而你能系统地产生椭圆上的有理点。这在"构造性几何""有理近似""符号计算测试数据"等场景很方便。

### 极点极线 {#_8}

过椭圆外一点 [\$P(x_0,y_0)\$]{.arithmatex} 做两条切线 [\$PC,PD\$]{.arithmatex}，容易知道

::: {.arithmatex}
\$\$ \ell\_{CD}:\dfrac{x_0x}{a\^2}+\dfrac{y_0y}{b\^2}=1 \$\$
:::

而我们不妨做两条 [\$\angle CPD\$]{.arithmatex} 内的线，分别与椭圆交于 [\$A_1,A_2\$]{.arithmatex} 与 [\$B_1,B_2\$]{.arithmatex} 点，如图。

![alt text](../image-26.avif){width="50%"}

我们发现 [\$A_2B_1,A_1B_2\$]{.arithmatex} 相交于 [\$T\$]{.arithmatex}，且 [\$T\$]{.arithmatex} 在 [\$CD\$]{.arithmatex} 上。

特殊的，如果 [\$P\$]{.arithmatex} 在椭圆的右准线上（左准线类似），容易知道极线方程：

::: {.arithmatex}
\$\$ \dfrac{x}{c}+\dfrac{yt}{b\^2}=1 \$\$
:::

一定是过右焦点 [\$F(c,0)\$]{.arithmatex} 的，且 [\$PF\perp CD\$]{.arithmatex}，弦长公式为：

::: {.arithmatex}
\$\$ \|CD\|=\dfrac{2a(c\^2t\^2+b\^4)}{c\^2t\^2+a\^2b\^2}\ge\dfrac{2b\^2}{a\^2} \$\$
:::

互极：设 [\$ABCD\$]{.arithmatex} 是椭圆

::: {.arithmatex}
\$\$ \frac{x\^2}{a\^2} + \frac{y\^2}{b\^2} = 1 \$\$
:::

的内接四边形，对边 [\$AB\$]{.arithmatex}，[\$CD\$]{.arithmatex} 交于点 [\$P(x_1, y_1)\$]{.arithmatex}，对边 [\$AD\$]{.arithmatex}，[\$BC\$]{.arithmatex} 交于点 [\$Q(x_2, y_2)\$]{.arithmatex}，对角线 [\$AC\$]{.arithmatex}，[\$BD\$]{.arithmatex} 交于点 [\$R(x_3, y_3)\$]{.arithmatex}，则 [\$P,Q,R\$]{.arithmatex} 三点满足：

其中任意两点确定的直线，恰为以第三点为极点关于椭圆的极线。即：对任意 [\$i, j = 1,2,3, i \ne j\$]{.arithmatex}，我们有

::: {.arithmatex}
\$\$ \frac{x_i x_j}{a\^2} + \frac{y_i y_j}{b\^2} = 1 \$\$
:::

![alt text](../image-27.avif){width="60%"}

如图 9-12 所示，已知 [\$P(x_P, y_P)\$]{.arithmatex} 和圆 [\$x\^2 + y\^2 = 1\$]{.arithmatex}，过点 [\$P\$]{.arithmatex} 任作一割线交圆于 [\$A,B\$]{.arithmatex} 两点，交 [\$\ell : x_Px + y_Py = 1\$]{.arithmatex} 于点 [\$Q\$]{.arithmatex}，则

::: {.arithmatex}
\$\$ \begin{aligned} \dfrac{PA}{PB} = \dfrac{QA}{QB}\\ \dfrac{2}{PQ} = \dfrac{1}{PA} + \dfrac{1}{PB} \end{aligned} \$\$
:::

同时，点 [\$P\$]{.arithmatex} 关于圆 [\$x\^2 + y\^2 = 1\$]{.arithmatex} 的极线经过点 [\$Q\$]{.arithmatex} 当且仅当点 [\$Q\$]{.arithmatex} 关于圆 [\$x\^2 + y\^2 = 1\$]{.arithmatex} 的极线经过点 [\$P\$]{.arithmatex}。

如图 9-13 所示，特别地，若 [\$PQ\$]{.arithmatex} 经过圆心并交圆于 [\$R\$]{.arithmatex}，则有 [\$\|OR\|\^2 = \|OP\|\cdot\|OQ\|\$]{.arithmatex}。反之，若 [\$\|OR\|\^2 = \|OP\|\cdot\|OQ\|\$]{.arithmatex}，则 [\$Q\$]{.arithmatex} 落在点 [\$P\$]{.arithmatex} 的极线 [\$x_Px + y_Py = 1\$]{.arithmatex} 上。

![alt text](../image-39.avif){width="80%"}

对于一般的圆锥曲线，将切线方程直接搬过来，就是极线方程，也有上面的两条性质。

### 等角共轭 {#_9}

椭圆的等角共轭：过椭圆外一点 [\$P\$]{.arithmatex} 做切线 [\$PX,PY\$]{.arithmatex}，切点为 [\$X,Y\$]{.arithmatex}。连接 [\$PF_1,PF_2\$]{.arithmatex}，则 [\$\angle XPF_1=\angle YPF_2\$]{.arithmatex}。

![alt text](../image-12.avif){width="50%"}

我们将 [\$F_1,F_2\$]{.arithmatex} 分别关于 [\$PX,PY\$]{.arithmatex} 对称，得到 [\$F_1\',F_2\'\$]{.arithmatex}，根据初中几何容易知道，[\$\triangle PF_1\'F_2\cong\triangle PF_1F_2\'\$]{.arithmatex}，两顶角减去公共部分 [\$\angle F_1PF_2\$]{.arithmatex}，即可得到。

根据已经证明的全等，因此 [\$\angle PF_1X = \angle PF_1\'F_2 = \angle PF_1F_2\' = \angle PF_1Y\$]{.arithmatex}，也就是说对于曲线外一点 [\$P\$]{.arithmatex} 与焦点的连线一定平分两个切点与这个焦点所构成的角。

双曲线有着类似的性质，但是需要注意切点是否位于同一分支上。

![alt text](../image-13.avif){width="40%"}

此时有 [\$\angle F_1PX = \pi - \angle F_2PY\$]{.arithmatex}。

### 蒙日圆 {#_10}

蒙日圆：若过椭圆外一点 [\$P\$]{.arithmatex} 做椭圆的两条切线相互垂直，则 [\$P\$]{.arithmatex} 的轨迹为一个圆，轨迹方程为

::: {.arithmatex}
\$\$ x\^2+y\^2=a\^2+b\^2 \$\$
:::

证明：不妨做 [\$F_1\$]{.arithmatex} 关于 [\$PX\$]{.arithmatex} 的对称点 [\$F_1\'\$]{.arithmatex}，不难得到 [\$\angle F_1\'PF_2=\angle XPY=90\^\circ\$]{.arithmatex}，

![alt text](../image-14.avif){width="40%"}

又因为 [\$PF_1\'=PF_1\$]{.arithmatex}，也就是说只需要令

::: {.arithmatex}
\$\$ PF_1\^2+PF_2\^2=F_1F_2\^2 \$\$
:::

即可，我们设 [\$P(x,y)\$]{.arithmatex}，而 [\$F_1F_2=2a\$]{.arithmatex}，带入得

::: {.arithmatex}
\$\$ (x+c)\^2+y\^2+(x-c)\^2+y\^2=4a\^2 \$\$
:::

整理即可得到上面的轨迹方程。

对双曲线而言，这样的圆并不总存在。当双曲线的两条渐近线所成角为锐角时，该圆的半径为虚数；若两条渐近线互相垂直，则该圆退化为双曲线的中心这一点。

还有一些奇怪的结论。

- 过点 [\$P\$]{.arithmatex} 作圆锥曲线的两条切线，若两切线的斜率之积为定值，则点 [\$P\$]{.arithmatex} 的轨迹为某一圆锥曲线。

- 将一根绳子套在椭圆 [\$\alpha\$]{.arithmatex} 上，并用铅笔把绳子绷紧。若使铅笔绕着椭圆转动，则它将描出另一条与 [\$\alpha\$]{.arithmatex} 同焦的椭圆。

- 一条椭圆内接于一个凸四边形，且它的两个焦点分别落在该四边形的两条（不同的）对角线上，则该四边形两对对边长度的乘积相等。

## 双曲线 {#_11}

### 第一定义 {#_12}

到两定点 [\$F_1,F_2\$]{.arithmatex} 距离之差的绝对值为常数（小于 [\$\|F_1F_2\|\$]{.arithmatex}）的点的轨迹称为双曲线。

与椭圆类似，我们设左焦点 [\$F_1=(-c,0)\$]{.arithmatex} 和右焦点 [\$F_2=(c,0)\$]{.arithmatex}，距离之差为 [\$2a\$]{.arithmatex}，其中 [\$c\>a\>0\$]{.arithmatex}，有双曲线的一般方程

::: {.arithmatex}
\$\$ \dfrac{x\^2}{a\^2}-\dfrac{y\^2}{c\^2-a\^2}=1 \$\$
:::

同样，令 [\$b=\sqrt{c\^2-a\^2}\$]{.arithmatex} 即 [\$c\^2=a\^2+b\^2\$]{.arithmatex}。

::: {.arithmatex}
\$\$ \dfrac{x\^2}{a\^2}-\dfrac{y\^2}{b\^2}=1 \$\$
:::

### 第二定义 {#_13}

到一定点 [\$F_1\$]{.arithmatex} 的距离与到一定直线的距离之比为定值（大于 [\$1\$]{.arithmatex}）的点所形成的轨迹称为双曲线。该定直线称为准线。

与抛物线一样，我们可以得到

::: {.arithmatex}
\$\$ \sqrt{(x-c)\^2+y\^2}=\dfrac{c}{a}\vert{x-\dfrac{a\^2}{c}} \$\$
:::

但是此时 [\$\dfrac{c}{a}\$]{.arithmatex} 应当是大于 [\$1\$]{.arithmatex} 的，同理

::: {.arithmatex}
\$\$ \sqrt{(x+c)\^2+y\^2}=\dfrac{c}{a}\vert{x+\dfrac{a\^2}{c}} \$\$
:::

前者是右焦点与右准线，后者是左焦点与左准线，准线方程依旧是

::: {.arithmatex}
\$\$ x=\pm\dfrac{a\^2}{c} \$\$
:::

比值就是 [\$\dfrac{c}{a}\$]{.arithmatex}，这称为离心率，定义为

::: {.arithmatex}
\$\$ e=\dfrac{c}{a}=\sqrt{1+\dfrac{b\^2}{a\^2}}\>1 \$\$
:::

离心率越大，双曲线的开口越大。

### 焦点三角形 {#_14}

此处写一点双曲线的焦点三角形相关内容，尽管下面的焦点三角形中已经有很多结论，但是大部分还是针对椭圆的，为了不引起歧义或混乱，一些东西在这里列举。

双曲线左右焦点为 [\$F_1,F_2\$]{.arithmatex}，双曲线上一点 [\$P\$]{.arithmatex} 的焦点弦：

::: {.arithmatex}
\$\$ \|PF_1\|=\|a+ex_0\| \$\$
:::

::: {.arithmatex}
\$\$ \|PF_2\|=\|a-ex_0\| \$\$
:::

注意这里要有绝对值符号，里面的式子正负取决于是否在同一侧，因为绝对值的存在，这不影响最终结果。

不妨设 [\$\angle PF_1F_2=\theta\$]{.arithmatex}，不妨假设 [\$P\$]{.arithmatex} 在左支（在 [\$F_1\$]{.arithmatex} 一侧），这条直线交另一支于点 [\$Q\$]{.arithmatex}，则：

::: {.arithmatex}
\$\$ \|PF_1\|=\dfrac{ep}{e\cos\theta+1}=\dfrac{a(e\^2-1)}{e\cos\theta+1} \$\$
:::

::: {.arithmatex}
\$\$ \|QF_1\|=\dfrac{ep}{e\cos\theta-1}=\dfrac{a(e\^2-1)}{e\cos\theta-1} \$\$
:::

双曲线的第三定义的主要区别在于，在椭圆的公式中去掉负号即可。

- [\$M,N\$]{.arithmatex} 是双曲线 [\$C:\dfrac{x\^2}{A\^2}-\dfrac{y\^2}{B\^2}=\pm1\$]{.arithmatex} 上的两点，则 [\$P\$]{.arithmatex} 是 [\$MN\$]{.arithmatex} 的中点，等价于

  ::: {.arithmatex}
  \$\$ k\_{MN} \cdot k\_{OP} = \dfrac{B\^2}{A\^2} \$\$
  :::

- 已知直线 [\$y=kx+m\$]{.arithmatex} 与双曲线 [\$C: \dfrac{x\^2}{A\^2} - \dfrac{y\^2}{B\^2} = 1\$]{.arithmatex} 的渐近线交于 [\$M, N\$]{.arithmatex} 两点，则 [\$P\$]{.arithmatex} 是 [\$MN\$]{.arithmatex} 的中点，等价于

  ::: {.arithmatex}
  \$\$ k\_{MN} \cdot k\_{OP} = \dfrac{B\^2}{A\^2} \$\$
  :::

  令 [\$M(x_1, y_1), N(x_2, y_2)\$]{.arithmatex}，点 [\$M, N\$]{.arithmatex} 在渐近线上，可得

  ::: {.arithmatex}
  \$\$ \begin{cases} \dfrac{x_2\^2}{a\^2} - \dfrac{y_2\^2}{b\^2} = 0 \\ \dfrac{x_1\^2}{a\^2} - \dfrac{y_1\^2}{b\^2} = 0 \end{cases} \implies \dfrac{y_2\^2 - y_1\^2}{x_2\^2 - x_1\^2} = \dfrac{b\^2}{a\^2} \implies \dfrac{y_2 - y_1}{x_2 - x_1} \cdot \dfrac{y_2 + y_1}{x_2 + x_1} = \dfrac{b\^2}{a\^2} \$\$
  :::

  由此可知 [\$k\_{OP} \cdot k\_{MN} = \dfrac{b\^2}{a\^2}\$]{.arithmatex}。

### 特征三角形 {#_15}

做焦点到渐近线的垂线，焦点、垂足、圆心所构成的三角形即为双曲线的特征三角形。

![alt text](../imagett.avif){width="60%"}

设焦点 [\$F(c,0)\$]{.arithmatex}，在渐近线 [\$bx=ay\$]{.arithmatex} 上的垂足为 [\$P\$]{.arithmatex}，坐标原点为 [\$O\$]{.arithmatex}，则

::: {.arithmatex}
\$\$ \|FP\|=\dfrac{bc}{\sqrt{a\^2+b\^2}}=b \$\$
:::

根据勾股定理，[\$\|OP\|=a\$]{.arithmatex}，这就是双曲线的特征三角形。

与之类似的，我们还可以从双曲线上任意一点向两条渐近线引垂线，如图

![alt text](../image-24.avif){width="40%"}

则有

::: {.arithmatex}
\$\$ \|PH_1\|\cdot\|PH_2\|=\dfrac{a\^2b\^2}{a\^2+b\^2} \$\$
:::

可以直接设出 [\$P\$]{.arithmatex} 点坐标，带入化简即可。

### 特殊双曲线 {#_16}

一些特殊的双曲线：

- 等轴双曲线（直角双曲线）：渐近线相互垂直 [\$a=b\$]{.arithmatex} 的双曲线，离心率 [\$e=\sqrt2\$]{.arithmatex}。

- 共轭双曲线：两条虚实轴互换的双曲线，共用两条渐近线，四焦点共圆。

根据我们在一般方程中的描述，很容易发现以下的函数也都是双曲线：

::: {.arithmatex}
\$\$ y=\dfrac{1}{x} \$\$
:::

::: {.arithmatex}
\$\$ y=x+\dfrac{1}{x} \$\$
:::

::: {.arithmatex}
\$\$ y=x-\dfrac{1}{x} \$\$
:::

其实大胆猜测，"形状像"双曲线的，可以化为二元二次实方程的，都是双曲线。

### 几何性质 {#_17}

我们知道

::: {.arithmatex}
\$\$ x\^2=a\^2\paren{1+\dfrac{y\^2}{b\^2}} \$\$
:::

因此

::: {.arithmatex}
\$\$ \|x\|\ge a \$\$
:::

即 [\$x\ge a\$]{.arithmatex} 或 [\$x\le-a\$]{.arithmatex}，而 [\$y\$]{.arithmatex} 为实数。

双曲线有两个顶点，左顶点 [\$A_1=(-a,0)\$]{.arithmatex} 和右顶点 [\$A_2=(a,0)\$]{.arithmatex}，线段 [\$A_1A_2\$]{.arithmatex} 称为实轴，[\$a\$]{.arithmatex} 称为实半轴长。

另外，设 [\$B_1=(0,b)\$]{.arithmatex} 和 [\$B_2=(0,-b)\$]{.arithmatex}，则 [\$B_1B_2\$]{.arithmatex} 称为虚轴，这个轴本身没有太多意义。

特别的，如果 [\$a=b\$]{.arithmatex}，则这个双曲线称为等轴双曲线。

双曲线有对称轴为坐标轴，对称中心为坐标原点。

双曲线有两条渐近线

::: {.arithmatex}
\$\$ y=\pm\dfrac{b}{a}x \$\$
:::

也就是

::: {.arithmatex}
\$\$ \dfrac{y}{b}\pm\dfrac{x}{a}=0 \$\$
:::

或者可以记为

::: {.arithmatex}
\$\$ \dfrac{x\^2}{a\^2}-\dfrac{y\^2}{b\^2}=0 \$\$
:::

### 双曲函数 {#_18}

双曲函数因为其性质极其类似三角函数，因此也称为双曲三角函数。

我们知道三角函数 [\$\sin\theta,\cos\theta\$]{.arithmatex} 是在单位圆上引入一条倾角为 [\$\theta\$]{.arithmatex} 的直线，与单位圆相交的点的坐标即为 [\$(\cos\theta,\sin\theta)\$]{.arithmatex}，类似的我们推出双曲函数的最初定义：倾角为 [\$\theta\$]{.arithmatex} 的直线与双曲线 [\$x\^2-y\^2=1\$]{.arithmatex} 交于点 [\$(\cosh\theta,\sinh\theta)\$]{.arithmatex}。

::: {.arithmatex}
\$\$ \sinh x=\dfrac{e\^x-e\^{-x}}{2} \$\$
:::

::: {.arithmatex}
\$\$ \cosh x=\dfrac{e\^x+e\^{-x}}{2} \$\$
:::

::: {.arithmatex}
\$\$ \tanh x=\dfrac{\sinh x}{\cosh x}=\dfrac{e\^x-e\^{-x}}{e\^x+e\^{-x}} \$\$
:::

其图像如图

![](../Sinh_cosh_tanh.svg){width="60%"}

我们在复数部分推导了欧拉公式，因此不难知道

::: {.arithmatex}
\$\$ \begin{cases} \cos x&=\cosh(ix)\\ \sin x&=-i\sinh(ix) \end{cases} \$\$
:::

我们利用这个可以从三角函数的几乎所有公式迁移到双曲函数。

一些公式

::: {.arithmatex}
\$\$ \cosh\^2x-\sinh\^2x=1 \$\$
:::

::: {.arithmatex}
\$\$ \sinh(x\pm y)=\sinh x\cosh y\pm \cosh x\sinh y \$\$
:::

::: {.arithmatex}
\$\$ \cosh(x\pm y)=\cosh x\cosh y\pm\sinh x\sinh y \$\$
:::

::: {.arithmatex}
\$\$ \tanh (x\pm y)=\frac{\tanh x\pm \tanh y}{1\pm \tanh x\tanh y} \$\$
:::

::: {.arithmatex}
\$\$ \sinh 2x=2\sinh x\cosh x \$\$
:::

::: {.arithmatex}
\$\$ \cosh 2x=\cosh\^2x+\sinh\^2x \$\$
:::

::: {.arithmatex}
\$\$ \tanh 2x=\frac{2\tanh x}{1+\tanh\^2x} \$\$
:::

::: {.arithmatex}
\$\$ (\sinh x)\'=\cosh x \$\$
:::

::: {.arithmatex}
\$\$ (\cosh x)\'=\sinh x \$\$
:::

## 焦点三角形 {#_19}

焦点三角形，即为圆锥曲线上一点或两点，与两个或一个焦点为顶点，所构成的三角形（或者退化的三角形），其在椭圆中表现的尤为重要，更多是因为双曲线的焦点三角形情况复杂、出题较少，且抛物线更常用到的模型是特征矩形而不是焦点三角形。

### 离心率 {#_20}

离心率问题是初学阶段最重要的一类题目，难度相对较低但是适合练手，对于离心率问题，常见的几种方法有：

1.  带入点或者根据定义直接求 [\$a,b,c\$]{.arithmatex} 的值或其比例。

2.  构造关于 [\$a,b,c\$]{.arithmatex} 的齐次方程，全部化为 [\$a,c\$]{.arithmatex} 的齐次方程后同除 [\$a\^2\$]{.arithmatex} 得到关于 [\$e\$]{.arithmatex} 的一元方程。

3.  在特征三角形中解决，或者在一般的焦点三角形中，利用余弦定理等解三角形方式解决，设椭圆上一点 [\$P\$]{.arithmatex}、左右焦点 [\$F_1,F_2\$]{.arithmatex} 构成三角形，设 [\$\theta=\angle F_1PF_2\$]{.arithmatex}，[\$\alpha=\angle PF_1F_2\$]{.arithmatex}，[\$\beta=\angle PF_2F_1\$]{.arithmatex}。

    不妨列出正弦定理：

    ::: {.arithmatex}
    \$\$ \dfrac{\|PF_1\|}{\sin\beta}=\dfrac{\|PF_2\|}{\sin\alpha}=\dfrac{\|F_1F_2\|}{\sin\theta} \$\$
    :::

    根据合比定理：

    ::: {.arithmatex}
    \$\$ \dfrac{\|PF_1\|+\|PF_2\|}{\sin\alpha+\sin\beta}=\dfrac{\|F_1F_2\|}{\sin\theta} \$\$
    :::

    注意到前者分子为 [\$2a\$]{.arithmatex}，后者分子为 [\$2c\$]{.arithmatex}，则

    ::: {.arithmatex}
    \$\$ e=\dfrac{2c}{2a}=\dfrac{\sin\theta}{\sin\alpha+\sin\beta}=\dfrac{\sin(\alpha+\beta)}{\sin\alpha\sin\beta} \$\$
    :::

    这类问题中要活用几何问题代数化，先思考然后才能简便的计算。

对于离心率的极值问题，我们通常取顶点作为特殊点（顶角的最大角），根据三角函数的单调性、配合离心率与开口大小的关系解决。

### 长度问题 {#_21}

椭圆左右焦点分别为 [\$F_1,F_2\$]{.arithmatex}，则椭圆上一点 [\$P(x_0,y_0)\$]{.arithmatex}，则：

::: {.arithmatex}
\$\$ \|PF_1\|=a+\dfrac{c}{a}x_0=a+ex_0 \$\$
:::

::: {.arithmatex}
\$\$ \|PF_2\|=a-\dfrac{c}{a}x_0=a-ex_0 \$\$
:::

据此，我们发现：

::: {.arithmatex}
\$\$ b\^2-c\^2\le\vecc{PF_1}\cdot\vecc{PF_2}\le b\^2 \$\$
:::

::: {.arithmatex}
\$\$ a\^2\le\|PF_1\|\cdot\|PF_2\|=a\^2-e\^2x_0\^2\le b\^2 \$\$
:::

而根据极化恒等式 [\$\vecc{PF_1}\cdot\vecc{PF_2}=\|PO\|\^2-c\^2\$]{.arithmatex}，得出：

::: {.arithmatex}
\$\$ b\le\|PO\|\le a \$\$
:::

双曲线中的一类特殊的长度问题：过一个焦点的直线，已知与双曲线交出的弦的长度 [\$k\$]{.arithmatex}，求可能的直线条数。分类讨论直线与双曲线交于一支还是两支，容易发现如果小于 [\$k\$]{.arithmatex} 通经 [\$2b\^2/a\$]{.arithmatex}，则直线不存在；如果大于实轴长 [\$2a\$]{.arithmatex}，则一定存在四条直线；在中间分界即可。

用参数方程表示直线：当我们考虑的式子是形如 [\$\|PA\|，\|PB\|\$]{.arithmatex} 的关系，不妨考虑以 [\$P(x_0,y_0)\$]{.arithmatex} 为极点建立极坐标系（形式上用参数方程），然后表示 [\$AB\$]{.arithmatex}（倾斜角为 [\$\theta\$]{.arithmatex}）的方程即为

::: {.arithmatex}
\$\$ \begin{cases} x&=x_0+\rho\cos\theta\\ y&=y_0+\rho\sin\theta \end{cases} \$\$
:::

这样 [\$\rho\$]{.arithmatex} 就表示一个点到 [\$P\$]{.arithmatex} 的距离，将其带入圆锥曲线，利用韦达定理可以快速得到 [\$\|PA\|，\|PB\|\$]{.arithmatex} 的关系。

### 角度问题 {#_22}

在上一节中，我们推导了关于 [\$P\$]{.arithmatex} 点坐标的焦半径公式，那如果不知道坐标呢？此时我们将 [\$P\$]{.arithmatex} 字母换为 [\$A\$]{.arithmatex} 字母，反向延长 [\$F_1A\$]{.arithmatex} 交椭圆于点 [\$B\$]{.arithmatex}，设 [\$\theta=\angle F_1AF_2\$]{.arithmatex} 那么就有焦半径公式点角度形式：

::: {.arithmatex}
\$\$ \|AF_1\|=\dfrac{ep}{1-e\cos\theta}=\dfrac{a(1-e\^2)}{1-e\cos\theta}=\dfrac{b\^2/a}{1-e\cos\theta} \$\$
:::

::: {.arithmatex}
\$\$ \|AF_2\|=\dfrac{ep}{1+e\cos\theta}=\dfrac{a(1-e\^2)}{1+e\cos\theta}=\dfrac{b\^2/a}{1+e\cos\theta} \$\$
:::

这两个东西即为椭圆的极坐标表示，即以左焦点为极点、长轴正方形为极轴，则

::: {.arithmatex}
\$\$ \rho=\dfrac{a(1-e\^2)}{1-e\cos\theta} \$\$
:::

我们不妨推导一些更有意思的东西：

::: {.arithmatex}
\$\$ \dfrac{1}{\|AF_1\|}+\dfrac{1}{AF_2}=\dfrac{2}{ep}=\dfrac{2}{a(1-e\^2)}=\dfrac{2a}{b\^2} \$\$
:::

::: {.arithmatex}
\$\$ \|AB\|=\|AF_1\|+\|AF_2\|=\dfrac{2b\^2/a}{1-e\^2\cos\^2\theta}\ge\dfrac{2b\^2}{a} \$\$
:::

这个最小值即为椭圆的通经，即过焦点垂直于轴的直线交椭圆的弦。

在圆锥曲线的选择与填空题中，若有中点这样的信息出现，就要联想到原点并连接原点与该点，构造中位线。因为原点是椭圆和双曲线的中心，是两焦点的天然中点。

![alt text](../image-32.avif){width="40%"}

通经公式可以作如下推广：过焦点 [\$F\$]{.arithmatex} 作 [\$n\$]{.arithmatex} 条夹角相等的射线交椭圆于 [\$P_1, P_2, \cdots, P_n\$]{.arithmatex}，则

::: {.arithmatex}
\$\$ \frac{1}{\|FP_1\|} + \frac{1}{\|FP_2\|} + \cdots + \frac{1}{\|FP_n\|} = \frac{na}{b\^2} \$\$
:::

焦比定理（简化形式）指出，若 [\$\|AF_1\|=\lambda\|BF_1\|\$]{.arithmatex}，我们列出：

::: {.arithmatex}
\$\$ \dfrac{1}{1-e\cos\theta}=\dfrac{\lambda}{1+e\cos\theta} \$\$
:::

那么，

::: {.arithmatex}
\$\$ e\|\cos\theta\|=\dfrac{\lambda-1}{\lambda+1} \$\$
:::

这个在一些小题可能有快速解题的作用。

### 固定关系 {#_23}

焦点三角形的**周长**与圆锥曲线的定义之间存在着紧密联系。

- 已知 [\$F_1, F_2\$]{.arithmatex} 分别为椭圆 [\$\dfrac{x\^2}{a\^2} + \dfrac{y\^2}{b\^2} = 1(a \> b \> 0)\$]{.arithmatex} 的左、右焦点，[\$l\$]{.arithmatex} 过焦点 [\$F_1\$]{.arithmatex} 且与椭圆交于 [\$A, B\$]{.arithmatex} 两点，则 [\$\triangle F_2AB\$]{.arithmatex} 的周长恒为定值 [\$4a\$]{.arithmatex}；

- 已知 [\$F_1, F_2\$]{.arithmatex} 分别为椭圆 [\$\dfrac{x\^2}{a\^2} + \dfrac{y\^2}{b\^2} = 1(a \> b \> 0)\$]{.arithmatex} 的左、右焦点，[\$P\$]{.arithmatex} 是椭圆上的动点，则 [\$\triangle PF_1F_2\$]{.arithmatex} 的周长恒为定值 [\$2a + 2c\$]{.arithmatex}。

  ![alt text](../image-28.avif)

- 已知 [\$F_1, F_2\$]{.arithmatex} 分别是双曲线 [\$\dfrac{x\^2}{a\^2} - \dfrac{y\^2}{b\^2} = 1(a \> 0, b \> 0)\$]{.arithmatex} 的左、右焦点，[\$l\$]{.arithmatex} 过焦点 [\$F_1\$]{.arithmatex} 且与双曲线交于 [\$A, B\$]{.arithmatex} 两点，则 [\$\|AF_2\| + \|BF_2\| - \|AB\| = 4a\$]{.arithmatex}。

  ![alt text](../image-29.avif)

面积则与顶角有联系，根据余弦定理等可以推导：

- 已知 [\$F_1, F_2\$]{.arithmatex} 为椭圆 [\$\dfrac{x\^2}{a\^2} + \dfrac{y\^2}{b\^2} = 1(a \> b \> 0)\$]{.arithmatex} 的两个焦点，[\$M\$]{.arithmatex} 是椭圆上的动点，则 [\$\triangle MF_1F_2\$]{.arithmatex} 的面积 [\$S = c\|y_M\| = b\^2 \tan\dfrac{\angle F_1MF_2}{2}\$]{.arithmatex}。

  证明

  不妨令 [\$\theta=\angle F_1MF_2\$]{.arithmatex}，[\$r_1=MF_1,r_2=MF_2\$]{.arithmatex}，根据余弦定理

  ::: {.arithmatex}
  \$\$ \cos\theta=\dfrac{r_1\^2+r_2\^2-4c\^2}{2r_1r_2}=\dfrac{(r_1+r_2)\^2-2r_1r_2-4c\^2}{2r_1r_2}=\dfrac{2b\^2}{r_1r_2}-1 \$\$
  :::

  因此：

  ::: {.arithmatex}
  \$\$ r_1r_2=\dfrac{2b\^2}{\cos\theta+1}\le a\^2 \$\$
  :::

  带入三角形面积公式：

  ::: {.arithmatex}
  \$\$ S=\dfrac12r_1r_2\sin\theta=b\^2\dfrac{\sin\theta}{\cos\theta+1}=b\^2\tan\dfrac{\theta}2 \$\$
  :::

- 已知 [\$F_1, F_2\$]{.arithmatex} 为双曲线 [\$\dfrac{x\^2}{a\^2} - \dfrac{y\^2}{b\^2} = 1(a \> 0, b \> 0)\$]{.arithmatex} 的两个焦点，[\$M\$]{.arithmatex} 是双曲线上的动点，则 [\$\triangle MF_1F_2\$]{.arithmatex} 的面积 [\$S = c\|y_M\| = b\^2\cot\dfrac{\angle F_1MF_2}{2}\$]{.arithmatex}。

内切圆即角平分线与面积也有着很大的关联：

- [\$P\$]{.arithmatex} 是椭圆 [\$\dfrac{x\^2}{a\^2} + \dfrac{y\^2}{b\^2} = 1(a \> b \> 0)\$]{.arithmatex} 上的动点，[\$\triangle PF_1F_2\$]{.arithmatex} 的内切圆为圆 [\$I\$]{.arithmatex}，半径为 [\$r\$]{.arithmatex}，则 [\$S\_{\triangle PF_1F_2} = r(a+c)\$]{.arithmatex}。

- 设椭圆 [\$\dfrac{x\^2}{a\^2} + \dfrac{y\^2}{b\^2} = 1(a \> b \> 0)\$]{.arithmatex} 的左、右焦点分别为 [\$F_1, F_2\$]{.arithmatex}，过焦点 [\$F_1\$]{.arithmatex} 的直线交椭圆于 [\$A, B\$]{.arithmatex} 两点，[\$\triangle AF_2B\$]{.arithmatex} 的内切圆为圆 [\$I\$]{.arithmatex}，半径为 [\$r\$]{.arithmatex}，则 [\$S\_{\triangle AF_2B} = 2ar\$]{.arithmatex}。

  ![alt text](../image-30.avif)

- 已知 [\$P\$]{.arithmatex} 是双曲线 [\$\dfrac{x\^2}{a\^2} - \dfrac{y\^2}{b\^2} = 1(a \> 0, b \> 0)\$]{.arithmatex} 上的动点，[\$\triangle PF_1F_2\$]{.arithmatex} 的内切圆的圆心为 [\$I(x_0, y_0)\$]{.arithmatex}，则 [\$\|S\_{\triangle PIF_1} - S\_{\triangle PIF_2}\| = \dfrac{S\_{\triangle F_1IF_2}}{e}\$]{.arithmatex}，[\$\|x_0\| = a\$]{.arithmatex}。

  ![alt text](../image-31.avif)

### 转换关系 {#_24}

转换问题，通常也是隐焦点问题，通常只给出一个焦点，我们需要作出另一个焦点，来构造三角形、平行四边形等。

- 我们注意到，如果 [\$P\$]{.arithmatex} 在椭圆上，那么 [\$PF_2=2a-PF_1\$]{.arithmatex}，这暗示我们可以对 [\$PF_1\$]{.arithmatex} 与令一点 [\$A\$]{.arithmatex} 应用两边之和大于第三边的同时，对 [\$PF_2=2a-PF_1\$]{.arithmatex} 应用两边之差小于第三边，同样可以得到求和的形式。

- 设 [\$A\$]{.arithmatex} 为椭圆上的动点，且 [\$F\$]{.arithmatex} 为椭圆的一个焦点，P为不在椭圆上的一定点，则 [\$\|PA\|+\|PF\|\$]{.arithmatex} 的最值的求法是先利用三角不等式，判断等号成立的条件是否成立？若不成立，则利用另外一个焦点进行转化。

设椭圆方程为 [\$\dfrac{x\^2}{a\^2} + \dfrac{y\^2}{b\^2} = 1(a \> b \> 0)\$]{.arithmatex}，[\$F_1, F_2\$]{.arithmatex} 分别为椭圆的左、右焦点，平面上一定点 [\$Q(x_0, y_0)\$]{.arithmatex}，[\$M\$]{.arithmatex} 为椭圆上任意一点。

- 定点 [\$Q(x_0, y_0)\$]{.arithmatex} 在椭圆内部，则 [\$2a - \|QF_1\| \le \|MF_2\| + \|MQ\| \le 2a + \|QF_1\|\$]{.arithmatex}；
- 定点 [\$Q(x_0, y_0)\$]{.arithmatex} 在椭圆外部，则 [\$\|QF_2\| \le \|MF_2\| + \|MQ\| \le 2a + \|QF_1\|\$]{.arithmatex}。

![alt text](../image-33.avif)

设双曲线方程为 [\$\dfrac{x\^2}{a\^2} - \dfrac{y\^2}{b\^2} = 1(a \> 0, b \> 0)\$]{.arithmatex}，[\$F_1, F_2\$]{.arithmatex} 分别为双曲线的左、右焦点，平面上一定点 [\$Q(x_0, y_0)\$]{.arithmatex}，[\$M\$]{.arithmatex} 为双曲线右支上任意一点。

- 若定点 [\$Q(x_0, y_0)\$]{.arithmatex} 与双曲线右焦点 [\$F_2\$]{.arithmatex} 在双曲线右支的同侧，则 [\$\|MQ\| + \|MF_2\|\$]{.arithmatex} 的最小值是 [\$\|QF_1\| - 2a\$]{.arithmatex}，最大值不存在；
- 若定点 [\$Q(x_0, y_0)\$]{.arithmatex} 与双曲线右焦点 [\$F_2\$]{.arithmatex} 在双曲线右支的异侧，则 [\$\|MQ\| + \|MF_2\|\$]{.arithmatex} 的最小值是 [\$\|QF_2\|\$]{.arithmatex}，最大值不存在。

![alt text](../image-34.avif)

- 不仅第一定义，我们也可以利用第二定义进行转化，把距离焦点的距离转化为距离准线的距离乘上离心率 [\$e\$]{.arithmatex}。

- 设 [\$A\$]{.arithmatex} 为抛物线上的动点，且 [\$F\$]{.arithmatex} 为焦点，[\$P\$]{.arithmatex} 为不在抛物线上的一定点，则 [\$\|PA\| + \|PF\|\$]{.arithmatex} 的最值的求法是先利用三角不等式，判断等号成立的条件是否成立。若不成立，则利用准线进行转化。

### 共焦点型 {#_25}

共焦点的关键在于两个：[\$c\$]{.arithmatex} 相等与定义，在设共焦点圆锥曲线的时候，可以关注 [\$a\^2,b\^2\$]{.arithmatex} 的和或者差的关系，用一个变量 [\$\lambda\$]{.arithmatex} 串联两个圆锥曲线。

例如椭圆 [\$a_1,b_1,c\$]{.arithmatex} 和双曲线 [\$a_2,b_2,c\$]{.arithmatex} 共焦点 [\$F_1,F_2\$]{.arithmatex}，且一交点为 [\$P\$]{.arithmatex} 不难写出

::: {.arithmatex}
\$\$ \begin{cases} PF_1+PF_2&=2a_1\\ PF_1-PF_2&=2a_2 \end{cases} \$\$
:::

也就是说

::: {.arithmatex}
\$\$ \begin{cases} PF_1&=a_1+a_2\\ PF_2&=a_1-a_2 \end{cases} \$\$
:::

已知 [\$F_1, F_2\$]{.arithmatex} 是椭圆 [\$C_1\$]{.arithmatex} 与双曲线 [\$C_2\$]{.arithmatex} 的公共焦点，[\$e_1, e_2\$]{.arithmatex} 分别是 [\$C_1, C_2\$]{.arithmatex} 的离心率。若点 [\$P\$]{.arithmatex} 为 [\$C_1, C_2\$]{.arithmatex} 的公共点，[\$\angle F_1PF_2 = 2\theta\$]{.arithmatex}，则 [\$\dfrac{\sin\^2\theta}{e_1\^2} + \dfrac{\cos\^2\theta}{e_2\^2} = 1\$]{.arithmatex}。

![alt text](../image-37.avif){width="40%"}

在这个图中，据余弦定理还可以推导：

::: {.arithmatex}
\$\$ S\_{\triangle PF_1F_2}=b_1b_2=\sqrt{(a_1\^2-c\^2)(c\^2-a_2\^2)} \$\$
:::

### 最值问题 {#_26}

距离最值：

- 将直线 [\$\ell\$]{.arithmatex} 平移到与曲线相切的位置，得到曲线的一条与直线 [\$\ell\$]{.arithmatex} 平行的切线 [\$\ell\'\$]{.arithmatex}，此时直线 [\$\ell\$]{.arithmatex} 与 [\$\ell\'\$]{.arithmatex} 之间的距离即为曲线与 [\$\ell\$]{.arithmatex} 距离的最值。

  ![alt text](../image-35.avif){width="30%"}

- 椭圆内或外一点到椭圆上一定点的最短距离，我们称所有可能是最近点的点为可能点的点集，而最短距离就是这些点集中的点到定点的距离的最小值。

  理论上，只要这个点集包含了椭圆上所有的点，我们就一定可以找到最小值，但是实际上我们不可能这么做。于是，我们得出几个程序化的方案，将点集缩小到可以手工计算。第一，椭圆的顶点一定是点集内的点。如果图形特征已知，我们也可以只找一两个顶点，取验证其对最小值的贡献即可。

  第二，我们不妨提出法线对齐的概念：当动点 [\$M\$]{.arithmatex} 在椭圆上运动到某点 [\$M_0\$]{.arithmatex} 时，如果连接定点 [\$P\$]{.arithmatex} 与 [\$M_0\$]{.arithmatex} 的线段 [\$PM_0\$]{.arithmatex} 恰好是椭圆在 [\$M_0\$]{.arithmatex} 点的法线，那么 [\$\|PM_0\|\$]{.arithmatex} 就是一个极值距离（极大值或极小值）。

  将法线方程与椭圆方程联立（同时还需要考虑斜率不存在的情况），解这个方程组，得到所有满足法线对齐条件的候选点 [\$M_i(x_i, y_i)\$]{.arithmatex} 的坐标。这通常会转化为一个关于 [\$x\$]{.arithmatex} 或 [\$y\$]{.arithmatex} 的四次方程，可能有 [\$0, 2, 4\$]{.arithmatex} 个实数解。只需验证这些点（顶点和极值点），即可得到最小距离。

长度最值：

- [\$F\$]{.arithmatex} 为椭圆 [\$\dfrac{x\^2}{a\^2} + \dfrac{y\^2}{b\^2} = 1(a \> b \> 0)\$]{.arithmatex} 的一个焦点，若 P 是椭圆上的点，则 [\$a - c \le \|PF\| \le a + c\$]{.arithmatex}。

- [\$F\$]{.arithmatex} 为双曲线 [\$\dfrac{x\^2}{a\^2} - \dfrac{y\^2}{b\^2} = 1(a \> 0, b \> 0)\$]{.arithmatex} 的右焦点，若 P 是双曲线右支上的动点，则 [\$\|PF\| \ge c - a\$]{.arithmatex}。若 P 是双曲线左支上的动点，则 [\$\|PF\| \ge c + a\$]{.arithmatex}。

![alt text](../image-36.avif)

角度最值：

- [\$F_1, F_2\$]{.arithmatex} 为椭圆 [\$\dfrac{x\^2}{a\^2} + \dfrac{y\^2}{b\^2} = 1(a \> b \> 0)\$]{.arithmatex} 的左、右焦点，[\$P\$]{.arithmatex} 是椭圆上的动点，当且仅当 [\$P\$]{.arithmatex} 为上、下顶点时，[\$\angle F_1PF_2\$]{.arithmatex} 最大。

- [\$A, B\$]{.arithmatex} 为椭圆 [\$\dfrac{x\^2}{a\^2} + \dfrac{y\^2}{b\^2} = 1(a \> b \> 0)\$]{.arithmatex} 的左、右顶点，[\$P\$]{.arithmatex} 是椭圆上的动点，当且仅当 [\$P\$]{.arithmatex} 为上、下顶点时，[\$\angle APB\$]{.arithmatex} 最大。

![alt text](../image-38.avif)

对于讨论垂直关系，更常用向量和斜率，或者勾股定理、射影定理等。

### 光学性质 {#_27}

费马原理：当一束光经过镜子的反射，那么入射角等于出射角，可以证明，这个路径是最短的。

证明

设光线从 [\$F_1\$]{.arithmatex} 经过直线 [\$\ell\$]{.arithmatex} 的反射到达 [\$F_2\$]{.arithmatex} 点，我们将 [\$F_1\$]{.arithmatex} 关于 [\$\ell\$]{.arithmatex} 对称的点设为 [\$F_1\'\$]{.arithmatex}

![alt text](../image-10.avif){width="40%"}

则 [\$P\$]{.arithmatex} 点位于 [\$F_1\'F_2\$]{.arithmatex} 与 [\$\ell\$]{.arithmatex} 的交点上，这就是将军饮马模型，也容易证明，入射角和出射角是相等的。

椭圆的光学性质：从一个焦点发出的光线，经过椭圆的反射后一定经过另一个焦点。

证明

如图，容易知道，我们只需要证明 [\$\angle DAF_1=\angle DAF_2\$]{.arithmatex} 即可，

![alt text](../image-3.avif){width="60%"}

根据角平分线逆定理，只需要证

::: {.arithmatex}
\$\$ \dfrac{AF_1}{AF_2}=\dfrac{MF_1}{MF_2} \$\$
:::

但是这比较复杂，我们发现费马定理可以非常容易的解决这个问题。

![alt text](../image-11.avif){width="40%"}

不妨设 [\$X\$]{.arithmatex} 是 [\$\ell\$]{.arithmatex} 上任意一点，则根据 [\$P\$]{.arithmatex} 在椭圆上、[\$X\$]{.arithmatex} 在椭圆外，

::: {.arithmatex}
\$\$ XF_1+XF_2\ge PF_1+PF_2 \$\$
:::

取等当且仅当 [\$P=X\$]{.arithmatex}，因此 [\$P\$]{.arithmatex} 就是费马定理的点，符合入射角等于出射角。

抛物线的光学性质：从焦点发出的光线，经过抛物线的反射后，一定平行于抛物线的轴。

证明

假设 [\$P\$]{.arithmatex} 为抛物线上一点，做到准线的垂线，垂足为 [\$P\'\$]{.arithmatex}，如图

![alt text](../image-9.avif){width="40%"}

我们不妨证明锅 [\$P\$]{.arithmatex} 点的切线 [\$\ell\$]{.arithmatex} 恰好平分 [\$\angle FPP\'\$]{.arithmatex}。

不妨假设角平分线 [\$\ell\'\$]{.arithmatex} 与抛物线相交与 [\$P,Q\$]{.arithmatex} 两点，做 [\$QQ\'\$]{.arithmatex} 垂直于准线。根据抛物线的定义，有 [\$FP=PP\'\$]{.arithmatex}，因此也有 [\$QF=QP\'\$]{.arithmatex}，又因为 [\$FQ=QQ\'\$]{.arithmatex}，因此 [\$P=Q\$]{.arithmatex}，即 [\$\ell=\ell\'\$]{.arithmatex}，证毕。

我们也可以证明角相等，

![alt text](../image-8.avif){width="60%"}

不难得到，只需要证 [\$\angle FPQ=\angle FQP\$]{.arithmatex} 即可。

不妨证明 [\$FP=FQ\$]{.arithmatex}，容易想到，列出直线方程直接求解，得到点的坐标即可。

双曲线的光学性质：从一个焦点发出的光线，经过双曲线的发射后反向延长经过另一个焦点。

证明

与椭圆类似，我们取作差的将军饮马模型，即延长线上的点最小。

与抛物线类似，我们用两边之差小于第三边，也可以证明。

椭圆的旁心：在椭圆上任取两点 [\$P,Q\$]{.arithmatex}，做 [\$F_1PF_2,F_1QF_2\$]{.arithmatex} 的外角角平分线，根据光学性质，也就是说 [\$PR,QR\$]{.arithmatex} 都是椭圆的切线，交于一点 [\$R\$]{.arithmatex}，连接 [\$RF_1\$]{.arithmatex}，则 [\$RF_1\perp PQ\$]{.arithmatex}。

证明：我们知道 [\$R\$]{.arithmatex} 是一个旁切圆的圆心，与 [\$PQ\$]{.arithmatex} 相切与 [\$F\'\$]{.arithmatex}（我们要证明它和 [\$F_1\$]{.arithmatex} 重合），设椭圆与 [\$F_2P,F_2Q\$]{.arithmatex} 相切于 [\$X,Y\$]{.arithmatex}，则 [\$F\'P+PF_2=XF_2\$]{.arithmatex}，[\$F\'Q+QF_2=YF_2\$]{.arithmatex}，因为 [\$RX=RY\$]{.arithmatex} 所以 [\$XF_2=YF_2\$]{.arithmatex}，因此 [\$F\'=F_1\$]{.arithmatex} 即为椭圆焦点。

## 抛物线 {#_28}

### 一般方程 {#_29}

平面内与一个定点 [\$F\$]{.arithmatex} 和一条定直线 [\$\ell\$]{.arithmatex}（不过 [\$F\$]{.arithmatex}）的距离相等的点的轨迹叫做抛物线。点 [\$F\$]{.arithmatex} 叫做抛物线的焦点，直线 [\$\ell\$]{.arithmatex} 叫做抛物线的准线。

![alt text](../desmos-graph%20%286%29.svg){width="40%"}

不妨设 [\$F\$]{.arithmatex} 到准线的距离（焦准距）为 [\$p\$]{.arithmatex} 且垂足为 [\$K\$]{.arithmatex}，容易知道，抛物线的顶点就是 [\$FK\$]{.arithmatex} 的中点，即 [\$F=\paren{\dfrac{p}{2},0},K=\paren{-\dfrac{p}{2},0}\$]{.arithmatex}，不难得到抛物线的标准方程为

::: {.arithmatex}
\$\$ y\^2=2px(p\>0) \$\$
:::

这个是开口朝向 [\$x\$]{.arithmatex} 轴正半轴的，同理我们还有另外四个方向。

### 简单性质 {#_30}

对于抛物线

::: {.arithmatex}
\$\$ y\^2=2px(p\>0) \$\$
:::

有 [\$x\ge0\$]{.arithmatex}，且关于 [\$y=0\$]{.arithmatex} 对称，没有对称中心。

容易知道，二次函数

::: {.arithmatex}
\$\$ f(x)=a\^2+bx+c(a\neq0) \$\$
:::

就是一条抛物线且定点为

::: {.arithmatex}
\$\$ \paren{-\dfrac{b}{2a},f\paren{-\dfrac{b}{2a}}} \$\$
:::

注意：抛物线的离心率恒为 [\$1\$]{.arithmatex}，而焦准距则衡量了开口大小。

### 几何方法 {#_31}

圆锥曲线（通常是抛物线）的弦与过弦的端点的两条切线所围成的三角形，称为**阿基米德三角形**。

如图，过抛物线 [\$x\^2=2py(p\>0)\$]{.arithmatex} 外的点 [\$P\$]{.arithmatex} 作抛物线的两条切线 [\$PA, PB\$]{.arithmatex}，设线段 [\$AB\$]{.arithmatex} 的中点为 [\$M\$]{.arithmatex}，则 [\$PM\$]{.arithmatex} 一定平行（或重合）与抛物线的轴，设线段 [\$PM\$]{.arithmatex} 的中点为 [\$R\$]{.arithmatex}，则 [\$R\$]{.arithmatex} 一定在抛物线上，且抛物线在 [\$R\$]{.arithmatex} 处的切线与 [\$AB\$]{.arithmatex} 平行。

![alt text](../image-1.avif){width="80%"}

不妨设 [\$P(x_0,y_0)\$]{.arithmatex}，直线 [\$AB\$]{.arithmatex} 与 [\$y\$]{.arithmatex} 轴交于点 [\$Q\$]{.arithmatex}，则有：

- [\$k\_{AB} \cdot k\_{PQ} = \dfrac{2y_0}{p}\$]{.arithmatex}；

- [\$k\_{PA} \cdot k\_{PB} = \dfrac{2y_0}{p}\$]{.arithmatex}；

假设 [\$\triangle ABC\$]{.arithmatex} 外切于一条抛物线，即直线 [\$AB\$]{.arithmatex}，[\$BC\$]{.arithmatex}，[\$CA\$]{.arithmatex} 均与抛物线相切，那么 [\$\triangle ABC\$]{.arithmatex} 的垂心始终过抛物线的准线。

![alt text](../image-22.avif){width="40%"}

- 兰伯特定理：由抛物线的三条切线所围成的三角形，其外接圆必经过抛物线的焦点。

- 西姆松定理：点 [\$P\$]{.arithmatex} 到 [\$\triangle ABC\$]{.arithmatex} 各边的投影共线，当且仅当 [\$P\$]{.arithmatex} 位于该三角形的外接圆上。

- 斯坦纳线定理：一个三角形外接圆上任意一点（该点不为三角形顶点）关于三角形三边的对称点，这三个对称点是共线的，并且这条直线（称为斯坦纳线）必经过该三角形的垂心。

下面是关于特征矩形的一些经典问题，选自 Geometry of Conics (Mathematical World VOLUME 26)。

1.  抛物线的焦点关于任意一条切线的对称点一定在准线上。

    证明：做 [\$PP\'\perp\ell\$]{.arithmatex}，根据抛物线的性质，[\$FP=PP\'\$]{.arithmatex}。

    ![alt text](../image-16.avif){width="40%"}

    因为 [\$FP\'\perp\ell\'\$]{.arithmatex}，因此 [\$\ell\'\$]{.arithmatex} 是 [\$\angle FPP\'\$]{.arithmatex} 角平分线，所以，[\$F\$]{.arithmatex} 关于 [\$\ell\'\$]{.arithmatex} 的反射点即为 [\$P\'\$]{.arithmatex} 在准线上。

    推论：抛物线的焦点到其各条切线的投影点，均位于抛物线顶点处的切线上。

2.  假设抛物线在点 [\$X\$]{.arithmatex} 和 [\$Y\$]{.arithmatex} 的切线相交于点 [\$P\$]{.arithmatex}。那么 [\$PX\'=PY\'=PF\$]{.arithmatex}，其中 [\$X\'\$]{.arithmatex} 和 [\$Y\'\$]{.arithmatex} 是 [\$X\$]{.arithmatex} 和 [\$Y\$]{.arithmatex} 在抛物线准线上的投影，而 [\$F\$]{.arithmatex} 是抛物线的焦点。

    证明：根据上一条，这两条切线分别是线段 [\$FX\'\$]{.arithmatex} 和 [\$FY\'\$]{.arithmatex} 的中垂线。因此，它们的交点即为三角形 [\$FX\'Y\'\$]{.arithmatex} 的外接圆圆心。

    ![alt text](../image-17.avif){width="90%"}

    推论：如果 [\$PX\$]{.arithmatex} 和 [\$PY\$]{.arithmatex} 是抛物线的切线，那么点 [\$P\$]{.arithmatex} 在准线上的投影，是 [\$X\$]{.arithmatex} 和 [\$Y\$]{.arithmatex} 在准线上的投影点所构成线段的中点。

3.  做抛物线上两点 [\$X,Y\$]{.arithmatex} 的切线，相交于点 [\$P\$]{.arithmatex}，若 [\$PX\perp PY\$]{.arithmatex}，则 [\$P\$]{.arithmatex} 在抛物线的准线上。反过来，过准线上一点 [\$P\$]{.arithmatex} 做抛物线的两条切线，则他们相互垂直。同时，[\$XY\$]{.arithmatex} 一定过焦点 [\$F\$]{.arithmatex} 且 [\$PF\perp XY\$]{.arithmatex}。

    证明：设 [\$X\',Y\'\$]{.arithmatex} 为 [\$X,Y\$]{.arithmatex} 到准线上的投影，因为 [\$P\$]{.arithmatex} 在准线上，

    ![alt text](../image-18.avif){width="40%"}

    那么 [\$XF=XX\',YF=YY\'\$]{.arithmatex}，因此可以得到两个三角形全等，那么 [\$\angle XPY=90\^\circ\$]{.arithmatex}。

4.  我们做推广，两条切线为 [\$\varphi\$]{.arithmatex} 或 [\$180\^\circ-\varphi\$]{.arithmatex} 的点的集合是一个以 [\$F\$]{.arithmatex} 焦点，抛物线准线 [\$\ell\$]{.arithmatex} 为准线的双曲线，其离心率等于 [\$\|\cos\varphi\|\$]{.arithmatex}。

    ![alt text](../image-19.avif){width="40%"}

    注意到 [\$P\$]{.arithmatex} 为 [\$\triangle FX\'Y\'\$]{.arithmatex} 外心，因此 [\$\angle X\'PY\'=360\^\circ-2\varphi\$]{.arithmatex}，那么 [\$P\$]{.arithmatex} 到准线的距离为 [\$PF\|\cos(180\^\circ-\varphi)\|=PF\|\cos\varphi\|\$]{.arithmatex}，证毕。

5.  设 [\$PX\$]{.arithmatex} 和 [\$PY\$]{.arithmatex} 为过点 [\$P\$]{.arithmatex} 的抛物线的两条切线，并设 [\$l\$]{.arithmatex} 为过 [\$P\$]{.arithmatex} 且平行于抛物线轴的直线。那么直线 [\$PY\$]{.arithmatex} 与 [\$l\$]{.arithmatex} 的夹角等于 [\$\angle XPF\$]{.arithmatex}，且 [\$\triangle XFP\backsim\triangle PFY\$]{.arithmatex}。由此可推知，[\$FP\$]{.arithmatex} 是角 [\$XFY\$]{.arithmatex} 的角平分线。

    设 [\$X\'\$]{.arithmatex} 和 [\$Y\'\$]{.arithmatex} 是 [\$X\$]{.arithmatex} 和 [\$Y\$]{.arithmatex} 在准线上的投影。那么，点 [\$F\$]{.arithmatex}、[\$X\'\$]{.arithmatex} 和 [\$Y\'\$]{.arithmatex} 位于一个以 [\$P\$]{.arithmatex} 为圆心的圆上，

    ![alt text](../image-20.avif){width="40%"}

    因此 [\$\angle X\'Y\'F = \dfrac{1}{2}\angle X\'PF = \angle XPF\$]{.arithmatex}。因为 [\$\ell\$]{.arithmatex} 垂直于 [\$X\'Y\'\$]{.arithmatex}，因此 [\$PY\$]{.arithmatex} 与 [\$\ell\$]{.arithmatex} 的夹角等于 [\$Y\'F\$]{.arithmatex} 与 [\$X\'Y\'\$]{.arithmatex} 的夹角，而 [\$Y\'F\$]{.arithmatex} 垂直于 [\$PY\$]{.arithmatex}。

    由于 [\$l\$]{.arithmatex} 平行于 [\$YY\'\$]{.arithmatex}，[\$PY\$]{.arithmatex} 与 [\$l\$]{.arithmatex} 的夹角等于角 [\$PYY\'\$]{.arithmatex}，根据光学性质，该角等于角 [\$FYP\$]{.arithmatex}。因此 [\$\angle FYP = \angle XPF\$]{.arithmatex}。类似地，[\$\angle FXP = \angle YPF\$]{.arithmatex}。因此 [\$\triangle XFP\backsim\triangle PFY\$]{.arithmatex}。

### 特征梯形 {#_32}

过焦点的直线交抛物线与点 [\$A,B\$]{.arithmatex} 过 [\$A,B\$]{.arithmatex} 做准线 [\$\ell\$]{.arithmatex} 的垂线 [\$AC,BC\$]{.arithmatex}，锁围成的直角梯形称为抛物线的特征直角梯形。

如下图，[\$M\$]{.arithmatex} 点的纵坐标是切点 [\$A,B\$]{.arithmatex} 的纵坐标之和的一半，也就是说，做 [\$AB\$]{.arithmatex} 的中点 [\$M\'\$]{.arithmatex}，则 [\$MM\'\$]{.arithmatex} 是平行于抛物线的轴（图中为 [\$x\$]{.arithmatex} 轴）的。

![alt text](../image-40.avif)

![alt text](../image-45.avif)

![alt text](../image-42.avif)

![alt text](../image-43.avif)

![alt text](../image-44.avif)

![alt text](../image-41.avif)

![alt text](../image-46.avif)

一些结论：

- 对于抛物线 [\$y\^2=2px(p\>0)\$]{.arithmatex}，任意一条过 [\$B(-2p,0)\$]{.arithmatex} 的斜率为 [\$k\$]{.arithmatex} 的割线 [\$PQ\$]{.arithmatex}，则顶点 [\$O\$]{.arithmatex} 到两交点 [\$P,Q\$]{.arithmatex} 的距离之积恒等于 [\$\dfrac{4p\^2}{\|k\|}\$]{.arithmatex}。

- 任意焦点弦的两个端点与原点构成的角都是钝角，即过焦点的直线与抛物线交于 [\$A,B\$]{.arithmatex} 两点，则 [\$\angle AOB\$]{.arithmatex} 一定是钝角。

### 参数方程 {#_33}

我们以标准抛物线

::: {.arithmatex}
\$\$ P:y\^2=2px \$\$
:::

为例，为了简化，不妨用半焦距 [\$c\$]{.arithmatex} 表示为：

::: {.arithmatex}
\$\$ P:y\^2=4cx \$\$
:::

用 [\$t\$]{.arithmatex} 作为参数，不妨设其参数方程为：

::: {.arithmatex}
\$\$ P(t)=(ct\^2,2ct) \$\$
:::

其实，也可以用其他的形式来作为参数方程，但是这个形式显然是最简洁的，因此我们下面说，或者直接用，都是以这个为标准形式。

![alt text](../image-2-9525fa1.avif){width="80%"}

参数方程最好用的地方在于，它将一个点变成了一个纯简洁的参数 [\$t\$]{.arithmatex}，尽管如果直接设点以 [\$x\$]{.arithmatex} 或 [\$y\$]{.arithmatex} 为参数，看似更容易得到结果，但是运算过程会非常复杂，这体现了圆锥曲线部分一个经典的思想------化繁为简，先列后算，最后得到结果，当我们把"列"的过程"变复杂"那么算就会简单，当我们把最后一步变成两步，可能前面就会少一步复杂的运算。

#### 割线问题 {#_34}

参数方程最有用的地方是，抛物线一条弦（割线），我们不妨设弦 [\$PQ\$]{.arithmatex} 中 [\$P(t_1),Q(t_2)\$]{.arithmatex}，那么就有如下非常简洁的性质：

1.  弦 [\$PQ\$]{.arithmatex} 的方程：

    ::: {.arithmatex}
    \$\$ y(t_1+t_2)=2x+2ct_1t_2 \$\$
    :::

2.  弦 [\$PQ\$]{.arithmatex} 的斜率：

    ::: {.arithmatex}
    \$\$ k\_{PQ}=\dfrac{2}{t_1+t_2} \$\$
    :::

3.  弦 [\$PQ\$]{.arithmatex} 的中点：

    ::: {.arithmatex}
    \$\$ M\paren{\dfrac{c}{2}(t_1\^2+t_2\^2),ct_1+ct_2} \$\$
    :::

    其中，[\$M\$]{.arithmatex} 的纵坐标更为简洁的：

    ::: {.arithmatex}
    \$\$ y_M=c(t_1+t_2)=\dfrac{2}{K\_{PQ}} \$\$
    :::

    这就是所谓的"平行弦---直径"定理。

4.  做题做的多的同学会发现，求抛物线中一条直线的定点，其实很多时候就是在 [\$x\$]{.arithmatex} 轴上，甚至就是焦点，因此，我们不妨写出弦与 [\$x\$]{.arithmatex} 轴的焦点------令 [\$y=0\$]{.arithmatex} 即可得到：

    ::: {.arithmatex}
    \$\$ T(-ct_1t_2,0) \$\$
    :::

    因此就有焦弦判定：

    弦 [[\$PQ\$]{.arithmatex}]{.arithmatex} 过焦点 [[\$\iff t_1t_2=-1\$]{.arithmatex}]{.arithmatex}

5.  中点弦公式，若某条弦的中点是 [\$M(x_1,y_1)\$]{.arithmatex}，那么这条弦的方程为：

    ::: {.arithmatex}
    \$\$ yy_1-2c(x+x_1)=y_1\^2-4cx_1 \$\$
    :::

    这就是常说的 [\$T=S_1\$]{.arithmatex} 形式。立刻推出：中点在抛物线上 ⇒ 弦退化为切线。

    经典题：过顶点 [\$O(0,0)\$]{.arithmatex} 的所有弦，其中点轨迹是什么？[\$y\^2=2cx\$]{.arithmatex}，与原抛物线 [\$y\^2=4cx\$]{.arithmatex} 相比，就是焦距减半。

    更一般：过定点 [\$P(x_2,y_2)\$]{.arithmatex} 的所有弦，其中点轨迹？也是一条抛物线，但是顶点不在坐标原点了，我们不再考虑了。

#### 切线问题 {#_35}

此外，参数方程还可以用于表示切线，容易发现抛物线在 [\$P(t_0)\$]{.arithmatex} 处的切线方程为：

::: {.arithmatex}
\$\$ T(t):ty=x\^2+ct \$\$
:::

而两条切线 [\$T(m),T(n)\$]{.arithmatex} 的交点为：

::: {.arithmatex}
\$\$ T(m)\cap T(n)=(cmn,cm+cn) \$\$
:::

你会发现：弦方程里出现 [\$t_1t_2,t_1+t_2\$]{.arithmatex}，而切线交点坐标也只依赖这两个量------这就是抛物线弦题"参数法秒杀"的根源。

#### 焦弦专题 {#_36}

前面已经提到过，焦弦的判定，或者说充要条件是 [\$t_1t_2=-1\$]{.arithmatex}，也就是说，我们可以设焦弦 [\$PQ\$]{.arithmatex} 的两点分别是 [\$P(t),Q(-1/t)\$]{.arithmatex}，因此：

::: {.arithmatex}
\$\$ \|PF\|=c(1+t\^2) \$\$
:::

::: {.arithmatex}
\$\$ \|QF\|=c\paren{1+\dfrac{1}{t\^2}} \$\$
:::

::: {.arithmatex}
\$\$ \|PQ\|=c\paren{t+\dfrac{1}{t}}\^2\ge 4c \$\$
:::

当且仅当 [\$t=\pm 1\$]{.arithmatex} 取等号，此时 [\$PQ\$]{.arithmatex} 就是通径（latus rectum），长度 [\$4a\$]{.arithmatex}，同时还有一个很漂亮的不变量（常用于竞赛简化）：

::: {.arithmatex}
\$\$ \dfrac{1}{\|PF\|}+\dfrac{1}{\|QF\|}=\dfrac{1}{c} \$\$
:::

几何拓展：以任意焦弦为直径的圆与准线相切。以任意焦弦为直径作圆，该圆与准线相切。这类题常见于"圆---抛物线---焦点/准线"的综合证明。

#### 极线极点 {#_37}

弦与切线的对偶结构------**关键对偶**：弦 [\$PQ\$]{.arithmatex} 是其端点切线交点 [\$R\$]{.arithmatex} 的**极线**（polar）。

- 切线与切点（参数式）：在 [\$P(t)\$]{.arithmatex} 处切线为 [\$ty=x+at\^2\$]{.arithmatex}。

- 两切线交点（切线 [\$t_1\$]{.arithmatex} 与 [\$t_2\$]{.arithmatex} 的交点）：[\$(at_1t_2,at_1+at_2)\$]{.arithmatex}。

**极线理论**：点 [\$(x_1, y_1)\$]{.arithmatex} 关于抛物线 [\$y\^2=4ax\$]{.arithmatex} 的极线方程为 [\$yy_1 = 2a(x + x_1)\$]{.arithmatex}。当点在曲线外时，该直线即为接触弦。将切线交点 [\$R(at_1t_2, a(t_1+t_2))\$]{.arithmatex} 代入公式：

::: {.arithmatex}
\$\$ y \cdot a(t_1+t_2) = 2a(x + at_1t_2) \implies (t_1+t_2)y = 2x + 2at_1t_2 \$\$
:::

这恰好就是弦 [\$PQ\$]{.arithmatex} 的方程。你不必在"弦、切线、过定点、轨迹"之间乱跳；把弦看成某个点的极线，把"二点确定一线"升级为"对偶变换"，许多复杂轨迹题会突然变成"某点满足某方程"。

**La Hire 定理（互反性质）**：若点 [\$P\$]{.arithmatex} 在点 [\$Q\$]{.arithmatex} 的极线上，则点 [\$Q\$]{.arithmatex} 必在点 [\$P\$]{.arithmatex} 的极线上。
