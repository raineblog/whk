# 集合与逻辑

## 基础知识

### 集合的定义

集合：

- 某些指定的对象集在⼀起就形成⼀个集合（简称集）。
- 元素：集合中每个对象叫做这个集合的元素。

集合的三要素：

- 确定性：集合内的元素是可以被确定的。
- 互异性：集合内的各元素都是唯⼀不重复的。
- ⽆序性：集合内的各元素的顺序是没有限制的。

子集与空集：

- 子集：A \\subseteq B 或 B \\supseteq A，表示 A 中的任意元素都属于 B

  A \\subseteq A, \\varnothing \\subseteq A

  A \\subseteq B 且 B \\subseteq C \\implies A \\subseteq C

  A \\subseteq B 且 B \\subseteq A \\implies A=B

- 真子集：A \\subsetneqq B 或 B \\supsetneqq A，表示 A \\subseteq B 且 B 中至少有一元素不属于 A

  A \\subsetneqq B 且 B \\subsetneqq C \\implies A \\subsetneqq C

- 空集（\\varnothing）是任何集合的子集，是任何非空集合的真子集。

- 有 n 个元素的集合，有 2^n 个子集，2^n-1 个真子集，2^n-1 个非空子集，2^n-2 个非空真子集。

- 空集只有一个子集，没有真子集、非空子集、非空真子集。

集合的表示：

- 列举法：{a,b}（a\\neq b）。
- 描述法：{x\\mid x=f(t), p(t)}。
- 符号法：\\R 实数集，\\C 复数集，\\Q 有理数集，\\N 自然数集，\\Z 整数集，\\P 质数集。右上角加星号（\*）表示去零，右下角加正、负号表示取正、负。
- 图示法：Venn（维恩）图。

### 集合的运算

表示某一元素属于某个集合时，用 \\in，例如 1 \\in {1, 2, 3}。若不属于则用 \\notin。

1. 并集：A = {2, 3, 4}, B = {1, 2, 3}, A \\cup B = {1, 2, 3, 4}。
1. 交集：A = {2, 3, 4}, B = {1, 2, 3}, A \\cap B = {2, 3}。
1. 补集：U = {1, 2, 3}, A \\subseteq U, 若 A = {1}, 则 \\complement_U A = {2, 3}。

交换律：

A \\cap B = B \\cap A, A \\cup B = B \\cup A

结合律：

A \\cup (B \\cup C) = (A \\cup B) \\cup C, A \\cap (B \\cap C) = (A \\cap B) \\cap C

分配对偶律：

A \\cap (B \\cup C) = (A \\cap B) \\cup (A \\cap C), A \\cup (B \\cap C) = (A \\cup B) \\cap (A \\cup C)

德摩根定律：

\\complement_U(A\\cap B)=(\\complement_UA)\\cup(\\complement_UB)

\\complement_U(A\\cup B)=(\\complement_UA)\\cap(\\complement_UB)

推广到多个集合中：

\\complement_U(A_1 \\cap A_2 \\cap \\cdots \\cap A_n) = (\\complement_U A_1) \\cup (\\complement_U A_2) \\cup \\cdots \\cup (\\complement_U A_n)

\\complement_U(A_1 \\cup A_2 \\cup \\cdots \\cup A_n) = (\\complement_U A_1) \\cap (\\complement_U A_2) \\cap \\cdots \\cap (\\complement_U A_n)

容斥原理：

|A\\cup B|=|A|+|B|-|A\\cap B|

等价转化：

A\\cup B=B \\iff A\\subseteq B

A\\cap B=A \\iff A\\subseteq B

A\\cup B=A\\cap B \\iff A=B

### 命题与量词

命题：

- 原命题：若 p 则 q。
- 逆命题：若 q 则 p。
- 否命题：若非 p 则非 q。
- 逆否命题：若非 q 则非 p。

容易知道，原命题与逆否命题同真同假，互为充要条件。

| 量词     | 命题                  | 否命题                      |
| -------- | --------------------- | --------------------------- |
| 全称量词 | \\forall x\\in M,p(x) | \\exist x\\in M,\\neg p(x)  |
| 存在量词 | \\exist x\\in M,p(x)  | \\forall x\\in M,\\neg p(x) |

## 序理论

序理论是利用二元关系来将「次序」这一概念严格化的数学分支，下面将介绍这一分支的基本定义。

### 二元关系

集合 X 和集合 Y 上的一个**二元关系**（binary relation）R 定义为元组 (X,Y,G(R))，其中 X 称为定义域（domain），Y 称为陪域（codomain），G(R)\\subseteq X\\times Y={(x,y):x\\in X,y\\in Y} 称为二元关系 R 的图（graph）。xRy 成立当且仅当 (x,y)\\in G(R)。

若 X=Y，则称该二元关系为齐次二元关系（homogeneous relation）或内关系（endorelation）。若没有特别说明，下文中的二元关系均为齐次二元关系。例如 \\mathbf{N}\_+ 上的整除 \\mid 和小于等于 \\leq 均为二元关系。

我们研究二元关系时，往往会关注其是否具有一些特别的性质。对集合 S 上的二元关系 R，我们定义如下特殊性质：

