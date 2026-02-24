# 三角函数例题 {#_1}

## 例题一 {#_2}

:::: {.arithmatex}
::: {.MathJax_Preview}
2\cos\^2{B\over2}+\sqrt3\sin B=3
:::

$$2\cos^2{B\over2}+\sqrt3\sin B=3$$
::::

- 求 []{.arithmatex}$B$.

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos B=2\cos\^2{B\over2}-1\\ \cos B+\sqrt3\sin B=2\\ {\sqrt3\over2}\sin B+{1\over2}\cos B=1\\ \sin B\cos30\^\circ+\cos B\sin30\^\circ=1\\ \sin(B+30\^\circ)=1=\sin90\^\circ\\ B=60\^\circ
:::

$$\cos B=2\cos^2{B\over2}-1\\
\cos B+\sqrt3\sin B=2\\
{\sqrt3\over2}\sin B+{1\over2}\cos B=1\\
\sin B\cos30^\circ+\cos B\sin30^\circ=1\\
\sin(B+30^\circ)=1=\sin90^\circ\\
B=60^\circ$$
::::

## 例题二 {#_3}

:::: {.arithmatex}
::: {.MathJax_Preview}
(\sin B-\sin C)\^2=\sin\^2 A-\sin B\sin C
:::

$$(\sin B-\sin C)^2=\sin^2 A-\sin B\sin C$$
::::

- 求 []{.arithmatex}$A$.
- 若 []{.arithmatex}$\sqrt2a + b= 2c$，求 []{.arithmatex}$C$.

观察到是角的二次齐次式，且都是正弦，考虑正弦定理，

:::: {.arithmatex}
::: {.MathJax_Preview}
(\sin B-\sin C)\^2=\sin\^2 A-\sin B\sin C\\\\ (b-c)\^2=a\^2-bc\\\\ b\^2+c\^2-2bc=a\^2-bc\\\\ a\^2=b\^2+c\^2-bc
:::

$$(\sin B-\sin C)^2=\sin^2 A-\sin B\sin C\\\\
(b-c)^2=a^2-bc\\\\
b^2+c^2-2bc=a^2-bc\\\\
a^2=b^2+c^2-bc$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos A={b\^2+c\^2-a\^2\over2bc}={1\over2}\\\\ A=60\^\circ
:::

$$\cos A={b^2+c^2-a^2\over2bc}={1\over2}\\\\
A=60^\circ$$
::::

观察到 []{.arithmatex}$\sqrt2a + b= 2c$ 为边的一次齐次，考虑用正弦定理。

:::: {.arithmatex}
::: {.MathJax_Preview}
\sqrt2a+b=2c\\\\ \sqrt2\sin A+\sin B=2\sin C
:::

$$\sqrt2a+b=2c\\\\
\sqrt2\sin A+\sin B=2\sin C$$
::::

根据上一问，[]{.arithmatex}$\sin A=\sin60^\circ=\sqrt3/2$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sqrt6/2+\sin B=2\sin C\\\\ \sqrt6/2+\sin(120-C)=2\sin C\\\\ \sqrt6/2+\sqrt3/2\cos C+\sin C/2=2\sin C
:::

$$\sqrt6/2+\sin B=2\sin C\\\\
\sqrt6/2+\sin(120-C)=2\sin C\\\\
\sqrt6/2+\sqrt3/2\cos C+\sin C/2=2\sin C$$
::::

继续整理，

:::: {.arithmatex}
::: {.MathJax_Preview}
{\sqrt6\over2}+{\sqrt3\over2}\cos C+{1\over2}\sin C=2\sin C\\\\ {3\over2}\sin C-{\sqrt3\over2}\cos C={\sqrt6\over2}\\\\ {\sqrt3\over2}\sin C-{1\over2}\cos C={\sqrt2\over2}\\\\ \sin C\cos30\^\circ-\cos C\sin30\^\circ={\sqrt2\over2}\\\\ \sin(C-30\^\circ)={\sqrt2\over2}=\sin45\^\circ
:::

