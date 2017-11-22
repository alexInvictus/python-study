#!/usr/bin/env python3
# -*- coding: utf-8 -*-



max,min=min,max                    #这个复制，并不是像C语言一样。min和max同时赋值了。也就是说max和min的功能反调了

print(max(1,2,3,4,5))

print(min(1,2,3,4,5))              #


def add(x,y,f):
    return f(x)+f(y)

def power(*args):
    str=1
    for sar in args:
        str=str*sar
    return str
	
f=power

def add2(f,nums):
    s=0
    for k in nums:
        s=s+f(k,2)
    return s


if __name__ == '__main__':
 #   print(add(-5,6,abs))           #可以把函数名复制给一个变量，这个变量会指向这个函数
                                   #可以理解为函数名本身就是一个变量，指向函数的一个变量
    ss=list(range(10,100,10))
    print(add2(f,ss))
    
