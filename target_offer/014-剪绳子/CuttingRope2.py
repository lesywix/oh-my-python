#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 16:46
# @Author  : WIX
# @File    : CuttingRope2.py

"""
用贪婪算法实现剪绳子问题
"""
"""
用贪婪算法时，每一步都可以做出一个贪婪选择，基于这个选择，我们能确定的到最优解？同时需要用数学证明这个贪婪选择是对的。
当n>=5时，可证2(n-2)>n且3(n-3)>n，就是说当绳子长度大于等于5时可以切成2或3。另外当n>=5时，3(n-3)>=2(n-2)，因此要竟可能剪出长度为3的段。
当长度为4时2*2>1*3，所以要切成2*2的段
"""
import unittest


def maxProductAfterCutting(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    # 尽可能分成长度为3的段
    timeOf3 = n // 3
    # 当最后长度为4的时候不能再分成3+1，而应该是分成2+2
    if (n - timeOf3 * 3) == 1:
        timeOf3 -= 1
    timeOf2 = (n - timeOf3 * 3) // 2
    return (3 ** timeOf3) * (2 ** timeOf2)


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