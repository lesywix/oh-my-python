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
    # 需要复制切割原列表
    length = len(arr)
    res = arr[:]
    if length <= 1:
        return res
    pivot = res[0]
    left = [i for i in res if i < pivot]
    middle = [i for i in res if i == pivot]
    right = [i for i in res if i > pivot]
    return quick_sort1(left) + middle + quick_sort1(right)


def partition(array, start, end):
    pivot_idx = start
    for i in range(start + 1, end + 1):
        # 一次循环完成定位 pivot 和交换元素
        # print(f'#1: array_i[{i}]: {array[i]}, '
        #       f'array_start[{start}]: {array[start]}, arr: {array}, '
        #       f'pivot: {pivot_idx}, start: {start}, end: {end}')
        if array[i] <= array[start]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[start] = array[start], array[pivot_idx]
    return pivot_idx


def quick_sort2_recurse(arr, start, end):
    if start < end:
        pivot_id = partition(arr, start, end)
        quick_sort2_recurse(arr, start, pivot_id - 1)
        quick_sort2_recurse(arr, pivot_id + 1, end)


def quick_sort2(arr: list, start=0, end=None):
    # 通过 index 在原列表的移动实现，不需要复制切割原列表
    length = len(arr)
    if end is None:
        end = length - 1
    r = arr[:]
    quick_sort2_recurse(r, start, end)
    return r


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
            for fun in [bubble_sort, selection_sort, quick_sort1, quick_sort2]:
                self.assertEqual(sorted(a), fun(a))
