"""
提目：给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该结点。
总结：
"""
import unittest


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(link, node):
    # only one node
    if link is node:
        del node
    # node is the last node
    if node.next is None:
        while link:
            if link.next is node:
                link.next = None
            link = link.next
    else:
        node.val = node.next.val
        next_node = node.next
        node.next = next_node.next
        del next_node


class Test(unittest.TestCase):
    def test(self):
        link = Node(1)
        link.next = Node(2)
        link.next.next = Node(3)
        delete_node(link, link.next)
        self.assertEqual(link.next.next, None)
        self.assertEqual(link.next.val, 3)
