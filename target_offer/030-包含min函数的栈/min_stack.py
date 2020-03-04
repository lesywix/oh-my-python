"""
提目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数。在该栈中，调用min、push及pop的时间复杂度都是O(1)。
总结：可使用额外的栈来存最小值，保证操作时间复杂度都是 O(1)
"""
import unittest


class Stack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if self.min_stack and self.min_stack[-1] < x:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()
        return None

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None


class Test(unittest.TestCase):
    def test(self):
        s = Stack()
        s.push(3)
        s.push(4)
        s.push(2)
        s.push(1)
        self.assertEqual(1, s.min())
        s.pop()
        self.assertEqual(2, s.min())
        s.pop()
        self.assertEqual(3, s.min())
        s.push(0)
        self.assertEqual(0, s.min())
