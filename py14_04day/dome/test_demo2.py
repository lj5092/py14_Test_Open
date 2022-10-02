#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/12 2:08 下午
# @Author  : LiangJun
# @Filename    : test_demo2.py

import unittest
from ddt import ddt, data


test_datas = [
    {'id': 1, 'title': '测试用例1'},
    {'id': 2, 'title': '测试用例2'},
    {'id': 3, 'title': '测试用例3'}
]


@ddt
class TestDemo(unittest.TestCase):

    @data(*test_datas)
    def test_demo1(self, i):
        print(i)
