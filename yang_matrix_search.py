"""
提目：在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
import unittest


def matrix_search(matrix, x):
    rows = len(matrix)
    cols = len(matrix[0])
    i = 0
    j = cols - 1
    while i < rows and j >= 0:
        if matrix[i][j] == x:
            return True
        elif matrix[i][j] < x:
            i += 1
        else:
            j -= 1
    return False


class Test(unittest.TestCase):
    def test(self):
        matrix = [
            [1, 2, 31],
            [2, 3, 44],
            [5, 55, 555]
        ]
        self.assertEqual(True, matrix_search(matrix, 3))
        self.assertEqual(True, matrix_search(matrix, 31))
        self.assertEqual(True, matrix_search(matrix, 2))
        self.assertEqual(True, matrix_search(matrix, 55))

        self.assertEqual(False, matrix_search(matrix, 6))
        self.assertEqual(False, matrix_search(matrix, 9))
        self.assertEqual(False, matrix_search(matrix, 33))
        self.assertEqual(False, matrix_search(matrix, 300))
