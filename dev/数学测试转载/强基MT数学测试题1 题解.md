# [强基MT数学测试题1 题解](https://www.luogu.com/article/qcubgr9r)

### **一、填空题**

**1.** 已知抛物线 $x^2=2y$ 上有两点 $A\left(-2,2\right),B\left(4,8\right)$，若点 $P$ 是抛物线上一动点，则当 $\triangle ABP$ 是直角三角形时，点 $P$ 的坐标为\_\_\_\_\_\_\_\_\_\_\_\_\_。   

正确答案: $\left(0,0\right)$ 或 $\left(-6,18\right)$ 或 $\left(-1-\sqrt5,3+\sqrt5\right)$ 或 $\left(-1+\sqrt5,3-\sqrt5\right)$   

解析：当点 $A$ 或点 $B$ 是直角顶点时，易求出直线 $AB$ 的解析式为 $y=x+4$，直线 $AP$ 和 $BP$ 的斜率为 $-1$。由此可求出直线 $AP$ : $y=-x$，直线 $BP$ : $y=-x+12$。解方程可得 $\left(0,0\right)$ 和 $\left(6,18\right)$ 这两解。   
当点 $P$ 是直角顶点时，设点P的坐标为 $\left(a,\dfrac{a^2}{2}\right)$，则直线 $AP$ 的斜率为 $\dfrac{\dfrac{a^2}{2}-2}{a+2}=\dfrac{a-2}{2}$，直线 $BP$ 的斜率为 $\dfrac{\dfrac{a^2}{2}-8}{a-4}=\dfrac{a+4}{2}$。令 $\dfrac{a-2}{2}\times\dfrac{a+4}{2}=-1$，解出 $a=-1-\sqrt5$ 或 $a=-1+\sqrt5$，则点 $P$ 的坐标为 $\left(-1-\sqrt5,3+\sqrt5\right)$ 或 $\left(-1+\sqrt5,3-\sqrt5\right)$。   
   

------------

**2.** 若实数 $x$、$y$ 满足 $x+y=1$ 且 $x^3+y^3=\dfrac{5}{2}$ ，则 $x^2+y^2$ 的值为\_\_\_\_\_\_\_\_\_\_\_。   

正确答案：$2$   

解析：$x^3+y^3=\left(x+y\right)\left(x^2-xy+y^2\right)=x^2-xy+y^2=\left(x+y\right)^2-3xy=1-3xy=\dfrac{5}{2}$，因此 $xy=-\dfrac{1}{2}$。则 $x^2+y^2=\left(x+y\right)^2-2xy=2$。   


------------

**3.** 已知一等差数列 $\{a_n\}$，$\{S_n\}$ 表示该等差数列前 $n$ 项的和。若 $S_1S_{25}=S_5^2$ 且 $S_3=6$，则 $a_1^d$=\_\_\_\_\_\_\_\_\_\_\_。   

正确答案：$\dfrac{2}{9}\sqrt[3]{18}$ 或 $1$   

解析：易得 $S_n=na_1+\dfrac{n\left(n-1\right)}{2}d$，则由题意可列方程   
$$\begin{cases}a_1\left(25a_1+300d\right)=\left(5a_1+10d\right)^2\\3a_1+3d=6\end{cases}$$
解该方程组，得 $\begin{cases}a_1=\dfrac{2}{3}\\d=\dfrac{4}{3}\end{cases}$ 或 $\begin{cases}a_1=2\\d=0\end{cases}$   
注意：根据等差数列的定义，当 $d=0$ 时仍然可以认为是一个等差数列。因此答案即为 $\left(\dfrac{2}{3}\right)^{\dfrac{4}{3}}$ 或 $2^0$，即 $\dfrac{2}{9}\sqrt[3]{18}$ 或 $1$。


------------

**4.** 已知 $m,a_i\in\mathbb{N}^+\;\left(i=1,2,3,\cdots,11\right)$，若 $\sqrt{m+20\sqrt2}=\sum\limits_{i=1}^{11}\sqrt{a_i}$，则 $m+\sum\limits_{i=1}^{11}a_i$ 的值为\_\_\_\_\_\_\_\_\_\_\_。

