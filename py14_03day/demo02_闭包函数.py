#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/3 8:05 下午
# @Author  : LiangJun
# @Filename    : demo02_闭包函数.py

# 什么是闭包函数？
# 函数+一个外层封闭的作用域,就会形成一个闭包
"""
闭包的三个特征：面试
    1、函数中嵌套函数
    2、外层函数返回值为 内层函数
    3、内层嵌套函数 有引用外部的非全局变量（引用外部函数作用域内的局部变量）

    场景：用来写装饰器和数据锁定
    后期做unitest中ddt更改时，做数据锁定
"""


def demo(name):
    a = 100
    def work():
        print("外层函数中作用域中的a= {}".format(a))
        print(name)
    return work
g = demo("liangjun")
g()
