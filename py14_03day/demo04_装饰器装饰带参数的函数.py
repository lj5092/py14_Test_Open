#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/19 9:13 下午
# @Author  : LiangJun
# @Filename    : demo04_装饰器装饰带参数的函数.py


def decrator(func):

    def wrapper(*args):
        func(*args)
    return wrapper


@decrator
def work(a, b):
    print("-----work------")
    print('a+b= {}'.format(a+b))

work(11,12)