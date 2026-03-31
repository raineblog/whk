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

- 子集：A⊆B 或 B⊇A，表示 A 中的任意元素都属于 B

  A⊆A,∅⊆A

  A⊆B 且 B⊆C⟹A⊆C

  A⊆B 且 B⊆A⟹A=B

- 真子集：A⫋B 或 B⫌A，表示 A⊆B 且 B 中至少有一元素不属于 A

  A⫋B 且 B⫋C⟹A⫋C

- 空集（∅）是任何集合的子集，是任何非空集合的真子集。

- 有 n 个元素的集合，有 2n 个子集，2n−1 个真子集，2n−1 个非空子集，2n−2 个非空真子集。

- 空集只有一个子集，没有真子集、非空子集、非空真子集。

集合的表示：

- 列举法：{a,b}（a=b）。
- 描述法：{x∣x=f(t),p(t)}。
- 符号法：R 实数集，C 复数集，Q 有理数集，N 自然数集，Z 整数集，P 质数集。右上角加星号（∗）表示去零，右下角加正、负号表示取正、负。
- 图示法：Venn（维恩）图。

### 集合的运算

表示某一元素属于某个集合时，用 ∈，例如 1∈{1,2,3}。若不属于则用 ∈/。

1. 并集：A={2,3,4},B={1,2,3},A∪B={1,2,3,4}。
1. 交集：A={2,3,4},B={1,2,3},A∩B={2,3}。
1. 补集：U={1,2,3},A⊆U, 若 A={1}, 则 ∁U​A={2,3}。

交换律：

A∩B=B∩A,A∪B=B∪A

结合律：

A∪(B∪C)=(A∪B)∪C,A∩(B∩C)=(A∩B)∩C

分配对偶律：

A∩(B∪C)=(A∩B)∪(A∩C),A∪(B∩C)=(A∪B)∩(A∪C)

德摩根定律：

∁U​(A∩B)=(∁U​A)∪(∁U​B)

∁U​(A∪B)=(∁U​A)∩(∁U​B)

推广到多个集合中：

∁U​(A1​∩A2​∩⋯∩An​)=(∁U​A1​)∪(∁U​A2​)∪⋯∪(∁U​An​)

∁U​(A1​∪A2​∪⋯∪An​)=(∁U​A1​)∩(∁U​A2​)∩⋯∩(∁U​An​)

容斥原理：

∣A∪B∣=∣A∣+∣B∣−∣A∩B∣

等价转化：

A∪B=B⟺A⊆B

A∩B=A⟺A⊆B

A∪B=A∩B⟺A=B

### 命题与量词

命题：

- 原命题：若 p 则 q。
- 逆命题：若 q 则 p。
- 否命题：若非 p 则非 q。
- 逆否命题：若非 q 则非 p。

容易知道，原命题与逆否命题同真同假，互为充要条件。

| 量词     | 命题                   | 否命题                       |
| -------- | ---------------------- | ---------------------------- |
| 全称量词 | ∀*x* ∈ *M*, *p*(*x*)   | $\\exist x\\in M,\\neg p(x)$ |
| 存在量词 | $\\exist x\\in M,p(x)$ | ∀*x* ∈ *M*, ¬*p*(*x*)        |

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
