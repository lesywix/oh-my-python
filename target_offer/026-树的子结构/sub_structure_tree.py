"""
提目：输入两棵二叉树A和B，判断B是不是A的子结构。
总结：使用递归，注意判断好结束条件
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


# 树的一些基本算法
class BinaryTree(object):
    def __init__(self, tree=None):
        self.tree = tree

    def construct_tree(self, l: TreeNode, d: TreeNode, r: TreeNode):
        if not self.tree:
            self.tree = d
        d.left = l
        d.right = r

    def pre_traversal(self):
        r = []

        def f(t):
            if not t:
                return
            r.append(t.val)
            f(t.left)
            f(t.right)

        f(self.tree)
        return r

    def in_traversal(self):
        r = []

        def f(t):
            if not t:
                return
            f(t.left)
            r.append(t.val)
            f(t.right)

        f(self.tree)
        return r

    def post_traversal(self):
        r = []

        def f(t):
            if not t:
                return
            f(t.left)
            f(t.right)
            r.append(t.val)

        f(self.tree)
        return r

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


def is_subtree(t1: TreeNode, t2: TreeNode):
    r = False
    if t1 and t2:
        # 若根节点值相同，则判断此根节点下所有节点值是否相同，并保留结果 r
        if t1.val == t2.val:
            r = has_subtree(t1, t2)
        # 如果上一个判断不成立，则判断 t1 的子节点
        if not r:
            r = is_subtree(t1.left, t2) or is_subtree(t1.right, t2)
    return r


def has_subtree(t1, t2):
    if not t2:
        return True
    if not t1:
        return False
    if t1.val != t2.val:
        return False
    return has_subtree(t1.left, t2.left) and has_subtree(t1.right, t2.right)


class Test(unittest.TestCase):
    def test(self):
        n1 = TreeNode(8)
        n2 = TreeNode(8)
        n3 = TreeNode(7)
        n4 = TreeNode(9)
        n5 = TreeNode(2)
        n6 = TreeNode(4)
        n7 = TreeNode(7)
        m1 = TreeNode(8)
        m2 = TreeNode(9)
        m3 = TreeNode(2)

        t1 = BinaryTree()
        t1.construct_tree(n2, n1, n3)
        t1.construct_tree(n4, n2, n5)
        t1.construct_tree(n6, n5, n7)
        t2 = BinaryTree()
        t2.construct_tree(m2, m1, m3)

        self.assertEqual(True, is_subtree(t1.tree, t2.tree))

