# 极限论 {#_1}

## 函数极限 {#_2}

### 初等函数 {#_3}

我们研究过常数函数、幂函数、指数函数、对数函数、三角函数、反三角函数，它们经过有限次加、减、乘、除、乘方、开方和复合运算，得到的函数称为初等函数。初等函数是数学中最基本的一类函数，具有相当重要的性质。

### 极限定义​ {#_4}

对于函数 [\$f(x)\$]{.arithmatex} 与实数 [\$a\$]{.arithmatex}，如果存在实数 [\$b\$]{.arithmatex}，使得 [\$\forall \varepsilon \> 0\$]{.arithmatex}，[\$\exist \delta \> 0\$]{.arithmatex}，对任意 [\$x \in (a - \delta, a) \cup (a, a + \delta)\$]{.arithmatex}，有 [\$\|f(x) - b\| \< \varepsilon\$]{.arithmatex}，则 [\$b\$]{.arithmatex} 称作 [\$f(x)\$]{.arithmatex} 在点 [\$a\$]{.arithmatex} 的极限，记作

::: {.arithmatex}
\$\$ \lim\_{x \to a} f(x) = b \$\$
:::

这就是严格定义函数极限的 [\$\varepsilon \text - \delta\$]{.arithmatex} 语言。也就是说，对于任意 [\$\varepsilon \> 0\$]{.arithmatex}，我们都能找到一段 包含 [\$a\$]{.arithmatex} 但是扣去 [\$a\$]{.arithmatex} 的区间，使得这个区间上对应的函数值与 [\$b\$]{.arithmatex} 的距离都小于 [\$\varepsilon\$]{.arithmatex}，就称函数在点 [\$a\$]{.arithmatex} 处的极限为 [\$b\$]{.arithmatex}。

可以证明，函数在某点存在极限，则这个极限唯一。

### 极限性质 {#_5}

唯一性：若函数 [\$f(x)\$]{.arithmatex} 在 [\$x_0\$]{.arithmatex} 有极限，则极限唯一。

有界性：设函数 [\$f(x)\$]{.arithmatex} 在 [\$x_0\$]{.arithmatex} 有极限，则 [\$f(x)\$]{.arithmatex} 在 [\$x_0\$]{.arithmatex} 附近有界，即存在正数 [\$M\$]{.arithmatex} 和 [\$\delta\$]{.arithmatex}，使得只要 [\$0\<\|x-x_0\|\<\delta\$]{.arithmatex}，就有 [\$\|f(x)\|\le M\$]{.arithmatex}。若 [\$a\<l\<b\$]{.arithmatex}，则在 [\$x_0\$]{.arithmatex} 附近有 [\$a\<f(x)\<b\$]{.arithmatex}。

保序性：设 [\$\lim\_{x\to x_0} f(x)=l_1\$]{.arithmatex}，[\$\lim\_{x\to x_0} g(x)=l_2\$]{.arithmatex}，若在 [\$x_0\$]{.arithmatex} 附近有 [\$f(x)\ge g(x)\$]{.arithmatex}，则 [\$l_1\ge l_2\$]{.arithmatex}；若 [\$l_1\>l_2\$]{.arithmatex}，则在 [\$x_0\$]{.arithmatex} 附近有 [\$f(x)\>g(x)\$]{.arithmatex}。

四则运算：

::: {.arithmatex}
\$\$ \lim\limits\_{x \to a} \[f(x) \pm g(x)\] = \lim\limits\_{x \to a} f(x) \pm \lim\limits\_{x \to a} g(x) \$\$
:::

::: {.arithmatex}
\$\$ \lim\limits\_{x \to a} \[f(x)g(x)\] = \lim\limits\_{x \to a} f(x) \cdot \lim\limits\_{x \to a} g(x) \$\$
:::

::: {.arithmatex}
\$\$ \lim\limits\_{x \to a} \dfrac{f(x)}{g(x)} = \dfrac{\lim\limits\_{x \to a} f(x)}{\lim\limits\_{x \to a} g(x)} \$\$
:::

除法应当 [\$\lim\limits\_{x \to a} g(x) \ne 0\$]{.arithmatex} 时。

夹逼定理：设在 [\$x_0\$]{.arithmatex} 附近有 [\$g(x)\le f(x)\le h(x)\$]{.arithmatex}，且 [\$\lim\_{x\to x_0} g(x)=\lim\_{x\to x_0} h(x)=l\$]{.arithmatex}，则 [\$\lim\_{x\to x_0} f(x)=l\$]{.arithmatex}。

## 极限应用 {#_6}

### 无穷小​ {#_7}

若 [\$\lim\limits\_{x \to a} f(x) = 0\$]{.arithmatex}，称 [\$f(x)\$]{.arithmatex} 为 [\$x \to a\$]{.arithmatex} 时的无穷小。

根据上面的四则运算规则，可以得知：

