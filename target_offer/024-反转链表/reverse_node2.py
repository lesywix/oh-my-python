"""
提目：1->2->3->4 转换成 2->1->4->3.
总结：
"""
import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __len__(self):
        length = 1
        next = self.next
        while next is not None:
            length += 1
            next = next.next
        return length

    def __repr__(self):
        return f'<ListNode object val: {self.val} next_val: {getattr(self.next, "val", None)}>'


def reverse(node):
    if node.next is None or len(node) % 2 != 0:
        raise ValueError('node incorrect')
    res = node.next
    next_node = node.next

    # only one couple
    if len(node) < 3:
        node.next = None
        next_node.next = node
        return next_node

    second_couple_1 = node.next.next
    second_couple_2 = second_couple_1.next
    while second_couple_1 is not None:
        next_node.next = node
        node.next = second_couple_2

        node, next_node = second_couple_1, second_couple_2

        second_couple_1 = getattr(node.next, 'next', None)
        second_couple_2 = second_couple_1.next if second_couple_1 else None
    next_node.next = node
    node.next = None
    return res


def reverse2(node):
    # 迭代的方法，更清晰明了
    if node is not None and node.next is not None:
        next = node.next
        node.next = reverse2(next.next)
        next.next = node
        return next
    return node


class Test(unittest.TestCase):
    def test(self):
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n4 = ListNode(4)
        n5 = ListNode(5)
        n6 = ListNode(6)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n6
        res = reverse2(n1)
        self.assertEqual(2, res.val)
        self.assertEqual(1, res.next.val)
        self.assertEqual(4, res.next.next.val)
        self.assertEqual(5, res.next.next.next.next.next.val)
