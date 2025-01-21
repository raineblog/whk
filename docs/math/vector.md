# 平面向量

## 有向线段

带有方向的线段称为有向线段。有向线段的三要素为：起点、方向、长度。

根据初等几何，那么只要知道这三要素，这个有向线段就已经被确定了，也就是终点可知。

从另一个角度思考，也可以认为是知道起点、终点，就可以唯一的确定一个有向线段。

一个有向线段由其两个端点表示，记为 $\overrightarrow{AB}$ 或 $\bm{a}$，同时我们记其长度，称为**向量的模**。

### 向量

向量（vector）又称欧几里得向量（Euclidean vector）。

目前没有准确而统一的中文翻译，在物理、工程中通称矢量。

一般指一个同时具有大小和方向，且满足平行四边形法则的几何对象。

向量是数学、物理学和工程科学等多个自然科学中的基本概念。 

与向量相对的概念称标量、纯量、数量，即：

只有大小、绝大多数情况下没有方向（电流是特例）、不满足平行四边形法则的量。

**固定向量**：尤其在物理学领域，有些向量会与起点有关（力与其的作用点有关，质点运动速度与该质点的位置有关），因而假设向量有确定的起点和终点，当起点和终点改变后，构成的向量就不再是原来的向量。这样的向量也被称为固定向量。

**自由向量**：向量的位置可自由移动。在另一些时候，由于向量的共性都具有大小和方向，会认为向量的起点和终点并不那么重要。两个起点不一样的向量，只要大小相等，方向相同，就可以称为是同一个向量。这样的向量被称为自由向量。在数学中，一般只研究自由向量，并且数学中所指的向量就是指自由向量。也就是只要大小以及方向一样，即可视为同一向量，与向量的起始点并无关系。

特殊的向量：遇到某些特殊情况（如表示磁场的磁感应强度）需要表示与记载纸面垂直的向量，则会使用圆圈中打叉或打点的方式来表示（如右图）。圆圈中带点的记号（⊙）表示由纸下方指向纸上方的向量，而圆圈中带叉的记号（⊗）则表示由纸的上方指向纸下方的向量。由于这种记号不表示向量的大小，所以必须时需要在旁边或其它地方另外注明。

下文为高中数学中定义的向量。

无特殊说明，下文的向量均指**自由向量**，大部分都是**平面向量**。

既有大小又有方向的量称为向量。这个定义很抽象，我们逐个分解。

我们已经有了有向线段，但是实际应用中，大部分时候，向量的位置并不重要。

于是我们将有向线段的起点不固定，将一个有向线段抽象为一个可以随意移动的量。

此时，你也许发现了。有向线段其实可以再次表示为，起点和一个向量。

我们通常把向量表示在平面直角坐标系内，没有说明的情况下，起点通常标在坐标轴原点。

我们取这个向量在横、纵坐标上延伸的长度作为两个元素，将向量记为 $(a,b)$。

那么我们就得出了向量的几何意义，即向量 $(a,b)$ 表示向右走 $a$、向上走 $b$ 的位移。

已知两点 $A(a,b),B(c,d)$，易证
$\overrightarrow{AB}=(c-a,d-b)$。

### 向量的模

对于一个向量 $\vec a$，有向线段
$\vec a$ 的长度称为向量的模，即为这个向量的大小。

符号表示为 $|\bm a|$ 或 $|\overrightarrow{AB}|$ ，根据勾股定理，我们知道 $|\vec a|=|(x,y)|=\sqrt{x^2+y^2}$。

### 特殊的向量

**零向量**：模为 $0$ 的向量，零向量的方向任意（不过其实是无意义）。一般记为：$\vec 0$。

**单位向量**：模为 $1$ 的向量称为单位向量。一般记为 $\bm e$，最常见的单位向量就是基向量。

**基向量**：$\bm i=(1,0)$ 表示 $x$ 方向的单位向量，$\bm j=(0,1)$ 表示 $y$ 方向的单位向量。

**平行向量**：方向相同或相反的两个非零向量，规定零向量与任何向量平行。记作： $\bm x\parallel\bm y$。

**共线向量**：任一组平行向量都可以平移到同一直线上，所以平行向量又叫共线向量。

**相等向量**：模相等且方向相同的向量。**相反向量**：模相等且方向相反的向量。

## 向量的线性运算

### 向量数乘

我们规定实数 $\lambda$ 与向量 $\bm a$ 的积为一个向量，称为向量的数乘运算，记作 $\lambda\vec a$。

我们定义 $\lambda\bm a=\lambda(x,y)=(\lambda x,\lambda y)$。据此，我们可以得出以下向量数乘常用的结论：

- $|\lambda\bm a|=|\lambda||\bm a|$；
- 当 $\lambda >0$ 时，$\lambda\bm a$ 与 $\bm a$ 同向；
- 当 $\lambda =0$ 时，$\lambda \bm a=\vec 0$；
- 当 $\lambda<0$ 时，$\lambda \bm a$ 与 $\bm a$ 方向相反。

根据数乘的定义，可以得出向量的数乘满足交换律、结合律、分配律等，即，

$$
\lambda(\mu\bm a)=(\lambda\mu)\bm a\\
\lambda(\bm a+\bm b)=\lambda\bm a+\lambda\bm b\\
(\lambda+\mu)\bm a=\lambda\bm a+\mu\bm a\\
(-\lambda)\bm a=-(\lambda\bm a)=\lambda(-\bm a)
$$

