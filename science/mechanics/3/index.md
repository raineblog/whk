# 动力学模型 {#_1}

## 动力学模型 {#_2}

### 晾衣绳模型 {#_3}

等腰三角形、晾衣杆问题，特征为动滑轮通过刚性轻绳固定，有公式：

:::: {.arithmatex}
::: {.MathJax_Preview}
F=\dfrac{G}{2\cos\theta}
:::

$$F=\dfrac{G}{2\cos\theta}$$
::::

特征；[]{.arithmatex}$F$ 仅与 []{.arithmatex}$\theta$ 有关，上下移动绳子端点力不变，端点水平靠近拉力下降、远离拉力上升。

物体的平衡可以分为稳定平衡、不稳定平衡和随遇平衡三种。

### 弹簧突变 {#_4}

因为弹簧的弹力无法突变，因此我们：

1.  受力分析初状态，得出弹簧弹力。

2.  把弹簧弹力当做外力，重新受力分析。

沿绳方向速度、受力大小一定相等。

### 斜面模型 {#_5}

斜面模型「物体是否会下滑」，设斜面与水平面夹角为 []{.arithmatex}$\theta$：

受力分析，得 []{.arithmatex}$G_x=mg\sin\theta$，[]{.arithmatex}$f=\mu mg\cos\theta$。

- 若物体下滑：[]{.arithmatex}$G_x>f \Rightarrow G_x/f>1 \Rightarrow \tan\theta/\mu>1 \Rightarrow \tan\theta>\mu$。
- 同理，若物体静止不动，[]{.arithmatex}$G_x\le f \Rightarrow \tan\theta\le\mu$。

即，若 []{.arithmatex}$\tan\theta>\mu$，物体会下滑。

同时也可以根据此探究动摩擦因数 []{.arithmatex}$\mu=\arctan\theta$。

### 直角劈模型 {#_6}

注意物体的位置应该在惯性系中表示，否则应用牛顿定律会产生麻烦。

根据已知常量列出方程，例如绳长不变，绳子切面速度相同，以及对应的加速度关系。

典例是直角劈模型，有 []{.arithmatex}$\theta$ 角度的直角劈，一木块放在上面，则：

![直角劈模型](../mnt847j0.avif)

其中 []{.arithmatex}$V$ 和 []{.arithmatex}$A$ 为劈的速度和加速度，[]{.arithmatex}$x$ 为木块相对参考系的水平位移，[]{.arithmatex}$X$ 为木块相对参考系的水平位移，[]{.arithmatex}$(h-y)$ 为木块滑下的竖直高度：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} (x-X)=(h-y)\cot\theta\\ v_x-V=-v_y\cot\theta\\ a_x-A=-a_y\cot\theta \end{aligned}
:::

$$\begin{aligned}
(x-X)=(h-y)\cot\theta\\
v_x-V=-v_y\cot\theta\\
a_x-A=-a_y\cot\theta
\end{aligned}$$
::::

上式从上到下，实为对方程两边做一次时间变化率，常数项忽略，常数系数不变。

注意：约束方程与作用力无关，各接触面有无摩擦不影响约束方程。

### 狭义连接体模型 {#_7}

整体法可求得加速度。

隔离法可求得压力／绳子拉力，也可以整体一部分物体。

如果绳子是弯的，那么直接两次隔离把力约掉算加速度。

可以得出，绳子拉力与斜面夹角、摩擦因数均无关：

:::: {.arithmatex}
::: {.MathJax_Preview}
T=\dfrac{m_1}{m_1+m_2}F
:::

$$T=\dfrac{m_1}{m_1+m_2}F$$
::::

这个公式可以成为连接体的质量分配原则，其中 []{.arithmatex}$1$ 是绳子没有直接拉着的那个物体。

推广：如果两个物体两侧分别拉着（[]{.arithmatex}$F_1$ 拉质量为 []{.arithmatex}$m_1$ 的物体，[]{.arithmatex}$F_2$ 对于 []{.arithmatex}$m_2$）：

