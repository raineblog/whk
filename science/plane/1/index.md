# 平面向量 {#_1}

## 有向线段 {#_2}

带有方向的线段称为有向线段。有向线段的三要素为：起点、方向、长度。

根据初等几何，那么只要知道这三要素，这个有向线段就已经被确定了，也就是终点可知。

从另一个角度思考，也可以认为是知道起点、终点，就可以唯一的确定一个有向线段。

一个有向线段由其两个端点表示，记为 []{.arithmatex}$\overrightarrow{AB}$ 或 []{.arithmatex}$\bm{a}$，同时我们记其长度，称为**向量的模**。

### 向量 {#_3}

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

我们取这个向量在横、纵坐标上延伸的长度作为两个元素，将向量记为 []{.arithmatex}$(a,b)$。

那么我们就得出了向量的几何意义，即向量 []{.arithmatex}$(a,b)$ 表示向右走 []{.arithmatex}$a$、向上走 []{.arithmatex}$b$ 的位移。

已知两点 []{.arithmatex}$A(a,b),B(c,d)$，易证 []{.arithmatex}$\overrightarrow{AB}=(c-a,d-b)$。

### 向量的模 {#_4}

对于一个向量 []{.arithmatex}$\vec a$，有向线段 []{.arithmatex}$\vec a$ 的长度称为向量的模，即为这个向量的大小。

符号表示为 []{.arithmatex}$|\bm a|$ 或 []{.arithmatex}$|\overrightarrow{AB}|$ ，根据勾股定理，我们知道 []{.arithmatex}$|\vec a|=|(x,y)|=\sqrt{x^2+y^2}$。

### 特殊的向量 {#_5}

**零向量**：模为 []{.arithmatex}$0$ 的向量，零向量的方向任意（不过其实是无意义）。一般记为：[]{.arithmatex}$\vec 0$。

**单位向量**：模为 []{.arithmatex}$1$ 的向量称为单位向量。一般记为 []{.arithmatex}$\bm e$，最常见的单位向量就是基向量。

**基向量**：[]{.arithmatex}$\bm i=(1,0)$ 表示 []{.arithmatex}$x$ 方向的单位向量，[]{.arithmatex}$\bm j=(0,1)$ 表示 []{.arithmatex}$y$ 方向的单位向量。

**平行向量**：方向相同或相反的两个非零向量，规定零向量与任何向量平行。记作： []{.arithmatex}$\bm x\parallel\bm y$。

**共线向量**：任一组平行向量都可以平移到同一直线上，所以平行向量又叫共线向量。

**相等向量**：模相等且方向相同的向量。**相反向量**：模相等且方向相反的向量。

### 斜坐标系 {#_6}

我们称 []{.arithmatex}$x$ 轴与 []{.arithmatex}$y$ 轴的角度为 []{.arithmatex}$\theta(\theta\neq\pi/2)$ 的坐标系。

定义平面直角坐标系中的点 []{.arithmatex}$P(x,y)$，将 []{.arithmatex}$P$ 转移到斜坐标系中变成 []{.arithmatex}$P'(x',y')$ 满足：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} x\'=x+y\cos\theta\\ y\'=y\sin\theta \end{cases}
:::

$$\begin{cases}
x'=x+y\cos\theta\\
y'=y\sin\theta
\end{cases}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} x=x\'-\dfrac{y\'}{\tan\theta}\\ y=\dfrac{y\'}{\sin\theta} \end{cases}
:::