### 向量加法

注意，向量的数乘本质上也属于向量的线性运算，不过我把他们分开，方便理解。

下面讨论向量的加法，类比的，向量的减法可以从公式入手理解。

类比物理中的位移，从 $A$ 经 $B$ 到 $C$，那么经过的位移等价于直接从 $A$ 到 $C$。

符号表示即：$\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$，其实这个也就是三角形法则所表述的。

向量减法类似：$\overrightarrow{OA}-\overrightarrow{OB}=\overrightarrow{OA}+\overrightarrow{BO}=\overrightarrow{BA}$，后面用到了交换律。

同时，注意到力的合成法则（平行四边形法则），同样也可以看做向量的相加。

因此，我们得出向量相加的两个运算法则，即三角形法则、平行四边形法则：

- 三角形法则：首尾顺次相连，和为从第一个向量的起点指向最后一个向量的终点；
- 平行四边形法则：向量共起点，和为以这两个向量为邻边的平行四边形的对角线，  
  起点为两个向量共有的起点，方向沿平行四边形对角线方向。

这样，向量的加法就具有了几何意义。并且向量的加法满足交换律与结合律。

然后从几何的角度可以推出一些公式，其中三角形法则的公式比较简单，如下：

$$
(x_1,y_1)+(x_2,y_2)=(x_1+x_2,y_1+y_2)
$$

向量加法满足结合律和交换律，画图理解即可。

向量加法可以导出三角形不等式，

$$
||\bm a|-|\bm b||\le|\bm a+\bm b|\le|\bm a|+|\bm b|
$$

当且仅当两向量方向相同（注意不是平行），取等。

## 向量的点积

### 声明

对于向量的乘法：

|物理|数学|直译|俗称|
|:-:|:-:|:-:|:-:|
|标量积|数量积|内积|点积|
|矢量积|向量积|外积|叉积|

物理和数学上的用语采用了意译的方法，分别表示运算的结果为标量和矢量。

在数学学科，通常也可以翻译成「内积」和「外积」，是两个名词的直译。

而「点积」和「叉积」是根据运算符号得来的俗称，这种俗称也很常见。

### 定义

*点积的概念对于任意维数的向量都适用*。

已知两个向量 $\bm a,\bm b$ ，它们的夹角为 $\theta$，那么这两个向量的点积为：

$$
\bm a \cdot \bm b=|\bm a||\bm b|\cos \theta
$$

其中，我们称 $|\bm a|\cos \theta$ 为 $\bm a$ 在 $\bm b$ 方向上的投影。

其中，$\theta\in[0,\pi]$，但是直线的夹角 $\theta\in[0,\pi)$，因为相反向量是完全不同的。

### 意义

点积的几何意义即为：点积 $\bm a \cdot \bm b$ 等于 $\bm a$ 的模与 $\bm b$ 在 $\bm a$ 方向上的投影的乘积。

另外，我们定义向量点积数值上表示为（简记为先相乘再相加）：

$$
(x_1,y_1)\cdot(x_2,y_2)=x_1x_2+y_1y_2
$$

可以发现，这种运算得到的结果是一个标量，并不属于向量的线性运算。

向量与零向量点积，结果为 $\vec0$。在不引起混淆的情况下，点积的点号可以省略不写。

### 性质

向量点乘满足交换律：

$$
\bm a\cdot\bm b=\bm b\cdot\bm a=|\bm a|\cdot|\bm b|\cdot\cos\theta
$$

向量点乘对数乘有结合律：

$$
(\lambda\bm a)\cdot\bm b=\lambda(\bm a\cdot\bm b)=\bm a\cdot(\lambda\bm b)
$$

向量点乘对向量加法有分配率：

$$
(\bm a+\bm b)\cdot\bm c=\bm a\cdot\bm c+\bm b\cdot\bm c
$$

但是向量点乘不满足结合律，

$$
(\bm a\cdot\bm b)\cdot\bm c\neq\bm a\cdot(\bm b\cdot\bm c)
$$

注意到向量运算具有大部分的数字运算的性质（除了除法），因此可以当做字母计算。

可以得到，若 $\bm b\neq\bm c$，$\bm a\cdot\bm b=\bm a\cdot\bm c$ 的充要条件是 $\bm a\perp(\bm b-\bm c)$，

$$
\bm a\cdot\bm b=\bm a\cdot\bm c\\
\bm a\cdot(\bm b-\bm c)=\vec0
$$

即，

$$
\bm a\perp(\bm b-\bm c)
$$

我们可以发现，

$$
|\bm a+\bm b|^2-|\bm a-\bm b|^2=4\bm a\cdot\bm b\\
\bm a\cdot\bm b={1\over4}\left(|\bm a+\bm b|^2-|\bm a-\bm b|^2\right)
$$

即极化恒等式，我们可以不通过求夹角的方式得出两向量点积。

同时，常用的，

$$
\begin{aligned}
|\bm a+\bm b|&=\lambda\\
(\bm a+\bm b)\cdot(\bm a+\bm b)&=\lambda^2\\
|\bm a|^2+2\bm a\cdot\bm b+|\bm b|^2&=\lambda^2
\end{aligned}
$$

即，

$$
|\bm a|^2+2\bm a\cdot\bm b+|\bm b|^2=|\bm a+\bm b|^2\\
\bm a\cdot\bm b={1\over2}\left(|\bm a+\bm b|^2-|\bm a|^2-|\bm b|^2\right)\\
$$

