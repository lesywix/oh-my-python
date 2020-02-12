"""
提目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
总结：需要注意边界条件
"""
import unittest


def print_matrix(matrix):
    r = []
    entry = 0
    length = len(matrix[0]) if matrix else 0
    width = len(matrix)
    while entry * 2 < length or entry * 2 < width:
        print_circle(matrix, entry, length, width, r)
        entry += 1
    print(r)
    return r


def print_circle(matrix, entry, length, width, r):
    # the last row
    row = length - entry - 1
    # the last column
    col = width - entry - 1

    # left -> right
    for i in range(entry, col + 1):
        r.append(matrix[entry][i])

    # top -> bottom
    if entry < row:
        for i in range(entry + 1, row + 1):
            r.append(matrix[i][col])

    # right -> left
    if entry < row and entry < col:
        for i in range(entry, col)[::-1]:
            r.append(matrix[row][i])

    # bottom -> top
    if entry < col and entry < row:
        for i in range(entry + 1, row)[::-1]:
            r.append(matrix[i][entry])


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(
            [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
            print_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        )
