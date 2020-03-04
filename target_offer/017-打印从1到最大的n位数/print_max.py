"""
提目：输入数字n，按顺序打印出从1最大的n位十进制数。比如输入3，则打印出1、2、3一直到最大的3位数即999。
总结：python 不需要考虑大数
"""


def print_max(n):
    for i in range(10 ** n):
        print(i)


if __name__ == '__main__':
    print_max(3)
