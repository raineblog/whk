# 三角函数例题 {#_1}

## 例题一 {#_2}

::: {.arithmatex}
\$\$ 2\cos\^2{B\over2}+\sqrt3\sin B=3 \$\$
:::

- 求 [\$B\$]{.arithmatex}.

::: {.arithmatex}
\$\$ \cos B=2\cos\^2{B\over2}-1\\ \cos B+\sqrt3\sin B=2\\ {\sqrt3\over2}\sin B+{1\over2}\cos B=1\\ \sin B\cos30\^\circ+\cos B\sin30\^\circ=1\\ \sin(B+30\^\circ)=1=\sin90\^\circ\\ B=60\^\circ \$\$
:::

## 例题二 {#_3}

::: {.arithmatex}
\$\$ (\sin B-\sin C)\^2=\sin\^2 A-\sin B\sin C \$\$
:::

- 求 [\$A\$]{.arithmatex}.
- 若 [\$\sqrt2a + b= 2c\$]{.arithmatex}，求 [\$C\$]{.arithmatex}.

观察到是角的二次齐次式，且都是正弦，考虑正弦定理，

::: {.arithmatex}
\$\$ (\sin B-\sin C)\^2=\sin\^2 A-\sin B\sin C\\\\ (b-c)\^2=a\^2-bc\\\\ b\^2+c\^2-2bc=a\^2-bc\\\\ a\^2=b\^2+c\^2-bc \$\$
:::

于是，

::: {.arithmatex}
\$\$ \cos A={b\^2+c\^2-a\^2\over2bc}={1\over2}\\\\ A=60\^\circ \$\$
:::

观察到 [\$\sqrt2a + b= 2c\$]{.arithmatex} 为边的一次齐次，考虑用正弦定理。

::: {.arithmatex}
\$\$ \sqrt2a+b=2c\\\\ \sqrt2\sin A+\sin B=2\sin C \$\$
:::

根据上一问，[\$\sin A=\sin60\^\circ=\sqrt3/2\$]{.arithmatex}，

::: {.arithmatex}
\$\$ \sqrt6/2+\sin B=2\sin C\\\\ \sqrt6/2+\sin(120-C)=2\sin C\\\\ \sqrt6/2+\sqrt3/2\cos C+\sin C/2=2\sin C \$\$
:::

继续整理，

::: {.arithmatex}
\$\$ {\sqrt6\over2}+{\sqrt3\over2}\cos C+{1\over2}\sin C=2\sin C\\\\ {3\over2}\sin C-{\sqrt3\over2}\cos C={\sqrt6\over2}\\\\ {\sqrt3\over2}\sin C-{1\over2}\cos C={\sqrt2\over2}\\\\ \sin C\cos30\^\circ-\cos C\sin30\^\circ={\sqrt2\over2}\\\\ \sin(C-30\^\circ)={\sqrt2\over2}=\sin45\^\circ \$\$
:::

因为 [\$C \in (0\^\circ,120 \^\circ)\$]{.arithmatex}，[\$C-30\^\circ\in(-30\^\circ,90\^\circ)\$]{.arithmatex}，因此，

::: {.arithmatex}
\$\$ C-30\^\circ=45\^\circ,\\ C=75\^\circ \$\$
:::

## 例题三 {#_4}

在锐角 [\$\triangle ABC\$]{.arithmatex} 中，

::: {.arithmatex}
\$\$ 2b\sin A-\sqrt3a=0 \$\$
:::

- 求 [\$B\$]{.arithmatex}.
- 求 [\$\cos A+\cos B+\cos C\$]{.arithmatex} 的取值范围。

不考虑 [\$\sin A\$]{.arithmatex} 是边的二次齐次式，于是应用正弦定理，

::: {.arithmatex}
\$\$ 2\sin B\sin A-\sqrt2\sin A=0\\\\ 2\sin B=\sqrt3\\ \sin B=\sqrt3/2 \$\$
:::

因为 [\$\angle B\$]{.arithmatex} 是锐角，

::: {.arithmatex}
\$\$ B=60\^\circ \$\$
:::

设，

