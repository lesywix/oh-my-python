"""
提目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""
import unittest


def is_numeric(s):
    if s is None or len(s) <= 0:
        return False
    s_list = [i.lower() for i in s]
    if 'e' in s_list:
        index_e = s_list.index('e')
        front = s_list[:index_e]
        behind = s_list[index_e + 1:]
        if '.' in behind or len(behind) == 0:
            return False
        is_digit_front = is_digit(front)
        is_digit_behind = is_digit(behind)
        return is_digit_behind and is_digit_front
    else:
        return is_digit(s_list)


def is_digit(s_list):
    dot_num = 0
    allow_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.', 'e']
    for i in range(len(s_list)):
        if s_list[i] not in allow_values:
            return False
        if s_list[i] == '.':
            dot_num += 1
        if s_list[i] in '+-' and i != 0:
            return False
    if dot_num > 1 or (dot_num == 1 and len(s_list) == 1):
        return False
    return True


class Test(unittest.TestCase):
    def test_success(self):
        self.assertEqual(True, is_numeric("100"))
        self.assertEqual(True, is_numeric("123.45e+6"))
        self.assertEqual(True, is_numeric("+500"))
        self.assertEqual(True, is_numeric("5e2"))
        self.assertEqual(True, is_numeric("1.79769313486232E+308"))
        self.assertEqual(True, is_numeric("-1E-16"))
        self.assertEqual(True, is_numeric("-.123"))
        self.assertEqual(True, is_numeric("600."))

    def test_fail(self):
        self.assertEqual(False, is_numeric("12e"))
        self.assertEqual(False, is_numeric("1a3.14"))
        self.assertEqual(False, is_numeric("1+23"))
        self.assertEqual(False, is_numeric("1.2.3"))
        self.assertEqual(False, is_numeric("+-5"))
        self.assertEqual(False, is_numeric("12e+5.4"))
        self.assertEqual(False, is_numeric("."))
        self.assertEqual(False, is_numeric(".e1"))

