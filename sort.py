"""
提目：排序算法汇总
"""
import unittest


def bubble_sort(arr: list):
    length = len(arr)
    res = arr[:]
    if length <= 1:
        return res
    for i in range(length):
        is_swap = False
        for j in range(length - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
                is_swap = True
        if not is_swap:
            break
    return res


def selection_sort(arr: list):
    length = len(arr)
    res = arr[:]
    if length <= 1:
        return res
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if res[j] < res[min_index]:
                min_index = j
        if min_index != i:
            res[i], res[min_index] = res[min_index], res[i]
    return res


def quick_sort1(arr: list):
    length = len(arr)
    res = arr[:]
    if length <= 1:
        return res
    pivot = res[0]
    left = [i for i in res if i < pivot]
    middle = [i for i in res if i == pivot]
    right = [i for i in res if i > pivot]
    return quick_sort1(left) + middle + quick_sort1(right)


class Test(unittest.TestCase):
    def test(self):
        arr = [
            [5, 3, 6, 4, 1, 2],
            [1],
            [3, 4, 1, 6, 4, 5],
            [5, 4, 3, 2, 1],
            [1, 2, 3, 4, 5],
            [1, 1, 1]
        ]
        for a in arr:
            for fun in [bubble_sort, selection_sort, quick_sort1]:
                self.assertEqual(sorted(a), fun(a))
            # self.assertEqual(sorted(a), quick_sort1(a))
