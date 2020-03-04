#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 20:40
# @Author  : WIX
# @File    : relevant2.py

"""
判断两个数的二进制表示有多少位不一样
"""
"""
先求两个数的异或，再比较两个数的二进制异或就可以
"""


def andOr(m, n):
    diff = m ^ n
    count = 0
    while diff:
        count += 1
        diff = diff & (diff - 1)
    return count