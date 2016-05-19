# -*- coding: utf-8 -*-
# functools.partial把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数

import functools

def main():

    print("------Demo 1-----")
    int2 = functools.partial(int, base=2)
    print("1000000 convert to %d" % int2('1000000'))


if __name__ == '__main__':
    main()