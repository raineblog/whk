# 三角函数公式 {#_1}

## 任意角和角的计量 {#_2}

### 任意角的定义 {#_3}

平面内一条射线绕其端点从一个位置旋转到另一个位置形成的图形叫做角。

开始的位置称为始边，结束的位置称为终边。并规定：

- 按逆时针方向旋转形成的角叫做正角，其角度为正；
- 按顺时针方向旋转形成的角叫做负角，其角度为负；
- 终边相对于始边没有做任何旋转的角叫做零角，其角度为 [\$0\$]{.arithmatex}。

为什么逆时针是正角？考虑点 [\$(1,0)\$]{.arithmatex} 绕着 [\$(0,0)\$]{.arithmatex} 转一个锐角：

得到的点 [\$A(x,y)\$]{.arithmatex} 一定满足 [\$x,y\>0\$]{.arithmatex}，因此定义逆时针为正角。

这样就把角的概念推向了任意角。

### 弧度制的定义 {#_4}

弧度用符号 [\$\text{rad}\$]{.arithmatex} 表示，读作「弧度」。

定义正角的弧度为正、负角的弧度为负，零角的弧度为 [\$0\$]{.arithmatex}；

如果半径为 [\$r\$]{.arithmatex} 的圆的圆心角 [\$\alpha\$]{.arithmatex} 所对弧长为 [\$l\$]{.arithmatex} ，则：

::: {.arithmatex}
\$\$ \|\alpha\|=\dfrac{l}{r} \$\$
:::

与角 [\$\alpha\$]{.arithmatex} 终边位置相同的角的集合很容易得出，为：

::: {.arithmatex}
\$\$ \\\varphi \mid \varphi = \alpha - 2k\pi, k \in \mathbb{Z}\\ \$\$
:::

### 弧度与角度的转化 {#_5}

关键是，[\$180\^\circ=\pi\$]{.arithmatex}，具体的：

以度数表示的角，把数字乘以 [\$\dfrac{\pi}{180\^\circ}\$]{.arithmatex} 便转换成弧度；

以弧度表示的角，乘以 [\$\dfrac{180\^\circ}{\pi}\$]{.arithmatex} 便转换成度数。

## 三角函数的定义 {#_6}

### 用直角三角形定义 {#_7}

直角三角形只有锐角三角函数的定义。

指定锐角 [\$\theta\$]{.arithmatex}，可做出直角三角形，使一个内角为 [\$\theta\$]{.arithmatex}：

定义：正弦 [\$\sin\alpha\$]{.arithmatex} 表示 [\$\alpha\$]{.arithmatex} 的对边与斜边的比值。

定义：余弦 [\$\cos\alpha\$]{.arithmatex} 表示 [\$\alpha\$]{.arithmatex} 的邻边与斜边的比值。

定义：正切 [\$\tan\alpha\$]{.arithmatex} 表示 [\$\alpha\$]{.arithmatex} 的对边与邻边的比值。

### 用直角坐标系定义 {#_8}

设点 [\$P(x,y)\$]{.arithmatex} 是平面直角坐标系 [\$xOy\$]{.arithmatex} 中的一点。

我们记 [\$\theta\$]{.arithmatex} 是从 [\$x\$]{.arithmatex} 旋转到 [\$OP\$]{.arithmatex} 的角度，[\$r\$]{.arithmatex} 是 [\$OP\$]{.arithmatex} 长度。

则：

::: {.arithmatex}
\$\$ \begin{aligned} r=\sqrt{x\^2+y\^2}\\ \sin\theta=\frac{y}{r}\\ \cos\theta=\frac{x}{r}\\ \tan\theta=\frac{y}{x}\\ \end{aligned} \$\$
:::

这样可以定义任何角度的三角函数（除非当定义式无意义时）。

### 用单位圆定义 {#_9}

单位圆指半径为单位长度的圆。

通常是平面直角坐标系中以 [\$(0,0)\$]{.arithmatex} 为圆心、半径为 [\$1\$]{.arithmatex} 的圆。

单位圆上的点满足：[\$x\^2+y\^2=1\$]{.arithmatex}，即毕达哥拉斯定理。

指定一角 [\$\theta\$]{.arithmatex}，点 [\$(1,0)\$]{.arithmatex} 旋转 [\$\theta\$]{.arithmatex} 度得到的点 [\$A(x,y)\$]{.arithmatex}，那么：

::: {.arithmatex}
\$\$ \begin{aligned} x\^2+y\^2=1\\ \sin\theta=y\\ \cos\theta=x\\ \tan\theta=\frac{y}{x}\\ \end{aligned} \$\$
:::

### 常见的三角函数定义 {#_10}

::: {.arithmatex}
\$\$ \begin{aligned} \tan\alpha=\frac{\sin\alpha}{\cos\alpha}\\ \cot\alpha=\frac{1}{\tan\alpha}\\ \sec\alpha=\frac{1}{\cos\alpha}\\ \csc\alpha=\frac{1}{\sin\alpha} \end{aligned} \$\$
:::

### 常见角度的三角函数 {#_11}

