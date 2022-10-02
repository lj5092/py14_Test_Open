#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/6 9:12 下午
# @Author  : LiangJun
# @Filename    : demo4_unitest框架用例参数化的库DDT的使用.py

"""
setattr用来做属性管理，设置属性的，只要属性是个函数，就能作为方法
"""
class Demo:

    def test_1(self):
        pass


print(Demo.__dict__)

datas = [11, 22, 33, 44]


def login_haha(self, item):
    print("login_haha-----执行了，参数为：", item)


# 使用闭包做数据锁定
def create_method(i):
    def wapper(self):
        login_haha(self, i)
    return wapper


# 通过动态的形式给类添加方法的实现思路
for i in datas:
    name = 'test_1_{}'.format(i)
    wapper = create_method(i)
    # 给类添加方法
    setattr(Demo, name, wapper)
# setattr(对象/类，属性名/方法名，属性值/方法)
print("通过动态形式添加方法后，Demo中的方法有： ")
print(Demo.__dict__)


Demo().test_1_11() # 调用test_1_11()方法相当于执行的闭包，执行的闭包就执行了login_haha这个方法，所以打印出了i的值
Demo().test_1_22()




