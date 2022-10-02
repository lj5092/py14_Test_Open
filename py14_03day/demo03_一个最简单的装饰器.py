#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/3 8:36 下午
# @Author  : LiangJun
# @Filename    : demo03_一个最简单的装饰器.py

"""
面向对象的一个原则：开放封闭原则
    开放：
    封闭：

装饰器可以用来做什么？
    可以在不修改功能函数内部代码的情况下，给功能函数进行扩展新的功能，(对开放封闭原则有很好的提现)

装饰器的定义：
    1、闭包实现装饰器
        def login_check(func):
            def work():
                函数执行前的功能扩展代码
                func()
                函数执行后的功能扩展代码
            return work
    2、类实现
    3、普通函数
    只要是可调用的对象，都可以作为装饰器使用

可调用的对象？
    加括号就可以想调用函数一样执行，可以通过内置函数callable来进行判断
    a = callable(函数名)
    如果返回true 就是可调动对象

    @艾特函数就是调用这个函数，然后在调用函数时会把被装饰的函数当成参数传进去


"""

# 装饰器的创建于使用：如下demo


def demo(fun):
    def hello():
        print("今天要先将排期任务完成")
        fun()
        print("要写木森老师留的作业")
    return hello


@demo
def work():
    print("我今天要上柠檬班的课")

work()