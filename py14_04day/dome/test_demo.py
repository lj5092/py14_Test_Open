#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/7 9:17 下午
# @Author  : LiangJun
# @Filename    : test_demo.py
# 需要先 pip install ddt
import unittest
from ddt import ddt, data
test_datas = [
    {'id': 1, 'title': '测试用例1'},
    {'id': 2, 'title': '测试用例2'},
    {'id': 3, 'title': '测试用例3'}
]


@ddt
class TetsDemo(unittest.TestCase):

    @data(*test_datas)
    def test_demo1(self, jie_shou_can_shu):
        print("测试用例执行:", jie_shou_can_shu)


"""
unitests中的测试用例：
    测试类中的每一个test开头的方法，就是一条测试用例
    
ddt生成根据用例数据生成测试用例的思路：
    1、利用data装饰器，传入测试数据，在装饰器中将测试数据保存起来
    2、data装饰器遍历测试数据，每遍历处一条数据，往测试类中添加一个test开头的方法
        通过 setattr(类，方法名，方法) 对类进行设置
"""
