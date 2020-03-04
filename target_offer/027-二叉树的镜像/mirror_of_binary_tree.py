"""
提目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。
总结：用递归解决，注意退出条件
"""
import unittest
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<{self.val}, {self.left}, {self.right}>'


class BinaryTree(object):
    def __init__(self, tree=None):
        self.tree = tree

    def bfs(self):
        r = []
        q = deque([self.tree])
        while q:
            n = q.popleft()
            if n:
                r.append(n.val)
                q.append(n.left)
                q.append(n.right)
        return r


def mirror_reverse(t):
    if not t:
        return
    t.left, t.right = mirror_reverse(t.right), mirror_reverse(t.left)
    return t


class Test(unittest.TestCase):
    def test(self):
        n1 = TreeNode(8)
        n2 = TreeNode(6)
        n3 = TreeNode(10)
        n4 = TreeNode(5)
        n5 = TreeNode(7)
        n6 = TreeNode(9)
        n7 = TreeNode(11)
        n1.left, n1.right = n2, n3
        n2.left, n2.right = n4, n5
        n3.left, n3.right = n6, n7

        r = mirror_reverse(n1)
        t = BinaryTree(r)
        self.assertEqual([8, 10, 6, 11, 9, 7, 5], t.bfs())
