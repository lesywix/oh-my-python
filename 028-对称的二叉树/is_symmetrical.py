"""
提目：请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
总结：递归的思想。另外也可以用书本提供的遍历算法，使用前序遍历（LDR）与前序遍历相反的遍历法（RDL）得出的 list 相对比
"""
import unittest


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<{self.val}, {self.left}, {self.right}>'


def is_symmetrical(t):
    def f(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        return f(t1.left, t2.right) and f(t1.right, t2.left)

    return f(t, t)


class Test(unittest.TestCase):
    def test(self):
        n1 = TreeNode(8)
        n2 = TreeNode(6)
        n3 = TreeNode(6)
        n4 = TreeNode(5)
        n5 = TreeNode(7)
        n6 = TreeNode(7)
        n7 = TreeNode(5)
        n1.left, n1.right = n2, n3
        n2.left, n2.right = n4, n5
        n3.left, n3.right = n6, n7

        self.assertEqual(True, is_symmetrical(n1))
