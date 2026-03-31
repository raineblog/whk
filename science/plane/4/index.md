# 三角函数例题

## 例题一

2cos22B​+3​sinB=3

- 求 *B*.

cosB=2cos22B​−1cosB+3​sinB=223​​sinB+21​cosB=1sinBcos30∘+cosBsin30∘=1sin(B+30∘)=1=sin90∘B=60∘

## 例题二

(sinB−sinC)2=sin2A−sinBsinC

- 求 *A*.
- 若 $\\sqrt2a + b= 2c$，求 *C*.

观察到是角的二次齐次式，且都是正弦，考虑正弦定理，

(sinB−sinC)2=sin2A−sinBsinC(b−c)2=a2−bcb2+c2−2bc=a2−bca2=b2+c2−bc

于是，

cosA=2bcb2+c2−a2​=21​A=60∘

观察到 2​a+b=2c 为边的一次齐次，考虑用正弦定理。

2​a+b=2c2​sinA+sinB=2sinC

根据上一问，sinA=sin60∘=3​/2，

6​/2+sinB=2sinC6​/2+sin(120−C)=2sinC6​/2+3​/2cosC+sinC/2=2sinC

继续整理，

26​​+23​​cosC+21​sinC=2sinC23​sinC−23​​cosC=26​​23​​sinC−21​cosC=22​​sinCcos30∘−cosCsin30∘=22​​sin(C−30∘)=22​​=sin45∘

因为 C∈(0∘,120∘)，C−30∘∈(−30∘,90∘)，因此，

C−30∘=45∘, C=75∘

## 例题三

在锐角 △ABC 中，

2bsinA−3​a=0

- 求 *B*.
- 求 cos *A* + cos *B* + cos *C* 的取值范围。

不考虑 sinA 是边的二次齐次式，于是应用正弦定理，

2sinBsinA−2​sinA=02sinB=3​sinB=3​/2

因为 ∠B 是锐角，

B=60∘

设，

S​=cosA+cosB+cosC=cosA+cosC+1/2=cos(120∘−C)+cosC+1/2=−21​cosC+23​​sinC+cosC+21​=23​​sinC+21​cosC+21​=sinCcos30∘+cosCsin30∘+1/2=sin(C+30∘)+1/2​

因为 0∘\<A,B,C\<90∘，

