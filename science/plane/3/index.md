# 三角函数题型 {#_1}

## 函数思想 {#_2}

### 变角思想 {#_3}

在三角函数式的化简中，"次降角升"和"次升角降"是基本的规律，根号中含有三角函数式时，一般需要升次。其化简往往要遵循以下三个原则：

1.  一看"角"，这是最重要的一环，通过看角之间的差别与联系，把角进行合理的拆分，从而正确使用公式；
2.  二看"函数名称"，看函数名称之间的差异，从而确定使用的公式，常见的有"切化弦"等；
3.  三看"结构特征"，分析结构特征，可以帮助我们找到变形的方向，如"遇到分式要通分"等。

我们知道单独考查三角函数式的化简是极少见的，绝大多数的化简其背后就是求值，常见的求值问题有：给值求值、给角求值、给值求角。

![变角](../图片1.avif#class="custom-img";align="right";float=30%"

三角函数：角为先，公式特征为要。

公式特征注意：用 $\cos2\alpha$ 联系 $\sin\alpha,\cos\alpha$。

$$
4\sin\alpha\cos\alpha=(\sin\alpha+\cos\alpha)^2-(\sin\alpha-\cos\alpha)^2
$$

右图为这三者的转换关系。

$$
\left\{ \begin{aligned} x&=\sin\alpha-\sin\beta\\ y&=\cos\alpha-\cos\beta \end{aligned} \right.
$$

根据上面的可以推出 $\alpha,\beta$ 和差角的正余弦。

- 两式平方后作和、平方后作差。

- 两式相乘。

也可以换元，设 $t$ 为 $\sin,\cos$ 等，将原式化为关于 $t$ 的二次函数或分式。

注意求区间上的值域，也可以结合不等式相关内容。

### 一角一函数 {#_4}

一角一函数，可以简单的理解为 $y=A\sin(\omega x+\varphi)$ 的形式。

即一个角在一个三角函数里，可以更好的求解。

### 齐次思想 {#_5}

齐次思想，也可以归为次数的重要性。

三角函数中，弦为一次，切为零次，割为负一次。

例如对于求值类问题，升幂降角、降幂升角，是很关键的。

当一个式子中的函数次数仅为奇数后者偶数的时候，可以补充 $\sin^2+\cos^2=1$ 齐次。

也可以结合弦化切，除以一个 $\sin^2+cos^2$ 的若干次方。

当然也存在次数的奇偶性转化，例如：

$$
\sin-\cos=\pm\sqrt{(\sin^2-\cos^2)}=\pm\sqrt{1-2\sin\cos}
$$

这种不常用，注意正负号。

### 整体角思想 {#_6}

整体角，即将 $y=A\sin(\omega x+\varphi)$ 中的 $\omega x+\varphi$ 设为单独的变量如 $t$ 后进行解决的思想。

化为一角一函数后，用整体角结合三角函数性质进行快速解决。

根据整体角的范围，画出函数图像或者列出关于 $k,k\in\mathbb Z$ 的方程。

注意区间的开闭问题。

### 弦化切思想 {#_7}

切化弦通常是很容易想到的，我们直接令：

$$
\tan\alpha=\dfrac{\sin\alpha}{\cos\alpha}
$$

但是弦化切也有很大的用处，具体体现在：

- 将一个复杂的式子化为仅关于一个变量的式子。

- 对于某些求值类问题，可以使用正切半角公式（万能公式）。

## 三角函数求参数 {#_8}

### 参变分离思想 {#_9}

也就是主元思想的体现，将参数作为主元化简。

然后根据等式右侧的函数性质得到参数的特征。

也可以使用等式相当于左右两侧函数交点问题。

### 不同参数的常见求法 {#_10}

对于：

$$
y=A\sin(\omega x+\varphi)+B
$$

- $A$：振幅。

- $B$：极值。

- $\omega$：周期。

- $\varphi$：通常带入求解。

### 根据周期长度解题 {#_11}

对于有多少零点的问题，可以在还原之前根据区间长度和周期长度得到一个大体的范围。

给定单调区间，首先可以写出，单调区间长度小于等于半周期，即：

$$
r_0-l_0\le\frac{T}{2}=\frac{\pi}{\omega}
$$

然后就可以在这个大体的范围内求解，如果不好求解也会方便枚举。

然后如果可以求出 $\omega$ 的一些其他条件（比如奇偶性），直接求出来。

### 已知起点终点 {#_12}

思想：复合函数、还原。

对于 $f(x)=A\sin(\omega x+\varphi)$，我们令 $t=\omega x+\varphi$。

注意 $\omega$ 的正负性，得出 $t$ 的取值范围，进行进一步求解。

比如，给定零点横坐标、对称轴，转化为：

$$
\omega x_0+\varphi=\lambda k\pi(+\pi/2)
$$

未知 $\varphi$：根据已知点或特殊信息（对称轴、对称中心）带入，列出方程组求出 $\varphi$。

### 未知起点终点 {#_13}

可以将问题再分为：正正、正负。

- 对于正负的，通常区间内存在一个已知点（$\omega=0$），画图解题。

- 对于正正的，通常先用周期长度限制，然后列关于 $k$ 的式子。

特殊的，如果 $\omega$ 的正负不确定，应当讨论 $\operatorname{sgn}(\omega)$。

### $\varphi$ 未知求 $\omega$ {#varphi-omega}

这一类问题通常比较难：

- 各种条件，先转化为区间长度，初步限制 $\omega$ 的范围。

- 根据特殊信息，限制 $\omega$ 的奇偶性等性质。

- 在独立的 $\omega$ 取值中，一次判断是否满足条件。

比较难算。

## 三角形中的三角函数 {#_14}

条件，在三角形中，有 $x+y+z=\pi$（三角形内角和），那么：

### 正切恒等式 {#_15}

#### 形式一 {#_16}

$$
\tan x+\tan y+\tan z=\tan x\tan y\tan z
$$

证明：

$$
\begin{aligned} \tan z&=\tan(\pi-x-y)=-\tan(x+y)\\ \tan z&=-{\tan x+\tan y\over1-\tan x\tan y} \end{aligned}
$$

下面的式子整理即可。

#### 形式二 {#_17}

$$
\tan{x\over2}\tan{y\over2}+\tan{y\over2}\tan{z\over2}+\tan{z\over2}\tan{x\over2}=1
$$

证明：

$$
\begin{aligned} \tan{z\over2}&=\tan\left({\pi\over2}-{x\over2}-{y\over2}\right)={1\over\tan({x\over2}+{y\over2})}\\ \tan{z\over2}&={1-\tan{x\over2}\tan{y\over2}\over\tan{x\over2}+\tan{y\over2}} \end{aligned}
$$

下面的式子整理即可。

### 余切恒等式 {#_18}

#### 形式一 {#_19}

$$
\cot x\cot y+\cot y\cot z+\cot z\cot x=1
$$

证明：

根据 $\displaystyle\tan\alpha={1\over\cot\alpha}$ 展开正切的形式一即可。

#### 形式二 {#_20}

$$
\cot{x\over2}+\cot{y\over2}+\cot{y\over2}=\cot{x\over2}\cot{y\over2}\cot{y\over2}
$$

证明：

根据 $\displaystyle\tan\alpha={1\over\cot\alpha}$ 展开正切的形式二即可。

### 一倍角弦 {#_21}

#### 形式一 {#_22}

$$
\sin x+\sin y+\sin z=4\cos{x\over2}\cos{y\over2}\cos{z\over2}
$$

证明：

$$
\begin{aligned} \sin x+\sin y&=2\sin{x+y\over2}\cos{x-y\over2}\\ &=2\cos{z\over2}\cos{x-y\over2}\\ \sin z&=2\sin{z\over2}\cos{z\over2}\\ &=2\cos{z\over2}\cos{x+y\over2} \end{aligned}
$$

然后加起来用和差化积公式即可。

#### 形式二 {#_23}

$$
\cos x+\cos y+\cos z=1+4\sin{x\over2}\sin{y\over2}\sin{z\over2}
$$

证明：

$$
\begin{aligned} \cos z&=1-\sin^2{z\over2}\\ &=1-\sin{z\over2}\cos{x+y\over2}\\ \cos x+\cos y&=2\cos{x+y\over2}\cos{x-y\over2}\\ &=2\sin{z\over2}\cos{x-y\over2} \end{aligned}
$$

然后加起来用和差化积公式即可。

### 二倍角弦 {#_24}

#### 形式一 {#_25}

$$
\sin2x+\sin2y+\sin2z=4\sin x\sin y\sin z
$$

证明：

$$
\begin{aligned} \sin2z&=2\sin z\cos z\\ &=-2\sin z\cos(x+y)\\ \sin2x+\sin2y&=2\sin(x+y)\cos(x-y)\\ &=2\sin z\cos(x-y) \end{aligned}
$$

然后加起来用和差化积公式即可。

#### 形式二 {#_26}

$$
\cos2x+\cos2y+\cos2z=-1-\cos x\cos y\cos z
$$

证明：

$$
\begin{aligned} \cos2z&=2\cos^2z-1\\ &=-2\cos z\cos(x+y)-1\\ \cos2x+\cos2y&=2\cos(x+y)\cos(x-y)\\ &=-2\cos z\cos(x-y) \end{aligned}
$$

然后加起来用和差化积公式即可。

## 例题 {#_27}

### 例题一 {#_28}

已知 $\tan\beta$ 有意义，且 $\sin(\alpha+\beta)={1\over2}$，$\sin(\alpha-\beta)={1\over3}$，求 $\dfrac{\tan\alpha}{\tan\beta}$。

S1：和差恒等式

易得：

$$
\begin{cases} \sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta={1\over2}\\ \sin(\alpha-\beta)=\sin\alpha\cos\beta-\cos\alpha\sin\beta={1\over3}\\ \end{cases}
$$

解得：

$$
\begin{cases} \sin\alpha\cos\beta={5\over12}\\ \cos\alpha\sin\beta={1\over12}\\ \end{cases}
$$

易知：

$$
{\tan\alpha\over\tan\beta}={\sin\alpha\cos\beta\over\cos\alpha\sin\beta}={{5\over12}\over{1\over12}}=5
$$

S2：和差化积恒等式

易得：

$$
\begin{cases} \sin(\alpha+\beta)+\sin(\alpha-\beta)=2\sin\alpha\cos\beta={1\over2}+{1\over3}={5\over6}\\ \sin(\alpha+\beta)-\sin(\alpha-\beta)=2\cos\alpha\sin\beta={1\over2}-{1\over3}={1\over6} \end{cases}
$$

易知：

$$
{\tan\alpha\over\tan\beta}={2\sin\alpha\cos\beta\over2\cos\alpha\sin\beta}={{5\over6}\over{1\over6}}=5
$$

### 例题二 {#_29}

已知 $\theta\in[0,2\pi)$ 且 $\sin(x+\theta)$ 是偶函数，求 $\theta$。

根据偶函数定义：

$$
\begin{aligned} \sin(x+\theta)=\sin(-x+\theta)\\ \sin\theta\cos x+\cos\theta\sin x=\sin\theta\cos x-\cos\theta\sin x\\ \cos\theta\sin x=0 \end{aligned}
$$

因为 $x\in\mathbb R$，所以 $\cos\theta=0$，即： $\displaystyle\theta={\pi\over2}/{3\pi\over2}$。

知识点：偶函数、和差恒等式。

### 例题三 {#_30}

求函数 $\displaystyle g(x)=\sin^2\left(x+{\pi\over12}\right)+\sin^2\left(x+{\pi\over4}\right)$ 的值域。

化简：

$$
\begin{aligned} &\sin^2\left(x+{\pi\over12}\right)+\sin^2\left(x+{\pi\over4}\right)\\ =\;&{1\over2}\left[1-\cos\left(2x+{\pi\over6}\right)+1-\cos\left(2x+{\pi\over2}\right)\right]\\ =\;&1-{1\over2}\left[\cos\left(2x+{\pi\over6}\right)+\cos\left(2x+{\pi\over2}\right)\right]\\ =\;&1-{1\over2}\left({\sqrt3\over2}\cos2x-{1\over2}\sin2x-\sin2x\right)\\ =\;&1+{1\over4}\left(3\sin2x-\sqrt3\cos2x\right)\\ =\;&1+{\sqrt3\over2}\sin\left(2x-{\pi\over6}\right)\end{aligned}
$$

然后就忒简单了，答案是，函数 $g$ 的值域为 $\displaystyle\left[1-{\sqrt3\over2},1+{\sqrt3\over2}\right]$。

知识点：函数、和差恒等式、降次公式、辅助角公式。

另外：最后辅助角公式的应用中，$\arctan b/a$ 可以不用算出来，因为 $x$ 属于实数域，$\sin$ 函数里面一定是任何一个实数都取得到，直接取 $r=\sqrt{a^2+b^2}=2\sqrt3$ 即可得出答案。

### 例题四 {#_31}

求值：

$$
\cos20\degree\cos40\degree\cos80\degree
$$

答案：

$$
\begin{aligned} S&=\dfrac{1}{\sin20\degree}\sin20\degree\cos20\degree\cdot\cos40\degree\cos80\degree\\ &=\dfrac{1}{2\sin20\degree}\sin40\degree\cos40\degree\cdot\cos80\degree\\ &=\dfrac{1}{4\sin20\degree}\sin80\degree\cos80\degree\\ &=\dfrac{1}{8\sin20\degree}\sin160\degree=\dfrac{1}{8} \end{aligned}
$$

本质是角的变换。

### 例题五 {#_32}

求值：

$$
\sin10\degree+\dfrac{\sqrt3}4\tan10\degree
$$

答案：

$$
\begin{aligned} S&=\dfrac{4\sin10\degree\cos10\degree+\sqrt3\sin10\degree}{4\cos10\degree}\\ &=\dfrac{2\sin(30\degree-10\degree)+\sqrt3\sin10\degree}{4\cos10\degree}\\ &=\dfrac{\cos10\degree}{4\cos10\degree}=\dfrac14 \end{aligned}
$$

本质也是角的变换。
