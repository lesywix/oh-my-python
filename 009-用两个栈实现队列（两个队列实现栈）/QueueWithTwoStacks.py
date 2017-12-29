#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 16:06
# @Author  : WIX
# @File    : QueueWithTwoStacks.py


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack2 and not self.stack1:
            return None
        elif not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()


s = Solution()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
s.push(4)
print(s.pop())
print(s.pop())
s.push(5)
print(s.pop())
print(s.pop())
