#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
	x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
	x2=(-b-math.sqrt(power(b)-4*a*c))/(2*a)
	
	return x1,x2
	
#def main():
	
print('quadratic(2,3,1)=',quadratic(2,3,1))
print('quadratic(1,3,-4)=',quadratic(1,3,-4))	
	
#return 的值不能含有传入参数
#/2*a的意思是除以2，乘以a，而不是除以2a


