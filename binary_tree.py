"""
提目：二叉树遍历算法
"""


class TreeNode(object):
    def __init__(self, x):
        self.x = x
        self.right = None
        self.left = None


def pre_traversal(root: TreeNode):
    def f(root):
        if not root:
            return
        r.append(root.x)
        f(root.left)
        f(root.right)
    r = []
    f(root)
    return r


def in_traversal(root: TreeNode):
    def f(root):
        if not root:
            return
        f(root.left)
        r.append(root.x)
        f(root.right)
    r = []
    f(root)
    return r


def post_traversal(root: TreeNode):
    def f(root):
        if not root:
            return
        f(root.left)
        f(root.right)
        r.append(root.x)
    r = []
    f(root)
    return r


def bfs(root: TreeNode):
    queue = []
    r = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        if node:
            r.append(node.x)
            queue.append(node.left)
            queue.append(node.right)
    return r


def max_depth(root: TreeNode):
    # 求二叉树深度
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


def is_same_tree(p, q):
    # 两树是否相同
    if p is None and q is None:
        return True
    elif p and q:
        return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    else:
        return False