总结一下，上面两个式子，

$$
\bm a\cdot\bm b={1\over4}\left(|\bm a+\bm b|^2-|\bm a-\bm b|^2\right)\\
\bm a\cdot\bm b={1\over2}\left(|\bm a+\bm b|^2-|\bm a|^2-|\bm b|^2\right)\\
$$

再结合点乘的定义，

$$
\bm a\cdot\bm b=|\bm a|\cdot|\bm b|\cdot\cos\theta\\
\cos\theta={\bm a\cdot\bm b\over|\bm a|\cdot|\bm b|}
$$

就可以求出向量夹角。


特殊的，

$$
\theta=0\,(\cos\theta=1),\,\bm a\cdot\bm b=|\bm a|\cdot|\bm b|\\
\theta=\pi\,(\cos\theta=-1),\,\bm a\cdot\bm b=-|\bm a|\cdot|\bm b|\\
\theta=\pi/2\,(\cos\theta=0),\,\bm a\cdot\bm b=0\\
\bm a\cdot\bm a=|\bm a|^2,\,|\bm a|=\sqrt{\bm a\cdot\bm a}\\
$$

其中，第三条即，垂直向量向量点积等于零。

根据 $\cos 90^\circ=0$，$\bm a \perp \bm b \iff \bm a\cdot \bm b=0$。

### 柯西不等式向量形式

$$
|\bm a\cdot\bm b|\le|\bm a|\cdot|\bm b|
$$

当且仅当两向量共线，取等。

据此，可以判断两向量共线：

两个非零向量 $\bm a$ 与 $\bm b$ 共线，等价于，有唯一实数 $\lambda$，使得 $\bm b=\lambda \bm a$。

由数乘的定义知，对于非零向量 $\bm a$，如果存在实数 $\lambda$，使得 $\bm b=\lambda \bm a$，那么 $\bm a \parallel \bm b$。

数值上，有判别式 $\bm a = \lambda \bm b \iff |\bm a\cdot \bm b|=|\bm a||\bm b|$。

## 平面直角坐标系中的应用

### 平面向量基本定理

若基底 $\bm e_1,\bm e_2$ 不共线，则对于平面内任一向量 $\bm a$，存在唯一实数 $x,y$ 使得 $\bm a=x\bm e_1+y\bm e_2$。

形式化的，平面内的任一向量都可以唯一的表示为两个不共线向量的线性组合。

存在性的证明：感性理解（雾

唯一性的证明，反证：假设存在两组实数 $\langle x_1,y_1\rangle$、$\langle x_2,y_2\rangle$，

$$
\bm a=x_1\bm e_1+y_1\bm e_2=x_2\bm e_1+y_2\bm e_2\\
\bm e_1(x_1-x_2)=\bm e_2(y_2-y_1)
$$

因为 $x_1\neq x_2,y_1\neq y_2$，则 $\bm e_1,\bm e_2$ 共线，与条件不符，因此存在唯一性。

考虑构造性的证明，

若，

$$
\bm a\cdot\bm e_1=a_1,\,\bm a\cdot\bm e_2=a_2\\
\langle\bm e_1,\bm e_2\rangle=\theta
$$

设，$\bm a=x\bm e_1+y\bm e_2$，用 $a_1,a_2,\theta$ 表示 $\bm a$。

考虑，

$$
\bm e_1\bm e_2=\cos\theta\\
\bm a\cdot\bm e_1=x+y\bm e_1\bm e_2=a_1\\
\bm a\cdot\bm e_2=y+x\bm e_1\bm e_2=a_2
$$

列出方程组，

$$
\begin{cases}
x+y\cos\theta=a_1\\
y+x\cos\theta=a_2
\end{cases}
$$

解得，

$$
\left\{\begin{aligned}
x={a_1-a_2\cos\theta\over\sin^2\theta}\\
y={a_2-a_1\cos\theta\over\sin^2\theta}
\end{aligned}\right.
$$

这个思想很重要，常用一个很奇怪的式子，去点乘两个不共线向量。

### 线段中点

设 $A(x_1,y_1)$、$B(x_2,y_2)$ 为一平面内两点。

设 $C(x,y)$ 为线段 $AB$ 中点，则 $\overrightarrow{AC}=\overrightarrow{CB}$：

$$
x-x_1=x_2-x\\
y-y_1=y_2-y
$$

最终解得，

$$
C\left({x_1+x_2\over2},{y_1+y_2\over2}\right)
$$

即中点坐标。

### 线段长度

设 $A(x_1,y_1)$、$B(x_2,y_2)$ 为一平面内两点，则，

$$
|\overrightarrow{AB}|=\sqrt{\overrightarrow{AB}\cdot\overrightarrow{AB}}=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}
$$

则线段 $AB$，

$$
|AB|=|\overrightarrow{AB}|=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}
$$

即线段长度。

### 三点共线

对于线段 $AB$ 及一点 $Q$，若存在一点 $O$ 满足，

$$
\overrightarrow{OQ}=\lambda\overrightarrow{OA}+(1-\lambda)\overrightarrow{OB}
$$

则 $Q$ 在直线 $AB$ 上，即 $A,B,Q$ 三点共线。

类似的，若 $C$ 是线段 $AB$ 中点，则对于任意一点 $O$，有，

$$
\overrightarrow{OC}={1\over2}\overrightarrow{OA}+{1\over2}\overrightarrow{OB}
$$

## 解三角形