:::: {.arithmatex}
::: {.MathJax_Preview}
T=\dfrac{F_1m_2+F_2m_1}{m_1+m_2}
:::

$$T=\dfrac{F_1m_2+F_2m_1}{m_1+m_2}$$
::::

即总是一个力乘上没有直接连接的物体。

### 等时圆模型 {#_8}

![alt text](../image-2.avif){align="right" width="50%"}

质点自半径为 []{.arithmatex}$R$ 的空心球（对于平面而言是圆环）的最高点由静止开始无摩擦地沿任一弦下滑至球面（或圆环），所需时间相等，且等于：

:::: {.arithmatex}
::: {.MathJax_Preview}
\sqrt{\dfrac{4R}{g}}
:::

$$\sqrt{\dfrac{4R}{g}}$$
::::

证明：

设下滑的弦与法线的夹角为 []{.arithmatex}$\beta$，则弦长：

:::: {.arithmatex}
::: {.MathJax_Preview}
l=2R\cos\beta
:::

$$l=2R\cos\beta$$
::::

沿弦方向加速度为：

:::: {.arithmatex}
::: {.MathJax_Preview}
a=g\cos\beta
:::

$$a=g\cos\beta$$
::::

列运动学方程：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} l&=\dfrac{1}{2}at\^2\\ 2R\cos\beta&=\dfrac{1}{2}(g\cos\beta)t\^2 \end{aligned}
:::

$$\begin{aligned}
l&=\dfrac{1}{2}at^2\\
2R\cos\beta&=\dfrac{1}{2}(g\cos\beta)t^2
\end{aligned}$$
::::

易得 []{.arithmatex}$t$ 与 []{.arithmatex}$\beta$ 无关，且：

:::: {.arithmatex}
::: {.MathJax_Preview}
t=\sqrt{\dfrac{4R}{g}}
:::

$$t=\sqrt{\dfrac{4R}{g}}$$
::::

经典例题：

一小球从角度为 []{.arithmatex}$\alpha$ 的斜面上某一点的上方 []{.arithmatex}$l$ 处沿某一直线无摩擦的滑下，问落到斜面上的最短时间。

由上面的结论，最佳下落线与法线的夹角 []{.arithmatex}$\theta=\alpha/2$。

易知，该圆的直径（[]{.arithmatex}$Q$ 为圆与斜面的切点，[]{.arithmatex}$H$ 为最高点到斜面的垂足）：

:::: {.arithmatex}
::: {.MathJax_Preview}
2R=\dfrac{OQ}{\cos\theta}=\dfrac{OH}{\cos\^2\theta}=\dfrac{l\cos\alpha}{\cos\^2(\alpha/2)}
:::

$$2R=\dfrac{OQ}{\cos\theta}=\dfrac{OH}{\cos^2\theta}=\dfrac{l\cos\alpha}{\cos^2(\alpha/2)}$$
::::

则：

:::: {.arithmatex}
::: {.MathJax_Preview}
R=\dfrac{l\cos\alpha}{1+\cos\alpha}
:::

$$R=\dfrac{l\cos\alpha}{1+\cos\alpha}$$
::::

则最短时间：

:::: {.arithmatex}
::: {.MathJax_Preview}
t=\sqrt{\dfrac{4R}{g}}=2\sqrt{\dfrac{l\cos\alpha}{g(1+\cos\alpha)}}
:::

$$t=\sqrt{\dfrac{4R}{g}}=2\sqrt{\dfrac{l\cos\alpha}{g(1+\cos\alpha)}}$$
::::

等时圆的构造：

设定一点为最高点或最低点即可，根据几何关系得到距离圆心的距离。

### 最速降线问题 {#_9}

在平面内，[]{.arithmatex}$B$ 点在 []{.arithmatex}$A$ 右下，自 []{.arithmatex}$A$ 静止释放一个小球，运动到 []{.arithmatex}$B$ 点的最短时间。