::: {.arithmatex}
\$\$ \def\degree{\^\circ} \begin{aligned} S&=\cos A+\cos B+\cos C\\ &=\cos A+\cos C+1/2\\ &=\cos(120\degree-C)+\cos C+1/2\\ &=-{1\over2}\cos C+{\sqrt3\over2}\sin C+\cos C+{1\over2}\\ &={\sqrt3\over2}\sin C+{1\over2}\cos C+{1\over2}\\ &=\sin C\cos30\degree+\cos C\sin30\degree +1/2\\ &=\sin(C+30\degree)+1/2 \end{aligned} \$\$
:::

因为 [\$0\^\circ\<A,B,C\<90\^\circ\$]{.arithmatex}，

::: {.arithmatex}
\$\$ \def\degree{\^\circ} \begin{cases} 0\degree\<&C&\<90\degree\\ 0\degree\<&B&\<90\degree \end{cases} \Longleftrightarrow \begin{cases} 0\degree\<&C&\<90\degree\\ 0\degree\<&120-C&\<90\degree \end{cases} \$\$
:::

即，[\$30\^\circ\<C\<90\^\circ\$]{.arithmatex}，[\$60\^\circ\<C+30\^\circ\<120\^\circ\$]{.arithmatex}。

画出单位圆，易得 [\$\sin(C+30\degree)\in(\sqrt3/2,1\]\$]{.arithmatex}，即，

::: {.arithmatex}
\$\$ \cos A+\cos B+\cos C\in\left({\sqrt3+1\over2},{3\over2}\right\] \$\$
:::

## 例题四 {#_5}

在 [\$\triangle ABC\$]{.arithmatex} 中，[\$a+b=11\$]{.arithmatex}，

::: {.arithmatex}
\$\$ \cos A={1\over8},\\\cos B={9\over16} \$\$
:::

- 求 [\$a,b\$]{.arithmatex}。

考虑余弦转正弦，因为是三角形的角，因此正弦值非负，

::: {.arithmatex}
\$\$ \sin A=\sqrt{1-\cos\^2 A}=\sqrt{63\over64}={3\sqrt7\over8}\\ \sin B=\sqrt{1-\cos\^2 B}=\sqrt{175\over256}={5\sqrt7\over16} \$\$
:::

::: {.arithmatex}
\$\$ {a\over b}={\sin A\over\sin B}={6\over5} \$\$
:::

因此 [\$a=6,\\b=5\$]{.arithmatex}。

## 例题五 {#_6}

::: {.arithmatex}
\$\$ {\sin A\over\sin B-\sin C}={b+c\over b-a} \$\$
:::

- 求 [\$\cos C\$]{.arithmatex}。

考虑 [\$\cos C\$]{.arithmatex} 可以怎么表示，可以通过 [\$\sin C\$]{.arithmatex} 用毕达哥拉斯定理，也可以余弦定理。

考虑到这个原形式是一次齐次，因此考虑角化变。

::: {.arithmatex}
\$\$ {a\over b-c}={b+c\over b-a}\\ b\^2-c\^2=ab-a\^2\\ c\^2=a\^2+b\^2-ab \$\$
:::

因此，

::: {.arithmatex}
\$\$ \cos C={a\^2+b\^2-c\^2\over2bc}={1\over2} \$\$
:::

## 例题六 {#_7}

若，

::: {.arithmatex}
\$\$ \begin{cases} \sin A=3\sin B\\ c=\sqrt5\\ \cos C=5/6 \end{cases} \$\$
:::

- 求 [\$a\$]{.arithmatex}。

尝试考虑这三个东西各自什么用。

最容易发现第二个式子最简单，可以最后带入用。

因为 [\$\cos\$]{.arithmatex} 关于余弦定理，关于边数多，因此考虑后用。

第一个式子结构很好，是一次齐次，因此带入第一个正弦定理。

::: {.arithmatex}
\$\$ a=3b \$\$
:::

又因为，

::: {.arithmatex}
\$\$ \cos C={a\^2+b\^2-c\^2\over2ab} \$\$
:::

带入即可，解得 [\$a=3\$]{.arithmatex}。

## 例题七 {#_8}

若，

::: {.arithmatex}
\$\$ \begin{cases} b\sin2A=a\sin B\\ c=2b \end{cases} \$\$
:::

- 求 [\$a/b\$]{.arithmatex}。

考虑到第二个式子的形式很简单，因此用于消元。

第一个形式中，出现了二倍角，是不好处理的，因此考虑正弦定理。

::: {.arithmatex}
\$\$ \sin B\sin2A=\sin A\sin B\\ \sin A=\sin2A\\ \sin A=2\sin A\cos A\\ \cos A=1/2 \$\$
:::

