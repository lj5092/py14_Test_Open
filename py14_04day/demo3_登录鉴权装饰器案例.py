#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 9:53 下午
# @Author  : LiangJun
# @Filename    : demo3_登录鉴权装饰器案例.py


users = {'name': 'lj', 'pw': 123, 'islog': False}


def loging():
    name = input("请输入用户名：")
    pw = int(input("请输入密码："))
    if name == users['name'] and pw == users['pw']:
        print("登陆成功")
        # users['islog'] = True
        return True
    else:
        print("账号或密码错误")
        return loging()


def check_login(func):
    def warpper(*args, **kwargs):
        if users['islog']:
            return func()
        else:
            if loging():
                return func()
    return warpper


@check_login
def user():
    """用户信息"""
    print("这个是用户信息")

@check_login
def setpw():
    """修改密码"""
    print("这里是修改密码位置")


if __name__ == '__main__':
    user()
    setpw()