![](../%E6%9C%80%E9%80%9F%E9%99%8D%E7%BA%BF.avif){width="100%"}

伯努利（哥哥和弟弟分别）证明了最速降线是一条摆线。

## 传送带和板块模型 {#_10}

![](../%E6%96%B9%E6%B3%95%E6%80%BB%E7%BB%93.avif){width="90%"}

**例题1**：质量为 []{.arithmatex}$2\text{kg}$ 的物体沿光滑斜面下滑，斜面与水平面的夹角为 []{.arithmatex}$37^\circ$，求木块的加速度。

列式：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} F_r&=ma\\ F_r&=G\sin37\^\circ\\ G&=mg\\ m&=2\text{kg} \end{cases}
:::

$$\begin{cases}
F_r&=ma\\
F_r&=G\sin37^\circ\\
G&=mg\\
m&=2\text{kg}
\end{cases}$$
::::

解得：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} m&=2&\text{kg}\\ G&=20&\text{N}\\ F_r&=12&\text{N}\\ a&=6&\text{m/s}\^2\\ \end{cases}
:::

$$\begin{cases}
m&=2&\text{kg}\\
G&=20&\text{N}\\
F_r&=12&\text{N}\\
a&=6&\text{m/s}^2\\
\end{cases}$$
::::

所以，加速度为 []{.arithmatex}$6\text{m/s}^2$，方向沿斜面向下。

**例题2**：质量为 []{.arithmatex}$2\text{kg}$ 的物体沿斜面下滑，斜面的摩擦因数为 []{.arithmatex}$0.2$，斜面与水平面的夹角为 []{.arithmatex}$37^\circ$，求木块的加速度。

列式：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} F_r&=ma\\ F_r&=G\sin37\^\circ-f\\ f&=\mu N\\ N&=G\cos37\^\circ\\ G&=mg\\ m&=2\text{kg} \end{cases}
:::

$$\begin{cases}
F_r&=ma\\
F_r&=G\sin37^\circ-f\\
f&=\mu N\\
N&=G\cos37^\circ\\
G&=mg\\
m&=2\text{kg}
\end{cases}$$
::::

解得：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} m&=2&\text{kg}\\ G&=20&\text{N}\\ N&=16&\text{N}\\ f&=3.2&\text{N}\\ F_r&=8.8&\text{N}\\ a&=4.4&\text{m/s}\^2\\ \end{cases}
:::

$$\begin{cases}
m&=2&\text{kg}\\
G&=20&\text{N}\\
N&=16&\text{N}\\
f&=3.2&\text{N}\\
F_r&=8.8&\text{N}\\
a&=4.4&\text{m/s}^2\\
\end{cases}$$
::::

所以，加速度为 []{.arithmatex}$4.4\text{m/s}^2$，方向沿斜面向下。

**例题3**：质量为 []{.arithmatex}$2\text{kg}$ 的物体静止于水平面的 []{.arithmatex}$A$ 处，[]{.arithmatex}$AB$ 间距 []{.arithmatex}$L=20\text{m}$，如图：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{matrix} \underline{\kern{1em}\Box\kern{7em}\Box\kern{1em}}\\\[-0.8em\] \cdot\kern{7.5em}\cdot\\\[-0.4em\] {\small{A}}\kern{7em}{\small{B}} \end{matrix}
:::

$$\begin{matrix}
\underline{\kern{1em}\Box\kern{7em}\Box\kern{1em}}\\[-0.8em]
\cdot\kern{7.5em}\cdot\\[-0.4em]
{\small{A}}\kern{7em}{\small{B}}
\end{matrix}$$
::::

现用大小为 []{.arithmatex}$30\text{N}$ 的力，沿水平方向拉物体，[]{.arithmatex}$2\text{s}$ 后到达 []{.arithmatex}$B$ 处。

求物体与地面的摩擦因数 []{.arithmatex}$\mu$。

解：

对物体 []{.arithmatex}$A$ 受力分析：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} F_r&=F-f\\ N&=G \end{cases}
:::

