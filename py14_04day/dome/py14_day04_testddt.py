#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/12 10:52 下午
# @Author  : LiangJun
# @Filename    : py14_day04_testddt.py
import unittest

datas = [{'id': 1, 'name': '第一条case'},
{'id': 2, 'name': '第二条case'},
{'id': 3, 'name': '第三条case'}
]


def bibao(method, value):
    def wrapper(self):
        method(self, value)
    return wrapper


def data(*args):
    def wrapper(func):
        func.datas = args
        return func
    return wrapper


def ddt(cls):
    """
    name:test_demo
    method_name:test_demo_1
    value:{'id': 1, 'title': '测试用例1'}

    :param cls:
    :return:
    """
    for name, method in list(cls.__dict__.items()):
        # print(name, method)
        if hasattr(method, 'datas'):
            print(name, method)
            datas = getattr(method, 'datas')
            # 遍历数据，并把索引取出来
            for index, value in enumerate(datas):
                method_name = '{}_{}'.format(value, index+1)
                wrapper = bibao(method, value)
                setattr(cls, method_name, wrapper)
            else:
                delattr(cls, name)
    return cls


@ddt
class DemoTest(unittest.TestCase):

    @data(*datas)
    def test_demo(self, case):
        print("执行用例：", case)
