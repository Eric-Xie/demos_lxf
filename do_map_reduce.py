# -*- coding: utf-8 -*-
from functools import reduce

# 利用map()函数，把用户输入的不规范的英文名字，
# 变为首字母大写，其他小写的规范名字。
# 如输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    return name.capitalize()

# 请编写一个prod()函数，
# 可以接受一个list并利用reduce()求积
def prod(L):
    return reduce(lambda x, y: x * y, L)

# 利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456
def str2float(s):
    def f_div(x, y):
        return x / 10 + y
    
    def f_mul(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    l, r = s.split('.')
    return reduce(f_mul, map(char2num, l)) + reduce(f_div, map(char2num, r[::-1])) / 10

def main():

    print("------Demo 1-----")
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)

    print("------Demo 2-----")
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

    print("------Demo 3-----")
    print('str2float(\'123.456\') =', str2float('123.456'))

if __name__ == '__main__':
    main()