$$\begin{cases}
x=x'-\dfrac{y'}{\tan\theta}\\
y=\dfrac{y'}{\sin\theta}
\end{cases}$$
::::

于是我们可以把平面向量在平面直角坐标系中的一些运算迁移到斜坐标系中：

- 数量积：[]{.arithmatex}$(x_1',y_1')\cdot(x_2',y_2')=x_1x_2+y_1y_2+(x_1y_2+x_2y_1)\cos\theta$。

- 模长：[]{.arithmatex}$\overrightarrow{a}=(x',y'),|\overrightarrow{a}|=\sqrt{x^2+y^2+2xy\cos\theta}$。

- 夹角：[]{.arithmatex}$\displaystyle\overrightarrow{a}=(x_1',y_1'),\overrightarrow{b}=(x_2',y_2'),\cos\gamma=\frac{\overrightarrow{a}\cdot\overrightarrow{b}}{|\overrightarrow{a}||\overrightarrow{b}|}$。

## 向量的线性运算 {#_7}

### 向量数乘 {#_8}

我们规定实数 []{.arithmatex}$\lambda$ 与向量 []{.arithmatex}$\bm a$ 的积为一个向量，称为向量的数乘运算，记作 []{.arithmatex}$\lambda\vec a$。

我们定义 []{.arithmatex}$\lambda\bm a=\lambda(x,y)=(\lambda x,\lambda y)$。据此，我们可以得出以下向量数乘常用的结论：

- []{.arithmatex}$|\lambda\bm a|=|\lambda||\bm a|$；
- 当 []{.arithmatex}$\lambda >0$ 时，[]{.arithmatex}$\lambda\bm a$ 与 []{.arithmatex}$\bm a$ 同向；
- 当 []{.arithmatex}$\lambda =0$ 时，[]{.arithmatex}$\lambda \bm a=\vec 0$；
- 当 []{.arithmatex}$\lambda<0$ 时，[]{.arithmatex}$\lambda \bm a$ 与 []{.arithmatex}$\bm a$ 方向相反。

根据数乘的定义，可以得出向量的数乘满足交换律、结合律、分配律等，即，

:::: {.arithmatex}
::: {.MathJax_Preview}
\lambda(\mu\bm a)=(\lambda\mu)\bm a\\ \lambda(\bm a+\bm b)=\lambda\bm a+\lambda\bm b\\ (\lambda+\mu)\bm a=\lambda\bm a+\mu\bm a\\ (-\lambda)\bm a=-(\lambda\bm a)=\lambda(-\bm a)
:::

$$\lambda(\mu\bm a)=(\lambda\mu)\bm a\\
\lambda(\bm a+\bm b)=\lambda\bm a+\lambda\bm b\\
(\lambda+\mu)\bm a=\lambda\bm a+\mu\bm a\\
(-\lambda)\bm a=-(\lambda\bm a)=\lambda(-\bm a)$$
::::

### 向量加法 {#_9}

注意，向量的数乘本质上也属于向量的线性运算，不过我把他们分开，方便理解。

下面讨论向量的加法，类比的，向量的减法可以从公式入手理解。

类比物理中的位移，从 []{.arithmatex}$A$ 经 []{.arithmatex}$B$ 到 []{.arithmatex}$C$，那么经过的位移等价于直接从 []{.arithmatex}$A$ 到 []{.arithmatex}$C$。

符号表示即：[]{.arithmatex}$\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$，其实这个也就是三角形法则所表述的。

向量减法类似：[]{.arithmatex}$\overrightarrow{OA}-\overrightarrow{OB}=\overrightarrow{OA}+\overrightarrow{BO}=\overrightarrow{BA}$，后面用到了交换律。

同时，注意到力的合成法则（平行四边形法则），同样也可以看做向量的相加。

因此，我们得出向量相加的两个运算法则，即三角形法则、平行四边形法则：

- 三角形法则：首尾顺次相连，和为从第一个向量的起点指向最后一个向量的终点；

- 平行四边形法则：向量共起点，和为以这两个向量为邻边的平行四边形的对角线，

  起点为两个向量共有的起点，方向沿平行四边形对角线方向。

![alt text](../image-2.avif)

这样，向量的加法就具有了几何意义。并且向量的加法满足交换律与结合律。

然后从几何的角度可以推出一些公式，其中三角形法则的公式比较简单，如下：

:::: {.arithmatex}
::: {.MathJax_Preview}
(x_1,y_1)+(x_2,y_2)=(x_1+x_2,y_1+y_2)
:::

$$(x_1,y_1)+(x_2,y_2)=(x_1+x_2,y_1+y_2)$$
::::

向量加法满足结合律和交换律，画图理解即可。

向量加法可以导出三角形不等式，

:::: {.arithmatex}
::: {.MathJax_Preview}
\|\|\bm a\|-\|\bm b\|\|\le\|\bm a+\bm b\|\le\|\bm a\|+\|\bm b\|
:::

$$||\bm a|-|\bm b||\le|\bm a+\bm b|\le|\bm a|+|\bm b|$$
::::

当且仅当两向量方向相同（注意不是平行），取等。

### 线段中点 {#_10}

设 []{.arithmatex}$A(x_1,y_1)$、[]{.arithmatex}$B(x_2,y_2)$ 为一平面内两点。

设 []{.arithmatex}$C(x,y)$ 为线段 []{.arithmatex}$AB$ 中点，则 []{.arithmatex}$\overrightarrow{AC}=\overrightarrow{CB}$：

:::: {.arithmatex}
::: {.MathJax_Preview}
x-x_1=x_2-x\\ y-y_1=y_2-y
:::

$$x-x_1=x_2-x\\
y-y_1=y_2-y$$
::::

最终解得，

:::: {.arithmatex}
::: {.MathJax_Preview}
C\left({x_1+x_2\over2},{y_1+y_2\over2}\right)
:::

$$C\left({x_1+x_2\over2},{y_1+y_2\over2}\right)$$
::::

即中点坐标。

### 线段长度 {#_11}

设 []{.arithmatex}$A(x_1,y_1)$、[]{.arithmatex}$B(x_2,y_2)$ 为一平面内两点，则，

:::: {.arithmatex}
::: {.MathJax_Preview}
\|\overrightarrow{AB}\|=\sqrt{\overrightarrow{AB}\cdot\overrightarrow{AB}}=\sqrt{(x_1-x_2)\^2+(y_1-y_2)\^2}
:::

$$|\overrightarrow{AB}|=\sqrt{\overrightarrow{AB}\cdot\overrightarrow{AB}}=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$$
::::

则线段 []{.arithmatex}$AB$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\|AB\|=\|\overrightarrow{AB}\|=\sqrt{(x_1-x_2)\^2+(y_1-y_2)\^2}
:::

$$|AB|=|\overrightarrow{AB}|=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$$
::::

即线段长度。

## 向量的点积 {#_12}

### 点积的声明 {#_13}

对于向量的乘法：

|  物理  |  数学  | 直译 | 俗称 |
|:------:|:------:|:----:|:----:|
| 标量积 | 数量积 | 内积 | 点积 |
| 矢量积 | 向量积 | 外积 | 叉积 |

物理和数学上的用语采用了意译的方法，分别表示运算的结果为标量和矢量。

在数学学科，通常也可以翻译成「内积」和「外积」，是两个名词的直译。

而「点积」和「叉积」是根据运算符号得来的俗称，这种俗称也很常见。

### 点积的定义 {#_14}

提示：点积的概念对于任意维数的向量都适用。

已知两个向量 []{.arithmatex}$\bm a,\bm b$ ，它们的夹角为 []{.arithmatex}$\theta$，那么这两个向量的点积为：

:::: {.arithmatex}
::: {.MathJax_Preview}
\bm a \cdot \bm b=\|\bm a\|\|\bm b\|\cos \theta
:::

$$\bm a \cdot \bm b=|\bm a||\bm b|\cos \theta$$
::::

- 其中，我们称 []{.arithmatex}$|\bm a|\cos \theta$ 为 []{.arithmatex}$\bm a$ 在 []{.arithmatex}$\bm b$ 方向上的投影。

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  \|\bm a\|\cos\theta=\dfrac{\bm a\cdot\bm b}{\|\bm b\|}
  :::

  $$|\bm a|\cos\theta=\dfrac{\bm a\cdot\bm b}{|\bm b|}$$
  ::::

  而投影向量需要再乘上 []{.arithmatex}$\bm b$ 方向的单位向量：

  :::: {.arithmatex}
  ::: {.MathJax_Preview}
  \dfrac{\bm a\cdot\bm b}{\|\bm b\|\^2}\bm b
  :::

  $$\dfrac{\bm a\cdot\bm b}{|\bm b|^2}\bm b$$
  ::::

- 其中，[]{.arithmatex}$\theta\in[0,\pi]$，但是直线的夹角 []{.arithmatex}$\theta\in[0,\pi)$，因为相反向量是完全不同的。

点积的几何意义即为：点积 []{.arithmatex}$\bm a \cdot \bm b$ 等于 []{.arithmatex}$\bm a$ 的模与 []{.arithmatex}$\bm b$ 在 []{.arithmatex}$\bm a$ 方向上的投影的乘积。

另外，我们定义向量点积数值上表示为（简记为先相乘再相加）：

:::: {.arithmatex}
::: {.MathJax_Preview}
(x_1,y_1)\cdot(x_2,y_2)=x_1x_2+y_1y_2
:::

$$(x_1,y_1)\cdot(x_2,y_2)=x_1x_2+y_1y_2$$
::::

可以发现，这种运算得到的结果是一个标量，并不属于向量的线性运算。

向量与零向量点积，结果为 []{.arithmatex}$\vec0$。在不引起混淆的情况下，点积的点号可以省略不写。

### 点积的性质 {#_15}

向量点乘满足交换律：

:::: {.arithmatex}
::: {.MathJax_Preview}
\bm a\cdot\bm b=\bm b\cdot\bm a=\|\bm a\|\cdot\|\bm b\|\cdot\cos\theta
:::

$$\bm a\cdot\bm b=\bm b\cdot\bm a=|\bm a|\cdot|\bm b|\cdot\cos\theta$$
::::

向量点乘对数乘有结合律：

:::: {.arithmatex}
::: {.MathJax_Preview}
(\lambda\bm a)\cdot\bm b=\lambda(\bm a\cdot\bm b)=\bm a\cdot(\lambda\bm b)
:::

$$(\lambda\bm a)\cdot\bm b=\lambda(\bm a\cdot\bm b)=\bm a\cdot(\lambda\bm b)$$
::::

向量点乘对向量加法有分配率：

:::: {.arithmatex}
::: {.MathJax_Preview}
(\bm a+\bm b)\cdot\bm c=\bm a\cdot\bm c+\bm b\cdot\bm c
:::

$$(\bm a+\bm b)\cdot\bm c=\bm a\cdot\bm c+\bm b\cdot\bm c$$
::::

但是向量点乘不满足结合律，

:::: {.arithmatex}
::: {.MathJax_Preview}
(\bm a\cdot\bm b)\cdot\bm c\neq\bm a\cdot(\bm b\cdot\bm c)
:::

$$(\bm a\cdot\bm b)\cdot\bm c\neq\bm a\cdot(\bm b\cdot\bm c)$$
::::

注意到向量运算具有大部分的数字运算的性质（除了除法），因此可以当做字母计算。

可以得到，若 []{.arithmatex}$\bm b\neq\bm c$，[]{.arithmatex}$\bm a\cdot\bm b=\bm a\cdot\bm c$ 的充要条件是 []{.arithmatex}$\bm a\perp(\bm b-\bm c)$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\bm a\cdot\bm b=\bm a\cdot\bm c\\ \bm a\cdot(\bm b-\bm c)=\vec0
:::

$$\bm a\cdot\bm b=\bm a\cdot\bm c\\
\bm a\cdot(\bm b-\bm c)=\vec0$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
\bm a\perp(\bm b-\bm c)
:::

$$\bm a\perp(\bm b-\bm c)$$
::::

我们可以发现，

:::: {.arithmatex}
::: {.MathJax_Preview}
\|\bm a+\bm b\|\^2-\|\bm a-\bm b\|\^2=4\bm a\cdot\bm b\\ \bm a\cdot\bm b={1\over4}\left(\|\bm a+\bm b\|\^2-\|\bm a-\bm b\|\^2\right)
:::

$$|\bm a+\bm b|^2-|\bm a-\bm b|^2=4\bm a\cdot\bm b\\
\bm a\cdot\bm b={1\over4}\left(|\bm a+\bm b|^2-|\bm a-\bm b|^2\right)$$
::::

即极化恒等式，我们可以不通过求夹角的方式得出两向量点积。

同时，常用的，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \|\bm a+\bm b\|&=\lambda\\ (\bm a+\bm b)\cdot(\bm a+\bm b)&=\lambda\^2\\ \|\bm a\|\^2+2\bm a\cdot\bm b+\|\bm b\|\^2&=\lambda\^2 \end{aligned}
:::

$$\begin{aligned}
|\bm a+\bm b|&=\lambda\\
(\bm a+\bm b)\cdot(\bm a+\bm b)&=\lambda^2\\
|\bm a|^2+2\bm a\cdot\bm b+|\bm b|^2&=\lambda^2
\end{aligned}$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
\|\bm a\|\^2+2\bm a\cdot\bm b+\|\bm b\|\^2=\|\bm a+\bm b\|\^2\\ \bm a\cdot\bm b={1\over2}\left(\|\bm a+\bm b\|\^2-\|\bm a\|\^2-\|\bm b\|\^2\right)\\
:::

$$|\bm a|^2+2\bm a\cdot\bm b+|\bm b|^2=|\bm a+\bm b|^2\\
\bm a\cdot\bm b={1\over2}\left(|\bm a+\bm b|^2-|\bm a|^2-|\bm b|^2\right)\\$$
::::

总结一下，上面两个式子，

:::: {.arithmatex}
::: {.MathJax_Preview}
\bm a\cdot\bm b={1\over4}\left(\|\bm a+\bm b\|\^2-\|\bm a-\bm b\|\^2\right)\\ \bm a\cdot\bm b={1\over2}\left(\|\bm a+\bm b\|\^2-\|\bm a\|\^2-\|\bm b\|\^2\right)\\
:::

$$\bm a\cdot\bm b={1\over4}\left(|\bm a+\bm b|^2-|\bm a-\bm b|^2\right)\\
\bm a\cdot\bm b={1\over2}\left(|\bm a+\bm b|^2-|\bm a|^2-|\bm b|^2\right)\\$$
::::

再结合点乘的定义，

:::: {.arithmatex}
::: {.MathJax_Preview}
\bm a\cdot\bm b=\|\bm a\|\cdot\|\bm b\|\cdot\cos\theta\\ \cos\theta={\bm a\cdot\bm b\over\|\bm a\|\cdot\|\bm b\|}
:::

$$\bm a\cdot\bm b=|\bm a|\cdot|\bm b|\cdot\cos\theta\\
\cos\theta={\bm a\cdot\bm b\over|\bm a|\cdot|\bm b|}$$
::::

就可以求出向量夹角。

特殊的，

:::: {.arithmatex}
::: {.MathJax_Preview}
\theta=0\\(\cos\theta=1),\\\bm a\cdot\bm b=\|\bm a\|\cdot\|\bm b\|\\ \theta=\pi\\(\cos\theta=-1),\\\bm a\cdot\bm b=-\|\bm a\|\cdot\|\bm b\|\\ \theta=\pi/2\\(\cos\theta=0),\\\bm a\cdot\bm b=0\\ \bm a\cdot\bm a=\|\bm a\|\^2,\\\|\bm a\|=\sqrt{\bm a\cdot\bm a}\\
:::

$$\theta=0\,(\cos\theta=1),\,\bm a\cdot\bm b=|\bm a|\cdot|\bm b|\\
\theta=\pi\,(\cos\theta=-1),\,\bm a\cdot\bm b=-|\bm a|\cdot|\bm b|\\
\theta=\pi/2\,(\cos\theta=0),\,\bm a\cdot\bm b=0\\
\bm a\cdot\bm a=|\bm a|^2,\,|\bm a|=\sqrt{\bm a\cdot\bm a}\\$$
::::

经典的套路是，见模长便平方。

其中，第三条即，垂直向量向量点积等于零。

根据 []{.arithmatex}$\cos 90^\circ=0$，[]{.arithmatex}$\bm a \perp \bm b \iff \bm a\cdot \bm b=0$。

### 柯西不等式 {#_16}

:::: {.arithmatex}
::: {.MathJax_Preview}
\|\bm a\cdot\bm b\|\le\|\bm a\|\cdot\|\bm b\|
:::

$$|\bm a\cdot\bm b|\le|\bm a|\cdot|\bm b|$$
::::

当且仅当两向量共线，取等。

据此，可以判断两向量共线：

两个非零向量 []{.arithmatex}$\bm a$ 与 []{.arithmatex}$\bm b$ 共线，等价于，有唯一实数 []{.arithmatex}$\lambda$，使得 []{.arithmatex}$\bm b=\lambda \bm a$。

由数乘的定义知，对于非零向量 []{.arithmatex}$\bm a$，如果存在实数 []{.arithmatex}$\lambda$，使得 []{.arithmatex}$\bm b=\lambda \bm a$，那么 []{.arithmatex}$\bm a \parallel \bm b$。

数值上，有判别式 []{.arithmatex}$\bm a = \lambda \bm b \iff |\bm a\cdot \bm b|=|\bm a||\bm b|$。

### 极化恒等式 {#_17}

对于任意平面向量 []{.arithmatex}$\vec a,\vec b$ 有：

:::: {.arithmatex}
::: {.MathJax_Preview}
4\vec a\cdot\vec b=(\vec a+\vec b)\^2-(\vec a-\vec b)\^2
:::

$$4\vec a\cdot\vec b=(\vec a+\vec b)^2-(\vec a-\vec b)^2$$
::::

常见形式为：

:::: {.arithmatex}
::: {.MathJax_Preview}
\vecc{PA}\cdot\vecc{PB}=\|PM\|\^2-\dfrac{1}{4}\|AB\|\^2
:::

$$\vecc{PA}\cdot\vecc{PB}=|PM|^2-\dfrac{1}{4}|AB|^2$$
::::

其中 []{.arithmatex}$M$ 为 []{.arithmatex}$AB$ 中点。

## 基底分解 {#_18}

### 平面向量基本定理 {#_19}

若基底 []{.arithmatex}$\bm e_1,\bm e_2$ 不共线，则对于平面内任一向量 []{.arithmatex}$\bm a$，存在唯一实数 []{.arithmatex}$x,y$ 使得 []{.arithmatex}$\bm a=x\bm e_1+y\bm e_2$。

形式化的，平面内的任一向量都可以唯一的表示为两个不共线向量的线性组合。

存在性的证明：感性理解（雾

唯一性的证明，反证：假设存在两组实数 []{.arithmatex}$\langle x_1,y_1\rangle$、[]{.arithmatex}$\langle x_2,y_2\rangle$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\bm a=x_1\bm e_1+y_1\bm e_2=x_2\bm e_1+y_2\bm e_2\\ \bm e_1(x_1-x_2)=\bm e_2(y_2-y_1)
:::

$$\bm a=x_1\bm e_1+y_1\bm e_2=x_2\bm e_1+y_2\bm e_2\\
\bm e_1(x_1-x_2)=\bm e_2(y_2-y_1)$$
::::

因为 []{.arithmatex}$x_1\neq x_2,y_1\neq y_2$，则 []{.arithmatex}$\bm e_1,\bm e_2$ 共线，与条件不符，因此存在唯一性。

考虑构造性的证明，

若，

:::: {.arithmatex}
::: {.MathJax_Preview}
\bm a\cdot\bm e_1=a_1,\\\bm a\cdot\bm e_2=a_2\\ \langle\bm e_1,\bm e_2\rangle=\theta
:::

$$\bm a\cdot\bm e_1=a_1,\,\bm a\cdot\bm e_2=a_2\\
\langle\bm e_1,\bm e_2\rangle=\theta$$
::::

设，[]{.arithmatex}$\bm a=x\bm e_1+y\bm e_2$，用 []{.arithmatex}$a_1,a_2,\theta$ 表示 []{.arithmatex}$\bm a$。

考虑，

:::: {.arithmatex}
::: {.MathJax_Preview}
\bm e_1\bm e_2=\cos\theta\\ \bm a\cdot\bm e_1=x+y\bm e_1\bm e_2=a_1\\ \bm a\cdot\bm e_2=y+x\bm e_1\bm e_2=a_2
:::

$$\bm e_1\bm e_2=\cos\theta\\
\bm a\cdot\bm e_1=x+y\bm e_1\bm e_2=a_1\\
\bm a\cdot\bm e_2=y+x\bm e_1\bm e_2=a_2$$
::::

列出方程组，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} x+y\cos\theta=a_1\\ y+x\cos\theta=a_2 \end{cases}
:::

