# 博弈论

## Defination

### 组合游戏（Combinatorial Games）

定义如下：

+ 有两个参与者（称为游戏者）；

+ 游戏规则规定了玩家可以做出的决策集合（通常是有限的）；

+ 游戏者轮流决策，决策时双方均知道游戏的完整信息；

+ 当游戏者无法做出决策时，游戏结束；

+ 游戏总有一个有限的结局，若不存在，则称为平局（Draw）。

注意我们还有一些更严格的定义，

+ 游戏不允许存在任何随机运动，例如掷骰子或发牌（针对扑克等）；

+ 游戏不允许任何同时决策或隐藏移动（针对剪刀石头布等）；

+ 游戏不允许在有限决策中存在平局（这排除了井字棋）。

### 公平组合游戏（Impartial Game）

双方在某一确定状态可以做出的决策集合只与当前状态无关，与游戏者无关。

也可以表述为，在任意状态，双方可以做出的决策集合是相同的。

### 非公平组合游戏（Partizan Game）

游戏者在某一状态可以做出的决策集合与游戏者有关。

例如围棋、国际象棋等，因为双方均不能使用对方的棋子。

### 反常游戏（Misère Game）

一般来说，游戏为最后一个决策者获胜。

反常游戏指的是，最后无法决策的一方获胜。

反常游戏的规则被称为反常规则（Misère Play Rule）。

### P-Position & N-Position

此处仅考虑非反常游戏，定义，

+ **P**-Position：上一位玩家必胜（**P**revious player）；

+ **N**-Position：下一位玩家必胜（**N**ext player）。

注意我们所谓上下，指的是当前局面（the player who just moved）。

我们再看一个英文定义，

+ **P**-position: The **P**revious player has a winning strategy

+ **N**-position: The **N**ext player has a winning strategy.

容易发现，上文所谓必胜，其实指的是存在有一个使其获胜的策略。

按照一般中文环境的术语就是，

+ 我们称一游戏者的 N 状态为她决策前的局面为她的必胜状态（她马上就要决策）；

+ 我们称一游戏者的 P 状态为她决策前的局面为她的必败状态（决策点已经转移）。

由此，可以引出先手必胜和先手必败的定义。

特殊的，我们称最后无法进行任何决策的状态为 **T**-Position（**T**erminal Position），

+ 每一个 T-Position 都是 P-Position；

+ 每一个 N-Position 都有至少一种决策转移到 P-Position；

+ 每一个 P-Position 都只能转移到 N-Position。

反过来也可以作为判定，

+ 可以转移到 P-Position 的都是 N-Position；

+ 所有转移都为 N-Position 才是 P-Position。

我们可以总结一个判断所有状态 N/P 的方法：

+ 直接定义 T-Position 为 P-Position；

+ 每一个可以转移到 P-Position 的都定义为 N-Position；

+ 当且仅当一个状态的每一个转移都为 N-Position，我们定义它为 P-Position。

## TO BE DONE

<https://web.mit.edu/sp.268/www/nim.pdf>

<https://www.cs.cmu.edu/afs/cs/academic/class/15859-s05/www/ferguson/comb.pdf>

<http://www.maths.liv.ac.uk/~mathsclub/talks/20220226/talk1/NIM.pdf>

<https://assets.hkoi.org/training2021/game-theory.pdf>

<https://www.luogu.com.cn/article/nhpwudt7>

<https://oi-wiki.org/math/game-theory/impartial-game/>