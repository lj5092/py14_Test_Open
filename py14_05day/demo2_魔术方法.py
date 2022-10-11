#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/19 9:25 下午
# @Author  : LiangJun
# @Filename    : demo2_魔术方法.py


"""
在python中，所有以双下划线开头的方法，例如__init__，都叫魔术方法
魔术方法不需要手动去调用，是在特定的情况下触发执行的
__init__:对对象做初始化
__call__:实现对象可调用，可用callable方法进行验证
"""


class Demo():

    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        """对象后边加括号，调用的时候执行__call__方法
           之后该对象就变成了可调用对象"""
        print(self.name, '调用了')


d = Demo('lj')
d()  # 对象调用的时候触发了__call__方法，之后就变成了可调用对象
print("如果返回值是True，那么就是可调用对象：返回值为：{}".format(callable(d)))