$$\begin{cases}
F_r&=F-f\\
N&=G
\end{cases}$$
::::

展开：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} ma&=F-\mu N\\ N&=mg \end{cases}
:::

$$\begin{cases}
ma&=F-\mu N\\
N&=mg
\end{cases}$$
::::

得到方程组：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} x&=\dfrac{1}{2}at\^2\\ ma&=F-\mu mg \end{cases}
:::

$$\begin{cases}
x&=\dfrac{1}{2}at^2\\
ma&=F-\mu mg
\end{cases}$$
::::

代数，得：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} 20\text{m}&=\dfrac{1}{2}a\cdot(2\text{s})\^2\\ 2\text{kg}\cdot a&=30\text{N}-\mu\cdot20\text{N} \end{cases}
:::

$$\begin{cases}
20\text{m}&=\dfrac{1}{2}a\cdot(2\text{s})^2\\
2\text{kg}\cdot a&=30\text{N}-\mu\cdot20\text{N}
\end{cases}$$
::::

解得：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} a&=10\text{m/s}\^2\\ \mu&=0.5 \end{cases}
:::

$$\begin{cases}
a&=10\text{m/s}^2\\
\mu&=0.5
\end{cases}$$
::::

即 []{.arithmatex}$\mu=0.5$。

### 传送带模型 {#_11}

加速度：

:::: {.arithmatex}
::: {.MathJax_Preview}
a=g\sin\theta\pm\mu g\cos\theta
:::

$$a=g\sin\theta\pm\mu g\cos\theta$$
::::

表示重力下滑分量和滑动摩擦力的作用。

假设可以共速静止，比较 []{.arithmatex}$\tan\theta$ 和 []{.arithmatex}$\mu$。

判断共速时的位与和传送带长度之间的关系。

善用 []{.arithmatex}$v-t$ 图像。

### 一板一物模型 {#_12}

地面光滑：

- 木板有初速度。

- 木板无初速度。

地面不光滑：

- 木板有初速度。

- 木板无初速度。

详见[课件](https://huggingface.co/datasets/RainPPR/whk/resolve/main/physics/%E7%AC%AC13%E8%AE%B2%20%E6%9D%BF%E5%9D%97%E6%A8%A1%E5%9E%8B.pdf)内容。

### 叠加体相对静止 {#_13}

广义连接体，指不用绳子连接的连接体，常见的有用静摩擦力、刚体弹力提供的。

叠加体相对静止，可以看为是由摩擦力提供拉力的连接体模型，因此下面的步骤也非常相似。

整体法可求得加速度。

隔离法可求得摩擦力，也可以整体一部分物体。

可以得出，摩擦力与斜面夹角无关，与摩擦因数有关：

:::: {.arithmatex}
::: {.MathJax_Preview}
f=\dfrac{m_1}{m_1+m_2}F-\mu mg\cos\theta
:::

$$f=\dfrac{m_1}{m_1+m_2}F-\mu mg\cos\theta$$
::::

若斜面是水平面（[]{.arithmatex}$\theta=0$），那么 []{.arithmatex}$\cos\theta=1$：

:::: {.arithmatex}
::: {.MathJax_Preview}
f=\dfrac{m_1}{m_1+m_2}F-\mu mg
:::

$$f=\dfrac{m_1}{m_1+m_2}F-\mu mg$$
::::

同样也类似质量分配原则，其中 []{.arithmatex}$1$ 是力没有直接作用在的那个物体。

### 叠加体相对滑动 {#_14}

1.  找到不受外力的物体，即可能会发生相对滑动的物体，
2.  隔离法，求出这个物体的最大加速度，
3.  整体法，求出最大的外力大小。

形式一：拉着下面的 []{.arithmatex}$M$ 走，其上表面 []{.arithmatex}$\mu_1$、下表面 []{.arithmatex}$\mu_2$：

:::: {.arithmatex}
::: {.MathJax_Preview}
F=(m+M)(\mu_1+\mu_2+\tan\theta)g\cdot\cos\theta
:::

$$F=(m+M)(\mu_1+\mu_2+\tan\theta)g\cdot\cos\theta$$
::::

若斜面是水平面（[]{.arithmatex}$\theta=0$），那么 []{.arithmatex}$\cos\theta=1,\tan\theta=0$：

:::: {.arithmatex}
::: {.MathJax_Preview}
F=(m+M)(\mu_1+\mu_2)g
:::

$$F=(m+M)(\mu_1+\mu_2)g$$
::::

形式二：拉着上面的 []{.arithmatex}$m$ 走，其下 []{.arithmatex}$M$ 上表面 []{.arithmatex}$\mu_1$、下表面 []{.arithmatex}$\mu_2$：

:::: {.arithmatex}
::: {.MathJax_Preview}
F=\dfrac{m}{M}(m+M)(\mu_1-\mu_2)g\cdot\cos\theta
:::

$$F=\dfrac{m}{M}(m+M)(\mu_1-\mu_2)g\cdot\cos\theta$$
::::

若斜面是水平面（[]{.arithmatex}$\theta=0$），那么 []{.arithmatex}$\cos\theta=1$：

:::: {.arithmatex}
::: {.MathJax_Preview}
F=\dfrac{m}{M}(m+M)(\mu_1-\mu_2)g
:::

$$F=\dfrac{m}{M}(m+M)(\mu_1-\mu_2)g$$
::::

注意此形式下，需要上物体能拉动下物体，拉不动的话就更简单了。

## 启动模型 {#_15}

### 解题方法 {#_16}

对（物体），做（运动段），如图（受力分析），列（平衡／牛二）。

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} F\_{\text{合}}=ma&=F-f\\ F&=\frac{P}{v} \end{aligned}
:::

