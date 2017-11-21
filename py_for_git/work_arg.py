#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def product(*args):
    if args==():
#    if args is None or len(args) <= 0:
       raise TypeError("args not null!")
    else:
       str=1
       for arg in args:
           str=str*arg
       return str

if __name__ == '__main__':
    print('product(5)=',product(5))
    print('product(5,6)=',product(5,6))
    print('product(5,6,7)=',product(5,6,7))
    print('product(5,6,7,9)=',product(5,6,7,9))
    if product(5) !=5:
        print("测试失败1")
    elif product(5,6) !=30:
        print("测试失败2")
    elif product(5,6,7) !=210:
        print("测试失败3")
    elif product(5,6,7,9) !=1890:
        print("测试失败4")
    else:		
        try:
            product()
            print("测试失败5")
            print("1")
        except TypeError:
            print("测试成功")