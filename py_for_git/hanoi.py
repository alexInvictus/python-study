#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def hanoi(n,a,b,c):
    if n==1:
       print(a,'-->',c)
    else:
       hanoi(n-1,a,c,b)
       hanoi(1,a,b,c)
       hanoi(n-1,b,a,c)	   

if __name__ == '__main__':
       hanoi(3,'A','B','C')

#汉诺塔递归  理解
#有n块东西，要从a-->c 第一步，借助c把前n-1块移到b上
#第二步，把最后一块东西从a移到c上
#最后把n-1块借助a从b移到c上