考虑到 [\$a/b\$]{.arithmatex} 是一个一次其次的比例式，因此余弦定理，

::: {.arithmatex}
\$\$ \cos A={b\^2+c\^2-a\^2\over2bc} \$\$
:::

带入，解得 [\$a\^2=3b\^2\$]{.arithmatex}，即 [\$a/b=\sqrt3\$]{.arithmatex}。

## 例题八 {#_9}

在 [\$\triangle ABC\$]{.arithmatex} 中，

::: {.arithmatex}
\$\$ S=a\^2-(b-c)\^2 \$\$
:::

求 [\$\sin A\$]{.arithmatex}。

这个式子没有很好的性质，考虑展开，

::: {.arithmatex}
\$\$ S=a\^2-b\^2-c\^2+2bc \$\$
:::

注意到这个形式，而且还是二次齐次式，根据余弦定理，

::: {.arithmatex}
\$\$ a\^2=b\^2+c\^2-2bc\cos A \$\$
:::

有，

::: {.arithmatex}
\$\$ S=2bc(1-\cos A)={1\over2}bc\sin A\\ \sin A=4-4\cos A \$\$
:::

联立得方程，

::: {.arithmatex}
\$\$ (4-4\cos A)\^2+\cos\^2A=1\\ 16(1-\cos A)\^2=(1-\cos A)(1+\cos A)\\ 16-16\cos A=1+\cos A\\ \cos A={15\over17},\\ \sin A={8\over17} \$\$
:::

## 例题九 {#_10}

在 [\$\triangle ABC\$]{.arithmatex} 中，

::: {.arithmatex}
\$\$ \sin A=2\sin B\cos C\\ a\^2=b\^2+c\^2-bc \$\$
:::

- 求，[\$\triangle ABC\$]{.arithmatex} 形状。

两个式子都很典型，第二个好说，先处理，

联立二式及余弦定理，

::: {.arithmatex}
\$\$ a\^2=b\^2+c\^2-bc\\ a\^2=b\^2+c\^2-2bc\cos A \$\$
:::

得，

::: {.arithmatex}
\$\$ \cos A={1\over2},\\A=60\^\circ \$\$
:::

第一个式子，可以不带入 [\$A\$]{.arithmatex}，尝试通过三角函数的变换，

::: {.arithmatex}
\$\$ \begin{aligned} \sin A&=\sin(\pi-B-C)=\sin(B+C)\\ &=\sin B\cos C+\cos B\sin C \end{aligned} \$\$
:::

联立下式及一式，

::: {.arithmatex}
\$\$ \sin B\cos C+\cos B\sin C=2\sin B\cos C\\ \sin B\cos C=\cos B\sin C\\ \tan B=\tan C \$\$
:::

因为 [\$B,C\in(0,\pi)\$]{.arithmatex}，正切函数在此范围内唯一，则

::: {.arithmatex}
\$\$ B=C=A=60\^\circ \$\$
:::

即 [\$\triangle ABC\$]{.arithmatex} 是正三角形。

## 例题十 {#_11}

在 [\$\triangle ABC\$]{.arithmatex} 中，

::: {.arithmatex}
\$\$ \cos(2B+C)+\cos C\>0 \$\$
:::

- 判断三角形是锐角、直角、钝角三角形。

容易发现，[\$\cos\$]{.arithmatex} 里面的角有很好的性质，考虑和差化积，

::: {.arithmatex}
\$\$ \begin{aligned} &\cos(2B+C)+\cos C\\ =\\&2\cos(B+C)\cos B\\ =\\&-2\cos A\cos B\>0 \end{aligned} \$\$
:::

因此，

::: {.arithmatex}
\$\$ \cos A\cos B\<0 \$\$
:::

即 [\$A,B\$]{.arithmatex} 中有一个钝角，即 [\$\triangle ABC\$]{.arithmatex} 为钝角三角形。

## 例题十一 {#_12}

在 [\$\triangle ABC\$]{.arithmatex} 中，三边长分别为 [\$a,a+2,a+4\$]{.arithmatex}，最小角余弦值为 [\$13/14\$]{.arithmatex}。

- 求该三角形的面积

因为大边对大角，因此最小角是 [\$a\$]{.arithmatex} 对的，

