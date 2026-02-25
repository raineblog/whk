# 恒定电流 \{#\_1}

## 电路概述 \{#\_2}

### 电流定义 \{#\_3}

电流：

- 电流：电荷的定向移动。

- 电流方向于正电荷运动方向相同，与负电荷（电子）运动方向相反。

电流的分类：

- 恒定电流：大小和方向都不变的电流。

- 直流电：方向不变的电流。

- 交流电：方向改变的电流。

物理学定义：

- 定义：单位时间内通过导体横截面的电荷量。

- 定义式：$I=\dfrac\{Q}\{t}$。

额外的，有微观表达式：$I=neSv$。

- 其中 $n$ 表示通过导体横截面的电子数。

- 其中 $e$ 表示电子的电荷量。

- 其中 $S$ 表示导体的横截面积大小。

- 其中 $v$ 表示导体中自由电子的运动速率。

三种速度数量级：

- 电子定向移动速率：$\pu\{10^-5m/s}$。

- 电子热运动速率：$\pu\{10^5m/s}$。

- 电子的传导速率：$\pu\{10^8m/s}$，即电场的形成速率。

电子运动速度这么低，为什么平常开灯的时候，按下开关的一瞬间灯就亮了呢？按下开关的一瞬间，导线内部的电场线光速建立好，使导线内部所有电子瞬间开始移动。注意这个过程是导线内所有电子同步开始移动的，虽然导线内开关处的电子移动到导线内灯泡处需要很长时间，但导线内灯泡处已经有电子了，这里的电子瞬间移动，就可以做功使灯泡发光。

电流既不依赖电路，也不依赖电源，任何电荷定向移动的情形都可以称作电流。如氢原子电子绕核运动可以等效为环形电流；原电池电解质溶液内离子的定向移动可以等效为电流；令一个摩擦后带上负电的橡胶棒向右运动，也可以等效为一个向左的电流。

一个 $\ce\{H}$ 原子的电子绕核运动可等效为一环形电流。已知电子电量大小 $e$，周期 $T$，绕质子顺时针运动。求电流的方向和电流强度 $I$ 的大小。

我们知道，「电流的电流强度的大小是多少」这种问题，应该在电流是恒定电流的时候才有意义。然而这类环形电流模型有点不符合常规的恒定电流：它并不是相当于导线内部处处有电子，而只是一个孤立电子在运动。这会导致一个问题：考虑钦定 $\dfrac T 2$ 这个时间，那么一半的横截面被电子经过，另一半却没有，这真的是恒定电流吗？

与力学不同，载流子（这里是电子）是一粒一粒的，因此电流通常是在 统计意义下 讨论的，并不适用对于极度微小的时间上的讨论。事实上，对于恒定电流，我们不能保证在两段相等的微小时间内，经过电路中某一点的电荷总量绝对相同。足够严谨的说法是：在宏观尺度上选取任意两段相等的时间，经过电路中某一点的电荷总量几乎不变，也即「恒定」是一个宏观意义上统计出的结果。

电子绕核运动速率很快，$T$ 很小。在统计意义上，对宏观尺度的时间计时，那么每个横截面经过电荷总量都近似相等，且与时间成正比，这就说明它是一个恒定电流。

那怎么计算这个恒定电流的大小呢？在统计意义上每个横截面经过的总电荷总量大小都近似相等，且与时间成正比，那这个比值就是电流大小了！分析一下这个比值，考虑经过宏观时间 $t$ 后，电子应近似做了 $\dfrac t T$ 次圆周运动，那么经过每个横截面的总电荷总量大小为 $\dfrac\{t e}T$。除以总时间 $t$ 即可得到电流大小 $\dfrac\{e}T$。

或者，可以直接钦定经过时间为 $T$ 的倍数，比如直接钦定为 $T$。那么经过每个横截面的电荷总量就是 $e$，可以直接计算得 $\dfrac\{e}T$。这里虽然选用了微小时间，但是它可以保证计算出的结果在统计意义上也正确，因为在统计意义上，一段宏观时间的电子运动就是很多次圆周运动拼起来（一次运动了部分圆周的运动可以忽略），而无论多少次圆周运动拼起来，统计意义上计算出的电流都等于 $\dfrac\{e}T$。

因此，对于单电子环形电流问题，取周期 $T$ 计算经过每个横截面的总电荷总量大小即可。

电流的方向为电子定向移动方向的反方向，即逆时针方向。经过时间 $T$ 后，经过任一横截面的电荷总量大小为 $e$。因此，电流大小为 $\dfrac\{\mathrm\{e}}T$。

### 欧姆定律 \{#\_4}

欧姆定律表明：处于某状态的导电体（**定温下**），其两端的电压与通过电导体的电流成正比，即：

$$
U\propto I
$$

- 人教版高中物理教材指出：欧姆定律适用于金属、电解液导电，不适用气态导体和半导体导电。

- 哈里德《物理学基础》指出，欧姆定律要求通过一器件的电流始终正比于加到该器件上的电势差。

也就是说，欧姆定律**仅适用于线性电路**。

