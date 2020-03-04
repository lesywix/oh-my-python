#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/17 20:32
# @Author  : WIX
# @File    : duplicationInArray.py

"""
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
"""

"""
思路：
由于数组长度为n，并且要求数组内的数字都在0~n-1范围内，那么如果对数组排序的话，数组的下标可以唯一表示这个数字。
由这个为切入点，对数组进行循环，若下标与数字不对应，则将该数字移动到对应的下标，直到下标能对应。
若数组循环完还不能找到，则没有重复数字；若移到对应下标时与原本在该下标下的数相等，则有重复数字。
时间复杂度O(n)，空间复杂度O(1)
"""
import unittest


class Solution(object):
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        n = len(numbers)
        if numbers is None or n <= 0 or isinstance(numbers, list) is False:
            return False
        for i in range(n):
            if numbers[i] < 0 or numbers[i] > n - 1:
                return False
        # 循环列表
        for i in range(n):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    index = numbers[i]
                    numbers[i], numbers[index] = numbers[index], numbers[i]
        return False


class TestFunc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.duplication = [0]

    def test_duplicate(self):
        test = [2, 3, 1, 0, 2, 5, 3]
        self.assertEqual(self.s.duplicate(test, self.duplication), True)

    def test_unique(self):
        test = [1, 2, 3, 4, 5, 0]
        self.assertEqual(self.s.duplicate(test, self.duplication), False)

    def test_bad(self):
        test1 = []
        test2 = [5, 6]
        test3 = 'rtgr'
        self.assertEqual(self.s.duplicate(test1, self.duplication), False)
        self.assertEqual(self.s.duplicate(test2, self.duplication), False)
        self.assertEqual(self.s.duplicate(test3, self.duplication), False)


if __name__ == '__main__':
    unittest.main()