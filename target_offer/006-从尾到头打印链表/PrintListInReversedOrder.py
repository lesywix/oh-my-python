#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 15:10
# @Author  : WIX
# @File    : PrintListInReversedOrder.py

"""
输入一个链表，从尾到头打印链表每个节点的值。
"""

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        l = []
        head = listNode
        while head:
            # 遍历链表，将链表的元素每次都插入到列表的开头，得到的列表便是所求的
            l.insert(0, head.val)
            head = head.next
        return l


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    def test_1(self):
        node1 = ListNode(10)
        node2 = ListNode(11)
        node3 = ListNode(13)
        node1.next = node2
        node2.next = node3
        self.assertEqual(self.s.printListFromTailToHead(node1), [13, 11, 10])

    def test_2(self):
        singleNode = ListNode(12)
        self.assertEqual(self.s.printListFromTailToHead(singleNode), [12])

    def test_3(self):
        test = ListNode(x=None)
        self.assertEqual(self.s.printListFromTailToHead(test), [None])


if __name__ == '__main__':
    unittest.main()
