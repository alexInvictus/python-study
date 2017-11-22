#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#列表生成式和生成器
list(range(1,11))  #list生成。生成一个从1-10的list

list(range(0))     #list生成。生成一个空list

print(range(0))

x='abc'

isinstance(x,str)   #isinstance判断一个变量是不是字符串

L1=['hello','World',18,'Apple',None]
L3=[]
for a in L1:
    if isinstance(a,str):
        L3.append(a.lower())
print(L3)
print(...)
L2=[]
L2=[a.lower() for a in L1 if isinstance(a,str)]
print(L2)
print(...)

g=(x*x for x in range(10))#生成器和list的唯一不同是[]变成() 通过next()打印出下一个值
                          #一般用for...in...去调用
def fib(max):             #普通的函数
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return "done"

def gener(max):             #只要函数中有yield，就是generator生成器
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return "done"

#work for generator
def triangle():
    N=[1]
    while True:
        yield N
        N.append(0)
        N=[N[i-1]+N[i] for i in range(len(N))] #写法

		
if __name__ == '__main__':          #一个生成器就是一个列表，但是是通过你的次数在决定列表的大小
    n=0                             #n来控制打印次数（或者说是生成器生成次数）每一次生成器的运行都会在list后面添加一个次数。
    for t in triangle():
        print(t)
        n=n+1
        if n==10:
            break;
'''
    fib(3)
    g=gener(3)
	next(g)                 #在程序中直接用next没有办法打印出生成器的值 在python解释器中直接用next语句可以逐条打印出来
    for a in g:             #需要用迭代的方式打印出生成器的值
        print(a)            
'''	
			
#TabError: inconsistent use of tabs and spaces in indentation  用tab缩进了
#补充range用法
# range(1,5)  代表从1到5不包含5           [1,2,3,4]
# range(1,5,2)代表从1到5，间隔2，不包含5  [1,3]
# range(5)    代表从0到5不包含5           [0,1,2,3,4]