1. 自反性（reflexive）：(\\forall~a \\in S)~~aRa，
1. 反自反性（irreflexive，anti-reflexive）：(\\forall~a \\in S)~~\\lnot(aRa)，
1. 对称性（symmetric）：(\\forall~a,b \\in S)~~aRb \\iff bRa，
1. 反对称性（antisymmetric）：(\\forall~a,b \\in S)~~(aRb \\land bRa) \\implies a=b，
1. 非对称性（asymmetric）：(\\forall~a,b \\in S)~~aRb \\implies \\lnot(bRa)，
1. 传递性（transitive）：(\\forall~a,b,c \\in S)~~(aRb \\land bRc) \\implies aRc，
1. 连接性（connected）：(\\forall~a,b \\in S)~~a \\neq b \\implies (aRb \\lor bRa)，
1. 良基性（well-founded）：(\\exists~m \\in S \\neq \\varnothing)~~(\\forall~a \\in S\\setminus{m})~~\\lnot(aRm)（即非空集合 S 中有极小元 m），
1. 不可比的传递性（transitive of incomparability）：(\\forall~a,b,c \\in S)~~(\\lnot(aRb \\lor bRa) \\land \\lnot(bRc \\lor cRb)) \\implies \\lnot(aRc \\lor cRa)（若 \\lnot(aRb \\lor bRa)，则称 a 和 b 是不可比的）。

同时我们定义一些特殊的二元关系：

| 二元关系                         | 自反性 | 反自反性 | 对称性 | 反对称性 | 非对称性 | 传递性 | 连接性 | 良基性 | 不可比的传递性 |
| -------------------------------- | ------ | -------- | ------ | -------- | -------- | ------ | ------ | ------ | -------------- |
| 等价关系（equivalence relation） | 有     |          | 有     |          |          | 有     |        |        |                |
| 预序（preorder，quasiorder）     | 有     |          |        |          |          | 有     |        |        |                |
| 偏序（partial order）            | 有     |          |        | 有       |          | 有     |        |        |                |
| 全序（total order）              | 有     |          |        | 有       |          | 有     | 有     |        |                |
| 良序（well-order）               | 有     |          |        | 有       |          | 有     | 有     | 有     |                |
| 严格预序（strict preorder）      |        | 有       |        |          |          | 有     |        |        |                |
| 严格偏序（strict partial order） |        | 有       |        |          | 有       | 有     |        |        |                |
| 严格弱序（strict weak order）    |        | 有       |        |          | 有       | 有     |        |        | 有             |
| 严格全序（strict total order）   |        | 有       |        |          | 有       | 有     | 有     |        |                |

关系间的运算：对集合 X 和集合 Y 上的二元关系 R 和 S，我们可以定义如下运算

1. R 和 S 的并 R\\cup S 满足 G(R\\cup S):={(x,y):xRy \\lor xSy}（如 \\leq 是 < 和 = 的并），
1. R 和 S 的交 R\\cap S 满足 G(R\\cap S):={(x,y):xRy \\land xSy}，
1. R 的补 \\bar{R} 满足 G(\\bar{R}):={(x,y):\\lnot(xRy)}，
1. R 的对偶 R^T 满足 G(R^T):={(y,x):xRy}.

对集合 X 和集合 Y 上的二元关系 R 以及集合 Y 和集合 Z 上的二元关系 S，我们可以定义其复合 S\\circ R 满足 G(S\\circ R):={(x,z):(\\exists~y\\in Y)~~xRy\\land ySz}。

在序理论中，对偶是非常常见的概念，如上文提到的极大元与极小元对偶、上界与下界对偶、上确界与下确界对偶。对偏序集 P 和其上的偏序 \\preceq，定义其 **对偶**（dual，opposite）偏序集 P^d 满足：x \\preceq y 在 P 中成立当且仅当 y \\preceq x 在 P^d 中成立。将 P 的 Hasse 图的边反转即可得到 P^d 的 Hasse 图。

### 偏序集

若集合 S 上的一个二元关系 \\preceq 具有**自反性**、**反对称性**、**传递性**，则称 S 是**偏序集**（partially ordered set，poset），\\preceq 为其上一**偏序**（partial order）。

若偏序 \\preceq 还具有**连接性**，则称其为**全序**（total order），对应的集合称为**全序集**（totally ordered set）、**线性序集**（linearly ordered set，loset）、**简单序集**（simply ordered set）。

不难发现 \\mathbf{N}，\\mathbf{Z}，\\mathbf{Q}、\\mathbf{R} 均关于 \\leq 构成全序集。

对于有限偏序集，我们可以用 Hasse 图直观地表示其上的偏序关系。对有限偏序集 S 和其上的偏序 \\preceq，定义 x\\prec y\\iff (x\\preceq y\\land x\\neq y) 其对应的 **Hasse 图**为满足如下条件的图 G=\\langle V,E\\rangle：

- V=S,
- E={(x,y)\\in S\\times S: x\\prec y \\land ((\\nexists~z\\in S)~~x\\prec z\\prec y)}

如对于集合 {0,1,2} 的幂集 S 和集合的包含关系 \\subseteq，其对应的 Hasse 图为：

由于偏序具有反对称性，所以 Hasse 图一定是有向无环图，进而我们可以根据拓扑排序对任意有限偏序集构造全序。

