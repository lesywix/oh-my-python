#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/19 16:34
# @Author  : WIX
# @File    : duplicationInArrary2.py

"""
在一个长度为n+1的数组里的所有数字都在1~n的范围内，所以数组中至少有一个数字是重复的。请找出数组中任意一个重复的数字，但是不能修改输入的数组。例如，如果输入长度为8的数组{2,3,5,4,3,2,6,7}，那么对应的输出是重复的数字2或者3
"""

"""
思路：
1. 初始化一个字典，循环列表，将列表里的数字存到字典中，键和值都为对应列表的值。若发现键存在，则有重复数字，反之则无。时间复杂度O(n)，空间复杂度O(n)
2. 用二分法的思想，将1~n-1分为两部分，若任意一部分的数字总和大于在这一部分的数字在列表汇总出现的次数，则存在重复数字。
例如，数组{2,3,5,4,3,2,6,7}，1~n-1 := 1~7(分为1~4,5~7)，其中1~4在列表中出现了5次，大于4，则存在重复。时间复杂度O(nlogn)，空间复杂度O(1)
"""

import unittest


class Solution(object):
    # 方法1
    def duplicate(self, numbers):
        n = len(numbers)
        repeated_num = {}
        if numbers is None or n <= 0 or isinstance(numbers, list) is False:
            return False
        for i in range(n):
            if numbers[i] < 0 or numbers[i] > n - 1:
                return False
        for i in range(n):
            if repeated_num.get(numbers[i]) is not None:
                return numbers[i]

            else:
                repeated_num[numbers[i]] = numbers[i]
        return False

    # 方法2（循环法）
    def duplicate2(self, numbers):
        n = len(numbers)
        if numbers is None or n <= 0 or isinstance(numbers, list) is False:
            return False
        for i in range(n):
            if numbers[i] < 0 or numbers[i] > n - 1:
                return False
        start = 1
        end = n - 1
        while end >= start:
            mid = (start + end) // 2
            count = self.num_count(numbers, start, mid)
            # 终结条件
            if end == start:
                if count > 1:
                    return start
                else:
                    return False
            if count > (mid - start + 1):
                end = mid
            else:
                start = mid + 1  # 这里应为mid + 1,否则start永远比end小1，mid永远等于start，死循环
        return False

    def num_count(self, numbers, start, end):
        count = 0
        for i in range(len(numbers)):
            if start <= numbers[i] <= end:
                count += 1
        return count

    # 方法2（递归法,写法1）
    def duplicate3(self, numbers, start, end):
        n = len(numbers)
        if numbers is None or n <= 0 or isinstance(numbers, list) is False:
            return False
        for i in range(n):
            if numbers[i] < 0 or numbers[i] > n - 1:
                return False
        mid = (start + end) // 2
        count = 0

        for i in range(len(numbers)):
            if start <= numbers[i] <= mid:
                count += 1

        if start > end:
            return False
        elif start == end:
            if count > 1:
                return start
            else:
                return False

        if count > (mid - start + 1):
            return self.duplicate3(numbers, start, mid)
        else:
            return self.duplicate3(numbers, mid + 1, end)

    # 方法2（递归法，写法2）
    def duplicate4(self, numbers, start, end):
        n = len(numbers)
        if numbers is None or n <= 0 or isinstance(numbers, list) is False:
            return False
        for i in range(n):
            if numbers[i] < 0 or numbers[i] > n - 1:
                return False

        mid = (start + end) // 2
        count = 0
        for i in range(len(numbers)):
            if start <= numbers[i] <= end:
                count += 1
        if start > end:
            return False
        elif start == end:
            if count > 1:
                return start
            else:
                return False
        elif count > (end - start + 1):
            result1 = self.duplicate4(numbers, start, mid)
            result2 = self.duplicate4(numbers, mid + 1, end)
            if result1:
                return result1
            if result2:
                return result2
        else:
            return False


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    # 多个重复数字
    def test_1(self):
        test = [2, 3, 5, 4, 3, 2, 6, 7]
        duplication = [2, 3]
        self.assertIn(self.s.duplicate(test), duplication)
        self.assertIn(self.s.duplicate2(test), duplication)
        self.assertIn(self.s.duplicate3(test, 1, len(test) - 1), duplication)

    # 一个重复数字
    def test_2(self):
        test = [3, 2, 1, 4, 4, 5, 6, 7]
        duplication = [4]
        self.assertIn(self.s.duplicate(test), duplication)
        self.assertIn(self.s.duplicate2(test), duplication)
        self.assertIn(self.s.duplicate3(test, 1, len(test) - 1), duplication)

    # 重复数字是数组中最小的
    def test_3(self):
        test = [1, 2, 3, 4, 5, 6, 7, 1, 8]
        duplication = [1]
        self.assertIn(self.s.duplicate(test), duplication)
        self.assertIn(self.s.duplicate2(test), duplication)
        self.assertIn(self.s.duplicate3(test, 1, len(test) - 1), duplication)

    # 重复数字是数组中最大的
    def test_4(self):
        test = [1, 7, 3, 4, 5, 6, 8, 2, 8]
        duplication = [8]
        self.assertIn(self.s.duplicate(test), duplication)
        self.assertIn(self.s.duplicate2(test), duplication)
        self.assertIn(self.s.duplicate3(test, 1, len(test) - 1), duplication)

    # 数组中只有两个数字
    def test_5(self):
        test = [1, 1]
        duplication = [1]
        self.assertIn(self.s.duplicate(test), duplication)
        self.assertIn(self.s.duplicate2(test), duplication)
        self.assertIn(self.s.duplicate3(test, 1, len(test) - 1), duplication)

    # 一个数字重复三次
    def test_6(self):
        test = [1, 2, 2, 6, 4, 5, 2]
        duplication = [2]
        self.assertIn(self.s.duplicate(test), duplication)
        self.assertIn(self.s.duplicate2(test), duplication)
        self.assertIn(self.s.duplicate3(test, 1, len(test) - 1), duplication)

    # 没有重复的数字
    def test_7(self):
        test = [1, 2, 6, 4, 5, 3]
        self.assertEqual(self.s.duplicate(test), False)
        self.assertEqual(self.s.duplicate2(test), False)
        self.assertEqual(self.s.duplicate3(test, 1, len(test) - 1), False)

    # 无效输入
    def test_8(self):
        test1 = []
        test2 = [5, 6]
        test3 = 'rtgr'
        self.assertEqual(self.s.duplicate(test1), False)
        self.assertEqual(self.s.duplicate(test2), False)
        self.assertEqual(self.s.duplicate(test3), False)
        self.assertEqual(self.s.duplicate2(test1), False)
        self.assertEqual(self.s.duplicate2(test2), False)
        self.assertEqual(self.s.duplicate2(test3), False)
        self.assertEqual(self.s.duplicate3(test1, 1, len(test1) - 1), False)
        self.assertEqual(self.s.duplicate3(test2, 1, len(test2) - 1), False)
        self.assertEqual(self.s.duplicate3(test3, 1, len(test3) - 1), False)


if __name__ == '__main__':
    unittest.main()