$${\sqrt6\over2}+{\sqrt3\over2}\cos C+{1\over2}\sin C=2\sin C\\\\
{3\over2}\sin C-{\sqrt3\over2}\cos C={\sqrt6\over2}\\\\
{\sqrt3\over2}\sin C-{1\over2}\cos C={\sqrt2\over2}\\\\
\sin C\cos30^\circ-\cos C\sin30^\circ={\sqrt2\over2}\\\\
\sin(C-30^\circ)={\sqrt2\over2}=\sin45^\circ$$
::::

因为 []{.arithmatex}$C \in (0^\circ,120 ^\circ)$，[]{.arithmatex}$C-30^\circ\in(-30^\circ,90^\circ)$，因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
C-30\^\circ=45\^\circ,\\ C=75\^\circ
:::

$$C-30^\circ=45^\circ,\ C=75^\circ$$
::::

## 例题三 {#_4}

在锐角 []{.arithmatex}$\triangle ABC$ 中，

:::: {.arithmatex}
::: {.MathJax_Preview}
2b\sin A-\sqrt3a=0
:::

$$2b\sin A-\sqrt3a=0$$
::::

- 求 []{.arithmatex}$B$.
- 求 []{.arithmatex}$\cos A+\cos B+\cos C$ 的取值范围。

不考虑 []{.arithmatex}$\sin A$ 是边的二次齐次式，于是应用正弦定理，

:::: {.arithmatex}
::: {.MathJax_Preview}
2\sin B\sin A-\sqrt2\sin A=0\\\\ 2\sin B=\sqrt3\\ \sin B=\sqrt3/2
:::

$$2\sin B\sin A-\sqrt2\sin A=0\\\\
2\sin B=\sqrt3\\
\sin B=\sqrt3/2$$
::::

因为 []{.arithmatex}$\angle B$ 是锐角，

:::: {.arithmatex}
::: {.MathJax_Preview}
B=60\^\circ
:::

$$B=60^\circ$$
::::

设，

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\degree{\^\circ} \begin{aligned} S&=\cos A+\cos B+\cos C\\ &=\cos A+\cos C+1/2\\ &=\cos(120\degree-C)+\cos C+1/2\\ &=-{1\over2}\cos C+{\sqrt3\over2}\sin C+\cos C+{1\over2}\\ &={\sqrt3\over2}\sin C+{1\over2}\cos C+{1\over2}\\ &=\sin C\cos30\degree+\cos C\sin30\degree +1/2\\ &=\sin(C+30\degree)+1/2 \end{aligned}
:::

$$\def\degree{^\circ}
\begin{aligned}
S&=\cos A+\cos B+\cos C\\
&=\cos A+\cos C+1/2\\
&=\cos(120\degree-C)+\cos C+1/2\\
&=-{1\over2}\cos C+{\sqrt3\over2}\sin C+\cos C+{1\over2}\\
&={\sqrt3\over2}\sin C+{1\over2}\cos C+{1\over2}\\
&=\sin C\cos30\degree+\cos C\sin30\degree
+1/2\\
&=\sin(C+30\degree)+1/2
\end{aligned}$$
::::

因为 []{.arithmatex}$0^\circ<A,B,C<90^\circ$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\def\degree{\^\circ} \begin{cases} 0\degree\<&C&\<90\degree\\ 0\degree\<&B&\<90\degree \end{cases} \Longleftrightarrow \begin{cases} 0\degree\<&C&\<90\degree\\ 0\degree\<&120-C&\<90\degree \end{cases}
:::

$$\def\degree{^\circ}
\begin{cases}
0\degree<&C&<90\degree\\
0\degree<&B&<90\degree
\end{cases}
\Longleftrightarrow
\begin{cases}
0\degree<&C&<90\degree\\
0\degree<&120-C&<90\degree
\end{cases}$$
::::

即，[]{.arithmatex}$30^\circ<C<90^\circ$，[]{.arithmatex}$60^\circ<C+30^\circ<120^\circ$。

画出单位圆，易得 []{.arithmatex}$\sin(C+30\degree)\in(\sqrt3/2,1]$，即，

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos A+\cos B+\cos C\in\left({\sqrt3+1\over2},{3\over2}\right\]
:::

$$\cos A+\cos B+\cos C\in\left({\sqrt3+1\over2},{3\over2}\right]$$
::::

## 例题四 {#_5}

