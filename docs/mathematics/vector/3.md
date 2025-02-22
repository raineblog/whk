# 例题

## 例题一

$$
2\cos^2{B\over2}+\sqrt3\sin B=3
$$

+ 求 $B$.

$$
\cos B=2\cos^2{B\over2}-1\\
\cos B+\sqrt3\sin B=2\\
{\sqrt3\over2}\sin B+{1\over2}\cos B=1\\
\sin B\cos30^\circ+\cos B\sin30^\circ=1\\
\sin(B+30^\circ)=1=\sin90^\circ\\
B=60^\circ
$$

## 例题二

$$
(\sin B-\sin C)^2=\sin^2 A-\sin B\sin C
$$

+ 求 $A$.
+ 若 $\sqrt2a + b= 2c$，求 $C$.

观察到是角的二次齐次式，且都是正弦，考虑正弦定理，

$$
(\sin B-\sin C)^2=\sin^2 A-\sin B\sin C\\\\
(b-c)^2=a^2-bc\\\\
b^2+c^2-2bc=a^2-bc\\\\
a^2=b^2+c^2-bc
$$

于是，

$$
\cos A={b^2+c^2-a^2\over2bc}={1\over2}\\\\
A=60^\circ
$$

观察到 $\sqrt2a + b= 2c$ 为边的一次齐次，考虑用正弦定理。

$$
\sqrt2a+b=2c\\\\
\sqrt2\sin A+\sin B=2\sin C
$$

根据上一问，$\sin A=\sin60^\circ=\sqrt3/2$，

$$
\sqrt6/2+\sin B=2\sin C\\\\
\sqrt6/2+\sin(120-C)=2\sin C\\\\
\sqrt6/2+\sqrt3/2\cos C+\sin C/2=2\sin C
$$

继续整理，

$$
{\sqrt6\over2}+{\sqrt3\over2}\cos C+{1\over2}\sin C=2\sin C\\\\
{3\over2}\sin C-{\sqrt3\over2}\cos C={\sqrt6\over2}\\\\
{\sqrt3\over2}\sin C-{1\over2}\cos C={\sqrt2\over2}\\\\
\sin C\cos30^\circ-\cos C\sin30^\circ={\sqrt2\over2}\\\\
\sin(C-30^\circ)={\sqrt2\over2}=\sin45^\circ
$$

因为 $C \in (0^\circ,120 ^\circ)$，$C-30^\circ\in(-30^\circ,90^\circ)$，因此，

$$
C-30^\circ=45^\circ,\ C=75^\circ
$$

## 例题三

在锐角 $\triangle ABC$ 中，

$$
2b\sin A-\sqrt3a=0
$$

+ 求 $B$.
+ 求 $\cos A+\cos B+\cos C$ 的取值范围.

不考虑 $\sin A$ 是边的二次齐次式，于是应用正弦定理，

$$
2\sin B\sin A-\sqrt2\sin A=0\\\\
2\sin B=\sqrt3\\
\sin B=\sqrt3/2
$$

因为 $\angle B$ 是锐角，

$$
B=60^\circ
$$

设，

$$
\def\degree{^\circ}
\begin{aligned}
S&=\cos A+\cos B+\cos C\\
&=\cos A+\cos C+1/2\\
&=\cos(120\degree-C)+\cos C+1/2\\
&=-{1\over2}\cos C+{\sqrt3\over2}\sin C+\cos C+{1\over2}\\
&={\sqrt3\over2}\sin C+{1\over2}\cos C+{1\over2}\\
&=\sin C\cos30\degree+\cos C\sin30\degree
+1/2\\
&=\sin(C+30\degree)+1/2
\end{aligned}
$$

因为 $0^\circ<A,B,C<90^\circ$，

$$
\def\degree{^\circ}
\begin{cases}
0\degree<&C&<90\degree\\
0\degree<&B&<90\degree
\end{cases}
\Longleftrightarrow
\begin{cases}
0\degree<&C&<90\degree\\
0\degree<&120-C&<90\degree
\end{cases}
$$

即，$30^\circ<C<90^\circ$，$60^\circ<C+30^\circ<120^\circ$。

画出单位圆，易得 $\sin(C+30\degree)\in(\sqrt3/2,1]$，即，

$$
\cos A+\cos B+\cos C\in\left({\sqrt3+1\over2},{3\over2}\right]
$$

## 例题四

在 $\triangle ABC$ 中，$a+b=11$，

$$
\cos A={1\over8},\,\cos B={9\over16}
$$

+ 求 $a,b$。

考虑余弦转正弦，因为是三角形的角，因此正弦值非负，

