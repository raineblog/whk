# 根式

注：下文只讨论自然数 $\mathbb N$ 中的。

## 公式

$$
\sqrt{a\pm\sqrt{b}}=\sqrt{a+\sqrt{a^2-b}\over2}\pm\sqrt{a-\sqrt{a^2-b}\over2}
$$

注：只有 $a^2-b$ 是完全平方数的时候，才能开出来。

## 例题

化简 $\sqrt{4+\sqrt9}$。

解：

$$
\begin{aligned}
&\sqrt{4+\sqrt9}\\
=\;&\sqrt{4+\sqrt7\over2}+\sqrt{4-\sqrt7\over2}\\
=\;&{1\over\sqrt2}(\sqrt{4+\sqrt7}+\sqrt{4
-\sqrt7})\\
=\;&{1\over\sqrt2}(\sqrt{7\over2}+\sqrt{7\over2}+\sqrt{7\over2}-\sqrt{7\over2})\\
=\;&{2\over\sqrt2}\sqrt{7\over2}=\sqrt7
\end{aligned}
$$

有人问，为什么不直接把 $\sqrt9$ 化成 $3$，因为我想多演示一遍，但是懒得再出一道题。

## 推导

我们设 $\sqrt{a+\sqrt{b}}$ 化简完的结果是 $\sqrt x+\sqrt y$：

$$
\begin{aligned}
\sqrt{a+\sqrt{b}}&=\sqrt x+\sqrt y\\
a+\sqrt{b}&=x+y+2\sqrt{xy}
\end{aligned}
$$

因为 $a$ 外面没有根号，与 $x+y$ 相对应：

$$
\left\{\begin{aligned}
a&=x+y\\
\sqrt{b}&=2\sqrt{xy}
\end{aligned}\right.
$$

然后我们把下面的式子平方，可以写出方程组：

$$
\left\{\begin{aligned}
x+y&=a\\
xy&={b\over4}
\end{aligned}\right.
$$

然后用公式：

$$
\left\{\begin{aligned}
x+y&=a\\
x-y&=\sqrt{(x+y)^2-4xy}\\
&=\sqrt{a^2-b}
\end{aligned}\right.
$$

---

PS：此时有一个初中不学（我们没学）的方法，

设 $t$ 满足：

$$
\begin{aligned}
(t-x)(t-y)&=0\\
t^2-(x+y)t+xy&=0
\end{aligned}
$$

解这个方程，得到的 $t$ 的两个根分别就是 $x$ 和 $y$。

具体的：

$$
\begin{aligned}
t^2-at+{b\over4}=0\\
t={a\pm\sqrt{a^2-b}\over2}
\end{aligned}
$$

---

解得：

$$
\left\{\begin{aligned}
x&={a+\sqrt{a^2-b}\over2}\\
y&={a-\sqrt{a^2-b}\over2}
\end{aligned}\right.
$$

因此：

$$
\begin{aligned}
&\sqrt{a+\sqrt{b}}=\sqrt x+\sqrt y\\
=\;&\sqrt{a+\sqrt{a^2-b}\over2}+\sqrt{a-\sqrt{a^2-b}\over2}
\end{aligned}
$$

减法同理。