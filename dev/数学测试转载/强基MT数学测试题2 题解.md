# [强基MT数学测试题2 题解](https://www.luogu.com/article/a0anlk3y)

### **一、解答题**   

**1.** $\text{(30分)}$ 在 $1$ 到 $n$ 中插入 $k$ 个实数，使得这 $k+2$ 个数构成递增的等比数列，令函数 $f(n,k)$ 表示这 $k+2$ 个数的乘积 $(n>1,k\in\mathbb{N}^+)$，   
$(1)$ 求函数 $f(n,k)$ 的解析式。$(\text{10分})$   
$(2)$ 令函数 $g(x)=\sum\limits_{i=1}^{x}f(2^{2i},x-2)\;,\;h(x)=\sum\limits_{i=1}^{x-2}f(2^{2x},i)\ (x\geq3\text{且}x\in\mathbb{Z})$，试求出 $g(x)$ 的解析式，并求出 $\dfrac{g(x)-h(x)}{\left(2\sqrt2\right)^x}$ 的最小值 。$(\text{20分})$   

解析：$(1)$ 设数列 $\{a_n\}$ 表示这 $k+2$ 个数，则有 $a_1=1,a_{k+2}=n$。    
由题意得 $\{a_n\}$ 是等比数列，又因为共有 $k+2$ 项且首尾项均已确定，所以容易得到 $a_i=\left(\sqrt[k+1]{n}\right)^{i-1}$。 $\cdots\cdots\text{(5分)}$   
则 $f(n,k)=\prod\limits_{i=1}^{k+2}a_i=\left(\sqrt[k+1]{n}\right)^{(0+1+\cdots+k+1)}=\left(\sqrt[k+1]{n}\right)^{\frac{(k+1)(k+2)}{2}}=n^{\frac{k+2}{2}}$。 $\cdots\cdots(\text{10分})$   
$(2)$ 首先计算 $g(x)$，我们有 $g(x)=\sum\limits_{i=1}^xf(2^{2i},x-2)=\sum\limits_{i=1}^x\left(2^i\right)^x=\sum\limits_{i=1}^x\left(2^x\right)^i$，由等比数列求和公式可知 $g(x)=\dfrac{\left(2^{x}\right)^{x+1}-2^x}{2^x-1}=\dfrac{2^x}{2^x-1}\left(2^{\left(x^2\right)}-1\right)$。 $\cdots\cdots\text{(10分)}$   
然后计算 $h(x)$，我们有 $h(x)=\sum\limits_{i=1}^{x-2}f(2^{2x},i)=\sum\limits_{i=1}^{x-2}\left(2^x\right)^{i+2}=\sum\limits_{i=3}^x\left(2^x\right)^i$，故 $g(x)-h(x)=2^x+4^x$。$\cdots\cdots\text{(15分)}$   
则 $\dfrac{g(x)-h(x)}{\left(2\sqrt2\right)^x}=\left(\sqrt2\right)^x+\dfrac{1}{\left(\sqrt2\right)^x}$。如果不考虑 $x$ 的取值范围，当 $x=0\;,\left(\sqrt2\right)^x=1$ 时原式取得最小值，但因为 $x\geq3$，所以当 $x=3$ 时，原式的最小值为 $\dfrac{9}{4}\sqrt2$。 $\cdots\cdots(\text{20分})$

------------

**2.** $\text{(40分)}$ 已知椭圆 $O_1:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\;,O_2:\dfrac{x^2}{b^2}+\dfrac{y^2}{a^2}=1(a>b)$，圆 $O$ 过椭圆 $O_1$ 和椭圆 $O_2$ 的四个交点，   
$(1)$ 求圆 $O$ 的方程。$(\text{5分})$   
$(2)$ 设椭圆 $O_1$ 与 $x$ 轴的左交点为 $A$，椭圆 $O_2$ 与 $y$ 轴的上交点为 $B$，椭圆 $O_1$ 与椭圆 $O_2$ 的左上交点为 $P$，   
$\ \ \ \ (\text{i})$ 若线段 $AB$ 过点 $P$，令椭圆 $O_1$ 与椭圆 $O_2$ 的右下交点为 $P'$，已知 $\overrightarrow{AP'}\cdot\overrightarrow{PB}=2$，求椭圆 $O_1$ 的焦点坐标。$(\text{15分})$   
$\ \ \ \ (\text{ii})$ 设点 $T$ 为原点，点 $Q$ 是 $\triangle ABT$ 内一点，若满足 $|QA|+|QB|+|QT|$ 的值最小的点 $Q$ 与点 $P$ 重合，求椭圆 $O_1$ 的离心率。$(\text{20分})$   