对偏序集 S 和其上的偏序 \\preceq，称 S 的全序子集为**链**（chain）。若 S 的子集 T 中任意两个不同元素均不可比（即 (\\forall~a,b \\in T)~~a \\neq b \\implies (a \\npreceq b \\land b \\npreceq a)），则称 T 为 **反链**（antichain）。

对偏序集 S 和其上的偏序 \\preceq，我们将偏序集 S 的最长反链长度称为**宽度**（partial order width）。如对于集合 {0,1,2} 的幂集 S 和集合的包含关系 \\subseteq，{\\varnothing,{1},{1,2}} 为一条链，{{1},{0,2}} 为一条反链，S 的宽度为 3.

### 预序集

在预序集中，我们可以定义极大（小）元、上（下）界、上（下）确界等概念，这些概念可以推广到其他序关系中。

对预序集 S 和其上的预序 \\preceq，取 S 中的元素 m：

1. 若 (\\forall~a \\in S\\setminus{m})~~\\lnot(m\\preceq a)，则称 m 为**极大元**（maximal element），
1. 若对 T \\subseteq S 满足 (\\forall~t\\in T)~~t\\preceq m，则称 m 为 T 的**上界**（upper bound），
1. 若对 T \\subseteq S 满足 m 是 T 的上界且对 T 的任意上界 n 均有 m \\preceq n，则称 m 为 T 的**上确界**（supremum）。

类似可定义**极小元**（minimal element）、**下界**（lower bound）和**下确界**（infimum）。如 1 是 \\mathbf{N}\_+ 的极小元和下界。

可以证明：

- 预序集中，极大（小）元、上（下）界、上（下）确界都是不一定存在的，即使存在也不一定唯一。

- 若偏序集 S 的子集 T 存在上（下）确界，则一定唯一。

  我们可将 T 的上确界、下确界分别记为 \\sup T，\\inf T. 若偏序集 S 既有上界又有下界，则称 S 是有界的。

在无限偏序集中，极大元不一定存在。可用 **Zorn 引理**（Zorn’s Lemma）来判断无限偏序集中是否存在极大元。

