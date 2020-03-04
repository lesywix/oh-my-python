"""
提目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。
总结：变量之间的转换
"""
import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'<ListNode object val: {self.val} next_val: {getattr(self.next, "val", None)}>'


def reverse_node(node):
    if not node.next or not node:
        return node
    next_node = node.next
    node.next = None
    next_next_node = next_node.next

    while next_node:
        # reverse node
        next_node.next = node
        # switch variables
        node = next_node
        next_node = next_next_node
        if next_node:
            next_next_node = next_node.next
    return node


def reverse_node2(head):
    q = head.next
    head.next = None
    while q:
        r = q.next
        q.next = head
        head = q
        q = r
    return head


class Test(unittest.TestCase):
    def test(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4

        n = reverse_node(node1)
        self.assertEqual(4, n.val)
        self.assertEqual(1, n.next.next.next.val)