$$
\sin A=\sqrt{1-\cos^2 A}=\sqrt{63\over64}={3\sqrt7\over8}\\
\sin B=\sqrt{1-\cos^2 B}=\sqrt{175\over256}={5\sqrt7\over16}
$$

$$
{a\over b}={\sin A\over\sin B}={6\over5}
$$

因此 $a=6,\,b=5$。

## 例题五

$$
{\sin A\over\sin B-\sin C}={b+c\over b-a}
$$

+ 求 $\cos C$。

考虑 $\cos C$ 可以怎么表示，可以通过 $\sin C$ 用毕达哥拉斯定理，也可以余弦定理。

考虑到这个原形式是一次齐次，因此考虑角化变。

$$
{a\over b-c}={b+c\over b-a}\\
b^2-c^2=ab-a^2\\
c^2=a^2+b^2-ab
$$

因此，

$$
\cos C={a^2+b^2-c^2\over2bc}={1\over2}
$$

## 例题六

若，

$$
\begin{cases}
\sin A=3\sin B\\
c=\sqrt5\\
\cos C=5/6
\end{cases}
$$

+ 求 $a$。

尝试考虑这三个东西各自什么用。

最容易发现第二个式子最简单，可以最后带入用。

因为 $\cos$ 关于余弦定理，关于边数多，因此考虑后用。

第一个式子结构很好，是一次齐次，因此带入第一个正弦定理。

$$
a=3b
$$

又因为，

$$
\cos C={a^2+b^2-c^2\over2ab}
$$

带入即可，解得 $a=3$。

## 例题七

若，

$$
\begin{cases}
b\sin2A=a\sin B\\
c=2b
\end{cases}
$$

+ 求 $a/b$。

考虑到第二个式子的形式很简单，因此用于消元。

第一个形式中，出现了二倍角，是不好处理的，因此考虑正弦定理。

$$
\sin B\sin2A=\sin A\sin B\\
\sin A=\sin2A\\
\sin A=2\sin A\cos A\\
\cos A=1/2
$$

考虑到 $a/b$ 是一个一次其次的比例式，因此余弦定理，

$$
\cos A={b^2+c^2-a^2\over2bc}
$$

带入，解得 $a^2=3b^2$，即 $a/b=\sqrt3$。

## 例题八

在 $\triangle ABC$ 中，

$$
S=a^2-(b-c)^2
$$

求 $\sin A$。

这个式子没有很好的性质，考虑展开，

$$
S=a^2-b^2-c^2+2bc
$$

注意到这个形式，而且还是二次齐次式，根据余弦定理，

$$
a^2=b^2+c^2-2bc\cos A
$$

有，

$$
S=2bc(1-\cos A)={1\over2}bc\sin A\\
\sin A=4-4\cos A
$$

联立得方程，

$$
(4-4\cos A)^2+\cos^2A=1\\
16(1-\cos A)^2=(1-\cos A)(1+\cos A)\\
16-16\cos A=1+\cos A\\
\cos A={15\over17},\,
\sin A={8\over17}
$$

## 例题九

在 $\triangle ABC$ 中，

$$
\sin A=2\sin B\cos C\\
a^2=b^2+c^2-bc
$$

+ 求，$\triangle ABC$ 形状。

两个式子都很典型，第二个好说，先处理，

联立二式及余弦定理，

$$
a^2=b^2+c^2-bc\\
a^2=b^2+c^2-2bc\cos A
$$

得，

$$
\cos A={1\over2},\,A=60^\circ
$$

第一个式子，可以不带入 $A$，尝试通过三角函数的变换，

$$
\begin{aligned}
\sin A&=\sin(\pi-B-C)=\sin(B+C)\\
&=\sin B\cos C+\cos B\sin C
\end{aligned}
$$

联立下式及一式，

$$
\sin B\cos C+\cos B\sin C=2\sin B\cos C\\
\sin B\cos C=\cos B\sin C\\
\tan B=\tan C
$$

因为 $B,C\in(0,\pi)$，正切函数在此范围内唯一，则

$$
B=C=A=60^\circ
$$

即 $\triangle ABC$ 是正三角形。

## 例题十

在 $\triangle ABC$ 中，

$$
\cos(2B+C)+\cos C>0
$$

+ 判断三角形是锐角、直角、钝角三角形。

容易发现，$\cos$ 里面的角有很好的性质，考虑和差化积，

$$
\begin{aligned}
&\cos(2B+C)+\cos C\\
=\;&2\cos(B+C)\cos B\\
=\;&-2\cos A\cos B>0
\end{aligned}
$$

因此，

$$
\cos A\cos B<0
$$

