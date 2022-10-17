#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/11 6:26 下午
# @Author  : LiangJun
# @Filename    : demo6_使用new方法实现单例模式.py


class Demo:
    __defull = None  # 定义一个属性，用来判断这个类是否创建过
    def __init__(self):
        print("这是init方法")

    def __new__(cls, *args, **kwargs):
        if not cls.__defull:
            cls.__defull = object.__new__(cls)
        return cls.__defull

a = Demo()
b = Demo()
print(a,b)