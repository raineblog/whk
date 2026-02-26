# 极限论

## 函数极限

### 初等函数

我们研究过常数函数、幂函数、指数函数、对数函数、三角函数、反三角函数，它们经过有限次加、减、乘、除、乘方、开方和复合运算，得到的函数称为初等函数。初等函数是数学中最基本的一类函数，具有相当重要的性质。

### 极限定义​

对于函数 $f(x)$ 与实数 $a$，如果存在实数 $b$，使得 $\forall \varepsilon > 0$，$\exist \delta > 0$，对任意 $x \in (a - \delta, a) \cup (a, a + \delta)$，有 $|f(x) - b| < \varepsilon$，则 $b$ 称作 $f(x)$ 在点 $a$ 的极限，记作

$$
\lim_{x \to a} f(x) = b
$$

这就是严格定义函数极限的 $\varepsilon \text - \delta$ 语言。也就是说，对于任意 $\varepsilon > 0$，我们都能找到一段 包含 $a$ 但是扣去 $a$ 的区间，使得这个区间上对应的函数值与 $b$ 的距离都小于 $\varepsilon$，就称函数在点 $a$ 处的极限为 $b$。

可以证明，函数在某点存在极限，则这个极限唯一。

### 极限性质

唯一性：若函数 $f(x)$ 在 $x_0$ 有极限，则极限唯一。

有界性：设函数 $f(x)$ 在 $x_0$ 有极限，则 $f(x)$ 在 $x_0$ 附近有界，即存在正数 $M$ 和 $\delta$，使得只要 $0<|x-x_0|<\delta$，就有 $|f(x)|\le M$。若 $a<l<b$，则在 $x_0$ 附近有 $a<f(x)<b$。

保序性：设 $\lim_{x\to x_0} f(x)=l_1$，$\lim_{x\to x_0} g(x)=l_2$，若在 $x_0$ 附近有 $f(x)\ge g(x)$，则 $l_1\ge l_2$；若 $l_1>l_2$，则在 $x_0$ 附近有 $f(x)>g(x)$。

四则运算：

$$
\lim\limits_{x \to a} [f(x) \pm g(x)] = \lim\limits_{x \to a} f(x) \pm \lim\limits_{x \to a} g(x)
$$

$$
\lim\limits_{x \to a} [f(x)g(x)] = \lim\limits_{x \to a} f(x) \cdot \lim\limits_{x \to a} g(x)
$$

$$
\lim\limits_{x \to a} \dfrac{f(x)}{g(x)} = \dfrac{\lim\limits_{x \to a} f(x)}{\lim\limits_{x \to a} g(x)}
$$

除法应当 $\lim\limits_{x \to a} g(x) \ne 0$ 时。

夹逼定理：设在 $x_0$ 附近有 $g(x)\le f(x)\le h(x)$，且 $\lim_{x\to x_0} g(x)=\lim_{x\to x_0} h(x)=l$，则 $\lim_{x\to x_0} f(x)=l$。

## 极限应用

### 无穷小​

若 $\lim\limits_{x \to a} f(x) = 0$，称 $f(x)$ 为 $x \to a$ 时的无穷小。

根据上面的四则运算规则，可以得知：

- 若 $f(x)$，$g(x)$ 都是 $x \to a$ 时的无穷小，则 $f(x) \pm g(x)$ 是 $x \to a$ 时的无穷小。

- 若 $f(x)$ 是 $x \to a$ 时的无穷小，且 $\lim\limits_{x \to a} g(x)$ 存在，则 $f(x) \cdot g(x)$ 是 $x \to a$ 时的无穷小。

但两个无穷小的商不能确定：运算法则规定了分母不能为无穷小。

设 $f(x)$，$g(x)$ 为 $x \to a$ 时的两个无穷小，且 $g(x) \ne 0$，当 $\lim\limits_{x \to a} \dfrac{f(x)}{g(x)}$ 存在时，

- 若 $\lim\limits_{x \to a} \dfrac{f(x)}{g(x)} = 0$，则称当 $x \to a$ 时，$f(x)$ 是 $g(x)$ 的高阶无穷小。

- 若 $\lim\limits_{x \to a} \dfrac{f(x)}{g(x)} = b \ne 0$，则称当 $x \to a$ 时，$f(x)$ 与 $g(x)$ 是同阶无穷小。

特别地，当 $b = 1$ 时，称当 $x \to a$ 时，$f(x)$ 与 $g(x)$ 是等价无穷小，记作 $f(x) \sim g(x)\quad(x \to a)$。

等价无穷小替换公式：设 $f(x) \sim F(x) \quad (x \to a)$，$g(x) \sim G(x) \quad (x \to a)$，则

$$
\begin{aligned} & \phantom = \lim\limits_{x \to a} \dfrac{f(x)}{g(x)} \\ & = \lim\limits_{x \to a} [\dfrac{F(x)}{G(x)} \cdot \dfrac{f(x)}{F(x)} \cdot \dfrac{G(x)}{g(x)}]\\ & = \lim\limits_{x \to a} \dfrac{F(x)}{G(x)} \cdot \lim\limits_{x \to a} \dfrac{f(x)}{F(x)} \cdot \lim\limits_{x \to a} \dfrac{G(x)}{g(x)} \\ & = \lim\limits_{x \to a} \dfrac{F(x)}{G(x)} \end{aligned}
$$