在 []{.arithmatex}$\triangle ABC$ 中，[]{.arithmatex}$a+b=11$，

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos A={1\over8},\\\cos B={9\over16}
:::

$$\cos A={1\over8},\,\cos B={9\over16}$$
::::

- 求 []{.arithmatex}$a,b$。

考虑余弦转正弦，因为是三角形的角，因此正弦值非负，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sin A=\sqrt{1-\cos\^2 A}=\sqrt{63\over64}={3\sqrt7\over8}\\ \sin B=\sqrt{1-\cos\^2 B}=\sqrt{175\over256}={5\sqrt7\over16}
:::

$$\sin A=\sqrt{1-\cos^2 A}=\sqrt{63\over64}={3\sqrt7\over8}\\
\sin B=\sqrt{1-\cos^2 B}=\sqrt{175\over256}={5\sqrt7\over16}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
{a\over b}={\sin A\over\sin B}={6\over5}
:::

$${a\over b}={\sin A\over\sin B}={6\over5}$$
::::

因此 []{.arithmatex}$a=6,\,b=5$。

## 例题五 {#_6}

:::: {.arithmatex}
::: {.MathJax_Preview}
{\sin A\over\sin B-\sin C}={b+c\over b-a}
:::

$${\sin A\over\sin B-\sin C}={b+c\over b-a}$$
::::

- 求 []{.arithmatex}$\cos C$。

考虑 []{.arithmatex}$\cos C$ 可以怎么表示，可以通过 []{.arithmatex}$\sin C$ 用毕达哥拉斯定理，也可以余弦定理。

考虑到这个原形式是一次齐次，因此考虑角化变。

:::: {.arithmatex}
::: {.MathJax_Preview}
{a\over b-c}={b+c\over b-a}\\ b\^2-c\^2=ab-a\^2\\ c\^2=a\^2+b\^2-ab
:::

$${a\over b-c}={b+c\over b-a}\\
b^2-c^2=ab-a^2\\
c^2=a^2+b^2-ab$$
::::

因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos C={a\^2+b\^2-c\^2\over2bc}={1\over2}
:::

$$\cos C={a^2+b^2-c^2\over2bc}={1\over2}$$
::::

## 例题六 {#_7}

若，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} \sin A=3\sin B\\ c=\sqrt5\\ \cos C=5/6 \end{cases}
:::

$$\begin{cases}
\sin A=3\sin B\\
c=\sqrt5\\
\cos C=5/6
\end{cases}$$
::::

- 求 []{.arithmatex}$a$。

尝试考虑这三个东西各自什么用。

最容易发现第二个式子最简单，可以最后带入用。

因为 []{.arithmatex}$\cos$ 关于余弦定理，关于边数多，因此考虑后用。

第一个式子结构很好，是一次齐次，因此带入第一个正弦定理。

:::: {.arithmatex}
::: {.MathJax_Preview}
a=3b
:::

$$a=3b$$
::::

又因为，

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos C={a\^2+b\^2-c\^2\over2ab}
:::

$$\cos C={a^2+b^2-c^2\over2ab}$$
::::

带入即可，解得 []{.arithmatex}$a=3$。

## 例题七 {#_8}

若，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{cases} b\sin2A=a\sin B\\ c=2b \end{cases}
:::

$$\begin{cases}
b\sin2A=a\sin B\\
c=2b
\end{cases}$$
::::

- 求 []{.arithmatex}$a/b$。

考虑到第二个式子的形式很简单，因此用于消元。

第一个形式中，出现了二倍角，是不好处理的，因此考虑正弦定理。

:::: {.arithmatex}
::: {.MathJax_Preview}
\sin B\sin2A=\sin A\sin B\\ \sin A=\sin2A\\ \sin A=2\sin A\cos A\\ \cos A=1/2
:::

$$\sin B\sin2A=\sin A\sin B\\
\sin A=\sin2A\\
\sin A=2\sin A\cos A\\
\cos A=1/2$$
::::

考虑到 []{.arithmatex}$a/b$ 是一个一次其次的比例式，因此余弦定理，

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos A={b\^2+c\^2-a\^2\over2bc}
:::

$$\cos A={b^2+c^2-a^2\over2bc}$$
::::

带入，解得 []{.arithmatex}$a^2=3b^2$，即 []{.arithmatex}$a/b=\sqrt3$。

