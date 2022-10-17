#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/11 6:26 下午
# @Author  : LiangJun
# @Filename    : demo6_使用new方法实现单例模式.py


class Demo:
    __defull = None  # 定义一个属性，用来判断这个类是否创建过
   # 为了安全，将这个属性设置为私有属性，这样在外边就不能被修改了
    def __init__(self):
        print("这是init方法")

    def __new__(cls, *args, **kwargs):
        if not cls.__defull:
            # cls.__defull == None 若果b属性没有值，那么就创建一个
            cls.__defull = object.__new__(cls)
        return cls.__defull

a = Demo()
b = Demo()
print(a,b)