"""
提目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是
否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1、2、3、4、
5是某栈的压栈序列，序列4、5、3、2、1是该压栈序列对应的一个弹出序列，但
4、3、5、1、2就不可能是该压栈序列的弹出序列。
总结：与书本不一样的解法，使用的额外的 tmp 栈模拟 push 入栈顺序。tmp 初始化为 push_order 头元素
1. 如果 pop_order 头元素不在 tmp 中的话，则将 push_order 入栈 tmp
2. 如果 pop_order 头元素与 tmp 栈顶元素相同，则表示 tmp 出栈，将 tmp 栈顶弹出，并删除 pop_order 头元素
3. 循环 tmp，如果 tmp 中还有元素，表明 tmp 无法模拟 pop_order 出栈顺序。如果 tmp 能完全弹出，则表明 tmp 已经模拟了 pop_order 出栈顺序
"""
import unittest


class Stack(object):
    def __init__(self, push_order: list):
        self.stack = push_order

    def is_correct_pop_order(self, pop_order: list):
        if not pop_order or not self.stack:
            return False
        tmp = [self.stack.pop(0)]
        while tmp:
            if pop_order[0] not in tmp and self.stack:
                tmp.append(self.stack.pop(0))
            elif pop_order[0] in tmp and pop_order[0] == tmp[-1]:
                tmp.pop()
                pop_order.pop(0)
            else:
                return False
        return True


class Test(unittest.TestCase):
    def test(self):
        s = Stack([1, 2, 3, 4, 5])
        self.assertEqual(True, s.is_correct_pop_order([4, 5, 3, 2, 1]))

    def test2(self):
        s = Stack([1, 2, 3, 4, 5])
        self.assertEqual(False, s.is_correct_pop_order([4, 3, 5, 1, 2]))

    def test3(self):
        s = Stack([1, 2, 3, 4, 5])
        self.assertEqual(True, s.is_correct_pop_order([3, 5, 4, 2, 1]))

    def test4(self):
        s = Stack([1, 2, 3, 4, 5])
        self.assertEqual(False, s.is_correct_pop_order([3, 5, 4, 1, 2]))

    def test5(self):
        s = Stack([1])
        self.assertEqual(False, s.is_correct_pop_order([2]))

    def test6(self):
        s = Stack([1])
        self.assertEqual(True, s.is_correct_pop_order([1]))
