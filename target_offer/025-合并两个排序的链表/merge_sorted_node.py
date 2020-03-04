"""
提目：输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按照递增排序的。
例如输入图3.11中的链表1和链表2，则合并之后的升序链表如链表3所示。
总结：需要注意最后节点为 None 的情况，避免链表断裂（另可用递归的思想，代码更加整洁）
"""
import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'<ListNode object val: {self.val} next_val: {getattr(self.next, "val", None)}>'


def get_node_val_list(n):
    r = []
    while n:
        r.append(n.val)
        n = n.next
    return r


def merge_sorted_nodes(n1: ListNode, n2: ListNode):
    if not n1 or not n2:
        return None
    # make minial node as n1
    if n2.val < n1.val:
        n1, n2 = n2, n1

    p1, p2 = n1, n2
    while p1 and p2:
        # print(p1, p2)
        # link the end node
        if not p1.next:
            p1.next = p2
            break

        next_p1 = p1.next
        next_p2 = p2.next

        if p2.val < p1.next.val:
            p1.next = p2
            p2.next = next_p1
            p1 = p1.next
            p2 = next_p2

        elif p2.val >= p1.next.val:
            p1 = next_p1
    return n1


class Test(unittest.TestCase):
    # n1: 1->3->5
    # m2: 2->4->6
    def test_1(self):
        n1 = ListNode(1)
        n2 = ListNode(3)
        n3 = ListNode(5)
        n1.next = n2
        n2.next = n3
        m1 = ListNode(2)
        m2 = ListNode(4)
        m3 = ListNode(6)
        m1.next = m2
        m2.next = m3
        r = merge_sorted_nodes(n1, m1)
        # print(r, r.next, r.next.next, r.next.next.next, r.next.next.next.next, r.next.next.next.next.next)
        self.assertEqual([1, 2, 3, 4, 5, 6], get_node_val_list(r))

    # 两个链表中有重复的数字
    # n1: 1->3->5
    # m2: 1->3->5
    def test_2(self):
        n1 = ListNode(1)
        n2 = ListNode(3)
        n3 = ListNode(5)
        n1.next = n2
        n2.next = n3
        m1 = ListNode(1)
        m2 = ListNode(3)
        m3 = ListNode(5)
        m1.next = m2
        m2.next = m3
        r = merge_sorted_nodes(n1, m1)
        # print(r, r.next, r.next.next, r.next.next.next, r.next.next.next.next, r.next.next.next.next.next)
        self.assertEqual([1, 1, 3, 3, 5, 5], get_node_val_list(r))

    # 两个链表都只有一个数字
    # list1: 1
    # list2: 2
    def test_3(self):
        n1 = ListNode(1)
        m1 = ListNode(2)
        r = merge_sorted_nodes(n1, m1)
        self.assertEqual([1, 2], get_node_val_list(r))

