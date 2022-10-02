#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 8:25 下午
# @Author  : LiangJun
# @Filename    : demo01_生成器对象的方法.py


"""
2、生成器比迭代器多了3个方法：
        g.close()：关闭生成器
        g.send()：和next 一样，可以用来生成数据，可以往生成器内部传递数据
        g.throw()：在生成器内部抛出异常，基本上没啥用

在使用生成器生成数据是
    1、不管使用next还是send方法，每次执行到yield时，就会暂停，并且将yield后边的值返回出来
    2、send使用时，生成器内部必须处于yield暂停的位置（使用send之前，生成器至少是通过next生成过一次数据）
"""


def demo():
    for i in range(5):
        values = yield i
        print("通过send传进来的值为：{}".format(values))

d = demo()
print("通过next方法生成出来的数据为：{}".format(next(d)))
print("send方法生成的数据为：{}".format(d.send('张三')))