**Zorn 引理**也被称为 **Kuratowski–Zorn 引理**，其内容为：若非空偏序集的每条链都有上界，则该偏序集存在极大元。Zorn 引理与 **[选择公理](https://en.wikipedia.org/wiki/Axiom_of_choice)**、**[良序定理](https://en.wikipedia.org/wiki/Well-ordering_theorem)** 等价。

### 有向集与格

我们知道若偏序集的子集存在上（下）确界，则一定唯一。但是这一点并不适用于极大（小）元。例如：考虑偏序集 S={{0},{1},{2},{0,1},{0,2},{1,2}} 和其上的偏序 \\subseteq，不难发现其有 3 个极大元和 3 个极小元。

我们希望通过向偏序集添加一定的条件来使得若极大（小）元存在则一定唯一，这样我们就可以定义最大（小）元的概念了。

对预序集 S 和其上的预序 \\preceq，若 (\\forall~a,b\\in S)~~(\\exists~c\\in S)~~a\\preceq c\\land b\\preceq c，则称 \\preceq 为 S 的一个**方向**（direction），S 称为**有向集**（directed set）或**过滤集**（filtered set）。

有时也将满足上述定义的集合 S 称为**上有向集**（upward directed set），类似地可定义**下有向集**（downward directed set）。

有向集也可用如下方式定义：对预序集 S 和其上的预序 \\preceq，若 S 的任意有限子集 T 均有上界，则称 \\preceq 为 S 的一个方向，S 称为有向集。

不难发现：

- 若上有向集存在极大元，则一定唯一。我们将上有向集的极大元称为**最大元**（greatest element）。
- 若下有向集存在极小元，则一定唯一。我们将下有向集的极小元称为**最小元**（least element）。

有方向的偏序集中，对任意元素 a,b，{a,b} 都有上界，若将上界修改为上确界，则得到了并半格的定义。

对偏序集 S 和其上的偏序 \\preceq：

- 若对 S 中的任意元素 a,b，{a,b} 均有上确界 c，则称 S 为**并半格**（join-semilattice，upper semilattice），并且我们称 c 为 a 和 b 的**并**（join），记为 a\\lor b.
- 若对 S 中的任意元素 a,b，{a,b} 均有下确界 c，则称 S 为**交半格**（meet-semilattice，lower semilattice），并且我们称 c 为 a 和 b 的**交**（meet），记为 a\\land b.
- 若 S 既是并半格也是交半格，则称 S 为**格**（lattice）。

例如 60 的正因子构成的集合 S={1,2,3,4,5,6,10,12,15,20,30,60} 关于整除构成偏序集，其上的任意正整数 a,b，\\operatorname{lcm}(a,b) 为 a 和 b 的并，\\gcd(a,b) 为 a 和 b 的交，从而 S 是格。

### Dilworth 定理与 Mirsky 定理

对有限偏序集 S 和其上的偏序 \\preceq，我们有如下的一对对偶的定理：

Dilworth 定理：S 的宽度（最长反链长度）等于最小的链覆盖数。

证明：考虑数学归纳法。当 |S|\\leq 3 时，命题显然成立。

假设命题对所有元素个数小于 |S| 的偏序集都成立，令 S 的宽度为 d. 若 |S| 中所有元素均不可比，则命题显然成立，否则在 S 中取一条长度大于 1 的链，令其中的最小元为 m，最大元为 M.

令 T=S\\setminus{m,M}，若 T 中的宽度不超过 d-1，则由归纳假设知 T 可被至多 d-1 条链覆盖，进而 S 可被这些链再加上链 {m,M} 覆盖，命题成立，否则说明 T 中的宽度也为 d，令 T 中最长的一条反链为 A.

我们考虑如下两个集合：

S^+:={x\\in S:(\\exists~a\\in A)~~a\\preceq x}

S^-:={x\\in S:(\\exists~a\\in A)~~x\\preceq a}

我们不难发现如下性质：

- S^+\\cup S^-=S，
- S^+\\cap S^-=A，
- |S^+|\<|S|,|S^-|\<|S|（因为 m\\notin S^+ 且 M\\notin S^-）。

对 S^+ 和 S^- 都应用归纳假设，则这两个集合的最小链覆盖数为 d，且这些链中恰好包含一个 A 中的元素 a，设这些链分别为 C_a^+，C_a^-，则 {C_a^-\\cup{a}\\cup C_a^+}\_{a\\in A} 是 S 的一个最小链覆盖，命题得证。

Mirsky 定理：S 的最长链长度等于最小的反链覆盖数。

证明：设 S 的最长链长度为 d，则由定义，最小反链覆盖数至少为 d.

令 f(s) 为以 s 为最小元的最长链长度，注意到若 f(s)=f(t)，则 s 与 t 不可比，进而 (\\forall~n\\in\\mathbf{N})~~f^{-1}({n}) 均为反链，其中 f^{-1}({n}):={a\\in S:f(a)=n} 称为 [水平集（level set）](https://en.wikipedia.org/wiki/Level_set)。

因此不难得出 {f^{-1}({i}):1\\leq i\\leq d} 是一个反链覆盖，从而最小反链覆盖数至多为 d.

Dilworth 定理与 Hall 婚配定理等价。我们可以用 Dilworth 定理证明如下定理：

Erdős–Szekeres 定理：含至少 rs+1 个元素的实数序列 {a_i} 要么有一个长为 r+1 的不下降子序列，要么有一个长为 s+1 的不上升子序列。

证明：设序列长度为 n\\geq rs+1，定义偏序集 {(i,a_i)}\_{i=1}^{n}，其上的偏序 \\preceq 定义为：

(i,a_i)\\preceq (j,a_j)\\iff (i\\leq j\\land a_i\\leq a_j)

假设该偏序集的宽度不超过 s，则由 Dilworth 定理可知该偏序集可以被至多 s 条链覆盖，若这些链的长度都不超过 r，则序列所含元素数至多为 rs，与条件矛盾。

## 布尔代数

### 布尔代数和布尔函数

在数理逻辑中，布尔代数（boolean algebra）是代数的一个分支。初等代数中变量的值是数字，其研究的主要运算符有加法、乘法、乘方以及这三种运算的逆运算。而布尔代数中变量的值仅为 **真** 和 **假** 两种（通常记作 1 和 0），其研究的主要运算符有合取（与，\\land）、析取（或，\\lor）、否定（非，\\lnot）。就像初等代数是描述数字运算的一种形式一样，布尔代数是描述逻辑运算的一种形式。

**布尔函数**（boolean function）指的是形如 f:\\mathbf{B}^k\\to \\mathbf{B} 的函数，其中 \\mathbf{B}={0,1} 为 **布尔域**（boolean domain），非负整数 k 为该布尔函数的 **元数**（arity）。k=1 的布尔函数为一元函数，以此类推。k=0 时，我们认为函数退化为 \\mathbf{B} 中的常量。

我们一般只研究一元和二元的布尔函数。如无特殊说明，下文的布尔函数仅限于一元和二元的情况。除了函数的一般表达方式外，我们还可以用 **真值表**（truth table）、**逻辑门**（logic gate）、[Venn 图](https://en.wikipedia.org/wiki/Venn_diagram) 来表示布尔函数。

n 元布尔函数也可以用含 n 个变量的 **命题公式**（propositional formula）表示，命题公式 p 与 q **逻辑等价**（logically equivalent）当且仅当其描述的是同一个布尔函数，记作 p\\iff q。

对一个布尔函数，我们枚举其输入的所有情况，并将输入和对应的输出列成一张表，这个表就叫做真值表。以下是一些常见布尔函数，我们也会把这些布尔函数统称为 **逻辑运算符**（logical connective）或 **逻辑算子**（logical operator）：

| 名称（数理逻辑）                                               | 其他名称                   | 记号                             |
| -------------------------------------------------------------- | -------------------------- | -------------------------------- |
| 恒真（truth、tautology）                                       |                            | \\top                            |
| 恒假（falsity、contradiction）                                 |                            | \\bot                            |
| 命题                                                           | 自身                       | A                                |
| 否定（negation）                                               | 非（NOT）                  | \\lnot A                         |
| 合取（conjunction）                                            | 与（AND）                  | A \\land B                       |
| 析取（disjunction）                                            | 或（OR）                   | A \\lor B                        |
| 非合取（non-conjunction）                                      | 与非（NAND）、Sheffer 竖线 | A \\bar{\\land} B、A\\uparrow B  |
| 非析取（non-disjunction）                                      | 或非（NOR）                | A \\bar{\\lor} B、A\\downarrow B |
|                                                                | 异或（Exclusive-OR，XOR）  | A \\oplus B                      |
|                                                                | 同或（Exclusive-NOR）      | A \\odot B                       |
| 实质蕴含（material implication）[1](#fn1)                      |                            | A \\to B                         |
| 实质非蕴含（material nonimplication）[2](#fn2)                 |                            | A \\nrightarrow B                |
| 反蕴涵（converse implication）[3](#fn3)                        |                            | A \\gets B                       |
| 非反蕴涵（converse nonimplication）[4](#fn4)                   |                            | A \\nleftarrow B                 |
| 双条件（biconditional）、等价（equivalence）[5](#fn5)[6](#fn6) |                            | A \\leftrightarrow B             |
| 非等价（non-equivalence）[7](#fn7)[8](#fn8)                    |                            | A \\nleftrightarrow B            |

我们把逻辑算子的组合称为 **逻辑表达式**（logical expression）。如果我们把 \\mathbf{B} 视作模 2 的一个剩余类，此时异或等价于模 2 加法，与等价于模 2 乘法，所以有时我们也用 \\mathbf{Z}\_2 表示布尔域。

一元逻辑算子优先级高于二元逻辑算子，即 \\lnot 的优先级高于 \\land、\\lor、\\oplus 等的优先级。二元逻辑算子之间的优先级有多种规定，有的资料认为 \\land、\\lor、\\oplus 的优先级比 \\to、\\gets、\\leftrightarrow 更高，而有的资料持相反观点。所以在使用时推荐多加括号来明确顺序。

实际上，我们只用与非或者或非即可表达其余的逻辑算子，CPU 也是基于这一点构建的。但是，由于 **与、或、非、异或** 这四种逻辑算子的性质更好，所以我们在研究布尔代数时一般只使用这四种函数。我们能不能用指定的若干逻辑算子描述所有的逻辑算子？这便引出了完备算子集的定义。

- 对一个给定的逻辑算子集，如果能只用这个集合里的函数描述所有的逻辑算子，则称该集合为 **完备算子集**（functionally complete operator set）。特别地，如果只用一个逻辑算子即可描述所有的逻辑算子，则称该算子为 **自足算子**（sole sufficient operator）或 **Sheffer 函数**（Sheffer function）。
- 如果在一个完备算子集中删去任意一个元素，其都不能描述所有的逻辑算子，则称该集合为 **极小完备算子集**（minimal functionally complete operator set）。

可以证明逻辑算子中只有 \\bar{\\land}、\\bar{\\lor} 是自足算子。

以下为常见的极小完备算子集[9](#fn9)：

- {\\bar{\\land}}，{\\bar{\\lor}}，
- {\\land,\\lnot}，{\\lor,\\lnot}，{\\gets,\\lnot}，{\\to,\\lnot}，{\\nleftarrow,\\lnot}，{\\nrightarrow,\\lnot}，
- {\\gets,\\bot}，{\\to,\\bot}，{\\nleftarrow,\\top}，{\\nrightarrow,\\top}，
- {\\gets,\\nleftarrow}，{\\to,\\nleftarrow}，{\\gets,\\nrightarrow}，{\\to,\\nrightarrow}，
- {\\gets,\\nleftrightarrow}，{\\to,\\nleftrightarrow}，{\\nleftarrow,\\leftrightarrow}，{\\nrightarrow,\\leftrightarrow}，
- {\\lor,\\leftrightarrow,\\bot}，{\\lor,\\leftrightarrow,\\nleftrightarrow}，{\\lor,\\nleftrightarrow,\\top}，
- {\\land,\\leftrightarrow,\\bot}，{\\land,\\leftrightarrow,\\nleftrightarrow}，{\\land,\\nleftrightarrow,\\top}。

首先是代数结构的相关性质：

- 与、或均关于 \\mathbf{B} 构成交换幺半群。即与运算和或运算均具有交换律、结合律和幺元（x\\land 1=x\\lor 0=x）。
- 异或、同或均关于 \\mathbf{B} 构成群。即异或运算和同或运算均具有交换律、结合律、幺元（x\\oplus 0=x\\odot 1=x）和逆元（x\\oplus x=0，x\\odot x=1）。
- 与非、或非均不具有结合律，所以不构成半群。

对于 \\land、\\lor，我们有

- 分配律：
  - a\\land(b\\diamond c)=(a\\land b)\\diamond (a\\land c)，其中 \\diamond 可以为 \\land、\\lor、\\oplus，
  - a\\lor(b\\diamond c)=(a\\lor b)\\diamond (a\\lor c)，其中 \\diamond 可以为 \\land、\\lor、\\odot。
- **幂等**（idempotence）律：x\\land x=x、x\\lor x=x。
- 单调性：a\\to b\\iff(a\\land c)\\to(b\\land c)、a\\to b\\iff(a\\lor c)\\to(b\\lor c)。
- **吸收**（absorption）律：x\\land(x\\lor y)=x\\lor(x\\land y)=x。
- 与「\\to」的关系：
  - a \\lor b \\iff (\\lnot a \\to b) \\land (\\lnot b \\to a)，
  - a \\land b \\iff \\lnot((a \\to \\lnot b) \\lor (b \\to \\lnot a))。

???+ abstract “布尔函数的单调性” 对一个布尔函数 f(x_1,\\dots,x_n) 和 \\mathbf{B}^n 中的两个元素 (a_1,\\dots,a_n),(b_1,\\dots,b_n)，若当 a_i\\leq b_i,~~\\forall i=1,\\dots,n 时恒有 f(a_1,\\dots,a_n)\\leq f(b_1,\\dots,b_n)，则称该布尔函数是单调的。

我们还有如下性质：

- **排中律**（law of excluded middle）：p\\lor\\lnot p 恒真。
- \\lnot p\\iff p\\to\\bot。
- 双重否定/\\lnot 的 **对合**（involution）律：\\lnot\\lnot x=x。
- \\oplus、\\odot 的对合律：x\\oplus y\\oplus y=x、x\\odot y\\odot y=x。
- De Morgan 律：\\lnot(p\\land q)=\\lnot p\\lor \\lnot q、\\lnot(p\\lor q)=\\lnot p\\land \\lnot q。

### 逻辑表达式的标准化

根据上述性质，我们可以对逻辑表达式进行一定的等价变换，使其符合特定的范式，这一点可用于自动定理证明中。常见的标准化范式有 **合取范式**（conjunctive normal form，CNF）、**析取范式**（disjunctive normal form，DNF）和 **代数范式**（algebraic normal form，ANF）。

“合取范式与析取范式”我们做如下递归式的定义：

1. **文字**（literal）：对变量 x，x 和 \\lnot x 是文字。
1. 子式：
   - 文字是子式，
   - 若 A 是文字、B 是子式，则 A\\lor B 是子式。
1. 合取范式：
   - 若 A 是子式，则 (A) 是合取范式，
   - 若 A 是子式、B 是合取范式，则 (A)\\land B 是合取范式。

类似地，交换上面定义中的 \\land 与 \\lor 即可得到析取范式的定义。

例如以下逻辑表达式均为析取范式：

- (A\\land\\lnot B)\\lor(C\\land D\\land\\lnot E)，
- (A\\land B)\\lor (C)，
- (A\\land B)，
- (A)。

以下逻辑表达式均为合取范式：

- (\\lnot A\\lor\\lnot B\\lor C)\\land(\\lor D\\lor\\lnot E)，
- (A\\lor B)\\land (C)，
- (A\\lor B)，
- (A)。

以下逻辑表达式既不为合取范式也不为析取范式：

- \\lnot(A\\land B)，
- A\\land (B\\lor (C\\land D))。

我们可以通过如下的步骤将任意一个只含有 \\lnot、\\land、\\lor 运算的逻辑表达式变形为 DNF：

\\begin{array}{rcccl} \\lnot\\lnot x &&\\mapsto&& x,\\ \\lnot(x\\lor y) &&\\mapsto&& \\lnot x\\land \\lnot y,\\ \\lnot(x\\land y) &&\\mapsto&& \\lnot x\\lor \\lnot y,\\ x\\land(y\\lor z) &&\\mapsto&& (x\\land y)\\lor (x\\land z),\\ (x\\lor y)\\land z &&\\mapsto&& (x\\land z)\\lor (y\\land z). \\end{array}

要得到表达式 X 的 CNF，只需得到 \\lnot X 的 DNF 后取反并应用 De Morgan 律即可。

“代数范式”首先，我们用如下递归式的定义来定义子式：

- 变量 x 是子式，
- 若 A 是子式，x 是变量，则 x\\land A 是子式。

则满足如下三种形式之一的逻辑表达式为代数范式：

1. 1、0，
1. 若干不等价子式的异或，如 a\\oplus b\\oplus(a\\land b)\\oplus(a\\land b\\land c)，
1. 若干不等价子式与唯一的 1 的异或，如 1\\oplus a\\oplus b\\oplus(a\\land b)\\oplus(a\\land b\\land c)。

注意到代数范式和 \\mathbf{Z}\_2 上的多项式一一对应，所以代数范式也被称为 **Zhegalkin 多项式**（Zhegalkin polynomial）。

我们可以通过如下的步骤将任意一个只含有 \\lnot、\\land、\\lor、\\oplus 运算的逻辑表达式变形为 ANF：

1. \\oplus：直接展开，如 (1\\oplus x)\\oplus(1\\oplus x\\oplus y)=1\\oplus x\\oplus 1\\oplus x\\oplus y=y，
1. \\land：用分配律展开，如 x\\land(1\\oplus x\\oplus y)=(x\\land 1)\\oplus (x\\land x)\\oplus (x\\land y)=x\\oplus (x\\land y)，
1. \\lnot：将 \\lnot x 用 1\\oplus x 代替，如 \\lnot(1\\oplus x\\oplus y)=1\\oplus 1\\oplus x\\oplus y=x\\oplus y，
1. \\lor：将 x\\lor y 用 1\\oplus((1\\oplus x)\\land(1\\oplus y)) 或 x\\oplus y\\oplus (x\\land y) 代替，如 (1\\oplus x)\\lor(1\\oplus x\\oplus y)=1\\oplus((1\\oplus 1\\oplus x)\\land(1\\oplus 1\\oplus x\\oplus y))=1\\oplus x\\oplus(x\\land y)。

## 线性规划基础

线性规划

1. 约束条件：变量 x,y,\\dots 满足的一组条件，上述二元一次不等式组就是对 x,y 的约束条件。
1. 线性约束条件：由变量 x,y,\\dots 的一次不等式 / 方程组成的不等式组就称为线性约束条件，如上述二元一次不等式。
1. 目标函数：欲求最大值或最小值所涉及的变量 x,y,\\dots 的解析式，如上述 z.
1. 线性目标函数：目标函数关于变量 x,y,\\dots 的一次解析式，如上述 z.
1. 线性规划问题：在线性约束条件下求线性目标函数的问题。
1. 可行解：满足线性约束条件的解 (x,y).
1. 可行域：由所有可行解组成的集合。
1. 最优解：使目标函数取得 \\max 或 \\min 的可行解。

\\circ Ax + By

转为直线切凸包。

\\circ x^2 + y^2

转为到原点距离。

\\circ \\frac{y-a}{x-b}

转为过一点斜率。

\\circ 其余情况先变换为以上三种或其他几何意义。

例题 1

\\begin{cases}5x-11y \\geq -22 \\ 2x+3y \\geq 9 \\ 2x \\leq 11\\end{cases}

$z = 10x + 10y, \\max{z} = $ ？

1. 画图，数形结合。

   \\begin{cases}5x-11y \\geq -22 & \\displaystyle \\implies y \\leq \\frac{5}{11}x + \\frac{1}{2} & \\implies & \\displaystyle y = \\frac{5}{11}x + \\frac{1}{2}\\ 图像的下边 \\ 2x+3y \\geq 9 & \\displaystyle \\implies y \\geq -\\frac{2}{3}x + 3 & \\implies & \\displaystyle y = -\\frac{2}{3}x + 3\\ 图像的上边 \\ 2x \\leq 11 & \\displaystyle \\implies x \\leq \\frac{11}{2} & \\implies & \\displaystyle x=\\frac{11}{2}\\ 图像的左边 \\end{cases}

   在平面直角坐标系上画出对应的平面区域（可行域），再把目标函数 z=ax+by 变形为 \\displaystyle y=-\\frac{a}{b}x + \\frac{z}{b}，\\ 所以求 z 的最值可看成是求直线 \\displaystyle y=-\\frac{a}{b}x + \\frac{z}{b} 在 y 轴上截距的最值。以这题为例，\\displaystyle z=10x+10y \\implies y= -x + \\frac{z}{10} 容易证明，当 z=85 时 y 轴上截距取最值，所以 \\max{z}=85.

   !

1. 仔细观察，可以发现最优解非常容易出现在可行域构成的**多面体的顶点**处。

例题 2

\\begin{cases}y \\geq x \\ x + y \\leq 2 \\ x \\geq a\\end{cases}

$(2x+y)*{\\mathrm{max}}=4(2x+y)*{\\mathrm{min}},\\ a= $ ?

- 求 (2x+y)_{\\mathrm{min}}：x_{\\min}=a \\implies y\_{\\min}=a \\implies (2x+y)\_{\\mathrm{min}}=3a
- 求 (2x+y)_{\\mathrm{max}}：\\begin{cases}x-y\\leq 0 \\ x+y\\leq 2\\end{cases}\\xRightarrow{\\mathrm{Add\\ }} x\\leq 1\\implies y\\leq 1\\implies (2x+y)_{\\mathrm{max}}=3
- \\displaystyle 3=4\\times 3a\\implies a=\\frac{1}{4}

例题 3（2024 九省联考 T14）

\\begin{cases} 0\<a\<b\<c\<1 \\ b\\geq 2a \\ \\ \\ \\mathrm{or}\\ \\ \\ a+b\\leq 1 \\end{cases}

\\max{\\set{b-a,c-b,1-c}} 的最小值 = ？

- 注意到 c 的约束条件是最少的，首先考虑消去它，得到

  \\max{\\set{b-a,c-b,1-c}}\\geq\\max{\\set{b-a,\\frac{1-b}{2}}}

  当且仅当 \\displaystyle c=\\frac{1+b}{2} 取等，消去 c 后把 a 看作 x，把 b 看作 y 得：

  \\begin{cases}0\<x \\ x\<y \\ y\<1 \\ y\\geq 2x\\ \\ \\ \\mathrm{or}\\ \\ \\ x+y\\leq 1\\end{cases}

- 作出可行域：\\mathrm{and} 连接的区域之间取交，\\mathrm{or} 连接的区域之间取并。阴影部分即为可行域。

  图中 y\\geq 2x\\ \\ \\ x+y\\leq 1 两条解析式用红色标出。

- 回到题目，要求 \\displaystyle M=\\max{\\set{y-x,\\frac{1-y}{2}}}，我们需要知道何时 M=y-x，何时 \\displaystyle M=\\frac{1-y}{2}.

  直接列方程 \\displaystyle y-x=\\frac{1-y}{2} 可以得到 \\displaystyle y=\\frac{2}{3}x+\\frac{1}{3}，在图中作出这条直线，得到：

- 因为最终要求的是 M 的最小值，所以对蓝色区域而言，y 尽量小，x 尽量大，根据例题 1 的经验，这样的极值点通常出现在多边形的顶点处，经过比较后 P 点是极值点，此时 M=0.2. 对绿色区域而言，只需满足 y 尽量大，显然，P 点也是极值点。

- 综上所述，\\max{\\set{b-a,c-b,1-c}} 的最小值 \\displaystyle=\\frac{1}{5}.

<https://oi-wiki.org/math/linear-programming/#%E5%BC%95%E5%85%A5>

## 博弈论

### 组合游戏

定义如下：

- 有两个参与者（称为游戏者）；
- 游戏规则规定了玩家可以做出的决策集合（通常是有限的）；
- 游戏者轮流决策，决策时双方均知道游戏的完整信息；
- 当游戏者无法做出决策时，游戏结束；
- 游戏总有一个有限的结局，若不存在，则称为平局（Draw）。

注意我们还有一些更严格的定义，

- 游戏不允许存在任何随机运动，例如掷骰子或发牌（针对扑克等）；
- 游戏不允许任何同时决策或隐藏移动（针对剪刀石头布等）；
- 游戏不允许在有限决策中存在平局（这排除了井字棋）。

### 公平组合游戏

双方在某一确定状态可以做出的决策集合只与当前状态无关，与游戏者无关。

也可以表述为，在任意状态，双方可以做出的决策集合是相同的。

### 非公平组合游戏

游戏者在某一状态可以做出的决策集合与游戏者有关。

例如围棋、国际象棋等，因为双方均不能使用对方的棋子。

### 反常游戏

一般来说，游戏为最后一个决策者获胜。

反常游戏指的是，最后无法决策的一方获胜。

反常游戏的规则被称为反常规则（Misère Play Rule）。

### P/N-Position

此处仅考虑非反常游戏，定义，

- **P**-Position：上一位玩家必胜（**P**revious player）；
- **N**-Position：下一位玩家必胜（**N**ext player）。

注意我们所谓上下，指的是当前局面（the player who just moved）。

我们再看一个英文定义，

- **P**-position: The **P**revious player has a winning strategy
- **N**-position: The **N**ext player has a winning strategy.

容易发现，上文所谓必胜，其实指的是存在有一个使其获胜的策略。

按照一般中文环境的术语就是，

- 我们称一游戏者的 N 状态为她决策前的局面为她的必胜状态（她马上就要决策）；
- 我们称一游戏者的 P 状态为她决策前的局面为她的必败状态（决策点已经转移）。

由此，可以引出先手必胜和先手必败的定义。

特殊的，我们称最后无法进行任何决策的状态为 **T**-Position（**T**erminal Position），

- 每一个 T-Position 都是 P-Position；
- 每一个 N-Position 都有至少一种决策转移到 P-Position；
- 每一个 P-Position 都只能转移到 N-Position。

反过来也可以作为判定，

- 可以转移到 P-Position 的都是 N-Position；
- 所有转移都为 N-Position 才是 P-Position。

我们可以总结一个判断所有状态 N/P 的方法：

- 直接定义 T-Position 为 P-Position；
- 每一个可以转移到 P-Position 的都定义为 N-Position；
- 当且仅当一个状态的每一个转移都为 N-Position，我们定义它为 P-Position。

### TO BE DONE

<https://web.mit.edu/sp.268/www/nim.pdf>

<https://www.cs.cmu.edu/afs/cs/academic/class/15859-s05/www/ferguson/comb.pdf>

<http://www.maths.liv.ac.uk/~mathsclub/talks/20220226/talk1/NIM.pdf>

<https://assets.hkoi.org/training2021/game-theory.pdf>

<https://www.luogu.com.cn/article/nhpwudt7>

<https://oi-wiki.org/math/game-theory/impartial-game/>

[RainPPR](mailto:PPR2125773894@163.com),  [Bot](mailto:bot@noreply.github.com)

______________________________________________________________________

1. 用于命题推导时应使用双横长箭头，如 A\\implies B、A\\impliedby B、A\\iff B 等。[↩︎](#fnref1)
1. 用于命题推导时应使用双横长箭头，如 A\\implies B、A\\impliedby B、A\\iff B 等。[↩︎](#fnref2)
1. 用于命题推导时应使用双横长箭头，如 A\\implies B、A\\impliedby B、A\\iff B 等。[↩︎](#fnref3)
1. 用于命题推导时应使用双横长箭头，如 A\\implies B、A\\impliedby B、A\\iff B 等。[↩︎](#fnref4)
1. 用于命题推导时应使用双横长箭头，如 A\\implies B、A\\impliedby B、A\\iff B 等。[↩︎](#fnref5)
1. 等价于同或。[↩︎](#fnref6)
1. 用于命题推导时应使用双横长箭头，如 A\\implies B、A\\impliedby B、A\\iff B 等。[↩︎](#fnref7)
1. 等价于异或。[↩︎](#fnref8)
1. Vaughan, H. E. (1942). Complete sets of logical functions.*Transactions of the American Mathematical Society 51*: 117–32.[↩︎](#fnref9)