| 角度 | 弧度 | 正弦（[\$\sin\$]{.arithmatex}） | 余弦（[\$\cos\$]{.arithmatex}） | 正切（[\$\tan\$]{.arithmatex}） |
|:--:|:--:|:--:|:--:|:--:|
| [\$0\^\circ\$]{.arithmatex} | [\$0\$]{.arithmatex} | [\$0\$]{.arithmatex} | [\$1\$]{.arithmatex} | [\$0\$]{.arithmatex} |
| [\$30\^\circ\$]{.arithmatex} | [\$\pi/6\$]{.arithmatex} | [\$1/2\$]{.arithmatex} | [\$\sqrt3/2\$]{.arithmatex} | [\$\sqrt3/3\$]{.arithmatex} |
| [\$45\^\circ\$]{.arithmatex} | [\$\pi/4\$]{.arithmatex} | [\$\sqrt2/2\$]{.arithmatex} | [\$\sqrt2/2\$]{.arithmatex} | [\$1\$]{.arithmatex} |
| [\$60\^\circ\$]{.arithmatex} | [\$\pi/3\$]{.arithmatex} | [\$\sqrt3/2\$]{.arithmatex} | [\$1/2\$]{.arithmatex} | [\$\sqrt3\$]{.arithmatex} |
| [\$90\^\circ\$]{.arithmatex} | [\$\pi/2\$]{.arithmatex} | [\$1\$]{.arithmatex} | [\$0\$]{.arithmatex} | 无意义 |
| [\$120\^\circ\$]{.arithmatex} | [\$2\pi/3\$]{.arithmatex} | [\$\sqrt3/2\$]{.arithmatex} | [\$-1/2\$]{.arithmatex} | [\$-\sqrt3\$]{.arithmatex} |
| [\$135\^\circ\$]{.arithmatex} | [\$3\pi/4\$]{.arithmatex} | [\$\sqrt2/2\$]{.arithmatex} | [\$-\sqrt2/2\$]{.arithmatex} | [\$-1\$]{.arithmatex} |
| [\$150\^\circ\$]{.arithmatex} | [\$5\pi/6\$]{.arithmatex} | [\$1/2\$]{.arithmatex} | [\$-\sqrt3/2\$]{.arithmatex} | [\$-\sqrt3/3\$]{.arithmatex} |
| [\$180\^\circ\$]{.arithmatex} | [\$\pi\$]{.arithmatex} | [\$0\$]{.arithmatex} | [\$-1\$]{.arithmatex} | [\$0\$]{.arithmatex} |
| [\$210\^\circ\$]{.arithmatex} | [\$7\pi/6\$]{.arithmatex} | [\$-1/2\$]{.arithmatex} | [\$-\sqrt3/2\$]{.arithmatex} | [\$\sqrt3/3\$]{.arithmatex} |
| [\$225\^\circ\$]{.arithmatex} | [\$5\pi/4\$]{.arithmatex} | [\$-\sqrt2/2\$]{.arithmatex} | [\$-\sqrt2/2\$]{.arithmatex} | [\$1\$]{.arithmatex} |
| [\$240\^\circ\$]{.arithmatex} | [\$4\pi/3\$]{.arithmatex} | [\$-\sqrt3/2\$]{.arithmatex} | [\$-1/2\$]{.arithmatex} | [\$\sqrt3\$]{.arithmatex} |
| [\$270\^\circ\$]{.arithmatex} | [\$3\pi/2\$]{.arithmatex} | [\$-1\$]{.arithmatex} | [\$0\$]{.arithmatex} | 无意义 |
| [\$300\^\circ\$]{.arithmatex} | [\$5\pi/3\$]{.arithmatex} | [\$-\sqrt3/2\$]{.arithmatex} | [\$1/2\$]{.arithmatex} | [\$-\sqrt3\$]{.arithmatex}​ |
| [\$315\^\circ\$]{.arithmatex} | [\$7/4\$]{.arithmatex} | [\$-\sqrt2/2\$]{.arithmatex} | [\$\sqrt2/2\$]{.arithmatex} | [\$-1\$]{.arithmatex} |
| [\$330\^\circ\$]{.arithmatex} | [\$11\pi/6\$]{.arithmatex} | [\$-1/2\$]{.arithmatex} | [\$\sqrt3/2\$]{.arithmatex} | [\$-\sqrt3/3\$]{.arithmatex} |
| [\$360\^\circ\$]{.arithmatex} | [\$2\pi\$]{.arithmatex} | [\$0\$]{.arithmatex} | [\$1\$]{.arithmatex} | [\$0\$]{.arithmatex} |

### 正切函数及其性质 {#_12}

定义域：[\$\\x\mid x\neq k\pi+\pi/2,k\in\mathbb Z\\\$]{.arithmatex}；

值域：[\$(-\infty,+\infty)\$]{.arithmatex}

周期性：[\$T=\pi\$]{.arithmatex}；

单调性：在 [\$(k\pi-\pi/2,k\pi+\pi/2)\$]{.arithmatex} 单调递增。

对称性：奇函数，关于 [\$(k\pi,0),k\in\mathbb Z\$]{.arithmatex} 对称。

### 尼云定理 {#_13}

尼云定理指出，在 [\$0\sim90\^\circ\$]{.arithmatex} 范围内，如果正弦函数 [\$\sin\$]{.arithmatex} 的自变量和因变量都要求是有理数，那么答案只有：

::: {.arithmatex}
\$\$ \begin{aligned} \sin0\^\circ&=0\\ \sin30\^\circ&=1/2\\ \sin90\^\circ&=1 \end{aligned} \$\$
:::

## 正弦、余弦函数及其性质 {#_14}

分析函数的套路：

- 定义域、值域、图像。

- 周期性、单调性。

- 对称轴、对称中心。

- 最大值、最小值、零点。

### 图像 {#_15}

