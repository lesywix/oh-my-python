"""
提目：不分行从上往下打印二叉树
总结：二叉树层次遍历
"""
import unittest


class Tree:
    def __init__(self, v):
        self.node = v
        self.left = None
        self.right = None


def print_tree_from_top_to_bottom(tree: Tree):
    res = []
    stack = [tree]
    while stack:
        node = stack.pop(0)
        res.append(node.node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res


class Test(unittest.TestCase):
    def test1(self):
        t1 = Tree('a')
        t2 = Tree('b')
        t3 = Tree('c')
        t4 = Tree('d')
        t5 = Tree('e')
        t1.left, t1.right = t2, t3
        t2.left, t2.right = t4, t5
        res = print_tree_from_top_to_bottom(t1)
        print(res)
        self.assertEqual(res, ['a', 'b', 'c', 'd', 'e'])
