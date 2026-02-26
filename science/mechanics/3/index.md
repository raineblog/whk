# 动力学模型

## 动力学模型

### 晾衣绳模型

等腰三角形、晾衣杆问题，特征为动滑轮通过刚性轻绳固定，有公式：

$$
F=\dfrac\{G}\{2\cos\theta}
$$

特征；$F$ 仅与 $\theta$ 有关，上下移动绳子端点力不变，端点水平靠近拉力下降、远离拉力上升。

物体的平衡可以分为稳定平衡、不稳定平衡和随遇平衡三种。

### 弹簧突变

因为弹簧的弹力无法突变，因此我们：

1. 受力分析初状态，得出弹簧弹力。

2. 把弹簧弹力当做外力，重新受力分析。

沿绳方向速度、受力大小一定相等。

### 斜面模型

斜面模型「物体是否会下滑」，设斜面与水平面夹角为 $\theta$：

受力分析，得 $G\_x=mg\sin\theta$，$f=\mu mg\cos\theta$。

- 若物体下滑：$G\_x>f \Rightarrow G\_x/f>1 \Rightarrow \tan\theta/\mu>1 \Rightarrow \tan\theta>\mu$。
- 同理，若物体静止不动，$G\_x\le f \Rightarrow \tan\theta\le\mu$。

即，若 $\tan\theta>\mu$，物体会下滑。

同时也可以根据此探究动摩擦因数 $\mu=\arctan\theta$。

### 直角劈模型

注意物体的位置应该在惯性系中表示，否则应用牛顿定律会产生麻烦。

根据已知常量列出方程，例如绳长不变，绳子切面速度相同，以及对应的加速度关系。

典例是直角劈模型，有 $\theta$ 角度的直角劈，一木块放在上面，则：

![直角劈模型](data:image/avif;base64,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)
其中 $V$ 和 $A$ 为劈的速度和加速度，$x$ 为木块相对参考系的水平位移，$X$ 为木块相对参考系的水平位移，$(h-y)$ 为木块滑下的竖直高度：

$$
\begin\{aligned} (x-X)=(h-y)\cot\theta\ v\_x-V=-v\_y\cot\theta\ a\_x-A=-a\_y\cot\theta \end\{aligned}
$$

上式从上到下，实为对方程两边做一次时间变化率，常数项忽略，常数系数不变。

注意：约束方程与作用力无关，各接触面有无摩擦不影响约束方程。

### 狭义连接体模型

整体法可求得加速度。

隔离法可求得压力／绳子拉力，也可以整体一部分物体。

如果绳子是弯的，那么直接两次隔离把力约掉算加速度。

可以得出，绳子拉力与斜面夹角、摩擦因数均无关：

$$
T=\dfrac\{m\_1}\{m\_1+m\_2}F
$$

这个公式可以成为连接体的质量分配原则，其中 $1$ 是绳子没有直接拉着的那个物体。

推广：如果两个物体两侧分别拉着（$F\_1$ 拉质量为 $m\_1$ 的物体，$F\_2$ 对于 $m\_2$）：

$$
T=\dfrac\{F\_1m\_2+F\_2m\_1}\{m\_1+m\_2}
$$

即总是一个力乘上没有直接连接的物体。

### 等时圆模型

![alt text|right|w50%](/static/image/image-2.c04a5084e8.avif)
质点自半径为 $R$ 的空心球（对于平面而言是圆环）的最高点由静止开始无摩擦地沿任一弦下滑至球面（或圆环），所需时间相等，且等于：

$$
\sqrt\{\dfrac\{4R}\{g}}
$$

证明：

设下滑的弦与法线的夹角为 $\beta$，则弦长：

$$
l=2R\cos\beta
$$

沿弦方向加速度为：

$$
a=g\cos\beta
$$

列运动学方程：

$$
\begin\{aligned} l&=\dfrac\{1}\{2}at^2\ 2R\cos\beta&=\dfrac\{1}\{2}(g\cos\beta)t^2 \end\{aligned}
$$

易得 $t$ 与 $\beta$ 无关，且：

$$
t=\sqrt\{\dfrac\{4R}\{g}}
$$

经典例题：

一小球从角度为 $\alpha$ 的斜面上某一点的上方 $l$ 处沿某一直线无摩擦的滑下，问落到斜面上的最短时间。