### 三角形的心

| 编号 | 心的名称| 定义 |
| :-: | :-: | :-: |
| $X_1$ | 内心 | 三条**角平分线**的交点 |
| $X_2$ | 重心 | 三条**中线**的交点 |
| $X_3$ | 外心 | 三条**中垂线**的交点 |
| $X_4$ | 垂心 | 三条**高线**的交点  |

### 三角形重心

存在有塞瓦定理、塞瓦定理逆定理。

0. 三角形重心到其各个顶点向量之和为零。

1. 一个三角形的重心同时也是其中点三角形的重心。

2. 重心到顶点的距离与重心到对边中点的距离之比为 $2:1$。

3. 在平面直角坐标系中，重心的坐标是顶点坐标的算术平均。

4. 重心和三角形任意两个顶点组成的三个三角形面积相等。

5. 重心到三条边的距离与三条边的长成反比。（上一条的推论）

6. 重心到三边距离之积最大、到三角形三个顶点距离的平方和最小。

7. 瓦塞定理：三顶点选一个作为起点，定一方向，绕一圈，三组比例相乘为一。

### 正弦定理

回顾初中几何，三角形面积，

$$
S={1\over2}ab\sin C={1\over2}bc\sin A={1\over2}ac\sin B
$$

下面的证明过程只考虑锐角三角形，对于钝角三角形，结论不变。

做过 $\angle A$ 的垂线，则该垂线长度 $h$：

$$
h=b\sin C=c\sin B
$$

对每个角应用，最后可得，

$$
{a\over\sin A}={b\over\sin B}={c\over\sin C}=k
$$

做出该三角形的外接圆，过圆心做 $BC$ 的高，则，

$$
a=2R\sin A,\,{a\over\sin A}=2R
$$

即值 $k$ 为三角形外接圆直径 $2R$。

常常这么写：

$$
a=2R\sin A,\,b=2R\sin B,\,c=2R\sin C\\
\sin A={a\over2R},\,\sin B={b\over2R},\,\sin C={c\over2R}
$$

正弦定理推论：大边对大角，小边对小角。

三角形外接圆半径：

$$
R={abc\over4S}
$$

### 余弦定理

在 $\triangle ABC$ 中，

$$
\begin{array}{c}
\overrightarrow{AB}=\overrightarrow{CB}-\overrightarrow{CA}\\[0.5em]
|\overrightarrow{AB}|^2=|\overrightarrow{CB}|^2+|\overrightarrow{CA}|^2-2|\overrightarrow{CB}|\cdot|\overrightarrow{CA}|\cdot\cos\theta\\[0.5em]
c^2=a^2+b^2-2ab\cos\theta
\end{array}
$$

其中 $\theta$ 为 $c$ 的对角，即 $\angle C$；第二步就是两边平方。

常写作：

$$
\cos A={b^2+c^2-a^2\over2bc},\,\cos B={a^2+c^2-b^2\over2ac},\,\cos C={a^2+b^2-c^2\over2ab}
$$

推论：

$$
\begin{aligned}
a^2+b^2-c^2>0 &\Longrightarrow \cos C>0 \Longrightarrow C\in(0,\pi/2)\\
a^2+b^2-c^2=0 &\Longrightarrow \cos C=0 \Longrightarrow C=\pi/2\\
a^2+b^2-c^2<0 &\Longrightarrow \cos C<0 \Longrightarrow C\in(\pi/2,\pi)
\end{aligned}
$$

### 解三角形

回忆初中平几，根据全等三角形的判断：

如果知道 ASA、AAS、SAS、SSS、HL 就可以唯一的确定一个三角形。

总结一下就是两个角全都可以，三个边可以，一个角两个边就需要是夹角。

即知道 $aCb$、$cBa$、$bAc$，才可以唯一确定一个两边一角的三角形。

至于 SSA，只有一个角是直角才可以唯一确定，不过这个就是 HL 了。

三角形确定，意味着我们可以求出所有边的长度以及所有角度的大小。

正弦定理、余弦定理就为我们提供了方法：可以利用角度和边长互相表示。

像这样，确定三角形边、角的过程，就是解三角形。

如何选择正弦定理、余弦定理？

遇到正弦选正弦定理，遇到齐次式考虑正弦定理。

遇到余弦选余弦定理，遇到边的二次齐次式考虑余弦定理。

原则：边角统一。

### 中线长定理

在 $\triangle ABC$ 中，$BC$ 的中点为 $M$，对于中线 $AM$，有：

$$
AM^2={1\over2}b^2+{1\over2}c^2-{1\over4}a^2
$$

或，

$$
AM^2+BM^2={1\over2}(AC^2+AB^2)
$$

或，

$$
AM={1\over2}\sqrt{2b^2+2c^2-a^2}
$$

证明，基底分解：

$$
\overrightarrow{AM}={1\over2}\overrightarrow{AB}+{1\over2}\overrightarrow{AC}\\[0.5em]
\overrightarrow{BM}={1\over2}\overrightarrow{AC}-{1\over2}\overrightarrow{AB}
$$

则，

$$
|\overrightarrow{AM}|^2+|\overrightarrow{BM}|^2={1\over2}|\overrightarrow{AB}|^2+{1\over2}|\overrightarrow{AC}|^2
$$

或者中点两个底角分别列余弦定理，相加化简。

### 角平分线定理

在 $\triangle ABC$ 中，$\angle A$ 的平分线 $AM$，有：