即 $A,B$ 中有一个钝角，即 $\triangle ABC$ 为钝角三角形。

## 例题十一

在 $\triangle ABC$ 中，三边长分别为 $a,a+2,a+4$，最小角余弦值为 $13/14$。

+ 求该三角形的面积

因为大边对大角，因此最小角是 $a$ 对的，

$$
\cos A={(a+2)^2+(a+4)^2-a^2\over2(a+2)(a+4)}={13\over14}
$$

解得，$a=3$，于是用海伦公式，

$$
p={3+5+7\over2}={15\over2}
$$

$$
S=\sqrt{{15\over2}\cdot{9\over2}\cdot{5\over2}\cdot{1\over2}}={15\sqrt3\over4}
$$

## 例题十二

在 $\triangle ABC$ 中，$\angle A=120^\circ$，$BC=6$。

+ 求：其面积最大值。

考虑面积可以怎么表示。

Solution 1:

$$
S={1\over2}bc\sin A={\sqrt3\over4}bc
$$

根据余弦定理，

$$
36=a^2=b^2+c^2-2bc\cos A=b^2+c^2+bc\ge3bc
$$

即，

$$
bc\le12,\,S\le3\sqrt3
$$

Solution 2：

考虑到顶角不变，则可以固定底边，使顶点移动。

易知其轨迹为一个圆弧，则面积最大即底边高线最大。

高线最大即该三角形为等腰三角形，做出高线，

$$
S={1\over2}ah=3\sqrt3
$$

## 例题十三

在 $\triangle ABC$ 中，若

$$
a-b=c(\cos B-\cos A)
$$

+ 判断其形状。

考虑到余弦定理展开后是三次式，有点复杂，因此正弦定理。

$$
\sin A-\sin B=\sin C\cos B-\sin C\cos A
$$

考虑凑项，右边的两项很像正弦的和角公式，于是，

$$
\begin{aligned}
&\sin(B+C)-\sin(A+C)\\
=\;&\sin B\cos C+\sin C\cos B-\sin A\cos C-\sin C\cos A\\
=\;&\sin C\cos B-\sin C\cos A
\end{aligned}
$$

化简，

$$
(\sin B-\sin A)\cos C=0
$$

即 $\sin A=\sin B$ 或 $\cos C=0$，

即 $\triangle ABC$ 为等腰三角形或直角三角形。

## 例题十四

若 $\triangle ABC$ 中，$\angle C$ 为钝角，且其面积，

$$
S={\sqrt3\over4}(a^2+c^2-b^2)
$$

+ 求 $\angle B$。

考虑到 $a^2+c^2-b^2$ 是经典掉牙的形式，

$$
\cos B={a^2+c^2-b^2\over2ac}
$$

于是，

$$
S={\sqrt3\over4}\cdot2ac\cos B={\sqrt3\over2}ac\cos B
$$

考虑很经典的面积公式，

$$
S={1\over2}ac\sin B={\sqrt3\over2}ac\cos B\\
\sin B=\sqrt3\cos B\\
\tan B=\sqrt3,\,B=60^\circ
$$

## 例题十五

在 $\triangle ABC$ 中，

$$
\sin^2A-\sin^2B-\sin^2C=\sin B\sin C
$$

+ 求 $A$.
+ 若 $BC=3$，求其周长最大值。

因为是正弦的二次齐次式，考虑正弦定理，

$$
a^2=b^2+c^2+bc
$$

于是 $\angle A=120^\circ$。

考虑周长最大，即 $b+c$ 最大，

$$
a^2=9=b^2+c^2+bc\ge3bc\\
bc\le3
$$

考虑周长如何建立联系

$$
b+c=\sqrt{b^2+c^2+2bc}=\sqrt{9+bc}\le2\sqrt3
$$

即周长，

$$
a+b+c\le2\sqrt3+3
$$

## 例题十六

在 $\triangle ABC$ 中，

$$
\sin A+2\sin B\cos C=0\\
c=\sqrt3b
$$

+ 求 $\tan A$。

考虑到第二个很适合消元 $c$，于是第一个式子可以看成一次齐次，

$$
a+2b\cos C=0\\
\cos C=-{a\over2b}={a^2+b^2-c^2\over2bc}={a^2-2b^2\over2bc}
$$

因此，

$$
a^2=b^2\\
a=b
$$

因为 $c=\sqrt3b$，这是一个 $30^\circ,30^\circ,120^\circ$ 的等腰三角形，

$$
\tan A=\tan30^\circ={\sqrt3\over3}
$$

## 例题十七

在 $\triangle ABC$ 中，

$$
a^2+b^2=2022c^2
$$