## 例题八 {#_9}

在 []{.arithmatex}$\triangle ABC$ 中，

:::: {.arithmatex}
::: {.MathJax_Preview}
S=a\^2-(b-c)\^2
:::

$$S=a^2-(b-c)^2$$
::::

求 []{.arithmatex}$\sin A$。

这个式子没有很好的性质，考虑展开，

:::: {.arithmatex}
::: {.MathJax_Preview}
S=a\^2-b\^2-c\^2+2bc
:::

$$S=a^2-b^2-c^2+2bc$$
::::

注意到这个形式，而且还是二次齐次式，根据余弦定理，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\^2=b\^2+c\^2-2bc\cos A
:::

$$a^2=b^2+c^2-2bc\cos A$$
::::

有，

:::: {.arithmatex}
::: {.MathJax_Preview}
S=2bc(1-\cos A)={1\over2}bc\sin A\\ \sin A=4-4\cos A
:::

$$S=2bc(1-\cos A)={1\over2}bc\sin A\\
\sin A=4-4\cos A$$
::::

联立得方程，

:::: {.arithmatex}
::: {.MathJax_Preview}
(4-4\cos A)\^2+\cos\^2A=1\\ 16(1-\cos A)\^2=(1-\cos A)(1+\cos A)\\ 16-16\cos A=1+\cos A\\ \cos A={15\over17},\\ \sin A={8\over17}
:::

$$(4-4\cos A)^2+\cos^2A=1\\
16(1-\cos A)^2=(1-\cos A)(1+\cos A)\\
16-16\cos A=1+\cos A\\
\cos A={15\over17},\,
\sin A={8\over17}$$
::::

## 例题九 {#_10}

在 []{.arithmatex}$\triangle ABC$ 中，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sin A=2\sin B\cos C\\ a\^2=b\^2+c\^2-bc
:::

$$\sin A=2\sin B\cos C\\
a^2=b^2+c^2-bc$$
::::

- 求，[]{.arithmatex}$\triangle ABC$ 形状。

两个式子都很典型，第二个好说，先处理，

联立二式及余弦定理，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\^2=b\^2+c\^2-bc\\ a\^2=b\^2+c\^2-2bc\cos A
:::

$$a^2=b^2+c^2-bc\\
a^2=b^2+c^2-2bc\cos A$$
::::

得，

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos A={1\over2},\\A=60\^\circ
:::

$$\cos A={1\over2},\,A=60^\circ$$
::::

第一个式子，可以不带入 []{.arithmatex}$A$，尝试通过三角函数的变换，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \sin A&=\sin(\pi-B-C)=\sin(B+C)\\ &=\sin B\cos C+\cos B\sin C \end{aligned}
:::

$$\begin{aligned}
\sin A&=\sin(\pi-B-C)=\sin(B+C)\\
&=\sin B\cos C+\cos B\sin C
\end{aligned}$$
::::

联立下式及一式，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sin B\cos C+\cos B\sin C=2\sin B\cos C\\ \sin B\cos C=\cos B\sin C\\ \tan B=\tan C
:::

$$\sin B\cos C+\cos B\sin C=2\sin B\cos C\\
\sin B\cos C=\cos B\sin C\\
\tan B=\tan C$$
::::

因为 []{.arithmatex}$B,C\in(0,\pi)$，正切函数在此范围内唯一，则

:::: {.arithmatex}
::: {.MathJax_Preview}
B=C=A=60\^\circ
:::

$$B=C=A=60^\circ$$
::::

即 []{.arithmatex}$\triangle ABC$ 是正三角形。

## 例题十 {#_11}

在 []{.arithmatex}$\triangle ABC$ 中，

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos(2B+C)+\cos C\>0
:::

$$\cos(2B+C)+\cos C>0$$
::::

- 判断三角形是锐角、直角、钝角三角形。

容易发现，[]{.arithmatex}$\cos$ 里面的角有很好的性质，考虑和差化积，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} &\cos(2B+C)+\cos C\\ =\\&2\cos(B+C)\cos B\\ =\\&-2\cos A\cos B\>0 \end{aligned}
:::

$$\begin{aligned}
&\cos(2B+C)+\cos C\\
=\;&2\cos(B+C)\cos B\\
=\;&-2\cos A\cos B>0
\end{aligned}$$
::::