由上面的结论，最佳下落线与法线的夹角 $\theta=\alpha/2$。

易知，该圆的直径（$Q$ 为圆与斜面的切点，$H$ 为最高点到斜面的垂足）：

$$
2R=\dfrac\{OQ}\{\cos\theta}=\dfrac\{OH}\{\cos^2\theta}=\dfrac\{l\cos\alpha}\{\cos^2(\alpha/2)}
$$

则：

$$
R=\dfrac\{l\cos\alpha}\{1+\cos\alpha}
$$

则最短时间：

$$
t=\sqrt\{\dfrac\{4R}\{g}}=2\sqrt\{\dfrac\{l\cos\alpha}\{g(1+\cos\alpha)}}
$$

等时圆的构造：

设定一点为最高点或最低点即可，根据几何关系得到距离圆心的距离。

### 最速降线问题

在平面内，$B$ 点在 $A$ 右下，自 $A$ 静止释放一个小球，运动到 $B$ 点的最短时间。

![alt text|w100%](/static/image/最速降线.4e9fb87f34.avif)
伯努利（哥哥和弟弟分别）证明了最速降线是一条摆线。

## 传送带和板块模型

![alt text|w90%](/static/image/方法总结.bf53825acb.avif)
**例题1**：质量为 $2\text\{kg}$ 的物体沿光滑斜面下滑，斜面与水平面的夹角为 $37^\circ$，求木块的加速度。

列式：

$$
\begin\{cases} F\_r&=ma\ F\_r&=G\sin37^\circ\ G&=mg\ m&=2\text\{kg} \end\{cases}
$$

解得：

$$
\begin\{cases} m&=2&\text\{kg}\ G&=20&\text\{N}\ F\_r&=12&\text\{N}\ a&=6&\text\{m/s}^2\ \end\{cases}
$$

所以，加速度为 $6\text\{m/s}^2$，方向沿斜面向下。

**例题2**：质量为 $2\text\{kg}$ 的物体沿斜面下滑，斜面的摩擦因数为 $0.2$，斜面与水平面的夹角为 $37^\circ$，求木块的加速度。

列式：

$$
\begin\{cases} F\_r&=ma\ F\_r&=G\sin37^\circ-f\ f&=\mu N\ N&=G\cos37^\circ\ G&=mg\ m&=2\text\{kg} \end\{cases}
$$

解得：

$$
\begin\{cases} m&=2&\text\{kg}\ G&=20&\text\{N}\ N&=16&\text\{N}\ f&=3.2&\text\{N}\ F\_r&=8.8&\text\{N}\ a&=4.4&\text\{m/s}^2\ \end\{cases}
$$

所以，加速度为 $4.4\text\{m/s}^2$，方向沿斜面向下。

**例题3**：质量为 $2\text\{kg}$ 的物体静止于水平面的 $A$ 处，$AB$ 间距 $L=20\text\{m}$，如图：

$$
\begin\{matrix} \underline\{\kern\{1em}\Box\kern\{7em}\Box\kern\{1em}}\\\[-0.8em] \cdot\kern\{7.5em}\cdot\\\[-0.4em] \{\small\{A}}\kern\{7em}\{\small\{B}} \end\{matrix}
$$

现用大小为 $30\text\{N}$ 的力，沿水平方向拉物体，$2\text\{s}$ 后到达 $B$ 处。

求物体与地面的摩擦因数 $\mu$。

解：

对物体 $A$ 受力分析：

$$
\begin\{cases} F\_r&=F-f\ N&=G \end\{cases}
$$

展开：

$$
\begin\{cases} ma&=F-\mu N\ N&=mg \end\{cases}
$$

得到方程组：

$$
\begin\{cases} x&=\dfrac\{1}\{2}at^2\ ma&=F-\mu mg \end\{cases}
$$

代数，得：

$$
\begin\{cases} 20\text\{m}&=\dfrac\{1}\{2}a\cdot(2\text\{s})^2\ 2\text\{kg}\cdot a&=30\text\{N}-\mu\cdot20\text\{N} \end\{cases}
$$

解得：

$$
\begin\{cases} a&=10\text\{m/s}^2\ \mu&=0.5 \end\{cases}
$$

即 $\mu=0.5$。

### 传送带模型

加速度：

$$
a=g\sin\theta\pm\mu g\cos\theta
$$

