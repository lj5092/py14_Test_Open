#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/3 7:36 下午
# @Author  : LiangJun
# @Filename    : demo01_functools模块中的高阶函数.py

# 引入functools官方库
from functools import partial, lru_cache, wraps
import requests
# partial:偏函数（作用：给函数添加参数的默认值）
# 场景：相当于别人的函数，参数特别多，但是有些参数的值是永远不变的，这样就可以给这些函数加默认值，通过偏函数的方法
# 通过不改源代码的情况下，给源代码的参数增加默认值，就叫偏函数


def work(name,age,sex):
    print("名字： ", name)
    print("年龄： ", age)
    print("性别： ", sex)

# 对work函数进行二次包装
work2 = partial(work, name="lj", sex="man")
work2(age=16)
work2(age=18)
work2(name='ym',sex='girl', age=18)
