#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/16 17:27
# @Author  : WIX
# @File    : singleton2.py

"""
使用__new__:
实现__new__方法,然后将类的一个实例绑定到类变量_instance上
如果cls._instance为None, 说明该类没有被实例化过, new一个该类的实例,并返回
如果cls._instance不是None, 直接返回_instance
"""


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    a = 1


class MyClass2(Singleton):
    b = 2


class MyClass4(MyClass):
    """如果继续继承，仍然会去调用原始父类 Singleton 的 __new__ 方法"""


if __name__ == '__main__':
    # test
    a = MyClass()
    b = MyClass()
    c = MyClass2()
    d = MyClass2()
    print(id(a), id(b), id(c), id(d))

    a.a = 3
    print(a.a, b.a)

    t = MyClass4()
    tt = MyClass4()
    print(id(t), id(tt))
