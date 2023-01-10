'''
题目：
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
'''
import unittest

class Solution:
    """
    @param: nums: an array of integers
            func: the filtering function
    """
    def reorder_odd_even(self, nums, func):
        if not isinstance(nums, list):
            raise TypeError("Invalid input type")
        if len(nums) <= 0:
            return
        begin = 0
        end = len(nums) - 1
        while begin < end:
            while begin < end and not func(nums[begin]):
                begin += 1
            while begin < end and func(nums[end]):
                end -= 1
            if begin < end:
                nums[begin], nums[end] = nums[end], nums[begin]
                begin += 1
        return nums

def is_even(n):
    return n & 1 == 0

s = Solution()
#print(s.reorder_odd_even([2,1],is_even))
#print(s.reorder_odd_even((2,1),is_even))
#print(s.reorder_odd_even([],is_even))


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 3, 2, 4],Solution().reorder_odd_even([1,2,3,4],is_even))

#Test().test()
