#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 8:57 下午
# @Author  : LiangJun
# @Filename    : demo1_多个装饰器装饰同一个函数.py

import unittest
from ddt import ddt, data, unpack


@ddt
class TestCase(unittest.TestCase):

    @unpack
    @data(*datas)
    def test_log(self, title, data, res):
        print("用例数据为：", title)
        print("用例数据为：", data)
        print("用例数据为：", res)


# 调用unpack需要给给他传参，传的参数是另一个装饰器
# test_log = unpack(data(*datas)(test_log))
