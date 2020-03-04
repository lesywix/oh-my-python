#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 18:44
# @Author  : WIX
# @File    : RobotMove.py

"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""

"""
总结：
一般矩阵运动问题都可以用回溯法解决，可以将每个功能写成独立的函数，比较好理解
通常可以将二维数组转化为一维数组，简化操作
"""


class Solution:
    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows < 0 or cols < 0:
            return False
        # 记录走过的方块
        visited = [0] * (rows * cols)
        count = self.movingCountCore(threshold, rows, cols, 0, 0, visited)
        return count

    def movingCountCore(self, threshold, rows, cols, row, col, visited):
        count = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row * cols + col] = 1
            count = 1 + self.movingCountCore(threshold, rows, cols, row, col - 1, visited) + \
                    self.movingCountCore(threshold, rows, cols, row - 1, col, visited) + \
                    self.movingCountCore(threshold, rows, cols, row, col + 1, visited) + \
                    self.movingCountCore(threshold, rows, cols, row + 1, col, visited)
        return count

    # 判断是否可进入某格子
    def check(self, threshold, rows, cols, row, col, visited):
        if rows > row >= 0 and cols > col >= 0 and self.getDigitSum(row) + self.getDigitSum(col) <= threshold and \
                        visited[row * cols + col] == 0:
            return True
        return False

    # 计算一个数字位数相加和
    def getDigitSum(self, number):
        sum = 0
        while number > 0:
            sum += number % 10
            number //= 10
        return sum


s = Solution()
print(s.movingCount(5, 10, 10))
