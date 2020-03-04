"""
提目：删除链表中重复的节点
总结：可用递归
"""
import unittest


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_duplicate_node(link: Node, vals: set):
    if link is None:
        return
    val = link.val
    if link.next is not None:
        if link.val in vals:
            link.val = link.next.val
            next_node = link.next
            link.next = next_node.next
            del next_node

        vals.add(val)
        delete_duplicate_node(link.next, vals)


class Test(unittest.TestCase):
    def test(self):
        link = Node(1)
        link.next = Node(2)
        link.next.next = Node(2)
        link.next.next.next = Node(3)
        delete_duplicate_node(link, set())
        self.assertEqual(link.next.next.val, 3)