电动势与电流的比例，即电阻，不会随着电流而改变。根据焦耳定律，导电体的焦耳加热与电流有关，当传导电流于导电体时，导电体的温度会改变，这称为温度效应。电阻对于温度的相关性，使得在典型实验里，电阻跟电流有关，从而很不容易直接核对这形式的欧姆定律。

需要注意的是，欧姆定律并没有提到电阻，而电阻的定义式与欧姆定律非常类似：

$$
R=\dfrac\{U}\{I}
$$

实际上有一定区别：

- 欧姆定律仅限于线性电路。

- 电阻的定义式对于任意元件成立，因为电阻与电路无关。

这也是欧姆定律的一个常见错误认知^[1](#fn:note100)\{.footnote-ref}^。

温度降低时，金属导体电阻率将会减小，一些金属在温度特别低时电阻可以减小到 $0$，称之为超导现象。目前发现的超导体只能在很低温度下保持超导性质。

在恒定电场的作用下，导体中的自由电荷做定向运动，在运动过程中与导体内不动的粒子不断碰撞，碰撞阻碍了自由电荷的定向运动（这个阻碍作用对应的就是导体的电阻）。

超导体上欧姆定律不成立，可以这样认为：欧姆定律适用于「电荷仅受电场力和与导体内不动粒子碰撞产生的阻力两个力作用」的情形，然而这里「电荷仅受电场力作用」。

### 电阻定律 \{#\_5}

我们知道电阻的决定式如下：

$$
R=\rho\dfrac\{l}\{S}
$$

其中 $\rho$ 为电阻率。

而对于一个均匀的柱体电阻，可以得到：

$$
R=\rho\dfrac\{l}\{S}=\rho\dfrac\{l^2}\{V}
$$

### 焦耳定律 \{#\_6}

发热量：

$$
Q=I^2Rt
$$

电功推导：

$$
W=Uq=UIt
$$

而热功率和电功率分别除以时间就可以了。

以上三个公式，适用于**任何电路**，而对于纯电阻电路才可以根据欧姆定律得到 $I^2R=UI$，我们将在电动机部分详细解释。

## 电路应用 \{#\_7}

### 电动势 \{#\_8}

电动势表征一些电路元件供应电能的特性（非静电力做功的本质），这些电路元件称为电动势源，而电动势源所供应的能量每单位电荷是其电动势，有公式表达：

$$
\mathcal\{E}=\dfrac\{W}\{Q}
$$

即把 $\pu\{1C}$ 正电荷从负极运回正极所做的功。通常，这能量是分离正负电荷所做的功，由于这正负电荷被分离至元件的两端，会出现对应电场与电势差。

![alt text](/static/image/image.a4569e067c.avif)
|                   符号                   |                   符号                   |
| :------------------------------------: | :------------------------------------: |
| 理想电压源 <img alt="image" src={image1} /> | 理想电流源 <img alt="image" src={image2} /> |
| 受控电压源 <img alt="image" src={image3} /> | 受控电流源 <img alt="image" src={image4} /> |
|  单电池 <img alt="image" src={image5} />  |  电池组 <img alt="image" src={image6} />  |

电池内阻相当于一个电池串联一个电阻，如果没有特殊说明，**电池的内阻不可忽略**。

### 串并联规律 \{#\_9}

串联规律：

- 电流 $I$ 相同、分压 $U=U\_1+U\_2$。

- 等效电阻为一个 $R=R\_1+R\_2$ 的电阻。

并联规律：

- 电压 $U$ 相同，分流 $I=I\_1+I\_2$。

- 等效电阻为一个 $R=\dfrac\{R\_1R\_2}\{R\_1+R\_2}$ 的电阻，记为鸡在和上飞。

串联电路：根据以上两个基本特点，运用欧姆定律，很容易得到以下三个推论。

1. 串联电路的总电阻 (等效电阻) 等于各电阻之和，即

   $$
   R=R\_1+R\_2+R\_3
   $$

2. 串联电路中各电阻的电压与它们的阻值成正比，或者说，电压按阻值成正比分配，即

   $$
   U\_1:U\_2:U\_3=R\_1:R\_2:R\_3
   $$

3. 串联电路中各电阻消耗的电功率与它们的阻值成正比，即

   $$
   P\_1:P\_2:P\_3=R\_1:R\_2:R\_3
   $$

并联电路：根据以上两个基本特点，运用欧姆定律，也可以得到三条推论。

1. 并联电路的总电阻 (等效电阻) 的倒数等于各电阻的倒数之和，即

   $$
   \frac\{1}\{R} = \frac\{1}\{R\_1} + \frac\{1}\{R\_2} + \frac\{1}\{R\_3}
   $$

2. 并联电路中各支路的电流与它们的电阻的倒数成正比，即

   $$
   I\_1:I\_2:I\_3 = \frac\{1}\{R\_1}:\frac\{1}\{R\_2}:\frac\{1}\{R\_3}
   $$

3. 并联电路中各电阻消耗的电功率与它们的电阻的倒数成正比，即

   $$
   P\_1:P\_2:P\_3 = \frac\{1}\{R\_1}:\frac\{1}\{R\_2}:\frac\{1}\{R\_3}
   $$

### 电源的串并联 \{#\_10}

我们只考虑 $n$ 个一样的电源（$E,r$）串并联：

- 串联：电动势增加，内阻增加。

  $$
  \begin\{cases} E'&=nE\ r'&=nr \end\{cases}
  $$

- 并联：电动势不变，内阻减小。

  $$
  \begin\{cases} E'&=E\ r'&=r/n \end\{cases}
  $$

聪明的你想到用 $n^2$ 个电池连成方格，于是电动势增加，内阻不变。

### 伏安特征曲线 \{#\_11}

- 只有图像是一条过原点的直线，才是线性元件，斜率是 $1/R$。

- 电灯泡随着电流、电压、电功率增大，电阻增大。

- 曲线向 $U$ 轴偏移为电压增加电阻变大，向 $I$ 轴偏移为电压增大电阻变小。

### 电流的能量 \{#\_12}

电源的功率：$P\_\{源} = I\epsilon = \frac\{\epsilon^2}\{(R+r)}$。

电源输出功率：

$$
P\_\{出} = IU = \frac\{\epsilon^2}\{(R+r)} \cdot R = \frac\{\epsilon^2}\{\frac\{(R+r)^2}\{R}+4r}
$$

功率最值问题：

- 若研究对象为定值：$R\_变=0$ 时功率最大。

- 若研究对象在改变：$R\_研=R\_\{其他}$ 时功率最大。

当 $R=r$ 时电源输出功率为最大：$P\_\{\max} = \frac\{\epsilon^2}\{4r}$，此时电源效率：$\eta = 50%$。

![alt text](/static/image/image-6.2f30b23987.avif)
### 闭合电路 \{#\_13}

基本概念：

- 内电路：电源内部的电路，$U\_内=Ir\_内 $。

- 外电路：电源外部的电路，$U\_外=E-U\_内 $。

- 测外电压（路端电压）：直接把电压表并在电池两端。

在闭合电路部分，除非特殊说明，电表和电池一般不能看做理想的。

- 理论基础：串并联规律、欧姆定律。

- 滑动变阻器电阻增大 $\implies$ 总电阻增大 $\implies$ 总电流减小 $\implies$ 内电路电压减小、外电路电压增大。

- 总电流减小，一条支路电流增大，另一条支路（滑动变阻器所在支路）电流减小。路端电压增大，滑动变阻器串联的电阻电压减小，滑动变阻器电压增大。

- 电路故障：将短路视为电阻减小到零，断路视为电阻增加到无穷大。

- 串反并同：前提是电源有内阻，外电路仅有电阻串联后并联。对于电流、电压、电功率，与滑动变阻器串联的用电器与滑动变阻器阻值变化相反，与滑动变阻器并联的用电器与滑动变阻器阻值变化相同。

- 未知电源电动势、内阻：联立两个方程，

  $$
  E=U\_外+Ir\_内
  $$

  对两个状态列方程即可。

$\Delta U/\Delta I$ 问题：

- 若研究对象电阻为定值：

  $$
  \dfrac\{\Delta U}\{\Delta I}=R
  $$

- 若研究对象电阻在改变：

  $$
  \dfrac\{\Delta U}\{\Delta I}=\dfrac\{\Delta(E-U)}\{\Delta I}=R\_\{其他}
  $$

含容电路：

1. 恒定电路中电容器所在支路没有电流流过，把电容器看做一个理想电压表。

2. 通过电势法求出电容器两端的电势差，通过 $Q=CU$ 算出电荷量。

3. 如果电容器被直接串联在电池上，电路中没有电流，电容器电势差即为电源电动势。

## 回路基础 \{#\_14}

### 电压源和电流源 \{#\_15}

电压源（理想电压源）具有两个基本的性质：

1. 它的端电压为定值 $U$，或为一时间函数 $U(t)$，与流过的电流无关。

2. 电压源自身电压是确定的，而流过它的电流是任意的。

常见实际电源的工作机理比较接近电压源，例如发电机以及蓄电池。电压源具有低内阻并且作为恒压电路工作。由于短路时会流过大电流，因此需要安全装置。

实际上，如果一个电压源在电流变化时，电压的波动不明显，我们通常就假定它是一个理想电压源。

电流源（理想电流源）具有两个基本的性质：

1. 它提供的电流是定值 $I$，或是一定的时间函数 $I(t)$ 与两端的电压无关。

2. 电流源自身电流是确定的，而它两端的电压是任意的。

电流源具有很大的内阻（理想状态是内阻无限大）并且作为恒流电路工作。由于负载波动，电压波动较大。实际上，如果一个电流源在电压变化时，电流的波动不明显，我们通常就假定它是一个理想电流源。

像光电池一类的器件，工作时的特性比较接近电流源。

:::note

电压源的工作原理

如图：

![image](data:image/avif;base64,AAAAHGZ0eXBhdmlmAAAAAG1pZjFhdmlmbWlhZgAAANZtZXRhAAAAAAAAACFoZGxyAAAAAAAAAABwaWN0AAAAAAAAAAAAAAAAAAAAAA5waXRtAAAAAAABAAAAImlsb2MAAAAAREAAAQABAAAAAAD6AAEAAAAAAAABGQAAACNpaW5mAAAAAAABAAAAFWluZmUCAAAAAAEAAGF2MDEAAAAAVmlwcnAAAAA4aXBjbwAAAAxhdjFDgSACAAAAABRpc3BlAAAAAAAAAHcAAABfAAAAEHBpeGkAAAAAAwgICAAAABZpcG1hAAAAAAAAAAEAAQOBAgMAAAEhbWRhdBIACgk4GbteYQENBpAyiQJEZAAABQDX/qzfjxPWetijxNB5ryS9uPjaOfRVgr1FW/rIbpRAvXCUmemCcK697mFKRsHqbV1kpqGFy+ON3YQKSFVXy1uWqD7rUpZXYcQSbNHtcFe1cCYAoZz4wMJiav+BxczwFHj/3/Di4nViG9/XRLoTx7DdjkhAh+UOOe2GaTuPWJoK3nx9gKOlRIcX1GY2b56KqaYYAOqbXOpUTT83MfWXzNQGWHmafKnl7oMvX63wbUyWC4tM8V+V4vWDdiUo50rArtd1ZPzaE09yAhzo0ZVV/XZ5AS7D27MIdACOINYv97rkagTGC8fAmtob5tJl0Mnx6jJm6ymVXmD1e23ARtYfOfHQwtRA)
设 $E\_S$ 为电源电动势，$R\_S$ 为内阻，$R$ 为负载，$V\_0$ 为施加电压，$I$
为电流：

$$
I=\dfrac\{E\_S}\{R\_S+R}
$$

因此：

$$
V\_0=IR=\dfrac\{R}\{R\_S+R}E\_S
$$

如果 $R\ll R\_S$，则 $V\_0\doteq E\_S$。因此，输出电压的波动不明显。

:::

:::note

电流源的工作原理

如图：

![image](data:image/avif;base64,AAAAHGZ0eXBhdmlmAAAAAG1pZjFhdmlmbWlhZgAAANZtZXRhAAAAAAAAACFoZGxyAAAAAAAAAABwaWN0AAAAAAAAAAAAAAAAAAAAAA5waXRtAAAAAAABAAAAImlsb2MAAAAAREAAAQABAAAAAAD6AAEAAAAAAAABZAAAACNpaW5mAAAAAAABAAAAFWluZmUCAAAAAAEAAGF2MDEAAAAAVmlwcnAAAAA4aXBjbwAAAAxhdjFDgSACAAAAABRpc3BlAAAAAAAAAIQAAABhAAAAEHBpeGkAAAAAAwgICAAAABZpcG1hAAAAAAAAAAEAAQOBAgMAAAFsbWRhdBIACgk4HaDwMICGg0gy1AJEZAAABQDVCA26uoVDJOE9hyfYEXDfusMqr40w4liJgKKIjtUchoRn/ponD+LOAiNyvd4yuT1Ki97RQ8mi68WSl7tYG7J59Vv4OW6O+WRAN9XjY/+eKgWGjlLCLq3+mL9hjNuiLzBRAtz8G8DmSG1wpy8OSqtI3lJbgPX5uVgN02GkamQTI+tbTC4jBDxcJ5FnMjPKUp1VPIHlXHdhSAgqYKnL2etqdLEa/oNChVlI0noaJcZo0tIq4CbviriFQ0Lw+zZu3jpdZa1LomNxTZkuQuIZl74Z9cYAAgcUm+dWqMEhMMl1Ml7hEjQEZz762cUrZBOL80l1fEexscpGGotjCsfpdzmjvtOBB/8GiVfOL0M36U/o+9H+OwZtbidYzXDmeakIvmbUnex1AyKfeSe+KhkoLOPH7fOBKsURO36Kb9Nmw8ivd/S/nQu2OYXsXv34NbZA)
设 $I\_S$ 为电源电流，$G\_S$ 为内部电导，$G$ 为负载电导，$V\_0$
为施加电压，$I$ 为电流：

$$
I\_S=V\_0(G\_S+G)=V\_0G\_S+I
$$

因此：

$$
V\_0=\dfrac\{I\_S}\{G\_S+G}
$$

如果 $G\ll G\_S$，则
$I\_S\doteq I$。因此，输出电压会因负载波动而发生较大变化。

:::

戴维南定理和诺尔顿定理：

![alt text](/static/image/image-7.c703f80b8b.avif)
![alt text](/static/image/image-8.ca24790430.avif)
### 基尔霍夫电路定律 \{#\_16}

基尔霍夫电路定律（基尔霍夫定律）涉及了电荷的守恒及电势的保守性。

1. 支路：

   - 每个元件就是一条支路。
   - 串联的元件我们视它为一条支路。
   - 在一条支路中电流处处相等。

2. 节点：

   - 支路与支路的连接点。
   - 两条以上的支路的连接点。

3. 回路：

   - 闭合的支路。
   - 闭合节点的集合。

基尔霍夫电路定律包括以下两条电路学定律：

- 基尔霍夫电流定律（基尔霍夫第一定律，KCL）。

- 基尔霍夫电压定律（基尔霍夫第二定律，KVL）。

基尔霍夫定律建立在电荷守恒定律、欧姆定律及电压环路定理的基础之上，在稳恒电流条件下严格成立。

当基尔霍夫第一、第二方程组联合使用时，可正确迅速地计算出电路中各支路的电流值。

对于含有电感器的电路，必需将基尔霍夫电压定律加以修正。

由于含时电流的作用，电路的每一个电感器都会产生对应的电动势 $E\_k$。

必需将这电动势纳入基尔霍夫电压定律，才能求得正确答案。

**例题一**：

![image](data:image/avif;base64,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)
可以列出三个式子：

$$
\left\{\begin\{array}\{c} E\_1&=\&i\_1r\_1+iR\ E\_2&=\&i\_2r\_2+iR\ i&=\&i\_1+i\_2 \end\{array}\right.
$$

已- 知 $E\_1,E\_2,r\_1,r\_2,R$，可以求出 $i\_1,i\_2,i$。

**例题二**：

![image](/static/image/kl2.ff95bfbe4b.avif)
根据基尔霍夫第一定律：

$$
i\_1=i\_2+i\_3
$$

将基尔霍夫第二定律应用于回路 $s\_1$：

$$
\mathcal\{E}\_1=R\_1i\_1+R\_2i\_2
$$

将基尔霍夫第二定律应用于回路 $s\_2$：

$$
\mathcal\{E}\_1+\mathcal\{E}\_2+R\_3i\_3=R\_2i\_2
$$

已知：$R\_1=100\Omega$，$R\_2=200\Omega$，$R\_3=300\Omega$，$\mathcal\{E}\_1=3V$，$\mathcal\{E}\_2=4V$。

解得：

$$
\left\{\begin\{array}\{c} i\_1&=&1/1100\&A\ i\_2&=&4/275\&A\ i\_3&=&-3/220\&A \end\{array}\right.
$$

注意到电流 $i\_3$ 带了负号，这意味着我们 $i\_3$ 的假定方向不正确。

这也意味着基尔霍夫电路定律解题不完全需要电流方向已知。

### 基尔霍夫电流定律 \{#\_17}

又称：基尔霍夫第一定律，KCL。

定义：所有进入某节点的电流的总和等于所有离开这节点的电流的总和。

或者：设电流流入为正，流出为负，则所有涉及某节点的电流的代数和等于零。

基尔霍夫电流定律是节点分析的基础定律。

对于方程表达：$\sum i\_k=0$；其中，$i\_k$ 是与这节点相连接的第 $k$ 个支路的电流。

如图，有 $i\_2+i\_3=i\_1+i\_4$，或者可以写成 $i\_2+i\_3-i\_1-i\_4=0$ 的形式。

![image](data:image/avif;base64,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)
### 基尔霍夫电压定律 \{#\_18}

又称：基尔霍夫第二定律，KVL。

定义：沿着闭合回路所有器件两端的电势差（电压）的代数和等于零。

或者：沿着闭合回路的所有电动势的代数和等于所有电压降的代数和。

基尔霍夫电压定律是网目分析的基础定律。

对于方程表示：$\sum v\_k=0$；其中，$v\_k$ 是器件两端的电压。

基尔霍夫电压定律不仅应用于闭合回路，也可以把它推广应用于回路的部分电路。

- 顺着电流的方向走，如果设定的电流是 $I$，走过的电阻是 $R$，则电压降低 $IR$，逆着电流走，则升高 $IR$。
- 走过一个电动势为 $E$ 的电源，如果是负到正，则电压升高 $E$；如果是正到负，则电压降低 $E$。
- 当然，更常用的方法是，设的时候不考虑正负，结果带入符号。

如图，有 $v\_1+v\_2+v\_3=v\_4$，或者可以写成 $v\_1+v\_2+v\_3-v\_4=0$ 的形式。

![image](/static/image/kvl.d22ae31b04.avif)
在具体使用回路电压方程时，应注意：

1. 选用的回路中，必须有一段是没有用过的电路。

2. 设定各条支路中电流的方向，在电流方向不明确的情况下，可以任意设。如果最后解出来的电流值为正，则真实电流方向与设定的方向相同；如果最后解出来的电流值为负，则真实电流方向与设定的方向相反。

## 分析拓展 \{#\_19}

### 线性电路 \{#\_20}

线性元件：

- 在电路中电流与电压有线性关系的电子元件，例如金属导体和电解液。

- 在温度不变的情况下，其两端电压和电流的关系就可以近似的认为是线性的。

- 理想的电阻是最普遍的线性元件，常见的线性元件还有理想的电容和电感。

- 在伏安特性曲线中，表示为一条过坐标轴原点的直线的器件，一定是线性元件。

- 注意：材料并不是线性元件的决定因素，例如避雷器在高电压下电阻值变小。

线性电路：

- 电子线路的基本类型之一，是指响应与输入信号成正比的电路。

- 从构成上，线性电路是指完全由线性元件，独立电源和线性受控源构成的电路。

- 其特点是输入信号的变化会导致输出信号的相应变化，输出信号与输入信号之间存在线性相关性。

### 叠加定理 \{#\_21}

叠加定理的描述：

- 定义上：对于一个线性系统，一个含多个独立源的双边线性电路的任何支路的响应，等于每个独立源单独作用时的响应的代数和，此时所有其他独立源被替换成他们各自的阻抗。

- 具体的：在线性电路中，任一支路的电压或电流（不包括功率等），都等于独立电源单独作用在该支路产生的电压和电流的代数和。

- 形式化：在一个线性元件组成的电路中，一条电路上的电压和电流，是周围其他电压源或电流源在这条电路上单独作用后叠加在一起产生的。

- 还有的：对于任一线性网络，若同时受到多个独立电源的作用，则这些共同作用的电源在某条支路上所产生的电压或电流等于每个独立电源各自单独作用时，在该支路上所产生的电压或电流分量的代数和。

求解步骤：

1. 做出每个独立电源单独作用的电路分图，不作用的独立源置零：

   - 电压源短路：从而消除电压，即令 $V = 0$；
   - 电流源开路：从而消除电流，即令 $I = 0$。

2. 求各电路分图中的相应，求代数和。

注意事项：

1. 只适用于求电压、电流，不适用于求功率；也不适用于非线性电路。
2. 某个独立电源单独作用时，其余独立源全为零值。
3. 代数和指分量参考方向与原方向一致取正，不一致取负。
4. 要计算电功率，我们应该先用叠加定理得到各线性器件的电压和电流，然后计算出倍增的电压和电流的总和。

线性电路的**齐次定理**，即叠加定理的齐次性：

在线性电路中当所有独立源同时缩放 $K$ 倍（$K$ 为实常数）时，响应也将同样增大或缩小 $K$ 倍。

### 无穷电路 \{#\_22}

1. 一类比较简单的无穷电路所含的器件是相同的，如图所示的电路就属于这一类，组成电路的所有电阻的阻值都是 $R$。

   <img alt="alt text" src={image16} />

   不难看出，这个电路是由很多单元组成的，每一个单元包含三个电阻，既然电路的右端是无穷的，那么左端多一个单元、少一个单元是不影响整个电路的电阻的，也就是说从 $A,B$ 两点向右看和从 $C,D$ 两点向右看的电阻是一样的，设从 $C,D$ 两点向右看的电阻是 $R\_x$，那么有：

   $$
   \dfrac\{R\_xR}\{R\_x+R}+2R=R\_x
   $$

   解得 $R\_x=(\sqrt3+1)R$。

2. 另一类比较复杂的无穷电路所含的器件是不同的，但有一定的规律，如图所示的电路就属于这一类，电路也同样由九数多个单元组成，相邻的后面一个单元电阻的阻值要比前一个单元的阻值大一倍。

   <img alt="alt text" src={image17} />

   这一类无穷电路需要寻找规律，把从 $A,B$ 向右看的总电阻和从 $A',B'$ 向右看的总电阻进行比较，后者对应的单元都要比前者大一倍，所以后者的总电阻也要比前者大一倍，设从 $A,B$ 向右看的总电阻为 $R\_x$，那么有：

   $$
   \dfrac\{2R\_x\cdot R}\{2R\_x+R}+2R=R\_x
   $$

   解得 $R\_x=(\sqrt\{41}+5)R/4$。

### 对称性简化 \{#\_23}

所谓对称性简化，就是利用电路网络中可能存在的各种对称性，作出某种判断或结论，以简化等效电阻计算。

![alt text](data:image/avif;base64,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)
平衡对称电路：

- 对一个电路，用垂直平分端口的平面横切，可将该电路切成上下完全相同的两部分，而且这两部分之间没有交叉连接和支路，这种电路称为**平衡对称电路**。

- 所用的横切面，即该电路对端口的**平衡对称面**，如右图中的 $OO'$ 平面。一般情况下，平衡对称面只有一个。如在端口处加上电压，则在平衡对称面上的点都是等势点，该平面是一个**等势面**。

![alt text](/static/image/image-15.5584684ff8.avif)
传递对称电路：

- 对一个电路，用过端口的平面直切，可将该电路切成左、右完全相同的两部分，这种电路称为**传递对称电路**。

- 所用的直切面，即该电路的**传递对称面**，如右图中的 $SS'$ 平面。传递对称面可能不止一个。与传递对称面对称的点称为**传递对称点**。如在端口处加上电压，每一对传递对称点的电势都是相等的。

应当指出的是，对称性简化往往并不给出等效电阻的某种直接计算公式，而只是使电阻的计算得到简化，最终的结果仍有赖于电阻串、并联的公式，电流分布法，极限法等计算完成。

## 一道例题 \{#\_24}

### 题目描述 \{#\_25}

有电路如图乙所示（图中电流表为理想电流表）：

![alt text](/static/image/image-16.80e914126e.avif)
电路参数为：$R\_1=1\Omega$，$R\_2=3\Omega$，$R\_3=2\Omega$，$R\_4=3\Omega$，$E\_1=3V$，$r\_1=2\Omega$，$E\_2=6V$，$r\_2=3\Omega$，$E\_3=9V$，$r\_3=1\Omega$。

电路正常工作时，电流表的示数是多少？

### 基尔霍夫电路定律 \{#\_26}

如图，存在两条回路 $s\_1$、$s\_2$，假设电流流向为从 $E\_2$、$E\_3$ 正极出发，干路、支路电流分别为 $i\_1$，$i\_2$、$i\_3$：

![alt text](/static/image/image-17.30ab537b98.avif)
对节点 $K$ 应用基尔霍夫第一定律，得 $i\_1-i\_2-i\_3=0$。

对回路 $s\_1$、$s\_2$ 分别应用基尔霍夫第二定律，最终可列出方程组：

$$
\begin\{cases} i\_1&=i\_2+i\_3\ E\_2&=i\_2r\_2+i\_2R\_2+i\_1R\_1+i\_1R\_4+i\_1r\_1+E\_1\ E\_3&=i\_3r\_3+i\_3R\_3+i\_1R\_1+i\_1R\_4+i\_1r\_1+E\_1 \end\{cases}
$$

代数，得：

$$
\begin\{cases} i\_1&=i\_2+i\_3\ 6V&=3\Omega\cdot i\_2+3\Omega\cdot i\_2+1\Omega\cdot i\_1+3\Omega\cdot i\_1+2\Omega\cdot i\_1+3V\ 9V&=1\Omega\cdot i\_3+2\Omega\cdot i\_3+1\Omega\cdot i\_1+3\Omega\cdot i\_1+2\Omega\cdot i\_1+3V \end\{cases}
$$

化简得：

$$
\begin\{cases} i\_1&=i\_2+i\_3\ 3V&=6\Omega\cdot i\_2+6\Omega\cdot i\_1\ 6V&=3\Omega\cdot i\_3+6\Omega\cdot i\_1 \end\{cases}
$$

解得：

$$
\begin\{cases} i\_1&=5/8\&A\ i\_2&=-1/8\&A\ i\_3&=3/4\&A \end\{cases}
$$

分析可知，我们假设的 $i\_2$ 电流流向是错误的，而电流表示数为 $\dfrac\{5}\{8}A$。

### 电路的叠加定理 \{#\_27}

忽略电流表，可以发现图中仅存在电阻和电压源，因此该电路是线性电路，存在电路的叠加原理。

分别考虑 $E\_1$，$E\_2$，$E\_3$ 的影响，设 $I\_1$、$I\_2$、$I\_3$ 其电流表的示数，以电流从上到下为正值，从下到上为负值：

![alt text](/static/image/image-18.f042dfd135.avif)
极易得：

$$
\begin\{array}\{l} I\_1&=-\dfrac\{E\_1}\{r\_1+R\_1+R\_4+\dfrac\{(r\_2+R\_2)(r\_3+R\_3)}\{r\_2+R\_2+r\_3+R\_3}}\\\[2em] &=-\dfrac\{3V}\{2\Omega+1\Omega+3\Omega+\dfrac\{(3\Omega+3\Omega)(1\Omega+2\Omega)}\{3\Omega+3\Omega+1\Omega+2\Omega}}\\\[2em] &=-\dfrac\{3}\{8}A \end\{array}
$$

$$
\begin\{array}\{l} I\_2&=\dfrac\{E\_2}\{r\_2+R\_2+\dfrac\{(r\_3+R\_3)(r\_1+R\_1+R\_4)}\{r\_3+R\_3+r\_1+R\_1+R\_4}}\times\dfrac\{r\_3+R\_3}\{r\_3+R\_3+r\_1+R\_1+R\_4}\\\[2em] &=\dfrac\{6V}\{3\Omega+3\Omega+\dfrac\{(1\Omega+2\Omega)(2\Omega+1\Omega+3\Omega)}\{1\Omega+2\Omega+2\Omega+1\Omega+3\Omega}}\times\dfrac\{1\Omega+2\Omega}\{1\Omega+2\Omega+2\Omega+1\Omega+3\Omega}\\\[2em] &=\dfrac\{1}\{4}A \end\{array}
$$

$$
\begin\{array}\{l} I\_3&=\dfrac\{E\_3}\{r\_3+R\_3+\dfrac\{(r\_2+R\_2)(r\_1+R\_1+R\_4)}\{r\_2+R\_2+r\_1+R\_1+R\_4}}\times\dfrac\{r\_2+R\_2}\{r\_2+R\_2+r\_1+R\_1+R\_4}\\\[2em] &=\dfrac\{9V}\{1\Omega+2\Omega+\dfrac\{(3\Omega+3\Omega)(2\Omega+1\Omega+3\Omega)}\{3\Omega+3\Omega+2\Omega+1\Omega+3\Omega}}\times\dfrac\{3\Omega+3\Omega}\{3\Omega+3\Omega+2\Omega+1\Omega+3\Omega}\\\[2em] &=\dfrac\{3}\{4}A \end\{array}
$$

根据叠加定理，得出电流表示数 $I=I\_1+I\_2+I\_3=-\dfrac\{3}\{8}+\dfrac\{1}\{4}+\dfrac\{3}\{4}=\dfrac\{5}\{8}A$。

### 电流源与电压源 \{#\_28}

这也是原题想让我们应用的方法，这里先对题目的铺垫加以简单总结。

我们发现，一个内阻为 $r$ 的电压源 $E$，等效如图丙。

其串联一个总电阻为 $R$ 的用电器（或等效用电器）后，干路电流为：

$$
I=\dfrac\{E}\{r+R}
$$

我们发现 $E/r$ 为电源的特性，于是想办法凑出来这个形式：

$$
I=\dfrac\{E}\{r}\times\dfrac\{r}\{r+R}
$$

注意到后面的式子就是并联分流公式，我们转化电路形如图丁。

![alt text](/static/image/image-21.3205f10c78.avif)
于是，我们就把一个内阻为 $r$ 的电压源 $E$ 串联一个总电阻为 $R$ 的用电器，等效转化为了一个电流源 $E/r$ 并联上原电压源内阻，以及用电器 $R$。

回到问题，（如图）我们可以把原电压源 $E\_2$、$E\_3$ 及其内阻、支路电阻等效转化为一个电压源：

![alt text](/static/image/image-19.8728900e80.avif)
- 把电压源 $E\_2$ 同其内阻 $r\_2$ 及并联的电阻 $R\_2$ 抽象为一个电压源 $E'\_2$，内阻为 $(r\_2+R\_2)$，也就等效为一个电流源 $E\_2/(r\_2+R\_2)$，并联电阻 $(r\_2+R\_2)$；具体的，电阻 $r\_2'=r\_2+R\_2=6\Omega$，电流 $I\_2'=E\_2/r\_2'=6V/6\Omega=1A$。
- 把电压源 $E\_3$ 同其内阻 $r\_3$ 及并联的电阻 $R\_3$ 抽象为一个电压源 $E'\_3$，内阻为 $(r\_3+R\_3)$，也就等效为一个电流源 $E\_3/(r\_3+R\_3)$，并联电阻 $(r\_3+R\_3)$；具体的，电阻 $r\_3'=r\_3+R\_3=3\Omega$，电流 $I\_3'=E\_3/r\_3'=9V/3\Omega=3A$。

观察到，这两个电流源（电流流向一致，电流大小相加）就可以合并为一个电流源。

具体的，电阻 $r'=(3\times6)/9=2\Omega$，电流 $I'=1A+3A=4A$；

这个电流源也就等效于一个电压源，电压为 $E'=2\Omega\times4A=8V$，$R'=2\Omega$。

其电流方向与 $E\_1$ 相反，电压相减 $V=E'-E\_1=8V-3V=5V$，

其总电阻 $R=R\_1+R\_4+r\_1+r'=1\Omega+3\Omega+2\Omega+2\Omega=8\Omega$。

于是，电流表示数即为 $I=V/R=5V/8\Omega=\dfrac\{5}\{8}A$。

### 简单欧姆定律 \{#\_29}

我们把原图抽象为三个支路，其电流分别记为 $i\_1$、$i\_2$、$i\_3$，如图：

![alt text](/static/image/image-20.9f77808b7e.avif)
我们假设有一个奇妙的总电源，给红色的和蓝色的部分，提供了大小为 $V$ 的电势差。

我们规定红色部分的电势高于蓝色部分，即 $\varphi\_1>\varphi\_2$，则有 $V=\varphi\_1-\varphi\_2$。

据此，我们可以列出三个方程：

$$
\begin\{cases} V&=i\_1(r\_1+R\_1+R\_4)-E\_1\ V&=i\_2(r\_2+R\_2)-E\_2\ V&=i\_3(r\_3+R\_3)-E\_3 \end\{cases}
$$

代数即（其实这个就是基尔霍夫第二定律的意思）：

$$
\begin\{cases} V&=i\_1(2\Omega+1\Omega+3\Omega)-3V&=6\Omega\times i\_1-3V\ V&=i\_2(3\Omega+3\Omega)-6V&=6\Omega\times i\_2-6V\ V&=i\_3(1\Omega+2\Omega)-9V&=3\Omega\times i\_3-9V \end\{cases}
$$

发现原式与 $i\_1$、$i\_2$、$i\_3$ 关系密切，尝试找到他们之间的关系。

设电路的等效电阻为 $R\_0$，注意到 $V$ 只提供了 $i\_1+i\_2+i\_3$ 的电流，则有：

$$
i\_1+i\_2+i\_3=V/R\_0
$$

回到原电路，我们发现并没有这个奇妙的电源，也就是 $V=0$，

因此有（其实这个也是基尔霍夫第一定律的内容）：

$$
i\_1+i\_2+i\_3=0V/R\_0=0V
$$

这意味着 $i\_1$、$i\_2$、$i\_3$ 中一定存在负数。综合上述四式，解得：

$$
\begin\{cases} V&=-27/4\&V\ i\_1&=-5/8\&A\ i\_2&=-1/8\&A\ i\_3&=3/4\&A \end\{cases}
$$

则电流表示数为 $i\_1$ 的绝对值，即电流表示数为 $\dfrac\{5}\{8}A$。

::: \{.footnote}

***

1. ::: \{#fn:note100}
   [https://zh.wikipedia.org/wiki/欧姆定律#常見錯誤](https://zh.wikipedia.org/wiki/欧姆定律#常見錯誤)。 [↩](#fnref:note100 "Jump back to footnote 1 in the text")\{.footnote-backref}
   :::
   :::