{0∘\<0∘\<​CB​\<90∘\<90∘​⟺{0∘\<0∘\<​C120−C​\<90∘\<90∘​

即，30∘\<C\<90∘，60∘\<C+30∘\<120∘。

画出单位圆，易得 sin(C+30∘)∈(3​/2,1\]，即，

cosA+cosB+cosC∈(23​+1​,23​\]

## 例题四

在 △ABC 中，a+b=11，

cosA=81​,cosB=169​

- 求 *a*, *b*。

考虑余弦转正弦，因为是三角形的角，因此正弦值非负，

sinA=1−cos2A​=6463​​=837​​sinB=1−cos2B​=256175​​=1657​​

ba​=sinBsinA​=56​

因此 a=6,b=5。

## 例题五

sinB−sinCsinA​=b−ab+c​

- 求 cos *C*。

考虑 cosC 可以怎么表示，可以通过 sinC 用毕达哥拉斯定理，也可以余弦定理。

考虑到这个原形式是一次齐次，因此考虑角化变。

b−ca​=b−ab+c​b2−c2=ab−a2c2=a2+b2−ab

因此，

cosC=2bca2+b2−c2​=21​

## 例题六

若，

⎩⎨⎧​sinA=3sinBc=5​cosC=5/6​

- 求 *a*。

尝试考虑这三个东西各自什么用。

最容易发现第二个式子最简单，可以最后带入用。

因为 cos 关于余弦定理，关于边数多，因此考虑后用。

第一个式子结构很好，是一次齐次，因此带入第一个正弦定理。

a=3b

又因为，

cosC=2aba2+b2−c2​

带入即可，解得 a=3。

## 例题七

若，

{bsin2A=asinBc=2b​

- 求 *a*/*b*。

考虑到第二个式子的形式很简单，因此用于消元。

第一个形式中，出现了二倍角，是不好处理的，因此考虑正弦定理。

sinBsin2A=sinAsinBsinA=sin2AsinA=2sinAcosAcosA=1/2

考虑到 a/b 是一个一次其次的比例式，因此余弦定理，

cosA=2bcb2+c2−a2​

带入，解得 a2=3b2，即 a/b=3​。

## 例题八

在 △ABC 中，

S=a2−(b−c)2

求 sinA。

这个式子没有很好的性质，考虑展开，

S=a2−b2−c2+2bc

注意到这个形式，而且还是二次齐次式，根据余弦定理，

a2=b2+c2−2bccosA

有，

S=2bc(1−cosA)=21​bcsinAsinA=4−4cosA

联立得方程，

(4−4cosA)2+cos2A=116(1−cosA)2=(1−cosA)(1+cosA)16−16cosA=1+cosAcosA=1715​,sinA=178​

## 例题九

在 △ABC 中，

sinA=2sinBcosCa2=b2+c2−bc

- 求，△*A**B**C* 形状。

两个式子都很典型，第二个好说，先处理，

联立二式及余弦定理，

a2=b2+c2−bca2=b2+c2−2bccosA

得，

cosA=21​,A=60∘

第一个式子，可以不带入 A，尝试通过三角函数的变换，

sinA​=sin(π−B−C)=sin(B+C)=sinBcosC+cosBsinC​

联立下式及一式，

sinBcosC+cosBsinC=2sinBcosCsinBcosC=cosBsinCtanB=tanC

因为 B,C∈(0,π)，正切函数在此范围内唯一，则

B=C=A=60∘

即 △ABC 是正三角形。

## 例题十

在 △ABC 中，

cos(2B+C)+cosC>0

- 判断三角形是锐角、直角、钝角三角形。

容易发现，cos 里面的角有很好的性质，考虑和差化积，

==​cos(2B+C)+cosC2cos(B+C)cosB−2cosAcosB>0​

因此，

cosAcosB\<0

即 A,B 中有一个钝角，即 △ABC 为钝角三角形。

## 例题十一

在 △ABC 中，三边长分别为 a,a+2,a+4，最小角余弦值为 13/14。

- 求该三角形的面积

因为大边对大角，因此最小角是 a 对的，

cosA=2(a+2)(a+4)(a+2)2+(a+4)2−a2​=1413​

解得，a=3，于是用海伦公式，

p=23+5+7​=215​

S=215​⋅29​⋅25​⋅21​​=4153​​

## 例题十二

在 △ABC 中，∠A=120∘，BC=6。

- 求：其面积最大值。

考虑面积可以怎么表示。

Solution 1:

S=21​bcsinA=43​​bc

根据余弦定理，

36=a2=b2+c2−2bccosA=b2+c2+bc≥3bc

即，

bc≤12,S≤33​

Solution 2:

考虑到顶角不变，则可以固定底边，使顶点移动。

易知其轨迹为一个圆弧，则面积最大即底边高线最大。

高线最大即该三角形为等腰三角形，做出高线，

S=21​ah=33​

## 例题十三

在 △ABC 中，若

a−b=c(cosB−cosA)

- 判断其形状。

考虑到余弦定理展开后是三次式，有点复杂，因此正弦定理。

sinA−sinB=sinCcosB−sinCcosA

考虑凑项，右边的两项很像正弦的和角公式，于是，

==​sin(B+C)−sin(A+C)sinBcosC+sinCcosB−sinAcosC−sinCcosAsinCcosB−sinCcosA​

化简，

(sinB−sinA)cosC=0

即 sinA=sinB 或 cosC=0，

即 △ABC 为等腰三角形或直角三角形。

## 例题十四

若 △ABC 中，∠C 为钝角，且其面积，

S=43​​(a2+c2−b2)

- 求 ∠*B*。

考虑到 a2+c2−b2 是经典掉牙的形式，

cosB=2aca2+c2−b2​

于是，

S=43​​⋅2accosB=23​​accosB

考虑很经典的面积公式，

S=21​acsinB=23​​accosBsinB=3​cosBtanB=3​,B=60∘

## 例题十五

在 △ABC 中，

sin2A−sin2B−sin2C=sinBsinC

- 求 *A*.
- 若 *B\*\*C* = 3，求其周长最大值。

因为是正弦的二次齐次式，考虑正弦定理，

a2=b2+c2+bc

于是 ∠A=120∘。

考虑周长最大，即 b+c 最大，

a2=9=b2+c2+bc≥3bcbc≤3

考虑周长如何建立联系

b+c=b2+c2+2bc​=9+bc​≤23​

即周长，

a+b+c≤23​+3

## 例题十六

在 △ABC 中，

sinA+2sinBcosC=0c=3​b

- 求 tan *A*。

考虑到第二个很适合消元 c，于是第一个式子可以看成一次齐次，

a+2bcosC=0cosC=−2ba​=2bca2+b2−c2​=2bca2−2b2​

因此，

a2=b2a=b

因为 c=3​b，这是一个 30∘,30∘,120∘ 的等腰三角形，

tanA=tan30∘=33​​

## 例题十七

在 △ABC 中，

a2+b2=2022c2

求，

tanC(tanA+tanB)2tanAtanB​

考虑到没有什么好玩的结构，因此展开正切。

S​=tanC(tanA+tanB)2tanAtanB​=sinC/cosC⋅(sinAcosB+cosA+sinB)2sinAsinB​=sin2C2sinAsinBcosC​​

考虑到上下正弦构成二次齐次，正弦定理，

S​=sin2C2sinAsinBcosC​=c22abcosC​​

注意到 2ab 和 cosC 的余弦定理的分母类似，

cosC=2aba2+b2−c2​

S​=c2a2+b2−c2​=c2a2+b2​−1=2022−1=2021​

## 例题十八

在锐角三角形 ABC 中，a2−b2=bc。

求证：A=2B。

经典题，因为角不好表示，上式又是边的二次齐次式，考虑，

cosA=2bcb2+c2−a2​=2bcc2−bc​=2bc−b​

cos2B​=2cos2B−1=2(2aca2+c2−b2​)2−1=2(2ac+b​)2−1=4a22c2+2b2+4bc−4a2​=4b2+4bc2c2−2b2​=4b(b+c)2(c+b)(c−b)​=2bc−b​​

于是，

(cosA=cos2B)⟹(A=2B)

[RainPPR](mailto:PPR2125773894@163.com),  [Bot](mailto:bot@noreply.github.com)
