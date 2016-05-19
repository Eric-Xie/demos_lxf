# -*- coding: utf-8 -*-

import time
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s()" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

def log2(func):
    def wrapper(*args, **kw):
        print("begin call")
        res = func(*args, **kw)
        print("end call")
        return res    
    return wrapper

@log("excute")
def now():
    print(time.strftime('%Y-%m-%d',time.localtime(time.time())))

@log2
def test():
    print("test")

def main():
    print("------Demo 1-----")
    now()

    print("------Demo 2-----")
    test()

if __name__ == '__main__':
    main()

