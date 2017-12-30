#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/30 16:12
# @Author  : WIX
# @File    : Fibonacci.py

"""
题目：写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项。
"""

import unittest


class Solution(object):
    # 最常见的写法，但是效率极低，存在大量的重复计算
    def Fibonacci_useless(self, n):
        if isinstance(n, int) is False or n < 0:
            return
        elif n == 0 or n == 1:
            return n
        else:
            return self.Fibonacci_useless(n - 1) + self.Fibonacci_useless(n - 2)

    # 后一个数由前两个数相加
    def Fibonacci(self, n):
        if isinstance(n, int) is False or n < 0:
            return
        fibonacci_one = 0
        fibonacci_two = 1
        fibonacci = 0
        if n <= 1:
            return fibonacci_one if n == 0 else fibonacci_two
        for i in range(n - 1):
            fibonacci = fibonacci_one + fibonacci_two
            fibonacci_one = fibonacci_two
            fibonacci_two = fibonacci
        return fibonacci

    # 更优雅的方式，利用列表
    def Fibonacci2(self, n):
        if isinstance(n, int) is False or n < 0:
            return
        fibonacci = [0, 1]
        if n <= 1:
            return fibonacci[n]
        for i in range(2, n + 1):
            fibonacci[i % 2] = fibonacci[0] + fibonacci[1]
        return fibonacci[n % 2]
        # 利用栈的思想（与上面的方法类似）：
        # if isinstance(n, int) is False or n < 0:
        #     return
        # fibonacci = [0, 1]
        # if n <= 1:
        #     return fibonacci[n]
        # for i in range(2, n + 1):
        #     num = fibonacci[0] + fibonacci[1]
        #     fibonacci.pop(0)
        #     fibonacci.append(num)
        # return fibonacci[-1]


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    def test_1(self):
        n1 = 0
        n2 = 1
        n3 = 2
        self.assertEquals((self.s.Fibonacci(n1)), (self.s.Fibonacci2(n1)), (self.s.Fibonacci_useless(n1)))
        self.assertEquals((self.s.Fibonacci(n2)), (self.s.Fibonacci2(n2)), (self.s.Fibonacci_useless(n2)))
        self.assertEquals((self.s.Fibonacci(n3)), (self.s.Fibonacci2(n3)),
                          (self.s.Fibonacci_useless(n3)))

    def test_2(self):
        n1 = 3
        n2 = 5
        n3 = 10
        self.assertEquals(self.s.Fibonacci(n1), self.s.Fibonacci2(n1), self.s.Fibonacci_useless(n1))
        self.assertEquals(self.s.Fibonacci(n2), self.s.Fibonacci2(n2), self.s.Fibonacci_useless(n2))
        self.assertEquals(self.s.Fibonacci(n3), self.s.Fibonacci2(n3),
                          self.s.Fibonacci_useless(n3))

    def test_3(self):
        n1 = 40
        n2 = 50
        n3 = 100
        self.assertEquals((self.s.Fibonacci(n1)),
                          (self.s.Fibonacci2(n1)))
        self.assertEquals((self.s.Fibonacci(n2)), (self.s.Fibonacci2(n2)),
                          )
        self.assertEquals((self.s.Fibonacci(n3)),

                          (self.s.Fibonacci2(n3)))


if __name__ == '__main__':
    unittest.main()
