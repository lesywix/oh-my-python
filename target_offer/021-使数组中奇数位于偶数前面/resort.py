"""
提目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
总结：合理运用 Python 迭代器特性解决问题
"""
import unittest

#fix the bug in your code

class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def reorder_odd_even(self, nums):
        if not isinstance(nums, list) or len(nums) == 0:
            return
        begin = 0
        end = len(nums) - 1
        while begin < end:
            while begin < end and (nums[begin] & 0x1) ==1:
                begin += 1
            while begin < end and (nums[end] & 0x1) == 0:
                end -= 1
            if begin < end:
                nums[begin], nums[end] = nums[end], nums[begin]
                begin += 1
        return nums

s = Solution()
print(s.reorder_odd_even([1,2,3,4,5]))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 3, 2, 4],Solution().reorder_odd_even([1,2,3,4]))

Test().test()
