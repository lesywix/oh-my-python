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


def print_tree_tire(tree: Tree):
    # 分行打印节点元素
    res = []
    stack = [tree]
    number_of_current_tire = 1  # 用于记录一层节点数量
    number_of_next_tire = 0  # 用于记录下一层节点数量
    while stack:
        node = stack.pop(0)
        res.append(node.node)
        number_of_current_tire -= 1
        if node.left:
            stack.append(node.left)
            number_of_next_tire += 1
        if node.right:
            stack.append(node.right)
            number_of_next_tire += 1
        if number_of_current_tire == 0:
            res.append('\n')
            number_of_current_tire = number_of_next_tire
            number_of_next_tire = 0
    res = ''.join(res)
    return res


def print_z_tree(tree: Tree):
    # 之字型打印节点
    res = []  # 记录每层元素
    ress = []  # 记录所有结果
    stack = [tree]
    number_of_current_tire = 1  # 用于记录一层节点数量
    number_of_next_tire = 0  # 用于记录下一层节点数量
    while stack:
        node = stack.pop(0)
        res.append(node.node)
        number_of_current_tire -= 1
        if node.left:
            stack.append(node.left)
            number_of_next_tire += 1
        if node.right:
            stack.append(node.right)
            number_of_next_tire += 1
        if number_of_current_tire == 0:
            number_of_current_tire = number_of_next_tire
            number_of_next_tire = 0
            ress.append(res)
            res = []
    # 进行翻转
    for i, res in enumerate(ress):
        if i % 2 == 1:
            res.reverse()

    return ress


class Test(unittest.TestCase):
    def test1(self):
        t1 = Tree('a')
        t2 = Tree('b')
        t3 = Tree('c')
        t4 = Tree('d')
        t5 = Tree('e')
        t6 = Tree('f')
        t7 = Tree('g')
        t1.left, t1.right = t2, t3
        t2.left, t2.right = t4, t5
        t3.left, t3.right = t6, t7
        res = print_tree_from_top_to_bottom(t1)
        print(res)
        self.assertEqual(res, ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

        res = print_tree_tire(t1)
        print(res)

        res = print_z_tree(t1)
        print(res)
