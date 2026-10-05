# 青岛二中 2022 年自主招生试题（物理）探究六（4）题解

本文详细解析青岛二中2022年自主招生物理电路题，给出基尔霍夫定律、叠加定理、源变换和简易欧姆四种解法，完整推导出电流表示数为5/8A，逻辑清晰适合学习参考。

## 题目描述

有电路如图乙所示（图中电流表为理想电流表）：

电路参数为：R_1=1\\Omega，R_2=3\\Omega，R_3=2\\Omega，R_4=3\\Omega，E_1=3V，r_1=2\\Omega，E_2=6V，r_2=3\\Omega，E_3=9V，r_3=1\\Omega。

电路正常工作时，电流表的示数是多少？

## Solution 1：基尔霍夫电路定律

如图，存在两条回路 s_1、s_2，假设电流流向为从 E_2、E_3 正极出发，干路、支路电流分别为 i_1，i_2、i_3：

对节点 K 应用基尔霍夫第一定律，得 i_1-i_2-i_3=0。

对回路 s_1、s_2 分别应用基尔霍夫第二定律，最终可列出方程组：

\\begin{cases} i_1&=i_2+i_3\\ E_2&=i_2r_2+i_2R_2+i_1R_1+i_1R_4+i_1r_1+E_1\\ E_3&=i_3r_3+i_3R_3+i_1R_1+i_1R_4+i_1r_1+E_1 \\end{cases}

代数，得：

\\begin{cases} i_1&=i_2+i_3\\ 6V&=3\\Omega\\cdot i_2+3\\Omega\\cdot i_2+1\\Omega\\cdot i_1+3\\Omega\\cdot i_1+2\\Omega\\cdot i_1+3V\\ 9V&=1\\Omega\\cdot i_3+2\\Omega\\cdot i_3+1\\Omega\\cdot i_1+3\\Omega\\cdot i_1+2\\Omega\\cdot i_1+3V \\end{cases}

化简得：

\\begin{cases} i_1&=i_2+i_3\\ 3V&=6\\Omega\\cdot i_2+6\\Omega\\cdot i_1\\ 6V&=3\\Omega\\cdot i_3+6\\Omega\\cdot i_1 \\end{cases}

解得：

\\begin{cases} i_1&=5/8&A\\ i_2&=-1/8&A\\ i_3&=3/4&A \\end{cases}

分析可知，我们假设的 i_2 电流流向是错误的，而电流表示数为 \\dfrac{5}{8}A。

## Solution 2：电路的叠加定理

忽略电流表，可以发现图中仅存在电阻和电压源，因此该电路是线性电路，存在电路的叠加原理。

分别考虑 E_1，E_2，E_3 的影响，设 I_1、I_2、I_3 其电流表的示数，以电流从上到下为正值，从下到上为负值：

极易得：

\\begin{array}{l} I_1&=-\\dfrac{E_1}{r_1+R_1+R_4+\\dfrac{(r_2+R_2)(r_3+R_3)}{r_2+R_2+r_3+R_3}}\\[2em] &=-\\dfrac{3V}{2\\Omega+1\\Omega+3\\Omega+\\dfrac{(3\\Omega+3\\Omega)(1\\Omega+2\\Omega)}{3\\Omega+3\\Omega+1\\Omega+2\\Omega}}\\[2em] &=-\\dfrac{3}{8}A \\end{array}

\\begin{array}{l} I_2&=\\dfrac{E_2}{r_2+R_2+\\dfrac{(r_3+R_3)(r_1+R_1+R_4)}{r_3+R_3+r_1+R_1+R_4}}\\times\\dfrac{r_3+R_3}{r_3+R_3+r_1+R_1+R_4}\\[2em] &=\\dfrac{6V}{3\\Omega+3\\Omega+\\dfrac{(1\\Omega+2\\Omega)(2\\Omega+1\\Omega+3\\Omega)}{1\\Omega+2\\Omega+2\\Omega+1\\Omega+3\\Omega}}\\times\\dfrac{1\\Omega+2\\Omega}{1\\Omega+2\\Omega+2\\Omega+1\\Omega+3\\Omega}\\[2em] &=\\dfrac{1}{4}A \\end{array}

\\begin{array}{l} I_3&=\\dfrac{E_3}{r_3+R_3+\\dfrac{(r_2+R_2)(r_1+R_1+R_4)}{r_2+R_2+r_1+R_1+R_4}}\\times\\dfrac{r_2+R_2}{r_2+R_2+r_1+R_1+R_4}\\[2em] &=\\dfrac{9V}{1\\Omega+2\\Omega+\\dfrac{(3\\Omega+3\\Omega)(2\\Omega+1\\Omega+3\\Omega)}{3\\Omega+3\\Omega+2\\Omega+1\\Omega+3\\Omega}}\\times\\dfrac{3\\Omega+3\\Omega}{3\\Omega+3\\Omega+2\\Omega+1\\Omega+3\\Omega}\\[2em] &=\\dfrac{3}{4}A \\end{array}

