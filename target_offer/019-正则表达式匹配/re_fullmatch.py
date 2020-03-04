"""
提目：请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
总结：使用递归来解决问题，重点在于对 '*' 的匹配
"""
import unittest


def full_match(s, pattern):
    # pattern 与 s 不能完全匹配，结束递归
    if len(pattern) == 0 and len(s) > 0:
        return False
    # pattern 与 s 都完全匹配，结束递归
    if len(pattern) == 0 and len(s) == 0:
        return True
    # 如果 pattern 第二个字符是 *，则可以选择忽略或者继续匹配
    if len(pattern) > 1 and pattern[1] == '*':
        # 若首位能匹配，则可以将 pattern 往后移两位，或者保持该 pattern 不变
        if len(s) > 0 and (pattern[0] == s[0] or pattern[0] == '.'):
            return full_match(s, pattern[2:]) or full_match(s[1:], pattern)
        # 如果首位不能匹配，则将 pattern 往后移两位，相当于忽略该 pattern
        else:
            return full_match(s, pattern[2:])

    # 如果 pattern 第二个字符不是 *
    if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
        return full_match(s[1:], pattern[1:])
    return False


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(full_match("", ""), True)
        self.assertEqual(full_match("", ".*"), True)
        self.assertEqual(full_match("", "."), False)
        self.assertEqual(full_match("", "c*"), True)
        self.assertEqual(full_match("a", ".*"), True)
        self.assertEqual(full_match("a", "a."), False)
        self.assertEqual(full_match("a", ""), False)
        self.assertEqual(full_match("a", "."), True)
        self.assertEqual(full_match("a", "ab*"), True)
        self.assertEqual(full_match("a", "ab*a"), False)
        self.assertEqual(full_match("aa", "aa"), True)
        self.assertEqual(full_match("aa", "a*"), True)
        self.assertEqual(full_match("aa", ".*"), True)
        self.assertEqual(full_match("aa", "."), False)
        self.assertEqual(full_match("ab", ".*"), True)
        self.assertEqual(full_match("ab", ".*"), True)
        self.assertEqual(full_match("aaa", "aa*"), True)
        self.assertEqual(full_match("aaa", "aa.a"), False)
        self.assertEqual(full_match("aaa", "a.a"), True)
        self.assertEqual(full_match("aaa", ".a"), False)
        self.assertEqual(full_match("aaa", "a*a"), True)
        self.assertEqual(full_match("aaa", "ab*a"), False)
        self.assertEqual(full_match("aaa", "ab*ac*a"), True)
        self.assertEqual(full_match("aaa", "ab*a*c*a"), True)
        self.assertEqual(full_match("aaa", ".*"), True)
        self.assertEqual(full_match("aab", "c*a*b"), True)
        self.assertEqual(full_match("aaca", "ab*a*c*a"), True)
        self.assertEqual(full_match("aaba", "ab*a*c*a"), False)
        self.assertEqual(full_match("bbbba", ".*a*a"), True)
        self.assertEqual(full_match("bcbbabab", ".*a*a"), False)