也即对一个分式求极限时，分子与分母可以替换为它的等价无穷小，而极限值不改变，这个规则称作等价无穷小替换规则。

一个最经典的等价无穷小是 $x \sim \sin x \quad (x \to 0)$ 和它的推论 $x \sim \sin x \sim \cos x \sim \tan x \quad (x \to 0)$（证明从略）。

高中物理中一些公式的推导用到的，所谓「$x$ 很小，将 $\sin x$ 近似为 $x$」的原理，其实就是在做上面的等价无穷小替换。

### 连续性

我们曾用 $\varepsilon$－$\delta$ 语言定义过连续性：设函数 $f$ 在 $x_0$ 附近有定义，如果对于任意的 $\varepsilon>0$，都存在 $\delta>0$，使得只要 $|x-x_0|<\delta$，就有 $|f(x)-f(x_0)|<\varepsilon$，那么称 $f$ 在点 $x_0$ 连续。

现在可以用极限写出更简洁的定义：设函数 $f$ 在 $x_0$ 附近有定义，如果 $\lim_{x\to x_0} f(x)=f(x_0)$，那么称 $f$ 在点 $x_0$ 连续。

如果函数在某一点不连续，那么称在这一点间断。如果函数 $f$ 在开区间 $I$ 的每一点连续，那么称函数 $f$ 是开区间 $I$ 上的连续函数。

函数 $f$ 在点 $x_0$ 连续当且仅当

$$
\lim_{x\to x_0^-}f(x)=\lim_{x\to x_0^+}f(x)=\lim_{x\to x_0}f(x)=f(x_0)
$$

与左右极限对应的左右连续概念为：如果 $\lim_{x\to x_0^-}f(x)=f(x_0)$，称 $f$ 在 $x_0$ 左连续；如果 $\lim_{x\to x_0^+}f(x)=f(x_0)$，称 $f$ 在 $x_0$ 右连续。

对于闭区间 $I$ 上的函数 $f$，如果 $f$ 在区间内每一点都连续，且在左端点右连续、右端点左连续，那么称函数 $f$ 是闭区间 $I$ 上的连续函数。

### 间断点

我们再来考虑间断点。间断点有三种情况：

1.  函数在某一点存在极限，即左右极限相等，但与函数值不相等，或者函数在这一点没有定义，即

    $$
    \lim_{x\to x_0^-} f(x)=\lim_{x\to x_0^+} f(x)\ne f(x_0)
    $$

    这类间断点称为可去间断点。因为只要修改这一点，就能变为连续函数，例如

    $$
    g(x)= \begin{cases} f(x) & x\ne x_0 \\ \lim_{x\to x_0} f(x) & x=x_0 \end{cases}
    $$

2.  函数在某一点的左右极限存在但不相等，即

    $$
    \lim_{x\to x_0^-} f(x)\ne \lim_{x\to x_0^+} f(x)
    $$

    这类间断点称为跳跃间断点。因为函数在 $x_0$ 处发生了

    $$
    \left|\lim_{x\to x_0^-} f(x)-\lim_{x\to x_0^+} f(x)\right|
    $$

    的跳跃。可去间断点和跳跃间断点统称为第一类间断点。

3.  函数在某一点的左右极限至少有一个不存在。这类间断点称为第二类间断点。例如，对于狄利克雷函数

    $$
    D(x)= \begin{cases} 1 & x\in \mathbb{Q} \\ 0 & x\in \mathbb{R}-\mathbb{Q} \end{cases}
    $$

    任意的 $x_0\in \mathbb{R}$ 都是其第二类间断点。

连续函数的四则运算和复合函数具有连续性。设函数 $f(x)$、$g(x)$ 在 $x_0$ 连续，则 $f(x)\pm g(x)$、$f(x)g(x)$、$\dfrac{f(x)}{g(x)}$（$g(x)\ne 0$）也在 $x_0$ 连续。

设函数 $u=g(x)$ 在区间 $I$ 有定义，$y=f(u)$ 在区间 $J$ 有定义，且 $g(I)\subset J$。若 $g$ 在 $x_0\in I$ 处连续，$f$ 在 $u_0=g(x_0)$ 处连续，则复合函数 $f\circ g$ 在 $x_0$ 处连续，即

$$
\lim_{x\to x_0} f\big(g(x)\big) = f\left(\lim_{x\to x_0} g(x)\right) = f\big(g(x_0)\big)
$$

此外，连续函数的反函数同样是连续函数。

连续函数还具有局部保号性：设函数 $f$ 在 $x_0$ 处连续，且 $f(x_0)\ne 0$，则存在 $\delta>0$，使得只要 $0<|x-x_0|<\delta$，就有 $f(x)f(x_0)>0$。

可以证明，所有初等函数在定义域上都处处连续。
