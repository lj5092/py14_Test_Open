#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 9:42 下午
# @Author  : LiangJun
# @Filename    : demo2_通过装饰器对函数和类进行属性的添加和修改.py


# 闭包形式的装饰器：一般用于对函数调用时，执行的功能进行扩展
# 普通函数的装饰器，一般就是对函数（或者是类）的属性进行添加或修改


def defunc(func):
     func.age = 1
     func.name = 'lj'
     return func


@defunc
def work():
    """
    函数文档字符串
    :return:
    """
    print(work.__name__)

print(work.__dict__)