![三角函数](../tri-sin-cos-tan.avif){width="100%"}

### 周期性 {#_16}

::: {.arithmatex}
\$\$ \begin{aligned} \sin\alpha=\sin(\alpha+2\pi)\\ \cos\alpha=\cos(\alpha+2\pi) \end{aligned} \$\$
:::

可知 [\$\sin\$]{.arithmatex}、[\$\cos\$]{.arithmatex} 是最小正周期为 [\$2\pi\$]{.arithmatex} 的周期函数。

### 奇偶性 {#_17}

正弦函数是奇函数，余弦函数是偶函数。

### 对称性 {#_18}

1.  正弦函数：

2.  中心对称：[\$(k\pi,0),k\in\mathbb Z\$]{.arithmatex}；

3.  轴对称：[\$x=k\pi-\pi/2,k\in\mathbb Z\$]{.arithmatex}；

4.  余弦函数：

5.  中心对称：[\$(k\pi-\pi/2),k\in\mathbb Z\$]{.arithmatex}；

6.  轴对称：[\$x=k\pi,k\in\mathbb Z\$]{.arithmatex}。

7.  对称中心：零点；对称轴：极值点。

### 单调性 {#_19}

1.  正弦函数：

2.  单调递增：[\$\[2k\pi-\pi/2,2k\pi+\pi/2\],k\in\mathbb Z\$]{.arithmatex}；

3.  单调递减：[\$\[2k\pi+\pi/2,2k\pi+3\pi/2\],k\in\mathbb Z\$]{.arithmatex}；

4.  余弦函数：

5.  单调递增：[\$\[2k\pi-\pi,2k\pi\],k\in\mathbb Z\$]{.arithmatex}；

6.  单调递减：[\$\[2k\pi,2k\pi+\pi\],k\in\mathbb Z\$]{.arithmatex}；

## 正弦曲线及其性质 {#_20}

定义：正弦曲线，形如 [\$y=A\sin(\omega x+\varphi)\$]{.arithmatex}。

注意到 [\$\sin\$]{.arithmatex}、[\$\cos\$]{.arithmatex} 其实都属于正弦曲线。

### 函数 [\$y=A\sin x\$]{.arithmatex} 的性质 {#yasin-x}

我们发现这个操作其实就是对 [\$y\$]{.arithmatex} 轴的伸缩：

若 [\$A\>1\$]{.arithmatex}，图像伸长；若 [\$A\<1\$]{.arithmatex}，图像压缩；伸缩倍率为 [\$A\$]{.arithmatex}。

也就是图像上任何一个点的纵坐标变成了原来的 [\$A\$]{.arithmatex} 倍。

其中 [\$A\$]{.arithmatex} 决定了函数上的点的纵坐标的变化幅度，我们称为振幅。

### 函数 [\$y=\sin(x+\varphi)\$]{.arithmatex} 的性质 {#ysinxvarphi}

我们发现这个操作其实就是对 [\$y=\sin x\$]{.arithmatex} 图像的平移：

若 [\$\varphi\>0\$]{.arithmatex}，图像向左平移；若 [\$\varphi\<0\$]{.arithmatex} 图像向右平移；平移单位为 [\$\|\varphi\|\$]{.arithmatex}。

