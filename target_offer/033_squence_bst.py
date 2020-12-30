"""
提目：判断给定的整数数组是不是二叉搜索树的后序遍历序列
整数数组中不包含重复值
整数序列的最后一个值是根结点，然后比根结点小的值是左子树，剩下的是右子树，递归左右子树
总结：
"""


def is_bst_tree(l):
    left = 0
    root = l[-1]
    while l[left] < root:
        left += 1
    right = left
    while right < len(l) - 1:
        if l[right] < root:
            return False
        right += 1
    rest_left = True if left == 0 else is_bst_tree(l[:left])
    rest_right = True if left == right else is_bst_tree(l[left:right])

    return rest_left and rest_right


if __name__ == '__main__':
    print(is_bst_tree([5, 7, 6, 9, 11, 10, 8]))