$$
{BM\over CM}={AB\over AC}
$$

是分角定理的直接推论，证明见下。

### 分角定理

在 $\triangle ABC$ 中，$BC$ 上有一点 $M$，则：

$$
{BM\over CM}={AB\sin\angle BAM\over AC\sin\angle CAM}
$$

证明，左右两边等面积法：

$$
{BM\over CM}={S_{\triangle ABM}\over S_{\triangle ACM}}={AB\cdot AM\sin\angle BAM\over AC\cdot AM\sin\angle CAM}={AB\sin\angle BAM\over AC\sin\angle CAM}
$$

或正弦定理：

$$
{BM\over\sin\angle BAM}={AB\over\sin\angle AMB}\\[0.5em]
{CM\over\sin\angle CAM}={AC\over\sin\angle AMC}
$$

上下做比。Q.E.D.

### 海伦公式

任意三角形面积可以表示为：

$$
\begin{aligned}
S&=\sqrt{p(p-a)(p-b)(p-c)}\\
p&={a+b+c\over2}
\end{aligned}
$$

其中 $p$ 为三角形的半周长。


### 奔驰定理

在锐角 $\triangle ABC$ 中，

$$
S_{\triangle BOC}\cdot\overrightarrow{OA}+S_{\triangle AOC}\cdot\overrightarrow{OB}+S_{\triangle AOB}\cdot\overrightarrow{OC}=\vec0
$$

推论：

+ 设 $I$ 为内心，则 $a\cdot\overrightarrow{IA}+b\cdot\overrightarrow{IB}+c\cdot\overrightarrow{IC}=\vec0$.

+ 设 $H$ 为垂心，则 $\tan A\cdot\overrightarrow{HA}+\tan B\cdot\overrightarrow{HB}+\tan C\cdot\overrightarrow{HC}=\vec0$.

+ 设 $O$ 为外心，则 $\sin2A\cdot\overrightarrow{OA}+\sin2B\cdot\overrightarrow{OB}+\sin2C\cdot\overrightarrow{OC}=\vec0$.

### 布雷特施奈德公式

任意四边形面积可以表示为：

$$
\begin{aligned}
S&=\sqrt{(p-a)(p-b)(p-c)(p-d)-abcd\cos^2{\alpha+\beta\over2}}\\
p&={a+b+c+d\over2}
\end{aligned}
$$

其中 $p$ 为四边形的半周长，$\alpha,\beta$ 为其中二个对角。

布雷特施奈德公式可视为婆罗摩笈多公式之推广。 

### 婆罗摩笈多公式

注意到圆内接四边形对角互补，其半角余弦值为零，$\cos90^\circ=0$ 则圆内接四边形面积可以简化为：

$$
\begin{aligned}
S&=\sqrt{(p-a)(p-b)(p-c)(p-d)}\\
p&={a+b+c+d\over2}
\end{aligned}
$$

其中 $p$ 为四边形的半周长。

### 一些结论

在三角形中，$a=b\cos C+c\cos B$。

若 $\sin^2A+\sin^2B=\sin^2C$，则该三角形是以 $\angle C$ 为直角的 $\mathrm{Rt\triangle}$。

解三角形里面常用的奇怪三角函数：

$$
\sin15^\circ=\cos75^\circ={\sqrt6-\sqrt2\over4}\\[0.5em]
\sin75^\circ=\cos15^\circ={\sqrt6+\sqrt2\over4}
$$

## 例题

### 例题一

$$
2\cos^2{B\over2}+\sqrt3\sin B=3
$$

+ 求 $B$.

$$
\cos B=2\cos^2{B\over2}-1\\
\cos B+\sqrt3\sin B=2\\
{\sqrt3\over2}\sin B+{1\over2}\cos B=1\\
\sin B\cos30^\circ+\cos B\sin30^\circ=1\\
\sin(B+30^\circ)=1=\sin90^\circ\\
B=60^\circ
$$

### 例题二

$$
(\sin B-\sin C)^2=\sin^2 A-\sin B\sin C
$$

+ 求 $A$.
+ 若 $\sqrt2a + b= 2c$，求 $C$.

观察到是角的二次齐次式，且都是正弦，考虑正弦定理，

$$
(\sin B-\sin C)^2=\sin^2 A-\sin B\sin C\\\\
(b-c)^2=a^2-bc\\\\
b^2+c^2-2bc=a^2-bc\\\\
a^2=b^2+c^2-bc
$$

于是，

$$
\cos A={b^2+c^2-a^2\over2bc}={1\over2}\\\\
A=60^\circ
$$

观察到 $\sqrt2a + b= 2c$ 为边的一次齐次，考虑用正弦定理。

$$
\sqrt2a+b=2c\\\\
\sqrt2\sin A+\sin B=2\sin C
$$

根据上一问，$\sin A=\sin60^\circ=\sqrt3/2$，

$$
\sqrt6/2+\sin B=2\sin C\\\\
\sqrt6/2+\sin(120-C)=2\sin C\\\\
\sqrt6/2+\sqrt3/2\cos C+\sin C/2=2\sin C
$$

继续整理，

$$
{\sqrt6\over2}+{\sqrt3\over2}\cos C+{1\over2}\sin C=2\sin C\\\\
{3\over2}\sin C-{\sqrt3\over2}\cos C={\sqrt6\over2}\\\\
{\sqrt3\over2}\sin C-{1\over2}\cos C={\sqrt2\over2}\\\\
\sin C\cos30^\circ-\cos C\sin30^\circ={\sqrt2\over2}\\\\
\sin(C-30^\circ)={\sqrt2\over2}=\sin45^\circ
$$

