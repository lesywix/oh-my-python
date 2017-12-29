#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 16:42
# @Author  : WIX
# @File    : StackWithTwoQueues.py

"""
拓展：
用两个队列实现栈
"""


class Solution(object):
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    # 往队列中有元素的
    def push(self, node):
        if self.queue1:
            self.queue1.append(node)
        else:
            self.queue2.append(node)

    def pop(self):
        if not self.queue2 and not self.queue1:
            return None
        if self.queue1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()
        else:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()


s = Solution()
s.push(10)
s.push(11)
s.push(12)
print(s.pop())
s.push(13)
print(s.pop())
print(s.pop())
print(s.pop())

