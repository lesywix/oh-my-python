#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/30 22:00
# @Author  : WIX
# @File    : 变态青蛙跳.py

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
f(0) = 1
f(1) = 1
f(2) = f(2-1) + f(2-2)
f(3) = f(3-1) + f(3-2) + f(3-3)
...
f(n) = f(n-1) + f(n-2) + ... + f(n-(n-1)) + f(n-n)
简单的解释一下：例如f(3-1)表示3阶跳了1阶后，剩下的跳阶方法数，f(3-2)表示3阶跳了两阶后剩下的跳阶方法数，以此类推，直到一次跳n阶后，剩下的跳阶方法数。
现在问题明了了很多，但是还不够，我们可以继续对其进行分解：
因为 ： f(n) = f(n-1) + f(n-2) + ... + f(n-(n-1)) + f(n-n) = f(0) + f(1) + f(2) + ... + f(n-2) + f(n-1)
所以 ： f(n-1) = f(0) + f(1) + ... + f((n-1)-1) = f(0) + f(1) + f(2) + ... + f(n-2)
则： f(n) = f(n-1) + f(n-1) = 2*f(n-1)
"""


class Solution(object):
    def biantai(self, n):
        result = 1
        if n >= 2:
            for i in range(n - 1):
                result = 2 * result
        return result


s = Solution()
print(s.biantai(5))