因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos A\cos B\<0
:::

$$\cos A\cos B<0$$
::::

即 []{.arithmatex}$A,B$ 中有一个钝角，即 []{.arithmatex}$\triangle ABC$ 为钝角三角形。

## 例题十一 {#_12}

在 []{.arithmatex}$\triangle ABC$ 中，三边长分别为 []{.arithmatex}$a,a+2,a+4$，最小角余弦值为 []{.arithmatex}$13/14$。

- 求该三角形的面积

因为大边对大角，因此最小角是 []{.arithmatex}$a$ 对的，

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos A={(a+2)\^2+(a+4)\^2-a\^2\over2(a+2)(a+4)}={13\over14}
:::

$$\cos A={(a+2)^2+(a+4)^2-a^2\over2(a+2)(a+4)}={13\over14}$$
::::

解得，[]{.arithmatex}$a=3$，于是用海伦公式，

:::: {.arithmatex}
::: {.MathJax_Preview}
p={3+5+7\over2}={15\over2}
:::

$$p={3+5+7\over2}={15\over2}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
S=\sqrt{{15\over2}\cdot{9\over2}\cdot{5\over2}\cdot{1\over2}}={15\sqrt3\over4}
:::

$$S=\sqrt{{15\over2}\cdot{9\over2}\cdot{5\over2}\cdot{1\over2}}={15\sqrt3\over4}$$
::::

## 例题十二 {#_13}

在 []{.arithmatex}$\triangle ABC$ 中，[]{.arithmatex}$\angle A=120^\circ$，[]{.arithmatex}$BC=6$。

- 求：其面积最大值。

考虑面积可以怎么表示。

Solution 1:

:::: {.arithmatex}
::: {.MathJax_Preview}
S={1\over2}bc\sin A={\sqrt3\over4}bc
:::

$$S={1\over2}bc\sin A={\sqrt3\over4}bc$$
::::

根据余弦定理，

:::: {.arithmatex}
::: {.MathJax_Preview}
36=a\^2=b\^2+c\^2-2bc\cos A=b\^2+c\^2+bc\ge3bc
:::

$$36=a^2=b^2+c^2-2bc\cos A=b^2+c^2+bc\ge3bc$$
::::

即，

:::: {.arithmatex}
::: {.MathJax_Preview}
bc\le12,\\S\le3\sqrt3
:::

$$bc\le12,\,S\le3\sqrt3$$
::::

Solution 2:

考虑到顶角不变，则可以固定底边，使顶点移动。

易知其轨迹为一个圆弧，则面积最大即底边高线最大。

高线最大即该三角形为等腰三角形，做出高线，

:::: {.arithmatex}
::: {.MathJax_Preview}
S={1\over2}ah=3\sqrt3
:::

$$S={1\over2}ah=3\sqrt3$$
::::

## 例题十三 {#_14}

在 []{.arithmatex}$\triangle ABC$ 中，若

:::: {.arithmatex}
::: {.MathJax_Preview}
a-b=c(\cos B-\cos A)
:::

$$a-b=c(\cos B-\cos A)$$
::::

- 判断其形状。

考虑到余弦定理展开后是三次式，有点复杂，因此正弦定理。

:::: {.arithmatex}
::: {.MathJax_Preview}
\sin A-\sin B=\sin C\cos B-\sin C\cos A
:::

$$\sin A-\sin B=\sin C\cos B-\sin C\cos A$$
::::

考虑凑项，右边的两项很像正弦的和角公式，于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} &\sin(B+C)-\sin(A+C)\\ =\\&\sin B\cos C+\sin C\cos B-\sin A\cos C-\sin C\cos A\\ =\\&\sin C\cos B-\sin C\cos A \end{aligned}
:::

$$\begin{aligned}
&\sin(B+C)-\sin(A+C)\\
=\;&\sin B\cos C+\sin C\cos B-\sin A\cos C-\sin C\cos A\\
=\;&\sin C\cos B-\sin C\cos A
\end{aligned}$$
::::

化简，

:::: {.arithmatex}
::: {.MathJax_Preview}
(\sin B-\sin A)\cos C=0
:::

