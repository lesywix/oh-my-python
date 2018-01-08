#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 22:54
# @Author  : WIX
# @File    : CuttingRope.py

"""
题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m≥1）。每段的绳子的长度记为
k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘积是多少？例如当绳子的长度是8时，我们把它
剪成长度分别为2、3、3的三段，此时得到最大的乘积18。
"""
"""
总结：
动态规划四个特点：
1. 求一个问题的最优解
2. 整个问题的最优解是依赖各个子问题的最优解
3. 把大问题分解成若干个小问题，这些小问题之间还有相互重叠的更小的子问题
4. 从上往下分析问题，从下往上求解问题
从剪绳子问题出发，首先他要求解剪出每段绳子的最大乘积，即求最优解；
求一段绳子剪完最大乘积，每剪一刀，得出来的结果最优解依赖于剪出来的绳子的最优解，以此递推；
对剪出来的绳子（子问题）求解时，还能再分解；
从上往下分析：先定义函数f(n)为把长度为n的绳子剪成若干段成绩最大值，当剪一刀时，有n-1种选择(1,2,...n-1)因此f(n)=max{f(i)*f(n-i)}(0<i<n)
从下往上求解：上式是一个从上往下递归公式，会有大量重复子问题的计算，所以更好的方法是从下往上计算，先得到f(2),f(3)，再根据f(2),f(3)得到f(4)...
"""

import unittest


def maxProductAfterCutting(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    # 创建一个长度为n的空数组存储子问题最优解
    f = [None for _ in range(n + 1)]
    f[0], f[1], f[2], f[3] = 0, 1, 2, 3
    result = 0
    # 从下往上求解
    for i in range(4, n + 1):
        # 求f(j)*f(i-j)的最大值（最优解），避免重复只需要循环一半即可
        for j in range(1, (i // 2) + 1):
            temp = f[j] * f[i - j]
            if temp > result:
                result = temp

        f[i] = result
    return result


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(maxProductAfterCutting(1), 0)
        self.assertEqual(maxProductAfterCutting(2), 1)
        self.assertEqual(maxProductAfterCutting(3), 2)

    def test_2(self):
        self.assertEqual(maxProductAfterCutting(4), 4)
        self.assertEqual(maxProductAfterCutting(5), 6)
        self.assertEqual(maxProductAfterCutting(6), 9)
        self.assertEqual(maxProductAfterCutting(7), 12)
        self.assertEqual(maxProductAfterCutting(8), 18)


if __name__ == '__main__':
    unittest.main()
