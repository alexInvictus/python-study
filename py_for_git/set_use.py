#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#set集合，也是一组key的集合。但是不存储value，由于key不能重复，所以,在set中，没有重复的key
#即使输入有重复，set后会自动过滤掉。顺序出来的结果并不表示set有排序的功能，只是告诉你有这个值
#set只接受一个变量。且变量中不可以含有可变的元素
set(1)              #错误，set只接受iterable的变量
set(1,2)            #错误，包含了两个元素
set((1,2,[2,3]))    #错误tuple中含有list元素，可变