因为 $C \in (0^\circ,120 ^\circ)$，$C-30^\circ\in(-30^\circ,90^\circ)$，因此，

$$
C-30^\circ=45^\circ,\ C=75^\circ
$$

### 例题三

在锐角 $\triangle ABC$ 中，

$$
2b\sin A-\sqrt3a=0
$$

+ 求 $B$.
+ 求 $\cos A+\cos B+\cos C$ 的取值范围.

不考虑 $\sin A$ 是边的二次齐次式，于是应用正弦定理，

$$
2\sin B\sin A-\sqrt2\sin A=0\\\\
2\sin B=\sqrt3\\
\sin B=\sqrt3/2
$$

因为 $\angle B$ 是锐角，

$$
B=60^\circ
$$

设，

$$
\def\degree{^\circ}
\begin{aligned}
S&=\cos A+\cos B+\cos C\\
&=\cos A+\cos C+1/2\\
&=\cos(120\degree-C)+\cos C+1/2\\
&=-{1\over2}\cos C+{\sqrt3\over2}\sin C+\cos C+{1\over2}\\
&={\sqrt3\over2}\sin C+{1\over2}\cos C+{1\over2}\\
&=\sin C\cos30\degree+\cos C\sin30\degree
+1/2\\
&=\sin(C+30\degree)+1/2
\end{aligned}
$$

因为 $0^\circ<A,B,C<90^\circ$，

$$
\def\degree{^\circ}
\begin{cases}
0\degree<&C&<90\degree\\
0\degree<&B&<90\degree
\end{cases}
\Longleftrightarrow
\begin{cases}
0\degree<&C&<90\degree\\
0\degree<&120-C&<90\degree
\end{cases}
$$

即，$30^\circ<C<90^\circ$，$60^\circ<C+30^\circ<120^\circ$。

画出单位圆，易得 $\sin(C+30\degree)\in(\sqrt3/2,1]$，即，

$$
\cos A+\cos B+\cos C\in\left({\sqrt3+1\over2},{3\over2}\right]
$$

### 例题四

在 $\triangle ABC$ 中，$a+b=11$，

$$
\cos A={1\over8},\,\cos B={9\over16}
$$

+ 求 $a,b$。

考虑余弦转正弦，因为是三角形的角，因此正弦值非负，

$$
\sin A=\sqrt{1-\cos^2 A}=\sqrt{63\over64}={3\sqrt7\over8}\\
\sin B=\sqrt{1-\cos^2 B}=\sqrt{175\over256}={5\sqrt7\over16}
$$

$$
{a\over b}={\sin A\over\sin B}={6\over5}
$$

因此 $a=6,\,b=5$。

### 例题五

$$
{\sin A\over\sin B-\sin C}={b+c\over b-a}
$$

+ 求 $\cos C$。

考虑 $\cos C$ 可以怎么表示，可以通过 $\sin C$ 用毕达哥拉斯定理，也可以余弦定理。

考虑到这个原形式是一次齐次，因此考虑角化变。

$$
{a\over b-c}={b+c\over b-a}\\
b^2-c^2=ab-a^2\\
c^2=a^2+b^2-ab
$$

因此，

$$
\cos C={a^2+b^2-c^2\over2bc}={1\over2}
$$

### 例题六

若，

$$
\begin{cases}
\sin A=3\sin B\\
c=\sqrt5\\
\cos C=5/6
\end{cases}
$$

+ 求 $a$。

尝试考虑这三个东西各自什么用。

最容易发现第二个式子最简单，可以最后带入用。

因为 $\cos$ 关于余弦定理，关于边数多，因此考虑后用。

第一个式子结构很好，是一次齐次，因此带入第一个正弦定理。

$$
a=3b
$$

又因为，

$$
\cos C={a^2+b^2-c^2\over2ab}
$$

带入即可，解得 $a=3$。

### 例题七

若，

$$
\begin{cases}
b\sin2A=a\sin B\\
c=2b
\end{cases}
$$

+ 求 $a/b$。

考虑到第二个式子的形式很简单，因此用于消元。

第一个形式中，出现了二倍角，是不好处理的，因此考虑正弦定理。

$$
\sin B\sin2A=\sin A\sin B\\
\sin A=\sin2A\\
\sin A=2\sin A\cos A\\
\cos A=1/2
$$

考虑到 $a/b$ 是一个一次其次的比例式，因此余弦定理，

$$
\cos A={b^2+c^2-a^2\over2bc}
$$

带入，解得 $a^2=3b^2$，即 $a/b=\sqrt3$。

### 例题八

在 $\triangle ABC$ 中，

$$
S=a^2-(b-c)^2
$$

- 求 $\sin A$。

这个式子没有很好的性质，考虑展开，

$$
S=a^2-b^2-c^2+2bc
$$

注意到这个形式，而且还是二次齐次式，根据余弦定理，

$$
a^2=b^2+c^2-2bc\cos A
$$

有，

$$
S=2bc(1-\cos A)={1\over2}bc\sin A\\
\sin A=4-4\cos A
$$

联立得方程，

$$
(4-4\cos A)^2+\cos^2A=1\\
16(1-\cos A)^2=(1-\cos A)(1+\cos A)\\
16-16\cos A=1+\cos A\\
\cos A={15\over17},\,
\sin A={8\over17}
$$

