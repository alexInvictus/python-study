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

#��ŵ���ݹ�  ���
#��n�鶫����Ҫ��a-->c ��һ��������c��ǰn-1���Ƶ�b��
#�ڶ����������һ�鶫����a�Ƶ�c��
#����n-1�����a��b�Ƶ�c��