$$\begin{cases}
x+y\cos\theta=a_1\\
y+x\cos\theta=a_2
\end{cases}$$
::::

解得，

:::: {.arithmatex}
::: {.MathJax_Preview}
\left\\\begin{aligned} x={a_1-a_2\cos\theta\over\sin\^2\theta}\\ y={a_2-a_1\cos\theta\over\sin\^2\theta} \end{aligned}\right.
:::

$$\left\{\begin{aligned}
x={a_1-a_2\cos\theta\over\sin^2\theta}\\
y={a_2-a_1\cos\theta\over\sin^2\theta}
\end{aligned}\right.$$
::::

这个思想很重要，常用一个很奇怪的式子，去点乘两个不共线向量。

### 共线向量基本定理 {#_20}

对于线段 []{.arithmatex}$AB$ 及一点 []{.arithmatex}$Q$，若存在一点 []{.arithmatex}$O$ 满足，

:::: {.arithmatex}
::: {.MathJax_Preview}
\overrightarrow{OQ}=\lambda\overrightarrow{OA}+(1-\lambda)\overrightarrow{OB}
:::

$$\overrightarrow{OQ}=\lambda\overrightarrow{OA}+(1-\lambda)\overrightarrow{OB}$$
::::

则 []{.arithmatex}$Q$ 在直线 []{.arithmatex}$AB$ 上，即 []{.arithmatex}$A,B,Q$ 三点共线。

证明如下：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \vecc{AQ}&=\lambda\vecc{AB}\\ \vecc{OQ}-\vecc{OA}&=\lambda(\vecc{OB}-\vecc{OA}) \end{aligned}
:::

$$\begin{aligned}
\vecc{AQ}&=\lambda\vecc{AB}\\
\vecc{OQ}-\vecc{OA}&=\lambda(\vecc{OB}-\vecc{OA})
\end{aligned}$$
::::

类似的，若 []{.arithmatex}$C$ 是线段 []{.arithmatex}$AB$ 中点，则对于任意一点 []{.arithmatex}$O$，有，

:::: {.arithmatex}
::: {.MathJax_Preview}
\overrightarrow{OC}={1\over2}\overrightarrow{OA}+{1\over2}\overrightarrow{OB}
:::

$$\overrightarrow{OC}={1\over2}\overrightarrow{OA}+{1\over2}\overrightarrow{OB}$$
::::

而坐标表示，[]{.arithmatex}$(a,b)$ 与 []{.arithmatex}$(c,d)$ 平行，等价于 []{.arithmatex}$ad=bc$。

### 等系数和线 {#_21}

![等系数和线](../%E7%AD%89%E7%B3%BB%E6%95%B0%E5%92%8C%E7%BA%BF.avif){width="100%"}

证明过程：

![等和线](../image-1.avif){width="100%"}
