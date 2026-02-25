# 空间几何体 \{#\_1}

## 基础知识 \{#\_2}

### 分类 \{#\_3}

<figure>

<figcaption><p>多面体和旋转体</p></figcaption>
</figure>

多面体是指三维空间中由平面多边形、直边和顶点组成的几何形状。多面体表面积通用公式就是将每一个平面多边形的面积相加求和。

旋转体是指平面曲线以同一平面内的一条直线作为旋转轴进行旋转所形成的立体几何图形。

### 斜二测画法 \{#\_4}

将平面 $x$ 轴不变，$y$ 轴向右倾斜 $45^\circ$ 并长度缩短到原来的 $1/2$，称为斜二测画法，画出来的图称为直观图。

容易知道，直观图的面积是原图形的 $\dfrac\{\sqrt2}4$，原图形的面积是直观图的 $2\sqrt2$ 倍。

竖直的 $z$ 轴也不变，称所画出的图形称为直观图。

### 祖暅原理 \{#\_5}

祖暅（gèng）之《缀术》有云：「缘幂势既同，则积不容异」。

$$
V=\int\_\{0}^HS(h)\mathrm\{d}h
$$

祖暅原理（也称等幂等积定理）指出：所有等高处横截面积相等的两个等高的立体，其体积也必然相等。经典推论是，两个等高的立体，如果其所有等高处横截面积相等，则其体积必然相等。

### 辛普森法则 \{#\_6}

设拟柱体的高为 $H$，如果用平行于底面的平面去截该图形，所得到的截面面积是与到底面之间距离 $h$ 的不超过 $3$ 次的函数，那么该拟柱体的体积 $V$ 为：

$$
V=\dfrac\{h(a+4b+c)}6
$$

其描述的是辛普森积分法（一种数值积分方法）：

$$
\int\_\{a}^\{b}f(x)\mathrm dx\approx \{\dfrac \{b-a}\{6}}\left\[f(a)+4f\left(\{\dfrac \{a+b}\{2}}\right)+f(b)\right]
$$

### 欧拉公式 \{#\_7}

欧拉公式表述为：$V-E+F=2$，即顶点数 Vertex $-$ 棱数 Edge $+$ 面数 Face $=2$。

|       |  面数  |  棱数  |  顶点数 | 每面边数 | 每顶点棱数 |      备注      |
| :---: | :--: | :--: | :--: | :--: | :---: | :----------: |
|  正四面体 |  $4$ |  $6$ |  $4$ |  $3$ |  $3$  |              |
|  正六面体 |  $6$ | $12$ |  $8$ |  $4$ |  $3$  |     即正方体     |
|  正八面体 |  $8$ | $12$ |  $6$ |  $3$ |  $4$  | 两个正四棱锥上下叠在一起 |
| 正十二面体 | $12$ | $30$ | $20$ |  $5$ |  $3$  |              |
| 正二十面体 | $20$ | $30$ | $12$ |  $3$ |  $5$  |              |

## 多面体 \{#\_8}

### 棱柱 \{#\_9}

![棱柱|right](data:image/avif;base64,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)
- 棱柱：上下底面平行（且全等），各侧面都是四边形，侧面的公共边互相平行。

- 棱柱分为直棱柱和**斜棱柱**（右图）。

- 底面是 $n$ 边形，叫做 $n$ 棱柱。

- 底面为正 $n$ 边形，叫做正 $n$ 棱柱。

- 侧棱竖直的 $n$ 棱柱，叫做直 $n$ 棱柱。

- 底面是平行四边形，叫做平行六面体。

根据祖暅原理，任何棱柱都可以转化为一个长方体，从而：

$$
V=Sh
$$

### 棱锥 \{#\_10}

- 侧面都是三角形，有公共顶点。

- 底面是 $n$ 边形，有 $n$ 个侧面，叫做 $n$ 棱锥。

- 底面是正 $n$ 边形，且顶点在底面上的投影在底面中心，叫做正 $n$ 棱锥。

