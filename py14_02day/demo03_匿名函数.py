#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 8:35 下午
# @Author  : LiangJun
# @Filename    : demo03_匿名函数.py

"""
匿名函数：使用lambda 参数 :表达式(也叫返回值)
add = lambda a,b :a+b
一般用来定义表达式简单的函数，作为函数的参数传递
"""

# 对下边列表进行排序，根据元素的name字段
li2 = [{'id': 1, 'name': 100}, {'id': 7, 'name': 3}, {'id': 9, 'name': 1}]

li2.sort(key=lambda i: i['name'])
li2.sort(key=lambda i: i['name'], reverse=False)
print(li2)