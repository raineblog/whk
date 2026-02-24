# 线性规划 {#_1}

![alt text](../image-24.avif)

## 例题 1 {#1}

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases}5x-11y \geq -22 \\ 2x+3y \geq 9 \\ 2x \leq 11\end{cases}
:::

$$\begin{cases}5x-11y \geq -22 \\ 2x+3y \geq 9 \\ 2x \leq 11\end{cases}$$
::::

\$z = 10x + 10y, \max{z} = \$ ？

### 基本概念 {#_2}

1.  约束条件：变量 []{.arithmatex}$x,y,\dots$ 满足的一组条件，上述二元一次不等式组就是对 []{.arithmatex}$x,y$ 的约束条件。
2.  线性约束条件：由变量 []{.arithmatex}$x,y,\dots$ 的一次不等式 / 方程组成的不等式组就称为线性约束条件，如上述二元一次不等式。
3.  目标函数：欲求最大值或最小值所涉及的变量 []{.arithmatex}$x,y,\dots$ 的解析式，如上述 []{.arithmatex}$z$.
4.  线性目标函数：目标函数关于变量 []{.arithmatex}$x,y,\dots$ 的一次解析式，如上述 []{.arithmatex}$z$.
5.  线性规划问题：在线性约束条件下求线性目标函数的问题。
6.  可行解：满足线性约束条件的解 []{.arithmatex}$(x,y)$.
7.  可行域：由所有可行解组成的集合。
8.  最优解：使目标函数取得 []{.arithmatex}$\max$ 或 []{.arithmatex}$\min$ 的可行解。

### 解法 {#_3}

1.  画图，数形结合。

\$[]{.arithmatex}$\begin{cases}5x-11y \geq -22 & \displaystyle \implies y \leq \frac{5}{11}x + \frac{1}{2} & \implies & \displaystyle y = \frac{5}{11}x + \frac{1}{2}\ 图像的下边 \\ 2x+3y \geq 9 & \displaystyle \implies y \geq -\frac{2}{3}x + 3 & \implies & \displaystyle y = -\frac{2}{3}x + 3\ 图像的上边 \\ 2x \leq 11 & \displaystyle \implies x \leq \frac{11}{2} & \implies & \displaystyle x=\frac{11}{2}\ 图像的左边 \end{cases}$\$

在平面直角坐标系上画出对应的平面区域（可行域），再把目标函数 []{.arithmatex}$z=ax+by$ 变形为 []{.arithmatex}$\displaystyle y=-\frac{a}{b}x + \frac{z}{b}$，[]{.arithmatex}$\\$ 所以求 []{.arithmatex}$z$ 的最值可看成是求直线 []{.arithmatex}$\displaystyle y=-\frac{a}{b}x + \frac{z}{b}$ 在 []{.arithmatex}$y$ 轴上截距的最值。以这题为例，[]{.arithmatex}$\displaystyle z=10x+10y \implies y= -x + \frac{z}{10}$ 容易证明，当 []{.arithmatex}$z=85$ 时 []{.arithmatex}$y$ 轴上截距取最值，所以 []{.arithmatex}$\max{z}=85.$

![](https://cdn.luogu.com.cn/upload/image_hosting/4tjm317j.png)

1.  仔细观察，可以发现最优解非常容易出现在可行域构成的**多面体的顶点**处。

### 例题 2 {#2}

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases}y \geq x \\ x + y \leq 2 \\ x \geq a\end{cases}
:::

$$\begin{cases}y \geq x \\ x + y \leq 2 \\ x \geq a\end{cases}$$
::::

\$(2x+y)*{\mathrm{max}}=4(2x+y)*, a= \$ ?}

- 求 []{.arithmatex}$(2x+y)_{\mathrm{min}}$：[]{.arithmatex}$x_{\min}=a \implies y_{\min}=a \implies (2x+y)_{\mathrm{min}}=3a$

- 求 []{.arithmatex}$(2x+y)_{\mathrm{max}}$：[]{.arithmatex}$\begin{cases}x-y\leq 0 \\ x+y\leq 2\end{cases}\xRightarrow{\mathrm{Add\ }} x\leq 1\implies y\leq 1\implies (2x+y)_{\mathrm{max}}=3$

