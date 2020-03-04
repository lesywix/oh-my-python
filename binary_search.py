"""
提目：二分查找
"""
import unittest


def binary_search(arr: list, x: int):
    if len(arr) == 1 and arr[0] != x:
        return False
    mid_index = len(arr) // 2
    mid = arr[mid_index]
    if x == mid:
        return True
    elif x < mid:
        return binary_search(arr[:mid_index], x)
    elif x > mid:
        return binary_search(arr[mid_index + 1:], x)
    else:
        return False


class Test(unittest.TestCase):
    def test(self):
        arr = [1, 3, 4, 6, 7, 9, 13]
        self.assertEqual(True, binary_search(arr, 7))
        self.assertEqual(True, binary_search(arr, 1))
        self.assertEqual(True, binary_search(arr, 13))
        self.assertEqual(True, binary_search(arr, 6))
        self.assertEqual(False, binary_search(arr, 2))
        self.assertEqual(False, binary_search(arr, 0))
        self.assertEqual(False, binary_search(arr, 15))
        arr = [2, 2, 2, 2]
        self.assertEqual(False, binary_search(arr, 3))
        self.assertEqual(False, binary_search(arr, 1))
        self.assertEqual(True, binary_search(arr, 2))
