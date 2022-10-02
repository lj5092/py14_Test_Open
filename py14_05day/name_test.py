#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 10:08 下午
# @Author  : LiangJun
# @Filename    : name_test.py


a = [1,2,3,4]
for index in enumerate(a):
    print(index)


def create_name(index, name):
    if index+1<10:
        test_name = name + '_00' + str(index+1)
    return test_name

b = []
for i in range(9):
    b.append(create_name(i, '测试用例1'))
print(b)
