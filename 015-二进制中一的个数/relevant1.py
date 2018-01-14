#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 20:37
# @Author  : WIX
# @File    : relevant1.py

"""
判断一个数是不是2得整数次幂
"""
"""
如果一个整数是2的整数次方，则他二进制中有且只有一个1
"""


def powerOf2(n):
    if n & (n - 1) == 0:
        return True
    else:
        return False