- 若 [\$f(x)\$]{.arithmatex}，[\$g(x)\$]{.arithmatex} 都是 [\$x \to a\$]{.arithmatex} 时的无穷小，则 [\$f(x) \pm g(x)\$]{.arithmatex} 是 [\$x \to a\$]{.arithmatex} 时的无穷小。

- 若 [\$f(x)\$]{.arithmatex} 是 [\$x \to a\$]{.arithmatex} 时的无穷小，且 [\$\lim\limits\_{x \to a} g(x)\$]{.arithmatex} 存在，则 [\$f(x) \cdot g(x)\$]{.arithmatex} 是 [\$x \to a\$]{.arithmatex} 时的无穷小。

但两个无穷小的商不能确定：运算法则规定了分母不能为无穷小。

设 [\$f(x)\$]{.arithmatex}，[\$g(x)\$]{.arithmatex} 为 [\$x \to a\$]{.arithmatex} 时的两个无穷小，且 [\$g(x) \ne 0\$]{.arithmatex}，当 [\$\lim\limits\_{x \to a} \dfrac{f(x)}{g(x)}\$]{.arithmatex} 存在时，

- 若 [\$\lim\limits\_{x \to a} \dfrac{f(x)}{g(x)} = 0\$]{.arithmatex}，则称当 [\$x \to a\$]{.arithmatex} 时，[\$f(x)\$]{.arithmatex} 是 [\$g(x)\$]{.arithmatex} 的高阶无穷小。

- 若 [\$\lim\limits\_{x \to a} \dfrac{f(x)}{g(x)} = b \ne 0\$]{.arithmatex}，则称当 [\$x \to a\$]{.arithmatex} 时，[\$f(x)\$]{.arithmatex} 与 [\$g(x)\$]{.arithmatex} 是同阶无穷小。

特别地，当 [\$b = 1\$]{.arithmatex} 时，称当 [\$x \to a\$]{.arithmatex} 时，[\$f(x)\$]{.arithmatex} 与 [\$g(x)\$]{.arithmatex} 是等价无穷小，记作 [\$f(x) \sim g(x)\quad(x \to a)\$]{.arithmatex}。

等价无穷小替换公式：设 [\$f(x) \sim F(x) \quad (x \to a)\$]{.arithmatex}，[\$g(x) \sim G(x) \quad (x \to a)\$]{.arithmatex}，则

::: {.arithmatex}
\$\$ \begin{aligned} & \phantom = \lim\limits\_{x \to a} \dfrac{f(x)}{g(x)} \\ & = \lim\limits\_{x \to a} \[\dfrac{F(x)}{G(x)} \cdot \dfrac{f(x)}{F(x)} \cdot \dfrac{G(x)}{g(x)}\]\\ & = \lim\limits\_{x \to a} \dfrac{F(x)}{G(x)} \cdot \lim\limits\_{x \to a} \dfrac{f(x)}{F(x)} \cdot \lim\limits\_{x \to a} \dfrac{G(x)}{g(x)} \\ & = \lim\limits\_{x \to a} \dfrac{F(x)}{G(x)} \end{aligned} \$\$
:::

也即对一个分式求极限时，分子与分母可以替换为它的等价无穷小，而极限值不改变，这个规则称作等价无穷小替换规则。

一个最经典的等价无穷小是 [\$x \sim \sin x \quad (x \to 0)\$]{.arithmatex} 和它的推论 [\$x \sim \sin x \sim \cos x \sim \tan x \quad (x \to 0)\$]{.arithmatex}（证明从略）。

高中物理中一些公式的推导用到的，所谓「[\$x\$]{.arithmatex} 很小，将 [\$\sin x\$]{.arithmatex} 近似为 [\$x\$]{.arithmatex}」的原理，其实就是在做上面的等价无穷小替换。

### 连续性 {#_8}

我们曾用 [\$\varepsilon\$]{.arithmatex}－[\$\delta\$]{.arithmatex} 语言定义过连续性：设函数 [\$f\$]{.arithmatex} 在 [\$x_0\$]{.arithmatex} 附近有定义，如果对于任意的 [\$\varepsilon\>0\$]{.arithmatex}，都存在 [\$\delta\>0\$]{.arithmatex}，使得只要 [\$\|x-x_0\|\<\delta\$]{.arithmatex}，就有 [\$\|f(x)-f(x_0)\|\<\varepsilon\$]{.arithmatex}，那么称 [\$f\$]{.arithmatex} 在点 [\$x_0\$]{.arithmatex} 连续。

现在可以用极限写出更简洁的定义：设函数 [\$f\$]{.arithmatex} 在 [\$x_0\$]{.arithmatex} 附近有定义，如果 [\$\lim\_{x\to x_0} f(x)=f(x_0)\$]{.arithmatex}，那么称 [\$f\$]{.arithmatex} 在点 [\$x_0\$]{.arithmatex} 连续。

如果函数在某一点不连续，那么称在这一点间断。如果函数 [\$f\$]{.arithmatex} 在开区间 [\$I\$]{.arithmatex} 的每一点连续，那么称函数 [\$f\$]{.arithmatex} 是开区间 [\$I\$]{.arithmatex} 上的连续函数。