正确答案：$114$ 或 $222$

解析：显然要使所有数均为正整数，$a_i$ 的值只能是 $1$ 或 $2$，否则必然要有某个 $a_i$ 的值为不为正数 (比如令某个 $a_i=4$，则剩下 $10$ 个数字无论怎样配也不可能使其平方后得到 $20\sqrt2$ )，或者 $m$ 是无理数 (比如出现了 $a_i=3$ 或 $a_i=5$ 之类的情况)。   
因此，可以构造两种情况，即 $a_1=a_2=\cdots=a_{10}=1,a_{11}=2$ 或 $a_1=a_2=\cdots=a_{10}=2,a_{11}=1$，分别求出 $m+\sum\limits_{i=1}^{11}a_i$ 的值为 $114$ 和 $222$。


------------

**5.** 若一个整系数六次方程的一个根为 $\sqrt2+\sqrt[3]{2}$，则这个六次方程为
\_\_\_\_\_\_\_\_\_\_\_。（化简成 $f\left(x\right)=0$ 的形式）

正确答案：$x^6-6x^4-4x^3+12x^2-24x-4=0$   

解析：令 $x=\sqrt2+\sqrt[3]2$，则有   
$$\begin{aligned}x-\sqrt{2}&=\sqrt[3]{2}\\\left(x-\sqrt2\right)^3&=2\\x^3-3\sqrt2x^2+6x-2\sqrt2&=2\\x^3+6x-2&=\sqrt2\left(3x^2+2\right)\\\left(x^3+6x-2\right)^2&=2\left(3x^2+2\right)^2\end{aligned}$$
化简，最终得到 $x^6-6x^4-4x^3+12x^2-24x-4=0$。


------------

**6.** 已知集合 $S\subseteq\left\{1,2,3,\cdots,100\right\}$，若从集合 $S$ 中取出任意三个互不相同的元素，这三个数的最大公因数都是 $1$，则 $|S|$ 的最大值为\_\_\_\_\_\_\_\_\_\_\_。  

正确答案：$30$  

解析：由题目条件可知，集合 $S$ 中的所有元素的质因数不能有任何一个出现超过两次。因此可以先加入所有的质数 (即 $2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97$ 共 $25$ 个) 。并且 $1$ 显然可以加进去。考虑到这些质因数可以再出现一次，因此可以构造是多个质数乘积的合数。若要使方案最优，则应选择 $2^2,3^2,5^2,7^2$。所以 $|S|$ 的最大值为 $25+1+4=30$。


------------

