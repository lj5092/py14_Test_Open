#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/10 9:25 下午
# @Author  : LiangJun
# @Filename    : demo5_魔术方法_new方法.py


class Demo(object):

    def __init__(self):
        print("这个是init方法")

    def __new__(cls, *args, **kwargs):
        """实例化对象时，是通过new方法来创建对象的"""
        print("这个是new方法")
        obj = object.__new__(cls)
        # return 'python'
        return obj


d = Demo()
print(d)