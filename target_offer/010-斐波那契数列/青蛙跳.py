#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/30 21:02
# @Author  : WIX
# @File    : 青蛙跳.py

"""
青蛙跳台阶, 每次可以跳1级或2级,求青蛙跳上一个n级的台阶一共有多少种跳法？
当n > 2时，第一次跳就有两种选择：
1. 第一次跳1级，后面的跳法相当于剩下n-1级的跳法，即f(n-1)
2. 第一次跳2级，后面的跳法相当于剩下n-2级的跳法，即f(n-2)
即f(n) = f(n-1) + f(n-2)
"""


class Solution(object):
    def jumpfrog(self, n):
        if isinstance(n, int) is False or n < 1:
            return
        result = [1, 2]
        if n <= 2:
            return result[n - 1]
        for i in range(n - 2):
            result[i % 2] = result[0] + result[1]
        return result[n % 2 - 1]


s = Solution()
print(s.jumpfrog(4))