**7.** 如图，在 $Rt\triangle ABC$ 中，$\angle C=90\degree,\angle BAD=45\degree,AC=3,BD=5$，则 $AB$ 的长度为\_\_\_\_\_\_\_\_\_\_\_。![](https://cdn.luogu.com.cn/upload/image_hosting/o64qn9wk.png)

正确答案：$3\sqrt5$

解析：  
### 方法1：   
![](https://cdn.luogu.com.cn/upload/image_hosting/y9anixux.png)   
如图，做 $DE\perp AB$，延长 $ED$ 和 $AC$ 交于点 $F$。易证 $\angle B=\angle F$，再由 $AE=ED,\angle DEA=\angle DEB=90\degree$ 可得 $\triangle AEF\cong\triangle EDB$。所以 $AF=BD=5,CF=2$。易证 $\triangle CDF\sim\triangle ABC$，所以 $\dfrac{CD}{AC}=\dfrac{CF}{BC}$，即 $\dfrac{CD}{3}=\dfrac{2}{5+CD}$，解得 $CD=1$ 或 $-6$ (舍去)。故 $AB=\sqrt{AC^2+BC^2}=\sqrt{3^2+\left(5+1\right)^2}=3\sqrt5$。

### 方法2：   
设 $CD=x$，则 $\tan\angle DAC=\dfrac{x}{3},\tan\angle BAC=\dfrac{x+5}{3}$。根据公式 $\tan\left(a+b\right)=\dfrac{\tan a+\tan b}{1-\tan a\tan b}$ 可列方程 $\dfrac{x+5}{3}=\dfrac{1+\dfrac{x}{3}}{1-\dfrac{x}{3}}$，解得 $x=1$ 或 $-6$ (舍去)。也可得到 $AB=\sqrt{AC^2+BC^2}=\sqrt{3^2+\left(5+1\right)^2}=3\sqrt5$。


------------

**8.** 将 $x^8-4x^2+3$ 因式分解得\_\_\_\_\_\_\_\_\_\_\_。   
   
正确答案：$\left(x-1\right)^2\left(x+1\right)^2\left(x^4+2x^2+3\right)$   

解析：   
$\begin{aligned}x^8-4x^2+3&=\left(x^8-x^6\right)+\left(x^6-x^4\right)+\left(x^4-x^2\right)-3\left(x^2-1\right)\\
&=x^6\left(x^2-1\right)+x^4\left(x^2-1\right)+x^2\left(x^2-1\right)-3\left(x^2-1\right)\\&=\left(x^6+x^4+x^2-3\right)\left(x^2-1\right)\\&=
\left[x^4\left(x^2+1\right)+2\left(x^2-1\right)-\left(x^2+1\right)\right]\left(x^2-1\right)\\&=\left[\left(x^4-1\right)\left(x^2+1\right)+2\left(x^2-1\right)\right]\left(x^2-1\right)\\&=\left(x^2-1\right)^2\left(x^4+2x^2+3\right)\\&=\left(x-1\right)^2\left(x+1\right)^2\left(x^4+2x^2+3\right)\end{aligned}$   


------------

**9.** 已知点 $D$ 是线段 $BC$ 的中点，$\angle CAD=15\degree$，则 $\angle ABC$ 的最大值为\_\_\_\_\_\_\_\_\_\_\_。

正确答案：$105\degree$

解析：   
![](https://cdn.luogu.com.cn/upload/image_hosting/cmiafsha.png)   
由于 $\angle CAD=15\degree$，易得点 $A$ 的运动轨迹在一个圆上，这个圆的圆心 $O$ 在 $CD$ 的中垂线上且 $\angle COD=30\degree$。显然当 $\angle ABC$ 最大时，$BA$ 与圆 $O$ 相切。因此可以得到上图。   
由圆幂定理得 $\triangle ABD\sim\triangle ABC$，故 $BA^2=BD\times BC=2BD^2$，$\dfrac{BA}{BD}=\dfrac{AC}{AD}=\sqrt2$。由于 $\angle CAD=15\degree$，在 $\triangle ADC$ 中设 $\angle ACD=\alpha$，则 $\angle ADC=165\degree-\alpha$。由正弦定理可得 $\dfrac{\sin\angle ADC}{\sin\angle ACD}=\dfrac{AC}{AD}$，即 $\begin{aligned}\dfrac{\sin\left(165\degree-\alpha\right)}{\sin\alpha}&=\sqrt2\\\sin165\degree\cos\alpha-\sin\alpha\cos165\degree&=\sqrt2\sin\alpha\\\sin15\degree\cos\alpha+\sin\alpha\cos15\degree&=\sqrt2\sin\alpha\\\sin15\degree+\cos15\degree\tan\alpha&=\sqrt2\tan\alpha\\\tan\alpha&=\dfrac{\sin15\degree}{\sqrt2-\cos15\degree}\\&=\dfrac{\left(\sqrt{\dfrac{1-\dfrac{\sqrt3}{2}}{2}}\right)}{\left(\sqrt2-\sqrt{\dfrac{1+\dfrac{\sqrt3}{2}}{2}}\right)}\\&=\dfrac{\sqrt3}{3}\end{aligned}$   
所以 $\angle ACD=30\degree$，进而得 $\angle AOD=2\angle ACD=60\degree,\angle ABC=360\degree-\angle AOD-\angle DOC-\angle OCB-\angle OAB=105\degree$。

------------

**10.** 函数 $f\left(x\right)=x^2-2x+\sqrt x$ 有\_\_\_\_\_\_\_\_\_\_\_个零点。   

正确答案：$3$   

解析：令 $f\left(x\right)=0$，可得   
$\begin{aligned}x^2-2x+\sqrt{x}&=0\\x^2-2x&=-\sqrt{x}\\x^2\left(x-2\right)^2&=x\\x^4-4x^3+4x^2-x&=0\\x\left(x-1\right)\left(x^2-3x+1\right)&=0\end{aligned}$   
解得 $x=0$ 或 $1$ 或 $\dfrac{3\pm\sqrt5}{2}$。但因为在变换的第二步中，$-\sqrt{x}\leq0$，所以必须要$x^2-2x\leq0$，从而舍去 $x=\dfrac{3+\sqrt5}{2}$。所以有 $3$ 个零点。

------------

### **二、解答题**
**11.** 如图所示，在矩形 $ABCD$ 中，$AD=3cm$，$CD=12cm$。点 $P$、$Q$ 同时从点 $D$ 出发，分别以 $1cm/s$ 和 $2cm/s$ 的速度沿射线 $DC$ 运动。当点 $P$ 运动到点 $C$ 时，$P$、$Q$ 两点同时停止运动。以 $PQ$ 为底向上做等边三角形 $PQR$。设点 $P$、$Q$ 的运动时间为 $t\left(s\right)\;\left(0<t<12\right)$，   
$\left(1\right)$ 当 $t$ 为何值时，$B$ 在 $RQ$ 的中垂线上？ $\left(3\text{分}\right)$   
$\left(2\right)$ 当 $t$ 为何值时，$\triangle DRB$ 是直角三角形？ $\left(6\text{分}\right)$   
$\left(3\right)$ 设 $\triangle PQR$ 与矩形 $ABCD$ 重合的部分的面积为 $S$，**直接写出** $S$ 与 $t$ 的关系式并写出 $t$ 的取值范围。 $\left(15\text{分}\right)$![](https://cdn.luogu.com.cn/upload/image_hosting/nz64hc8x.png)   

正确答案：$(1)\;t=12-3\sqrt3\;\;\;(2)\;t=6+\dfrac{\sqrt3}{2}\;\text{或}\;\dfrac{408-34\sqrt3}{47}$   
$(3)\;S=\begin{cases}\dfrac{\sqrt3}{4}t^2\left(0<t\leq2\sqrt3\right)\\3t-3\sqrt3\left(2\sqrt3<t\leq6\right)\\-2\sqrt3t^2+\left(24\sqrt3+3\right)t-75\sqrt3\left(6<t\leq6+\dfrac{\sqrt3}{2}\right)\\-3t+36-\dfrac{3\sqrt3}{2}\left(6+\dfrac{\sqrt3}{2}<t\leq12-\sqrt3\right)\\\dfrac{\sqrt3}{2}t^2-12\sqrt3t+72\sqrt3\left(12-\sqrt{3}<t<12\right)\end{cases}$   

解析：$(1)$ 由 $\triangle RPQ$ 是等边三角形，可知点 $P$ 也在 $RQ$ 的中垂线上，所以此时 $BP$ 即为 $RQ$ 的中垂线。由三线合一，可知 $RQ$ 的中垂线就是 $\angle RPQ$ 的角平分线，所以此时 $\angle BPC=30\degree$，$\sqrt3BC=CP$。所以 $3\sqrt3=12-t\;$，解得 $\;t=12-3\sqrt3$。   

$(2)$ ①若 $\angle RDB=90\degree$，显然这不可能。   
②若 $\angle DRB=90\degree$，![](https://cdn.luogu.com.cn/upload/image_hosting/faxy7hhf.png)   
因为 $DP=RP=PQ$，易证 $\angle DRQ=90\degree$。而且 $\angle DRB=90\degree$，所以点 $R,B,Q$ 三点共线。所以有 $\sqrt3CQ=BC$，$\sqrt3\left(2t-12\right)=3$。解得 $t=6+\dfrac{\sqrt3}{2}$。   
③若 $\angle DBR=90\degree$，作 $RS\bot AB$，![](https://cdn.luogu.com.cn/upload/image_hosting/n0u8q2yz.png)   
由 $\angle DBR=\angle BAD=90\degree$，易证 $\angle ABD=\angle BRS$，所以 $\triangle RBS\sim\triangle ABD,\dfrac{BS}{AD}=\dfrac{RS}{AB}$。易知 $RS=\dfrac{\sqrt3}{2}t-3,BS=12-\dfrac{3}{2}t$，所以得 $\dfrac{12-\dfrac{3}{2}t}{3}=\dfrac{\dfrac{\sqrt3}{2}t-3}{12}$，解得 $t=\dfrac{51}{6+\dfrac{\sqrt3}{2}}=\dfrac{102}{12+\sqrt3}=\dfrac{102\left(12-\sqrt3\right)}{141}=\dfrac{408-34\sqrt3}{47}$。   

$(3)$ 设 $S$ 表示 $\triangle RPQ$ 与矩形 $ABCD$ 的重叠部分的面积，   
①若点 $R$ 在线段 $AB$ 下方，即 $0<t\leq2\sqrt3$ 时，![](https://cdn.luogu.com.cn/upload/image_hosting/clgmgv4x.png)   
此时 $S=S_{\triangle RPQ}=\dfrac{\sqrt3}{4}t^2$。   
②若点 $R$ 在线段 $AB$ 上方，且线段 $RQ$ 与线段 $BC$ 没有交点，即 $2\sqrt3<t\leq6$ 时，![](https://cdn.luogu.com.cn/upload/image_hosting/knmkli2y.png)   
此时 $S=S_{\text{梯形}PEFQ}=\dfrac{1}{2}\times3\left(t+t-2\sqrt3\right)=3t-3\sqrt3$。   
③若点 $R$ 在线段 $AB$ 上方，且线段 $RQ$ 与线段 $BC$ 和线段 $AB$ 都有交点，即 $6<t\leq6+\dfrac{\sqrt3}{2}$ 时，![](https://cdn.luogu.com.cn/upload/image_hosting/9k4ta2u7.png)   
此时 $S=S_{\text{五边形}PEFGC}=S_{\text{梯形}PEFQ}-S_{\triangle GCQ}=3t-3\sqrt3-\dfrac{\sqrt3\left(2t-12\right)^2}{2}=-2\sqrt3t^2+\left(24\sqrt3+3\right)t-75\sqrt3$。   
④若点 $R$ 在线段 $AB$ 上方，且线段 $RQ$ 与线段 $AB$ 有交点、与线段 $BC$ 无交点，即 $6+\dfrac{\sqrt3}{2}<t\leq12-\sqrt3$ 时，![](https://cdn.luogu.com.cn/upload/image_hosting/055nmvau.png)  
此时 $S=S_{\text{梯形}PEBC}=\dfrac{1}{2}\times3\left(12-t+12-t-\sqrt3\right)=-3t+36-\dfrac{3\sqrt3}{2}$。   
⑤若点 $R$ 在线段 $AB$ 上方，且线段 $RP$ 与线段 $BC$ 有交点，即 $12-\sqrt3<t\leq12$ 时，![](https://cdn.luogu.com.cn/upload/image_hosting/0j3ve7ef.png)   
此时 $S=S_{\triangle PCH}=\dfrac{\sqrt3\left(12-t\right)^2}{2}=\dfrac{\sqrt3}{2}t^2-12\sqrt3t+72\sqrt3$。

------------

**12.** 已知函数 $f\left(x\right)=\dfrac{4x^2}{x^4+1}$ 的最大值为 $k$。   
$(1)$ 已知正方形 $ABCD$ 的边长为 $k$，若正方形内有一点 $P$，试求 $PA+PB+PD$ 的最小值。 $\left(12\text{分}\right)$   
$(2)$ 已知 $a$ 是负实数，方程 $ax^2+k^2\left(a-1\right)x+\left(a^2+2k^2a-9\right)=0$ 没有实数根，且函数 $f\left(x\right)=\left(\dfrac{x^2}{k}-\dfrac{x}{a}+1\right)\left(-ax^2+kx+1\right)$ 的最小值为 $\dfrac{7}{16}$，试求出以 $-a$ 为边长的正五边形的面积。 $\left(24\text{分}\right)$    

正确答案：$(1)\;\sqrt6+\sqrt2\;\;\;(2)\;\sqrt{25+10\sqrt5}$   

解析：首先我们求出 $k$ 的值，因为 $f(x)=\dfrac{4x^2}{x^4+1}=\dfrac{4}{x^2+\dfrac{1}{x^2}}$，而 $x^2+\dfrac{1}{x^2}\geq2$，所以 $f(x)\leq2$，即 $k=2$。   

$(1)$ 如图，将 $\triangle APB$ 顺时针旋转 $60\degree$ 到 $\triangle AP'E$，连接 $DE,PP'$，![](https://cdn.luogu.com.cn/upload/image_hosting/1b482j3o.png)   
显然有 $PA+PB+PD=PD+PP'+P'E$，而当点 $P$ 在线段 $DE$ 上且 $\angle PAB=45\degree$ 时，有 $D,P,P',E$ 四点共线。所以题目所求即为 $DE=\sqrt{\left(2+\sqrt3\right)^2+1^2}=\sqrt2+\sqrt6$。   

$(2)$ 因为方程 $ax^2+4\left(a-1\right)x+\left(a^2+8a-9\right)=0$ 没有实数根，所以 $\triangle=16\left(a-1\right)^2-4a\left(a^2+8a-9\right)<0$，化简后得 $(a-1)(a+1)(a+4)>0$，解得 $-4<a<-1\;\text{或}\;a>1$，但 $a$ 是负实数，所以 $-4<a<-1$。   
函数 $f\left(x\right)=\left(\dfrac{x^2}{2}-\dfrac{x}{a}+1\right)\left(-ax^2+2x+1\right)$ 的最小值为 $\dfrac{7}{16}$，注意到这个函数的两个因式都是二次项系数 $>0$ 的二次函数，且对称轴都是直线 $x=\dfrac{1}{a}$，所以 $f(x)$ 的最小值为 $f\left(\dfrac{1}{a}\right)=\left(-\dfrac{1}{2a^2}+1\right)\left(\dfrac{1}{a}+1\right)$。令该式 $=\dfrac{7}{16}$，在 $-4<a<-1$ 时试根，可以发现 $a=-2$。   
最后求边长为 $2$ 的正五边形的面积。如图，令点 $O$ 为正五边形的几何中心，![](https://cdn.luogu.com.cn/upload/image_hosting/43l3uy3g.png)   
显然该正五边形的面积 $=5S_{\triangle BOC}$，而 $\triangle BOC$ 是一个底边长为 $2$、顶角为 $72\degree$、底角为 $54\degree$ 的等腰三角形。注意到 $S_{\triangle BOC}=\dfrac{1}{2}\times2\times\tan54\degree=\tan54\degree=\cot36\degree$，我们构造一个顶角为 $36\degree$、底角为 $72\degree$ 的等腰三角形：![](https://cdn.luogu.com.cn/upload/image_hosting/zozktghy.png)   
如图，设 $AB=BD=CD=1,AD=x$，易证 $\triangle ABD\sim\triangle ABC$，所以 $\dfrac{x}{1}=\dfrac{1}{x+1},x=\dfrac{\sqrt5-1}{2}$。则 $\cot36\degree=\dfrac{1+\dfrac{\sqrt5-1}{4}}{\sqrt{1^2-\left(\dfrac{\sqrt5-1}{4}\right)^2}}=\dfrac{\sqrt{25+10\sqrt5}}{5}$，故边长为 $2$ 的正五边形的面积为 $\sqrt{25+10\sqrt5}$。