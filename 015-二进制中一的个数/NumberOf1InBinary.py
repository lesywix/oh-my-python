#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 12:38
# @Author  : WIX
# @File    : NumberOf1InBinary.py

"""
题目：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。
"""
"""
总结：
把一个整数减1后在和原来的整数做位的与运算，得到的结果相当于把整数的二进制表示中最右边的1变成0
"""

import unittest


class Solution(object):
    def number_of_1(self, n):
        if n < 0:
            s = bin(n & 0xffffffff)
        else:
            s = bin(n)
        return s.count('1')


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    def test_1(self):
        n = 1
        n2 = 0x7fffffff
        n3 = 10
        self.assertEqual(self.s.number_of_1(n), 1)
        self.assertEqual(self.s.number_of_1(n2), 31)
        self.assertEqual(self.s.number_of_1(n3), 2)

    def test_2(self):
        n = 0xFFFFFFFF
        n2 = 0x80000000
        self.assertEqual(self.s.number_of_1(n), 32)
        self.assertEqual(self.s.number_of_1(n2), 1)


if __name__ == '__main__':
    unittest.main()
