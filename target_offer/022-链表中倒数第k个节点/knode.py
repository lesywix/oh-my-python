"""
提目：输入一个链表，输出该链表中倒数第k个结点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾结点是倒数第1个结点。例如一个链表有6个结点，
从头结点开始它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个结点是值为4的结点。
总结：求单向链表中倒数第k个数，若只循环一次，可以用两个指针，第一个指针先往前走k-1步，然后从第k步开始第二个指针指向头结点然后两个指针一起遍历
当地一个指针指向尾节点的时候, 第二个指针正好指向倒数第k个结点
推广: 寻找中间节点,两个指针一起,第一个指针每次走两步,第二个指针每次走一步,快指针指到尾部,慢指针正好指到中间
"""
import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def find_last_k_node(node, k):
    if not node or k <= 0:
        return None
    first_index = node
    for i in range(k-1):
        if first_index.next is None:
            return None
        first_index = first_index.next
    second_index = node
    while first_index.next:
        first_index = first_index.next
        second_index = second_index.next
    return second_index


class Test(unittest.TestCase):
    def test(self):
        node = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node.next = node2
        node2.next = node3
        node3.next = node4
        self.assertEqual(3, find_last_k_node(node, 2).val)