::: {.arithmatex}
\$\$ \cos A={(a+2)\^2+(a+4)\^2-a\^2\over2(a+2)(a+4)}={13\over14} \$\$
:::

解得，[\$a=3\$]{.arithmatex}，于是用海伦公式，

::: {.arithmatex}
\$\$ p={3+5+7\over2}={15\over2} \$\$
:::

::: {.arithmatex}
\$\$ S=\sqrt{{15\over2}\cdot{9\over2}\cdot{5\over2}\cdot{1\over2}}={15\sqrt3\over4} \$\$
:::

## 例题十二 {#_13}

在 [\$\triangle ABC\$]{.arithmatex} 中，[\$\angle A=120\^\circ\$]{.arithmatex}，[\$BC=6\$]{.arithmatex}。

- 求：其面积最大值。

考虑面积可以怎么表示。

Solution 1:

::: {.arithmatex}
\$\$ S={1\over2}bc\sin A={\sqrt3\over4}bc \$\$
:::

根据余弦定理，

::: {.arithmatex}
\$\$ 36=a\^2=b\^2+c\^2-2bc\cos A=b\^2+c\^2+bc\ge3bc \$\$
:::

即，

::: {.arithmatex}
\$\$ bc\le12,\\S\le3\sqrt3 \$\$
:::

Solution 2:

考虑到顶角不变，则可以固定底边，使顶点移动。

易知其轨迹为一个圆弧，则面积最大即底边高线最大。

高线最大即该三角形为等腰三角形，做出高线，

::: {.arithmatex}
\$\$ S={1\over2}ah=3\sqrt3 \$\$
:::

## 例题十三 {#_14}

在 [\$\triangle ABC\$]{.arithmatex} 中，若

::: {.arithmatex}
\$\$ a-b=c(\cos B-\cos A) \$\$
:::

- 判断其形状。

考虑到余弦定理展开后是三次式，有点复杂，因此正弦定理。

::: {.arithmatex}
\$\$ \sin A-\sin B=\sin C\cos B-\sin C\cos A \$\$
:::

考虑凑项，右边的两项很像正弦的和角公式，于是，

::: {.arithmatex}
\$\$ \begin{aligned} &\sin(B+C)-\sin(A+C)\\ =\\&\sin B\cos C+\sin C\cos B-\sin A\cos C-\sin C\cos A\\ =\\&\sin C\cos B-\sin C\cos A \end{aligned} \$\$
:::

化简，

::: {.arithmatex}
\$\$ (\sin B-\sin A)\cos C=0 \$\$
:::

即 [\$\sin A=\sin B\$]{.arithmatex} 或 [\$\cos C=0\$]{.arithmatex}，

即 [\$\triangle ABC\$]{.arithmatex} 为等腰三角形或直角三角形。

## 例题十四 {#_15}

若 [\$\triangle ABC\$]{.arithmatex} 中，[\$\angle C\$]{.arithmatex} 为钝角，且其面积，

::: {.arithmatex}
\$\$ S={\sqrt3\over4}(a\^2+c\^2-b\^2) \$\$
:::

- 求 [\$\angle B\$]{.arithmatex}。

考虑到 [\$a\^2+c\^2-b\^2\$]{.arithmatex} 是经典掉牙的形式，

::: {.arithmatex}
\$\$ \cos B={a\^2+c\^2-b\^2\over2ac} \$\$
:::

于是，

::: {.arithmatex}
\$\$ S={\sqrt3\over4}\cdot2ac\cos B={\sqrt3\over2}ac\cos B \$\$
:::

考虑很经典的面积公式，

::: {.arithmatex}
\$\$ S={1\over2}ac\sin B={\sqrt3\over2}ac\cos B\\ \sin B=\sqrt3\cos B\\ \tan B=\sqrt3,\\B=60\^\circ \$\$
:::

## 例题十五 {#_16}

在 [\$\triangle ABC\$]{.arithmatex} 中，

::: {.arithmatex}
\$\$ \sin\^2A-\sin\^2B-\sin\^2C=\sin B\sin C \$\$
:::

- 求 [\$A\$]{.arithmatex}.
- 若 [\$BC=3\$]{.arithmatex}，求其周长最大值。

因为是正弦的二次齐次式，考虑正弦定理，

::: {.arithmatex}
\$\$ a\^2=b\^2+c\^2+bc \$\$
:::

