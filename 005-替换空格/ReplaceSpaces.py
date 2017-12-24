#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 9:51
# @Author  : WIX
# @File    : ReplaceSpaces.py

"""
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""

"""
常见错误：尝试修改string的值（导致“ TypeError: ‘str’ object does not support item assignment”）
**string是一种不可变的数据类型**，该错误发生在如下代码中：
spam = 'I have a pet cat.'
spam[13] = 'r'
print(spam)
而你实际想要这样做：
spam = 'I have a pet cat.'
spam = spam[:13] + 'r' + spam[14:]
print(spam)
"""

import unittest


class Solution(object):
    # 使用内置函数，新建了一个新的字符串
    def replaceSpace1(self, s):
        if not s or isinstance(s, str) is False or len(s) <= 0:
            return ''
        s = s.replace(' ', '%20')
        return s

    # 书上的方法，从后往前替换(由于python里string是不可变对象，因此不能在原字符串上操作，只能新建一个新字符串)
    def replaceSpace2(self, s):
        if not s or isinstance(s, str) is False or len(s) <= 0:
            return ''
        numOfBlank = 0
        for i in s:
            if i == ' ':
                numOfBlank += 1
        newStrLen = len(s) + 2 * numOfBlank
        # 新建长度为newStrLen，内容为None的列表
        newStr = newStrLen * [None]
        indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
        while 0 <= indexOfOriginal <= indexOfNew:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew - 2: indexOfNew + 1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return ''.join(newStr)


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = Solution()

    def test_1(self):
        s = 'hello world'
        self.assertEqual(self.a.replaceSpace1(s), 'hello%20world')
        self.assertEqual(self.a.replaceSpace2(s), 'hello%20world')

    def test_2(self):
        s = ' helloworld'
        self.assertEqual(self.a.replaceSpace1(s), '%20helloworld')
        self.assertEqual(self.a.replaceSpace2(s), '%20helloworld')

    def test_3(self):
        s = 'hello  world'
        self.assertEqual(self.a.replaceSpace1(s), 'hello%20%20world')
        self.assertEqual(self.a.replaceSpace2(s), 'hello%20%20world')

    def test_4(self):
        s = ''
        self.assertEqual(self.a.replaceSpace1(s), '')
        self.assertEqual(self.a.replaceSpace2(s), '')

    def test_5(self):
        s = ' '
        self.assertEqual(self.a.replaceSpace1(s), '%20')
        self.assertEqual(self.a.replaceSpace2(s), '%20')

    def test_6(self):
        s = 'helloworld'
        self.assertEqual(self.a.replaceSpace1(s), 'helloworld')
        self.assertEqual(self.a.replaceSpace2(s), 'helloworld')


if __name__ == '__main__':
    unittest.main()
