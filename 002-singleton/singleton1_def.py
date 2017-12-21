#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/16 16:55
# @Author  : WIX
# @File    : singleton1.py

"""
单例模式主要目的是确保某一个类只有一个实例存在
三个要点: 某个类只有一个实例; 必须自行创建这个实例; 必须自行向整个系统提供这个实例
"""

"""
singleton1:使用模块
Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。
"""


class Singleton1(object):
    def foo(self):
        print('singleton created')

my_singleton = Singleton1()

# 将上面代码保存为singleton1_def.py

