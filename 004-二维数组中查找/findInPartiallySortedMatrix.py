#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 20:54
# @Author  : WIX
# @File    : findInPartiallySortedMatrix.py

"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

"""
思路：
1. 最简单的可以采用暴力解法，遍历整个二维数组判断
2. 查找方式从右上角开始查找，如果当前元素大于target, 左移一位继续查找（右上角为该行最大），如果当前元素小于target, 下移一位继续查找（右上角为该列最小）
"""

import unittest


class Solution(object):
    def find(self, target, array):
        if not array or isinstance(array, list) is False or isinstance(target, int) is False:
            return False
        x = 0
        y = len(array[0]) - 1

        while x < len(array) and y >= 0:
            if array[x][y] == target:
                return True
            elif array[x][y] > target:
                y -= 1
            elif array[x][y] < target:
                x += 1
        return False


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()
        cls.test = [[1, 2, 8, 9],
                    [2, 4, 9, 12],
                    [4, 7, 10, 13],
                    [6, 8, 11, 15]]

    # 测试数字在数组中
    def test_1(self):
        target = 7
        self.assertEqual(self.s.find(target, self.test), True)

    # 测试数据不在数组中
    def test_2(self):
        target1 = 5
        target2 = 20
        target3 = -1
        self.assertEquals((self.s.find(target1, self.test), False), (self.s.find(target2, self.test), False),
                          (self.s.find(target3, self.test), False))

    # 测试数据是数组中最小的数
    def test_3(self):
        target = 1
        self.assertEqual(self.s.find(target, self.test), True)

    # 测试数据是数组中最大的数
    def test_4(self):
        target = 15
        self.assertEqual(self.s.find(target, self.test), True)

    # 无效数据
    def test_5(self):
        target1 = 'a'
        target2 = 7
        array1 = []
        array2 = ''
        self.assertEquals((self.s.find(target1, array1), False), (self.s.find(target1, array2), False),
                          (self.s.find(target2, array1), False))
        self.assertEqual(self.s.find(target2, array2), False)


if __name__ == '__main__':
    unittest.main()
