#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25 19:30
# @Author  : WIX
# @File    : ConstructBinaryTree.py

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""

import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        # 找到中序队列中根节点的下标
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:i + 1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i + 1:], tin[i + 1:])
        return root


pre = [1, 2, 4, 7, 3, 5, 6, 8]  # [1, 2, 3, 5, 6, 4]
tin = [4, 7, 2, 1, 5, 3, 8, 6]  # [5, 3, 6, 2, 4, 1]
test = Solution()
newTree = test.reConstructBinaryTree(pre, tin)


# 利用队列实现树的层次遍历
def level_queue(root):
    if root is None:
        return
    myQueue = []
    node = root
    myQueue.append(node)
    while myQueue:
        node = myQueue.pop(0)
        print(node.val)
        if node.left is not None:
            myQueue.append(node.left)
        if node.right is not None:
            myQueue.append(node.right)


level_queue(newTree)
