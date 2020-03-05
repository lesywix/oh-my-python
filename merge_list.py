"""
提目：合并两个有序列表
"""
import unittest


# def merge_list(l1, l2):
#     res = []
#     for i in l1:
#         if i < l2[0]:
#             res.append(i)
#         else:
#             rm = 0
#             for j in l2:
#                 if j <= i:
#                     res.append(j)
#                     rm += 1
#                 else:
#                     break
#             l2 = l2[rm:]
#             res.append(i)
#     res.extend(l2)
#     return res


def merge_list(l1, l2):
    res = []
    while l1 and l2:
        if l1[0] <= l2[0]:
            res.append(l1[0])
            l1.pop(0)
        else:
            res.append(l2[0])
            l2.pop(0)
    # append the rest
    res = res + l1 + l2
    return res


class Test(unittest.TestCase):
    def test(self):
        l1, l2 = [1, 3, 5], [2, 4, 6]
        self.assertEqual([1, 2, 3, 4, 5, 6], merge_list(l1, l2))

        l1, l2 = [1, 3, 5], [2, 4, 6]
        self.assertEqual([1, 2, 3, 4, 5, 6], merge_list(l1, l2))

        l1, l2 = [1, 1, 5], [2, 2, 6]
        self.assertEqual([1, 1, 2, 2, 5, 6], merge_list(l1, l2))

