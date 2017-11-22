#!/usr/bin/env python3
# -*- coding: utf-8 -*-


L1=['Hello','World',18,'Apple',None]
L2=[]

def product(L):
    for l in L :
        if isinstance(l,str):
            print(l)

		
if __name__ == '__main__':
    product(L1)