于是 [\$\angle A=120\^\circ\$]{.arithmatex}。

考虑周长最大，即 [\$b+c\$]{.arithmatex} 最大，

::: {.arithmatex}
\$\$ a\^2=9=b\^2+c\^2+bc\ge3bc\\ bc\le3 \$\$
:::

考虑周长如何建立联系

::: {.arithmatex}
\$\$ b+c=\sqrt{b\^2+c\^2+2bc}=\sqrt{9+bc}\le2\sqrt3 \$\$
:::

即周长，

::: {.arithmatex}
\$\$ a+b+c\le2\sqrt3+3 \$\$
:::

## 例题十六 {#_17}

在 [\$\triangle ABC\$]{.arithmatex} 中，

::: {.arithmatex}
\$\$ \sin A+2\sin B\cos C=0\\ c=\sqrt3b \$\$
:::

- 求 [\$\tan A\$]{.arithmatex}。

考虑到第二个很适合消元 [\$c\$]{.arithmatex}，于是第一个式子可以看成一次齐次，

::: {.arithmatex}
\$\$ a+2b\cos C=0\\ \cos C=-{a\over2b}={a\^2+b\^2-c\^2\over2bc}={a\^2-2b\^2\over2bc} \$\$
:::

因此，

::: {.arithmatex}
\$\$ a\^2=b\^2\\ a=b \$\$
:::

因为 [\$c=\sqrt3b\$]{.arithmatex}，这是一个 [\$30\^\circ,30\^\circ,120\^\circ\$]{.arithmatex} 的等腰三角形，

::: {.arithmatex}
\$\$ \tan A=\tan30\^\circ={\sqrt3\over3} \$\$
:::

## 例题十七 {#_18}

在 [\$\triangle ABC\$]{.arithmatex} 中，

::: {.arithmatex}
\$\$ a\^2+b\^2=2022c\^2 \$\$
:::

求，

::: {.arithmatex}
\$\$ {2\tan A\tan B\over\tan C(\tan A+\tan B)} \$\$
:::

考虑到没有什么好玩的结构，因此展开正切。

::: {.arithmatex}
\$\$ \begin{aligned} S&={2\tan A\tan B\over\tan C(\tan A+\tan B)}\\ &={2\sin A\sin B\over\sin C/\cos C\cdot(\sin A\cos B+\cos A+\sin B)}\\ &={2\sin A\sin B\cos C\over\sin\^2C} \end{aligned} \$\$
:::

考虑到上下正弦构成二次齐次，正弦定理，

::: {.arithmatex}
\$\$ \begin{aligned} S&={2\sin A\sin B\cos C\over\sin\^2C}\\ &={2ab\cos C\over c\^2} \end{aligned} \$\$
:::

注意到 [\$2ab\$]{.arithmatex} 和 [\$\cos C\$]{.arithmatex} 的余弦定理的分母类似，

::: {.arithmatex}
\$\$ \cos C={a\^2+b\^2-c\^2\over2ab} \$\$
:::

::: {.arithmatex}
\$\$ \begin{aligned} S&={a\^2+b\^2-c\^2\over c\^2}={a\^2+b\^2\over c\^2}-1\\ &=2022-1=2021 \end{aligned} \$\$
:::

## 例题十八 {#_19}

在锐角三角形 [\$ABC\$]{.arithmatex} 中，[\$a\^2-b\^2=bc\$]{.arithmatex}。

求证：[\$A=2B\$]{.arithmatex}。

经典题，因为角不好表示，上式又是边的二次齐次式，考虑，

::: {.arithmatex}
\$\$ \cos A={b\^2+c\^2-a\^2\over2bc}={c\^2-bc\over2bc}={c-b\over2b}\\ \$\$
:::

::: {.arithmatex}
\$\$ \begin{aligned} \cos 2B&=2\cos\^2B-1=2\left({a\^2+c\^2-b\^2\over2ac}\right)\^2-1\\ &=2\left({c+b\over2a}\right)\^2-1={2c\^2+2b\^2+4bc-4a\^2\over4a\^2}\\ &={2c\^2-2b\^2\over4b\^2+4bc}={2(c+b)(c-b)\over4b(b+c)}={c-b\over2b} \end{aligned} \$\$
:::

于是，

::: {.arithmatex}
\$\$ (\cos A=\cos2B)\Longrightarrow(A=2B) \$\$
:::
