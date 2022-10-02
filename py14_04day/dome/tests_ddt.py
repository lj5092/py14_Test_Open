#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/11 11:00 下午
# @Author  : LiangJun
# @Filename    : tests_ddt.py

import unittest


test_datas = [
    {'id': 1, 'title': '测试用例1'},
    {'id': 2, 'title': '测试用例2'},
    {'id': 3, 'title': '测试用例3'}
]


def create_method(method, value):
    """闭包函数，作用是将测试方法和参数，放到闭包中进行数据锁定
       方法里传入参数"""
    def wrapper(self):
        method(self, value)
    return wrapper


def ddt(cls):
    """遍历测试数据，给类动态添加方法"""
    # 如何通过类获取方法
    # res = cls.__dict__  # 查看类中所有的方法
    # print(res)
    for name, method in list(cls.__dict__.items()):  # 遍历属性名和属性值
        print(name, method)  # 打印所有的属性名和属性值
        if hasattr(method, 'datas'):  # 判断遍历出来的属性值是否用后datas这个数据
            # print(name, method)
            datas = getattr(method, 'datas')  # 获取方法中保存的测试数据
            for index, value in enumerate(datas):
                print("数据：", value, '顺序：', index)
                # 接下来给测试类动态添加测试用例
                method_name = '{}_{}'.format(name, index+1)
                print("方法名：", method_name, method)
                wrapper = create_method(method, value)
                setattr(cls, method_name, wrapper)
            else:
                delattr(cls, name)
    return cls


def data(*args):
    """
    将测试数据，保存为测试方法的属性
    :param args:
    :return:
    """
    # arge 接受到的是data传递的进来的数据
    def wapper(func):
        # func 接收到的是data装饰的函数
        func.datas = args  # 动态生成几条方法的属性数据datas并保存
        return func
    return wapper


@ddt
class TestDemo(unittest.TestCase):

    @data(*test_datas)
    def test_demo1(self, item):
        print("执行的测试用例是：", item)
