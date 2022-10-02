#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/19 9:42 下午
# @Author  : LiangJun
# @Filename    : demo3_通过类实现装饰器.py

"""
类实现装饰器，在类中一个__init__,__call__,就可以实现装饰器
"""


# 一、类实现装饰器，装饰不带参数的函数
class Demo:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("调用前执行")
        self.func()
        print("调用后执行")

@Demo  # test = Demo(test)
def test():
    print("你好")


# 如果想对象+括号就能执行的话，就需要在类中添加__call__方法，这样再通过类添加装饰器，装饰函数的时候，
# 就可以直接使用函数名进行执行操作，如下：
test()


# 二、类实现装饰器，装饰带参数的函数
class Tow():

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("执行函数前执行的代码")
        result = self.func(*args, **kwargs)
        print("执行函数后执行的代码")
        return result

@Tow
def tow_test(a, b):
    return a+b

tow = tow_test(111, 222)
print(tow)

# 三，类实现装饰器，装饰器带参数

class Three():

    def __init__(self, number):
        self.number = number
        print(self.number)

    def __call__(self, func):
        self.func = func
        return self.run

    def run(self, *args, **kwargs):
        print("装饰之前执行")
        res = self.func(*args, **kwargs)
        print("装饰之后执行")
        return res


@Three('123haha ')
def three_test():
    print("three_test执行了")
    return "lemon"

print(three_test())
three_test()

# ________________将多个装饰器封装到一个类____________


class Mytest:

    @staticmethod  # 静态方法
    def work1(func):
        def wrapper(*args, **kwargs):
            res = func()
            return res
        return wrapper

    @classmethod  # 类方法
    def work2(cls, func):
        """
        什么方法适合定义为类方法？
        方法内部执行的时候，要获取类属性，或调用其他类方法，才适合定义成类方法
        如果方法内部不会调用任何的类属性或类方法，那就应该定义成静态方法更合适
        :param func:
        :return:
        """
        def wrapper(*args, **kwargs):
            res = func()
            return res
        return wrapper

@Mytest.work1     # lemon = Mytest.work1(lemon)
def lemon():
    print('------lemon------')