函数 [\$f\$]{.arithmatex} 在点 [\$x_0\$]{.arithmatex} 连续当且仅当

::: {.arithmatex}
\$\$ \lim\_{x\to x_0\^-}f(x)=\lim\_{x\to x_0\^+}f(x)=\lim\_{x\to x_0}f(x)=f(x_0) \$\$
:::

与左右极限对应的左右连续概念为：如果 [\$\lim\_{x\to x_0\^-}f(x)=f(x_0)\$]{.arithmatex}，称 [\$f\$]{.arithmatex} 在 [\$x_0\$]{.arithmatex} 左连续；如果 [\$\lim\_{x\to x_0\^+}f(x)=f(x_0)\$]{.arithmatex}，称 [\$f\$]{.arithmatex} 在 [\$x_0\$]{.arithmatex} 右连续。

对于闭区间 [\$I\$]{.arithmatex} 上的函数 [\$f\$]{.arithmatex}，如果 [\$f\$]{.arithmatex} 在区间内每一点都连续，且在左端点右连续、右端点左连续，那么称函数 [\$f\$]{.arithmatex} 是闭区间 [\$I\$]{.arithmatex} 上的连续函数。

### 间断点 {#_9}

我们再来考虑间断点。间断点有三种情况：

1.  函数在某一点存在极限，即左右极限相等，但与函数值不相等，或者函数在这一点没有定义，即

    ::: {.arithmatex}
    \$\$ \lim\_{x\to x_0\^-} f(x)=\lim\_{x\to x_0\^+} f(x)\ne f(x_0) \$\$
    :::

    这类间断点称为可去间断点。因为只要修改这一点，就能变为连续函数，例如

    ::: {.arithmatex}
    \$\$ g(x)= \begin{cases} f(x) & x\ne x_0 \\ \lim\_{x\to x_0} f(x) & x=x_0 \end{cases} \$\$
    :::

2.  函数在某一点的左右极限存在但不相等，即

    ::: {.arithmatex}
    \$\$ \lim\_{x\to x_0\^-} f(x)\ne \lim\_{x\to x_0\^+} f(x) \$\$
    :::

    这类间断点称为跳跃间断点。因为函数在 [\$x_0\$]{.arithmatex} 处发生了

    ::: {.arithmatex}
    \$\$ \left\|\lim\_{x\to x_0\^-} f(x)-\lim\_{x\to x_0\^+} f(x)\right\| \$\$
    :::

    的跳跃。可去间断点和跳跃间断点统称为第一类间断点。

3.  函数在某一点的左右极限至少有一个不存在。这类间断点称为第二类间断点。例如，对于狄利克雷函数

    ::: {.arithmatex}
    \$\$ D(x)= \begin{cases} 1 & x\in \mathbb{Q} \\ 0 & x\in \mathbb{R}-\mathbb{Q} \end{cases} \$\$
    :::

    任意的 [\$x_0\in \mathbb{R}\$]{.arithmatex} 都是其第二类间断点。

连续函数的四则运算和复合函数具有连续性。设函数 [\$f(x)\$]{.arithmatex}、[\$g(x)\$]{.arithmatex} 在 [\$x_0\$]{.arithmatex} 连续，则 [\$f(x)\pm g(x)\$]{.arithmatex}、[\$f(x)g(x)\$]{.arithmatex}、[\$\dfrac{f(x)}{g(x)}\$]{.arithmatex}（[\$g(x)\ne 0\$]{.arithmatex}）也在 [\$x_0\$]{.arithmatex} 连续。

设函数 [\$u=g(x)\$]{.arithmatex} 在区间 [\$I\$]{.arithmatex} 有定义，[\$y=f(u)\$]{.arithmatex} 在区间 [\$J\$]{.arithmatex} 有定义，且 [\$g(I)\subset J\$]{.arithmatex}。若 [\$g\$]{.arithmatex} 在 [\$x_0\in I\$]{.arithmatex} 处连续，[\$f\$]{.arithmatex} 在 [\$u_0=g(x_0)\$]{.arithmatex} 处连续，则复合函数 [\$f\circ g\$]{.arithmatex} 在 [\$x_0\$]{.arithmatex} 处连续，即

::: {.arithmatex}
\$\$ \lim\_{x\to x_0} f\big(g(x)\big) = f\left(\lim\_{x\to x_0} g(x)\right) = f\big(g(x_0)\big) \$\$
:::

此外，连续函数的反函数同样是连续函数。

连续函数还具有局部保号性：设函数 [\$f\$]{.arithmatex} 在 [\$x_0\$]{.arithmatex} 处连续，且 [\$f(x_0)\ne 0\$]{.arithmatex}，则存在 [\$\delta\>0\$]{.arithmatex}，使得只要 [\$0\<\|x-x_0\|\<\delta\$]{.arithmatex}，就有 [\$f(x)f(x_0)\>0\$]{.arithmatex}。

可以证明，所有初等函数在定义域上都处处连续。
