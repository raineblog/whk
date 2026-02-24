# 多项式科技 \{#\_1}

## 生成函数 \{#\_2}

序列 $a$ （有穷无穷均可）的普通生成函数定义为形式幂级数：$displaystyle F(x)=\sum\_na\_nx^n$。例如：

1. $a=\lang1,2,3\rang$ 的普通生成函数是 $1+2x+3x^2$
2. $a=\lang1,1,1,\dots\rang$ 的普通生成函数是 $displaystyle\sum\_\{n\geq 0}x^n$
3. $a=\lang1,2,4,8,16,\dots\rang$ 的生成函数是 $displaystyle\sum\_\{n\geq 0}2^nx^n$
4. $a=\lang1,3,5,7,9\rang$ 的生成函数是 $displaystyle\sum\_\{n\geq 0}(2n+1)x^n$

换句话说，如果序列 $a$ 有通项公式，那么它的普通生成函数的系数就是通项公式。

### 基本运算 \{#\_3}

两个序列 $a,b$ 的生成函数 $F(x),G(x$，则 $F(x)\pm G(x$ 是序列 $lang a\_n\pm b\_n\rang$ 的生成函数。

$$
F(x)\pm G(x)=\sum\_\{n}(a\_n\pm b\_n)x^n
$$

乘法运算即卷积，推出 $F(x)G(x$ 是序列 $left\lang\displaystyle\sum\_\{i=0}^na\_ib\_\{n-i}\right\rang$ 的生成函数。

$$
F(x)G(x)=\sum\_nx^n\sum\_\{i=0}^na\_ib\_\{n-i}
$$

#### 形式幂级数形式 $to$ 封闭形式 \{#to}

例如 $a=\lang1,1,1,\dots\rang$ 的普通生成函数是 $displaystyle F(x)=\sum\_\{n\geq 0}x^n$，可以发现 $F(x)x+1=F(x$，于是解方程得到 $displaystyle F(x)=\frac\{1}\{1-x}$，这就是 $displaystyle\sum\_\{n\geq 0}x^n$ 的封闭形式。

又例如等比数列 $lang1,p,p^2,\dots\rang$ 的生成函数 $F(x)=\displaystyle\sum\_\{n\geq 0}p^nx^n$，有 $F(x)px+1=F(x$ 得 $F(x)=\displaystyle\frac\{1}\{1-px}$.

$a=\lang 1,0,1,0,1,\dots\rang$ 的 $F(x)=\displaystyle\sum\_\{n\geq 0}x^\{2n}=\frac\{1}\{1-x^2}$

$a=\lang 1,2,3,4,\dots\rang$ 的 $F(x)=\displaystyle\sum\_\{n\geq 0}(n+1)x^n=\sum\_\{n\geq 0}(x^n)'=\left(\frac\{1}\{1-x}\right)'=\frac\{1}\{(1-x)^2}$

$a\_n=\begin\{pmatrix}m\n\end\{pmatrix}$ 的 $F(x)=\displaystyle\sum\_\{n\geq 0}\begin\{pmatrix}m\n\end\{pmatrix}x^n=(1+x)^m$

$Fib$ 数列定义为 $a\_0=0,a\_1=1,a\_n=a\_\{n-1}+a\_\{n-2}$，于是有

$$
F(x)=xF(x)+x^2F(x)-a\_0x+a\_1x+a\_0\implies F(x)=\frac\{x}\{1-x-x^2}
$$

#### 应用 \{#\_4}

1. 在许多不同种类的食物中选出 $n$ 个，计算方案数。每种食物的限制如下：

|    汉堡：偶数个   | 可乐：不超高一个 |   鸡腿：不超过两个  |   蜜桃多：奇数个   |
| :---------: | :------: | :---------: | :---------: |
| 鸡块：$4$ 的倍数个 | 包子：不超过三个 | 土豆片炒肉：不超过一个 | 面包：$3$ 的倍数个 |

构造生成函数：

| $displaystyle\sum\_\{n\geq 0}x^\{2n}=\frac\{1}\{1-x^2}$ |                      $1+x$                     | $displaystyle 1+x+x^2=\frac\{1-x^3}\{1-x}$ | $displaystyle\frac\{x}\{1-x^2}$ |
| :-----------------------------------------------------: | :--------------------------------------------: | :----------------------------------------: | :-----------------------------: |
| $displaystyle\sum\_\{n\geq 0}x^\{4n}=\frac\{1}\{1-x^4}$ | $displaystyle 1+x+x^2+x^3=\frac\{1-x^4}\{1-x}$ |                    $1+x$                   | $displaystyle\frac\{1}\{1-x^3}$ |

全部乘起来得到答案的生成函数：

$$
F(x)=\frac\{(1+x)(1-x^3)x(1-x^4)(1+x)}\{(1-x^2)(1-x)(1-x^2)(1-x^4)(1-x)(1-x^3)}=\frac\{x}\{(1-x)^4}=\sum\_\{n\geq 1}\begin\{pmatrix}n+2\n-1\end\{pmatrix}x^n
$$

于是答案 $=\begin\{pmatrix}n+2\n-1\end\{pmatrix}=\begin\{pmatrix}n+2\3\end\{pmatrix}$

1. $a\_\{n+1}+a\_n=2^n,a\_0=0$，求通项。

$f(x)=\displaystyle\sum\_\{n=0}^\{+\infty}a\_nx^n$，原式变为 $x^\{-1}(a\_\{n+1}x^\{n+1})+a\_nx^n=(2x)^n$，再求和有

$$
\displaystyle\sum\_\{n=0}^\{+\infty}x^\{-1}(a\_\{n+1}x^\{n+1})+\sum\_\{n=0}^\{+\infty}(a\_nx^n)=\sum\_\{n=0}^\{+\infty}(2x)^n=\frac\{1}\{1-2x}\implies (\frac\{1}\{x}+1)f(x)=\frac\{1}\{1-2x}
$$

$$
f(x)=\frac\{x}\{(1-2x)(1+x)}=\frac\{1}\{3}(\frac\{1}\{1-2x}-\frac\{1}\{1+x})=\frac\{1}\{3}\sum\_\{n=0}^\{+\infty}\[2^n-(-1)^n]x^n
$$

于是 $displaystyle a\_n=\frac\{1}\{3}\[2^n-(-1)^n$.

1. 卡特兰数：一个 $n\times n$ 的方阵从 $0,0$ 走到 $n,n$，不经过对角线的方案数，记作 $C\_n$。

有如下关系：$C\_n=\displaystyle\sum\_\{k=0}^nC\_\{n-k}C\_k$，构造 $f(x)=\displaystyle\sum\_\{n=0}^\{+\infty}C\_nx^n$，有

$$
f^2(x)=C\_0^2+(C\_0C\_1+C\_1C\_0)x+\dots\implies xf^2(x)+C\_0=f(x)\implies f(x)=\frac\{1-\sqrt\{1-4x} }\{2x}
$$

$$
\implies f(x)=\frac\{1-\left\{1+\displaystyle\sum\_\{k=1}^\{+\infty}\left\[-2\begin\{pmatrix}2k-2\ k-1\end\{pmatrix}\right]x^k\right}}\{2x}=\sum\_\{k=0}^\{+\infty}\frac\{\begin\{pmatrix}2k\k\end\{pmatrix}x^k}\{k+1}\implies\red\{\boxed\{C\_n=\frac\{\begin\{pmatrix}2n\n\end\{pmatrix}}\{n+1}}}
$$
