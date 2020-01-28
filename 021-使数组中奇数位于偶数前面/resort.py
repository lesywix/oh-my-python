"""
提目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
总结：合理运用 Python 迭代器特性解决问题
"""
import unittest


def resort(s):
    return list(filter(is_odd, s)) + list(filter(is_even, s))


def is_even(n):
    return n & 1 == 0


def is_odd(n):
    return n & 1 == 1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 3, 2, 4], resort([1, 2, 3, 4]))
