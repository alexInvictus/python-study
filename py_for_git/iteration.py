#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d={'a':1,'b':2,'c':3}

for key in d:            #打印的是dict的key
    print(key)
print(...)

for chr in d.values():   #打印的是dict的values
    print(chr)
print(...)

for chr in d.items():    #打印的是dict的key和value
    print(chr)
print(...)

for key,value in enumerate(['A','C','B']):    #enumerate的功能仅仅是把list变成索引对，不排序
    print(key,value)
print(...)
#用isinstance('abc',Iterable)  来判断是否可迭代
#上面会顺序执行，然后去执行if __name__ == '__main__':里面的函数。
from collections import Iterable

def findMinAndMax(L):
    if not isinstance(L,Iterable):
        raise TypeError('L is not iterable')
    if(len(L)==0):
        return (None,None)
    elif(len(L)==1):
        return (L[0],L[0])
    else:
        min=L[0]
        max=L[0]
        for x in L:
            if(x<min):
                min=x
            if(x>max):
                max=x
        return (min,max)

if __name__ == '__main__':
    # 测试
    if findMinAndMax([]) != (None, None):
        print('测试失败1!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败2!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败3!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):       
        print('测试失败4!')
    elif findMinAndMax(123344) != (1, 9):       
        print('测试失败5!')		
    else:
        print('测试成功!')