表示重力下滑分量和滑动摩擦力的作用。

假设可以共速静止，比较 $\tan\theta$ 和 $\mu$。

判断共速时的位与和传送带长度之间的关系。

善用 $v-t$ 图像。

### 一板一物模型

地面光滑：

- 木板有初速度。

- 木板无初速度。

地面不光滑：

- 木板有初速度。

- 木板无初速度。

详见\[课件]\([https://huggingface.co/datasets/RainPPR/whk/resolve/main/physics/第13讲](https://huggingface.co/datasets/RainPPR/whk/resolve/main/physics/第13讲) 板块模型.pdf)内容。

### 叠加体相对静止

广义连接体，指不用绳子连接的连接体，常见的有用静摩擦力、刚体弹力提供的。

叠加体相对静止，可以看为是由摩擦力提供拉力的连接体模型，因此下面的步骤也非常相似。

整体法可求得加速度。

隔离法可求得摩擦力，也可以整体一部分物体。

可以得出，摩擦力与斜面夹角无关，与摩擦因数有关：

$$
f=\dfrac\{m\_1}\{m\_1+m\_2}F-\mu mg\cos\theta
$$

若斜面是水平面（$\theta=0$），那么 $\cos\theta=1$：

$$
f=\dfrac\{m\_1}\{m\_1+m\_2}F-\mu mg
$$

同样也类似质量分配原则，其中 $1$ 是力没有直接作用在的那个物体。

### 叠加体相对滑动

1. 找到不受外力的物体，即可能会发生相对滑动的物体，
2. 隔离法，求出这个物体的最大加速度，
3. 整体法，求出最大的外力大小。

形式一：拉着下面的 $M$ 走，其上表面 $\mu\_1$、下表面 $\mu\_2$：

$$
F=(m+M)(\mu\_1+\mu\_2+\tan\theta)g\cdot\cos\theta
$$

若斜面是水平面（$\theta=0$），那么 $\cos\theta=1,\tan\theta=0$：

$$
F=(m+M)(\mu\_1+\mu\_2)g
$$

形式二：拉着上面的 $m$ 走，其下 $M$ 上表面 $\mu\_1$、下表面 $\mu\_2$：

$$
F=\dfrac\{m}\{M}(m+M)(\mu\_1-\mu\_2)g\cdot\cos\theta
$$

若斜面是水平面（$\theta=0$），那么 $\cos\theta=1$：

$$
F=\dfrac\{m}\{M}(m+M)(\mu\_1-\mu\_2)g
$$

注意此形式下，需要上物体能拉动下物体，拉不动的话就更简单了。

## 启动模型

### 解题方法

对（物体），做（运动段），如图（受力分析），列（平衡／牛二）。

$$
\begin\{aligned} F\_\{\text\{合}}=ma&=F-f\ F&=\frac\{P}\{v} \end\{aligned}
$$

得出（一定要受力分析）：

$$
\begin\{aligned} F&=f+ma\ ma&=\frac\{P}\{v}-f \end\{aligned}
$$

### 恒定功率启动

随着汽车的加速，

1. $v$ 增大，$P$ 不变，$F$ 减小，$F\_r$ 减小；
2. $m$ 不变，$a$ 减小，$v$ 变化放缓。
3. 直至 $F=f$，汽车匀速运动。

即汽车加速到一定程度后，汽车将保持匀速运动。

### 恒定加速度启动

按照时间顺序：

1. $a$ 不变，$m$ 不变，$f$ 不变，$F$ 不变；
2. $v$ 增大，$P$ 增大，汽车持续增速；
3. 汽车增速到一定程度后，$P$ 无法继续增大：
4. 此时 $P$ 恒定，故进行恒定功率启动式的加速。

### 做题思路

1. 对匀速运动状态分析：平衡 $F=f$；
2. 对匀加速末状态分析：牛二 $ma=P/v-f$；
3. 对加速阶段状态分析：牛二 $ma=P/v-f$。

### F-1/v 图像

按照时间，从右往左，因为汽车速度增大，倒数减小。

- 牵引力为水平直线的：匀加速运动。
- 牵引力逐渐下降的：加速度逐渐减小。
- 牵引力端点位置：最终状态匀速直线运动。

做题方法：同上，一定要分析的是拐点和端点处的受力分析。
