# -*- coding: utf-8 -*-
# 素数算法：埃氏筛法
# 首先，列出从2开始的所有自然数，构造一个序列：
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 不断筛下去，就可以得到所有的素数。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

# 回数是指从左向右读和从右向左读都是一样的数，
# 例如12321，909
def is_palindrome(n):
    s = str(n)
    for i in range(int(len(s)/2)):
        if s[i] != s[-i-1]:
            return False
    return True

def main():
    print("------Demo 1-----")
    print("Print primes in [2, 100]")
    l = []
    for n in primes():
        if n < 100:
            l.append(n)
        else:
            break
    print(l)

    print("------Demo 2-----")
    print("Print palindrome number in [1, 1000]")
    output = filter(is_palindrome, range(1, 1000))
    print(list(output))

if __name__ == '__main__':
    main()
