# 线性规划 {#_1}

![alt text](../image-24.avif)

## 例题 1 {#1}

::: {.arithmatex}
\$\$\begin{cases}5x-11y \geq -22 \\ 2x+3y \geq 9 \\ 2x \leq 11\end{cases}\$\$
:::

\$z = 10x + 10y, \max{z} = \$ ？

### 基本概念 {#_2}

1.  约束条件：变量 [\$x,y,\dots\$]{.arithmatex} 满足的一组条件，上述二元一次不等式组就是对 [\$x,y\$]{.arithmatex} 的约束条件。
2.  线性约束条件：由变量 [\$x,y,\dots\$]{.arithmatex} 的一次不等式 / 方程组成的不等式组就称为线性约束条件，如上述二元一次不等式。
3.  目标函数：欲求最大值或最小值所涉及的变量 [\$x,y,\dots\$]{.arithmatex} 的解析式，如上述 [\$z\$]{.arithmatex}.
4.  线性目标函数：目标函数关于变量 [\$x,y,\dots\$]{.arithmatex} 的一次解析式，如上述 [\$z\$]{.arithmatex}.
5.  线性规划问题：在线性约束条件下求线性目标函数的问题。
6.  可行解：满足线性约束条件的解 [\$(x,y)\$]{.arithmatex}.
7.  可行域：由所有可行解组成的集合。
8.  最优解：使目标函数取得 [\$\max\$]{.arithmatex} 或 [\$\min\$]{.arithmatex} 的可行解。

### 解法 {#_3}

1.  画图，数形结合。

\$[\$\begin{cases}5x-11y \geq -22 & \displaystyle \implies y \leq \frac{5}{11}x + \frac{1}{2} & \implies & \displaystyle y = \frac{5}{11}x + \frac{1}{2}\\ 图像的下边 \\ 2x+3y \geq 9 & \displaystyle \implies y \geq -\frac{2}{3}x + 3 & \implies & \displaystyle y = -\frac{2}{3}x + 3\\ 图像的上边 \\ 2x \leq 11 & \displaystyle \implies x \leq \frac{11}{2} & \implies & \displaystyle x=\frac{11}{2}\\ 图像的左边 \end{cases}\$]{.arithmatex}\$

在平面直角坐标系上画出对应的平面区域（可行域），再把目标函数 [\$z=ax+by\$]{.arithmatex} 变形为 [\$\displaystyle y=-\frac{a}{b}x + \frac{z}{b}\$]{.arithmatex}，[\$\\\$]{.arithmatex} 所以求 [\$z\$]{.arithmatex} 的最值可看成是求直线 [\$\displaystyle y=-\frac{a}{b}x + \frac{z}{b}\$]{.arithmatex} 在 [\$y\$]{.arithmatex} 轴上截距的最值。以这题为例，[\$\displaystyle z=10x+10y \implies y= -x + \frac{z}{10}\$]{.arithmatex} 容易证明，当 [\$z=85\$]{.arithmatex} 时 [\$y\$]{.arithmatex} 轴上截距取最值，所以 [\$\max{z}=85.\$]{.arithmatex}

![](https://cdn.luogu.com.cn/upload/image_hosting/4tjm317j.png)

1.  仔细观察，可以发现最优解非常容易出现在可行域构成的**多面体的顶点**处。

### 例题 2 {#2}

::: {.arithmatex}
\$\$\begin{cases}y \geq x \\ x + y \leq 2 \\ x \geq a\end{cases}\$\$
:::

\$(2x+y)*{\mathrm{max}}=4(2x+y)*, a= \$ ?}

- 求 [\$(2x+y)\_{\mathrm{min}}\$]{.arithmatex}：[\$x\_{\min}=a \implies y\_{\min}=a \implies (2x+y)\_{\mathrm{min}}=3a\$]{.arithmatex}