$$\begin{aligned}
F_{\text{合}}=ma&=F-f\\
F&=\frac{P}{v}
\end{aligned}$$
::::

得出（一定要受力分析）：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} F&=f+ma\\ ma&=\frac{P}{v}-f \end{aligned}
:::

$$\begin{aligned}
F&=f+ma\\
ma&=\frac{P}{v}-f
\end{aligned}$$
::::

### 恒定功率启动 {#_17}

随着汽车的加速，

1.  []{.arithmatex}$v$ 增大，[]{.arithmatex}$P$ 不变，[]{.arithmatex}$F$ 减小，[]{.arithmatex}$F_r$ 减小；
2.  []{.arithmatex}$m$ 不变，[]{.arithmatex}$a$ 减小，[]{.arithmatex}$v$ 变化放缓。
3.  直至 []{.arithmatex}$F=f$，汽车匀速运动。

即汽车加速到一定程度后，汽车将保持匀速运动。

### 恒定加速度启动 {#_18}

按照时间顺序：

1.  []{.arithmatex}$a$ 不变，[]{.arithmatex}$m$ 不变，[]{.arithmatex}$f$ 不变，[]{.arithmatex}$F$ 不变；
2.  []{.arithmatex}$v$ 增大，[]{.arithmatex}$P$ 增大，汽车持续增速；
3.  汽车增速到一定程度后，[]{.arithmatex}$P$ 无法继续增大：
4.  此时 []{.arithmatex}$P$ 恒定，故进行恒定功率启动式的加速。

### 做题思路 {#_19}

1.  对匀速运动状态分析：平衡 []{.arithmatex}$F=f$；
2.  对匀加速末状态分析：牛二 []{.arithmatex}$ma=P/v-f$；
3.  对加速阶段状态分析：牛二 []{.arithmatex}$ma=P/v-f$。

### F-1/v 图像 {#f-1v}

按照时间，从右往左，因为汽车速度增大，倒数减小。

- 牵引力为水平直线的：匀加速运动。
- 牵引力逐渐下降的：加速度逐渐减小。
- 牵引力端点位置：最终状态匀速直线运动。

做题方法：同上，一定要分析的是拐点和端点处的受力分析。
