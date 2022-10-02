#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/3 9:15 下午
# @Author  : LiangJun
# @Filename    : py14_day03_homework.py

"""
1、现有有如下功能函数：
def work(a,b):
    res = a/b
    print('a除B的结果为:',res)
# 调用函数当参数b为0的时候，work执行会报错！如：work(10,0)
# 需求：在不更改函数代码的前提现，实现调用work函数传入参数b为0时，函数不报错，输出结果：参数b不能为零


2、(面试笔试题)请设计一个带参数的装饰器，装饰器接收一个int类型的参数number，可以用来装饰任何的函数，
如果函数运行的时间大于number，则打印出函数名和函数的运行时间
"""
import time


def zero(work1):
    def error1(a, b):
        try:
            work1(a, b)
        except ZeroDivisionError:
            print("参数b不能为零")

    return error1


@zero
def work(a, b):
    res = a/b
    print('a除B的结果为:', res)


def work_int(func):
    def exe(number):
        t1 = time.time()
        func(number)
        time.sleep(1)
        t2 = time.time()
        t3 = t2 - t1
        if (t2-t1) > number:
            print("函数的名字为:{}".format(func.__name__))
            print("函数的执行时长为：%.3fs" % t3)
    return exe


@work_int
def new_int(number):
    pass

def zuiwai(func):
    if not isinstance(func, int):
        raise TypeError("参数namber类型只能为int")
    def zhongjian(hanshu):
        def zuinei(*args, **kwargs):
            t1 = time.time()
            res = hanshu(*args, **kwargs)
            t2 = time.time()
            if t2-t1 > func:
                print("函数的名字为：{},函数的运行时长为{}".format(hanshu.__name__, t2-t1))
            return res
        return zuinei
    return zhongjian


@zuiwai(1)
def work02():
    time.sleep(2)
    print("这个函数")

work02()


if __name__ == '__main__':
    work(5, 2)
    new_int(1)