- 求 [\$(2x+y)\_{\mathrm{max}}\$]{.arithmatex}：[\$\begin{cases}x-y\leq 0 \\ x+y\leq 2\end{cases}\xRightarrow{\mathrm{Add\\ }} x\leq 1\implies y\leq 1\implies (2x+y)\_{\mathrm{max}}=3\$]{.arithmatex}

- [\$\displaystyle 3=4\times 3a\implies a=\frac{1}{4}\$]{.arithmatex}

### 例题 3（2024 九省联考 T14） {#32024-t14}

::: {.arithmatex}
\$\$\begin{cases} 0\<a\<b\<c\<1 \\ b\geq 2a \\ \\ \\ \mathrm{or}\\ \\ \\ a+b\leq 1 \end{cases}\$\$
:::

[\$\max{\set{b-a,c-b,1-c}}\$]{.arithmatex} 的最小值 [\$=\$]{.arithmatex} ？

- 注意到 [\$c\$]{.arithmatex} 的约束条件是最少的，首先考虑消去它，得到

::: {.arithmatex}
\$\$\max{\set{b-a,c-b,1-c}}\geq\max{\set{b-a,\frac{1-b}{2}}}\$\$
:::

[\$\\ \\ \\ \\ \\ \\ \text{}\$]{.arithmatex} 当且仅当 [\$\displaystyle c=\frac{1+b}{2}\$]{.arithmatex} 取等，消去 [\$c\$]{.arithmatex} 后把 [\$a\$]{.arithmatex} 看作 [\$x\$]{.arithmatex}，把 [\$b\$]{.arithmatex} 看作 [\$y\$]{.arithmatex} 得：

::: {.arithmatex}
\$\$\begin{cases}0\<x \\ x\<y \\ y\<1 \\ y\geq 2x\\ \\ \\ \mathrm{or}\\ \\ \\ x+y\leq 1\end{cases}\$\$
:::

- 作出可行域：[\$\mathrm{and}\$]{.arithmatex} 连接的区域之间取交，[\$\mathrm{or}\$]{.arithmatex} 连接的区域之间取并。阴影部分即为可行域。

[\$\\ \\ \\ \\ \\ \\ \text{}\$]{.arithmatex} 图中 [\$y\geq 2x\\ \\ \\ x+y\leq 1\$]{.arithmatex} 两条解析式用红色标出。

![](https://cdn.luogu.com.cn/upload/image_hosting/0uvhhx28.png)

- 回到题目，要求 [\$\displaystyle M=\max{\set{y-x,\frac{1-y}{2}}}\$]{.arithmatex}，我们需要知道何时 [\$M=y-x\$]{.arithmatex}，何时 [\$\displaystyle M=\frac{1-y}{2}\$]{.arithmatex}.

[\$\\ \\ \\ \\ \\ \\ \text{}\$]{.arithmatex} 直接列方程 [\$\displaystyle y-x=\frac{1-y}{2}\$]{.arithmatex} 可以得到 [\$\displaystyle y=\frac{2}{3}x+\frac{1}{3}\$]{.arithmatex}，在图中作出这条直线，得到：

![](https://cdn.luogu.com.cn/upload/image_hosting/0hyhebem.png)

- 因为最终要求的是 [\$M\$]{.arithmatex} 的最小值，所以对蓝色区域而言，[\$y\$]{.arithmatex} 尽量小，[\$x\$]{.arithmatex} 尽量大，根据例题 1 的经验，这样的极值点通常出现在多边形的顶点处，经过比较后 [\$P\$]{.arithmatex} 点是极值点，此时 [\$M=0.2\$]{.arithmatex}. 对绿色区域而言，只需满足 [\$y\$]{.arithmatex} 尽量大，显然，[\$P\$]{.arithmatex} 点也是极值点。
- 综上所述，[\$\max{\set{b-a,c-b,1-c}}\$]{.arithmatex} 的最小值 [\$\displaystyle=\frac{1}{5}\$]{.arithmatex}.

<https://oi-wiki.org/math/linear-programming/#%E5%BC%95%E5%85%A5>