根据叠加定理，得出电流表示数 I=I_1+I_2+I_3=-\\dfrac{3}{8}+\\dfrac{1}{4}+\\dfrac{3}{4}=\\dfrac{5}{8}A。

## Solution 3：电流源与电压源

这也是原题想让我们应用的方法，这里先对题目的铺垫加以简单总结。

我们发现，一个内阻为 r 的电压源 E，等效如图丙。

其串联一个总电阻为 R 的用电器（或等效用电器）后，干路电流为：

I=\\dfrac{E}{r+R}

我们发现 E/r 为电源的特性，于是想办法凑出来这个形式：

I=\\dfrac{E}{r}\\times\\dfrac{r}{r+R}

注意到后面的式子就是并联分流公式，我们转化电路形如图丁。

于是，我们就把一个内阻为 r 的电压源 E 串联一个总电阻为 R 的用电器，等效转化为了一个电流源 E/r 并联上原电压源内阻，以及用电器 R。

回到问题，（如图）我们可以把原电压源 E_2、E_3 及其内阻、支路电阻等效转化为一个电压源：

- 把电压源 E_2 同其内阻 r_2 及并联的电阻 R_2 抽象为一个电压源 E'\_2，内阻为 (r_2+R_2)，也就等效为一个电流源 E_2/(r_2+R_2)，并联电阻 (r_2+R_2)；具体的，电阻 r_2'=r_2+R_2=6\\Omega，电流 I_2'=E_2/r_2'=6V/6\\Omega=1A。
- 把电压源 E_3 同其内阻 r_3 及并联的电阻 R_3 抽象为一个电压源 E'\_3，内阻为 (r_3+R_3)，也就等效为一个电流源 E_3/(r_3+R_3)，并联电阻 (r_3+R_3)；具体的，电阻 r_3'=r_3+R_3=3\\Omega，电流 I_3'=E_3/r_3'=9V/3\\Omega=3A。

观察到，这两个电流源（电流流向一致，电流大小相加）就可以合并为一个电流源。

具体的，电阻 r'=(3\\times6)/9=2\\Omega，电流 I'=1A+3A=4A；

这个电流源也就等效于一个电压源，电压为 E'=2\\Omega\\times4A=8V，R'=2\\Omega。

其电流方向与 E_1 相反，电压相减 V=E'-E_1=8V-3V=5V，

其总电阻 R=R_1+R_4+r_1+r'=1\\Omega+3\\Omega+2\\Omega+2\\Omega=8\\Omega。

于是，电流表示数即为 I=V/R=5V/8\\Omega=\\dfrac{5}{8}A。

## Solution 4：简单欧姆定律（手搓基尔霍夫）

我们把原图抽象为三个支路，其电流分别记为 i_1、i_2、i_3，如图：

我们假设有一个奇妙的总电源，给红色的和蓝色的部分，提供了大小为 V 的电势差。

我们规定红色部分的电势高于蓝色部分，即 \\varphi_1>\\varphi_2，则有 V=\\varphi_1-\\varphi_2。

据此，我们可以列出三个方程：

\\begin{cases} V&=i_1(r_1+R_1+R_4)-E_1\\ V&=i_2(r_2+R_2)-E_2\\ V&=i_3(r_3+R_3)-E_3 \\end{cases}

代数即（其实这个就是基尔霍夫第二定律的意思）：

\\begin{cases} V&=i_1(2\\Omega+1\\Omega+3\\Omega)-3V&=6\\Omega\\times i_1-3V\\ V&=i_2(3\\Omega+3\\Omega)-6V&=6\\Omega\\times i_2-6V\\ V&=i_3(1\\Omega+2\\Omega)-9V&=3\\Omega\\times i_3-9V \\end{cases}

发现原式与 i_1、i_2、i_3 关系密切，尝试找到他们之间的关系。

设电路的等效电阻为 R_0，注意到 V 只提供了 i_1+i_2+i_3 的电流，则有：

i_1+i_2+i_3=V/R_0

回到原电路，我们发现并没有这个奇妙的电源，也就是 V=0，

因此有（其实这个也是基尔霍夫第一定律的内容）：

i_1+i_2+i_3=0V/R_0=0V

这意味着 i_1、i_2、i_3 中一定存在负数。综合上述四式，解得：

\\begin{cases} V&=-27/4&V\\ i_1&=-5/8&A\\ i_2&=-1/8&A\\ i_3&=3/4&A \\end{cases}

则电流表示数为 i_1 的绝对值，即电流表示数为 \\dfrac{5}{8}A。

2026-10-052026-10-05

[RainPPR](https://github.com/RainPPR),  [Bot](mailto:bot@noreply.github.com)