也就是点 [\$P(x,\sin x)\$]{.arithmatex} 平移到了 [\$P\'(x-\varphi,\sin x)\$]{.arithmatex}。

其中 [\$\varphi\$]{.arithmatex} 决定了初始时刻的位置，我们称为初相。

### 函数 [\$y=\sin(\omega x)\$]{.arithmatex} 的性质 {#ysinomega-x}

我们发现这个操作其实就是对 [\$x\$]{.arithmatex} 轴的伸缩：

若 [\$\omega\>1\$]{.arithmatex}，图像压缩；若 [\$\omega\<1\$]{.arithmatex}，图像伸长；伸缩倍率为 [\$1/\omega\$]{.arithmatex}。

也就是点 [\$P(x,\sin x)\$]{.arithmatex} 平移到了 [\$P\'\left(\dfrac{x}{\omega},\sin x\right)\$]{.arithmatex}。

其中 [\$\omega\$]{.arithmatex} 决定了函数值的变化快慢，我们称为角速度。

由于 [\$\sin x\$]{.arithmatex} 的最小正周期为 [\$2\pi\$]{.arithmatex}，因此 [\$\sin(\omega x)\$]{.arithmatex} 的最小正周期为：

::: {.arithmatex}
\$\$ T=\frac{2\pi}{\omega} \$\$
:::

### 函数 [\$y=\sin(\omega x+\varphi)\$]{.arithmatex} 的性质 {#ysinomega-xvarphi}

一下为作者以前写的文字，简单来说思想有两个：

- 一切变换是对于 [\$x,y\$]{.arithmatex} 的且满足左加右减，上加下减。

- [\$\omega,\varphi\$]{.arithmatex} 可以统称为相位（初相和角速度）。

我们把上面两个操作合在一起，但是，顺序？我们来分析一下。

考虑 [\$y=\sin x\$]{.arithmatex} 平移 [\$\varphi\$]{.arithmatex} 和 [\$x\$]{.arithmatex} 轴伸缩 [\$\omega\$]{.arithmatex} 这两个操作以不同的顺序会得到什么：

- 先平移 [\$\varphi\$]{.arithmatex}，后 [\$x\$]{.arithmatex} 轴伸缩 [\$\omega\$]{.arithmatex}：
  1.  [\$y=\sin x\$]{.arithmatex}
  2.  [\$y=\sin(x+\varphi)\$]{.arithmatex}
  3.  [\$y=\sin(\omega x+\varphi)\$]{.arithmatex}
- 先 [\$x\$]{.arithmatex} 轴伸缩 [\$\omega\$]{.arithmatex}，后平移 [\$\varphi\$]{.arithmatex}：
  1.  [\$y=\sin x\$]{.arithmatex}
  2.  [\$y=\sin(\omega x)\$]{.arithmatex}
  3.  [\$y=\sin(\omega(x+\varphi))\$]{.arithmatex}
  4.  [\$y=\sin(\omega x+\omega\varphi)\$]{.arithmatex}
- 易错点：
  - 平移是对于 [\$x\$]{.arithmatex} 的，而伸缩（在 [\$x\$]{.arithmatex} 轴上）是对应整个函数的。
  - 把函数 [\$y=\sin(\omega x+\varphi)\$]{.arithmatex}（可以看为 [\$f(x)=\sin(\omega x+\varphi)\$]{.arithmatex}）：
  - 平移 [\$\varphi\'\$]{.arithmatex} 是 [\$y=\sin(\omega(x+\varphi\')+\varphi)\$]{.arithmatex}，而不是 [\$y=\sin(\omega x+\varphi\'+\varphi)\$]{.arithmatex}
  - 伸缩 [\$\omega\'\$]{.arithmatex} 是 [\$y=\sin(\omega\'\omega x+\varphi)\$]{.arithmatex}，而不是 [\$y=\sin(\omega\'(\omega x+\varphi))\$]{.arithmatex}
  - 即，平移是对于 [\$x\$]{.arithmatex} 的操作，伸缩是对于传入函数的值的操作。

注意到 [\$y=\sin(\omega x+\varphi)\$]{.arithmatex} 相当于 [\$y=\sin(\omega x)\$]{.arithmatex} 平移 [\$\dfrac{\varphi}{\omega}\$]{.arithmatex} 得到的，

这个函数过点 [\$P\left(-\dfrac{\varphi}{\omega},0\right)\$]{.arithmatex}，而不是 [\$y=\sin(\omega x+\omega\varphi)\$]{.arithmatex} 过 [\$P\'(-\varphi,0)\$]{.arithmatex}。

据此，我们得出，从 [\$y=\sin x\$]{.arithmatex} 变换到 [\$y=\sin(\omega x+\varphi)\$]{.arithmatex}，需要：

- 先平移 [\$\varphi\$]{.arithmatex}，再对 [\$x\$]{.arithmatex} 轴伸缩 [\$\omega\$]{.arithmatex}。

因此可以得出，[\$P(x,\sin x)\$]{.arithmatex} 平移到了 [\$P\'\left(\dfrac{x-\varphi}{\omega},\sin x\right)\$]{.arithmatex}。

### 正弦函数到 [\$y=A\sin(\omega x+\varphi)\$]{.arithmatex} 的变换 {#yasinomega-xvarphi}

其实就相当于对函数 [\$y=\sin(\omega x+\varphi)\$]{.arithmatex} 的 [\$y\$]{.arithmatex} 轴伸缩 [\$A\$]{.arithmatex} 倍。

注意到 [\$A\$]{.arithmatex} 只是对 [\$y\$]{.arithmatex} 轴的伸缩，因此可以在任意时间变换。

注意到 [\$\omega\$]{.arithmatex} 是对 [\$x\$]{.arithmatex} 轴的伸缩，因此需要在 [\$\varphi\$]{.arithmatex} 的变换之后（前文已述）。

当然上面说的是分别进行三个变换各一次的顺序，据此我们进行组合：

1.  平移 [\$\varphi\$]{.arithmatex}；
2.  [\$x\$]{.arithmatex} 轴伸缩 [\$\omega\$]{.arithmatex}；
3.  [\$y\$]{.arithmatex} 轴伸缩 [\$A\$]{.arithmatex}。

可以从 [\$y=\sin x\$]{.arithmatex} 得到 [\$y=A\sin(\omega x+\varphi)\$]{.arithmatex} 的组合有：

::: {.arithmatex}
\$\$ (1,2,3),(1,3,2),(3,1,2) \$\$
:::

三种方式。

注意倒推法的应用。

## 函数 [\$y=A\sin(\omega x+\varphi)\$]{.arithmatex} 的性质 {#yasinomega-xvarphi_1}

### 图像 {#_21}

自行百度。

### 基础性质 {#_22}

上文写的很详细了，再梳理一遍：

我们知道，正弦函数和余弦函数只差了一个平移，

因此下文只讨论了正弦函数对应的正弦曲线，余弦函数的自己脑补。

PS：（其实也包括上文）

首先我们整理一下各个字母的含义：

- [\$A\$]{.arithmatex} 表示振幅：
  - 若 [\$A\>1\$]{.arithmatex}，图像在 [\$y\$]{.arithmatex} 轴上伸长；
  - 若 [\$A\<1\$]{.arithmatex}，图像在 [\$y\$]{.arithmatex} 轴上压缩；
  - 伸缩倍率为 [\$A\$]{.arithmatex}。
- [\$\omega\$]{.arithmatex} 表示角速度：
  - 若 [\$\omega\>1\$]{.arithmatex}，图像在 [\$x\$]{.arithmatex} 轴上压缩；
  - 若 [\$\omega\<1\$]{.arithmatex}，图像在 [\$x\$]{.arithmatex} 轴上伸长；
  - 伸缩倍率为 [\$1/\omega\$]{.arithmatex}。
- [\$\varphi\$]{.arithmatex} 表示初相，但是并不单独决定函数的位置。

这个函数相当于函数 [\$y=\sin x\$]{.arithmatex} 进行一定的操作（下面再说）。

其中，点 [\$P(x,\sin x)\$]{.arithmatex} 平移到了 [\$P\left(\dfrac{x-\varphi}{\omega},A\sin x\right)\$]{.arithmatex}。

### 定义域和值域 {#_23}

我们在这里统一说明正弦曲线的定义域和值域：

定义域，[\$\mathbb R\$]{.arithmatex}；值域，[\$\[-A,A\]\$]{.arithmatex}。

因此，[\$\sin\$]{.arithmatex}、[\$\cos\$]{.arithmatex} 函数的值域就是 [\$\[-1,1\]\$]{.arithmatex}。

### 最小正周期 {#_24}

由于其进行的变换对最小正周期没有影响，因此：

::: {.arithmatex}
\$\$ T=\frac{2\pi}{\omega} \$\$
:::

### 绘制简图 {#_25}

五点作图法：正弦曲线在一个周期内，一定是上去下来上去（或是歪了的）。

因此我们可以对于周期内的五个点（分为四个区间）画图：

比如，最小正周期为 [\$\pi\$]{.arithmatex} 的，我们可以做出 [\$\[0,\pi/4,\pi/2,3\pi/4,\pi\]\$]{.arithmatex} 五个点的图像。

然后用光滑的曲线连接，再根据周期性画出其他部位的图像即可。

也可以先看出来在所求范围内，函数的极大、极小点在哪里。

也就是正弦函数的最值点，求出传入函数的值中 [\$x\$]{.arithmatex} 对应多少。

然后先把这些点画出来，再找三个或更多上述性质的点求解、画图。

### 单调区间 {#_26}

可以用下面的方式：

我们知道正弦函数的单增区间是 [\$\[2k\pi-\pi/2,2k\pi+\pi/2\]\$]{.arithmatex}。

意思是当传入正弦函数的值在这个区间内，函数值单增。

因此可以把传入函数的值当做一个整体，对于 [\$y=A\sin(\omega x+\varphi)\$]{.arithmatex}：

::: {.arithmatex}
\$\$ 2k\pi-\pi/2\le\omega x+\varphi\le2k\pi+\pi/2 \$\$
:::

就是单调区间，化简即可。

单减区间是 [\$\[2k\pi+\pi/2,2k\pi+\pi\]\$]{.arithmatex}，计算同理。

不过单减区间还有一个求法，就是单增区间的两个端点都加上 [\$T/2\$]{.arithmatex}。

原理就是单增区间往右到下一个单增区间是单减的且长度是半周期。

### 极大、极小值 {#_27}

对于整个图像的最值，就是函数的值域 [\$\[-A,A\]\$]{.arithmatex}。

对于一个区间的最值，可以有两个方法：

1.  画出函数简图，找到区间在图像上的位置，找到极大极小点求解。
2.  画出单位圆的示意图，在单位圆上找到函数的极大极小点，求解。

### 对称轴、对称中心 {#_28}

对称轴：最值点。

正弦函数的最值点都可以表示为 [\$k\pi+\pi/2,k\in\mathbb Z\$]{.arithmatex}，余弦函数不加 [\$\pi/2\$]{.arithmatex}。

对称中心：零点。

余弦函数的零点都可以表示为 [\$k\pi+\pi/2,k\in\mathbb Z\$]{.arithmatex}，正弦函数不加 [\$\pi/2\$]{.arithmatex}。

### 求正弦曲线解析式 {#_29}

也就是求三个值：[\$A\$]{.arithmatex}、[\$\omega\$]{.arithmatex}、[\$\varphi\$]{.arithmatex}。

其中 [\$A\$]{.arithmatex} 只与函数的最值有关，因此我们可以求出来它，则 [\$A\$]{.arithmatex} 就是函数的最值。

其次 [\$\omega\$]{.arithmatex} 表示的是角速度，根据公式 [\$T=2\pi/\omega\$]{.arithmatex} 可以写出 [\$\omega=2\pi/T\$]{.arithmatex}。

而 [\$T\$]{.arithmatex} 就是两个相邻极值点的距离的两倍、极值和零点的距离的四倍。

考虑 [\$\varphi\$]{.arithmatex}，易发现最好求的方法就是函数与 [\$y\$]{.arithmatex} 轴的交点 [\$y\|\_{x=0}\$]{.arithmatex}，那么就有

::: {.arithmatex}
\$\$ A\sin\varphi=y\|\_{x=0} \$\$
:::

求解即可。其次我们可以用函数的最值点、零点等，列：

::: {.arithmatex}
\$\$ A\sin(\omega x_0+\varphi)=y\|\_{x=x_0} \$\$
:::

解方程时要注意 [\$\varphi\$]{.arithmatex} 的取值一般是 [\$0\le\varphi\<T\$]{.arithmatex}，[\$A\$]{.arithmatex}、[\$\omega\$]{.arithmatex} 的取值一般是正数。

## 诱导公式 {#_30}

### 函数关于 2π 的周期性 {#2}

是 [\$\sin\$]{.arithmatex}、[\$\cos\$]{.arithmatex} 的周期。

::: {.arithmatex}
\$\$ \begin{aligned} \sin(\alpha+2\pi)&=\sin\alpha\\ \cos(\alpha+2\pi)&=\cos\alpha\\ \tan(\alpha+2\pi)&=\tan\alpha \end{aligned} \$\$
:::

### 函数关于 π 的周期性 {#_31}

是 [\$\tan\$]{.arithmatex}、[\$\cot\$]{.arithmatex} 的周期。

::: {.arithmatex}
\$\$ \begin{aligned} \sin(\alpha+\pi)&=-\sin\alpha\\ \cos(\alpha+\pi)&=-\cos\alpha\\ \tan(\alpha+\pi)&=\tan\alpha \end{aligned} \$\$
:::

### 函数的奇偶性 {#_32}

奇函数：[\$\sin\$]{.arithmatex}、[\$\tan\$]{.arithmatex}、[\$\cot\$]{.arithmatex}，偶函数：[\$\cos\$]{.arithmatex}。

::: {.arithmatex}
\$\$ \begin{aligned} \sin(-\alpha )&=-\sin \alpha\\ \cos(-\alpha )&=\cos \alpha\\ \tan(-\alpha )&=-\tan \alpha\\ \end{aligned} \$\$
:::

### 函数关于 y 轴的对称性 {#y}

用单位圆象限角理解。

::: {.arithmatex}
\$\$ \begin{aligned} \sin(\pi-\alpha)&=\sin\alpha\\ \cos(\pi-\alpha)&=-\cos\alpha\\ \tan(\pi-\alpha)&=-\tan\alpha \end{aligned} \$\$
:::

### 余函数恒等式 {#_33}

用单位圆象限角理解。

::: {.arithmatex}
\$\$ \begin{aligned} \sin(\pi/2-\alpha)&=\cos\alpha\\ \cos(\pi/2-\alpha)&=\sin\alpha\\ \tan(\pi/2-\alpha)&=\cot\alpha \end{aligned} \$\$
:::

### 在直角三角形中的转换 {#_34}

用单位圆象限角理解。

::: {.arithmatex}
\$\$ \begin{aligned} \sin \left(\pi/2+\alpha\right)&=\cos\alpha\\ \cos \left(\pi/2+\alpha\right)&=-\sin\alpha\\ \tan \left(\pi/2+\alpha\right)&=-\cot\alpha\\ \end{aligned} \$\$
:::

### 综合：单位圆象限角 {#_35}

上述所有式子有一个联系：

::: {.arithmatex}
\$\$ \begin{aligned} \sin(k\pi/2\pm\alpha)&,k\in\mathbb{Z}\\ \cos(k\pi/2\pm\alpha)&,k\in\mathbb{Z}\\ \tan(k\pi/2\pm\alpha)&,k\in\mathbb{Z} \end{aligned} \$\$
:::

转换法则：

- 当 [\$k\$]{.arithmatex} 为偶数时，三角函数则不变换。
- 当 [\$k\$]{.arithmatex} 为奇数时，[\$\sin\$]{.arithmatex} 变为 [\$\cos\$]{.arithmatex}，[\$\cos\$]{.arithmatex} 变为 [\$\sin\$]{.arithmatex}，[\$\tan\$]{.arithmatex} 变为 [\$\cot\$]{.arithmatex}，[\$\cot\$]{.arithmatex} 变为 [\$\tan\$]{.arithmatex}。
- 对于正负号，则要看最后角所在的象限进行判断。

可使用口诀：奇变偶不变，符号看象限（ASTC, All Students Take Calculus）记忆。

- 第一象限的 A 即是 All（全部皆正）。
- 第二象限的 S 即是 Sine（正弦以及余割为正）。
- 第三象限的 T 即是 Tangent（正切以及余切为正）。
- 第四象限的 C 即是 Cosine（余弦以及正割为正）。

常见化简方法：周期性（[\$\sin\$]{.arithmatex}、[\$\cos\$]{.arithmatex} 是 [\$2\pi\$]{.arithmatex}，[\$\tan\$]{.arithmatex}、[\$\cot\$]{.arithmatex} 是 [\$\pi\$]{.arithmatex}），奇偶性（[\$\sin\$]{.arithmatex}、[\$\tan\$]{.arithmatex}、[\$\cot\$]{.arithmatex} 是奇函数，[\$\cos\$]{.arithmatex} 是偶函数），出现 [\$\pi/2\$]{.arithmatex} 系列的要变符号，画出单位圆求解。

## 毕达哥拉斯三角恒等式 {#_36}

### 基础形式 {#_37}

::: {.arithmatex}
\$\$ \begin{aligned} \sin\^2\alpha+\cos\^2\alpha=1 \end{aligned} \$\$
:::

也称为三角函数的勾股定理。

### 正弦和余弦的转换 {#_38}

根据上面的，易得：

::: {.arithmatex}
\$\$ \begin{aligned} \sin\^2\alpha&=1-\cos\^2\alpha\\ \cos\^2\alpha&=1-\sin\^2\alpha \end{aligned} \$\$
:::

开方，得：

::: {.arithmatex}
\$\$ \begin{aligned} \sin\alpha&=\pm\sqrt{1-\cos\^2\alpha}\\ \cos\alpha&=\pm\sqrt{1-\sin\^2\alpha} \end{aligned} \$\$
:::

一定要注意正负号，正负号由该角所在象限决定。

## 和差恒等式及其推导 {#_39}

也称为「和差定理」、「和差公式」或「和角公式」。

### 和差恒等式 {#_40}

::: {.arithmatex}
\$\$ \begin{aligned} \sin(\alpha\pm\beta)&=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta\\ \cos(\alpha\pm\beta)&=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta\\ \tan(\alpha\pm\beta)&=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta} \end{aligned} \$\$
:::

注意正负号的对应。

::: {.grid markdown=""}
![](../sin_cos.svg){width="80%"}

![](../tan.svg){width="80%"}
:::

### 二倍角公式 {#_41}

::: {.arithmatex}
\$\$ \begin{aligned} \sin2\alpha&=2\sin\alpha\cos\alpha\\ \cos2\alpha&=\cos\^2\alpha-\sin\^2\alpha\\ &=1-2\sin\^2\alpha\\ &=2\cos\^2\alpha-1\\ \tan2\alpha&=\frac{2\tan\alpha}{1-\tan\^2\alpha} \end{aligned} \$\$
:::

可以根据里面的结论推出降次公式。

### 三倍角公式 {#_42}

::: {.arithmatex}
\$\$ \begin{aligned} \sin3\alpha&=3\sin\alpha-4\sin\^3\alpha&&=4\sin\left(\dfrac\pi3-\alpha\right)\sin\alpha\sin\left(\dfrac\pi3+\alpha\right)\\ \cos3\alpha&=4\cos\^3\alpha-3\cos\alpha&&=4\cos\left(\dfrac\pi3-\alpha\right)\cos\alpha\cos\left(\dfrac\pi3+\alpha\right)\\ \end{aligned} \$\$
:::

下面的式子即为：

::: {.arithmatex}
\$\$ \cos3\alpha=4\cos(\alpha-60\^\circ)\cos\alpha\cos(\alpha+60\^\circ) \$\$
:::

正切同理，也可以用这个式子进行三次降幂。

::: {.arithmatex}
\$\$ \cos 3\theta=\begin{vmatrix}\cos\theta & 1 & 0 \\ 1 & 2\cos\theta & 1 \\ 0 & 1 & 2\cos\theta\end{vmatrix} \$\$
:::

::: {.arithmatex}
\$\$ \sin 3\theta=\begin{vmatrix}\sin\theta & 0 & 0 \\ 0 & 2\sin\theta & 1 \\ 0 & 1 & 2\cos\theta\end{vmatrix} \$\$
:::

::: {.arithmatex}
\$\$ \cos n\theta=\begin{vmatrix} \cos\theta & 1 & 0 & \cdots & 0 & 0 \\ 1 & 2\cos\theta & 1 & \cdots & 0 & 0 \\ 0 & 1 & 2\cos\theta & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & 2\cos\theta & 1 \\ 0 & 0 & 0 & \cdots & 1 & 2\cos\theta \end{vmatrix} \$\$
:::

::: {.arithmatex}
\$\$ \sin n\theta=\begin{vmatrix} \sin\theta & 0 & 0 & \cdots & 0 & 0 \\ 0 & 2\cos\theta & 1 & \cdots & 0 & 0 \\ 0 & 1 & 2\cos\theta & \cdots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & 2\cos\theta & 1 \\ 0 & 0 & 0 & \cdots & 1 & 2\cos\theta \end{vmatrix} \$\$
:::

这就是高倍角公式的行列式表示。

### 正切半角公式 {#_43}

也称为万能公式。

::: {.arithmatex}
\$\$ \begin{aligned} \sin\alpha&={2\tan{\alpha\over2}\over1+\tan\^2{\alpha\over2}}\\ \cos\alpha&={1-\tan\^2{\alpha\over2}\over1+\tan\^2{\alpha\over2}}\\ \tan\alpha&={2\tan{\alpha\over2}\over1-\tan\^2{\alpha\over2}} \end{aligned} \$\$
:::

其中下面的一个也等价于正切函数的二倍角公式。

### 降幂公式 {#_44}

降幂公式：

::: {.arithmatex}
\$\$ \begin{aligned} \sin\^2\alpha&=\frac{1-\cos2\alpha}{2}\\ \cos\^2\alpha&=\frac{1+\cos2\alpha}{2}\\ \tan\^2\alpha&=\frac{1-\cos2\alpha}{1+\cos2\alpha} \end{aligned} \$\$
:::

补充一个属于幂简约公式的：

::: {.arithmatex}
\$\$ \sin\^2\alpha\cos\^2\alpha={1-\cos4\alpha\over8} \$\$
:::

可以根据里面的结论推出半角公式。

### 半角公式 {#_45}

::: {.arithmatex}
\$\$ \begin{aligned} \sin\frac{\alpha}{2}&=\pm\sqrt{\frac{1-\cos\alpha}{2}}\\ \cos\frac{\alpha}{2}&=\pm\sqrt{\frac{1+\cos\alpha}{2}}\\ \tan{\frac{\alpha}{2}}&=\pm{\sqrt{1-\cos\theta\over1+\cos\theta}}\\ &=\frac{\sin\alpha}{1+\cos\alpha}=\frac{1-\cos\alpha}{\sin\alpha} \end{aligned} \$\$
:::

正负号由半角所在象限决定。

### 第一类切比雪夫多项式 {#_46}

第一类 Chebyshev（切比雪夫）多项式由以下递推关系确定：

::: {.arithmatex}
\$\$ \begin{aligned} T_0(x)&=1\\ T_1(x)&=x\\ T\_{n+1}(x)&=2xT_n(x)-T\_{n-1}(x) \end{aligned} \$\$
:::

有三角恒等式：

::: {.arithmatex}
\$\$ cos(n\theta)=T_n(\cos\theta) \$\$
:::

其中：

::: {.arithmatex}
\$\$ \begin{aligned} T\_{0}(x) & = 1\\ T\_{1}(x) & = x\\ T\_{2}(x) & = 2x\^{2}-1\\ T\_{3}(x) & = 4x\^{3}-3x\\ T\_{4}(x) & = 8x\^{4}-8x\^{2}+1\\ T\_{5}(x) & = 16x\^{5}-20x\^{3}+5x\\ T\_{6}(x) & = 32x\^{6}-48x\^{4}+18x\^{2}-1\\ T\_{7}(x) & = 64x\^{7}-112x\^{5}+56x\^{3}-7x\\ T\_{8}(x) & = 128x\^{8}-256x\^{6}+160x\^{4}-32x\^{2}+1\\ T\_{9}(x) & = 256x\^{9}-576x\^{7}+432x\^{5}-120x\^{3}+9x \end{aligned} \$\$
:::

## 和差化积与积化和差 {#_47}

### 和差化积恒等式 {#_48}

::: {.arithmatex}
\$\$ \begin{aligned} \sin\alpha+\sin\beta&=2\sin{\alpha+\beta\over2}\cos{\alpha-\beta\over2}\\ \sin\alpha-\sin\beta&=2\cos{\alpha+\beta\over2}\sin {\alpha-\beta\over2}\\ \cos\alpha+\cos\beta&=2\cos{\alpha+\beta\over2}\cos {\alpha-\beta\over2}\\ \cos\alpha-\cos\beta&=-2\sin{\alpha+\beta\over2}\sin {\alpha-\beta\over2} \end{aligned} \$\$
:::

### 积化和差恒等式 {#_49}

::: {.arithmatex}
\$\$ \begin{aligned} \sin\alpha\cos\beta&={\sin(\alpha+\beta)+\sin(\alpha-\beta)\over2}\\ \cos\alpha\sin\beta&={\sin(\alpha+\beta)-\sin(\alpha-\beta)\over2}\\ \cos\alpha\cos\beta&={\cos(\alpha+\beta)+\cos(\alpha-\beta)\over2}\\ \sin\alpha\sin\beta&=-{\cos(\alpha+\beta)-\cos(\alpha-\beta)\over2} \end{aligned} \$\$
:::

### 记忆方法 {#_50}

轮换 [\$\alpha,\beta\$]{.arithmatex}，令其为相反数，根据 [\$\sin,\cos\$]{.arithmatex} 奇偶性判断。

## 公式变形和推导 {#_51}

### 平方差公式 {#_52}

::: {.arithmatex}
\$\$ \begin{aligned} \sin(x+y)\sin(x-y)&&&=\sin\^2x-\sin\^2y&&=\cos\^2y-\cos\^2x\\ \cos(x+y)\cos(x-y)&&&=\cos\^2x-\sin\^2y&&=\cos\^2y-\sin\^2x \end{aligned} \$\$
:::

注意到右边的式子还可以用平方差公式展开。

### 辅助角公式 {#_53}

对于式子：

::: {.arithmatex}
\$\$ a\sin x+b\cos x \$\$
:::

如果 [\$a=r\cos\varphi\$]{.arithmatex}，[\$b=r\sin\varphi\$]{.arithmatex}，

可知

::: {.arithmatex}
\$\$ a\^2+b\^2=r\^2(\sin\^2\varphi+\cos\^2\varphi)=r\^2 \$\$
:::

即 [\$r=\sqrt{a\^2+b\^2}\$]{.arithmatex}，则有 [\$\cos\varphi=a/r\$]{.arithmatex}，[\$\sin\varphi=b/r\$]{.arithmatex}。

化简式子：

::: {.arithmatex}
\$\$ \begin{aligned} a\sin x+b\cos x&=r\cos\varphi\sin x+r\sin\varphi\cos x\\ &=r\sin(x+\varphi)=\sqrt{a\^2+b\^2}\sin(x+\varphi) \end{aligned} \$\$
:::

其中，[\$\varphi\$]{.arithmatex} 满足：

::: {.arithmatex}
\$\$ \begin{cases} \cos\varphi&=a/r\\ \sin\varphi&=b/r \end{cases} \$\$
:::

若 [\$a\>0\$]{.arithmatex}，可以写成 [\$\varphi=\arctan b/a\$]{.arithmatex} 的形式。

也就是 [\$a\sin x+b\cos x=\sqrt{a\^2+b\^2}\sin(x+\arctan b/a)\$]{.arithmatex}。

### 其他公式 {#_54}

::: {.arithmatex}
\$\$ (\sin\alpha\pm\cos\alpha)\^2=1\pm\sin2\alpha \$\$
:::

::: {.arithmatex}
\$\$ \dfrac{1+\tan\alpha}{1-\tan\alpha}=\dfrac{\tan\pi/4+\tan\alpha}{1-\tan\pi/4\tan\alpha}=tan\left(\alpha+\dfrac{\pi}{4}\right) \$\$
:::

::: {.arithmatex}
\$\$ \tan\alpha-\dfrac{1}{\tan\alpha}=\dfrac{\sin\^2\alpha-\cos\^2\alpha}{\sin\alpha\cos\alpha}=-2\dfrac{1}{\tan2\alpha} \$\$
:::
