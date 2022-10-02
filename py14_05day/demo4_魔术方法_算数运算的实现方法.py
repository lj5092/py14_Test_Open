#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/29 9:18 下午
# @Author  : LiangJun
# @Filename    : demo4_魔术方法_算数运算的实现方法.py

class Demo:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        # 两个对象进行相加，触发的魔术方法

       print(self.number)  # 相当于self接收的是a，other接收的是b
       print(other.number)
       return 999

a = Demo(11)
b = Demo(22)
print(a+b)  # a + b ==> self.__add__(a,b),如果类中有__add__的魔术方法，就可以进行相加的操作