$$(\sin B-\sin A)\cos C=0$$
::::

即 []{.arithmatex}$\sin A=\sin B$ 或 []{.arithmatex}$\cos C=0$，

即 []{.arithmatex}$\triangle ABC$ 为等腰三角形或直角三角形。

## 例题十四 {#_15}

若 []{.arithmatex}$\triangle ABC$ 中，[]{.arithmatex}$\angle C$ 为钝角，且其面积，

:::: {.arithmatex}
::: {.MathJax_Preview}
S={\sqrt3\over4}(a\^2+c\^2-b\^2)
:::

$$S={\sqrt3\over4}(a^2+c^2-b^2)$$
::::

- 求 []{.arithmatex}$\angle B$。

考虑到 []{.arithmatex}$a^2+c^2-b^2$ 是经典掉牙的形式，

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos B={a\^2+c\^2-b\^2\over2ac}
:::

$$\cos B={a^2+c^2-b^2\over2ac}$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
S={\sqrt3\over4}\cdot2ac\cos B={\sqrt3\over2}ac\cos B
:::

$$S={\sqrt3\over4}\cdot2ac\cos B={\sqrt3\over2}ac\cos B$$
::::

考虑很经典的面积公式，

:::: {.arithmatex}
::: {.MathJax_Preview}
S={1\over2}ac\sin B={\sqrt3\over2}ac\cos B\\ \sin B=\sqrt3\cos B\\ \tan B=\sqrt3,\\B=60\^\circ
:::

$$S={1\over2}ac\sin B={\sqrt3\over2}ac\cos B\\
\sin B=\sqrt3\cos B\\
\tan B=\sqrt3,\,B=60^\circ$$
::::

## 例题十五 {#_16}

在 []{.arithmatex}$\triangle ABC$ 中，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sin\^2A-\sin\^2B-\sin\^2C=\sin B\sin C
:::

$$\sin^2A-\sin^2B-\sin^2C=\sin B\sin C$$
::::

- 求 []{.arithmatex}$A$.
- 若 []{.arithmatex}$BC=3$，求其周长最大值。

因为是正弦的二次齐次式，考虑正弦定理，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\^2=b\^2+c\^2+bc
:::

$$a^2=b^2+c^2+bc$$
::::

于是 []{.arithmatex}$\angle A=120^\circ$。

考虑周长最大，即 []{.arithmatex}$b+c$ 最大，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\^2=9=b\^2+c\^2+bc\ge3bc\\ bc\le3
:::

$$a^2=9=b^2+c^2+bc\ge3bc\\
bc\le3$$
::::

考虑周长如何建立联系

:::: {.arithmatex}
::: {.MathJax_Preview}
b+c=\sqrt{b\^2+c\^2+2bc}=\sqrt{9+bc}\le2\sqrt3
:::

$$b+c=\sqrt{b^2+c^2+2bc}=\sqrt{9+bc}\le2\sqrt3$$
::::

即周长，

:::: {.arithmatex}
::: {.MathJax_Preview}
a+b+c\le2\sqrt3+3
:::

$$a+b+c\le2\sqrt3+3$$
::::

## 例题十六 {#_17}

在 []{.arithmatex}$\triangle ABC$ 中，

:::: {.arithmatex}
::: {.MathJax_Preview}
\sin A+2\sin B\cos C=0\\ c=\sqrt3b
:::

$$\sin A+2\sin B\cos C=0\\
c=\sqrt3b$$
::::

- 求 []{.arithmatex}$\tan A$。

考虑到第二个很适合消元 []{.arithmatex}$c$，于是第一个式子可以看成一次齐次，

:::: {.arithmatex}
::: {.MathJax_Preview}
a+2b\cos C=0\\ \cos C=-{a\over2b}={a\^2+b\^2-c\^2\over2bc}={a\^2-2b\^2\over2bc}
:::

$$a+2b\cos C=0\\
\cos C=-{a\over2b}={a^2+b^2-c^2\over2bc}={a^2-2b^2\over2bc}$$
::::

因此，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\^2=b\^2\\ a=b
:::

$$a^2=b^2\\
a=b$$
::::

因为 []{.arithmatex}$c=\sqrt3b$，这是一个 []{.arithmatex}$30^\circ,30^\circ,120^\circ$ 的等腰三角形，