- 有一条侧棱竖直的 $n$ 棱锥，叫做直 $n$ 棱锥。

根据祖暅原理，任何棱锥都可以转化为一个正棱锥，从而：

$$
V=\dfrac\{Sh}3
$$

证明：

$$
V=\int\_\{0}^HS(h)\mathrm\{d}h
$$

其中：

$$
S(h)=S\cdot\dfrac\{h^2}\{H^2}
$$

注意到：

$$
\dfrac\{\mathrm d(Sh^3/3H^2)}\{\mathrm dh}=\dfrac\{Sh^2}\{H^2}
$$

因此：

$$
V=\dfrac\{SH^3}\{3H^2}=\dfrac\{SH}\{3}
$$

这个公式对所有椎体成立。

### 棱台 \{#\_11}

- 将棱锥用一个平行于底面的平面截下，下半部分叫做棱台。

根据祖暅原理，任何棱台都可以转化为一个圆台，从而根据：

$$
V=\dfrac\{h}\{6}\[S+S'+4\times\dfrac\{1}\{4}(S+S'+2\sqrt\{SS'})]=\dfrac h3(S+\sqrt\{SS'}+S')
$$

棱台的体积公式也可以描述为一种希罗平均数：

$$
H=\{\dfrac \{1}\{3}}\left(A+\{\sqrt \{AB}}+B\right)
$$

用以计算棱台或圆台的体积等于棱台或圆台的高乘以两底面面积的希罗平均数。

希罗平均数也可以看成算术平均数与几何平均数的加权平均数。

$$
H=\{\dfrac \{2}\{3}}\cdot \{\dfrac \{A+B}\{2}}+\{\dfrac \{1}\{3}}\cdot \{\sqrt \{AB}}
$$

## 旋转体 \{#\_12}

### 圆柱 \{#\_13}

- 将一个长方形绕着一条边（轴）旋转得到的立体几何图形。

- 侧面的每一条平行于轴的线称为母线。

$$
V=Sh=\pi r^2h
$$

$$
S\_\{表}=2\pi r^2+2\pi rh=2\pi(r+h)
$$

显然。

### 圆锥 \{#\_14}

- 将一个直角三角形绕着一条直角边（轴）旋转得到的立体几何图形。

- 直角三角形的每一个斜边对应的线称为母线。

根据祖暅原理：

$$
V=\dfrac13Sh=\dfrac13\pi r^2h
$$

也可以用定积分算。

表面积可以直接拆分为侧面和底面：

$$
S=\pi r^2+\pi rl=\pi r(r+l)
$$

其中 $l$ 表示母线的长度：

$$
l=\sqrt\{r^2+h^2}
$$

### 圆台 \{#\_15}

- 将一个直角梯形绕着它的直角边（轴）旋转得到的立体几何图形。

- 直角梯形的每一个斜边对应的线称为母线。

- 也可以视为将圆台用一个平行于底面的平面截下，下半部分叫做圆台。

根据辛普森法则：

$$
V=\dfrac16h\left\[\pi r^2+\pi\left(\dfrac\{r+R}\{2}\right)^2+\pi R^2\right]=\dfrac\{\pi h}3(r^2+rR+R^2)
$$

表面积同样可以拆分：

$$
S=\pi\[r^2+(r+R)l+R^2]
$$

其中 $l$ 表示母线的长度：

$$
l=\sqrt\{h^2+(R-r)^2}
$$

## 方法总结 \{#\_16}

### 投影法 \{#\_17}

三棱锥 $ P-ABC $ 中，点 $ P $ 在平面 $ ABC $ 中的射影为 $ O $：

1. 若 $ PA=PB=PC $，则 $ O $ 是 $ \triangle ABC $ 的**外心**。
2. 若 $ PA $, $ PB $, $ PC $ 与平面 $ ABC $ 所成角相等，则 $ O $ 是 $ \triangle ABC $ 的**外心**。
3. 若 $ P $ 到 $ \triangle ABC $ 各边的距离相等，则 $ O $ 是 $ \triangle ABC $ 的**内心**。
4. 若三侧面与底面所成的二面角相等，则 $ O $ 是 $ \triangle ABC $ 的**内心**。
5. 若 $ PA \perp PB $, $ PA \perp PC $, $ PB \perp PC $，则 $ O $ 是 $ \triangle ABC $ 的**垂心**。
6. 若 $ PA \perp BC $, $ PB \perp AC $, $ PC \perp AB $，则 $ O $ 是 $ \triangle ABC $ 的**垂心**。

### 补形补体 \{#\_18}

1. 若四面体有三条棱两两互相垂直，则可将其放入某个长方体内。
2. 若四面体的四个面均是直角三角形，则可将其放入某个长方体内。
3. 正四面体 $ P-ABC $ 可以补形为正方体且正方体的棱长 $ a = \dfrac\{PA}\{\sqrt\{2}} $。
4. 若四面体的三组对棱分别相等，则可将其放入某个长方体内。

### 截面问题 \{#\_19}

![alt text|w100%](/static/image/image.a1891c123a.avif)
找截面有交线法和平行线法两个常用的方法，本人喜欢先用平行线，然后找交线。

![alt text|w80%](/static/image/截面问题.54249acd5f.avif)
1. 连接被截的若干点。

2. 做面上的平行线、延长线。

3. 算长度，勾股判断图形。

### 最值问题 \{#\_20}

### 翻折问题 \{#\_21}

### 反射问题 \{#\_22}

## 球的概述 \{#\_23}

### 球的定义 \{#\_24}

一个半圆绕着它的直径（轴）旋转得到的立体几何图形。

球内两个端点在球面上且过球心的线段称为直径。

根据球心 $O$ 称一个球为「球 $O$」。

### 球的体积表面积 \{#\_25}

根据辛普森法则：

$$
V=\dfrac\{1}\{6}\times2r\times(0+4\pi r^2+0)=\dfrac43\pi r^3
$$

根据球的表面积等于其外接圆柱的侧面面积（详细看 3B1B 的视频）：

$$
S=2\pi r\times2r=4\pi r^2
$$

### 球中的定值问题 \{#\_26}

画一个圆，画出上下两个椭圆表示两个截面，有勾股定理。

### 球中的最值问题 \{#\_27}

## 外接球问题 \{#\_28}

### 方体的外接球 \{#\_29}

容易发现，长方体外接球直径就是其对角线的长度，也就是：

$$
R=\dfrac\{\sqrt\{a^2+b^2+c^2}}\{2}
$$

### 棱锥的外接球 \{#\_30}

我们尝试求出外接球的半径 $R$ 找到三棱锥的一个底面 $ABC$，容易发现外接球的球心 $O$ 在底面的投影一定是 $ABC$ 的外心（$r=AH=BH=CH$），另外根据 $OD=R$，那么就有：

$$
R^2=OH^2+r^2=R^2
$$

其中 $r$ 为底面外接圆半径，可以通过正弦定理求出。

特殊的，若顶点在底面任意顶点正上方，则外接球球心位与底面外接圆正上方 $h=H/2$ 处。

对于 $n$ 棱锥也类似。

### 棱柱的外接球 \{#\_31}

同样是找底面的外接圆圆心，然后向上做高 $h$ 即可。

特殊的，如果是直棱柱，$h=H/2$ 其中 $H$ 是体的高度。

### 三棱锥内切球 \{#\_32}

注意到可以将三棱锥分为，等面积法：

$$
V=\dfrac\{1}\{3}S\_1r+\dfrac\{1}\{3}S\_2r+\dfrac\{1}\{3}S\_3r+\dfrac\{1}\{3}S\_4r
$$

即：

$$
r=\dfrac\{3V}\{S\_1+S\_2+S\_3+S\_4}=\dfrac\{3V}\{S\_表}
$$