### 例题九

在 $\triangle ABC$ 中，

$$
\sin A=2\sin B\cos C\\
a^2=b^2+c^2-bc
$$

+ 求，$\triangle ABC$ 形状。

两个式子都很典型，第二个好说，先处理，

联立二式及余弦定理，

$$
a^2=b^2+c^2-bc\\
a^2=b^2+c^2-2bc\cos A
$$

得，

$$
\cos A={1\over2},\,A=60^\circ
$$

第一个式子，可以不带入 $A$，尝试通过三角函数的变换，

$$
\begin{aligned}
\sin A&=\sin(\pi-B-C)=\sin(B+C)\\
&=\sin B\cos C+\cos B\sin C
\end{aligned}
$$

联立下式及一式，

$$
\sin B\cos C+\cos B\sin C=2\sin B\cos C\\
\sin B\cos C=\cos B\sin C\\
\tan B=\tan C
$$

因为 $B,C\in(0,\pi)$，正切函数在此范围内唯一，则

$$
B=C=A=60^\circ
$$

即 $\triangle ABC$ 是正三角形。

### 例题十

在 $\triangle ABC$ 中，

$$
\cos(2B+C)+\cos C>0
$$

+ 判断三角形是锐角、直角、钝角三角形。

容易发现，$\cos$ 里面的角有很好的性质，考虑和差化积，

$$
\begin{aligned}
&\cos(2B+C)+\cos C\\
=\;&2\cos(B+C)\cos B\\
=\;&-2\cos A\cos B>0
\end{aligned}
$$

因此，

$$
\cos A\cos B<0
$$

即 $A,B$ 中有一个钝角，即 $\triangle ABC$ 为钝角三角形。

### 例题十一

在 $\triangle ABC$ 中，三边长分别为 $a,a+2,a+4$，最小角余弦值为 $13/14$。

+ 求该三角形的面积

因为大边对大角，因此最小角是 $a$ 对的，

$$
\cos A={(a+2)^2+(a+4)^2-a^2\over2(a+2)(a+4)}={13\over14}
$$

解得，$a=3$，于是用海伦公式，

$$
p={3+5+7\over2}={15\over2}
$$

$$
S=\sqrt{{15\over2}\cdot{9\over2}\cdot{5\over2}\cdot{1\over2}}={15\sqrt3\over4}
$$

### 例题十二

在 $\triangle ABC$ 中，$\angle A=120^\circ$，$BC=6$。

+ 求：其面积最大值。

考虑面积可以怎么表示。

Solution 1:

$$
S={1\over2}bc\sin A={\sqrt3\over4}bc
$$

根据余弦定理，

$$
36=a^2=b^2+c^2-2bc\cos A=b^2+c^2+bc\ge3bc
$$

即，

$$
bc\le12,\,S\le3\sqrt3
$$

Solution 2：

考虑到顶角不变，则可以固定底边，使顶点移动。

易知其轨迹为一个圆弧，则面积最大即底边高线最大。

高线最大即该三角形为等腰三角形，做出高线，

$$
S={1\over2}ah=3\sqrt3
$$

### 例题十三

在 $\triangle ABC$ 中，若

$$
a-b=c(\cos B-\cos A)
$$

+ 判断其形状。

考虑到余弦定理展开后是三次式，有点复杂，因此正弦定理。

$$
\sin A-\sin B=\sin C\cos B-\sin C\cos A
$$

考虑凑项，右边的两项很像正弦的和角公式，于是，

$$
\begin{aligned}
&\sin(B+C)-\sin(A+C)\\
=\;&\sin B\cos C+\sin C\cos B-\sin A\cos C-\sin C\cos A\\
=\;&\sin C\cos B-\sin C\cos A
\end{aligned}
$$

化简，

$$
(\sin B-\sin A)\cos C=0
$$

即 $\sin A=\sin B$ 或 $\cos C=0$，

即 $\triangle ABC$ 为等腰三角形或直角三角形。

### 例题十四

若 $\triangle ABC$ 中，$\angle C$ 为钝角，且其面积，

$$
S={\sqrt3\over4}(a^2+c^2-b^2)
$$

+ 求 $\angle B$。

考虑到 $a^2+c^2-b^2$ 是经典掉牙的形式，

$$
\cos B={a^2+c^2-b^2\over2ac}
$$

于是，

$$
S={\sqrt3\over4}\cdot2ac\cos B={\sqrt3\over2}ac\cos B
$$

考虑很经典的面积公式，

$$
S={1\over2}ac\sin B={\sqrt3\over2}ac\cos B\\
\sin B=\sqrt3\cos B\\
\tan B=\sqrt3,\,B=60^\circ
$$

### 例题十五

在 $\triangle ABC$ 中，

$$
\sin^2A-\sin^2B-\sin^2C=\sin B\sin C
$$

+ 求 $A$.
+ 若 $BC=3$，求其周长最大值。

因为是正弦的二次齐次式，考虑正弦定理，

$$
a^2=b^2+c^2+bc
$$

于是 $\angle A=120^\circ$。

考虑周长最大，即 $b+c$ 最大，

$$
a^2=9=b^2+c^2+bc\ge3bc\\
bc\le3
$$

考虑周长如何建立联系

$$
b+c=\sqrt{b^2+c^2+2bc}=\sqrt{9+bc}\le2\sqrt3
$$

即周长，

