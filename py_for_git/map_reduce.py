#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def normalize(name):
    return name[0].upper()+name[:-1].lower() 
'''
def prod(L):
    s=1
    for a in L:
        s=s*a
    return s
'''

def prod(L):
    def add(x,y):
        return x*y
    return reduce(add,L)
	
from functools import reduce 

def str2float(s):

#    str=s.split('.')
#    s1=str[0]
#    s2=str[1]
    s1=s[:s.index('.')]
    s2=s[s.index('.')+1:]
    print(s2)	
    def add(x,y):
        return x*10+y
    def delete(y):
        str=1
        while y>0:
            y=y-1
            str=str*0.1
            if y==0:               
                return str
    def char2num(s):
        return{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(add,map(char2num,s1))+reduce(add,map(char2num,s2))*delete(len(s2))		
if __name__ == '__main__':
# 测试:

    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)

    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!') 

    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')