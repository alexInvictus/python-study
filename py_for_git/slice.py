#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
def trim(s):
    if len(s)==0:
       return ''
    if s[-1]==' ':
       s=s[:-1]
       return trim(s)
    elif s[0]==' ':
       s=s[1:]
       return trim(s) 
    elif s[0]==' ' and s[-1]==' ':
       s=s[1:-1]
       return trim(s)	
    else:
       return s
'''
def trim(vstr):
    if(len(vstr)==0 or (vstr[0]!=' ' and vstr[-1]!=' ')):
        return vstr
    else:       
        return trim(vstr[0]==' ' and vstr[1:] or vstr[:-1])
	   
if __name__ == '__main__':
    # 测试:
    if trim('hello  ') != 'hello':
        print('测试失败1!')
    elif trim('  hello') != 'hello':
        print('测试失败2!')
    elif trim('  hello  ') != 'hello':
        print('测试失败3!')
    elif trim('') != '':
        print('测试失败4!')
    elif trim('    ') != '':
        print('测试失败5!')
    else:
        print('测试成功!')

#s[1:-1]  从第一个元素开始到倒数第二个元素结束		
#切片那一节没有理解#号部分为什么错了   错误原因：''不等于' '判断有没有空格