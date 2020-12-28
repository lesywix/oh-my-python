#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/17 15:36
# @Author  : WIX
# @File    : singleton3.py

"""
使用装饰器：
可以使用装饰器来装饰某个类，使其只能生成一个实例
单例类本身根本不知道自己是单例的，因为他自己的代码并不是单例的
"""

from functools import wraps


def singleton3(cls, *args, **kwargs):
    instances = {}

    @wraps(cls)
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


@singleton3
class MyClass(object):
    a = 1


a = MyClass()
b = MyClass()
print(id(a), id(b))

