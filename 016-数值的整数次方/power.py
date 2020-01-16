import unittest
"""
提目：实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。
总结：需要考虑 base，exponent 为 0，正数，负数的情况
使用如下公式优化循环次数：
当n为偶数, a^n = a^(n/2) * a^(n/2)
当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a
利用位运算代替乘除提高效率：
利用右移一位运算代替除以2
利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
"""


def power_value(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    r = power_value(base, exponent >> 1)
    r *= r
    if exponent & 1 == 1:
        r *= base
    return r


def power(base, exponent):
    if exponent == 0:
        return 1
    if base == 0:
        return 0
    r = power_value(base, abs(exponent))
    if exponent < 0:
        r = 1 / r
    return r


class Test(unittest.TestCase):
    def test(self):
        r = power(2, 3)
        self.assertEqual(pow(2, 3), r)
        r = power(2, -3)
        self.assertEqual(pow(2, -3), r)
        r = power(-2, 3)
        self.assertEqual(pow(-2, 3), r)
        r = power(2, 0)
        self.assertEqual(pow(2, 0), r)
        r = power(0, 0)
        self.assertEqual(pow(0, 0), r)
        r = power(0, 4)
        self.assertEqual(pow(0, 4), r)
        r = power(0, -4)
        self.assertEqual(0, r)
