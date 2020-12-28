#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/17 17:15
# @Author  : WIX
# @File    : singleton4.py

"""
共享属性；
所谓单例就是所有引用（实例、对象）拥有相同的的状态（属性）和行为（方法）
同一个类的所有实例天然拥有相同的行为（方法）
只需要保证一个类的所有实例具有相同的状态（属性）即可
所有实例共享属性的最简单方法就是__dict__属性指向（引用）同一个字典（dict）
"""


class Singleton4(object):
    _instance = {}

    def __new__(cls, *args, **kwargs):
        oj = super(Singleton4, cls).__new__(cls, *args, **kwargs)
        oj.__dict__ = cls._instance
        return oj


class MyClass(Singleton4):
    a = 1


a = MyClass()
b = MyClass()
print(id(a), id(b))
print(id(a.__dict__), id(b.__dict__))

