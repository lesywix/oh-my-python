"""
提目：一个链表中包含环，如何找出环的入口结点？
总结：
先确定是否存在环：设置两个一快一慢指针，如果相遇，则存在环，并且相遇点在环中。
再确定环中的节点个数：循环环中的某一个节点（由前一个问题可得），直到回到该节点，可得环中节点数
最后找到环起始节点：设置两个指针，一个在起点，一个在起点后的第 n 个节点（n 为环中节点数，由前一个问题可得），以相同速度向前移动，直到两者相同则是环的起始节点
"""

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'<ListNode object val: {self.val} next_val: {getattr(self.next, "val", None)}>'


def has_meeting_node(node):
    if node is None:
        return None

    p_slow = node.next
    if p_slow is None:
        return None
    p_fast = p_slow.next
    while p_fast:
        if p_slow == p_fast:
            return p_slow
        p_slow = p_slow.next
        p_fast = p_fast.next
        if p_fast:
            p_fast = p_fast.next


def entry_node_of_loop(node):
    meeting_node = has_meeting_node(node)
    if not meeting_node:
        return None

    len_of_loop = 1
    flag_node = meeting_node
    while flag_node.next != meeting_node:
        len_of_loop += 1
        flag_node = flag_node.next

    p_fast = node
    for i in range(len_of_loop):
        # start from the last len_of_loop node of the beginning of the node
        p_fast = p_fast.next
    # start from the beginning of the node
    p_slow = node
    # will meet at the entry of the loop
    while p_fast != p_slow:
        p_fast = p_fast.next
        p_slow = p_slow.next
    return p_fast


class Test(unittest.TestCase):
    def test(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node6 = ListNode(6)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node3
        self.assertEqual(3, entry_node_of_loop(node1).val)
