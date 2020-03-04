#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 9:48
# @Author  : WIX
# @File    : 快速排序.py


def quick_sort(array):
    if isinstance(array, list) is False:
        return False
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)



a = [4, 3, 1, 2]
print(quick_sort(a))