- []{.arithmatex}$\displaystyle 3=4\times 3a\implies a=\frac{1}{4}$

### 例题 3（2024 九省联考 T14） {#32024-t14}

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} 0\<a\<b\<c\<1 \\ b\geq 2a \\ \\ \\ \mathrm{or}\\ \\ \\ a+b\leq 1 \end{cases}
:::

$$\begin{cases} 0<a<b<c<1 \\ b\geq 2a \ \ \ \mathrm{or}\ \ \ a+b\leq 1 \end{cases}$$
::::

[]{.arithmatex}$\max{\set{b-a,c-b,1-c}}$ 的最小值 []{.arithmatex}$=$ ？

- 注意到 []{.arithmatex}$c$ 的约束条件是最少的，首先考虑消去它，得到

:::: {.arithmatex}
::: {.MathJax_Preview}
\max{\set{b-a,c-b,1-c}}\geq\max{\set{b-a,\frac{1-b}{2}}}
:::

$$\max{\set{b-a,c-b,1-c}}\geq\max{\set{b-a,\frac{1-b}{2}}}$$
::::

[]{.arithmatex}$\ \ \ \ \ \ \text{}$ 当且仅当 []{.arithmatex}$\displaystyle c=\frac{1+b}{2}$ 取等，消去 []{.arithmatex}$c$ 后把 []{.arithmatex}$a$ 看作 []{.arithmatex}$x$，把 []{.arithmatex}$b$ 看作 []{.arithmatex}$y$ 得：

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases}0\<x \\ x\<y \\ y\<1 \\ y\geq 2x\\ \\ \\ \mathrm{or}\\ \\ \\ x+y\leq 1\end{cases}
:::

$$\begin{cases}0<x \\ x<y \\ y<1 \\ y\geq 2x\ \ \ \mathrm{or}\ \ \ x+y\leq 1\end{cases}$$
::::

- 作出可行域：[]{.arithmatex}$\mathrm{and}$ 连接的区域之间取交，[]{.arithmatex}$\mathrm{or}$ 连接的区域之间取并。阴影部分即为可行域。

[]{.arithmatex}$\ \ \ \ \ \ \text{}$ 图中 []{.arithmatex}$y\geq 2x\ \ \  x+y\leq 1$ 两条解析式用红色标出。

![](https://cdn.luogu.com.cn/upload/image_hosting/0uvhhx28.png)

- 回到题目，要求 []{.arithmatex}$\displaystyle M=\max{\set{y-x,\frac{1-y}{2}}}$，我们需要知道何时 []{.arithmatex}$M=y-x$，何时 []{.arithmatex}$\displaystyle M=\frac{1-y}{2}$.

[]{.arithmatex}$\ \ \ \ \ \ \text{}$ 直接列方程 []{.arithmatex}$\displaystyle y-x=\frac{1-y}{2}$ 可以得到 []{.arithmatex}$\displaystyle y=\frac{2}{3}x+\frac{1}{3}$，在图中作出这条直线，得到：

![](https://cdn.luogu.com.cn/upload/image_hosting/0hyhebem.png)

- 因为最终要求的是 []{.arithmatex}$M$ 的最小值，所以对蓝色区域而言，[]{.arithmatex}$y$ 尽量小，[]{.arithmatex}$x$ 尽量大，根据例题 1 的经验，这样的极值点通常出现在多边形的顶点处，经过比较后 []{.arithmatex}$P$ 点是极值点，此时 []{.arithmatex}$M=0.2$. 对绿色区域而言，只需满足 []{.arithmatex}$y$ 尽量大，显然，[]{.arithmatex}$P$ 点也是极值点。
- 综上所述，[]{.arithmatex}$\max{\set{b-a,c-b,1-c}}$ 的最小值 []{.arithmatex}$\displaystyle=\frac{1}{5}$.

<https://oi-wiki.org/math/linear-programming/#%E5%BC%95%E5%85%A5>
