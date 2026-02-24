# 概率入门 {#_1}

以下部分内容来自 [**OI Wiki**](https://oi-wiki.org/)。

## 概率论基本概念 {#_2}

### 样本空间 {#_3}

简而言之，样本空间 []{.arithmatex}$\Omega$ 指明随机现象**所有**可能出现的结果。

具体的，一个随机现象中可能发生的不能再细分的结果被称为**样本点**，所有样本点的集合称为**样本空间**，通常用 []{.arithmatex}$\Omega$ 来表示。

二维样本空间的列举，表格法：

|  | 1 | 2 | 3 | 4 | 5 | 6 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **1** | []{.arithmatex}$(1, 1)$ | []{.arithmatex}$(1, 2)$ | []{.arithmatex}$(1, 3)$ | []{.arithmatex}$(1, 4)$ | []{.arithmatex}$(1, 5)$ | []{.arithmatex}$(1, 6)$ |
| **2** | []{.arithmatex}$(2, 1)$ | []{.arithmatex}$(2, 2)$ | []{.arithmatex}$(2, 3)$ | []{.arithmatex}$(2, 4)$ | []{.arithmatex}$(2, 5)$ | []{.arithmatex}$(2, 6)$ |
| **3** | []{.arithmatex}$(3, 1)$ | []{.arithmatex}$(3, 2)$ | []{.arithmatex}$(3, 3)$ | []{.arithmatex}$(3, 4)$ | []{.arithmatex}$(3, 5)$ | []{.arithmatex}$(3, 6)$ |
| **4** | []{.arithmatex}$(4, 1)$ | []{.arithmatex}$(4, 2)$ | []{.arithmatex}$(4, 3)$ | []{.arithmatex}$(4, 4)$ | []{.arithmatex}$(4, 5)$ | []{.arithmatex}$(4, 6)$ |
| **5** | []{.arithmatex}$(5, 1)$ | []{.arithmatex}$(5, 2)$ | []{.arithmatex}$(5, 3)$ | []{.arithmatex}$(5, 4)$ | []{.arithmatex}$(5, 5)$ | []{.arithmatex}$(5, 6)$ |
| **6** | []{.arithmatex}$(6, 1)$ | []{.arithmatex}$(6, 2)$ | []{.arithmatex}$(6, 3)$ | []{.arithmatex}$(6, 4)$ | []{.arithmatex}$(6, 5)$ | []{.arithmatex}$(6, 6)$ |

### 随机事件 {#_4}

一个**事件**是样本空间 []{.arithmatex}$\Omega$ 的**任意子集**，又分为：

- 一个**随机事件**是样本空间 []{.arithmatex}$\Omega$ 的**非空真子集**。
- 一个**必然事件**是样本空间 []{.arithmatex}$\Omega$ 本身。
- 一个**不可能事件**是一个空集 []{.arithmatex}$\varnothing$。
- 一个**基本事件**是样本空间 []{.arithmatex}$\Omega$ 的一个大小为 []{.arithmatex}$1$ 的子集。

由此可知，事件是一个由若干样本点构成，用大写字母 []{.arithmatex}$A, B, C, \cdots$ 表示。

对于一个随机现象的结果 []{.arithmatex}$\omega$ 和一个随机事件 []{.arithmatex}$A$，我们称事件 []{.arithmatex}$A$ 发生了 当且仅当 []{.arithmatex}$\omega \in A$。

例如：掷一次骰子得到的点数是一个随机现象，其样本空间可以表示为 []{.arithmatex}$\Omega=\{1,2,3,4,5,6\}$。设随机事件 []{.arithmatex}$A$ 为「获得的点数大于 []{.arithmatex}$4$」，则 []{.arithmatex}$A = \{ 5, 6 \}$。若某次掷骰子得到的点数 []{.arithmatex}$\omega = 3$，由于 []{.arithmatex}$\omega \notin A$，故事件 []{.arithmatex}$A$ 没有发生。

### 事件的运算 {#_5}

由于我们将随机事件定义为了样本空间 []{.arithmatex}$\Omega$ 的子集，故我们可以将集合的运算（如交、并、补等）移植到随机事件上。记号与集合运算保持一致。

- 并（和）事件：事件的并 []{.arithmatex}$A \cup B$ 也可记作 []{.arithmatex}$A + B$，表示至少有一个事件发生。
- 交（积）事件：事件的交 []{.arithmatex}$A \cap B$ 也可记作 []{.arithmatex}$AB$，表示事件全部发生。

## 概率的定义和性质 {#_6}

### 古典概型 {#_7}

在概率论早期实践中，由于涉及到的随机现象都比较简单，具体表现为样本空间 []{.arithmatex}$\Omega$ 是有限集，且直观上所有样本点是等可能出现的，因此人们便总结出了下述定义（称为**传统概率模型**或**古典概率模型**或**拉普拉斯概率模型**）：

如果一个随机现象满足：

- 只有有限个基本结果。
- 每个基本结果出现的**可能性是一样的**。

那么对于每个事件 []{.arithmatex}$A$，定义它的概率为：

:::: {.arithmatex}
::: {.MathJax_Preview}
P(A)=\dfrac{\|A\|}{\|\Omega\|}
:::

$$P(A)=\dfrac{|A|}{|\Omega|}$$
::::

最经典的例子是，掷硬币、掷骰子。

或者用 []{.arithmatex}$\#(\cdot)$ 表示对随机事件（一个集合）大小的度量：

:::: {.arithmatex}
::: {.MathJax_Preview}
P(A)=\dfrac{\\(A)}{\\(\Omega)}
:::

$$P(A)=\dfrac{\#(A)}{\#(\Omega)}$$
::::

古典概型做题公式：

1.  记事件 []{.arithmatex}$A=\dots$。

2.  []{.arithmatex}$\Omega=\{\dots\}$ 共几个。

3.  []{.arithmatex}$A=\{\dots\}$ 共几个。

4.  []{.arithmatex}$P(A)=\dfrac{\#(A)}{\#(\Omega)}$。

后来人们发现这一定义可以直接推广到 []{.arithmatex}$\Omega$ 无限的一部分情景中，于是就有了所谓几何概型。

在古典概型中，最应当注意的是**一致的可能性**，例如扔两次硬币，一正一反就不应当是一个于两正、两反等概率的事件。

### 几何概型 {#_8}

在这个模型下，随机实验所有可能的结果是无限的，并且每个基本结果发生的**概率是相同的**。

几何概型定义，概率 []{.arithmatex}$=$ 有利区域测度 []{.arithmatex}$\div$ 总区域测度。当所求解问题可以转化为某种随机分布的特征数，比如随机事件出现的概率，或者随机变量的期望，就可以使用蒙特卡罗法。

通过大量随机抽样的方法，以随机事件出现的频率估计其概率，或者以抽样的数字特征估算随机变量的数字特征，并将其作为问题的解。

经常的，我们会因为概率相同犯错误，这也导致了 [Bertrand（伯特兰）悖论](https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)) 等问题的产生，于是也就诞生了概率的公理化描述。

### 概率公理 {#_9}

公理一：[]{.arithmatex}$0\le P(A)\le1(A\subset\Omega)$。

公理二：[]{.arithmatex}$P(\Omega)=1,P(\varnothing)=0$。

公理三：[]{.arithmatex}$A\cap B=\varnothing\iff P(A\cup B)=P(A)+P(B)$。

推论：

- 若 []{.arithmatex}$A\subset B$，则 []{.arithmatex}$P(A)<P(B)$（概率的单调性）。

- 若 []{.arithmatex}$A$ 与 []{.arithmatex}$B$ 对立，则 []{.arithmatex}$P(A)+P(B)=1$。

- 容斥原理：[]{.arithmatex}$P(A\cup B)=P(A)+P(B)-P(A\cap B)$。

其中上面第二条就是容斥原理的推论。

### 频率学派 {#_10}

频率学派强调通过数据出现的**频率**或比例，从样本数据中得出结论。

根据大数定律，样本数量越多，则其算术平均值就有越高的概率接近期望。

最经典的例子是，抛硬币正面向上的频率趋近于 []{.arithmatex}$0.5$。

### 主观概率 {#_11}

主观概率，是指建立在过去的经验与判断的基础上，根据对未来事态发展的预测和历史统计资料的研究确定的概率。主观概率反映的只是一种主观可能性，尽管有一定的科学性，但和能客观地反映事物发展规律的自然概率不同。

最经典的例子是，降雨概率。

## 条件概率 {#_12}

### 条件概率 {#_13}

当某事件已经发生时，一些随机事件的概率会因为已知信息的增加发生变化。

若已知事件 []{.arithmatex}$A$ 发生，在此条件下事件 []{.arithmatex}$B$ 发生的概率称为 条件概率，记作 []{.arithmatex}$P(B|A)$。

在样本空间中，若事件 []{.arithmatex}$A$ 满足 []{.arithmatex}$P(A) > 0$，则条件概率 []{.arithmatex}$P(\cdot|A)$ 定义为：

:::: {.arithmatex}
::: {.MathJax_Preview}
P(B\|A) = \frac{P(AB)}{P(A)}
:::

$$P(B|A) = \frac{P(AB)}{P(A)}$$
::::

条件概率有时候也称为**后验概率**，与先验概率相对。

1.  []{.arithmatex}$P(\Omega|A)=1$.

2.  若 []{.arithmatex}$B,C$ 互斥（[]{.arithmatex}$BC=\varnothing$）则：

    :::: {.arithmatex}
    ::: {.MathJax_Preview}
    P(BC)=P(B)+P(C)
    :::

    $$P(BC)=P(B)+P(C)$$
    ::::

    :::: {.arithmatex}
    ::: {.MathJax_Preview}
    P(PC\|A)=P(B\|A)+P(C\|A)
    :::

    $$P(PC|A)=P(B|A)+P(C|A)$$
    ::::

    :::: {.arithmatex}
    ::: {.MathJax_Preview}
    P(\bar B\|A)=1-P(B\|A)
    :::

    $$P(\bar B|A)=1-P(B|A)$$
    ::::

条件概率的计算有还有三个公式，我们详细讲解。

### 概率乘法公式 {#_14}

若 []{.arithmatex}$P(A) > 0$，则对任意事件 []{.arithmatex}$B$ 都有

:::: {.arithmatex}
::: {.MathJax_Preview}
P(AB) = P(A)P(B\|A)
:::

$$P(AB) = P(A)P(B|A)$$
::::

注意到这也就是条件概率的定义式。

### 全概率公式 {#_15}

全概率公式指出，对于 []{.arithmatex}$A,B$ 两组对立事件，

:::: {.arithmatex}
::: {.MathJax_Preview}
P(B)=P(A)P(B\|A)+P(\bar A)P(B\|\bar A)
:::

$$P(B)=P(A)P(B|A)+P(\bar A)P(B|\bar A)$$
::::

可以理解为，[]{.arithmatex}$A$ 发生后 []{.arithmatex}$B$ 发生，和 []{.arithmatex}$A$ 不发生但是 []{.arithmatex}$B$ 发生概率之和。

In general，若一组事件 []{.arithmatex}$A_1, \cdots, A_n$ 共同对立（两两不交、互相独立且和为 []{.arithmatex}$\Omega$），则对任意事件 []{.arithmatex}$B$ 都有：

:::: {.arithmatex}
::: {.MathJax_Preview}
P(B) = \sum\_{i=1}\^{n} P(A_i)P(B\|A_i)
:::

$$P(B) = \sum_{i=1}^{n} P(A_i)P(B|A_i)$$
::::

### Bayes 公式 {#bayes}

贝叶斯定理（也成贝氏定理）指出，若 []{.arithmatex}$P(A),P(B)>0$，则：

:::: {.arithmatex}
::: {.MathJax_Preview}
P(A\|B)=\dfrac{P(AB)}{P(B)}=\dfrac{P(A)P(B\|A)}{P(B)}
:::

$$P(A|B)=\dfrac{P(AB)}{P(B)}=\dfrac{P(A)P(B|A)}{P(B)}$$
::::

可以理解为将中间的 []{.arithmatex}$P(AB)$ 用概率乘法公式展开，向左向右写出。

也可以将 []{.arithmatex}$P(A)$ 提出来，剩余的部分 []{.arithmatex}$P(B|A)/P(B)$ 称为标准似然度。

带入全概率公式，于是有：

:::: {.arithmatex}
::: {.MathJax_Preview}
P(A\|B)=\dfrac{P(A)P(B\|A)}{P(A)P(B\|A)+P(\bar A)P(B\|\bar A)}
:::

$$P(A|B)=\dfrac{P(A)P(B|A)}{P(A)P(B|A)+P(\bar A)P(B|\bar A)}$$
::::

一般来说，设可能导致事件 []{.arithmatex}$B$ 发生的原因为 []{.arithmatex}$A_1, A_2, \cdots, A_n$（同样构成了**互斥**），则在 []{.arithmatex}$P(A_i)$ 和 []{.arithmatex}$P(B|A_i)$ 已知时可以通过全概率公式计算事件 []{.arithmatex}$B$ 发生的概率。但在很多情况下，我们需要根据「事件 []{.arithmatex}$B$ 发生」这一结果反推其各个原因事件的发生概率。

:::: {.arithmatex}
::: {.MathJax_Preview}
P(A_i\|B) = \frac{P(A_iB)}{P(B)} = \frac{P(A_i)P(B\|A_i)}{\sum\_{j=1}\^{n} P(A_j)P(B\|A_j)}
:::

$$P(A_i|B) = \frac{P(A_iB)}{P(B)} = \frac{P(A_i)P(B|A_i)}{\sum_{j=1}^{n} P(A_j)P(B|A_j)}$$
::::

## 事件的独立性 {#_16}

### 互斥和对立事件 {#_17}

**互斥事件**：[]{.arithmatex}$P(AB)=0$，即有 []{.arithmatex}$A$ 没 []{.arithmatex}$B$ 有 []{.arithmatex}$B$ 没 []{.arithmatex}$A$。

:::: {.arithmatex}
::: {.MathJax_Preview}
A,B\textsf{ 互斥}\iff AB=\varnothing
:::

$$A,B\textsf{ 互斥}\iff AB=\varnothing$$
::::

**对立事件**：其中必有一个发生的两个互斥事件。

:::: {.arithmatex}
::: {.MathJax_Preview}
A,B\textsf{ 对立}\iff AB=\varnothing,A\cup B=\Omega
:::

$$A,B\textsf{ 对立}\iff AB=\varnothing,A\cup B=\Omega$$
::::

对于互斥事件和对立事件（是互斥事件的一个特例）：

:::: {.arithmatex}
::: {.MathJax_Preview}
P(AB)=P(A)+P(B)
:::

$$P(AB)=P(A)+P(B)$$
::::

### 独立事件和独立性 {#_18}

**独立事件**：[]{.arithmatex}$A$ 发生不影响 []{.arithmatex}$B$ 而 []{.arithmatex}$B$ 发生也不影响 []{.arithmatex}$A$。

:::: {.arithmatex}
::: {.MathJax_Preview}
P(AB)=P(A)P(B)
:::

$$P(AB)=P(A)P(B)$$
::::

根据这个式子，如果 []{.arithmatex}$A,B$ 独立，那么 []{.arithmatex}$A$ 及其补集，[]{.arithmatex}$B$ 及其补集也应当都是独立的。

在条件概率中，若 []{.arithmatex}$A,B$ 独立：

:::: {.arithmatex}
::: {.MathJax_Preview}
P(A\|B)=\dfrac{P(AB)}{P(B)}=P(A)
:::

$$P(A|B)=\dfrac{P(AB)}{P(B)}=P(A)$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
P(B\|A)=\dfrac{P(AB)}{P(A)}=P(B)
:::

$$P(B|A)=\dfrac{P(AB)}{P(A)}=P(B)$$
::::

也可以用条件概率推导独立，这是 iff 的。

### 多个事件的独立性 {#_19}

对于多个事件 []{.arithmatex}$A_1, A_2, \cdots, A_n$，我们称其独立，当且仅当对任意一组事件 []{.arithmatex}$\{ A_{i_k} : 1 \leq i_1 < i_2 < \cdots < i_k \leq n \}$ 都有：

:::: {.arithmatex}
::: {.MathJax_Preview}
P( A\_{i_1}A\_{i_2} \cdots A\_{i_r} ) = \prod\_{k=1}\^{r} P(A\_{i_k})
:::

$$P( A_{i_1}A_{i_2} \cdots A_{i_r} ) = \prod_{k=1}^{r} P(A_{i_k})$$
::::

对于多个事件，一般不能从两两独立推出这些事件独立。考虑以下反例：

- 有一个正四面体骰子，其中三面被分别涂成红色、绿色、蓝色，另一面则三色皆有。现在扔一次该骰子，令事件 []{.arithmatex}$A,B,C$ 分别表示与桌面接触的一面包含红色、绿色、蓝色。

不难计算：

:::: {.arithmatex}
::: {.MathJax_Preview}
P(A) = P(B) = P(C) = \frac{1}{2}
:::

$$P(A) = P(B) = P(C) = \frac{1}{2}$$
::::

:::: {.arithmatex}
::: {.MathJax_Preview}
P(AB) = P(BC) = P(CA) = P(ABC) = \frac{1}{4}
:::

$$P(AB) = P(BC) = P(CA) = P(ABC) = \frac{1}{4}$$
::::

显然 []{.arithmatex}$A, B, C$ 两两独立，但由于 []{.arithmatex}$P(ABC) \neq P(A)P(B)P(C)$，故 []{.arithmatex}$A, B, C$ 不独立。

## 概率的应用 {#_20}

### 条件概率谬论 {#_21}

条件概率的谬论是假设 []{.arithmatex}$P(A|B)$ 大致等于 []{.arithmatex}$P(B|A)$。

根据 Bayes 公式：

:::: {.arithmatex}
::: {.MathJax_Preview}
P(A)P(B\|A)=P(B)P(A\|B)
:::

$$P(A)P(B|A)=P(B)P(A|B)$$
::::

最经典的例子是患病概率，考虑到灵敏度、特异度等因素，本文不予讲解，详见 [Wikipedia](https://en.wikipedia.org/wiki/Positive_and_negative_predictive_values)。