求，

$$
{2\tan A\tan B\over\tan C(\tan A+\tan B)}
$$

考虑到没有什么好玩的结构，因此展开正切。

$$
\begin{aligned}
S&={2\tan A\tan B\over\tan C(\tan A+\tan B)}\\
&={2\sin A\sin B\over\sin C/\cos C\cdot(\sin A\cos B+\cos A+\sin B)}\\
&={2\sin A\sin B\cos C\over\sin^2C}
\end{aligned}
$$

考虑到上下正弦构成二次齐次，正弦定理，

$$
\begin{aligned}
S&={2\sin A\sin B\cos C\over\sin^2C}\\
&={2ab\cos C\over c^2}
\end{aligned}
$$

注意到 $2ab$ 和 $\cos C$ 的余弦定理的分母类似，

$$
\cos C={a^2+b^2-c^2\over2ab}
$$

$$
\begin{aligned}
S&={a^2+b^2-c^2\over c^2}={a^2+b^2\over c^2}-1\\
&=2022-1=2021
\end{aligned}
$$

## 例题十八

在锐角三角形 $ABC$ 中，$a^2-b^2=bc$。

求证：$A=2B$。

经典题，因为角不好表示，上式又是边的二次齐次式，考虑，

$$
\cos A={b^2+c^2-a^2\over2bc}={c^2-bc\over2bc}={c-b\over2b}\\
$$

$$
\begin{aligned}
\cos 2B&=2\cos^2B-1=2\left({a^2+c^2-b^2\over2ac}\right)^2-1\\
&=2\left({c+b\over2a}\right)^2-1={2c^2+2b^2+4bc-4a^2\over4a^2}\\
&={2c^2-2b^2\over4b^2+4bc}={2(c+b)(c-b)\over4b(b+c)}={c-b\over2b}
\end{aligned}
$$

于是，

$$
(\cos A=\cos2B)\Longrightarrow(A=2B)
$$

## 例题：CF995C

题目：[CF995C Leaving the Bar](https://www.luogu.com.cn/problem/CF995C)

题目简述：给定 $n$ 个向量，你将一些向量取反，试求出一种取反方法，使得这 $n$ 个向量之和的模小于 $1.5\times10^6$。

正解思路：考虑任意三个向量 $\vec v_1,\vec v_2,\vec v_3$ 及其取反的向量 $-\vec v_1,-\vec v_2,-\vec v_3$。此时一共有了 $6$ 个向量。根据抽屉原理，这六个向量一定存在两个向量，其夹角小于等于 $60^\circ$。根据余弦定理 $a^2=b^2+c^2-2bc\cos\theta$。当 $\theta\le60^\circ$，$2\cos\theta\ge1$，则 $2bc\cos\theta\ge bc$。记 $M=\max\{b,c\}$，有 $a^2\le b^2+c^2-ab\le 2M^2-M^2=M^2$。也就是这两个向量相加后得到的向量的模一定不超过这两个向量的模的较大值。于是我们考虑合并任意三个向量，最终得到两个长度不超过 $10^6$ 的向量，然后我们考虑这两个向量如何定向去合并，那么当这两个向量垂直的时候，他们合并的结果最大，且一定不超过 $\sqrt 2\times10^6<1.5\times10^6$。

然而作者不会这个思路。于是采取了一个随机化的方法。考虑随机重排这些向量。然后用（假的）贪心思路来合并，即对于每一个向量只考虑合并上它的当前的最优情况。那么这个思路可能（很容易）被 Hack。于是我们重复这个过程，知道找到一组解即可。代码如下：

```cpp
#include <bits/stdc++.h>

using namespace std;

#define range(x) x.begin(), x.end()

struct emm {
    int id, x, y;
};

mt19937 rd(time(0) * clock());

int n;
vector<emm> a;
vector<int> ans;

double dis(int x, int y) {
    return sqrt(1.0 * x * x + 1.0 * y * y);
}

double solev() {
    shuffle(range(a), rd);
    int x = 0, y = 0;
    for (auto &[id, i, j] : a) {
        ans[id] = dis(x + i, y + j) < dis(x - i, y - j) ? 1 : -1;
        x += i * ans[id], y += j * ans[id];
    } return dis(x, y);
}

void print() {
    for (int i : ans) cout << i << " ";
    cout << endl;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr), cout.tie(nullptr);
    cin >> n; a.resize(n), ans.resize(n);
    for (int i = 0; i < n; ++i) cin >> a[i].x >> a[i].y, a[i].id = i;
    while (1) if (solev() <= 1.5e6) print(), exit(0);
    return 0;
}

```
