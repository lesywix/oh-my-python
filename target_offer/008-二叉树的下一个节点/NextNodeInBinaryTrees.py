#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 9:33
# @Author  : WIX
# @File    : NextNodeInBinaryTrees.py

"""
给定一棵二叉树和其中的一个结点，如何找出中序遍历顺序的下一个结点？
树中的结点除了有两个分别指向左右子结点的指针以外，还有一个指向父结点的指针。
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        if pNode is None:
            return None
        # 若此节点存在右子树，则找右子树的最左节点
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        # 若此节点不存在右子树
        else:
            # 需要先判断父节点存不存在，否则会报错
            # 此节点是父节点的左子节点，则父节点就是下一个节点
            if pNode.next and pNode == pNode.next.left:
                pNode = pNode.next
                return pNode
            # 此节点是父节点的右子节点，则沿父节点向上遍历，找到一个是他父节点的右子节点的节点
            elif pNode.next and pNode == pNode.next.right:
                while pNode.next is not None:
                    if pNode == pNode.next.left:
                        return pNode.next
                    pNode = pNode.next
                return None


node1 = TreeLinkNode('a')
node2 = TreeLinkNode('b')
node3 = TreeLinkNode('c')
node4 = TreeLinkNode('d')
node5 = TreeLinkNode('e')
node6 = TreeLinkNode('f')
node7 = TreeLinkNode('g')
node8 = TreeLinkNode('h')
node9 = TreeLinkNode('i')

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node2.next = node1
node3.left = node6
node3.right = node7
node3.next = node1
node4.next = node2
node5.left = node8
node5.right = node9
node5.next = node2
node6.next = node3
node7.next = node3
node8.next = node5
node9.next = node5

s = Solution()
result = s.GetNext(node7)
if result:
    print(result.val)
else:
    print(result)