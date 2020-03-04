#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 9:54
# @Author  : WIX
# @File    : StringPathInMatrix.py


"""
题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中任意一格开始，
每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如在
下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用下划线标出）。但矩阵中不包含字符串“abfb”的路径，因为
字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
A B T G
C F C S
J D E H
"""
"""
总结：
如果题目由多个步骤组成，并且每个步骤都有多个选项，可以尝试用回溯法（可以形象地用树状图表示）
比如在二维数组找路径
注意点：
一条判断语句有多个判断项且有关联时要注意先后顺序！
二维矩阵和一维矩阵可以分开判断（一维可用if a in ''.join(b)判断）
"""

import unittest


class Solution(object):
    def __init__(self, matrix, path):
        self.matrix = matrix
        self.rows = len(self.matrix) if isinstance(self.matrix[0], list) else 1
        self.cols = len(self.matrix[0]) if isinstance(self.matrix[0], list) else len(self.matrix)
        self.path = path
        # 字符串指针，表示已经匹配到多少个字符
        self.pathIndex = 0
        # 创建一个与matrix大小相同，值为零的矩阵
        self.checkBox = [[0 for j in range(len(self.matrix[0]))] if isinstance(self.matrix[0], list) else 0 for i in
                         range(len(self.matrix))]

    def hasPath(self):
        if self.matrix is None or self.path is None or self.rows < 0 or self.cols < 0:
            return None
        # 判断一下是否为一维数组，是的话直接查找
        if self.rows == 1:
            return True if self.path in ''.join(self.matrix) else False
        # 否则循环整个数组，将拿到的值作为路径第一个字符判断，进入Core函数，如果函数最终返回真，说明以这个字符开始有路径能匹配所给字符串
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.hasPathCore(i, j):
                        return True
            return False

    def hasPathCore(self, row, col):
        # 如果字符串的指针大小等于所给的字符串长度，说明已经完整匹配，返回真
        if self.pathIndex == len(self.path):
            return True
        has_path = False
        # 判断行和列有没有越界，某条路径是否重复以及当前指针下的字符串与当前矩阵下某个值是否相等
        if row >= 0 and col >= 0 and row < self.rows and col < self.cols and self.path[self.pathIndex] == self.matrix[row][col] and self.checkBox[row][col] == 0:
            # 条件成立，指针加1，路径标记为1
            self.pathIndex += 1
            self.checkBox[row][col] = 1
            # 递归矩阵当前元素的上下左右的值，用or判断有没有一条是成立的
            has_path = self.hasPathCore(row - 1, col) or self.hasPathCore(row, col - 1) or self.hasPathCore(row + 1, col) or self.hasPathCore(row, col + 1)
            # 若没有，则需要回退
            if has_path is False:
                self.pathIndex -= 1
                self.checkBox[row][col] = 0
        return has_path


class Test(unittest.TestCase):
    def test_1(self):
        m = [['a', 'b', 't', 'g'], ['c', 'f', 'c', 's'], ['j', 'd', 'e', 'h']]
        p1 = 'bfce'
        p2 = 'abcd'
        s1 = Solution(m, p1)
        s2 = Solution(m, p2)
        self.assertEqual(s1.hasPath(), True)
        self.assertEqual(s2.hasPath(), False)

    def test_2(self):
        m = [['a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a']]
        p = 'aaaa'
        s = Solution(m, p)
        self.assertEqual(s.hasPath(), True)

    def test_3(self):
        m = ['a', 'a', 'a', 'a']
        p = 'aa'
        s = Solution(m, p)
        self.assertEqual(s.hasPath(), True)
        p2 = 'bb'
        s2 = Solution(m, p2)
        self.assertEqual(s2.hasPath(), False)

    def test_4(self):
        m = [['a'], ['a'], ['a']]
        p = 'aa'
        s = Solution(m, p)
        self.assertEqual(s.hasPath(), True)


if __name__ == '__main__':
    unittest.main()