$$
a+b+c\le2\sqrt3+3
$$

### 例题十六

在 $\triangle ABC$ 中，

$$
\sin A+2\sin B\cos C=0\\
c=\sqrt3b
$$

+ 求 $\tan A$。

考虑到第二个很适合消元 $c$，于是第一个式子可以看成一次齐次，

$$
a+2b\cos C=0\\
\cos C=-{a\over2b}={a^2+b^2-c^2\over2bc}={a^2-2b^2\over2bc}
$$

因此，

$$
a^2=b^2\\
a=b
$$

因为 $c=\sqrt3b$，这是一个 $30^\circ,30^\circ,120^\circ$ 的等腰三角形，

$$
\tan A=\tan30^\circ={\sqrt3\over3}
$$

### 例题十七

在 $\triangle ABC$ 中，

$$
a^2+b^2=2022c^2
$$

求，

$$
{2\tan A\tan B\over\tan C(\tan A+\tan B)}
$$

考虑到没有什么好玩的结构，因此展开正切。

$$
\begin{aligned}
S&={2\tan A\tan B\over\tan C(\tan A+\tan B)}\\
&={2\sin A\sin B\over\sin C/\cos C\cdot(\sin A\cos B+\cos A+\sin B)}\\
&={2\sin A\sin B\cos C\over\sin^2C}
\end{aligned}
$$

考虑到上下正弦构成二次齐次，正弦定理，

$$
\begin{aligned}
S&={2\sin A\sin B\cos C\over\sin^2C}\\
&={2ab\cos C\over c^2}
\end{aligned}
$$

注意到 $2ab$ 和 $\cos C$ 的余弦定理的分母类似，

$$
\cos C={a^2+b^2-c^2\over2ab}
$$

$$
\begin{aligned}
S&={a^2+b^2-c^2\over c^2}={a^2+b^2\over c^2}-1\\
&=2022-1=2021
\end{aligned}
$$

### 例题十八

在锐角三角形 $ABC$ 中，$a^2-b^2=bc$。

求证：$A=2B$。

经典题，因为角不好表示，上式又是边的二次齐次式，考虑，

$$
\cos A={b^2+c^2-a^2\over2bc}={c^2-bc\over2bc}={c-b\over2b}\\
$$

$$
\begin{aligned}
\cos 2B&=2\cos^2B-1=2\left({a^2+c^2-b^2\over2ac}\right)^2-1\\
&=2\left({c+b\over2a}\right)^2-1={2c^2+2b^2+4bc-4a^2\over4a^2}\\
&={2c^2-2b^2\over4b^2+4bc}={2(c+b)(c-b)\over4b(b+c)}={c-b\over2b}
\end{aligned}
$$

于是，

$$
(\cos A=\cos2B)\Longrightarrow(A=2B)
$$

### 例题：CF995C

题目：[CF995C Leaving the Bar](https://www.luogu.com.cn/problem/CF995C)

题目简述：给定 $n$ 个向量，你将一些向量取反，试求出一种取反方法，使得这 $n$ 个向量之和的模小于 $1.5\times10^6$。

正解思路：考虑任意三个向量 $\vec v_1,\vec v_2,\vec v_3$ 及其取反的向量 $-\vec v_1,-\vec v_2,-\vec v_3$。此时一共有了 $6$ 个向量。根据抽屉原理，这六个向量一定存在两个向量，其夹角小于等于 $60^\circ$。根据余弦定理 $a^2=b^2+c^2-2bc\cos\theta$。当 $\theta\le60^\circ$，$2\cos\theta\ge1$，则 $2bc\cos\theta\ge bc$。记 $M=\max\{b,c\}$，有 $a^2\le b^2+c^2-ab\le 2M^2-M^2=M^2$。也就是这两个向量相加后得到的向量的模一定不超过这两个向量的模的较大值。于是我们考虑合并任意三个向量，最终得到两个长度不超过 $10^6$ 的向量，然后我们考虑这两个向量如何定向去合并，那么当这两个向量垂直的时候，他们合并的结果最大，且一定不超过 $\sqrt 2\times10^6<1.5\times10^6$。

然而作者不会这个思路。于是采取了一个随机化的方法。考虑随机重排这些向量。然后用（假的）贪心思路来合并，即对于每一个向量只考虑合并上它的当前的最优情况。那么这个思路可能（很容易）被 Hack。于是我们重复这个过程，知道找到一组解即可。代码如下：

```cpp
#include <bits/stdc++.h>

using namespace std;

#define range(x) x.begin(), x.end()

struct emm {
	int id, x, y;
};

mt19937 rd(time(0) * clock());

int n;
vector<emm> a;
vector<int> ans;

double dis(int x, int y) {
	return sqrt(1.0 * x * x + 1.0 * y * y);
}

double solev() {
	shuffle(range(a), rd);
	int x = 0, y = 0;
	for (auto &[id, i, j] : a) {
		ans[id] = dis(x + i, y + j) < dis(x - i, y - j) ? 1 : -1;
		x += i * ans[id], y += j * ans[id];
	} return dis(x, y);
}

void print() {
	for (int i : ans) cout << i << " ";
	cout << endl;
}

signed main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr), cout.tie(nullptr);
	cin >> n; a.resize(n), ans.resize(n);
	for (int i = 0; i < n; ++i) cin >> a[i].x >> a[i].y, a[i].id = i;
	while (1) if (solev() <= 1.5e6) print(), exit(0);
	return 0;
}

```