:::: {.arithmatex}
::: {.MathJax_Preview}
\tan A=\tan30\^\circ={\sqrt3\over3}
:::

$$\tan A=\tan30^\circ={\sqrt3\over3}$$
::::

## 例题十七 {#_18}

在 []{.arithmatex}$\triangle ABC$ 中，

:::: {.arithmatex}
::: {.MathJax_Preview}
a\^2+b\^2=2022c\^2
:::

$$a^2+b^2=2022c^2$$
::::

求，

:::: {.arithmatex}
::: {.MathJax_Preview 2_tan="2\\tan" a_tan="A+\\tan" b_="B)" b_over_tan="B\\over\\tan" c_tan="C(\\tan"}
:::

$$$$
::::

考虑到没有什么好玩的结构，因此展开正切。

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} S&={2\tan A\tan B\over\tan C(\tan A+\tan B)}\\ &={2\sin A\sin B\over\sin C/\cos C\cdot(\sin A\cos B+\cos A+\sin B)}\\ &={2\sin A\sin B\cos C\over\sin\^2C} \end{aligned}
:::

$$\begin{aligned}
S&={2\tan A\tan B\over\tan C(\tan A+\tan B)}\\
&={2\sin A\sin B\over\sin C/\cos C\cdot(\sin A\cos B+\cos A+\sin B)}\\
&={2\sin A\sin B\cos C\over\sin^2C}
\end{aligned}$$
::::

考虑到上下正弦构成二次齐次，正弦定理，

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} S&={2\sin A\sin B\cos C\over\sin\^2C}\\ &={2ab\cos C\over c\^2} \end{aligned}
:::

$$\begin{aligned}
S&={2\sin A\sin B\cos C\over\sin^2C}\\
&={2ab\cos C\over c^2}
\end{aligned}$$
::::

注意到 []{.arithmatex}$2ab$ 和 []{.arithmatex}$\cos C$ 的余弦定理的分母类似，

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos C={a\^2+b\^2-c\^2\over2ab}
:::

$$\cos C={a^2+b^2-c^2\over2ab}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} S&={a\^2+b\^2-c\^2\over c\^2}={a\^2+b\^2\over c\^2}-1\\ &=2022-1=2021 \end{aligned}
:::

$$\begin{aligned}
S&={a^2+b^2-c^2\over c^2}={a^2+b^2\over c^2}-1\\
&=2022-1=2021
\end{aligned}$$
::::

## 例题十八 {#_19}

在锐角三角形 []{.arithmatex}$ABC$ 中，[]{.arithmatex}$a^2-b^2=bc$。

求证：[]{.arithmatex}$A=2B$。

经典题，因为角不好表示，上式又是边的二次齐次式，考虑，

:::: {.arithmatex}
::: {.MathJax_Preview}
\cos A={b\^2+c\^2-a\^2\over2bc}={c\^2-bc\over2bc}={c-b\over2b}\\
:::

$$\cos A={b^2+c^2-a^2\over2bc}={c^2-bc\over2bc}={c-b\over2b}\\$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
\begin{aligned} \cos 2B&=2\cos\^2B-1=2\left({a\^2+c\^2-b\^2\over2ac}\right)\^2-1\\ &=2\left({c+b\over2a}\right)\^2-1={2c\^2+2b\^2+4bc-4a\^2\over4a\^2}\\ &={2c\^2-2b\^2\over4b\^2+4bc}={2(c+b)(c-b)\over4b(b+c)}={c-b\over2b} \end{aligned}
:::

$$\begin{aligned}
\cos 2B&=2\cos^2B-1=2\left({a^2+c^2-b^2\over2ac}\right)^2-1\\
&=2\left({c+b\over2a}\right)^2-1={2c^2+2b^2+4bc-4a^2\over4a^2}\\
&={2c^2-2b^2\over4b^2+4bc}={2(c+b)(c-b)\over4b(b+c)}={c-b\over2b}
\end{aligned}$$
::::

于是，

:::: {.arithmatex}
::: {.MathJax_Preview}
(\cos A=\cos2B)\Longrightarrow(A=2B)
:::

$$(\cos A=\cos2B)\Longrightarrow(A=2B)$$
::::
