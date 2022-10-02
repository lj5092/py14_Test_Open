#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 8:40 下午
# @Author  : LiangJun
# @Filename    : demo1_装饰器的副作用.py

"""
由于装饰器装饰了函数之后，原函数名指向的是装饰器内部的闭包，于是会产生副作用，无法再通过
原函数名去正常获取函数的属性

"""
import time

def decorator(fun):
    def warpper(*args, **kwargs):
        res = fun(*args, **kwargs)
        print("函数的名字为：{}".format(fun.__name__))
        return res
    return warpper


@decorator
def work01():
    """
    这里是文档字符串
    :return:
    """
    print("函数-----work-----")


print(work01.__name__)
work01()

# =================消除装饰器给函数带来的副作用==================
from functools import wraps

def decorator(fun):
    @wraps(fun)
    def warpper(*args, **kwargs):
        res = fun(*args, **kwargs)
        print("函数的名字为：{}".format(fun.__name__))
        return res
    return warpper


@decorator
def work01():
    """
    这里是文档字符串
    :return:
    """
    print("函数-----work-----")


print("通过使用wraps函数对装饰器的副作用进行消除，在打印被调用函数的名字是就变为：{}".format(work01.__name__))


