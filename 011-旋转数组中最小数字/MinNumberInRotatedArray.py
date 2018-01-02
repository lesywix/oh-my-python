#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 9:48
# @Author  : WIX
# @File    : MinNumberInRotatedArray.py

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""

"""
思路：二分查找的变种，需要用两个下标指针。
两点需要注意：
1. 若没有翻转部分，即数组已经是有序的，第一个即为最小
2. 若左指针的值等于右指针的值等于中间的值，则不能用二分查找的方法，只能通过遍历找到最小值
"""

import unittest


class Solution(object):
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        lp = 0
        rp = len(rotateArray) - 1
        minVal = rotateArray[0]
        # mid = len(rotateArray) // 2
        if rotateArray[lp] < rotateArray[rp]:
            return rotateArray[lp]
        else:
            while (rp - lp) > 1:
                mid = (lp + rp) // 2
                if rotateArray[lp] < rotateArray[mid]:
                    lp = mid
                elif rotateArray[rp] > rotateArray[mid]:
                    rp = mid
                elif rotateArray[rp] == rotateArray[lp] == rotateArray[mid]:
                    for i in range(len(rotateArray)):
                        if rotateArray[i] < minVal:
                            minVal = rotateArray[i]
                    return minVal
        return rotateArray[rp]


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    def test_1(self):
        l = [3, 4, 5, 1, 2]
        self.assertEqual(self.s.minNumberInRotateArray(l), 1)

    def test_2(self):
        l = [1, 2, 3, 4, 5]
        self.assertEqual(self.s.minNumberInRotateArray(l), 1)

    def test_3(self):
        l = [1, 0, 1, 1, 1]
        self.assertEqual(self.s.minNumberInRotateArray(l), 0)

    def test_4(self):
        l = [3, 4, 5, 1, 1, 2]
        self.assertEqual(self.s.minNumberInRotateArray(l), 1)

    def test_5(self):
        l = [3, 4, 5, 1, 2, 2]
        self.assertEqual(self.s.minNumberInRotateArray(l), 1)


if __name__ == '__main__':
    unittest.main()