解析：$(1)$ 联立椭圆 $O_1$ 和椭圆 $O_2$ 的方程，可以解出 $\begin{cases}x^2=\dfrac{a^2b^2}{a^2+b^2}\\y^2=\dfrac{a^2b^2}{a^2+b^2}\end{cases}$。故圆 $O$ 的半径为 $\sqrt{\dfrac{2a^2b^2}{a^2+b^2}}$，方程为 $x^2+y^2=\dfrac{2a^2b^2}{a^2+b^2}$。 $\cdots\cdots\text{(5分)}$   
$(2)$ 首先，容易得到 $\triangle ABT$ 是等腰直角三角形，其腰长为 $a$。   
$(\text{i})$ 由线段 $AB$ 过点 $P$，可以得到 $TP=PA=\dfrac{\sqrt2}{2}a$，故 $\sqrt{\dfrac{2a^2b^2}{a^2+b^2}}=\dfrac{\sqrt2}{2}a,a=\sqrt3b$。 $\cdots\cdots\text{(5分)}$   
可以发现 $\overrightarrow{PB}=\overrightarrow{AP}$，并且线段 $AP$ 和线段 $AP'$ 的夹角的余弦值为 $\dfrac{\sqrt5}{5}$。因此考虑 $\overrightarrow{AP'}\cdot\overrightarrow{PB}=\dfrac{\sqrt5}{5}\times|\overrightarrow{AP'}|\times|\overrightarrow{AP}|=\dfrac{\sqrt5}{5}\times\dfrac{\sqrt{10}}{2}a\times\dfrac{\sqrt2}{2}a=\dfrac{a^2}{2}$，故可得 $a=2,b=\dfrac{2}{3}\sqrt3$。则 $c=\sqrt{a^2-b^2}=\dfrac{2}{3}\sqrt6$，椭圆 $O_1$ 的焦点坐标为 $\left(\dfrac{2}{3}\sqrt6,0\right)$ 和 $\left(-\dfrac{2}{3}\sqrt6,0\right)$。 $\cdots\cdots\text{(15分)}$   
$(\text{ii})$ 考虑满足条件的点 $Q$ 的坐标，我们构造一个等腰直角三角形 $ABC$：   
![](https://cdn.luogu.com.cn/upload/image_hosting/xx7xubju.png)   
如图，将 $\triangle AEB$ 顺时针旋转 $60\degree$，则有 $EA+EB+EC=CE+EE'+E'B\geq CB'$，当且仅当点 $E$ 在线段 $CB'$ 上且 $\angle EAB=45\degree$ 时，点 $C,E,E',B$ 四点共线，等号成立。此时有 $\angle ECA=15\degree$，故可以得到点 $Q$ 满足 $\angle QAT=15\degree$。 $\cdots\cdots\text{(5分)}$   
由于 $\dfrac{\sqrt3}{3}=\tan 30\degree=\dfrac{2\tan 15\degree}{1-\tan^2 15\degree}$，可以解出 $\tan 15\degree=2-\sqrt3$。设点 $Q$ 的坐标为 $(-t,t)$，则有 $\dfrac{t}{a-t}=2-\sqrt3$，解得点 $Q$ 的坐标为 $\left(-\dfrac{3-\sqrt3}{6}a,\dfrac{3-\sqrt3}{6}a\right)$。 $\cdots\cdots\text{(15分)}$   
由于点 $P$ 和点 $Q$ 重合，所以有 $\sqrt{\dfrac{a^2b^2}{a^2+b^2}}=\dfrac{3-\sqrt3}{6}a$，解得 $a^2=\left(6\sqrt3+11\right)b^2$。故椭圆 $O_1$ 的离心率为 $e=\dfrac{\sqrt{a^2-b^2}}{a}=\dfrac{\sqrt{78\sqrt{3}+26}}{13}$。 $\cdots\cdots\text{(20分)}$

------------

**3.** $\text{(50分)}$ 已知函数 $f(x)$ 表示 $t^x+\dfrac{x}{e^3t}\;(t>0)$ 的最小值，且 $x\in \mathbb{N}^+$，  
$(1)$ 求 $f(x)$ 的解析式。$(\text{5分})$   
$(2)$ 若 $p$ 表示 $f(x)$ 的最小值，求 $p$ 的值。$(\text{15分})$   
$(3)$ 若实数 $k$ 满足 $k+\ln p=\ln3$，令函数 $g(x)=\log_k\left(-24x^3+108x^2-144x+64\right)\;,\;h(x)=|a|x^2-2x+a$，若 $\exists x_1\in[1,2]$，使得方程 $h(x_2)=g(x_1)$ 在 $x_2\in[1,3]$ 时有解，求 $a$ 的取值范围。$(\text{30分})$   

解析：$(1)$ 由均值不等式，可得 $t^x+\dfrac{x}{e^3t}=t^x+\begin{matrix}\underbrace{\dfrac{1}{e^3t}+\cdots+\dfrac{1}{e^3t}}\\x\text{项}\end{matrix}\geq\left(x+1\right)\sqrt[x+1]{\left(\dfrac{1}{e^3}\right)^x}=\left(x+1\right)e^\frac{-3x}{x+1}$，当且仅当 $t=\sqrt[x+1]{\dfrac{1}{e^3}}$ 时，等号成立。故 $f(x)=\left(x+1\right)e^\frac{-3x}{x+1}$。 $\cdots\cdots\text{(5分)}$   
$(2)$ 首先计算 $f(x)$ 的导函数。设 $m(x)=x+1,n(x)=e^{\frac{-3x}{x+1}}$，则 $n(x)=e^{-3}e^{\frac{3}{x+1}}$，然后易得 $n'(x)=-\dfrac{3}{\left(x+1\right)^2}e^{\frac{-3x}{x+1}}$。故 $f'(x)=m'(x)n(x)+m(x)n'(x)=e^{\frac{-3x}{x+1}}-\dfrac{3}{x+1}e^{\frac{-3x}{x+1}}=\dfrac{x-2}{x+1}e^{\frac{-3x}{x+1}}$。 $\cdots\cdots\text{(10分)}$  
令 $f'(x)=0$，显然有此时 $x=2$。可以发现，$e^{\frac{-3x}{x+1}}$ 恒为正数，而在 $x<2$ 时，$\dfrac{x-2}{x+1}<0$，故可知 $f(x)$ 在 $[1,2]$ 上单调递减，在 $[2,+\infty)$ 上单调递增。则 $p=f(2)=\dfrac{3}{e^2}$。 $\cdots\cdots\text{(15分)}$   
$(3)$ 由 $k+\ln p=\ln3$，可得 $k=\ln3-\ln p=\ln \dfrac{3}{p}=2$，故 $g(x)=\log_2\left(-24x^3+108x^2-144x+64\right)$。   
设 $q(x)=-24x^3+108x^2-144x+64$，则 $q'(x)=-72x^2+216x-144$。令 $q'(x)=0$，可得 $x_1=1,x_2=2$。因为 $q'(x)$ 在 $[1,2]$ 上恒大于等于 $0$，所以 $q(x)$ 在 $[1,2]$ 上单调递增，从而 $g(x)$ 在 $[1,2]$ 上单调递增，故 $g(x)_{min}=g(1)=2,g(x)_{max}=g(2)=4$，题目中 $g(x_1)$ 的取值范围为 $[2,4]$。 $\cdots\cdots\text{(10分)}$   
要满足题目中的条件，只需使 $h(x_2)$ 的取值范围与 $\{x|2\leq x\leq4\}$ 的交集不为空集即可。下面分两种情况讨论：   
$1.$ 若 $a=0$，则 $h(x)=-2x$，在 $x_2\in[1,3]$ 时 $h(x)\notin[2,4]$，不满足条件。    
$2.$ 若 $a\neq0$，再分以下两种情况：   
① 若对称轴在 $[1,3]$ 范围内，即当 $\dfrac{1}{3}\leq|a|\leq1$ 时，有 $h(x_2)_{min}=h\left(\dfrac{1}{|a|}\right)=a-\dfrac{1}{|a|}$。由于此时 $a-\dfrac{1}{|a|}\leq0$，故只需考虑最大值是否大于等于 $2$ 即可。   
若 $\dfrac{1}{2}\leq|a|\leq1$，则 $h(x_2)_{max}=h(3)=a+9|a|-6$。令 $a+9|a|-6\geq2$，可得 $\dfrac{4}{5}\leq a\leq1$ 或 $a=-1$。   
若 $\dfrac{1}{3}\leq |a|<\dfrac{1}{2}$，则 $h(x_2)_{max}=h(1)=a+|a|-2$。令 $a+|a|-2\geq2$，可得此时无解。 $\cdots\cdots\text{(20分)}$   
② 若对称轴不在 $[1,3]$ 范围内，即当 $|a|<\dfrac{1}{3}$ 或 $|a|>1$ 时，此时最大最小值均在端点处取得。   
若 $|a|<\dfrac{1}{3}$，则对称轴在 $3$ 的右侧，故 $h(x_2)_{min}=h(3)=a+9|a|-6,h(x_2)_{max}=h(1)=a+|a|-2$。由于此时 $a+|a|-2<-\dfrac{4}{3}$，可得此时无解。   
若 $|a|>1$，则对称轴在 $1$ 的左侧，故 $h(x_2)_{min}=h(1)=a+|a|-2,h(x_2)_{max}=h(3)=a+9|a|-6$。令 $\begin{cases}a+|a|-2\leq4\\a+9|a|-6\geq2\end{cases}$ ，可得 $1<a\leq3$ 或 $a<-1$。   
综合以上所有情况，可得 $a$ 的取值范围为 $\{a|a\leq-1\text{或}\;\dfrac{4}{5}\leq a\leq3\}$。 $\cdots\cdots\text{(30分)}$   

------------

**4.** $\text{(60分)}$ 已知 $a$ 是无理数，集合 $Q(a)$ 满足： $\mathbb{Q}\subseteq Q(a),a\in Q(a)$ 且 $\forall x,y\in Q(a)$，$x+y,\dfrac{x}{y}\in Q(a)\;(y\neq0)$，   
$(1)$ 求证：若 $m,n,p,q$ 是不等于 $0$ 的有理数且 $\dfrac{m}{p}\neq\dfrac{n}{q}$，则 $\sqrt2\in Q\left(\dfrac{m+n\sqrt2}{p+q\sqrt2}\right)$。 $\text{(10分)}$   
$(2)$ 已知 $a\in\mathbb{Z}$，若方程 $ax^2+x-1=0$ 在 $x\in Q(\sqrt{13}+\sqrt{17})$ 时有解，求 $a$ 的所有可能取值构成的集合。 $\text{(50分)}$   

解析：$(1)$ 首先有 $\dfrac{m+n\sqrt2}{p+q\sqrt2}=\dfrac{\left(m+n\sqrt2\right)\left(p-q\sqrt2\right)}{p^2-2q^2}=\dfrac{\left(mp-2nq\right)+\left(np-mq\right)\sqrt2}{p^2-2q^2}$。因为 $m,n,p,q\in\mathbb{Q}$，有 $p^2-2q^2,mp-2nq,np-mq\in\mathbb{Q}$，且由题意可得 $np-mq\neq0,p^2-2q^2\neq0$。所以 $\sqrt2=\dfrac{\dfrac{m+n\sqrt2}{p+q\sqrt2}\times\left(p^2-2q^2\right)+\left(2nq-mp\right)}{np-mq}\in Q\left(\dfrac{m+n\sqrt2}{p+q\sqrt2}\right)$，故得证。 $\cdots\cdots\text{(10分)}$   
$(2)$ ①若 $a=0$，易知方程的解为 $x=1\in\mathbb{Q}$，符合题意。 $\cdots\cdots\text{(5分)}$   
②若 $a\neq0$，则需满足 $\triangle =1+4a\geq0$，得 $a\geq-\dfrac{1}{4}$，也即 $a\geq1$。   
此时方程的两个根为 $\dfrac{-1\pm\sqrt{4a+1}}{2a}$。若要满足题意，只需令 $\sqrt{4a+1}\in Q\left(\sqrt{13}+\sqrt{17}\right)$ 即可。   
首先考虑 $Q\left(\sqrt{13}+\sqrt{17}\right)$ 包含哪些形如 $\sqrt{4a+1}$ 的元素。因为 $\dfrac{1}{\sqrt{13}+\sqrt{17}}=\dfrac{\sqrt{17}-\sqrt{13}}{4}$，易知 $\sqrt{13},\sqrt{17}\in Q\left(\sqrt{13}+\sqrt{17}\right)$。进一步得到 $\sqrt{221}\in Q\left(\sqrt{13}+\sqrt{17}\right)$。此外所有形如 $\sqrt{4a+1}$ 的元素都一定可以化简成某个正整数乘以这三个元素的形式。 $\cdots\cdots\text{(15分)}$   
下面分四种情况讨论：   
$1.$ 若 $4a+1$ 是完全平方数，   
设 $k^2=4a+1$，则有 $a=\dfrac{k-1}{2}\times\dfrac{k+1}{2}$。此时易知 $k$ 是正奇数，故可设 $k=2k'+1$，则 $a=k'(k'+1)\;(k'\geq1)$。这种情况下 $a$ 的取值可以表示成集合 $S_1=\{x|x=t(t+1),t\in\mathbb{N^+}\}$。 $\cdots\cdots\text{(25分)}$   
$2.$ 若 $13$ 整除 $4a+1$，且 $\dfrac{4a+1}{13}$ 是完全平方数，   
首先考虑何时有 $13$ 整除 $4a+1$。当 $a=3$ 时有 $4a+1=13$，此后当且仅当 $a$ 增大 $13$ 时才能使 $13$ 再次整除 $4a+1$。故可设 $a=13k+3$ ($k$ 是非负整数)，则 $\dfrac{4a+1}{13}=4k+1$。   
由情况 $1$ 的结论，可知当 $4k+1$ 为完全平方数时满足 $k=k'(k'+1)\;(k'\geq1)$。同时当 $k=0$，即 $a=3$ 时也满足条件。故这种情况下 $a$ 的取值可以表示成集合 $S_2=\{x|x=13t(t+1)+3,t\in\mathbb{N}\}$。 $\cdots\cdots\text{(35分)}$   
$3.$ 若 $17$ 整除 $4a+1$，且 $\dfrac{4a+1}{17}$ 是完全平方数，   
类似情况 $2$，先考虑何时 $17$ 整除 $4a+1$。当 $a=4$ 时有 $4a+1=17$，此后当且仅当 $a$ 增大 $17$ 时才能使 $17$ 再次整除 $4a+1$。故可设 $a=17k+4$ ($k$ 是非负整数)，则 $\dfrac{4a+1}{17}=4k+1$。   
和情况 $2$ 一样，易得此时 $a$ 的取值可以表示成集合 $S_3=\{x|x=17t(t+1)+4,t\in\mathbb{N}\}$。 $\cdots\cdots\text{(40分)}$   
$4.$ 若 $221$ 整除 $4a+1$，且 $\dfrac{4a+1}{221}$ 是完全平方数，   
此时必须要同时满足 $13$ 整除 $4a+1$ 和 $17$ 整除 $4a+1$。当 $a=55$ 时有 $4a+1=221$，此后当且仅当 $a$ 增大 $221$ 时才能使 $221$ 再次整除 $4a+1$。故可设 $a=221k+55$ ($k$ 是非负整数)，则 $\dfrac{4a+1}{221}=4k+1$。   
和情况 $2,3$ 一样，易得此时 $a$ 的取值可以表示成集合 $S_4=\{x|x=221t(t+1)+55,t\in\mathbb{N}\}$。 $\cdots\cdots\text{(45分)}$   
最终结果即为集合 $S=S_1\cup S_2\cup S_3\cup S_4\cup\{0\}=\{x|x=t(t+1)\;\text{或}\;x=13t(t+1)+3\;\text{或}\;x=17t(t+1)+4\;\text{或}\;x=221t(t+1)+55,t\in\mathbb{N}\}$。 $\cdots\cdots\text{(50分)}$